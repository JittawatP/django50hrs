from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from openpyxl import Workbook,load_workbook
import os
import pandas as pd


# def Sawatdee(request):
#     return HttpResponse('<h1>สวัสดีจ้า</h1>')

def AllTable(request):
    try:
        all_table = Table.objects.all()
    except Table.DoesNotExist:
        all_table = None

    context = {"all_table": all_table}

    return render(request,"pos/all_table.html", context)


def OrderMenus(request, table_id):
    try:
        table = Table.objects.get(id=table_id)
    except Table.DoesNotExist :
        table = None

    all_category = Category.objects.all()
    all_menu = Menu.objects.all()

    if request.method == "POST":
        data = request.POST.copy()
        order_menu = OrderMenu.objects.create(
            table=table,
            status="pending"
        )
        selected_menu = data.getlist("menu")
        counts = data.getlist("count")

        total_price = 0
        items_data = []

        for i, menu_id in enumerate(selected_menu):
            menu = Menu.objects.get(id=menu_id) 
            count = int(counts[i])

            item_total = menu.price_discount * count

            total_price += item_total

            OrderMenuItem.objects.create(
                order_menu=order_menu,
                menu=menu,
                count=count,
                item_total=item_total
            )
        
        
            items_data.append({
                "รายการอาหาร": menu.name,
                "จำนวน": count,
                "ราคา": item_total,
                "เวลา": order_menu.order_time        
            })

        total_price = float(data.get("total_buyer_price"))
        vat =float(data.get("vat"))
        final_price_with_vat = float(data.get("final_price_with_vat"))
        order_menu.total_buyer_price= total_price
        order_menu.vat = vat
        order_menu.final_price_with_vat= final_price_with_vat

        order_menu.save()

        # บันทึกข้อมูลลง Excel
        data_frame = pd.DataFrame(items_data)
        data_frame["โต๊ะ"] = table.number
        data_frame["ภาษีมูลค่าเพิ่ม"] = vat

        # กำหนดเส้นทางของไฟล์ 
        file_path = "order_menu_data.xlsx"

        try:
            if os.path.exists(file_path):
                with pd.ExcelWriter(file_path, engine="openpyxl", mode="a", if_sheet_exists="overlay") as writer:
                    data_frame.to_excel(writer, sheet_name="Sheet1", index=False, header=False, startrow=writer.sheets["Sheet1"].max_row)
            else:
                data_frame.to_excel(file_path,index=False)        
        except Exception as e:
            context = {
                "error": f"เกิดข้อผิดพลาดที่ไม่คาดคิด: {e}"
            }
            return render(request, "pos/sum-order-menu.html",context)
        
        context = {"order_menu": order_menu}
        return render(request, "pos/sum-order-menu.html",context)
    
    context = {"table": table, "all_category": all_category, "all_menu": all_menu}
    return render(request, "pos/order-menu.html",context)


