# model.py
class Product:
    def __init__(self, product_id, title, description, price):
        self.product_id = product_id
        self.title = title
        self.description = description
        self.price = price

class ProductModel:
    def __init__(self):
        self.products = [
            Product(1, "STEM Robot Kit", "Build and program your own robot!", 49.99),
            Product(2, "Coding Board Game", "Learn coding basics with fun challenges!", 24.99),
            Product(3, "Electronic Circuit Set", "Create circuits and learn electricity basics.", 29.99)
        ]

    def get_all_products(self):
        return self.products

    def get_product_by_id(self, product_id):
        for product in self.products:
            if product.product_id == product_id:
                return product
        return None
