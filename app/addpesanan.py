from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from database import Database

class Pelanggan(BoxLayout):
    def __init__(self, pelanggan_id, pelanggan_data, pilih_callback, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'horizontal'
        self.size_hint_y = None
        self.height = 120
        self.padding = 5
        self.spacing = 10

        # Save pelanggan id and data
        self.pelanggan_id = pelanggan_id
        self.pelanggan_data = pelanggan_data

        # Create info layout
        info_layout = BoxLayout(orientation='vertical', size_hint_x=0.7)
        
        # pelanggan info label
        name = pelanggan_data.get('nama', 'No Name')
        nomer = pelanggan_data.get('nomer')
        alamat = pelanggan_data.get('alamat')
        
        info_label = Label(
            text=f"Nama: {name}\nNomer: {nomer}\nAlamat: {alamat}",
            size_hint_y=None,
            height=100,
            halign='left',
            valign='middle',
            color=(0, 0, 0, 1)  # Warna teks hitam
            
        )
        info_label.bind(size=info_label.setter('text_size'))
        info_layout.add_widget(info_label)

        # Button layout
        button_layout = BoxLayout(orientation='vertical', size_hint_x=0.3, spacing=5)
        
        pilih_btn = Button(text='PILIH', size_hint_y=0.5, background_color=(0.2, 0.6, 0.8, 1), background_normal='')
        pilih_btn.bind(on_press=lambda x: pilih_callback())

        button_layout.add_widget(pilih_btn)

        self.add_widget(info_layout)
        self.add_widget(button_layout)

class AddPesanan(Screen):
    container = ObjectProperty(None)
    
    def on_enter(self):
        self.load_pelanggan()
    
    def load_pelanggan(self):
        self.container.clear_widgets()
        pelanggan = Database.get_all_pelanggan()
        
        if pelanggan:
            for pelanggan_id, pelanggan_data in pelanggan:
                pelanggan_item = Pelanggan(
                    pelanggan_id,
                    pelanggan_data,
                    self.pilih_pelanggan
                )
                self.container.add_widget(pelanggan_item)
        else:
            self.container.add_widget(
                Label(
                    text="Tidak ada pelanggan yang tersedia",
                    size_hint_y=None,
                    height=100
                )
            )
    
    def show_add_pelanggan(self):
        self.manager.current = 'add_pelanggan'

    def pilih_pelanggan(self):
        self.manager.current = 'ambil'