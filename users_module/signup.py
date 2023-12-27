from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton

KV = """
<SignupScreen>:

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
        pos_hint: {'center_x': 0.5, 'center_y': 0.95}
        size_hint: None, None
        size: "1500dp", "400dp"  # Adjust the size as needed
    MDCard:
        size_hint: (None, None)
        size: 370, 700
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        elevation: 2
        padding: 25
        spacing: 20
        orientation: 'vertical'
        radius: [30,]

        MDLabel:
            id: label1
            text: 'Sign Up'
            font_size: 30
            halign: 'center'
            font_name: "Roboto-Bold"
            pos_hint: {'center_x': 0.5, 'center_y': 1}
            height: self.texture_size[1]
            padding:15


        MDTextField:
            id:name
            hint_text: "Enter Full Name"
            helper_text: "Invalid name"
            helper_text_mode: "on_error"
            icon_left: 'account'
            size_hint_x: None
            width: 300
            font_size: 15
            pos_hint: {'center_x':0.5}
            helper_text_color: 1, 0, 0, 1
            font_name: "Roboto-Bold"
        MDTextField:
            id:mobile
            hint_text: "Mobile No"
            helper_text: "Invalid number"
            helper_text_mode: "on_error"
            icon_left: 'cellphone'
            size_hint_x: None
            width: 300
            font_size: 15
            pos_hint: {'center_x':0.5}
            font_name: "Roboto-Bold"

        MDTextField:
            id:email
            hint_text: "Enter Your Email"
            helper_text: "Invalid email"
            helper_text_mode: "on_error"
            icon_left: 'email'
            size_hint_x: None
            width: 300
            font_size: 15
            pos_hint: {'center_x':0.5}
            font_name: "Roboto-Bold"



        MDTextField:
            id:password
            hint_text: "Enter Your Password"
            icon_left: 'lock-outline'
            size_hint_x: None
            width: 300
            helper_text: "Password must greater than 8 characters"
            helper_text_mode: "on_error"
            font_size: 15
            pos_hint: {'center_x':0.5}
            password: True
            font_name: "Roboto-Bold"





        MDTextField:
            id:password2
            hint_text: "Re-Enter Your Password"
            helper_text: "Password does not match"
            helper_text_mode: "on_error"
            icon_left: 'lock-outline'
            size_hint_x: None
            width: 300
            font_size: 14
            pos_hint: {'center_x':0.5}
            password: True
            font_name: "Roboto-Bold"




        BoxLayout:
            spacing: dp(10)
            size_hint_x: None
            height: "60dp"
            width: "60dp"
            pos_hint: {'center_x': 0.25, 'center_y': 0.5}
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            md_bg_color: 0, 0, 0, 1

            MDRectangleFlatButton:
                text: "Back"
                text_color: 1, 1, 1, 1
                pos_hint: {'center_x': 0.3, 'center_y': 0.3}
                md_bg_color: 6/255, 143/255, 236/255, 1
                on_release: app.root.get_screen("MainScreen").manager.current = 'MainScreen'
                font_name: "Roboto-Bold"


            MDRectangleFlatButton:
                text: "Signup"
                text_color: 1, 1, 1, 1  # Black text color
                pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                md_bg_color: 6/255, 143/255, 236/255, 1
                on_release: root.go_to_login()
                font_name: "Roboto-Bold"

    BoxLayout:
        orientation: 'horizontal'
        spacing: 0
        size_hint: None, None
        width: "190dp"
        height: "35dp"
        pos_hint: {'center_x': 0.5, 'center_y': 0.05}

        MDLabel:
            text: "Already have an account?"
            font_size: 16

            theme_text_color: 'Secondary'
            halign: 'center'
            valign: 'center'

        MDFlatButton:
            text: "Sign In"
            theme_text_color: 'Custom'
            text_color: 6/255, 143/255, 236/255, 1
            on_release: root.go_to_login()

"""


class SignupScreen(Screen):
    Builder.load_string(KV)

    def on_pre_enter(self, *args):
        # Adjust the visibility of the background image
        self.ids.bg_image.opacity = 0.3

    def go_to_login(self):
        # Access the app instance and change the current screen to 'LoginScreen'
        self.manager.current = 'LoginScreen'