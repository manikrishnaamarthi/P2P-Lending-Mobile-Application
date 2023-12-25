from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDRectangleFlatButton

KV = """
<MainScreen>:
    id: main
    canvas.before:
        Color:
            rgba: 116/255, 187/255, 251/255, 1  # Background color
        Rectangle:
            size: self.size
            pos: self.pos

    FloatLayout:
        size_hint: None, None
        size: "300dp", "500dp"
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}

        Image:

            pos_hint: {'center_x': 0.1, 'center_y': 1}
            size_hint: None, None
            size: "1200dp", "90dp"
            canvas:
                Color:
                    rgba: 116/255, 187/255, 251/255, 0.0  # Adjust the alpha value (0.0 to 1.0) as needed
                Rectangle:
                    pos: self.pos
                    size: self.size

        MDCard:
            size_hint: None, None
            size: "300dp", "400dp"
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            md_bg_color: 1, 1, 1, 0  # Card background color

            BoxLayout:
                orientation: 'vertical'
                spacing: 20

                MDLabel:
                    text: "Welcome"
                    font_size: 40
                    halign: 'center'
                    size_hint_y: None
                    height: self.texture_size[1]
                    theme_text_color: 'Custom'
                    text_color: 1, 1, 1, 1

                MDLabel:
                    text: "P2P Bank"
                    font_size: 50
                    halign: 'center'
                    size_hint_y: None
                    height: self.texture_size[1]
                    theme_text_color: 'Custom'
                    text_color: 1, 1, 1, 1
                    bold:True
                    padding: "0dp", "0dp", "0dp", "50dp"

                MDRaisedButton:
                    text: "Sign Up With Google"
                    padding: 20
                    icon: "Google"
                    md_bg_color: 236/255, 93/255, 93/255, 1
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    bold: True
                    font_size: 20



                MDRaisedButton:
                    text: 'Sign Up With Facebook'
                    icon: "facebook"
                    padding: 20
                    md_bg_color: 2/255, 2/255, 187/255, 1
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    bold: True
                    font_size: 20


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
                        md_bg_color: 2/255, 61/255, 224/255, 1

                    MDRaisedButton:
                        id: signout
                        text: "Signup"                       
                        on_release: root.go_to_signup()
                        pos_hint: {'right': 1, 'y': 0.5}
                        md_bg_color: 2/255, 61/255, 224/255, 1

"""


class MainScreen(Screen):
    Builder.load_string(KV)

    def go_to_login(self):
        # Access the app instance and change the current screen to 'LoginScreen'
        self.manager.current = 'LoginScreen'

    def go_to_signup(self):
        # Access the app instance and change the current screen to 'SigninScreen'
        self.manager.current = 'SignupScreen'