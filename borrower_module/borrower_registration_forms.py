from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivymd.uix.button import MDRectangleFlatButton
from kivy.metrics import dp
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.pickers import MDDatePicker
from kivy.core.window import Window
from kivymd.app import MDApp

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
            BoxLayout:
                spacing: dp(10)
                size_hint_x: None
                height: "60dp"
                width: "60dp"
                pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                md_bg_color: 0, 0, 0, 1

                MDRaisedButton:
                    text: 'Home'
                    text_color: 0, 0, 0, 1  # Black text color
                    pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    on_release: app.root.current()

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

            Spinner:
                id: gender_id
                text: "select gender"
                values: ["Male", "Female", "Others"]
                multiline: False
                size_hint: (None, None)
                height: 70
                width: 330
                background_color: (0, 0, 0, 0)
                background_normal: ''
                canvas.before:
                    Color:
                        rgba: 0.031, 0.463, 0.91, 1
                    RoundedRectangle:
                        size: self.size
                        pos: self.pos
                        radius: [15]

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

                MDRaisedButton:
                    text: 'Next'
                    text_color: 0, 0, 0, 1  # Black text color
                    pos_hint: {'center_x': 0.3, 'center_y': 0.5}
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
            BoxLayout:
                spacing: dp(10)
                size_hint_x: None
                height: "60dp"
                width: "60dp"
                pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                md_bg_color: 0, 0, 0, 1

                MDRaisedButton:
                    text: 'Home'
                    text_color: 0, 0, 0, 1  # Black text color
                    pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    on_release: app.root.current()

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
            BoxLayout:
                spacing: dp(10)
                size_hint_x: None
                height: "60dp"
                width: "60dp"
                pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                md_bg_color: 0, 0, 0, 1

                MDRaisedButton:
                    text: 'Home'
                    text_color: 0, 0, 0, 1  # Black text color
                    pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    on_release: app.root.current()

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
            BoxLayout:
                spacing: dp(10)
                size_hint_x: None
                height: "60dp"
                width: "60dp"
                pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                md_bg_color: 0, 0, 0, 1

                MDRaisedButton:
                    text: 'Home'
                    text_color: 0, 0, 0, 1  # Black text color
                    pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    on_release: app.root.current()

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
            BoxLayout:
                spacing: dp(10)
                size_hint_x: None
                height: "60dp"
                width: "60dp"
                pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                md_bg_color: 0, 0, 0, 1

                MDRaisedButton:
                    text: 'Home'
                    text_color: 0, 0, 0, 1  # Black text color
                    pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    on_release: app.root.current()

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
            BoxLayout:
                spacing: dp(10)
                size_hint_x: None
                height: "60dp"
                width: "60dp"
                pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                md_bg_color: 0, 0, 0, 1

                MDRaisedButton:
                    text: 'Home'
                    text_color: 0, 0, 0, 1  # Black text color
                    pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    on_release: app.root.current()

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
<BorrowerScreen6>:
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
            BoxLayout:
                spacing: dp(10)
                size_hint_x: None
                height: "60dp"
                width: "60dp"
                pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                md_bg_color: 0, 0, 0, 1

                MDRaisedButton:
                    text: 'Home'
                    text_color: 0, 0, 0, 1  # Black text color
                    pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    on_release: app.root.current()

            MDLabel:
                text: 'Borrower Registration Form'
                font_size: 25
                halign: 'center'
                bold: True

            Spinner:
                id: spinner_id
                text: "select option"
                values: ["Student", "Employee", "Business"]
                multiline: False
                size_hint: (None, None)
                height: 70
                width: 330
                background_color: (0, 0, 0, 0)
                background_normal: ''
                canvas.before:
                    Color:
                        rgba: 0.031, 0.463, 0.91, 1
                    RoundedRectangle:
                        size: self.size
                        pos: self.pos
                        radius: [15]

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
                    on_release: app.root.current = 'BorrowerScreen5'

                MDRectangleFlatButton:
                    text: 'Next'
                    text_color: 0, 0, 0, 1  # Black text color
                    pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    on_press: root.next_pressed(spinner_id.text)
