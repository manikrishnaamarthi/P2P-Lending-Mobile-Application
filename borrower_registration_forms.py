from kivy.core.window import Window
from kivymd.uix.dialog import MDDialog
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivymd.app import MDApp
import sqlite3
from datetime import date
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivymd.uix.pickers import MDDatePicker
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserIconView
from kivymd.uix.filemanager import MDFileManager

Borrower = '''
<BorrowerScreen>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'BorrowerScreen2')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(30)
        padding: dp(30)
        MDLabel:
            text: ""
            size_hint_y: None
            height: dp(50)
        MDLabel:
            text: ""
            size_hint_y: None
            height: dp(50)

        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(50)
            padding: dp(30)
            md_bg_color: 253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1  # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text: 'Borrower Registration Form'
                halign: 'center'
                font_size: "20dp"
                font_name: "Roboto-Bold"               

            MDTextField:
                id: username
                hint_text: 'Enter Full Name'
                halign: 'left'
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                multiline: False
                helper_text: "Enter Valid Name"
                helper_text_mode: 'on_focus'
                font_name: "Roboto-Bold"
                bold: True

            Spinner:
                padding: [dp(10), dp(10)]
                id: gender_id
                text: "Select Gender"
                values: ["Select Gender","Male", "Female", "Others"]
                multiline: False
                size_hint: 1 , None

                background_color: 1, 1 ,1, 0 
                color: 0, 0, 0, 1
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1  
                    Line:
                        width: 0.7
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDTextField:
                id: date_textfield
                hint_text: 'Select Date of Birth'
                halign: 'left'
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                multiline: False
                helper_text: "Select Valid Date of Birth"
                helper_text_mode: 'on_focus'
                font_name: "Roboto-Bold"
                bold: True
                on_focus: root.show_date_picker()

            MDTextField:
                id: mobile_number
                hint_text: ' Enter Mobile No'
                halign: 'left'
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                multiline: False
                helper_text: "Enter Valid Mobile No"
                helper_text_mode: 'on_focus'
                font_name: "Roboto-Bold"
                bold: True
                input_type: 'number'  
                on_touch_down: root.on_mobile_number_touch_down()

            BoxLayout:
                orientation: 'vertical'
                padding: "40dp"

                MDRaisedButton:
                    text: 'Next'
                    text_color: 0, 0, 0, 1  
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    size_hint: 1, None
                    height: "50dp"
                    on_release: root.add_data(username.text, gender_id.text, date_textfield.text, mobile_number.text)

<BorrowerScreen1>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'BorrowerScreen2')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(30)
        padding: dp(30)
        MDLabel:
            text: ""
            size_hint_y: None
            height: dp(50)
        MDLabel:
            text: ""
            size_hint_y: None
            height: dp(50)

        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(50)
            padding: dp(30)
            md_bg_color: 253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1  # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text: 'Borrower Registration Form'
                halign: 'center'
                font_size: "20dp"
                font_name: "Roboto-Bold"               

            MDTextField:
                id: alternate_mobile_number
                hint_text: ' Enter Alternate Mobile No'
                halign: 'left'
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                multiline: False
                helper_text: "Enter Valid Alternate Mobile No"
                helper_text_mode: 'on_focus'
                font_name: "Roboto-Bold"
                bold: True
                input_type: 'number'
                on_touch_down: root.on_mobile_number_touch_down()

            MDTextField:
                id: alternate_email
                hint_text: ' Enter Alternate Email ID'
                halign: 'left'
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                multiline: False
                helper_text: "Enter Valid Alternate Email ID"
                helper_text_mode: 'on_focus'
                font_name: "Roboto-Bold"
                bold: True
                input_type: 'number'
                on_touch_down: root.on_mobile_number_touch_down()

            BoxLayout:
                orientation: 'horizontal'
                padding: "10dp"
                spacing: "10dp"
                size_hint: None, None
                size: dp(200), dp(50)  # Adjust size as needed
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}

                canvas:
                    Color:
                        rgba: 0, 0, 0, 1
                    Line:
                        width: 0.4
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

                MDIconButton:
                    icon: 'upload'
                    id: upload_icon1
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1
                    size_hint_x: None
                    width: dp(24)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    on_release: root.file_manager_open_1()

                MDLabel:
                    id: upload_label1
                    text: 'Upload Profile Image'
                    halign: 'left'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_y: None
                    height: dp(36)
                    valign: 'middle'  # Align the label text vertically in the center
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            GridLayout:
                cols: 1
                spacing: dp(30)
                padding: dp(20)
                pos_hint: {'center_x': 0.50, 'center_y': 0.5}
                size_hint: 1, None
                height: "50dp"

                MDRaisedButton:
                    text: "Next"
                    on_release: root.add_data(alternate_mobile_number.text, alternate_email.text)
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    size_hint: 1, None
                    height: "50dp"
        Label:
            text: ''

<BorrowerScreen2>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'BorrowerScreen2')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(30)
        padding: dp(30)
        MDLabel:
            text: ""
            size_hint_y: None
            height: dp(50)
        MDLabel:
            text: ""
            size_hint_y: None
            height: dp(50)

        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(50)
            padding: dp(30)
            md_bg_color: 253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1  # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text: 'Borrower Registration Form'
                halign: 'center'
                font_size: "20dp"
                font_name: "Roboto-Bold"               

            MDTextField:
                id: aadhar_number
                hint_text: 'Enter Gov ID1 Number '
                multiline: False
                helper_text: "Enter Valid Gov ID1 No"
                helper_text_mode: 'on_focus'
                halign: 'left'
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                font_name: "Roboto-Bold"
                bold: True
    
            BoxLayout:
                orientation: 'horizontal'
                padding: "10dp"
                spacing: "10dp"
                size_hint: None, None
                size: dp(200), dp(50)  # Adjust size as needed
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    
                canvas:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.4  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)
    
                MDIconButton:
                    icon: 'upload'
                    id: upload_icon2
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_x: None
                    width: dp(24)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    on_release: root.file_manager_open_1()
    
                MDLabel:
                    id: upload_label1
                    text: 'Upload Gov ID1'
                    halign: 'left'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_y: None
                    height: dp(36)
                    valign: 'middle'  # Align the label text vertically in the center
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    
            MDTextField:
                id: pan_number
                hint_text: 'Enter Gov ID2 Number '
                multiline: False
                helper_text: "Enter Valid Gov ID2 No"
                helper_text_mode: 'on_focus'
                halign: 'left'
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                font_name: "Roboto-Bold"
                bold: True
    
            BoxLayout:
                orientation: 'horizontal'
                padding: "10dp"
                spacing: "10dp"
                size_hint: None, None
                size: dp(200), dp(50)  # Adjust size as needed
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    
                canvas:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.4  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)
    
                MDIconButton:
                    icon: 'upload'
                    id: upload_icon3
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1
                    size_hint_x: None
                    width: dp(24)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    on_release: root.file_manager_open_2()
    
                MDLabel:
                    id: upload_label2
                    text: 'Upload Gov ID2'
                    halign: 'left'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1
                    size_hint_y: None
                    height: dp(36)
                    valign: 'middle'
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    
            GridLayout:
                cols: 1
                spacing: dp(30)
                padding: dp(20)
                pos_hint: {'center_x': 0.50, 'center_y': 0.5}
                size_hint: 1, None
                height: "50dp"
    
                MDRaisedButton:
                    text: "Next"
                    on_release: root.add_data(aadhar_number.text, pan_number.text)
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    size_hint: 1, None
                    height: "50dp"
            Label:
                text: ""

<BorrowerScreen3>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'BorrowerScreen2')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(30)
        padding: dp(30)
        MDLabel:
            text: ""
            size_hint_y: None
            height: dp(50)
        MDLabel:
            text: ""
            size_hint_y: None
            height: dp(50)

        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(50)
            padding: dp(30)
            md_bg_color: 253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1  # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text: 'Borrower Registration Form'
                halign: 'center'
                font_size: "20dp"
                font_name: "Roboto-Bold"               

            MDLabel:
                text: 'Education Details'
                halign: 'center'
                bold: True

            Spinner:
                id: spinner_id
                text: "Please Select Education Details"
                values: ["Select Education Details", "10th class", "Intermediate", "Bachelors", "Masters", "PHD"]
                multiline: False
                size_hint_y: None
                background_color: (0, 0, 0, 0)
                background_normal: ''
                color: 0, 0, 0, 1
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.7  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            GridLayout:
                cols: 1
                spacing: dp(30)

                MDRectangleFlatButton:
                    text: "Next"
                    on_press: root.next_pressed(spinner_id.text)
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"

            MDLabel:
                text: ""

<BorrowerScreen_Edu_10th>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'BorrowerScreen3')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(30)
        padding: dp(30)
        MDLabel:
            text: ""
            size_hint_y: None
            height: dp(50)

        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(50)
            padding: dp(30)
            md_bg_color: 253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1  # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text: 'Education Details'
                halign: 'center'
                bold: True
                size_hint_y: None
                height: dp(50)

            MDLabel:
                text: "Upload 10th class certificate"
                halign: 'center'
                bold: True
                size_hint_y: None
                height: dp(50)

            BoxLayout:
                orientation: 'horizontal'
                padding: "10dp"
                spacing: "10dp"
                size_hint: None, None
                size: dp(200), dp(50)  # Adjust size as needed
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                canvas:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.4  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

                MDIconButton:
                    icon: 'upload'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_x: None
                    width: dp(24)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    on_release: root.upload_1()

                MDLabel:
                    id: upload_label1
                    text: 'Upload Certificate'
                    halign: 'left'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_y: None
                    height: dp(36)
                    valign: 'middle'  # Align the label text vertically in the center
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            GridLayout:
                cols: 1
                spacing: dp(30)

                MDRectangleFlatButton:
                    text: "Next"
                    on_release: app.root.current = 'BorrowerScreen4'
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"

<BorrowerScreen_Edu_Intermediate>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'BorrowerScreen3')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(30)
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
                halign: 'center'
                bold: True

            MDLabel:
                text: "Upload 10th class"
                halign: 'center'
                bold: True

            BoxLayout:
                orientation: 'horizontal'
                padding: "10dp"
                spacing: "10dp"
                size_hint: None, None
                size: dp(200), dp(50)  # Adjust size as needed
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                canvas:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.4  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

                MDIconButton:
                    icon: 'upload'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_x: None
                    width: dp(24)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    on_release: root.upload_1()

                MDLabel:
                    id: upload_label1
                    text: 'Upload Certificate'
                    halign: 'left'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_y: None
                    height: dp(36)
                    valign: 'middle'  # Align the label text vertically in the center
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            MDLabel:
                text: "Upload Intermediate/PUC"
                halign: 'center'
                bold: True

            BoxLayout:
                orientation: 'horizontal'
                padding: "10dp"
                spacing: "10dp"
                size_hint: None, None
                size: dp(200), dp(50)  # Adjust size as needed
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                canvas:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.4  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

                MDIconButton:
                    icon: 'upload'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_x: None
                    width: dp(24)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    on_release: root.upload_2()

                MDLabel:
                    id: upload_label2
                    text: 'Upload Certificate'
                    halign: 'left'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_y: None
                    height: dp(36)
                    valign: 'middle'  # Align the label text vertically in the center
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            GridLayout:
                cols: 1
                spacing: dp(30)
                padding: [0, "30dp", 0, 0]

                MDRectangleFlatButton:
                    text: "Next"
                    on_release: app.root.current = 'BorrowerScreen4'
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"

<BorrowerScreen_Edu_Bachelors>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'BorrowerScreen3')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title"

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
                text: "Upload 10th class Certificate"
                halign: 'center'
                bold: True

            BoxLayout:
                orientation: 'horizontal'
                padding: "10dp"
                spacing: "10dp"
                size_hint: None, None
                size: dp(200), dp(50)  # Adjust size as needed
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                canvas:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.4  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

                MDIconButton:
                    icon: 'upload'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_x: None
                    width: dp(24)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    on_release: root.upload_1()

                MDLabel:
                    id: upload_label1
                    text: 'Upload Certificate'
                    halign: 'left'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_y: None
                    height: dp(36)
                    valign: 'middle'  # Align the label text vertically in the center
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            MDLabel:
                text: "Upload Intermediate/PUC Certificate"
                halign: 'center'
                bold: True

            BoxLayout:
                orientation: 'horizontal'
                padding: "10dp"
                spacing: "10dp"
                size_hint: None, None
                size: dp(200), dp(50)  # Adjust size as needed
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                canvas:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.4  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

                MDIconButton:
                    icon: 'upload'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_x: None
                    width: dp(24)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    on_release: root.upload_2()

                MDLabel:
                    id: upload_label2
                    text: 'Upload Certificate'
                    halign: 'left'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_y: None
                    height: dp(36)
                    valign: 'middle'  # Align the label text vertically in the center
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            MDLabel:
                text: "Upload B.tech/B.E certificate"
                halign: 'center'
                bold: True

            BoxLayout:
                orientation: 'horizontal'
                padding: "10dp"
                spacing: "10dp"
                size_hint: None, None
                size: dp(200), dp(50)  # Adjust size as needed
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                canvas:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.4  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

                MDIconButton:
                    icon: 'upload'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_x: None
                    width: dp(24)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    on_release: root.upload_3()

                MDLabel:
                    id: upload_label3
                    text: 'Upload Certificate'
                    halign: 'left'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_y: None
                    height: dp(36)
                    valign: 'middle'  # Align the label text vertically in the center
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            GridLayout:
                cols: 1
                spacing: dp(30)
                padding: [0, "30dp", 0, 0]

                MDRectangleFlatButton:
                    text: "Next"
                    on_release: app.root.current = 'BorrowerScreen4'
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"

<BorrowerScreen_Edu_Masters>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'BorrowerScreen3')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title

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
                halign: 'center'
                bold: True
            MDLabel:
                text: "Upload 10th class Certificate"
                halign: 'center'
                bold: True

            BoxLayout:
                orientation: 'horizontal'
                padding: "10dp"
                spacing: "10dp"
                size_hint: None, None
                size: dp(200), dp(50)  # Adjust size as needed
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                canvas:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.4  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

                MDIconButton:
                    icon: 'upload'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_x: None
                    width: dp(24)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    on_release: root.upload_1()

                MDLabel:
                    id: upload_label1
                    text: 'Upload Certificate'
                    halign: 'left'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_y: None
                    height: dp(36)
                    valign: 'middle'  # Align the label text vertically in the center
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            MDLabel:
                text: "Upload Intermediate/PUC Certificate"
                halign: 'center'
                bold: True

            BoxLayout:
                orientation: 'horizontal'
                padding: "10dp"
                spacing: "10dp"
                size_hint: None, None
                size: dp(200), dp(50)  # Adjust size as needed
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                canvas:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.4  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

                MDIconButton:
                    icon: 'upload'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_x: None
                    width: dp(24)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    on_release: root.upload_2()

                MDLabel:
                    id: upload_label2
                    text: 'Upload Certificate'
                    halign: 'left'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_y: None
                    height: dp(36)
                    valign: 'middle'  # Align the label text vertically in the center
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            MDLabel:
                text: "Upload B.tech/B.E Certificate"
                halign: 'center'
                bold: True

            BoxLayout:
                orientation: 'horizontal'
                padding: "10dp"
                spacing: "10dp"
                size_hint: None, None
                size: dp(200), dp(50)  # Adjust size as needed
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                canvas:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.4  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

                MDIconButton:
                    icon: 'upload'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_x: None
                    width: dp(24)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    on_release: root.upload_3()

                MDLabel:
                    id: upload_label3
                    text: 'Upload Certificate'
                    halign: 'left'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_y: None
                    height: dp(36)
                    valign: 'middle'  # Align the label text vertically in the center
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            MDLabel:
                text: "Upload Masters Certificate"
                halign: 'center'
                bold: True

            BoxLayout:
                orientation: 'horizontal'
                padding: "10dp"
                spacing: "10dp"
                size_hint: None, None
                size: dp(200), dp(50)  # Adjust size as needed
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                canvas:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.4  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

                MDIconButton:
                    icon: 'upload'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_x: None
                    width: dp(24)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    on_release: root.upload_4()

                MDLabel:
                    id: upload_label4
                    text: 'Upload Certificate'
                    halign: 'left'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_y: None
                    height: dp(36)
                    valign: 'middle'  # Align the label text vertically in the center
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            GridLayout:
                cols: 1
                spacing: dp(30)
                padding: [0, "30dp", 0, 0]

                MDRectangleFlatButton:
                    text: "Next"
                    on_release: app.root.current = 'BorrowerScreen4'
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"

<BorrowerScreen_Edu_PHD>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'BorrowerScreen3')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title

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
                halign: 'center'
                bold: True
            MDLabel:
                text: "Upload 10th Class Certificate"
                halign: 'center'
                bold: True

            BoxLayout:
                orientation: 'horizontal'
                padding: "10dp"
                spacing: "10dp"
                size_hint: None, None
                size: dp(200), dp(50)  # Adjust size as needed
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                canvas:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.4  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

                MDIconButton:
                    icon: 'upload'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_x: None
                    width: dp(24)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    on_release: root.upload_1()

                MDLabel:
                    id: upload_label1
                    text: 'Upload Certificate'
                    halign: 'left'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_y: None
                    height: dp(36)
                    valign: 'middle'  # Align the label text vertically in the center
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            MDLabel:
                text: "Upload Intermediate/PUC Certificate"
                halign: 'center'
                bold: True

            BoxLayout:
                orientation: 'horizontal'
                padding: "10dp"
                spacing: "10dp"
                size_hint: None, None
                size: dp(200), dp(50)  # Adjust size as needed
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                canvas:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.4  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

                MDIconButton:
                    icon: 'upload'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_x: None
                    width: dp(24)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    on_release: root.upload_2()

                MDLabel:
                    id: upload_label2
                    text: 'Upload Certificate'
                    halign: 'left'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_y: None
                    height: dp(36)
                    valign: 'middle'  # Align the label text vertically in the center
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            MDLabel:
                text: "Upload Btech/B.E Certificate"
                halign: 'center'
                bold: True

            BoxLayout:
                orientation: 'horizontal'
                padding: "10dp"
                spacing: "10dp"
                size_hint: None, None
                size: dp(200), dp(50)  # Adjust size as needed
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                canvas:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.4  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

                MDIconButton:
                    icon: 'upload'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_x: None
                    width: dp(24)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    on_release: root.upload_3()

                MDLabel:
                    id: upload_label3
                    text: 'Upload Certificate'
                    halign: 'left'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_y: None
                    height: dp(36)
                    valign: 'middle'  # Align the label text vertically in the center
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            MDLabel:
                text: "Upload Masters Certificate"
                halign: 'center'
                bold: True

            BoxLayout:
                orientation: 'horizontal'
                padding: "10dp"
                spacing: "10dp"
                size_hint: None, None
                size: dp(200), dp(50)  # Adjust size as needed
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                canvas:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.4  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

                MDIconButton:
                    icon: 'upload'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_x: None
                    width: dp(24)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    on_release: root.upload_4()

                MDLabel:
                    id: upload_label4
                    text: 'Upload Certificate'
                    halign: 'left'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_y: None
                    height: dp(36)
                    valign: 'middle'  # Align the label text vertically in the center
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            MDLabel:
                text: "Upload PHD Certificate"
                halign: 'center'
                bold: True

            BoxLayout:
                orientation: 'horizontal'
                padding: "10dp"
                spacing: "10dp"
                size_hint: None, None
                size: dp(200), dp(50)  # Adjust size as needed
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                canvas:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.4  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

                MDIconButton:
                    icon: 'upload'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_x: None
                    width: dp(24)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    on_release: root.upload_5()

                MDLabel:
                    id: upload_label5
                    text: 'Upload Certificate'
                    halign: 'left'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_y: None
                    height: dp(36)
                    valign: 'middle'  # Align the label text vertically in the center
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            GridLayout:
                cols: 1
                spacing: dp(30)
                padding: [0, "30dp", 0, 0]

                MDRectangleFlatButton:
                    text: "Next"
                    on_release: app.root.current = 'BorrowerScreen4'
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"

<BorrowerScreen4>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'BorrowerScreen3')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(30)
        padding: dp(30)

        MDLabel:
            text:""
            size_hint_y: None
            height:dp(50)

        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(50)
            padding: dp(30)
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text: 'Borrower Registration Form Address'
                font_size: dp(20)
                font_name: "Roboto-Bold"
                halign: 'center'
                bold: True
    
            MDLabel:
                text: 'Address'
                halign: 'center'
                bold: True
    
            MDTextField:
                id: country
                hint_text: 'Enter Country Name'
                multiline: False
                helper_text_mode: 'on_focus'
    
            MDTextField:
                id: state
                hint_text: 'Enter State Name'
                multiline: False
                helper_text_mode: 'on_focus'
                size_hint_y: None
    
            MDTextField:
                id: city
                hint_text: 'Enter City Name'
                multiline: False
                helper_text_mode: 'on_focus'
                size_hint_y: None  
    
            MDTextField:
                id: zip_code
                hint_text: 'Enter postal/zipcode '
                multiline: False
                helper_text_mode: 'on_focus'
                size_hint_y: None  
                input_type: 'number'  
                on_touch_down: root.on_mobile_number_touch_down()
    
            MDTextField:
                id: street_address
                hint_text: 'Enter Street Name'
                multiline: False
                helper_text: 'Enter valid address'
                helper_text_mode: 'on_focus'
    
            GridLayout:
                cols: 1
                spacing: dp(30)
                padding: dp(20)
                pos_hint: {'center_x': 0.50, 'center_y': 0.5}
                size_hint: 1, None
                height: "50dp"
    
                MDRaisedButton:
                    text: "Next"
                    on_release: root.add_data(street_address.text, city.text, zip_code.text, state.text, country.text)
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"
    
            Label:
                text: ""
    
<BorrowerScreen5>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'BorrowerScreen4')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(50)

        MDLabel:
            text:""
            size_hint_y: None
            height:dp(40)

        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(10)
            padding: dp(30)  # Reduce the top padding
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text: 'Borrower Registration Form Father Information'
                font_size:dp(25)
                halign: 'center'
                font_name: "Roboto-Bold"
    
            MDTextField:
                id: father_name
                hint_text: 'Enter Father Name'
                helper_text: 'Enter valid Father Name'
                multiline: False
                helper_text_mode: 'on_focus'
                halign: 'left'
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                font_name: "Roboto-Bold"
                bold: True
    
            MDTextField:
                id: father_age
                hint_text: 'Enter Father Age'
                helper_text: 'Enter valid Father Age'
                multiline: False
                helper_text_mode: 'on_focus'
                halign: 'left'
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                font_name: "Roboto-Bold"
                bold: True
                input_type: 'number'  
                on_touch_down: root.on_father_age_touch_down()
    
            MDTextField:
                id: father_occupation
                hint_text: 'Enter Father Occupation'
                helper_text: 'Enter valid Father Occupation'
                multiline: False
                helper_text_mode: 'on_focus'
                halign: 'left'
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                font_name: "Roboto-Bold"
                bold: True
    
            MDTextField:
                id: father_ph_no
                hint_text: 'Enter Father Phone NO'
                multiline: False
                helper_text: 'Enter valid PH No'
                helper_text_mode: 'on_focus'
                halign: 'left'
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                font_name: "Roboto-Bold"
                bold: True
                input_type: 'number'  
                on_touch_down: root.on_father_ph_no_touch_down()
    
            GridLayout:
                cols: 1
                spacing:dp(30)
                padding:dp(20)
                pos_hint: {'center_x': 0.50, 'center_y': 0.5}
                size_hint: 1, None
                height: "50dp"
    
                MDRaisedButton:
                    text: "Next"
                    on_release: root.add_data(father_name.text, father_age.text, father_occupation.text, father_ph_no.text)
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    size_hint: 1, None
                    height: "50dp"
    
            Label:
                text: ""

<BorrowerScreen6>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'BorrowerScreen5')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(50)

        MDLabel:
            text:""
            size_hint_y: None
            height:dp(40)

        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(10)
            padding: dp(30)  # Reduce the top padding
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text: 'Borrower Registration Form Mother Information'
                font_size:dp(25)
                halign: 'center'
                font_name: "Roboto-Bold" 
                bold: True
    
            MDTextField:
                id: mother_name
                hint_text: 'Enter Mother Name'
                helper_text: 'Enter Valid Mother Name'
                multiline: False
                helper_text_mode: 'on_focus'
                halign: 'left'
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                font_name: "Roboto-Bold"
                bold: True
    
            MDTextField:
                id: mother_age
                hint_text: 'Enter Mother Age'
                helper_text: 'Enter Valid Mother Age'
                multiline: False
                helper_text_mode: 'on_focus'
                halign: 'left'
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                font_name: "Roboto-Bold"
                bold: True
                input_type: 'number'  
                on_touch_down: root.on_mother_age_touch_down()
    
            MDTextField:
                id: mother_occupation
                hint_text: 'Enter Mother Occupation'
                helper_text: 'Enter Valid Mother Occupation'
                multiline: False
                helper_text_mode: 'on_focus'
                halign: 'left'
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                font_name: "Roboto-Bold"
                bold: True
    
            MDTextField:
                id: mother_ph_no
                hint_text: 'Enter Mother Phone No'
                helper_text: 'Enter Valid Mother Phone No'
                helper_text_mode: 'on_focus'
                halign: 'left'
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                font_name: "Roboto-Bold"
                bold: True
                input_type: 'number'  
                on_touch_down: root.on_mother_ph_no_touch_down()
    
            GridLayout:
                cols: 2
                spacing:dp(30)
                padding:dp(20)
                pos_hint: {'center_x': 0.50, 'center_y': 0.5}
                size_hint: 1, None
                height: "50dp"
    
                MDRaisedButton:
                    text: "Back"
                    on_release: app.root.current = 'BorrowerScreen4'
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    theme_text_color: 'Custom'
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
    
                MDRaisedButton:
                    text: "Next"
                    on_release: root.add_data(mother_name.text, mother_age.text, mother_occupation.text, mother_ph_no.text)
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    size_hint: 1, None
                    height: "50dp"
    
            Label:
                text: ""

<BorrowerScreen7>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'BorrowerScreen6')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(50)

        MDLabel:
            text:""
            size_hint_y: None
            height:dp(40)

        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(10)
            padding: dp(30)  # Reduce the top padding
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text: 'Borrower Registration Form Profession Information'
                font_size:dp(25)
                halign: 'center'
                bold: True
    
            Spinner:
                id: spinner_id
                text: "Select Proficient type"
                values: ["Select Proficient type", "Student", "Employee", "Business"]
                multiline: False
                size_hint: 1 , None
                bold: True
                background_color: 1, 1 ,1, 0 
                color: 0, 0, 0, 1
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1
                    Line:
                        width: 0.7  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)
    
            GridLayout:
                cols: 1
                spacing: dp(30)
                padding: dp(20)
                pos_hint: {'center_x': 0.50, 'center_y': 0.5}
                size_hint: 1, None
                height: "50dp"
    
                MDRaisedButton:
                    text: "Next"
                    on_press: root.add_data(spinner_id.text)
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    size_hint: 1, None
                    height: "50dp"
    
            Label:
                text: ""
    
<BorrowerScreen8>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'BorrowerScreen7')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(50)

        MDLabel:
            text:""
            size_hint_y: None
            height:dp(40)

        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(10)
            padding: dp(30)  # Reduce the top padding
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text: 'STUDENT TYPE'
                font_size:dp(20)
                halign: 'center'
                font_name: "Roboto-Bold"
                bold: True
    
            MDTextField:
                id: collage_name
                hint_text: 'Enter Collage Name '
                halign: 'left'
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                multiline: False
                helper_text: 'Enter Valid Collage Name'
                helper_text_mode: 'on_focus'
                font_name: "Roboto-Bold"
                bold: True
    
            MDTextField:
                id: collage_id
                hint_text: 'Enter Collage ID'
                halign: 'left'
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                multiline: True
                helper_text: "Enter valid Collage ID"
                helper_text_mode: 'on_focus'
                font_name: "Roboto-Bold"
                bold: True
    
            BoxLayout:
                orientation: 'horizontal'
                padding: "10dp"
                spacing: "10dp"
                size_hint: None, None
                size: dp(200), dp(50)  # Adjust size as needed
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    
                canvas:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.4  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)
    
                MDIconButton:
                    icon: 'upload'
                    id: upload_icon4
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_x: None
                    width: dp(24)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    on_release: root.file_manager_open_1()
    
                MDLabel:
                    id: upload_label2
                    text: 'Upload Collage proof'
                    halign: 'left'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_y: None
                    height: dp(36)
                    valign: 'middle'  # Align the label text vertically in the center
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    
            MDTextField:
                id:  college_address
                hint_text: 'Enter College Address'
                halign: 'left'
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                multiline: False
                helper_text: 'Enter valid College Address'
                helper_text_mode: 'on_focus'
                font_name: "Roboto-Bold"
                bold: True
    
            GridLayout:
                cols: 1
                spacing: dp(30)
                padding: dp(20)
                pos_hint: {'center_x': 0.50, 'center_y': 0.5}
                size_hint: 1, None
                height: "50dp"
    
                MDRaisedButton:
                    text: "Next"
                    on_release: root.add_data(collage_name.text, college_address.text, collage_id.text)
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    size_hint: 1, None
                    height: "50dp"
    
            Label:
                text: ""
    
<BorrowerScreen9>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'BorrowerScreen7')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(50)

        MDLabel:
            text:""
            size_hint_y: None
            height:dp(40)

        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(10)
            padding: dp(30)  # Reduce the top padding
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text: 'Business Type'
                font_size:dp(25)
                halign: 'center'
                bold: True
    
            MDLabel:
                text: 'STEP-1'
                font_size:dp(25)
                halign: 'center'
                bold: True
    
            MDTextField:
                id: business_name
                hint_text: 'Enter Business Name '
                halign: 'left'
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                multiline: False
                helper_text: "Enter valid Business Name"
                helper_text_mode: 'on_focus'
                font_name: "Roboto-Bold"
                bold: True
                markup: True
    
            MDTextField:
                id: business_location
                hint_text: 'Enter Business Location'
                halign: 'left'
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                multiline: False
                helper_text: "Enter valid Business Location"
                helper_text_mode: 'on_focus'
                font_name: "Roboto-Bold"
                bold: True
                markup: True
    
            MDTextField:
                id:  business_address
                hint_text: 'Enter Business Address'
                halign: 'left'
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                multiline: False
                helper_text: "Enter valid Business Address"
                helper_text_mode: 'on_focus'
                font_name: "Roboto-Bold"
                bold: True
                markup: True
    
            GridLayout:
                cols: 1
                spacing: dp(30)
                padding: dp(20)
                pos_hint: {'center_x': 0.50, 'center_y': 0.5}
                size_hint: 1, None
                height: "50dp"
    
                MDRaisedButton:
                    text: "Next"
                    on_release: root.add_data(business_name.text, business_location.text, business_address.text)
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    size_hint: 1, None
                    height: "50dp"
    
            Label:
                text: ""

<BorrowerScreen10>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'BorrowerScreen7')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(50)
        MDLabel:
            text:""
            size_hint_y: None
            height:dp(40)
        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(10)
            padding: dp(30)  # Reduce the top padding
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text: 'STEP-2'
                font_size:dp(20)
                halign: 'center'
                bold: True
    
            MDTextField:
                id: landmark
                hint_text: 'Enter LandMark '
                halign: 'left'
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                multiline: False
                helper_text: "Enter Valid LandMark"
                helper_text_mode: 'on_focus'
                font_name: "Roboto-Bold"
                bold: True
    
            MDTextField:
                id: business_type
                hint_text: 'Enter Business Type'
                halign: 'left'
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                multiline: False
                helper_text: "Enter valid Business Type"
                helper_text_mode: 'on_focus'
                font_name: "Roboto-Bold"
                bold: True
    
            Spinner:
                id: no_of_employees_working
                text: "No of Employees Working"
                values: ["No of Employees Working","<50", "50-100", "100-150", "150-200", ">200"]
                multiline: False
                size_hint: 1 , None
                background_color: 1, 1 ,1, 0 
                color: 0, 0, 0, 1
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1  
                    Line:
                        width: 0.7  
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)
    
            MDTextField:
                id: reg_office_address
                hint_text: 'Enter Registered Office Address '
                halign: 'left'
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                multiline: False
                helper_text: "Enter valid Registration Office Address"
                helper_text_mode: 'on_focus'
                font_name: "Roboto-Bold"
                bold: True
                markup: True
    
            MDTextField:
                id: year_of_estd
                hint_text: 'Enter Year of Estd'
                halign: 'left'
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                multiline: False
                helper_text: "Enter valid Year of Estd"
                helper_text_mode: 'on_focus'
                font_name: "Roboto-Bold"
                bold: True
    
            GridLayout:
                cols: 1
                spacing:dp(30)
                padding:dp(20)
                pos_hint: {'center_x': 0.50, 'center_y': 0.5}
                size_hint: 1, None
                height: "50dp"
    
                MDRaisedButton:
                    text: "Next"
                    on_release: root.add_data(landmark.text,business_type.text,no_of_employees_working.text,reg_office_address.txt,year_of_estd.text)
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    size_hint: 1, None
                    height: "50dp"
            Label:
                text: ""

<BorrowerScreen11>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'BorrowerScreen7')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(50)
        MDLabel:
            text:""
            size_hint_y: None
            height:dp(40)
        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(10)
            padding: dp(30)  # Reduce the top padding
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text: 'Step-3'
                font_size:dp(20)
                halign: 'center'
                bold: True
    
            MDTextField:
                id: industry_type
                hint_text: 'Enter Industry Type '
                halign: 'left'
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                multiline: False
                helper_text: "Enter valid Industry Type"
                helper_text_mode: 'on_focus'
                font_name: "Roboto-Bold"
                bold: True
    
            MDTextField:
                id: last_six_months_turnover
                hint_text: 'Enter Last 6 Months Turnover'
                halign: 'left'
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                multiline: False
                helper_text: "Enter valid 6 months Turnover"
                helper_text_mode: 'on_focus'
                font_name: "Roboto-Bold"
                bold: True
                input_type: 'number'  
                on_touch_down: root.on_last_six_months_turnover_touch_down()
    
            MDLabel:
                text: "Last 6 months Bank Statements"
                font_size:dp(22)
                halign: 'center'
    
            BoxLayout:
                orientation: 'horizontal'
                padding: "10dp"
                spacing: "10dp"
                size_hint: None, None
                size: dp(200), dp(50)  # Adjust size as needed
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    
                canvas:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.4  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)
    
                MDIconButton:
                    icon: 'upload'
                    id: upload_icon5
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_x: None
                    width: dp(24)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    on_release: root.file_manager_open_1()
    
                MDLabel:
                    id: upload_label1
                    text: 'Upload 6M statement proof'
                    halign: 'left'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_y: None
                    height: dp(36)
                    valign: 'middle'  # Align the label text vertically in the center
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    
    
            GridLayout:
                cols: 1
                spacing:dp(30)
                padding:dp(20)
                pos_hint: {'center_x': 0.50, 'center_y': 0.5}
                size_hint: 1, None
                height: "50dp"
    
                MDRaisedButton:
                    text: "Next"
                    on_release: root.add_data(industry_type.text,last_six_months_turnover.text)
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    size_hint: 1, None
                    height: "50dp"
            Label:
                text: ""

<BorrowerScreen12>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'BorrowerScreen7')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(50)
        MDLabel:
            text:""
            size_hint_y: None
            height:dp(40)
        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(10)
            padding: dp(30)  # Reduce the top padding
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text: 'Employment Details'
                font_size:dp(25)
                halign: 'center'
                bold: True
            Spinner:
                id: spinner1
                text: "Please Select Employment Type"
                values: ["Employment Type","Full-Time", "Part-Time","Contract","Freelance","Intern"]
                multiline:False
                size_hint_y: None
                background_color: 0,0,0,0
                background_normal: ''
                color: 0,0,0,1
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.7  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)
    
    
            MDTextField:              
                id:company_name
                hint_text: 'Enter company name'
                multiline: False                        
                helper_text_mode: 'on_focus'
                size_hint_y: None

            Spinner:
                id: spinner2
                text: "Please Select Organisation Type"
                values: ["Select Organisation Type","Cooperation","Partnership","Sole proprietorship","Hierarchical Organization"]
                multiline:False
                size_hint_y: None
                background_color: 0,0,0,0
                background_normal: ''
                color: 0,0,0,1
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.7  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)


            GridLayout:
                cols: 1
                spacing:dp(30)
                padding: [0, "30dp", 0, 0]


                MDRaisedButton:
                    text: "Next"
                    on_release: root.add_data(spinner1.text, company_name.text, spinner2.text)
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"

<BorrowerScreen13>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'BorrowerScreen7')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(50)

        MDLabel:
            text:""
            size_hint_y: None
            height: dp(40)

        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(10)
            padding: dp(30)  # Reduce the top padding
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text: 'Employment Details'
                halign: 'center'
                font_size: "20dp"
                font_name: "Roboto-Bold"

            MDTextField:              
                id:company_address
                hint_text: 'Enter company address'
                multiline: False                        
                helper_text_mode: 'on_focus'
                size_hint_y: None

            MDTextField:              
                id:company_pincode
                hint_text: 'Enter Company Pincode'
                multiline: False                        
                helper_text_mode: 'on_focus'
                size_hint_y: None
                input_type: 'number'  
                on_touch_down: root.on_company_pincode_touch_down()

            MDTextField:              
                id:company_country
                hint_text: 'Enter Company Country'
                multiline: False                        
                helper_text_mode: 'on_focus'
                size_hint_y: None

            MDTextField:              
                id:landmark
                hint_text: 'Enter landmark'
                multiline: False                        
                helper_text_mode: 'on_focus'
                size_hint_y: None

            MDTextField:              
                id:business_number
                hint_text: 'Enter Business Phone Number'
                multiline: False                        
                helper_text_mode: 'on_focus'
                size_hint_y: None
                input_type: 'number'  
                on_touch_down: root.on_business_number_touch_down()

            GridLayout:
                cols: 1
                spacing: dp(30)
                padding: [0, "30dp", 0, 0]

                MDRaisedButton:
                    text: "Next"
                    on_release: root.add_data(company_address.text, company_pin_code.text, company_country.text, landmark.text, business_phone_number.text)
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"

<BorrowerScreen14>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'BorrowerScreen13')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(50)

        MDLabel:
            text:""
            size_hint_y: None
            height: dp(40)

        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(10)
            padding: dp(30)  # Reduce the top padding
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text: 'Employment Details'
                font_size: dp(25)
                halign: 'center'
                bold: True   

            MDTextField:              
                id: annual_salary
                hint_text: 'Enter Annual Salary'
                halign: 'left'
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                multiline: False
                helper_text:  "Enter Valid Annual Salary"
                helper_text_mode: 'on_focus'
                font_name: "Roboto-Bold"
                bold: True
                input_type: 'number'  
                on_touch_down: root.on_annual_salary_touch_down()

            MDTextField:              
                id: designation
                hint_text: 'Enter Designation'
                halign: 'left'
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                multiline: False
                helper_text: "Enter Valid Designation"
                helper_text_mode: 'on_focus'
                font_name: "Roboto-Bold"
                bold: True

            MDLabel:
                text: "Upload Employee ID"
                font_size: dp(18)
                halign: 'center'

            BoxLayout:
                orientation: 'horizontal'
                padding: "10dp"
                spacing: "10dp"
                size_hint: None, None
                size: dp(200), dp(50)  # Adjust size as needed
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}

                canvas:
                    Color:
                        rgba: 0, 0, 0, 1 
                    Line:
                        width: 0.4  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

                MDIconButton:
                    icon: 'upload'
                    id: upload_icon7
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_x: None
                    width: dp(24)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    on_release: root.file_manager_open_1()

                MDLabel:
                    id: upload_label1
                    text: 'Upload ID'
                    halign: 'left'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_y: None
                    height: dp(36)
                    valign: 'middle'  # Align the label text vertically in the center
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            MDLabel:
                text: "Upload Last 6 months Bank Statements"
                font_size: dp(18)
                halign: 'center'

            BoxLayout:
                orientation: 'horizontal'
                padding: "10dp"
                spacing: "10dp"
                size_hint: None, None
                size: dp(200), dp(50)  
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}

                canvas:
                    Color:
                        rgba: 0, 0, 0, 1  
                    Line:
                        width: 0.4  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

                MDIconButton:
                    icon: 'upload'
                    id: upload_icon8
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  
                    size_hint_x: None
                    width: dp(24)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    on_release: root.file_manager_open_2()

                MDLabel:
                    id: upload_label2
                    text: 'Upload Statement'
                    halign: 'left'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_y: None
                    height: dp(36)
                    valign: 'middle'  # Align the label text vertically in the center
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            GridLayout:
                cols: 1
                spacing: dp(30)
                padding: dp(20)
                pos_hint: {'center_x': 0.50, 'center_y': 0.5}
                size_hint: 1, None
                height: "50dp"
                
                MDRaisedButton:
                    text: "Next"
                    on_release: root.add_data(annual_salary.text, designation.text)
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    size_hint: 1, None
                    height: "50dp"

            Label:
                text: ""

<BorrowerScreen15>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'BorrowerScreen14')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(50)

        MDLabel:
            text:""
            size_hint_y: None
            height: dp(40)

        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(10)
            padding: dp(30)  # Reduce the top padding
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text: 'Borrower Registration Form'
                font_size: dp(20)
                font_name: "Roboto-Bold"
                halign: 'center'
                bold: True
    
            Spinner:
                id: marital_status_id
                text: "Please Select Marital Status"
                values: ["Select Marital Status","Married", "Un-Married", "Divorced"]
                size_hint: 1 , None
                background_color: 1, 1 ,1, 0 
                color: 0, 0, 0, 1
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1  
                    Line:
                        width: 0.7
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)
    
            GridLayout:
                cols: 1
                spacing: dp(30)
                padding: dp(20)
                pos_hint: {'center_x': 0.50, 'center_y': 0.5}
                size_hint: 1, None
                height: "50dp"
    
                MDRaisedButton:
                    text: "Next"
                    on_release: root.add_data(marital_status_id.text)
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    size_hint: 1, None
                    height: "50dp"
    
            Label:
                text: ""

<BorrowerScreen16>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'BorrowerScreen15')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(50)

        MDLabel:
            text:""
            size_hint_y: None
            height: dp(40)

        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(10)
            padding: dp(30)  # Reduce the top padding
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text: 'Step-1'
                font_size: dp(25)
                halign: 'center'
                bold: True
    
            MDTextField:
                id: spouse_name
                hint_text: 'Enter Spouse Name '
                halign: 'left'
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                multiline: False
                helper_text: "Enter Valid Spouse Name"
                helper_text_mode: 'on_focus'
                font_name: "Roboto-Bold"
                bold: True
    
            MDTextField:
                id: spouse_date_textfield
                hint_text: " Enter Spouse Birth Date"
                on_focus: root.show_date_picker()
                icon_right: "calendar"
                halign: 'left'
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                multiline: False
                helper_text: "Enter valid date Of Birth"
                helper_text_mode: 'on_focus'
                font_name: "Roboto-Bold"
                bold: True
    
            MDTextField:
                id: spouse_mobile
                hint_text: 'Enter Spouse Mobile No'
                halign: 'left'
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                multiline: False
                helper_text: "Enter valid Spouse Mobile No"
                helper_text_mode: 'on_focus'
                font_name: "Roboto-Bold"
                bold: True
                input_type: 'number'  
                on_touch_down: root.on_spouse_mobile_touch_down()
    
            MDTextField:
                id: spouse_profession
                hint_text: 'Enter Spouse Profession '
                halign: 'left'
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                multiline: False
                helper_text: "Enter valid Spouse Profession"
                helper_text_mode: 'on_focus'
                font_name: "Roboto-Bold"
                bold: True
    
            GridLayout:
                cols: 1
                spacing: dp(30)
                padding: dp(20)
                pos_hint: {'center_x': 0.50, 'center_y': 0.5}
                size_hint: 1, None
                height: "50dp"
                
                MDRaisedButton:
                    text: "Next"
                    on_release: root.add_data(spouse_name.text, spouse_date_textfield.text, spouse_mobile.text, spouse_profession.text)
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    size_hint: 1, None
                    height: "50dp"
            
            Label:
                text: ""
                    
<BorrowerScreen17>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'BorrowerScreen16')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(50)
        MDLabel:
            text: ""
            size_hint_y: None
            height: dp(40)

        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(10)
            padding: dp(30)  # Reduce the top padding
            md_bg_color: 253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1  # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text: 'Step-2'
                font_size: dp(20)
                font_name: "Roboto-Bold"
                halign: 'center'
    
            MDTextField:
                id: spouse_company_name
                hint_text: 'Enter Spouse Company Name '
                halign: 'left'
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                multiline: False
                helper_text: 'Enter Valid Spouse Company Name '
                helper_text_mode: 'on_focus'
                font_name: "Roboto-Bold"
                bold: True
    
            MDTextField:
                id: spouse_company_address
                hint_text: 'Enter Spouse Company Address'
                halign: 'left'
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                multiline: False
                helper_text: "Enter valid Spouse Company Address"
                helper_text_mode: 'on_focus'
                font_name: "Roboto-Bold"
                bold: True
    
            MDTextField:
                id: spouse_annual_salary
                hint_text: 'Enter Annual Salary'
                halign: 'left'
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                multiline: False
                helper_text: 'Enter valid Annual Salary'
                helper_text_mode: 'on_focus'
                font_name: "Roboto-Bold"
                bold: True
                input_type: 'number'
                on_touch_down: root.on_spouse_annual_salary_touch_down()
    
            MDTextField:
                id: spouse_office_no
                hint_text: 'Enter Spouse Office Number'
                halign: 'left'
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                multiline: False
                helper_text: "Enter valid Spouse Office No"
                helper_text_mode: 'on_focus'
                font_name: "Roboto-Bold"
                bold: True
                input_type: 'number'
                on_touch_down: root.on_spouse_office_no_touch_down()
    
            GridLayout:
                cols: 1
                spacing: dp(30)
                padding: dp(20)
                pos_hint: {'center_x': 0.50, 'center_y': 0.5}
                size_hint: 1, None
                height: "50dp"
    
                MDRaisedButton:
                    text: "Next"
                    on_release: root.add_data(spouse_company_name.text, spouse_company_address.text, spouse_annual_salary.text, spouse_office_no.text)
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    size_hint: 1, None
                    height: "50dp"
    
            Label:
                text: ""

<BorrowerScreen18>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'BorrowerScreen15')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(50)
        MDLabel:
            text: ""
            size_hint_y: None
            height: dp(40)

        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(10)
            padding: dp(30)  # Reduce the top padding
            md_bg_color: 253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1  # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text: 'Applicant Bank Details'
                font_size: dp(20)
                font_name: "Roboto-Bold"
                halign: 'center'
                bold: True
    
            MDTextField:
                id: account_holder_name
                hint_text: 'Enter Account Holder Name '
                helper_text: 'Enter valid account holder name'
                halign: 'left'
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                multiline: False
                helper_text_mode: 'on_focus'
                font_name: "Roboto-Bold"
                bold: True
    
            Spinner:
                id: account_type_id
                text: "Select Account Type"
                values: ["Select Account Type", "Savings Account", "Salary Account", "Current Account", "NRI Account", "Re-Curing Account"]
                size_hint: 1, None
                background_color: 1, 1, 1, 0
                color: 0, 0, 0, 1
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1
                    Line:
                        width: 0.7
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)
    
            MDTextField:
                id: account_number
                hint_text: 'Enter Account number '
                multiline: False
                helper_text: 'Enter valid Account number'
                halign: 'left'
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                multiline: False
                helper_text_mode: 'on_focus'
                font_name: "Roboto-Bold"
                bold: True
    
            MDTextField:
                id: bank_name
                hint_text: 'Enter Bank Name '
                helper_text: 'Enter valid Bank Name'
                multiline: False
                helper_text_mode: 'on_focus'
                halign: 'left'
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                multiline: False
                font_name: "Roboto-Bold"
                bold: True
    
            GridLayout:
                cols: 1
                spacing: dp(30)
                padding: dp(20)
                pos_hint: {'center_x': 0.50, 'center_y': 0.5}
                size_hint: 1, None
                height: "50dp"
    
                MDRaisedButton:
                    text: "Next"
                    on_release: root.add_data(account_holder_name.text, account_type_id.text, account_number.text, bank_name.text)
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    size_hint: 1, None
                    height: "50dp"
    
            Label:
                text: ""

<BorrowerScreen19>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'BorrowerScreen18')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(50)
        MDLabel:
            text: ""
            size_hint_y: None
            height: dp(40)

        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(10)
            padding: dp(30)  # Reduce the top padding
            md_bg_color: 253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1  # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text: 'Applicant Bank Details'
                font_size: dp(20)
                font_name: "Roboto-Bold"
                halign: 'center'
                bold: True
    
            MDTextField:
                id: ifsc_code
                hint_text: 'Enter Bank ID '
                multiline: False
                helper_text: 'Enter valid Bank ID'
                helper_text_mode: 'on_focus'
                halign: 'left'
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                multiline: False
                font_name: "Roboto-Bold"
                bold: True
    
            Spinner:
                id: salary_id
                text: "Select Salary Paid Option"
                values: ["Salary Paid Option", "Cash", "Online"]
                multiline: False
                size_hint: 1, None
                background_color: (0, 0, 0, 0)
                background_normal: ''
                background_color: 1, 1, 1, 0 
                color: 0, 0, 0, 1
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1  
                    Line:
                        width: 0.7
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)
    
            MDTextField:
                id: branch_name
                hint_text: 'Enter Branch Name'
                helper_text: 'Enter valid Branch Name'
                hint_text_mode: 'on_focus'
                multiline: False
                halign: 'left'
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                multiline: False
                font_name: "Roboto-Bold"
    
            GridLayout:
                cols: 2
                spacing: dp(30)
                padding: dp(20)
                pos_hint: {'center_x': 0.50, 'center_y': 0.5}
                size_hint: 1, None
                height: "50dp"
    
                MDRaisedButton:
                    text: "Back"
                    on_release: app.root.current = 'BorrowerScreen18'
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    theme_text_color: 'Custom'
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
    
                MDRaisedButton:
                    text: "Submit"
                    on_release: root.go_to_borrower_dashboard(ifsc_code.text, salary_id.text, branch_name.text)
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    size_hint: 1, None
                    height: "50dp"
    
            Label:
                text: ""
'''

