# controller.py
class ProductController:
    """
    Manages interactions between the model and the view.
    """
    def __init__(self, model, view):
        """
        Initializes the controller with the given model and view.
        Args:
            model (ProductModel): The data layer.
            view (ProductView): The presentation layer.
        """
        self.model = model
        self.view = view

    def list_products(self):
        """
        Retrieves the list of all products from the model and passes it to the view for display.
        """
        products = self.model.get_all_products()
        self.view.display_product_list(products)

    def show_product_details(self, product_id):
        """
        Retrieves detailed information about a product by ID and passes it to the view for display.
        Args:
            product_id (int): The ID of the product to display.
        """
        product = self.model.get_product_by_id(product_id)
        if product:
            self.view.display_product_details(product)
        else:
            self.view.display_message("Product not found!")
