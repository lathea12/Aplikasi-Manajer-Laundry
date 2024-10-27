from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup
from kivy.uix.label import Label

class LoginPage(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def login(self, username, password):
        # Contoh pengecekan username dan password
        if username == "admin" and password == "123":
            self.manager.current = "home"  # Pindah ke halaman home
        else:
            self.show_popup("Login Gagal", "Username atau Password salah")  # Tampilkan pop-up

    def show_popup(self, title, message):
        # Membuat pop-up
        popup = Popup(title=title, content=Label(text=message), size_hint=(0.8, 0.4))
        popup.open()  # Menampilkan pop-up

    def show_confirmation_popup(self):
        # Membuat konten popup dari file .kv
        self.popup = ()
        self.popup.open()

    def logout(self):
        # Logika untuk logout, misalnya kembali ke layar login
        print("Logged out and returning to login screen")
        # Tambahkan logika kembali ke login screen di sini
        self.popup.dismiss()
        # Ganti layar ke login screen
        self.manager.current = 'login'

    def dismiss_popup(self):
        # Menutup popup
        self.popup.dismiss()