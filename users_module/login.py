from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton
import sqlite3
from borrower_module import borrower_registration_forms
from lender_module import lender_registration_form

kv = '''
<MainScreen>:

    FloatLayout:

        MDCard:

            size_hint: None, None
            size: "300dp", "600dp"
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            BoxLayout:
                orientation: 'vertical'


                MDLabel:
                    text: "It’s an exciting time to be in finance, and more so at Kotak.The explosion of digital media has changed the way customers live and bank.We’re not just adapting to this change,but anticipating it and staying one step ahead.It all begins with our people, and with a work culture designed for new age banking."

                MDGridLayout:
                    cols: 2
                    spacing: 60
                    pos_hint: {'center_x': 0.7, 'center_y': 0.2}

                    MDRaisedButton:
                        id: logout
                        text: "Login"
                        on_release: app.root.current = "login"
                        on_release: app.root.get_screen("main").change_text()

                    MDRaisedButton:
                        id: signout
                        text: "Signup"
                        on_release: app.root.current = "signup"
                        on_release: app.root.get_screen("main").change_text1()
                        pos_hint: {'right': 1, 'y': 0.5}




<SignupScreen>:
    MDCard:
        size_hint: (None, None)
        size: 340, 700
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
            helper_text: "Password must greater than 6 characters"
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
                on_release: app.root.current = "main"

            MDRaisedButton:
                text: "signup"
                size_hint_x: None
                on_release: app.root.get_screen("signup").login(name.text,mobile.text,email.text, password.text, password2.text)


<DScreen>:
    id: signout
    BoxLayout:
        orientation: "vertical"
        spacing: "10dp"
        padding: "10dp"

        MDRaisedButton:
            id: signout
            text: "SignOut"
            on_release: app.root.current = "main"
            pos_hint: {'center_x':0.9, 'center_y':0.1}
            on_release: app.root.get_screen("success").change_text3()

        MDLabel:
            text: ''

        MDGridLayout:
            size_hint: (None, None)
            size: 300, 600
            cols: 2
            spacing: 20
            padding: 50
            pos_hint: {'center_x': 0.4, 'center_y': 0.5}

            MDRaisedButton:
                id: borrower
                text: "Borrower Registration"
                on_release:app.on_next_button_click()

            MDRaisedButton:
                id: lender
                text: "Lender Registration"

<LoginScreen>:
    MDCard:
        size_hint: (None, None)
        size: 300, 450
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


            MDRaisedButton:
                text: "Back"
                size_hint_x: None
                on_release: app.root.current = "main"
                on_release: app.root.get_screen("login").change_text3()

            MDRaisedButton:
                text: "Login"
                size_hint_x: None
                on_release: app.root.get_screen("login").on_login(email.text, password.text)

        MDLabel:
            id: error_label
            text: ""
'''

Builder.load_string(kv)


class MainScreen(Screen):

    def change_text(self):
        # Access the label in another screen and update its text
        login_status_label = MDApp.get_running_app().root.get_screen('success')
        login_status_label.ids.signout.text = "Logout"

    def change_text1(self):
        # Access the label in another screen and update its text
        login_status_label = MDApp.get_running_app().root.get_screen('success')
        login_status_label.ids.signout.text = "Signout"