<BorrowerScreen7>
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
            BoxLayout:
                spacing: dp(10)
                size_hint_x: None
                height: "60dp"
                width: "60dp"
                pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                md_bg_color: 0, 0, 0, 1

                MDRaisedButton:
                    text: 'Home'
                    text_color: 0, 0, 0, 1  # Black text color
                    pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    on_release: app.root.current()

            MDLabel:
                text: 'Student Type'
                font_size: 25
                halign: 'center'
                bold: True

            MDTextField:
                id: collage_name
                hint_text: 'Enter college name '
                multiline: False
                helper_text_mode: 'on_focus'
                size_hint_y: None
                height: self.minimum_height
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x: None
                width: 300

            MDTextField:
                id: collage_id
                hint_text: 'Enter college id'
                multiline: False
                helper_text_mode: 'on_focus'
                size_hint_y: None
                height: self.minimum_height
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x: None
                width: 300

            MDRectangleFlatButton:
                text: 'Upload college proof '
                text_color: 0, 0, 0, 1  # Black text color
                pos_hint: {'center_x': 0.5, 'center_y': 0.37}
                md_bg_color: 0.031, 0.463, 0.91, 1
                on_release: app.file_manager_open()
                size_hint: (0.1, 0.01)
                font_size: "12sp"
                size_hint_y: None
                size_hint_x: None

            MDTextField:
                id:  college_address
                hint_text: 'Enter college address'
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
                    on_release: app.root.current='BorrowerScreen6'

                MDRectangleFlatButton:
                    text: 'Next'
                    text_color: 0, 0, 0, 1  # Black text color
                    pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    on_release: app.root.current='BorrowerScreen15'
<BorrowerScreen8>:
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
            BoxLayout:
                spacing: dp(10)
                size_hint_x: None
                height: "60dp"
                width: "60dp"
                pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                md_bg_color: 0, 0, 0, 1

                MDRaisedButton:
                    text: 'Home'
                    text_color: 0, 0, 0, 1  # Black text color
                    pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    on_release: app.root.current()

            MDLabel:
                text: 'Business Type'
                font_size: 25
                halign: 'center'
                bold: True

            MDLabel:
                text: 'Step-1'
                font_size: 25
                halign: 'center'
                bold: True

            MDTextField:
                id: business_name
                hint_text: 'Enter business name '
                multiline: False
                helper_text_mode: 'on_focus'
                size_hint_y: None
                height: self.minimum_height
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x: None
                width: 300

            MDTextField:
                id: business_location
                hint_text: 'Enter business_location'
                multiline: False                   
                helper_text_mode: 'on_focus'
                size_hint_y: None
                height: self.minimum_height
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x: None
                width: 300

            MDTextField:
                id:  business_address
                hint_text: 'Enter business address'
                multiline: False
                helper_text_mode: 'on_focus'
                size_hint_y: None
                height: self.minimum_height
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x: None
                width: 300

            MDTextField:
                id: branch_name
                hint_text: 'Enter branch_name'
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
                    on_release: app.root.current = 'BorrowerScreen6'

                MDRectangleFlatButton:
                    text: 'Next'
                    text_color: 0, 0, 0, 1  # Black text color
                    pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    on_release: app.root.current = 'BorrowerScreen9'
