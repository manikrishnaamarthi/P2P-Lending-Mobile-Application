from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivymd.uix.button import MDRectangleFlatButton
from kivy.metrics import dp
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.pickers import MDDatePicker
from kivy.core.window import Window

Window.size = (350, 600)

KV = '''
<LenderScreen>:# lender_module/lender_registration_form.py


    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(10)
        padding: dp(10)
        size_hint_y: None
        height: self.minimum_height
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        size_hint_x: None
        width: 300

        MDLabel:
            text: 'Lender Registration Form'
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
            id: gender_field
            hint_text: "Select gender"
            on_focus: if self.focus: app.show_gender_menu()
            size_hint: (None, None)
            readonly: True
            width: 300
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            theme_text_color: "Custom"
            hint_text_color: (0, 0, 0, 1)  # Black hint text color
            text_color: (0, 0, 0, 1)  # Black text color
            helper_text: "Select gender"
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
                on_release: app.root.current = 'LenderScreen1'
<LenderScreen1>:
    BoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(20)

        MDLabel:
            text: 'Lender Registration Form'
            font_size: 25
            halign: 'center'
            bold: True

        MDTextField:
            id: username
            hint_text: 'Enter mobile number'
            multiline: False
            helper_text: 'Enter valid number'
            helper_text_mode: 'on_focus'
            size_hint_y: None
            height: self.minimum_height
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            size_hint_x: None
            width: 300
            font_name: "Roboto-Bold"
        MDTextField:
            id: username
            hint_text: 'Enter alternate email'
            multiline: False
            helper_text: 'Enter valid email'
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
                on_release: app.root.current = 'LenderScreen2'
<LenderScreen2>:
    BoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(20)



        MDLabel:
            text: 'Lender Registration Form'
            font_size: 25
            halign: 'center'
            bold: True                


        MDRectangleFlatButton:
            text: 'HOME'
            text_color: 0, 0, 0, 1  # Black text color
            pos_hint: {'center_x': 0.5, 'center_y': 0.3}
            md_bg_color: 0.031, 0.463, 0.91, 1
            pos_hint: {'right': 1, 'top': 1}
            on_release: app.go_home()
            size_hint: (0.1, 0.03)
            font_size: "13sp"



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
            id: upload_aadhar_1
            text: 'Upload aadharcard '
            text_color: 0, 0, 0, 1  # Black text color
            pos_hint: {'center_x': 0.5, 'center_y': 0.37}
            md_bg_color: 0.031, 0.463, 0.91, 1
            on_release: app.file_manager_open('aadhar')
            size_hint: (0.1, 0.01)
            font_size: "12sp"
            size_hint_y: None
            size_hint_x: None

        MDLabel:
            id: aadhar_reg_label
            text: ''
            text_color: 1, 0, 0, 1  # Set text color to red
            halign: "center"
            font_style: "Caption"
            size_hint_y: None
            height: dp(36)     

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
            id: upload_pan_1
            text: 'Upload pancard '
            text_color: 0, 0, 0, 1  # Black text color
            pos_hint: {'center_x': 0.5, 'center_y': 0.37}
            md_bg_color: 0.031, 0.463, 0.91, 1
            on_release: app.file_manager_open('pan')
            size_hint: (0.1, 0.01)
            font_size: "12sp"
            size_hint_y: None
            size_hint_x: None

        MDLabel:
            id: pan_reg_label
            text: ''
            text_color: 1, 0, 0, 1  # Set text color to red
            halign: "center"
            font_style: "Caption"
            size_hint_y: None
            height: dp(36) 
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
                on_release: app.root.ids.screen_manager.current = 'lender_reg_form2'

            MDRectangleFlatButton:
                text: 'Next'
                text_color: 0, 0, 0, 1  # Black text color
                pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                md_bg_color: 0.031, 0.463, 0.91, 1
                on_release: app.root.current = 'LenderScreen3'
<LenderScreen3>:
    BoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(20)


        MDRectangleFlatButton:
            text: 'HOME'
            text_color: 0, 0, 0, 1  # Black text color
            pos_hint: {'center_x': 0.5, 'center_y': 0.3}
            md_bg_color: 0.031, 0.463, 0.91, 1
            pos_hint: {'right': 1, 'top': 1}
            on_release: app.go_home()
            size_hint: (0.1, 0.03)
            font_size: "13sp"



        MDLabel:
            text: 'Lender Registration Form'
            font_size: 25
            halign: 'center'
            bold: True
        MDLabel:
            text: 'Education Details'
            font_size: 25
            halign: 'center'
            bold: True

        MDTextField:
            id: qualification_field
            hint_text: "Select qualification"
            on_touch_down: app.show_qualification_menu() if self.collide_point(*args[1].pos) else None
            size_hint: (None, None)
            readonly: True
            width: 300
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            theme_text_color: "Custom"
            hint_text_color: (0, 0, 0, 1)  # Black hint text color
            text_color: (0, 0, 0, 1)  # Black text color
            helper_text: "Select gender"
            helper_text_mode: "on_focus"
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
                text: 'Back'
                text_color: 0, 0, 0, 1  # Black text color
                pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                md_bg_color: 0.031, 0.463, 0.91, 1
                on_release: app.root.ids.screen_manager.current = 'lender_reg_form2'

            MDRectangleFlatButton:
                text: 'Next'
                text_color: 0, 0, 0, 1  # Black text color
                pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                md_bg_color: 0.031, 0.463, 0.91, 1
                on_release: app.on_next_button1_click()


<LenderScreen_Edu_10th>:
    BoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(20)



        MDRectangleFlatButton:
            text: 'HOME'
            text_color: 0, 0, 0, 1  # Black text color
            pos_hint: {'center_x': 0.5, 'center_y': 0.3}
            md_bg_color: 0.031, 0.463, 0.91, 1
            pos_hint: {'right': 1, 'top': 1}
            on_release: app.go_home()
            size_hint: (0.1, 0.03)
            font_size: "13sp"



        MDLabel:
            text: 'Education Details'
            font_size: 25
            halign: 'center'
            bold: True
        MDLabel:
            text: "Upload 10th class certificate"
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
                on_release: app.root.ids.screen_manager.current = 'lender_reg_edu_form'

            MDRectangleFlatButton:
                text: 'Next'
                text_color: 0, 0, 0, 1  # Black text color
                pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                md_bg_color: 0.031, 0.463, 0.91, 1
                on_release: app.root.ids.screen_manager.current = 'lender_reg_form3'    


'''


class LenderScreen(Screen):
    pass


class LenderScreen1(Screen):
    pass


class LenderScreen2(Screen):
    pass


class LenderScreen3(Screen):
    pass


class LenderScreen_Edu_10th(Screen):
    pass

