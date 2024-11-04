from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from auth import AuthService
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

auth_service = AuthService()

class RegisterPage(Screen):
    def register(self, email, password):
        success, message = auth_service.register(email, password, role='pengguna')
        if success:
            print(message)  # Feedback saat registrasi berhasil
            App.get_running_app().root.current = 'login'
        else:
            print(message)  # Anda dapat mengganti ini dengan popup atau notifikasi
            self.show_popup('Gagal', 'Daftar Gagal \n Cek Kembali Email & Password Anda!')

    def show_popup(self, title, message):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        label = Label(text=message, halign='center', valign='middle')
        label.bind(size=label.setter('text_size'))  # Agar label bisa membungkus teks dengan benar
        layout.add_widget(label)

        popup = Popup(title=title, content=layout, size_hint=(None, None), size=(400, 200))
        popup.open()