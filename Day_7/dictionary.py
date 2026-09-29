product = {
    "product_name" : "Mouse" ,
    "price" : 21,
    "category" : "accessories",
    "stock" : "first",
    "available" : True
} 

product["price"] = 24
del product["category"]

print(product["product_name"])
print(product["price"])
print(product)

if "stock" not in product:
    print("Stock Missing")
else : print("Stock Available")