class SignupScreen(Screen):

    def show_alert_dialog(self, alert_text):
        if not hasattr(self, 'dialog') or not self.dialog:
            self.dialog = MDDialog(
                text=alert_text,
                buttons=[
                    MDFlatButton(
                        text="OK", on_release=self.close_dialog
                    ),
                ],
            )

        self.dialog.text = alert_text
        self.dialog.open()

    # Click Cancel Button
    def close_dialog(self, obj):
        # Close alert box
        self.dialog.dismiss()

    def login(self, name, mobile, email, password, password2):

        conn = sqlite3.connect('kivymd.db')
        cursor = conn.cursor()

        # Create a table if it doesn't exist
        cursor.execute(''' CREATE TABLE IF NOT EXISTS signup (
                                    name TEXT,
                                    mobile INTEGER,
                                    email TEXT,
                                    password TEXT,
                                    customer_id INTEGER PRIME NUMBER NOT NULL)
                            ''')

        cursor.execute('select * from signup')

        p = cursor.fetchall()

        email_list = []
        id_list = []
        for i in p:
            email_list.append(i[2])
            id_list.append(i[4])

        if len(id_list) == 0:
            a = 1000
        else:
            a = id_list[-1]

        if name == '' or mobile == '' or email == '' or password == '' or password2 == '':
            self.show_alert_dialog("You Must Enter All Fields")

        if name.isdigit() or len(name) < 3:
            self.ids.name.error = True

        if not mobile.isdigit() or len(mobile) != 10:
            self.ids.mobile.error = True

        if not email.endswith("@gmail.com"):
            self.ids.email.error = True

        if len(password) < 8:
            self.ids.password.error = True

        if password != password2:
            self.ids.password2.error = True

        elif email in email_list:
            self.show_alert_dialog("email already exist")

        else:

            if (
                    password == password2
                    and email not in email_list
                    and not name.isdigit()
                    and len(name) >= 3
                    and email.endswith("@gmail.com")
                    and len(mobile) == 10
                    and mobile.isdigit()
                    and len(password) >= 8
            ):
                try:
                    a = a + 1
                    print(a)
                    self.ids.name.error = False
                    self.ids.mobile.error = False
                    self.ids.email.error = False
                    self.ids.password.error = False
                    self.ids.password2.error = False

                    cursor.execute(
                        "INSERT INTO signup (name, mobile, email, password, customer_id) VALUES (?,?,?, ?, ?)",
                        (name, mobile, email, password, a))

                    self.show_alert_dialog(f'{email} is successfully signed up')
                    self.manager.current = "login"

                except sqlite3.Error as err:
                    self.show_alert_dialog(f"Error signing up: {err}")

        conn.commit()
        conn.close()


class DScreen(Screen):

    def change_text3(self):
        # Access the label in another screen and update its text
        login_status_label = MDApp.get_running_app().root.get_screen('login')
        login_status_label.ids.email.text = ""
        login_status_label.ids.password.text = ""
        login_status_label1 = MDApp.get_running_app().root.get_screen('signup')
        login_status_label1.ids.name.text = ""
        login_status_label1.ids.mobile.text = ""
        login_status_label1.ids.email.text = ""
        login_status_label1.ids.password.text = ""
        login_status_label1.ids.password2.text = ""


class LoginScreen(Screen):

    def change_text3(self):
        # Access the label in another screen and update its text
        login_status_label1 = MDApp.get_running_app().root.get_screen('signup')
        login_status_label1.ids.name.text = ""
        login_status_label1.ids.mobile.text = ""
        login_status_label1.ids.email.text = ""
        login_status_label1.ids.password.text = ""
        login_status_label1.ids.password2.text = ""

    def show_alert_dialog(self, alert_text):
        if not hasattr(self, 'dialog') or not self.dialog:
            self.dialog = MDDialog(
                text=alert_text,
                buttons=[
                    MDFlatButton(
                        text="OK", on_release=self.close_dialog
                    ),
                ],
            )
        self.dialog.text = alert_text
        self.dialog.open()

    def close_dialog(self, obj):
        # Close alert box
        self.dialog.dismiss()

    def on_login(self, email, password):
        # Add your authentication logic here
        conn = sqlite3.connect('kivymd.db')
        cursor = conn.cursor()
        cursor.execute('select * from signup')

        p = cursor.fetchall()

        email_list = []
        password_list = []
        for i in p:
            email_list.append(i[2])
            password_list.append(i[3])

        if email == '' and password == '':
            self.show_alert_dialog(f'Enter All Fields')

        elif email in email_list and password in password_list:
            for i in p:
                if email == i[2] and password == i[3]:
                    self.manager.current = "success"

        else:
            self.show_alert_dialog(f'Invalid Credits')

        conn.commit()
        conn.close()


class LoginApp(MDApp):
    def build(self):
        sm = ScreenManager()
        self.theme_cls.theme_style = 'Light'
        self.theme_cls.primary_palette = "Blue"

        # Add screens
        sm.add_widget(MainScreen(name="main"))
        sm.add_widget(LoginScreen(name="login"))
        sm.add_widget(SignupScreen(name="signup"))
        sm.add_widget(DScreen(name="success"))

        return sm

    def on_stop(self):
        if hasattr(self.root.get_screen('signup'), 'connection') and self.root.get_screen(
                'signup').connection.is_connected():
            self.root.get_screen('signup').cursor.close()
            self.root.get_screen('signup').connection.close()


if __name__ == "__main__":
    LoginApp().run()
