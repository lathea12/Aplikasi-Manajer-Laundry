import pyrebase
from config import get_firebase_config

class Database:
    config = get_firebase_config()
    firebase = pyrebase.initialize_app(config)
    db = firebase.database()

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