from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from database import Database

class EditPelanggan(Screen):
    name_input = ObjectProperty(None)
    nomer_input = ObjectProperty(None)
    alamat_input = ObjectProperty(None)
    pelanggan_id = StringProperty(None)

    def on_enter(self):
        if hasattr(self, 'pelanggan_data'):
            self.name_input.text = str(self.pelanggan_data.get('nama', ''))
            self.nomer_input.text = str(self.pelanggan_data.get('nomer', ''))
            self.alamat_input.text = str(self.pelanggan_data.get('alamat', ''))

    def set_pelanggan(self, pelanggan_id, pelanggan_data):
        self.pelanggan_id = pelanggan_id
        self.pelanggan_data = pelanggan_data

    def update_pelanggan(self):
        nama = self.name_input.text.strip()
        nomer = self.nomer_input.text.strip()
        alamat = self.alamat_input.text.strip()
        
        if nama and nomer and alamat:
            try:
                pelanggan_data = {
                    'nama': nama,
                    'nomer': int(nomer),
                    'alamat': alamat,
                }
                
                Database.update_pelanggan(self.pelanggan_id, pelanggan_data)
                self.show_popup('Sukses', 'Produk berhasil diupdate!')
                self.manager.current = 'data_pelanggan'
            except Exception as e:
                self.show_popup('Error', f'Terjadi kesalahan: {str(e)}')
        else:
            self.show_popup('Error', 'Semua field harus diisi!')

    def show_popup(self, title, content):
        popup = Popup(
            title=title,
            content=Label(text=content),
            size_hint=(None, None),
            size=(400, 200)
        )
        popup.open()

    def cancel(self):
        self.manager.current = 'data_pelanggan'
