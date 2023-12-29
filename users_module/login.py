import sqlite3

from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivymd.uix.label import MDLabel
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton, MDFlatButton

KV = """
<LoginScreen>:
    canvas.before:
        Color:
            rgba: 174/255, 214/255, 241/255, 1
        Rectangle:
            size: self.size
            pos: self.pos
    Image:
        source: "C:\\P2P-Lending-Mobile-Application\\Images\\LOGO.png"
        pos_hint: {'center_x': 0.5, 'center_y': 0.85}
        size_hint: None, None
        size: "60dp", "60dp"  # Adjust the size as needed
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
        size_hint: (None, None)
        size: 340, 500
        pos_hint: {'center_x':0.5, 'center_y':0.47}

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

    def go_to_dashboard(self):
        # Get the entered email and password
        entered_email = self.ids.email.text
        entered_password = self.ids.password.text

        if not entered_email or "@" not in entered_email or "." not in entered_email:
            self.show_error_dialog("Invalid email address")
            return

        if not entered_password:
            self.show_error_dialog("Please enter password")
            return

        conn = sqlite3.connect("user_profile.db")
        cursor = conn.cursor()

        cursor.execute('''
            SELECT * FROM users
            WHERE email = ?
        ''', (entered_email,))

        user_data = cursor.fetchone()

        conn.close()

        if user_data:

            if user_data[4] == entered_password:  # Fix index to 4 for the password field

                self.manager.current = 'dashboard'
            else:

                self.show_error_dialog("Incorrect password")
        else:

            self.show_error_dialog("Invalid credentials")

    def show_error_dialog(self, message):

        dialog = MDDialog(
            text=message,
            size_hint=(0.8, 0.3),
            buttons=[
                MDFlatButton(
                    text="OK",
                    on_release=lambda *args: dialog.dismiss()
                )
            ]
        )
        dialog.open()


    def go_to_signup(self):
        self.manager.current = 'SignupScreen'
