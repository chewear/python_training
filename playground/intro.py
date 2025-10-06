# GROUP NUMBER : 1

# python use 4 spaces for indentation
# python is snake case
# use snake case for methods and variables names
# use PascalCase for class names


def greet(first_name : str)->str:
    # this is using an F-string functionality
    print(f"Hello, {first_name}!")
    
    # this is using string concatenation
    print("Hello, " + first_name + "!")
    
"""
    This is a multi-line comment
    This is another line of the multi-line comment
    This is yet another line of the multi-line comment
"""
greet("Alice")

# dictionary - allows you to store a collection of key value pairs

def retrieve_products()->dict:
    return {
        "product" : [
            {
                "product_name" : "apple", "price" : "85"
            },
            {
                "product_name" : "mango", "price" : "60"
            }
        ]
    }
    
products = retrieve_products()
key = "product"

# use get in retrieving data
print(products.get(key,"key_does_not_exists"))

# looping with dict
for p in products.get(key,[]):
    print(f"{p.get('product_name')} \t\t {p.get('price')}")
    
