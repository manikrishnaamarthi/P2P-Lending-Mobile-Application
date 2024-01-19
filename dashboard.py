from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.screenmanager import SlideTransition
from kivy.metrics import dp
from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton

import lender_registration_form

KV = """

<DashScreen>:
    canvas.before:
        Color:
            rgba:  1, 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size
    Image:
        source: "LOGO.png"
        pos_hint: {'center_x': 0.5, 'center_y': 0.8}
        size_hint: None, None
        size: "170dp", "170dp"

    Widget:
        # Widget to draw a line below the image
        size_hint_y: None
        height: dp(1)
        pos_hint: {'center_x': 0.5, 'center_y': 0.72}
        canvas.before:
            Color:
                rgba: 155/255, 160/255, 162/255, 1  # Change the color to blue (R, G, B, A)
            Line:
                points: [self.x + dp(8), self.y, self.x + self.width - dp(8), self.y]
                width: dp(0.5)  # Decrease the width of the line
    Label:
        text: 'Start your journey with us'
        font_size: 23
        pos_hint: {'center_x': 0.5, 'center_y': 0.66}
        color: 0, 0, 0, 1

    Label:
        text: 'P2P - an RBI registered NBFC '
        font_size: 25
        pos_hint: {'center_x': 0.5, 'center_y': 0.6}
        color: 4/255, 104/255, 153/255, 1
    Label:
        text: 'Platform powered by GTPL'
        font_size: 23
        pos_hint: {'center_x': 0.5, 'center_y': 0.57}
        color: 4/255, 104/255, 153/255, 1




    MDRaisedButton:
        text: 'Continue as Borrower'
        on_release: root.go_to_borrower_landing()
        size_hint: (0.8, 0.07)
        height: dp(150)  # Fixed height
        pos_hint: {'center_x': 0.5, 'center_y': 0.28}
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 1
        md_bg_color: 133/255, 193/255, 233/255, 1       
        font_name: "Roboto-Bold"
        font_size: 23




    MDRaisedButton:
        text: 'Continue as Lender'
        on_release: root.go_to_lender_landing()
        size_hint: (0.8, 0.07)
        height: dp(100)  # Fixed height
        pos_hint: {'center_x': 0.5, 'center_y': 0.15}
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 1
        md_bg_color: 52/255, 152/255, 219/255, 1     
        font_name: "Roboto-Bold"
        font_size: 23


"""


class DashScreen(Screen):
    Builder.load_string(KV)

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)
    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)
    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False
    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'MainScreen'

    def switch_screen(self, screen_name):
        print(f"Switching to screen: {screen_name}")

        # Get the screen manager
        sm = self.manager

        sm.transition = SlideTransition(direction='left')
        sm.current = screen_name


    def go_to_lender_landing(self):
        # Get the screen manager
        sm = self.manager

        # Access the desired screen by name and change the current screen
        sm.current = 'LenderLanding'

    def go_to_borrower_landing(self):
        # Get the screen manager
        sm = self.manager

        # Access the desired screen by name and change the current screen
        sm.current = 'BorrowerLanding'