<BorrowerScreen9>:
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
            BoxLayout:
                spacing: dp(10)
                size_hint_x: None
                height: "60dp"
                width: "60dp"
                pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                md_bg_color: 0, 0, 0, 1

                MDRaisedButton:
                    text: 'Home'
                    text_color: 0, 0, 0, 1  # Black text color
                    pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    on_release: app.root.current()

            MDLabel:
                text: 'Step-2'
                font_size: 25
                halign: 'center'
                bold: True

            MDTextField:
                id: nearest_location
                hint_text: 'Enter nearest location '
                multiline: False
                helper_text_mode: 'on_focus'
                size_hint_y: None
                height: self.minimum_height
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x: None
                width: 300

            MDTextField:
                id: business_type
                hint_text: 'Enter business type'
                multiline: False                   
                helper_text_mode: 'on_focus'
                size_hint_y: None
                height: self.minimum_height
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x: None
                width: 300

            Spinner:
                id: employee_id
                text: "select no of employees working"
                values: ["<50", "50-100", "100-150", "150-200", ">200"]
                multiline: False
                size_hint: (None, None)
                height: 70
                width: 330
                background_color: (0, 0, 0, 0)
                background_normal: ''
                canvas.before:
                    Color:
                        rgba: 0.031, 0.463, 0.91, 1
                    RoundedRectangle:
                        size: self.size
                        pos: self.pos
                        radius: [15]

            MDTextField:
                id: year_of_estd
                hint_text: 'Enter year of estd'
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
                    on_release: app.root.current = 'BorrowerScreen8'

                MDRectangleFlatButton:
                    text: 'Next'
                    text_color: 0, 0, 0, 1  # Black text color
                    pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    on_release: app.root.current = 'BorrowerScreen10'

<BorrowerScreen10>:
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
            BoxLayout:
                spacing: dp(10)
                size_hint_x: None
                height: "60dp"
                width: "60dp"
                pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                md_bg_color: 0, 0, 0, 1

                MDRaisedButton:
                    text: 'Home'
                    text_color: 0, 0, 0, 1  # Black text color
                    pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    on_release: app.root.current()

            MDLabel:
                text: 'Step-3'
                font_size: 25
                halign: 'center'
                bold: True

            MDTextField:
                id: industry_type
                hint_text: 'Enter industry type '
                multiline: False
                helper_text_mode: 'on_focus'
                size_hint_y: None
                height: self.minimum_height
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x: None
                width: 300

            MDTextField:
                id: last_six_months_turnover
                hint_text: 'Enter last 6 months turnover'
                multiline: False                   
                helper_text_mode: 'on_focus'
                size_hint_y: None
                height: self.minimum_height
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x: None
                width: 300

            MDLabel:
                text: "Last 6 months bank statements"
                font_size: 22
                halign: 'center'

            MDRectangleFlatButton:
                text: 'Upload here'
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
                    on_release: app.root.current = 'BorrowerScreen9'

                MDRectangleFlatButton:
                    text: 'Next'
                    text_color: 0, 0, 0, 1  # Black text color
                    pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    on_release: app.root.current = 'BorrowerScreen11'

<BorrowerScreen11>:
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
            BoxLayout:
                spacing: dp(10)
                size_hint_x: None
                height: "60dp"
                width: "60dp"
                pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                md_bg_color: 0, 0, 0, 1

                MDRaisedButton:
                    text: 'Home'
                    text_color: 0, 0, 0, 1  # Black text color
                    pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    on_release: app.root.current()

            MDLabel:
                text: 'Step-4'
                font_size: 25
                halign: 'center'
                bold: True

            MDTextField:
                id: director_name
                hint_text: 'Enter director name '
                multiline: False
                helper_text_mode: 'on_focus'
                size_hint_y: None
                height: self.minimum_height
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x: None
                width: 300

            MDTextField:
                id: director_mobile_number
                hint_text: 'Enter director mobile number'
                multiline: False
                helper_text_mode: 'on_focus'
                size_hint_y: None
                height: self.minimum_height
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x: None
                width: 300

            MDTextField:
                id: din
                hint_text: 'Enter DIN here'
                multiline: False
                helper_text_mode: 'on_focus'
                size_hint_y: None
                height: self.minimum_height
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x: None
                width: 300

            MDTextField:
                id: cin
                hint_text: 'Enter CIN here'
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
                    on_release: app.root.current = 'BorrowerScreen10'

                MDRectangleFlatButton:
                    text: 'Next'
                    text_color: 0, 0, 0, 1  # Black text color
                    pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    on_release: app.root.current = 'BorrowerScreen12'

