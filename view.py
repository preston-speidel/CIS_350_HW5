# view.py
class ProductView:
    """
    Handles the presentation of product information to the user.
    """
    @staticmethod
    def display_product_list(products):
        """
        Displays a list of all products.
        Args:
            products (list): List of Product objects.
        """
        print("\nProduct List:")
        for product in products:
            print(f"ID: {product.product_id} | {product.title} - ${product.price:.2f}")

    @staticmethod
    def display_product_details(product):
        """
        Displays detailed information about a single product.
        Args:
            product (Product): The product to display details for.
        """
        print(f"\n--- {product.title} ---")
        print(f"Description: {product.description}")
        print(f"Price: ${product.price:.2f}")

    @staticmethod
    def display_message(message):
        """
        Displays a message to the user.
        Args:
            message (str): The message to display.
        """
        print(message)
