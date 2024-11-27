# model.py
class Product:
    """
    Represents a product in the store.
    Attributes:
        product_id (int): Unique identifier for the product.
        title (str): Name of the product.
        description (str): Brief description of the product.
        price (float): Price of the product.
    """
    def __init__(self, product_id, title, description, price):
        self.product_id = product_id
        self.title = title
        self.description = description
        self.price = price

class ProductModel:
    """
    Manages a collection of products.
    Attributes:
        products (list of Products): List of all available products.
    """
    def __init__(self):
        self.products = [
            Product(1, "STEM Robot Kit", "Build and program your own robot!", 49.99),
            Product(2, "Coding Board Game", "Learn coding basics with fun challenges!", 24.99),
            Product(3, "Electronic Circuit Set", "Create circuits and learn electricity basics.", 29.99)
        ]

    def get_all_products(self):
        """
        Retrieves the list of all products.
        Returns:
            list: List of Product objects.
        """
        return self.products

    def get_product_by_id(self, product_id):
        """
        Retrieves a product by its unique ID.
        Args:
            product_id (int): The ID of the product to retrieve.
        Returns:
            Product: The matching product, or None if not found.
        """
        for product in self.products:
            if product.product_id == product_id:
                return product
        return None
