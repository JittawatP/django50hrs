from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from openpyxl import Workbook,load_workbook
import os
import pandas as pd
from datetime import timedelta
from django.utils.timezone import now
from collections import *
from django.utils import timezone

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
    # EP24 ทำโปรโมชั่น
    new_products = Menu.objects.filter(is_new=True).order_by('-id')
    promotions = Menu.objects.filter(is_promotion=True).order_by('-id')

    current_promotions = Promotion.objects.filter(start_date__lte=now(),end_date__gte=now())
    # End EP24
    if request.method == "POST":
        data = request.POST.copy()
        # EP24 เพิ่ม order_date=timezone.now()  อัพเดทเวลาให้เราตอนเราจะไป plot graph
        order_menu = OrderMenu.objects.create(
            table=table,
            status="pending",
            order_date=timezone.now()
        )
        selected_menu = data.getlist("menu")
        counts = data.getlist("count")

        total_price = 0
        items_data = []

        for i, menu_id in enumerate(selected_menu):
            # EP24 เพิ่ม if และ try except เพื่อตรวจสอบว่า Menu มี ID นี้ไหม
            if not menu_id or not str(menu_id).isdigit():
                continue
            try:
                menu = Menu.objects.get(id=menu_id) 
            except Menu.DoesNotExist:
                continue

            # End EP24
            count = int(counts[i])
            item_total = menu.price_discount * count
            total_price += item_total

            # สร้าง OrderMenuItem สำหรับแต่ละเมนูที่สั่ง
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
    
    context = {"table": table, "all_category": all_category, "all_menu": all_menu,
               "new_products": new_products, "promotions": promotions, "current_promotions": current_promotions}
    
    return render(request, "pos/order-menu.html",context)

# EP24 Graph
def MonthlyOrderSummary(request):
    now = timezone.now()
    start_date = now.replace(day=1)
    end_date = (start_date+timezone.timedelta(days=31)).replace(day=1)

    orders = OrderMenu.objects.filter(order_date__range=(start_date, end_date))

    total_orders = orders.count()   
    total_sales = sum(order.final_price_with_vat for order in orders)

    daily_sales = defaultdict(float)

    for order in orders:
        order_date = order.order_date.date()
        daily_sales[order_date] += order.final_price_with_vat

    labels = list(map(str, daily_sales.keys()))
    data = list(daily_sales.values())

    context = {
        "total_orders": total_orders,
        "total_sales": total_sales,
        "daily_sales_labels": labels,
        "daily_sales_data": data
    }
    return render(request, "pos/monthly-order-summary.html",context)
# End EP24