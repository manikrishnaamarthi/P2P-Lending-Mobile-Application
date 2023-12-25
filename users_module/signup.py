from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDRectangleFlatButton

KV = """
<SignupScreen>:
    MDCard:
        size_hint: (None, None)
        size: 350, 700
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        elevation: 2
        padding: 25
        spacing: 20
        orientation: 'vertical'
        radius: [10,]

        MDLabel:
            id: label1
            text: 'Sign Up'
            font_size: 40
            halign: 'center'
            size_hint_y: None
            height: self.texture_size[1]
            padding:15

        MDTextField:
            id:name
            hint_text: "Enter Full Name"
            helper_text: "Invalid name"
            helper_text_mode: "on_error"
            icon_right: 'account'
            size_hint_x: None
            width: 300
            font_size: 18
            pos_hint: {'center_x':0.5}
            helper_text_color: 1, 0, 0, 1

        MDTextField:
            id:mobile
            hint_text: "Mobile No"
            helper_text: "Invalid number"
            helper_text_mode: "on_error"
            icon_right: 'cellphone'
            size_hint_x: None
            width: 300
            font_size: 18
            pos_hint: {'center_x':0.5}

        MDTextField:
            id:email
            hint_text: "Enter Your Email"
            helper_text: "Invalid email"
            helper_text_mode: "on_error"
            icon_right: 'email'
            size_hint_x: None
            width: 300
            font_size: 18
            pos_hint: {'center_x':0.5}


        MDTextField:
            id:password
            hint_text: "Enter Your Password"
            icon_right: 'eye-off'
            size_hint_x: None
            width: 300
            helper_text: "Password must greater than 8 characters"
            helper_text_mode: "on_error"
            font_size: 18
            pos_hint: {'center_x':0.5}
            password: True

        MDTextField:
            id:password2
            hint_text: "Re-Enter Your Password"
            helper_text: "Password does not match"
            helper_text_mode: "on_error"
            icon_right: 'eye-off'
            size_hint_x: None
            width: 300
            font_size: 18
            pos_hint: {'center_x':0.5}
            password: True

        MDBoxLayout:
            orientation: 'horizontal'
            spacing: 60
            size_hint: None, None
            height: dp(48)  # Adjust the height as needed
            pos_hint: {'center_x': 0.36, 'center_y': 0.64}

            MDRaisedButton:
                padding_left: 10
                spacing: 150
                text: "Back"
                size_hint_x: None
                on_release: app.root.get_screen("MainScreen").manager.current = 'MainScreen'


            MDRaisedButton:
                text: "signup"
                size_hint_x: None
                on_release: root.go_to_login()


"""


class SignupScreen(Screen):
    Builder.load_string(KV)

    def go_to_login(self):
        # Access the app instance and change the current screen to 'LoginScreen'
        self.manager.current = 'LoginScreen'

