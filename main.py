from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.app import App
from app.login import LoginPage
from app.daftar import DaftarPage
from app.home import HomePage
from app.selesai import SelesaiPage
from app.antrian import AntrianPage
from app.ambil import AmbilPage
from app.rincian import RincianPage
from app.popup import MyPopup
from app.mutasi import MutasiPage
from app.editpelanggan import EditDataPelangganPage
from app.datapelanggan import DataPelangganPage
from app.addpelanggan import TambahPelangganPage
from app.addpesanan import TambahPesananPage

class MyScreenManager(ScreenManager):
    pass

class MyApp(App):
    def build(self):
        # Memuat file .kv secara manual
        Builder.load_file('screen/login.kv')
        Builder.load_file('screen/daftar.kv')
        Builder.load_file('screen/home.kv')
        Builder.load_file('screen/selesai.kv')
        Builder.load_file('screen/antrian.kv')
        Builder.load_file('screen/ambil.kv')
        Builder.load_file('screen/rincian.kv')
        Builder.load_file('screen/popup.kv')
        Builder.load_file('screen/mutasi.kv')
        Builder.load_file('screen/editpelanggan.kv')
        Builder.load_file('screen/datapelanggan.kv')
        Builder.load_file('screen/addpelanggan.kv')
        Builder.load_file('screen/addpesanan.kv')
        
        sm = MyScreenManager()
        sm.add_widget(LoginPage(name='login'))
        sm.add_widget(DaftarPage(name='daftar'))
        sm.add_widget(HomePage(name='home'))
        sm.add_widget(SelesaiPage(name='selesai'))
        sm.add_widget(AntrianPage(name='antrian'))
        sm.add_widget(AmbilPage(name='ambil'))
        sm.add_widget(RincianPage(name='rincian'))
        sm.add_widget(MyPopup(name='popup'))
        sm.add_widget(MutasiPage(name='mutasi'))
        sm.add_widget(EditDataPelangganPage(name='editpelanggan'))
        sm.add_widget(DataPelangganPage(name='datapelanggan'))
        sm.add_widget(TambahPelangganPage(name='addpelanggan'))
        sm.add_widget(TambahPesananPage(name='addpesanan'))
        
        return sm

if __name__ == '__main__':
    Window.size = (360, 640)
    Window.clearcolor = (1, 1, 1, 1)
    MyApp().run()
    
# if __name__ == '__main__':
#     Window.size = (360, 640)
#     Window.clearcolor = (1, 1, 1, 1)
#     Builder.load_file("style.kv")
#     MainApp().run()