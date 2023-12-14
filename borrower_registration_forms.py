from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu

borrower_help = """
ScreenManager:
    MenuScreen:
    FirstScreen:
    SecondScreen:
    ThirdScreen:
    FourthScreen:
    FifthScreen:
    SixthScreen:
    SevenScreen:
    EightScreen:
    NineScreen:
    TenthScreen:
    ElvenScreen:
    TwelveScreen:
    ThirteenScreen:

<MenuScreen>:
    name: 'menu'
    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(10)
        padding: dp(10)
        size_hint_y: None
        height: self.minimum_height
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        size_hint_x:None
        width:300
        MDCard:
            orientation: "vertical"
            size_hint: None, None
            size: "280dp", "180dp"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}

            MDRectangleFlatButton:
                text: 'Borrower Registration Form'
                on_press: root.manager.current = 'first'
                bold:True

#41-141 first screen code
<FirstScreen>:
    name: 'first'
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
                id: name_field
                hint_text: 'Enter Full Name'
                multiline: False
                helper_text: 'Enter a valid name'
                helper_text_mode: 'on_focus'
                #required: True
                size_hint_y: None
                height: self.minimum_height
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x:None
                width:300

            MDTextField:
                id: email_field
                hint_text: 'Enter email'
                multiline: False
                helper_text: 'Enter email'
                helper_text_mode: 'on_focus'
                size_hint_y: None
                height: self.minimum_height
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x:None
                width:300

            MDTextField:
                id: Mobile_field
                hint_text: 'Enter Mobile No'
                multiline: False
                helper_text: 'Enter a valid mobile no'
                helper_text_mode: 'on_focus'
                size_hint_y: None
                height: self.minimum_height
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x:None
                width:300

            MDTextField:
                id: gender_field
                hint_text: 'Select gender'
                helper_text: 'Enter valid gender'
                helper_text_mode: 'on_focus'
                on_focus:if self.focus:app.show_gender_menu()
                size_hint_y: None
                height: self.minimum_height
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x:None
                width:300
                multiline:False
                readonly:True
            MDTextField:
                id: alternate_mobile_field
                hint_text: 'Enter Alternate Mobile No'
                multiline: False
                helper_text: 'Enter a valid alternate mobile no'
                helper_text_mode: 'on_focus'
                size_hint_y: None
                height: self.minimum_height
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x:None
                width:300

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
                    text: 'Back'
                    on_press: root.manager.current = 'menu'

                MDRaisedButton:
                    text: 'Next'
                    on_press: root.manager.current = 'second'

#142-242 second screen code
<SecondScreen>:
    name: 'second'
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
                id: aadhaar_no_field
                hint_text: 'Enter Aadhaar no'
                multiline: False
                helper_text: 'Enter a valid aadhaar no'
                helper_text_mode: 'on_focus'
                #required: True
                size_hint_y: None
                height: self.minimum_height
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x:None
                width:300

            MDRectangleFlatButton:
                text: 'Upload aadhar card '
                #text_color: 0, 0, 0, 1  # Black text color
                pos_hint: {'center_x': 0.5, 'center_y': 0.37}
                #md_bg_color: 0.031, 0.463, 0.91, 1
                on_release: app.file_manager_open()
                size_hint: (0.1, 0.01)
                font_size: "12sp"
                size_hint_y: None
                size_hint_x: None


            MDTextField:
                id: pan_no_field
                hint_text: 'Enter Pan No'
                multiline: False
                helper_text: 'Enter a valid pan no'
                helper_text_mode: 'on_focus'
                size_hint_y: None
                height: self.minimum_height
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x:None
                width:300

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


            MDTextField:
                id: dob_field
                hint_text: 'Enter Date of birth'
                icon_right:'calendar'
                readonly:True
                multiline: False
                helper_text: 'Enter a valid alternate mobile no'
                helper_text_mode: 'on_focus'
                on_focus:if self.focus:app.show_date_picker()
                size_hint_y: None
                height: self.minimum_height
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x:None
                width:300
            
            MDRectangleFlatButton:
                text: 'Upload your Image'
                #text_color: 0, 0, 0, 1  # Black text color
                pos_hint: {'center_x': 0.5, 'center_y': 0.37}
                #md_bg_color: 0.031, 0.463, 0.91, 1
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
                MDRaisedButton:
                    text: 'Back'
                    on_press: root.manager.current = 'first'

                MDRaisedButton:
                    text: 'Next'
                    on_press: root.manager.current = 'third'

#244-330
<ThirdScreen>:
    name: 'third'
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
                id: address1_field
                hint_text: 'Enter Street address 1'
                multiline: False
                helper_text: 'Enter a Street address 1'
                helper_text_mode: 'on_focus'
                size_hint_y: None
                height: self.minimum_height
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x:None
                width:300

            MDTextField:
                id: address2_field
                hint_text: 'Enter Street address 2'
                multiline: False
                helper_text: 'Enter a Street address 2'
                helper_text_mode: 'on_focus'
                size_hint_y: None
                height: self.minimum_height
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x:None
                width:300

            MDTextField:
                id: city_field
                hint_text: 'Enter city'
                helper_text: 'Enter city'
                helper_text_mode: 'on_focus'
                size_hint_y: None
                height: self.minimum_height
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x:None
                width:300

            MDTextField:
                id: pincode_field
                hint_text: 'Enter Pincode'
                multiline: False
                helper_text: 'Enter a valid pincode'
                helper_text_mode: 'on_focus'
                size_hint_y: None
                height: self.minimum_height
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x:None
                width:300

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
                    text: 'Back'
                    on_press: root.manager.current = 'second'

                MDRaisedButton:
                    text: 'Next'
                    on_press: root.manager.current = 'fourth'

#331-418 
<FourthScreen>:
    name: 'fourth'
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
                id: father_name_field
                hint_text: 'Enter Father name'
                multiline: False
                helper_text: 'Enter a valid father name'
                helper_text_mode: 'on_focus'
                #required: True
                size_hint_y: None
                height: self.minimum_height
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x:None
                width:300

            MDTextField:
                id: father_age_field
                hint_text: 'father age'
                multiline: False
                helper_text: 'Enter a father age'
                helper_text_mode: 'on_focus'
                size_hint_y: None
                height: self.minimum_height
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x:None
                width:300

            MDTextField:
                id: father_occupation_field
                hint_text: 'Enter father occupation'
                multiline: False
                helper_text: 'Enter a father occupation'
                helper_text_mode: 'on_focus'
                size_hint_y: None
                height: self.minimum_height
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x:None
                width:300

            MDTextField:
                id: father_no_field
                hint_text: 'mother age'
                helper_text: 'Enter mother age'
                helper_text_mode: 'on_focus'
                size_hint_y: None
                height: self.minimum_height
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x:None
                width:300

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
                    text: 'Back'
                    on_press: root.manager.current = 'third'

                MDRaisedButton:
                    text: 'Next'
                    on_press: root.manager.current = 'fifth'

#420-507(mother related)
<FifthScreen>:
    name: 'fifth'
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
                id: mother_name_field
                hint_text: 'Enter Mother name'
                multiline: False
                helper_text: 'Enter mother name'
                helper_text_mode: 'on_focus'
                #required: True
                size_hint_y: None
                height: self.minimum_height
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x:None
                width:300

            MDTextField:
                id: mother_age_field
                hint_text: 'Enter mother age'
                multiline: False
                helper_text: 'Enter a mother age'
                helper_text_mode: 'on_focus'
                size_hint_y: None
                height: self.minimum_height
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x:None
                width:300

            MDTextField:
                id: mother_occupation_field
                hint_text: 'enter mother occupation'
                multiline: False
                helper_text: 'Enter mother occupation'
                helper_text_mode: 'on_focus'
                size_hint_y: None
                height: self.minimum_height
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x:None
                width:300

            MDTextField:
                id: mother_no_field
                hint_text: 'Enter mother no'
                helper_text: 'Enter mother no'
                helper_text_mode: 'on_focus'
                size_hint_y: None
                height: self.minimum_height
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x:None
                width:300

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
                    text: 'Back'
                    on_press: root.manager.current = 'fourth'

                MDRaisedButton:
                    text: 'Next'
                    on_press: root.manager.current = 'sixth'

#509-562(profession feild)
<SixthScreen>:
    name:'sixth'
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
                id: profession_field
                multiline: False
                hint_text: "Select one"
                on_focus: if self.focus: app.show_borrower_type_menu()
                height: self.minimum_height
                readonly: True
                width: 300
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                #theme_text_color: "Custom"
                #hint_text_color: (0, 0, 0, 1)  # Black hint text color
                #text_color: (0, 0, 0, 1)  # Black text color
                size_hint_x: None
                size_hint_y: None
                helper_text_mode: "on_focus"


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
                    text: 'Back'
                    on_press: root.manager.current = 'fifth'

                MDRaisedButton:
                    text: 'Next'
                    on_press: root.manager.current = 'seventh'

<SevenScreen>:
    name: 'seventh'
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
                id: college_name_field
                hint_text: 'Enter College Name'
                multiline: False
                helper_text: 'Enter college name'
                helper_text_mode: 'on_focus'
                #required: True
                size_hint_y: None
                height: self.minimum_height
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x:None
                width:300

            MDTextField:
                id: college_id_field
                hint_text: 'Enter college id'
                multiline: False
                helper_text: 'Enter college id'
                helper_text_mode: 'on_focus'
                size_hint_y: None
                height: self.minimum_height
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x:None
                width:300

            MDRectangleFlatButton:
                text: 'Upload college proof '
                #text_color: 0, 0, 0, 1  # Black text color
                pos_hint: {'center_x': 0.5, 'center_y': 0.37}
                #md_bg_color: 0.031, 0.463, 0.91, 1
                on_release: app.file_manager_open()
                size_hint: (0.1, 0.01)
                font_size: "12sp"
                size_hint_y: None
                size_hint_x: None

            MDTextField:
                id: college_address_field
                hint_text: 'Enter college address'
                helper_text: 'Enter college address'
                helper_text_mode: 'on_focus'
                size_hint_y: None
                height: self.minimum_height
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x:None
                width:300
                multiline:True

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
                    text: 'Back'
                    on_press: root.manager.current = 'sixth'

                MDRaisedButton:
                    text: 'Next'
                    on_press: root.manager.current = 'eight'
<SevenScreen>:
    name: 'seventh'
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
                id: home_loans_field
                hint_text: ''
                multiline: False
                helper_text: 'Enter college name'
                helper_text_mode: 'on_focus'
                #required: True
                size_hint_y: None
                height: self.minimum_height
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x:None
                width:300

            MDTextField:
                id: college_id_field
                hint_text: 'Enter college id'
                multiline: False
                helper_text: 'Enter college id'
                helper_text_mode: 'on_focus'
                size_hint_y: None
                height: self.minimum_height
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x:None
                width:300

            MDRectangleFlatButton:
                text: 'Upload college proof '
                #text_color: 0, 0, 0, 1  # Black text color
                pos_hint: {'center_x': 0.5, 'center_y': 0.37}
                #md_bg_color: 0.031, 0.463, 0.91, 1
                on_release: app.file_manager_open()
                size_hint: (0.1, 0.01)
                font_size: "12sp"
                size_hint_y: None
                size_hint_x: None

            MDTextField:
                id: college_address_field
                hint_text: 'Enter college address'
                helper_text: 'Enter college address'
                helper_text_mode: 'on_focus'
                size_hint_y: None
                height: self.minimum_height
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x:None
                width:300
                multiline:True

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
                    text: 'Back'
                    on_press: root.manager.current = 'sixth'

                MDRaisedButton:
                    text: 'Next'
                    on_press: root.manager.current = 'eight'

<NineScreen>:
    name: 'nine'
    MDLabel:
        text: 'Borrower Registration Form'
        font_size:32
        halign: 'center'
        pos_hint: {'center_x': 0.5, 'center_y': 0.7}
        bold:True
    MDLabel:
        text: 'Branch Name:'
        halign: 'center'
        pos_hint: {'center_x': 0.2, 'center_y': 0.6}
        size_hint_x: None
        width: 250
    MDTextField:
        id: branch_name_field
        hint_text: 'Enter Branch Name'
        multiline: False
        pos_hint: {'center_x': 0.8, 'center_y': 0.6}
        helper_text: 'Enter a valid Branch name'
        helper_text_mode: 'on_focus'
        size_hint_x: None
        width: 250

    MDLabel:
        text: 'Account Holder Name:'
        halign: 'center'
        pos_hint: {'center_x': 0.2, 'center_y': 0.5}
    MDTextField:
        id: account_holder_field
        hint_text: 'account holder'
        multiline: False
        pos_hint: {'center_x': 0.8, 'center_y': 0.5}
        helper_text: 'Account Holder Name'
        helper_text_mode: 'on_focus'
        size_hint_x: None
        width: 250
    MDLabel:
        text: 'Account Number:'
        halign: 'center'
        pos_hint: {'center_x': 0.2, 'center_y': 0.4}
    MDTextField:
        id: account_no_field
        hint_text: 'Enter account No'
        pos_hint: {'center_x': 0.8, 'center_y': 0.4}
        helper_text: 'Enter account No'
        helper_text_mode: 'on_focus'
        size_hint_x: None
        width: 250

    MDLabel:
        text: 'Account Type:'
        halign: 'center'
        pos_hint: {'center_x': 0.2, 'center_y': 0.3}
    MDTextField:
        id: account_type_field
        hint_text: 'account type'
        multiline: False
        pos_hint: {'center_x': 0.8, 'center_y': 0.3}
        helper_text: 'Account Type'
        helper_text_mode: 'on_focus'
        size_hint_x: None
        width: 250

    MDRaisedButton:
        text: 'Back'
        pos_hint: {'center_x': 0.3, 'center_y': 0.1}
        on_press: root.manager.current = 'seventh'

    MDRaisedButton:
        text: 'Next'
        pos_hint: {'center_x': 0.7, 'center_y': 0.1}
        on_press: root.manager.current='nine'
<NineScreen>:
    name: 'nine'
    MDLabel:
        text: 'Borrower Registration Form'
        font_size:32
        halign: 'center'
        pos_hint: {'center_x': 0.5, 'center_y': 0.7}
        bold:True
    MDLabel:
        text: 'IFSC Code:'
        halign: 'center'
        pos_hint: {'center_x': 0.2, 'center_y': 0.6}
        size_hint_x: None
        width: 250
    MDTextField:
        id: ifsc_field
        hint_text: 'Enter IFSC Code'
        multiline: False
        pos_hint: {'center_x': 0.8, 'center_y': 0.6}
        helper_text: 'Enter a Ifsc Code'
        helper_text_mode: 'on_focus'
        size_hint_x: None
        width: 250

    MDLabel:
        text: 'Salary Paid:'
        halign: 'center'
        pos_hint: {'center_x': 0.2, 'center_y': 0.5}
    MDTextField:
        id: salary_paid_field
        hint_text: 'salary paid'
        multiline: False
        pos_hint: {'center_x': 0.8, 'center_y': 0.5}
        helper_text: 'salary paid'
        helper_text_mode: 'on_focus'
        size_hint_x: None
        width: 250
    MDLabel:
        text: 'Net Banking:'
        halign: 'center'
        pos_hint: {'center_x': 0.2, 'center_y': 0.4}
    MDTextField:
        id: net_banking_field
        hint_text: 'Select feild'
        pos_hint: {'center_x': 0.8, 'center_y': 0.4}
        helper_text: 'select option'
        helper_text_mode: 'on_focus'
        size_hint_x: None
        width: 250


    MDRaisedButton:
        text: 'Back'
        pos_hint: {'center_x': 0.3, 'center_y': 0.1}
        on_press: root.manager.current = 'eight'

    MDRaisedButton:
        text: 'Next'
        pos_hint: {'center_x': 0.7, 'center_y': 0.1}
        on_press: root.manager.current='tenth'

"""


