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
                on_release: app.root.current = 'LenderScreen1'

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

        Spinner:
            id: spinner_id
            text: "select education details"
            values: ["10th class", "Intermediate", "Bachelors", "Masters", "PHD"]
            multiline:False
            size_hint: (None, None)
            height: 70
            width: 400
            background_color: (0,0,0,0)
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
                on_release: app.root.current = 'LenderScreen2'

            MDRectangleFlatButton:
                text: 'Next'
                text_color: 0, 0, 0, 1  # Black text color
                pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                md_bg_color: 0.031, 0.463, 0.91, 1
                on_press: root.next_pressed(spinner_id.text)


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
                on_release: app.root.current = 'LenderScreen3'
                
            MDRectangleFlatButton:
                text: 'Next'
                text_color: 0, 0, 0, 1  # Black text color
                pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                md_bg_color: 0.031, 0.463, 0.91, 1
                on_release: app.root.current = 'LenderScreen4'

<LenderScreen_Edu_Intermediate>:
    MDRectangleFlatButton:
        text: 'HOME'
        text_color: 0, 0, 0, 1  # Black text color
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        md_bg_color: 0.031, 0.463, 0.91, 1
        pos_hint: {'right': 1, 'top': 1}
        on_release: app.go_home()
        size_hint: (0.1, 0.03)
        font_size: "13sp"

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
                text: 'Education Details'
                font_size: 25
                halign: 'center'
                bold: True
            MDLabel:
                text: "Upload 10th class"
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
                text: "Upload Intermediate/PUC"
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
                    on_release: app.root.current = 'LenderScreen3'

                MDRectangleFlatButton:
                    text: 'Next'
                    text_color: 0, 0, 0, 1  # Black text color
                    pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    on_release: app.root.current = 'LenderScreen4'

<LenderScreen_Edu_Bachelors>:
    MDRectangleFlatButton:
        text: 'HOME'
        text_color: 0, 0, 0, 1  # Black text color
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        md_bg_color: 0.031, 0.463, 0.91, 1
        pos_hint: {'right': 1, 'top': 1}
        on_release: app.go_home()
        size_hint: (0.1, 0.03)
        font_size: "13sp"

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
                text: "Upload 10th class"
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
                text: "Upload Intermediate/PUC"
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
                text: "Upload B.tech/B.E certificate"
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
                    on_release: app.root.current = 'LenderScreen3'
                    
                MDRectangleFlatButton:
                    text: 'Next'
                    text_color: 0, 0, 0, 1  # Black text color
                    pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    on_release: app.root.current = 'LenderScreen4'  

<LenderScreen_Edu_Masters>:
    MDRectangleFlatButton:
        text: 'HOME'
        text_color: 0, 0, 0, 1  # Black text color
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        md_bg_color: 0.031, 0.463, 0.91, 1
        pos_hint: {'right': 1, 'top': 1}
        on_release: app.go_home()
        size_hint: (0.1, 0.03)
        font_size: "13sp"

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
                text: 'Education Details'
                font_size: 25
                halign: 'center'
                bold: True
            MDLabel:
                text: "Upload 10th class"
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
                text: "Upload Intermediate/PUC"
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
                text: "Upload B.tech/B.E"
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
                text: "Upload Masters Certificate"
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
                    on_release: app.root.current = 'LenderScreen3'
                    
                MDRectangleFlatButton:
                    text: 'Next'
                    text_color: 0, 0, 0, 1  # Black text color
                    pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    on_release: app.root.current = 'LenderScreen4'

