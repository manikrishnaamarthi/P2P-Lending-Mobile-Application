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
    BoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(10)

        BoxLayout:
            orientation: 'horizontal'
            size_hint_y: None
            height: dp(50)
            spacing: dp(10)

            MDLabel:
                text: 'Kotak Bank'
                theme_text_color: 'Primary'
                font_size: '20sp'
                bold: True

        MDLabel:
            text: 'CARE OF TRUST '
            font_size: '26sp'
            bold: True
            theme_text_color: 'Primary'

        BoxLayout:
            orientation: 'horizontal'
            size_hint_y: None
            height: dp(50)
            spacing: dp(10)
            pos_hint: {'center_x': 0.5}

            MDRectangleFlatButton:
                text: 'Borrower'
                on_release: root.switch_screen('borrower_registration_forms')
                size_hint: (0.5, 1)
                width: dp(50)
                pos_hint: {'center_x': 0.5, 'y': 0.7}
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                md_bg_color: 0, 193/255, 245/255, 1

            MDRectangleFlatButton:
                text: 'Lender'
                on_release: root.switch_screen('lender_registration_form')
                size_hint: (0.5, 1)
                width: dp(50)
                pos_hint: {'center_x': 0.5, 'y': 0.7}
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                md_bg_color: 0, 193/255, 245/255, 1
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

class MyApp(MDApp):
    def build(self):
        # Create the screen manager
        sm = ScreenManager()

        # Add the DashScreen to the screen manager
        dash_screen = DashScreen()
        sm.add_widget(dash_screen)
        sm.add_widget(lender_module.lender_registration_form.LenderScreen)

        # Add additional screens (Borrower and Lender) here if needed

        return sm

if __name__ == "__main__":
    MyApp().run()