class MenuScreen(Screen):
    pass


class FirstScreen(Screen):
    pass


class SecondScreen(Screen):
    pass


class ThirdScreen(Screen):
    pass


class FourthScreen(Screen):
    pass


class FifthScreen(Screen):
    pass


class SixthScreen(Screen):
    pass


class SevenScreen(Screen):
    pass


class EightScreen(Screen):
    pass


class NineScreen(Screen):
    pass


class DemoApp(MDApp):
    def build(self):
        self.gender_dropdown = None
        self.name_field = None
        self.mobile_field = None
        self.gender_field = None
        self.email_field = None
        self.alternate_mobile_field = None

        screen = Builder.load_string(borrower_help)
        return screen

    def show_gender_dropdown(self):
        try:
            if self.gender_dropdown and self.gender_dropdown.is_open:
                self.gender_dropdown.dismiss()
            else:
                self.gender_dropdown = MDDropdownMenu(
                    caller=self.root.get_screen('first').ids.gender_field,
                    items=[{'text': 'Male'}, {'text': 'Female'}, {'text': 'Other'}],
                    width_mult=4,
                )
                self.gender_dropdown.bind(on_release=self.on_gender_select)
                self.gender_dropdown.open()
        except AttributeError:
            pass  # Handle the AttributeError (no is_open attribute) gracefully

    def on_gender_select(self, instance_menu, instance_menu_item):
        self.root.get_screen('first').ids.gender_field.text = instance_menu_item.text
        self.gender_dropdown.dismiss()

    def show_profession_dropdown(self):
        try:
            if self.profession_dropdown and self.profession_dropdown.is_open:
                self.profession_dropdown.dismiss()
            else:
                self.profession_dropdown = MDDropdownMenu(
                    caller=self.root.get_screen('fifth').ids.profession_field,
                    items=[
                        {'text': 'Student'},
                        {'text': 'Employee'},
                        {'text': 'Business'},
                        # Add more professions as needed
                    ],
                    width_mult=4,
                )
                self.profession_dropdown.bind(on_release=self.on_profession_select)
                self.profession_dropdown.open()
        except AttributeError:
            pass  # Handle the AttributeError (no is_open attribute) gracefully

    def on_profession_select(self, instance_menu, instance_menu_item):
        self.root.get_screen('fifth').ids.profession_field.text = instance_menu_item.text
        self.profession_dropdown.dismiss()

    def validate_and_proceed(self):
        current_screen = self.root.current_screen.name

        if current_screen == 'first':
            user_id = "123"  # Replace this with the actual user ID logic
            name = self.root.get_screen('first').ids.name_field.text
            mobile = self.root.get_screen('first').ids.mobile_field.text
            gender = self.root.get_screen('first').ids.gender_field.text
            email = self.root.get_screen('first').ids.email_field.text
            alternate_mobile = self.root.get_screen('first').ids.alternate_mobile_field.text

            if not name or not mobile or not gender or not email or not alternate_mobile:
                self.show_error_message("Please enter all required information.")
            else:
                print(
                    f"User ID: {user_id}, Name: {name}, Mobile No: {mobile}, Gender: {gender}, Email: {email}, Alternate Mobile No: {alternate_mobile}")
                self.root.manager.current = 'second'

        elif current_screen == 'second':
            # Handle validation and processing for the second screen
            pass

    def show_error_message(self, message):
        # You can customize this method to display an error message
        print(f"Error: {message}")


DemoApp().run()