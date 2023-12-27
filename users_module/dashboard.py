from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.screenmanager import SlideTransition
from kivy.metrics import dp
from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton

import lender_module.lender_registration_form

KV = """

<DashScreen>:
    name: 'login'

    Image:
        source: "C:\\P2P-Lending-Mobile-Application\\Images\\LOGO.png"
        pos_hint: {'center_x': 0.2, 'center_y': 0.95}
        size_hint: None, None
        size: "1300dp", "300dp"  # Adjust the size as needed

    MDRaisedButton:
        text: 'BORROWER'
        on_release: root.switch_screen('borrower_registration_forms')
        size_hint: (0.8, 0.1)
        height: dp(350)  # Fixed height
        pos_hint: {'center_x': 0.5, 'center_y': 0.4}
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 1
        md_bg_color: 255/255, 255/255, 255/255, 1
        elevation: 3
        font_name: "Roboto-Bold"

        MDLabel:
            text: 'Register as lender'
            pos_hint: {'center_x': 0.1, 'center_y': 1}
            font_size: 12.5
            theme_text_color: "Custom"
            text_color: 6/255, 143/255, 236/255, 1


    MDRaisedButton:
        text: 'LENDER'
        on_release: root.switch_screen('lender_registration_form')
        size_hint: (0.8, 0.1)
        height: dp(350)  # Fixed height
        pos_hint: {'center_x': 0.5, 'center_y': 0.6}
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 1
        md_bg_color: 255/255, 255/255, 255/255, 1
        elevation: 3
        font_name: "Roboto-Bold"
        MDLabel:
            text: 'Register as lender'
            pos_hint: {'center_x': 0.7, 'center_y': 1}
            font_size: 13
            theme_text_color: "Custom"
            text_color: 6/255, 143/255, 236/255, 1

"""


class DashScreen(Screen):
    Builder.load_string(KV)

    def switch_screen(self, screen_name):
        # Logic for handling the submit button in DashScreen
        print(f"Switching to screen: {screen_name}")

        # Get the screen manager
        sm = self.manager

        # Switch to the specified screen
        sm.transition = SlideTransition(direction='left')
        sm.current = screen_name


