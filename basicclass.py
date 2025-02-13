class Product:
    # Attribute
    # name = ชื่อสินค้า
    # quantity = จำนวนสินค้า
    # price = ราคาสินค้าต่อชิ้น

    # Constructor
    def __init__(self, name="water",quantity=3,price=8.50):
        self.name = name
        self.quantity = quantity
        self.price = price

    # Method
    def hello(self):
        print('สวัสดีคุณลูกค้าที่นี้คือร้านขายน้ำ')

# product01 = Product()
# product02 = Product("coffee",2,10)
# print(product01.name)
# print(product01.quantity)
# print(product01.price)
# product01.hello()
# print("=================================")
# print(product02.name)
# print(product02.quantity)
# print(product02.price)
# product02.hello()

# การสืบทอดคลาส  ลูกใช้ของแม่ได้ทุกอย่าง
class Customer(Product):
    # Attribute
    # fullname = ขื้อลูกค้า
    # money = จำนวนเงินที่มีอยู่
    def __init__(self, fullname, money, name, quantity, price):
        super().__init__(name, quantity, price)
        self.fullname = fullname
        self.money = money

    # Method
    def calculate(self):
        self.total = self.quantity * self.price
        self.money = self.money - self.total
        print(f"ลูกค้าเหลือเงิน {self.money} บาท")

customer01 = Customer("สมชาย สบายดี", 500, "Water", 2, 8.5)
print(customer01.fullname)
customer01.calculate()
print("=================================")
customer02 = Customer("Somying", 1000, "Coffee", 3, 15)
print(customer02.fullname)
customer02.calculate()
print("=================================")
customer03 = Customer("Sompong", 10000, "Green Tea", 2 , 100)
print(customer03.fullname)
customer03.calculate()