<BorrowerScreen12>:
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
            BoxLayout:
                spacing: dp(10)
                size_hint_x: None
                height: "60dp"
                width: "60dp"
                pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                md_bg_color: 0, 0, 0, 1

                MDRaisedButton:
                    text: 'Home'
                    text_color: 0, 0, 0, 1  # Black text color
                    pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    on_release: app.root.current()

            MDLabel:
                text: 'Step-5'
                font_size: 25
                halign: 'center'
                bold: True

            MDTextField:
                id: reg_office_address
                hint_text: 'Enter registered office address '
                multiline: False
                helper_text_mode: 'on_focus'
                size_hint_y: None
                height: self.minimum_height
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x: None
                width: 300

            MDTextField:
                id: office_address_proof
                hint_text: 'Enter office address proof'
                multiline: False
                helper_text_mode: 'on_focus'
                size_hint_y: None
                height: self.minimum_height
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x: None
                width: 300

            MDLabel:
                text: "Proof of verification"
                font_size: 22
                halign: 'center'

            MDRectangleFlatButton:
                text: 'Upload here'
                text_color: 0, 0, 0, 1  # Black text color
                pos_hint: {'center_x': 0.5, 'center_y': 0.37}
                md_bg_color: 0.031, 0.463, 0.91, 1
                on_release: app.file_manager_open()
                size_hint: (0.1, 0.01)
                font_size: "12sp"
                size_hint_y: None
                size_hint_x: None

            MDTextField:
                id: branch_name
                hint_text: 'Enter branch_name'
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
                    on_release: app.root.current = 'BorrowerScreen11'

                MDRectangleFlatButton:
                    text: 'Next'
                    text_color: 0, 0, 0, 1  # Black text color
                    pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    on_release: app.root.current = 'BorrowerScreen15'
<BorrowerScreen13>:
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
            BoxLayout:
                spacing: dp(10)
                size_hint_x: None
                height: "60dp"
                width: "60dp"
                pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                md_bg_color: 0, 0, 0, 1

                MDRaisedButton:
                    text: 'Home'
                    text_color: 0, 0, 0, 1  # Black text color
                    pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    on_release: app.root.current()

            MDLabel:
                text: 'Employment Details'
                font_size: 25
                halign: 'center'
                bold: True
            MDTextField:
                id: company_name
                hint_text: 'Enter company_name'
                multiline: False
                helper_text_mode: 'on_focus'
                size_hint_y: None
                height: self.minimum_height
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x: None
                width: 300

            MDTextField:              
                id: pincode
                hint_text: 'Enter pincode'
                multiline: False                        
                helper_text_mode: 'on_focus'
                size_hint_y: None
                height: self.minimum_height
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x: None
                width: 300
            MDTextField:              
                id: country
                hint_text: 'Enter country'
                multiline: False                        
                helper_text_mode: 'on_focus'
                size_hint_y: None
                height: self.minimum_height
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x: None
                width: 300
            MDTextField:              
                id: landmark
                hint_text: 'Enter landmark'
                multiline: False                        
                helper_text_mode: 'on_focus'
                size_hint_y: None
                height: self.minimum_height
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x: None
                width: 300

            MDTextField:              
                id: business_phone_number
                hint_text: 'Enter business phone number'
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
                    on_release: app.root.current = 'BorrowerScreen6'

                MDRectangleFlatButton:
                    text: 'Next'
                    text_color: 0, 0, 0, 1  # Black text color
                    pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    on_release: app.root.current = 'BorrowerScreen14'

