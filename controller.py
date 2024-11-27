# controller.py
class ProductController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def list_products(self):
        products = self.model.get_all_products()
        self.view.display_product_list(products)

    def show_product_details(self, product_id):
        product = self.model.get_product_by_id(product_id)
        if product:
            self.view.display_product_details(product)
        else:
            self.view.display_message("Product not found!")
