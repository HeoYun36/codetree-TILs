class product:
    def __init__(self, name, code):
        self.name = name
        self.code = code
    
product1 = product("codetree", "50")

product2_name, product2_code = input().split()

product2 = product(product2_name, product2_code)

print(f"product {product1.code} is {product1.name}")
print(f"product {product2.code} is {product2.name}")