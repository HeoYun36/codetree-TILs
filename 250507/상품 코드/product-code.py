class Product:
    def __init_(self, name, code):
        self.name = name
        self.code = code

tuple1 = tuple(input().split())

product1 = Product()
product2 = Product()

product1.name = "codetree"
product1.code = 50

product2.name, product2.code = tuple1

print(f"product {product1.code} is {product1.name}")
print(f"product {product2.code} is {product2.name}")