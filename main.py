from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.app import App
from app.login import LoginPage
from app.register import RegisterPage
from app.home import HomePage
from app.selesai import SelesaiPage
from app.antrian import AntrianPage
from app.ambil import AmbilPage
from app.rincian import RincianPage
from app.popup import MyPopup
from app.mutasi import MutasiPage
from app.datapelanggan import DataPelanggan
from app.manager import ProductList, EditProduct, AddProduct
from app.addpesanan import AddPesanan, Daftar_Paket
from app.editpelanggan import EditPelanggan
from app.addpelanggan import AddPelanggan
from auth import AuthService
from kivy.uix.screenmanager import ScreenManager

class MyScreenManager(ScreenManager):
    pass

class MyApp(App):
    def build(self):
        # Memuat file .kv secara manual
        Builder.load_file('screen/home.kv')
        Builder.load_file('screen/selesai.kv')
        Builder.load_file('screen/antrian.kv')
        Builder.load_file('screen/ambil.kv')
        Builder.load_file('screen/rincian.kv')
        Builder.load_file('screen/popup.kv')
        Builder.load_file('screen/mutasi.kv')
        Builder.load_file('screen/datapelanggan.kv')
        Builder.load_file('screen/addpelanggan.kv')
        Builder.load_file('screen/addpesanan.kv')
        Builder.load_file('screen/manager.kv')
        Builder.load_file('screen/login.kv')
        Builder.load_file('screen/register.kv')
        # Builder.load_file('auth.kv')
        
        sm = MyScreenManager()
        sm.add_widget(LoginPage(name='login'))
        sm.add_widget(HomePage(name='home'))
        sm.add_widget(DataPelanggan(name='data_pelanggan'))
        sm.add_widget(EditPelanggan(name='edit_pelanggan'))
        sm.add_widget(AddPelanggan(name='add_pelanggan'))
        sm.add_widget(AddPesanan(name='add_pesanan'))
        sm.add_widget(RegisterPage(name='register'))
        sm.add_widget(SelesaiPage(name='selesai'))
        sm.add_widget(AntrianPage(name='antrian'))
        sm.add_widget(AmbilPage(name='ambil'))
        sm.add_widget(RincianPage(name='rincian'))
        sm.add_widget(MyPopup(name='popup'))
        sm.add_widget(MutasiPage(name='mutasi'))
        sm.add_widget(ProductList(name='product_list'))
        sm.add_widget(AddProduct(name='add_product'))
        sm.add_widget(EditProduct(name='edit_product'))
        sm.add_widget(Daftar_Paket(name='daftar_paket'))
        
        return sm

if __name__ == '__main__':
    Window.size = (360, 640)
    Window.clearcolor = (1, 1, 1, 1)
    MyApp().run()