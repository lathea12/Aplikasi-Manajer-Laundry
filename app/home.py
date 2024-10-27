from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup


class HomePage(Screen):
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
        
    def show_popup(self, title, message):
        popup_content = MyPopup()
        popup = Popup(title="Konfirmasi",
                      content=popup_content,
                      size_hint=(None, None), size=(400, 200))
        popup_content.set_popup(popup)
        popup_content.manager = self.manager  # Set manager untuk navigasi
        popup.open()

class MyPopup(Screen):
    def on_yes(self):
        print("Pengguna memilih Ya")
        self.manager.current = "login"  # Pindah ke halaman home
        
        self.popup.dismiss()

    def on_no(self):
        print("Pengguna memilih Tidak")
        self.popup.dismiss()

    def set_popup(self, popup):
        self.popup = popup