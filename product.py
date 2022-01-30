products_details = [
{
    'Name': 'Tandoori Chicken',
    'Price': 240,
    'Quant':'4 Pcs',
    'Id':1,
    'Seller':'RS Restaurant'
},
{
    'Name': 'Vegan Burger',
    'Price': 320,
    'Quant':'1 Pc',
    'Id':2,
    'Seller':'RS Restaurant'
    
},
    {
    'Name': 'Truffle Cake',
    'Price': 900,
    'Quant':'500 gm',
    'Id':3,
    'Seller':'RS Restaurant'
    
}
]

def show_products():
    for product in products_details:
        print('---------------------')
        print(product['Name'])
        print('Buy at ',product['Price'])
        print('Quant',product['Quant'])
        print('Sold by ',product['Seller'])

def add_new_product():
    name = input("Product Name")
    price = float(input("Price in Float"))
    Quantity = input("Quantity")
    id_of_product = input("Id")
    seller = input("Seller")
    products_details.append({
        'Name':name,
        "Price":price,
        "Quant": Quantity,
        "Id":id_of_product,
        "Seller": seller

})
