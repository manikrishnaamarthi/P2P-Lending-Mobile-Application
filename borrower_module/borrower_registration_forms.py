from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivymd.uix.button import MDRectangleFlatButton
from kivy.metrics import dp
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.pickers import MDDatePicker
from kivy.core.window import Window
from kivymd.app import MDApp
Window.size = (350, 600)
Borrower = '''
<BorrowerScreen>:
    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(10)
        padding: dp(10)
        size_hint_y: None
        height: self.minimum_height
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        size_hint_x: None
        width: 300
        MDCard:
            orientation: "vertical"
            size_hint: None, None
            size: "280dp", "480dp"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}

            MDLabel:
                text: 'Borrower Registration Form'
                font_size: 25
                halign: 'center'
                bold: True

            MDTextField:
                id: username
                hint_text: 'Enter full name'
                multiline: False
                helper_text: 'Enter valid name'
                helper_text_mode: 'on_focus'
                size_hint_y: None
                height: self.minimum_height
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x: None
                width: 300
                font_name: "Roboto-Bold"

            MDTextField:
                id: email
                hint_text: 'Enter email'
                multiline: False
                helper_text: 'Enter valid email'
                helper_text_mode: 'on_focus'
                size_hint_y: None
                height: self.minimum_height
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x: None
                width: 300
                font_name: "Roboto-Bold"

            MDTextField:
                id: gender_field
                multiline: False
                hint_text: "Select gender"
                on_focus: if self.focus: app.show_gender_menu()
                height: self.minimum_height
                readonly: True
                width: 300
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                theme_text_color: "Custom"
                hint_text_color: (0, 0, 0, 1)  # Black hint text color
                text_color: (0, 0, 0, 1)  # Black text color
                helper_text: "Select gender"
                size_hint_x: None
                size_hint_y: None
                helper_text_mode: "on_focus"
                font_name: "Roboto-Bold"

            MDTextField:
                id: date_textfield
                hint_text: "Select Date"
                icon_right: "calendar"
                readonly: True
                width: 300
                size_hint_x: None
                size_hint_y: None
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                on_focus: if self.focus: app.show_date_picker()
                font_name: "Roboto-Bold"

            MDTextField:
                id: mobile_no
                hint_text: 'Enter mobile no'
                multiline: False
                helper_text: 'Enter valid mobile no'
                helper_text_mode: 'on_focus'
                size_hint_y: None
                height: self.minimum_height
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x: None
                width: 300
                font_name: "Roboto-Bold"

            BoxLayout:
                spacing: dp(10)
                size_hint_x: None
                height: "60dp"
                width: "60dp"
                pos_hint: {'center_x': 0.4, 'center_y': 0.6}
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                md_bg_color: 0, 0, 0, 1

                MDRectangleFlatButton:
                    text: 'Next'
                    text_color: 0, 0, 0, 1  # Black text color
                    pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    on_release: app.root.current = 'BorrowerScreen1'

<BorrowerScreen1>:
    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(10)
        padding: dp(10)
        size_hint_y: None
        height: self.minimum_height
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        size_hint_x: None
        width: 300
        MDCard:
            orientation: "vertical"
            size_hint: None, None
            size: "280dp", "480dp"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}

            MDLabel:
                text: 'Borrower Registration Form'
                font_size: 25
                halign: 'center'
                bold: True

            MDTextField:
                id: alternate_mobile_number
                hint_text: "Enter alternate mobile number"
                pos_hint: {'center_x': 0.5, 'center_y': 0.6}
                size_hint_x: None
                width: 300
                theme_text_color: "Custom"
                hint_text_color: (0, 0, 0, 1)  # Black hint text color
                text_color: (0, 0, 0, 1)  # Black text color
                helper_text: "Enter valid number"
                helper_text_mode: "on_focus"
                font_name: "Roboto-Bold"

            MDTextField:
                id: alternate_email
                hint_text: 'Enter alternate email'
                multiline: False
                helper_text: 'Enter valid email'
                helper_text_mode: 'on_focus'
                size_hint_y: None
                height: self.minimum_height
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x: None
                width: 300

            MDRectangleFlatButton:
                text: 'Upload your Image'
                text_color: 0, 0, 0, 1  # Black text color
                pos_hint: {'center_x': 0.5, 'center_y': 0.37}
                md_bg_color: 0.031, 0.463, 0.91, 1
                on_release: app.file_manager_open()
                size_hint: (0.1, 0.01)
                font_size: "12sp"
                size_hint_y: None
                size_hint_x: None

            BoxLayout:
                spacing: dp(10)
                size_hint_x: None
                height: "60dp"
                width: "60dp"
                pos_hint: {'center_x': 0.4, 'center_y': 0.6}
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                md_bg_color: 0, 0, 0, 1
                MDRectangleFlatButton:
                    text: 'Back'
                    text_color: 0, 0, 0, 1  # Black text color
                    pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    on_release: app.root.current = 'borrower_registration_forms'

                MDRectangleFlatButton:
                    text: 'Next'
                    text_color: 0, 0, 0, 1  # Black text color
                    pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    on_release: app.root.current = 'BorrowerScreen2'
<BorrowerScreen2>:
    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(10)
        padding: dp(10)
        size_hint_y: None
        height: self.minimum_height
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        size_hint_x: None
        width: 300
        MDCard:
            orientation: "vertical"
            size_hint: None, None
            size: "280dp", "480dp"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}

            MDLabel:
                text: 'Borrower Registration Form'
                font_size: 25
                halign: 'center'
                bold: True
            MDTextField:
                id: aadhar_number
                hint_text: 'Enter aadhar number '
                multiline: False
                helper_text: 'Enter valid number'
                helper_text_mode: 'on_focus'
                size_hint_y: None
                height: self.minimum_height
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x: None
                width: 300

            MDRectangleFlatButton:
                text: 'Upload aadhar card '
                text_color: 0, 0, 0, 1  # Black text color
                pos_hint: {'center_x': 0.5, 'center_y': 0.37}
                md_bg_color: 0.031, 0.463, 0.91, 1
                on_release: app.file_manager_open()
                size_hint: (0.1, 0.01)
                font_size: "12sp"
                size_hint_y: None
                size_hint_x: None

            MDTextField:
                id: pan_number
                hint_text: 'Enter pan number '
                multiline: False
                helper_text: 'Enter valid number'
                helper_text_mode: 'on_focus'
                size_hint_y: None
                height: self.minimum_height
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x: None
                width: 300

            MDRectangleFlatButton:
                text: 'Upload pancard '
                text_color: 0, 0, 0, 1  # Black text color
                pos_hint: {'center_x': 0.5, 'center_y': 0.37}
                md_bg_color: 0.031, 0.463, 0.91, 1
                on_release: app.file_manager_open()
                size_hint: (0.1, 0.01)
                font_size: "12sp"
                size_hint_y: None
                size_hint_x: None

            BoxLayout:
                spacing: dp(10)
                size_hint_x: None
                height: "60dp"
                width: "60dp"
                pos_hint: {'center_x': 0.4, 'center_y': 0.6}
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                md_bg_color: 0, 0, 0, 1
                MDRectangleFlatButton:
                    text: 'Back'
                    text_color: 0, 0, 0, 1  # Black text color
                    pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    on_release: app.root.current = 'BorrowerScreen1'
                MDRectangleFlatButton:
                    text: 'Next'
                    text_color: 0, 0, 0, 1  # Black text color
                    pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    on_release: app.root.current = 'BorrowerScreen3'
<BorrowerScreen3>:
    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(10)
        padding: dp(10)
        size_hint_y: None
        height: self.minimum_height
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        size_hint_x: None
        width: 300
        MDCard:
            orientation: "vertical"
            size_hint: None, None
            size: "280dp", "480dp"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}

            MDLabel:
                text: 'Borrower Registration Form'
                font_size: 25
                halign: 'center'
                bold: True
            MDLabel:
                text: 'Address'
                font_size: 25
                halign: 'center'
                bold: True

            MDTextField:
                id: street_address
                hint_text: 'Enter street address '
                multiline: False
                helper_text: 'Enter valid address'
                helper_text_mode: 'on_focus'
                size_hint_y: None
                height: self.minimum_height
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x: None
                width: 300

            MDTextField:
                id: city
                hint_text: 'Enter city here'
                multiline: False
                helper_text_mode: 'on_focus'
                size_hint_y: None
                height: self.minimum_height
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x: None
                width: 300

            MDTextField:
                id: Zip_code
                hint_text: 'Enter postal/zipcode '
                multiline: False
                helper_text_mode: 'on_focus'
                size_hint_y: None
                height: self.minimum_height
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x: None
                width: 300

            MDTextField:
                id: state
                hint_text: 'Enter state here'
                multiline: False
                helper_text_mode: 'on_focus'
                size_hint_y: None
                height: self.minimum_height
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x: None
                width: 300

            MDTextField:
                id: country
                hint_text: 'Enter country here'
                multiline: False
                helper_text_mode: 'on_focus'
                size_hint_y: None
                height: self.minimum_height
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x: None
                width: 300

            BoxLayout:
                spacing: dp(10)
                size_hint_x: None
                height: "60dp"
                width: "60dp"
                pos_hint: {'center_x': 0.4, 'center_y': 0.6}
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                md_bg_color: 0, 0, 0, 1
                MDRectangleFlatButton:
                    text: 'Back'
                    text_color: 0, 0, 0, 1  # Black text color
                    pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    on_release: app.root.current = 'BorrowerScreen2'

                MDRectangleFlatButton:
                    text: 'Next'
                    text_color: 0, 0, 0, 1  # Black text color
                    pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    on_release: app.root.current = 'BorrowerScreen4'
<BorrowerScreen4>:
    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(10)
        padding: dp(10)
        size_hint_y: None
        height: self.minimum_height
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        size_hint_x: None
        width: 300
        MDCard:
            orientation: "vertical"
            size_hint: None, None
            size: "280dp", "480dp"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}

            MDLabel:
                text: 'Borrower Registration Form'
                font_size: 25
                halign: 'center'
                bold: True
            MDLabel:
                text: 'Father Information'
                font_size: 25
                halign: 'center'
                bold: True

            MDTextField:
                id: father_name
                hint_text: 'Enter father name'
                multiline: False
                helper_text_mode: 'on_focus'
                size_hint_y: None
                height: self.minimum_height
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x: None
                width: 300

            MDTextField:
                id: father_age
                hint_text: 'Enter father age '
                multiline: False
                helper_text_mode: 'on_focus'
                size_hint_y: None
                height: self.minimum_height
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x: None
                width: 300

            MDTextField:
                id: father_occupation
                hint_text: 'Enter father occupation'
                multiline: False
                helper_text_mode: 'on_focus'
                size_hint_y: None
                height: self.minimum_height
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x: None
                width: 300

            MDTextField:
                id: father_ph_no
                hint_text: 'Enter father ph no'
                multiline: False
                helper_text_mode: 'on_focus'
                size_hint_y: None
                height: self.minimum_height
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x: None
                width: 300

            BoxLayout:
                spacing: dp(10)
                size_hint_x: None
                height: "60dp"
                width: "60dp"
                pos_hint: {'center_x': 0.4, 'center_y': 0.6}
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                md_bg_color: 0, 0, 0, 1
                MDRectangleFlatButton:
                    text: 'Back'
                    text_color: 0, 0, 0, 1  # Black text color
                    pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    on_release: app.root.current = 'BorrowerScreen3'

                MDRectangleFlatButton:
                    text: 'Next'
                    text_color: 0, 0, 0, 1  # Black text color
                    pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    on_release: app.root.current = 'BorrowerScreen5'

<BorrowerScreen5>:
    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(10)
        padding: dp(10)
        size_hint_y: None
        height: self.minimum_height
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        size_hint_x: None
        width: 300
        MDCard:
            orientation: "vertical"
            size_hint: None, None
            size: "280dp", "480dp"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}

            MDLabel:
                text: 'Borrower Registration Form'
                font_size: 25
                halign: 'center'
                bold: True
            MDLabel:
                text: 'Mother Information'
                font_size: 25
                halign: 'center'
                bold: True

            MDTextField:
                id: mother_name
                hint_text: 'Enter mother name'
                multiline: False
                helper_text_mode: 'on_focus'
                size_hint_y: None
                height: self.minimum_height
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x: None
                width: 300

            MDTextField:
                id: mother_age
                hint_text: 'Enter mother age '
                multiline: False
                helper_text_mode: 'on_focus'
                size_hint_y: None
                height: self.minimum_height
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x: None
                width: 300

            MDTextField:
                id: mother_occupation
                hint_text: 'Enter mother occupation'
                multiline: False
                helper_text_mode: 'on_focus'
                size_hint_y: None
                height: self.minimum_height
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x: None
                width: 300

            MDTextField:
                id: mother_ph_no
                hint_text: 'Enter mother ph no'
                multiline: False
                helper_text_mode: 'on_focus'
                size_hint_y: None
                height: self.minimum_height
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x: None
                width: 300

            BoxLayout:
                spacing: dp(10)
                size_hint_x: None
                height: "60dp"
                width: "60dp"
                pos_hint: {'center_x': 0.4, 'center_y': 0.6}
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                md_bg_color: 0, 0, 0, 1
                MDRectangleFlatButton:
                    text: 'Back'
                    text_color: 0, 0, 0, 1  # Black text color
                    pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    on_release: app.root.current = 'BorrowerScreen4'

                MDRectangleFlatButton:
                    text: 'Next'
                    text_color: 0, 0, 0, 1  # Black text color
                    pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    on_release: app.root.current = 'BorrowerScreen6'

'''

class BorrowerScreen(Screen):
    pass
class BorrowerScreen1(Screen):
    pass
class BorrowerScreen2(Screen):
    pass
class BorrowerScreen3(Screen):
    pass
class BorrowerScreen4(Screen):
    pass
class BorrowerScreen5(Screen):
    pass