<BorrowerScreen14>:
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
            BoxLayout:
                spacing: dp(10)
                size_hint_x: None
                height: "60dp"
                width: "60dp"
                pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                md_bg_color: 0, 0, 0, 1

                MDRaisedButton:
                    text: 'Home'
                    text_color: 0, 0, 0, 1  # Black text color
                    pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    on_release: app.root.current()

            MDLabel:
                text: 'Employment Details'
                font_size: 25
                halign: 'center'
                bold: True   

            MDTextField:              
                id: annual_salary
                hint_text: 'Enter annual salary'
                multiline: False                        
                helper_text_mode: 'on_focus'
                size_hint_y: None
                height: self.minimum_height
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x: None
                width: 300

            MDTextField:              
                id: designation
                hint_text: 'Enter designation'
                multiline: False                        
                helper_text_mode: 'on_focus'
                size_hint_y: None
                height: self.minimum_height
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x: None
                width: 300

            MDLabel:
                text: "Upload Employee ID"
                font_size: 18
                halign: 'center'

            MDRectangleFlatButton:
                text: 'Upload here'
                text_color: 0, 0, 0, 1  # Black text color
                pos_hint: {'center_x': 0.5, 'center_y': 0.37}
                md_bg_color: 0.031, 0.463, 0.91, 1
                on_release: app.file_manager_open()
                size_hint: (0.1, 0.01)
                font_size: "10sp"
                size_hint_y: None
                size_hint_x: None

            MDLabel:
                text: "Upload last 6 months bank statements"
                font_size: 18
                halign: 'center'

            MDRectangleFlatButton:
                text: 'Upload here'
                text_color: 0, 0, 0, 1  # Black text color
                pos_hint: {'center_x': 0.5, 'center_y': 0.37}
                md_bg_color: 0.031, 0.463, 0.91, 1
                on_release: app.file_manager_open()
                size_hint: (0.1, 0.01)
                font_size: "10sp"
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
                    on_release: app.root.current = 'BorrowerScreen13'

                MDRectangleFlatButton:
                    text: 'Next'
                    text_color: 0, 0, 0, 1  # Black text color
                    pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    on_release: app.root.current = 'BorrowerScreen15'
<BorrowerScreen15>:
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
            BoxLayout:
                spacing: dp(10)
                size_hint_x: None
                height: "60dp"
                width: "60dp"
                pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                md_bg_color: 0, 0, 0, 1

                MDRaisedButton:
                    text: 'Home'
                    text_color: 0, 0, 0, 1  # Black text color
                    pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    on_release: app.root.current()

            MDLabel:
                text: 'Borrower Registration Form'
                font_size: 25
                halign: 'center'
                bold: True

            Spinner:
                id: marrital_status_id
                text: "select option"
                values: ["Married", "Un-Married", "Diversed"]
                multiline: False
                size_hint: (None, None)
                height: 70
                width: 330
                background_color: (0, 0, 0, 0)
                background_normal: ''
                canvas.before:
                    Color:
                        rgba: 0.031, 0.463, 0.91, 1
                    RoundedRectangle:
                        size: self.size
                        pos: self.pos
                        radius: [15]

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
                    on_release: app.root.current = 'BorrowerScreen14'

                MDRectangleFlatButton:
                    text: 'Next'
                    text_color: 0, 0, 0, 1  # Black text color
                    pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    on_release: root.next_button(marrital_status_id.text)

