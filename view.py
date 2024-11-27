# view.py
class ProductView:
    @staticmethod
    def display_product_list(products):
        print("\nProduct List:")
        for product in products:
            print(f"ID: {product.product_id} | {product.title} - ${product.price:.2f}")

    @staticmethod
    def display_product_details(product):
        print(f"\n--- {product.title} ---")
        print(f"Description: {product.description}")
        print(f"Price: ${product.price:.2f}")

    @staticmethod
    def display_message(message):
        print(message)
