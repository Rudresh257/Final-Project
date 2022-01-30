import product
import auth
import registration
import discount
import history


username = input('Username')
password = input('Password')

is_user_valid = auth.log_in(username,password)
main.initialise_system()

if is_user_valid:
    print("*******RS Restaurant*******")
    print("Menu-Tandoori Chicken,Vegan Burger,Truffle cake")

def get_order():
    MENU = {"Tandoori Chicken","Vegan Burger","Truffle Cake"}
    current_order = []
    while True:
        print("What can I get for you?")
        order = input()
        if order in MENU:
            current_order.append(order)
        else:
            print("I'm sorry, we don't serve that.")
            continue
        if is_order_complete():
            return current_order


def is_order_complete():
    print("Anything else? yes/no")
    choice = input()
    if choice == "no":
        return True
    elif choice == "yes":
        return False
    else:
        raise Exception("invalid input")


def output_order(order_list):
    print("Okay, so you want")
    for order in order_list:
        print(order)
        for prod_info in products.products_details:
                if prod_info['Id'] == product_id:
                    amount = prod_info['Price']
            payment_method = main.choose_payment_method()
            main.pay(amount, payment_method)
            else:
            products.add_new_product()


def main():
    order = get_order()
    output_order(order)
    print("")


if __name__ == "__main__":
    main()
    