<BorrowerScreen16>:
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
            BoxLayout:
                spacing: dp(10)
                size_hint_x: None
                height: "60dp"
                width: "60dp"
                pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                md_bg_color: 0, 0, 0, 1

                MDRaisedButton:
                    text: 'Home'
                    text_color: 0, 0, 0, 1  # Black text color
                    pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    on_release: app.root.current()

            MDLabel:
                text: 'Step-1'
                font_size: 25
                halign: 'center'
                bold: True

            MDTextField:
                id: spouse_name
                hint_text: 'Enter spouse name '
                multiline: False
                helper_text_mode: 'on_focus'
                size_hint_y: None
                height: self.minimum_height
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x: None
                width: 300

            MDTextField:
                id: spouse_date_textfield
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
                id: spouse_mobile
                hint_text: 'Enter spouse mobile no'
                multiline: False
                helper_text_mode: 'on_focus'
                size_hint_y: None
                height: self.minimum_height
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x: None
                width: 300

            MDTextField:
                id: spouse_profession
                hint_text: 'Enter spouse profession '
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
                    on_release: app.root.current = 'BorrowerScreen15'

                MDRectangleFlatButton:
                    text: 'Next'
                    text_color: 0, 0, 0, 1  # Black text color
                    pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    on_release: app.root.current = 'BorrowerScreen17'
<BorrowerScreen17>:
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
            BoxLayout:
                spacing: dp(10)
                size_hint_x: None
                height: "60dp"
                width: "60dp"
                pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                md_bg_color: 0, 0, 0, 1

                MDRaisedButton:
                    text: 'Home'
                    text_color: 0, 0, 0, 1  # Black text color
                    pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    on_release: app.root.current()

            MDLabel:
                text: 'Step-2'
                font_size: 25
                halign: 'center'
                bold: True

            MDTextField:
                id: spouse_company_name
                hint_text: 'Enter spouse company name '
                multiline: False
                helper_text_mode: 'on_focus'
                size_hint_y: None
                height: self.minimum_height
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x: None
                width: 300

            MDTextField:
                id: spouse_company_address
                hint_text: 'Enter spouse company address'
                multiline: False                   
                helper_text_mode: 'on_focus'
                size_hint_y: None
                height: self.minimum_height
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x: None
                width: 300

            MDTextField:
                id:  spouse_annual_salary
                hint_text: 'Enter annual salary'
                multiline: False
                helper_text_mode: 'on_focus'
                size_hint_y: None
                height: self.minimum_height
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x: None
                width: 300

            MDTextField:
                id:spouse_office_no
                hint_text: 'Enter spouse office no'
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
                    on_release: app.root.current = 'BorrowerScreen16'

                MDRectangleFlatButton:
                    text: 'Next'
                    text_color: 0, 0, 0, 1  # Black text color
                    pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    on_release: app.root.current = 'BorrowerScreen18'

<BorrowerScreen18>:
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
            BoxLayout:
                spacing: dp(10)
                size_hint_x: None
                height: "60dp"
                width: "60dp"
                pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                md_bg_color: 0, 0, 0, 1

                MDRaisedButton:
                    text: 'Home'
                    text_color: 0, 0, 0, 1  # Black text color
                    pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    on_release: app.root.current()

            MDLabel:
                text: 'Applicant Bank Details'
                font_size: 25
                halign: 'center'
                bold: True

            MDTextField:
                id: account_holder_name
                hint_text: 'Enter account holder name '
                multiline: False
                helper_text: 'Enter valid account holder name'
                helper_text_mode: 'on_focus'
                size_hint_y: None
                height: self.minimum_height
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x: None
                width: 300

            Spinner:
                id: account_type_id
                text: "select account type option"
                values: ["Savings Account", "Salary Account", "Current Account", "NRI Account", "Fixed Account", "Re-Curing Account"]
                multiline: False
                size_hint: (None, None)
                height: 70
                width: 330
                background_color: (0, 0, 0, 0)
                background_normal: ''
                canvas.before:
                    Color:
                        rgba: 0.031, 0.463, 0.91, 1
                    RoundedRectangle:
                        size: self.size
                        pos: self.pos
                        radius: [15]
            MDTextField:
                id: account_number
                hint_text: 'Enter account number '
                multiline: False
                helper_text: 'Enter valid account number'
                helper_text_mode: 'on_focus'
                size_hint_y: None
                height: self.minimum_height
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x: None
                width: 300

            MDTextField:
                id: bank_name
                hint_text: 'Enter bank name '
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
                    on_release: app.root.current = 'BorrowerScreen17'

                MDRectangleFlatButton:
                    text: 'Next'
                    text_color: 0, 0, 0, 1  # Black text color
                    pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    on_release: app.root.current = 'BorrowerScreen19'
