from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel


class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)

        
        label = MDLabel(text="Welcome to the P2P Lending App", halign="center", theme_text_color="Secondary")

        
        button = MDRaisedButton(text="Initiate P2P Transaction", on_press=self.on_p2p_button_press)

        
        self.add_widget(label)
        self.add_widget(button)

    def on_p2p_button_press(self, instance):
        print("P2P Transaction initiated!")
