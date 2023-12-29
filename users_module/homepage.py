# main.py
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton, MDIconButton, MDRectangleFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel
from kivy.properties import ObjectProperty

KV = """
<MainScreen>:
    id: main
    canvas.before:
        Color:
            rgba: 174/255, 214/255, 241/255, 1
        Rectangle:
            size: self.size
            pos: self.pos

    FloatLayout:
        size_hint: None, None
        size: "300dp", "500dp"
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}


        Image:
            source: "C:\\P2P-Lending-Mobile-Application\\Images\\LOGO.png"
            pos_hint: {'center_x': 0.5, 'center_y': 0.85}
            size_hint: None, None
            size: "80dp", "70dp"  # Adjust the size as needed
            allow_stretch: True
            keep_ratio: False
            canvas.before:
                StencilPush
                Ellipse:
                    pos: self.pos
                    size: self.size
            canvas.after:
                StencilPop


        MDCard:
            size_hint: None, None
            size: "300dp", "400dp"
            pos_hint: {'center_x': 0.5, 'center_y': 0.25}
            md_bg_color: 1, 1, 1, 0  # Card background color

            BoxLayout:
                orientation: 'vertical'
                spacing: 20




                MDRaisedButton:
                    size_hint: None, None
                    size: "190dp", "40dp"
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    md_bg_color: 255/255, 255/255, 2555/255, 1

                    on_release: root.sign_up_with_google()

                    BoxLayout:
                        orientation: 'horizontal'
                        spacing: 10

                        Image:
                            source: "C:\\P2P-Lending-Mobile-Application\\Images\\google-logo-9808.png"
                            size_hint: None, None
                            size: "20dp", "25dp"  # Adjust the size as needed

                        MDLabel:
                            text: "Sign In with Google"
                            font_size: 22
                            theme_text_color: 'Custom'
                            text_color: 0, 0, 0, 1
                            pos_hint: {'center_x': 0.8, 'center_y': 0.5}
                            bold: True


                MDRaisedButton:
                    size_hint: None, None
                    size: "200dp", "40dp"
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}                    
                    on_release: root.sign_up_with_google()

                    BoxLayout:
                        orientation: 'horizontal'
                        spacing: 10  # Adjust the spacing as needed

                        Image:
                            source: "C:\P2P-Lending-Mobile-Application\Images\logo-facebookpng-32256.png"
                            size_hint: None, None
                            size: "20dp", "25dp"  # Adjust the size as needed
                            allow_stretch: True
                            keep_ratio: True

                        MDLabel:
                            text: "Sign In with Facebook"
                            font_size: 20
                            theme_text_color: 'Custom'
                            text_color: 1, 1, 1, 1
                            pos_hint: {'center_x': 0.8, 'center_y': 0.5}
                            bold: True


                MDGridLayout:
                    cols: 2
                    spacing: 50
                    pos_hint: {'center_x': 0.70, 'center_y': 0.3}
                    padding: "0dp", "40dp", "0dp", "0dp"

                    MDRaisedButton:
                        id: logout
                        text: "Login"
                        on_release: root.go_to_login()
                        theme_text_color: 'Custom'
                        text_color: 1, 1, 1, 1
                        md_bg_color: 6/255, 143/255, 236/255, 1
                        font_size: 20  # Adjust the initial font size as needed
                        font_name: "Roboto-Bold"

                    MDRaisedButton:
                        id: signout
                        text: "Signup"
                        on_release: root.go_to_signup()
                        pos_hint: {'right': 1, 'y': 0.5}
                        md_bg_color: 6/255, 143/255, 236/255, 1
                        font_size: 20  # Adjust the font size as needed
                        font_name: "Roboto-Bold"

"""


class GoogleSignInButton(MDIconButton):
    pass


class MainScreen(Screen):
    Builder.load_string(KV)

    def go_to_login(self):
        self.manager.current = 'LoginScreen'

    def go_to_signup(self):
        self.manager.current = 'SignupScreen'

    def go_to_dashboard(self):
        self.manager.current = 'dashboard'