<BorrowerScreen19>:
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
            BoxLayout:
                spacing: dp(10)
                size_hint_x: None
                height: "60dp"
                width: "60dp"
                pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                md_bg_color: 0, 0, 0, 1

                MDRaisedButton:
                    text: 'Home'
                    text_color: 0, 0, 0, 1  # Black text color
                    pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    on_release: app.root.current()

            MDLabel:
                text: 'Applicant Bank Details'
                font_size: 25
                halign: 'center'
                bold: True

            MDTextField:
                id: bank_id
                hint_text: 'Enter Bank id '
                multiline: False
                helper_text: 'Enter valid bank id'
                helper_text_mode: 'on_focus'
                size_hint_y: None
                height: self.minimum_height
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x: None
                width: 300

            Spinner:
                id: salary_id
                text: "select salary paid option"
                values: ["Cash", "Online", "Check"]
                multiline: False
                size_hint: (None, None)
                height: 70
                width: 330
                background_color: (0, 0, 0, 0)
                background_normal: ''
                canvas.before:
                    Color:
                        rgba: 0.031, 0.463, 0.91, 1
                    RoundedRectangle:
                        size: self.size
                        pos: self.pos
                        radius: [15]

            MDTextField:
                id: branch_name
                hint_text: 'Enter branch name'
                multiline: False
                helper_text_mode: 'on_focus'
                size_hint_y: None
                height: self.minimum_height
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x: None
                width: 300

            Spinner:
                id: net_banking_id
                text: "select net banking option"
                values: ["Yes", "No"]
                multiline: False
                size_hint: (None, None)
                height: 70
                width: 330
                background_color: (0, 0, 0, 0)
                background_normal: ''
                canvas.before:
                    Color:
                        rgba: 0.031, 0.463, 0.91, 1
                    RoundedRectangle:
                        size: self.size
                        pos: self.pos
                        radius: [15]

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
                    on_release: app.root.current = 'BorrowerScreen18'

                MDRectangleFlatButton:
                    text: 'Next'
                    text_color: 0, 0, 0, 1  # Black text color
                    pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    on_release: root.go_to_borrower_dashboard()

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


class BorrowerScreen6(Screen):
    def next_pressed(self, id):
        if id == 'Student':
            self.manager.current = 'BorrowerScreen7'

        elif id == 'Business':
            self.manager.current = 'BorrowerScreen8'

        elif id == 'Employee':
            self.manager.current = 'BorrowerScreen13'
        print(id)


class BorrowerScreen7(Screen):
    pass


class BorrowerScreen8(Screen):
    pass


class BorrowerScreen9(Screen):
    pass


class BorrowerScreen10(Screen):
    pass


class BorrowerScreen11(Screen):
    pass


class BorrowerScreen12(Screen):
    pass


class BorrowerScreen13(Screen):
    pass


class BorrowerScreen14(Screen):
    pass


class BorrowerScreen15(Screen):
    def next_button(self, id):
        if id == 'Married':
            self.manager.current = 'BorrowerScreen18'

        elif id == 'Un-Married':
            self.manager.current = 'BorrowerScreen16'

        elif id == 'Diversed':
            self.manager.current = 'BorrowerScreen18'


class BorrowerScreen16(Screen):
    pass


class BorrowerScreen17(Screen):
    pass


class BorrowerScreen18(Screen):
    pass


class BorrowerScreen19(Screen):
    def go_to_borrower_dashboard(self):
        # Access the app instance and change the current screen to 'dashboard'
        self.manager.current = 'borrower_dashboard'
