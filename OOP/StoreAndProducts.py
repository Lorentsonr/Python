class Store:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_products(self, new_product):
        self.products.append(new_product)
        return self

    def sell_products(self, id):
        sold = self.products[id]
        self.products.pop(id)
        sold.print_info()
        return self

    def inflation(self, percent_increasls
    e):
        for product in self.products:
            product.update_price(percent_increase, True)
        return self

    def set_clearance(self, category, percent_discount):
        for product in self.products:
            if product.category == category:
                product.update_price(percent_discount, False)
        return self

    def view_products(self):
        for i in range (len(self.products)):
            self.products[i].print_info()
        return self

class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def update_price(self, percentage_change, is_increased):
        if is_increased == True:
            self.price *= percentage_change + 1
        else:
            self.price *= 1 - percentage_change
        return self

    def print_info(self):
        print(f"{self.name}  {self.category} $ {self.price}")
        return self


store1=Store("Grocery")

prod1=Product("Lettuce", 5, "food")
prod2=Product("Bread", 7, "food")
prod3=Product("Shirt", 30, "clothes")
prod4=Product("Shoes", 60, "clothes")
prod5=Product("Camera", 20, "tech")

store1.add_products(prod1).add_products(prod2).add_products(prod3).add_products(prod4).add_products(prod5)
store1.view_products()
print()
store1.sell_products(1)
print()
store1.view_products()
print()
store1.inflation(.05).view_products()
print()
store1.set_clearance("clothes", .5).view_products()
print()
print()
prod1.update_price(1, True).print_info()
print()
print()
store1.view_products()