<LenderScreen_Edu_PHD>:
    MDRectangleFlatButton:
        text: 'HOME'
        text_color: 0, 0, 0, 1  # Black text color
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        md_bg_color: 0.031, 0.463, 0.91, 1
        pos_hint: {'right': 1, 'top': 1}
        on_release: app.go_home()
        size_hint: (0.1, 0.03)
        font_size: "13sp"

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
                text: 'Education Details'
                font_size: 25
                halign: 'center'
                bold: True
            MDLabel:
                text: "Upload 10th class"
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
                text: "Upload Intermediate/PUC"
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
                text: "Upload Btech/B.E"
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
                text: "Upload Mtech"
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
                text: "Upload Phd"
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
                    on_release: app.root.current = 'LenderScreen3'
                    
                MDRectangleFlatButton:
                    text: 'Next'
                    text_color: 0, 0, 0, 1  # Black text color
                    pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    on_release: app.root.current = 'LenderScreen4'
<LenderScreen4>:
    MDRectangleFlatButton:
        text: 'HOME'
        text_color: 0, 0, 0, 1  # Black text color
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        md_bg_color: 0.031, 0.463, 0.91, 1
        pos_hint: {'right': 1, 'top': 1}
        on_release: app.go_home()
        size_hint: (0.1, 0.03)
        font_size: "13sp"
    
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
                text: 'Lender Registration Form'
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
                    on_release: app.root.current = 'LenderScreen4'
    
                MDRectangleFlatButton:
                    text: 'Next'
                    text_color: 0, 0, 0, 1  # Black text color
                    pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    on_release: app.root.current = 'LenderScreen5'
                    
<LenderScreen5>:
    MDRectangleFlatButton:
        text: 'HOME'
        text_color: 0, 0, 0, 1  # Black text color
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        md_bg_color: 0.031, 0.463, 0.91, 1
        pos_hint: {'right': 1, 'top': 1}
        on_release: app.go_home()
        size_hint: (0.1, 0.03)
        font_size: "13sp"

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
                text: 'Lender Registration Form'
                font_size: 25
                halign: 'center'
                bold: True

            Spinner:
                id: spinner_id
                text: "select option"
                values: ["Individual", "Institutional"]
                multiline:False
                size_hint: (None, None)
                height: 70
                width: 330
                background_color: (0,0,0,0)
                background_normal: ''
                canvas.before:
                    Color:
                        rgba: 0.031, 0.463, 0.91, 1
                    RoundedRectangle:
                        size: self.size
                        pos: self.pos
                        radius: [15]
    
    


            MDTextField:
                id: investment
                hint_text: 'Enter investment '
                multiline: False
                helper_text: 'Enter above 10000'
                helper_text_mode: 'on_focus'
                size_hint_y: None
                height: self.minimum_height
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x: None
                width: 300

            MDTextField:
                id: lending_period_field
                multiline: False
                hint_text: "Select one"
                on_focus: if self.focus: app.show_lending_period_menu()
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
                    on_release: app.root.current = 'LenderScreen4'
                    
                MDRectangleFlatButton:
                    text: 'Next'
                    text_color: 0, 0, 0, 1  # Black text color
                    pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    on_release: app.on_next_button_click()
                    
'''


class LenderScreen(Screen):
    pass


class LenderScreen1(Screen):
    pass


class LenderScreen2(Screen):
    pass


class LenderScreen3(Screen):

    def next_pressed(self, id):
        if id == '10th class':
            self.manager.current = 'LenderScreen_Edu_10th'

        elif id == 'Intermediate':
            self.manager.current = 'LenderScreen_Edu_Intermediate'

        elif id == 'Bachelors':
            self.manager.current = 'LenderScreen_Edu_Bachelors'
        elif id == 'Masters':
            self.manager.current = 'LenderScreen_Edu_Masters'
        elif id == 'PHD':
            self.manager.current = 'LenderScreen_Edu_PHD'
        print(id)
class LenderScreen_Edu_10th(Screen):
    pass
class LenderScreen_Edu_Intermediate(Screen):
    pass
class LenderScreen_Edu_Bachelors(Screen):
    pass
class LenderScreen_Edu_Masters(Screen):
    pass
class LenderScreen_Edu_PHD(Screen):
    pass
class LenderScreen4(Screen):
    pass
class LenderScreen5(Screen):
    pass