from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from database import Database

class Pelanggan(BoxLayout):
    def __init__(self, pelanggan_id, pelanggan_data, delete_callback, edit_callback, **kwargs):
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
        
        edit_btn = Button(text='EDIT', size_hint_y=0.5, background_color=(0.2, 0.6, 0.8, 1))
        edit_btn.bind(on_press=lambda x: edit_callback(pelanggan_id, pelanggan_data))
        
        delete_btn = Button(text='HAPUS', size_hint_y=0.5, background_color=(0.9, 0.3, 0.3, 1))
        delete_btn.bind(on_press=lambda x: delete_callback(pelanggan_id))

        button_layout.add_widget(edit_btn)
        button_layout.add_widget(delete_btn)

        self.add_widget(info_layout)
        self.add_widget(button_layout)

class DataPelanggan(Screen):
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
                    self.delete_pelanggan,
                    self.edit_pelanggan
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

    def edit_pelanggan(self, pelanggan_id, pelanggan_data):
        edit_screen = self.manager.get_screen('edit_pelanggan')
        edit_screen.set_pelanggan(pelanggan_id, pelanggan_data)
        self.manager.current = 'edit_pelanggan'

    def delete_pelanggan(self, pelanggan_id):
        confirm_popup = Popup(
            title='Konfirmasi',
            size_hint=(None, None),
            size=(300, 200)
        )
        
        content = BoxLayout(orientation='vertical', padding=10, spacing=10)
        content.add_widget(Label(text='Apakah Anda yakin ingin\nmenghapus pelanggan ini?'))
        
        buttons = BoxLayout(size_hint_y=None, height=40, spacing=10)
        
        cancel_btn = Button(text='Batal')
        cancel_btn.bind(on_press=confirm_popup.dismiss)
        
        def confirm_delete(instance):
            try:
                Database.delete_pelanggan(pelanggan_id)
                self.load_pelanggan()
                confirm_popup.dismiss()
                self.show_popup('Sukses', 'Pelanggan berhasil dihapus!')
            except Exception as e:
                confirm_popup.dismiss()
                self.show_popup('Error', f'Gagal menghapus pelanggan: {str(e)}')
        
        confirm_btn = Button(text='Hapus', background_color=(0.9, 0.3, 0.3, 1))
        confirm_btn.bind(on_press=confirm_delete)
        
        buttons.add_widget(cancel_btn)
        buttons.add_widget(confirm_btn)
        
        content.add_widget(buttons)
        confirm_popup.content = content
        confirm_popup.open()

    def show_popup(self, title, content):
        popup = Popup(
            title=title,
            content=Label(text=content),
            size_hint=(None, None),
            size=(400, 200)
        )
        popup.open()