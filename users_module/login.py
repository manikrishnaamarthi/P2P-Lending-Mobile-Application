from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDRectangleFlatButton

KV = """
<LoginScreen>:
    MDCard:
        size_hint: (None, None)
        size: 350, 500
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        elevation: 2
        padding:25
        spacing: 20
        radius: [15,]
        orientation: 'vertical'

        MDLabel:
            id: label1
            text: 'Login Form'
            font_size: 40
            halign: 'center'
            size_hint_y: None
            height: self.texture_size[1]
            padding:15
            bold: True

        MDTextField:
            id: email
            hint_text: "Email"
            helper_text_mode: "on_focus"
            icon_right: "account"

        MDTextField:
            id: password
            hint_text: "Password"
            helper_text: "Forgot your password?"
            helper_text_mode: "on_focus"
            icon_right: "key"
            password: True
            spacing: 20

        MDBoxLayout:
            orientation: 'horizontal'
            spacing: 60
            size_hint: None, None
            pos_hint: {'center_x': 0.36, 'center_y': 0.64}


            MDRaisedButton:
                text: "Back"
                size_hint_x: None

                on_release: app.root.current = "MainScreen"


            MDRaisedButton:
                text: "Login"
                size_hint_x: None
                on_release: root.go_to_dashboard()

        MDLabel:
            id: error_label
            text: ""

"""


class LoginScreen(Screen):
    Builder.load_string(KV)

    def go_to_dashboard(self):
        # Access the app instance and change the current screen to 'dashboard'
        self.manager.current = 'dashboard'