import pyrebase
from config import get_firebase_config

class Database:
    config = get_firebase_config()
    firebase = pyrebase.initialize_app(config)
    db = firebase.database()

    # DATABASE PELANGGAN
    # DATABASE PELANGGAN
    # DATABASE PELANGGAN
    
    @staticmethod
    def get_all_pelanggan():
        try:
            pelanggan = Database.db.child("pelanggan").get()
            if pelanggan.each():
                return [(pelanggan.key(), pelanggan.val()) for pelanggan in pelanggan.each()]
            return []
        except Exception as e:
            print(f"Error getting pelanggan: {e}")
            return []

    @staticmethod
    def add_pelanggan(pelanggan_data):
        try:
            return Database.db.child("pelanggan").push(pelanggan_data)
        except Exception as e:
            print(f"Error adding pelanggan: {e}")
            raise e

    @staticmethod
    def update_pelanggan(pelanggan_id, pelanggan_data):
        try:
            return Database.db.child("pelanggan").child(pelanggan_id).update(pelanggan_data)
        except Exception as e:
            print(f"Error updating pelanggan: {e}")
            raise e

    @staticmethod
    def delete_pelanggan(pelanggan_id):
        try:
            return Database.db.child("pelanggan").child(pelanggan_id).remove()
        except Exception as e:
            print(f"Error deleting pelanggan: {e}")
            raise e

    # DATABASE PRODUK ATAU PAKET
    # DATABASE PRODUK ATAU PAKET
    # DATABASE PRODUK ATAU PAKET 

    # @staticmethod
    # def get_all_products():
    #     try:
    #         products = Database.db.child("products").get()
    #         if products.each():
    #             return [(product.key(), product.val()) for product in products.each()]
    #         return []
    #     except Exception as e:
    #         print(f"Error getting products: {e}")
    #         return []

    # @staticmethod
    # def add_product(product_data):
    #     try:
    #         return Database.db.child("products").push(product_data)
    #     except Exception as e:
    #         print(f"Error adding product: {e}")
    #         raise e

    # @staticmethod
    # def update_product(product_id, product_data):
    #     try:
    #         return Database.db.child("products").child(product_id).update(product_data)
    #     except Exception as e:
    #         print(f"Error updating product: {e}")
    #         raise e

    # @staticmethod
    # def delete_product(product_id):
    #     try:
    #         return Database.db.child("products").child(product_id).remove()
    #     except Exception as e:
    #         print(f"Error deleting product: {e}")
    #         raise e