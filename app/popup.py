from kivy.uix.screenmanager import Screen

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
