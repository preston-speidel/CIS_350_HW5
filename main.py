# main.py
from model import ProductModel
from view import ProductView
from controller import ProductController

def main():
    model = ProductModel()
    view = ProductView()
    controller = ProductController(model, view)

    while True:
        print("\n1. View Product List")
        print("2. View Product Details")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            controller.list_products()
        elif choice == "2":
            try:
                product_id = int(input("Enter Product ID: "))
                controller.show_product_details(product_id)
            except ValueError:
                print("Invalid ID. Please enter a number.")
        elif choice == "3":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()