conn = sqlite3.connect("fin_user_profile.db")
cursor = conn.cursor()


class BorrowerScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.date_picker = MDDatePicker()
        self.date_picker.bind(on_save=self.on_date_selected)

    def show_date_picker(self):
        self.date_picker.open()

    def on_date_selected(self, instance, the_date, a):
        print(f"Selected date: {the_date, the_date.year}")
        self.ids.date_textfield.text = f'{the_date.year}-{the_date.month}-{the_date.day}'

    def add_data(self, name, gender, date_of_birth, mobile_number):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        b = 'borrower'
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute(
            "UPDATE fin_registration_table SET name = ?, gender = ?,  date_of_birth = ?,mobile_number = ?,  user_type = ? WHERE customer_id = ?",
            (name, gender, date_of_birth, mobile_number, b, row_id_list[log_index]))
        conn.commit()
        self.manager.current = 'BorrowerScreen1'

    def go_to_dashboard(self):
        self.manager.current = 'dashboard'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'BorrowerLanding'

    def on_mobile_number_touch_down(self):
        # Change keyboard mode to numeric when the mobile number text input is touched
        self.ids.mobile_number.input_type = 'number'


class BorrowerScreen1(Screen):
    def on_mobile_number_touch_down(self):
        # Change keyboard mode to numeric when the mobile number text input is touched
        self.ids.alternate_mobile_number.input_type = 'number'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.manager_open_1 = False
        self.file_manager_1 = MDFileManager(
            exit_manager=self.exit_manager_1,
            select_path=self.select_path_1
        )

    # Other existing methods here...

    def file_manager_open_1(self):
        self.file_manager_1.show('/')
        self.manager_open_1 = True

    def select_path_1(self, path):
        print(f"Selected path 1: {path}")
        self.update_data_with_file_1(path)
        self.exit_manager_1()

    def update_data_with_file_1(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute("UPDATE fin_registration_table SET profile_file = ? WHERE customer_id = ?",
                       (file_path, row_id_list[log_index]))
        conn.commit()

        self.ids.upload_label1.text = 'Upload Successfully'

    def exit_manager_1(self, *args):
        self.manager_open_1 = False
        self.file_manager_1.close()

    def upload_1(self):
        if not self.manager_open_1:
            self.file_manager_open_1()

    def add_data(self, alternate_mobile_number, alternate_email):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute(
            "UPDATE fin_registration_table SET alternate_mobile_number = ?, alternate_email = ? WHERE customer_id = ?",
            (alternate_mobile_number, alternate_email, row_id_list[log_index]))
        conn.commit()
        self.manager.current = 'BorrowerScreen2'

    def go_to_dashboard(self):
        self.manager.current = 'dashboard'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'BorrowerScreen'


class BorrowerScreen2(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.manager_open_1 = False
        self.manager_open_2 = False
        self.file_manager_1 = MDFileManager(
            exit_manager=self.exit_manager_1,
            select_path=self.select_path_1
        )
        self.file_manager_2 = MDFileManager(
            exit_manager=self.exit_manager_2,
            select_path=self.select_path_2
        )

    # Other existing methods here...

    def file_manager_open_1(self):
        self.file_manager_1.show('/')
        self.manager_open_1 = True

    def select_path_1(self, path):
        print(f"Selected path 1: {path}")
        self.update_data_with_file_1(path)
        self.exit_manager_1()

    def update_data_with_file_1(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute("UPDATE fin_registration_table SET aadhar_file = ? WHERE customer_id = ?",
                       (file_path, row_id_list[log_index]))
        conn.commit()

        self.ids.upload_label1.text = 'Upload Successfully'

    def exit_manager_1(self, *args):
        self.manager_open_1 = False
        self.file_manager_1.close()

    def upload_1(self):
        if not self.manager_open_1:
            self.file_manager_open_1()

    # Repeat similar methods for file manager 2...

    def file_manager_open_2(self):
        self.file_manager_2.show('/')
        self.manager_open_2 = True

    def select_path_2(self, path):
        print(f"Selected path 2: {path}")
        self.update_data_with_file_2(path)
        self.exit_manager_2()

    def update_data_with_file_2(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute("UPDATE fin_registration_table SET pan_file = ? WHERE customer_id = ?",
                       (file_path, row_id_list[log_index]))
        conn.commit()
        self.ids.upload_label2.text = 'Upload Successfully'

    def exit_manager_2(self, *args):
        self.manager_open_2 = False
        self.file_manager_2.close()

    def upload_2(self):
        if not self.manager_open_2:
            self.file_manager_open_2()

    def add_data(self, aadhar_number, pan_number):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute("UPDATE fin_registration_table SET aadhar_number = ?, pan_number = ? WHERE customer_id = ?",
                       (aadhar_number, pan_number, row_id_list[log_index]))
        conn.commit()
        self.manager.current = 'BorrowerScreen3'

    def go_to_dashboard(self):
        self.manager.current = 'dashboard'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'BorrowerScreen1'


class BorrowerScreen3(Screen):

    def next_pressed(self, id):
        if id == '10th class':
            BorrowerScreen_Edu_10th()
            self.manager.current = 'BorrowerScreen_Edu_10th'

        elif id == 'Intermediate':
            BorrowerScreen_Edu_Intermediate()
            self.manager.current = 'BorrowerScreen_Edu_Intermediate'

        elif id == 'Bachelors':
            self.manager.current = 'BorrowerScreen_Edu_Bachelors'
        elif id == 'Masters':
            self.manager.current = 'BorrowerScreen_Edu_Masters'
        elif id == 'PHD':
            self.manager.current = 'BorrowerScreen_Edu_PHD'
        print(id)
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')
        cursor.execute("UPDATE fin_registration_table SET highest_qualification = ? WHERE customer_id = ?",
                       (id, row_id_list[log_index]))
        conn.commit()

    def go_to_dashboard(self):
        self.manager.current = 'dashboard'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'BorrowerScreen2'


class BorrowerScreen_Edu_10th(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.manager_open_1 = False
        self.file_manager_1 = MDFileManager(
            exit_manager=self.exit_manager_1,
            select_path=self.select_path_1
        )

    # Other existing methods here...

    def file_manager_open_1(self):
        self.file_manager_1.show('/')
        self.manager_open_1 = True

    def select_path_1(self, path):
        print(f"Selected path 1: {path}")
        self.update_data_with_file_1(path)
        self.exit_manager_1()

    def update_data_with_file_1(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute("UPDATE fin_registration_table SET tenth_certificate = ? WHERE customer_id = ?",
                       (file_path, row_id_list[log_index]))
        conn.commit()
        self.ids.upload_label1.text = 'Upload Successfully'

    def exit_manager_1(self, *args):
        self.manager_open_1 = False
        self.file_manager_1.close()

    def upload_1(self):
        if not self.manager_open_1:
            self.file_manager_open_1()

    def go_to_dashboard(self):
        self.manager.current = 'dashboard'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'BorrowerScreen3'


class BorrowerScreen_Edu_Intermediate(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.manager_open_1 = False
        self.manager_open_2 = False
        self.file_manager_1 = MDFileManager(
            exit_manager=self.exit_manager_1,
            select_path=self.select_path_1
        )
        self.file_manager_2 = MDFileManager(
            exit_manager=self.exit_manager_2,
            select_path=self.select_path_2
        )

    # Other existing methods here...

    def file_manager_open_1(self):
        self.file_manager_1.show('/')
        self.manager_open_1 = True

    def select_path_1(self, path):
        print(f"Selected path 1: {path}")
        self.update_data_with_file_1(path)
        self.exit_manager_1()

    def update_data_with_file_1(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')
        cursor.execute("UPDATE fin_registration_table SET tenth_certificate = ? WHERE customer_id = ?",
                       (file_path, row_id_list[log_index]))
        conn.commit()
        self.ids.upload_label1.text = 'Upload Successfully'

    def exit_manager_1(self, *args):
        self.manager_open_1 = False
        self.file_manager_1.close()

    def upload_1(self):
        if not self.manager_open_1:
            self.file_manager_open_1()

    # Repeat similar methods for file manager 2...

    def file_manager_open_2(self):
        self.file_manager_2.show('/')
        self.manager_open_2 = True

    def select_path_2(self, path):
        print(f"Selected path 2: {path}")
        self.update_data_with_file_2(path)
        self.exit_manager_2()

    def update_data_with_file_2(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute("UPDATE fin_registration_table SET inter_certificate = ? WHERE customer_id = ?",
                       (file_path, row_id_list[log_index]))
        conn.commit()
        self.ids.upload_label2.text = 'Upload Successfully'

    def exit_manager_2(self, *args):
        self.manager_open_2 = False
        self.file_manager_2.close()

    def upload_2(self):
        if not self.manager_open_2:
            self.file_manager_open_2()

    def go_to_dashboard(self):
        self.manager.current = 'dashboard'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'BorrowerScreen3'


class BorrowerScreen_Edu_Bachelors(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.manager_open_1 = False
        self.manager_open_2 = False
        self.manager_open_3 = False
        self.file_manager_1 = MDFileManager(
            exit_manager=self.exit_manager_1,
            select_path=self.select_path_1
        )
        self.file_manager_2 = MDFileManager(
            exit_manager=self.exit_manager_2,
            select_path=self.select_path_2
        )
        self.file_manager_3 = MDFileManager(
            exit_manager=self.exit_manager_3,
            select_path=self.select_path_3
        )

    # Other existing methods here...

    def file_manager_open_1(self):
        self.file_manager_1.show('/')
        self.manager_open_1 = True

    def select_path_1(self, path):
        print(f"Selected path 1: {path}")
        self.update_data_with_file_1(path)
        self.exit_manager_1()

    def update_data_with_file_1(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')
        cursor.execute("UPDATE fin_registration_table SET tenth_certificate = ? WHERE customer_id = ?",
                       (file_path, row_id_list[log_index]))
        conn.commit()
        self.ids.upload_label1.text = 'Upload Successfully'

    def exit_manager_1(self, *args):
        self.manager_open_1 = False
        self.file_manager_1.close()

    def upload_1(self):
        if not self.manager_open_1:
            self.file_manager_open_1()

    # Repeat similar methods for file manager 2...

    def file_manager_open_2(self):
        self.file_manager_2.show('/')
        self.manager_open_2 = True

    def select_path_2(self, path):
        print(f"Selected path 2: {path}")
        self.update_data_with_file_2(path)
        self.exit_manager_2()

    def update_data_with_file_2(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute("UPDATE fin_registration_table SET inter_certificate = ? WHERE customer_id = ?",
                       (file_path, row_id_list[log_index]))
        conn.commit()
        self.ids.upload_label2.text = 'Upload Successfully'

    def exit_manager_2(self, *args):
        self.manager_open_2 = False
        self.file_manager_2.close()

    def upload_2(self):
        if not self.manager_open_2:
            self.file_manager_open_2()

    def file_manager_open_3(self):
        self.file_manager_3.show('/')
        self.manager_open_3 = True

    def select_path_3(self, path):
        print(f"Selected path 3: {path}")
        self.update_data_with_file_3(path)
        self.exit_manager_3()

    def update_data_with_file_3(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute("UPDATE fin_registration_table SET bachelors_certificate = ? WHERE customer_id = ?",
                       (file_path, row_id_list[log_index]))
        conn.commit()
        self.ids.upload_label3.text = 'Upload Successfully'

    def exit_manager_3(self, *args):
        self.manager_open_3 = False
        self.file_manager_3.close()

    def upload_3(self):
        if not self.manager_open_3:
            self.file_manager_open_3()

    def go_to_dashboard(self):
        self.manager.current = 'dashboard'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'BorrowerScreen3'


class BorrowerScreen_Edu_Masters(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.manager_open_1 = False
        self.manager_open_2 = False
        self.manager_open_3 = False
        self.manager_open_4 = False
        self.file_manager_1 = MDFileManager(
            exit_manager=self.exit_manager_1,
            select_path=self.select_path_1
        )
        self.file_manager_2 = MDFileManager(
            exit_manager=self.exit_manager_2,
            select_path=self.select_path_2
        )
        self.file_manager_3 = MDFileManager(
            exit_manager=self.exit_manager_3,
            select_path=self.select_path_3
        )
        self.file_manager_4 = MDFileManager(
            exit_manager=self.exit_manager_4,
            select_path=self.select_path_4
        )

    # Other existing methods here...

    def file_manager_open_1(self):
        self.file_manager_1.show('/')
        self.manager_open_1 = True

    def select_path_1(self, path):
        print(f"Selected path 1: {path}")
        self.update_data_with_file_1(path)
        self.exit_manager_1()

    def update_data_with_file_1(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')
        cursor.execute("UPDATE fin_registration_table SET tenth_certificate = ? WHERE customer_id = ?",
                       (file_path, row_id_list[log_index]))
        conn.commit()
        self.ids.upload_label1.text = 'Upload Successfully'

    def exit_manager_1(self, *args):
        self.manager_open_1 = False
        self.file_manager_1.close()

    def upload_1(self):
        if not self.manager_open_1:
            self.file_manager_open_1()

    # Repeat similar methods for file manager 2...

    def file_manager_open_2(self):
        self.file_manager_2.show('/')
        self.manager_open_2 = True

    def select_path_2(self, path):
        print(f"Selected path 2: {path}")
        self.update_data_with_file_2(path)
        self.exit_manager_2()

    def update_data_with_file_2(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute("UPDATE fin_registration_table SET inter_certificate = ? WHERE customer_id = ?",
                       (file_path, row_id_list[log_index]))
        conn.commit()
        self.ids.upload_label2.text = 'Upload Successfully'

    def exit_manager_2(self, *args):
        self.manager_open_2 = False
        self.file_manager_2.close()

    def upload_2(self):
        if not self.manager_open_2:
            self.file_manager_open_2()

    def file_manager_open_3(self):
        self.file_manager_3.show('/')
        self.manager_open_3 = True

    def select_path_3(self, path):
        print(f"Selected path 3: {path}")
        self.update_data_with_file_3(path)
        self.exit_manager_3()

    def update_data_with_file_3(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute("UPDATE fin_registration_table SET bachelors_certificate = ? WHERE customer_id = ?",
                       (file_path, row_id_list[log_index]))
        conn.commit()
        self.ids.upload_label3.text = 'Upload Successfully'

    def exit_manager_3(self, *args):
        self.manager_open_3 = False
        self.file_manager_3.close()

    def upload_3(self):
        if not self.manager_open_3:
            self.file_manager_open_3()

    def file_manager_open_4(self):
        self.file_manager_4.show('/')
        self.manager_open_4 = True

    def select_path_4(self, path):
        print(f"Selected path 4: {path}")
        self.update_data_with_file_4(path)
        self.exit_manager_4()

    def update_data_with_file_4(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')
        cursor.execute("UPDATE fin_registration_table SET masters_certificate = ? WHERE customer_id = ?",
                       (file_path, row_id_list[log_index]))
        conn.commit()
        self.ids.upload_label4.text = 'Upload Successfully'

    def exit_manager_4(self, *args):
        self.manager_open_4 = False
        self.file_manager_4.close()

    def upload_4(self):
        if not self.manager_open_4:
            self.file_manager_open_4()

    def go_to_dashboard(self):
        self.manager.current = 'dashboard'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'BorrowerScreen3'


class BorrowerScreen_Edu_PHD(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.manager_open_1 = False
        self.manager_open_2 = False
        self.manager_open_3 = False
        self.manager_open_4 = False
        self.manager_open_5 = False
        self.file_manager_1 = MDFileManager(
            exit_manager=self.exit_manager_1,
            select_path=self.select_path_1
        )
        self.file_manager_2 = MDFileManager(
            exit_manager=self.exit_manager_2,
            select_path=self.select_path_2
        )
        self.file_manager_3 = MDFileManager(
            exit_manager=self.exit_manager_3,
            select_path=self.select_path_3
        )
        self.file_manager_4 = MDFileManager(
            exit_manager=self.exit_manager_4,
            select_path=self.select_path_4
        )
        self.file_manager_5 = MDFileManager(
            exit_manager=self.exit_manager_5,
            select_path=self.select_path_5
        )

    # Other existing methods here...

    def file_manager_open_1(self):
        self.file_manager_1.show('/')
        self.manager_open_1 = True

    def select_path_1(self, path):
        print(f"Selected path 1: {path}")
        self.update_data_with_file_1(path)
        self.exit_manager_1()

    def update_data_with_file_1(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')
        cursor.execute("UPDATE fin_registration_table SET tenth_certificate = ? WHERE customer_id = ?",
                       (file_path, row_id_list[log_index]))
        conn.commit()
        self.ids.upload_label1.text = 'Upload Successfully'

    def exit_manager_1(self, *args):
        self.manager_open_1 = False
        self.file_manager_1.close()

    def upload_1(self):
        if not self.manager_open_1:
            self.file_manager_open_1()

    # Repeat similar methods for file manager 2...

    def file_manager_open_2(self):
        self.file_manager_2.show('/')
        self.manager_open_2 = True

    def select_path_2(self, path):
        print(f"Selected path 2: {path}")
        self.update_data_with_file_2(path)
        self.exit_manager_2()

    def update_data_with_file_2(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute("UPDATE fin_registration_table SET inter_certificate = ? WHERE customer_id = ?",
                       (file_path, row_id_list[log_index]))
        conn.commit()
        self.ids.upload_label2.text = 'Upload Successfully'

    def exit_manager_2(self, *args):
        self.manager_open_2 = False
        self.file_manager_2.close()

    def upload_2(self):
        if not self.manager_open_2:
            self.file_manager_open_2()

    def file_manager_open_3(self):
        self.file_manager_3.show('/')
        self.manager_open_3 = True

    def select_path_3(self, path):
        print(f"Selected path 3: {path}")
        self.update_data_with_file_3(path)
        self.exit_manager_3()

    def update_data_with_file_3(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute("UPDATE fin_registration_table SET bachelors_certificate = ? WHERE customer_id = ?",
                       (file_path, row_id_list[log_index]))
        conn.commit()
        self.ids.upload_label3.text = 'Upload Successfully'

    def exit_manager_3(self, *args):
        self.manager_open_3 = False
        self.file_manager_3.close()

    def upload_3(self):
        if not self.manager_open_3:
            self.file_manager_open_3()

    def file_manager_open_4(self):
        self.file_manager_4.show('/')
        self.manager_open_4 = True

    def select_path_4(self, path):
        print(f"Selected path 4: {path}")
        self.update_data_with_file_4(path)
        self.exit_manager_4()

    def update_data_with_file_4(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute("UPDATE fin_registration_table SET masters_certificate = ? WHERE customer_id = ?",
                       (file_path, row_id_list[log_index]))
        conn.commit()
        self.ids.upload_label4.text = 'Upload Successfully'

    def exit_manager_4(self, *args):
        self.manager_open_4 = False
        self.file_manager_4.close()

    def upload_4(self):
        if not self.manager_open_4:
            self.file_manager_open_4()

    def file_manager_open_5(self):
        self.file_manager_5.show('/')
        self.manager_open_5 = True

    def select_path_5(self, path):
        print(f"Selected path 5: {path}")
        self.update_data_with_file_5(path)
        self.exit_manager_5()

    def update_data_with_file_5(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute("UPDATE fin_registration_table SET phd_certificate = ? WHERE customer_id = ?",
                       (file_path, row_id_list[log_index]))
        conn.commit()
        self.ids.upload_label5.text = 'Upload Successfully'

    def exit_manager_5(self, *args):
        self.manager_open_5 = False
        self.file_manager_5.close()

    def upload_5(self):
        if not self.manager_open_5:
            self.file_manager_open_5()

    def go_to_dashboard(self):
        self.manager.current = 'dashboard'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'BorrowerScreen3'


class BorrowerScreen4(Screen):
    def add_data(self, street, city, zip_code, state, country):
        cursor.execute('select * from fin_users')

        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute(
            "UPDATE fin_registration_table SET street_name = ?, city_name = ?, zip_code = ?, state_name = ?, country_name = ? WHERE customer_id = ?",
            (street, city, zip_code, state, country, row_id_list[log_index]))
        conn.commit()
        self.manager.current = 'BorrowerScreen5'


def on_mobile_number_touch_down(self):
    # Change keyboard mode to numeric when the mobile number text input is touched
    self.ids.zip_code.input_type = 'number'


def go_to_dashboard(self):
    self.manager.current = 'dashboard'


def on_pre_enter(self):
    Window.bind(on_keyboard=self.on_back_button)


def on_pre_leave(self):
    Window.unbind(on_keyboard=self.on_back_button)


def on_back_button(self, instance, key, scancode, codepoint, modifier):
    if key == 27:
        self.go_back()
        return True
    return False


def go_back(self):
    self.manager.transition = SlideTransition(direction='right')
    self.manager.current = 'BorrowerScreen3'


class BorrowerScreen5(Screen):
    def on_father_age_touch_down(self):
        # Change keyboard mode to numeric when the mobile number text input is touched
        self.ids.father_age.input_type = 'number'

    def on_father_ph_no_touch_down(self):
        # Change keyboard mode to numeric when the mobile number text input is touched
        self.ids.father_ph_no.input_type = 'number'

    def add_data(self, father_name, father_age, father_occupation, father_ph_no):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute(
            "UPDATE fin_registration_table SET father_name = ?, father_age = ?, father_occupation = ?, father_ph_no = ? WHERE customer_id = ?",
            (father_name, father_age, father_occupation, father_ph_no, row_id_list[log_index]))
        conn.commit()
        self.manager.current = 'BorrowerScreen6'

    def go_to_dashboard(self):
        self.manager.current = 'dashboard'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'BorrowerScreen4'


class BorrowerScreen6(Screen):
    def on_mother_age_touch_down(self):
        # Change keyboard mode to numeric when the mobile number text input is touched
        self.ids.mother_age.input_type = 'number'

    def on_mother_ph_no_touch_down(self):
        # Change keyboard mode to numeric when the mobile number text input is touched
        self.ids.mother_ph_no.input_type = 'number'

    def add_data(self, mother_name, mother_age, mother_occupation, mother_ph_no):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute(
            "UPDATE fin_registration_table SET mother_name = ?, mother_age = ?, mother_occupation = ?, mother_ph_no = ? WHERE customer_id = ?",
            (mother_name, mother_age, mother_occupation, mother_ph_no, row_id_list[log_index]))
        conn.commit()
        self.manager.current = 'BorrowerScreen7'

    def go_to_dashboard(self):
        self.manager.current = 'dashboard'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'BorrowerScreen5'


class BorrowerScreen7(Screen):

    def add_data(self, spinner_id):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute(
            "UPDATE fin_registration_table SET proficient_type = ? WHERE customer_id = ?",
            (spinner_id, row_id_list[log_index]))
        conn.commit()
        if spinner_id == 'Student':
            self.manager.current = 'BorrowerScreen8'

        elif spinner_id == 'Business':
            self.manager.current = 'BorrowerScreen9'

        elif spinner_id == 'Employee':
            self.manager.current = 'BorrowerScreen12'
        print(id)

    def go_to_dashboard(self):
        self.manager.current = 'dashboard'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'BorrowerScreen5'


class BorrowerScreen8(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.manager_open_1 = False
        self.file_manager_1 = MDFileManager(
            exit_manager=self.exit_manager_1,
            select_path=self.select_path_1
        )

    # Other existing methods here...

    def file_manager_open_1(self):
        self.file_manager_1.show('/')
        self.manager_open_1 = True

    def select_path_1(self, path):
        print(f"Selected path 1: {path}")
        self.update_data_with_file_1(path)
        self.exit_manager_1()

    def update_data_with_file_1(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute("UPDATE fin_registration_table SET collage_id_file = ? WHERE customer_id = ?",
                       (file_path, row_id_list[log_index]))
        conn.commit()

        self.ids.upload_label2.text = 'Upload Successfully'

    def exit_manager_1(self, *args):
        self.manager_open_1 = False
        self.file_manager_1.close()

    def upload_1(self):
        if not self.manager_open_1:
            self.file_manager_open_1()

    def add_data(self, collage_name, college_address, collage_id):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute(
            "UPDATE fin_registration_table SET collage_name = ?, college_address = ?, college_id = ? WHERE customer_id = ?",
            (collage_name, college_address, collage_id, row_id_list[log_index]))
        conn.commit()
        self.manager.current = 'BorrowerScreen15'

    def go_to_dashboard(self):
        self.manager.current = 'dashboard'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'BorrowerScreen7'


class BorrowerScreen9(Screen):
    def add_data(self, business_name, business_location, business_address):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute(
            "UPDATE fin_registration_table SET business_name = ?, business_location = ?, business_address = ? WHERE customer_id = ?",
            (business_name, business_location, business_address, row_id_list[log_index]))
        conn.commit()
        self.manager.current = 'BorrowerScreen10'

    def go_to_dashboard(self):
        self.manager.current = 'dashboard'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'BorrowerScreen7'


class BorrowerScreen10(Screen):
    def add_data(self, landmark, business_type, no_of_employees_working,registered_office_address, year_of_estd):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute(
            "UPDATE fin_registration_table SET landmark = ?, business_type = ?, no_of_employees_working = ?,registered_office_address= ?, year_of_estd = ? WHERE customer_id = ?",
            (landmark, business_type, no_of_employees_working, registered_office_address, year_of_estd,
             row_id_list[log_index]))
        conn.commit()
        self.manager.current = 'BorrowerScreen11'

    def go_to_dashboard(self):
        self.manager.current = 'dashboard'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'BorrowerScreen9'


class BorrowerScreen11(Screen):
    def on_last_six_months_turnover_touch_down(self):
        # Change keyboard mode to numeric when the mobile number text input is touched
        self.ids.last_six_months_turnover.input_type = 'number'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.manager_open_1 = False
        self.file_manager_1 = MDFileManager(
            exit_manager=self.exit_manager_1,
            select_path=self.select_path_1
        )

    # Other existing methods here...

    def file_manager_open_1(self):
        self.file_manager_1.show('/')
        self.manager_open_1 = True

    def select_path_1(self, path):
        print(f"Selected path 1: {path}")
        self.update_data_with_file_1(path)
        self.exit_manager_1()

    def update_data_with_file_1(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute("UPDATE fin_registration_table SET last_six_months_turnover_file = ? WHERE customer_id = ?",
                       (file_path, row_id_list[log_index]))
        conn.commit()
        self.ids.upload_label1.text = 'Upload Successfully'

    def exit_manager_1(self, *args):
        self.manager_open_1 = False
        self.file_manager_1.close()

    def upload1(self):
        if not self.manager_open_1:
            self.file_manager_open_1()

    def add_data(self, industry_type, last_six_months_turnover):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute(
            "UPDATE fin_registration_table SET industry_type = ?, last_six_months_turnover = ? WHERE customer_id = ?",
            (industry_type, last_six_months_turnover, row_id_list[log_index]))
        conn.commit()
        self.manager.current = 'BorrowerScreen11'

    def go_to_dashboard(self):
        self.manager.current = 'dashboard'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'BorrowerScreen15'


class BorrowerScreen12(Screen):
    def add_data(self, employeent_type, company_name, organization):
        cursor.execute('select * from fin_users')

        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute(
            "UPDATE fin_registration_table SET employment_type = ?, company_name = ?, organization_type = ? WHERE customer_id = ?",
            (employeent_type, company_name, organization, row_id_list[log_index]))
        conn.commit()
        self.manager.current = 'BorrowerScreen13'


def go_to_dashboard(self):
    self.manager.current = 'dashboard'


def on_pre_enter(self):
    Window.bind(on_keyboard=self.on_back_button)


def on_pre_leave(self):
    Window.unbind(on_keyboard=self.on_back_button)


def on_back_button(self, instance, key, scancode, codepoint, modifier):
    if key == 27:
        self.go_back()
        return True
    return False


def go_back(self):
    self.manager.transition = SlideTransition(direction='right')
    self.manager.current = 'BorrowerScreen7'


class BorrowerScreen13(Screen):
    def add_data(self, company_address, company_pincode, company_country, landmark, business_number):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute(
            "UPDATE fin_registration_table SET company_address = ?, company_pincode = ?, company_country = ?, landmark = ?, business_number = ? WHERE customer_id = ?",
            (company_address, company_pincode, company_country, landmark, business_number, row_id_list[log_index]))
        conn.commit()
        self.manager.current = 'BorrowerScreen14'

    def on_company_pin_code_touch_down(self):
        # Change keyboard mode to numeric when the mobile number text input is touched
        self.ids.company_pin_code.input_type = 'number'

    def on_business_phone_number_touch_down(self):
        # Change keyboard mode to numeric when the mobile number text input is touched
        self.ids.business_phone_number.input_type = 'number'

    def go_to_dashboard(self):
        self.manager.current = 'dashboard'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'BorrowerScreen12'


class BorrowerScreen14(Screen):
    def on_annual_salary_touch_down(self):
        # Change keyboard mode to numeric when the mobile number text input is touched
        self.ids.annual_salary.input_type = 'number'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.manager_open_1 = False
        self.manager_open_2 = False
        self.file_manager_1 = MDFileManager(
            exit_manager=self.exit_manager_1,
            select_path=self.select_path_1
        )
        self.file_manager_2 = MDFileManager(
            exit_manager=self.exit_manager_2,
            select_path=self.select_path_2
        )

    # Other existing methods here...

    def file_manager_open_1(self):
        self.file_manager_1.show('/')
        self.manager_open_1 = True

    def select_path_1(self, path):
        print(f"Selected path 1: {path}")
        self.update_data_with_file_1(path)
        self.exit_manager_1()

    def update_data_with_file_1(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute("UPDATE fin_registration_table SET employee_id_file = ? WHERE customer_id = ?",
                       (file_path, row_id_list[log_index]))
        conn.commit()
        self.ids.upload_label1.text = 'Upload Successfully'

    def exit_manager_1(self, *args):
        self.manager_open_1 = False
        self.file_manager_1.close()

    def upload1(self):
        if not self.manager_open_1:
            self.file_manager_open_1()

    # Repeat similar methods for file manager 2...

    def file_manager_open_2(self):
        self.file_manager_2.show('/')
        self.manager_open_2 = True

    def select_path_2(self, path):
        print(f"Selected path 2: {path}")
        self.update_data_with_file_2(path)
        self.exit_manager_2()

    def update_data_with_file_2(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute("UPDATE fin_registration_table SET six_months_bank_statement_file = ? WHERE customer_id = ?",
                       (file_path, row_id_list[log_index]))
        conn.commit()
        self.ids.upload_label2.text = 'Upload Successfully'

    def exit_manager_2(self, *args):
        self.manager_open_2 = False
        self.file_manager_2.close()

    def upload2(self):
        if not self.manager_open_2:
            self.file_manager_open_2()

    def add_data(self, annual_salary, designation):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute(
            "UPDATE fin_registration_table SET annual_salary = ?, designation = ? WHERE customer_id = ?",
            (annual_salary, designation, row_id_list[log_index]))
        conn.commit()
        self.manager.current = 'BorrowerScreen15'

    def go_to_dashboard(self):
        self.manager.current = 'dashboard'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'BorrowerScreen13'


class BorrowerScreen15(Screen):
    def add_data(self, marital_status_id):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute(
            "UPDATE fin_registration_table SET marital_status = ? WHERE customer_id = ?",
            (marital_status_id, row_id_list[log_index]))
        conn.commit()

        if marital_status_id == 'Un-Married':
            self.manager.current = 'BorrowerScreen18'

        elif marital_status_id == 'Married':
            self.manager.current = 'BorrowerScreen16'

        elif marital_status_id == 'Divorced':
            self.manager.current = 'BorrowerScreen18'

    def go_to_dashboard(self):
        self.manager.current = 'dashboard'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'BorrowerScreen6'


class BorrowerScreen16(Screen):
    def on_spouse_mobile_touch_down(self):
        # Change keyboard mode to numeric when the mobile number text input is touched
        self.ids.spouse_mobile.input_type = 'number'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.date_picker = MDDatePicker()
        self.date_picker.bind(on_save=self.on_date_selected)

    def show_date_picker(self):
        self.date_picker.open()

    def on_date_selected(self, instance, the_date, a):
        print(f"Selected date: {the_date, the_date.year}")
        self.ids.spouse_date_textfield.text = f'{the_date.year}-{the_date.month}-{the_date.day}'

    def add_data(self, spouse_name, spouse_date_textfield, spouse_mobile, spouse_profession):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute(
            "UPDATE fin_registration_table SET spouse_name = ?,spouse_date_textfield = ?, spouse_mobile = ?, spouse_profession = ? WHERE customer_id = ?",
            (spouse_name, spouse_date_textfield, spouse_mobile, spouse_profession, row_id_list[log_index]))
        conn.commit()
        self.manager.current = 'BorrowerScreen17'

    def go_to_dashboard(self):
        self.manager.current = 'dashboard'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'BorrowerScreen15'


class BorrowerScreen17(Screen):
    def on_spouse_annual_salary_touch_down(self):
        # Change keyboard mode to numeric when the mobile number text input is touched
        self.ids.spouse_annual_salary.input_type = 'number'

    def on_spouse_office_no_touch_down(self):
        # Change keyboard mode to numeric when the mobile number text input is touched
        self.ids.spouse_office_no.input_type = 'number'

    def add_data(self, spouse_company_name, spouse_company_address, spouse_annual_salary, spouse_office_no):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute(
            "UPDATE fin_registration_table SET spouse_company_name = ?,spouse_company_address = ?, spouse_annual_salary = ?, spouse_office_no = ? WHERE customer_id = ?",
            (spouse_company_name, spouse_company_address, spouse_annual_salary, spouse_office_no,
             row_id_list[log_index]))
        conn.commit()
        self.manager.current = 'BorrowerScreen18'

    def go_to_dashboard(self):
        self.manager.current = 'dashboard'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'BorrowerScreen16'


class BorrowerScreen18(Screen):
    def add_data(self, account_holder_name, account_type, account_number, bank_name):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute(
            "UPDATE fin_registration_table SET account_holder_name = ?, account_type = ?, account_number = ?, bank_name = ? WHERE customer_id = ?",
            (account_holder_name, account_type, account_number, bank_name, row_id_list[log_index]))
        conn.commit()
        self.manager.current = 'BorrowerScreen19'

    def go_to_dashboard(self):
        self.manager.current = 'dashboard'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'BorrowerScreen15'


class BorrowerScreen19(Screen):
    def go_to_borrower_dashboard(self, bank_id, branch_name, salary_id):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute(
            "UPDATE fin_registration_table SET bank_id = ?,salary_id = ?, branch_name = ? WHERE customer_id = ?",
            (bank_id, branch_name, salary_id, row_id_list[log_index]))
        conn.commit()

        self.manager.current = 'borrower_dashboard'

    def go_to_dashboard(self):
        self.manager.current = 'dashboard'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'BorrowerScreen18'
