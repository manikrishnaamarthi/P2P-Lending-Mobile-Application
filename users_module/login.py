from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDRectangleFlatButton

KV = """
<LoginScreen>:
    Image:
        id: bg_image
        source: "C:\P2P-Lending-Mobile-Application\Images\P2P-Lending.png"
        allow_stretch: True
        keep_ratio: False
        size_hint: None, None
        size: self.parent.size if self.parent else (0, 0)
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    Image:
        source: "C:\\P2P-Lending-Mobile-Application\\Images\\LOGO.png"
        pos_hint: {'center_x': 0.5, 'center_y': 0.85}
        size_hint: None, None
        size: "1500dp", "400dp"  # Adjust the size as needed
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
            font_size: 30
            halign: 'center'
            size_hint_y: None
            height: self.texture_size[1]
            padding:15
            bold: True

        MDTextField:
            id: email
            hint_text: "Email/Mobile Number"
            helper_text_mode: "on_focus"
            icon_right: "account"
            font_name: "Roboto-Bold"

        MDTextField:
            id: password
            hint_text: "Password"
            helper_text: "Forgot your password?"
            helper_text_mode: "on_focus"
            icon_right: "key"
            password: True
            spacing: 20
            font_name: "Roboto-Bold"

        MDBoxLayout:
            orientation: 'horizontal'
            spacing: 20
            size_hint: None, None
            pos_hint: {'center_x': 0.3, 'center_y': 0.5}


            MDRaisedButton:
                text: "Back"
                size_hint_x: None
                font_name: "Roboto-Bold"
                on_release: app.root.current = "MainScreen"


            MDRaisedButton:
                text: "Login"
                size_hint_x: None
                on_release: root.go_to_dashboard()
                font_name: "Roboto-Bold"

        MDLabel:
            id: error_label
            text: ""

    BoxLayout:
        orientation: 'horizontal'
        spacing: 0
        size_hint: None, None
        width: "190dp"
        height: "35dp"
        pos_hint: {'center_x': 0.5, 'center_y': 0.12}

        MDLabel:
            text: "Don't have an account?"
            font_size: 16

            theme_text_color: 'Secondary'
            halign: 'center'
            valign: 'center'

        MDFlatButton:
            text: "Sign Up"
            theme_text_color: 'Custom'
            text_color: 6/255, 143/255, 236/255, 1
            on_release: root.go_to_signup()

"""


class LoginScreen(Screen):
    Builder.load_string(KV)

    def on_pre_enter(self, *args):
        # Adjust the visibility of the background image
        self.ids.bg_image.opacity = 0.3

    def go_to_dashboard(self):
        # Access the app instance and change the current screen to 'dashboard'
        self.manager.current = 'dashboard'

    def go_to_signup(self):
        # Access the app instance and change the current screen to 'LoginScreen'
        self.manager.current = 'SignupScreen'