from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivymd.uix.button import MDRectangleFlatButton
from kivy.metrics import dp
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.pickers import MDDatePicker


KV = '''
<LenderScreen>:# lender_module/lender_registration_form.py
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
        spacing: dp(30)
        padding: dp(50)
        MDLabel:
            text:""
            size_hint_y: None
            height: 50


        MDLabel:
            text: 'Lender Registration Form'
            halign: 'center'
            bold: True
            size_hint_y: None
            height: 50

        MDTextField:
            id: username
            hint_text: 'Enter full name'
            multiline: False
            helper_text: 'Enter valid name'
            helper_text_mode: 'on_focus'
            size_hint_y: None
            height: self.minimum_height
            font_name: "Roboto-Bold"


        Spinner:
            id: spinner_id
            text: "Select Gender"
            values: ["Select Gender", "Male", "Female", "Other"]
            multiline:False
            size_hint_y: (None)
            background_color: (0,0,0,0)
            background_normal: ''
            color: 0,0,0,1
            canvas.before:
                Color:
                    rgba: 0, 0, 0, 1  # Border color (black in this example)
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)


        MDTextField:
            id: date_textfield
            hint_text: "Select Date Of Birth"
            icon_right: "calendar"
            readonly: True
            on_focus: if self.focus: app.show_date_picker()
            font_name: "Roboto-Bold"
            hint_text_color: 0, 0, 0, 1

        GridLayout:
            cols: 2

            MDRectangleFlatButton:
                text: 'Next'
                md_bg_color: 0.031, 0.463, 0.91, 1
                theme_text_color: 'Custom'
                text_color: 0, 0, 0, 1
                size_hint: 1, None
                height: "50dp"
                font_name: "Roboto-Bold"
                on_release: app.root.current = 'LenderScreen1'


<LenderScreen1>:
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
        spacing: dp(30)
        padding: dp(50)
        MDLabel:
            text: ""
            size_hint_y: None
            height: 100

        MDLabel:
            text: 'Lender Registration Form'
            halign: 'center'
            bold: True
            size_hint_y: None
            height: 50

        MDTextField:
            id: username
            hint_text: 'Enter mobile number'
            multiline: False
            helper_text: 'Enter valid number'
            helper_text_mode: 'on_focus'
            font_name: "Roboto-Bold"
            hint_text_color: 0, 0, 0, 1

        MDTextField:
            id: username
            hint_text: 'Enter alternate email'
            multiline: False
            helper_text: 'Enter valid email'
            helper_text_mode: 'on_focus'
            hint_text_color: 0, 0, 0, 1
            font_name: "Roboto-Bold"

        GridLayout:
            cols: 2
            spacing: 30

            MDRaisedButton:
                text: "Back"
                on_release: app.root.current = 'lender_registration_form'
                md_bg_color: 0.031, 0.463, 0.91, 1
                theme_text_color: 'Custom'
                text_color: 0, 0, 0, 1
                size_hint: 1, None
                height: "50dp"
                font_name: "Roboto-Bold"

            MDRaisedButton:
                text: "Next"
                on_release: app.root.current = 'LenderScreen2'
                md_bg_color: 0.031, 0.463, 0.91, 1
                pos_hint: {'right': 1, 'y': 0.5}
                text_color: 0, 0, 0, 1
                size_hint: 1, None
                height: "50dp"
                font_name: "Roboto-Bold"

<LenderScreen2>:
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
        spacing: dp(30)
        padding: dp(50)
        MDLabel:
            text:""
            size_hint_y: None
            height: 50

        MDLabel:
            text: 'Lender Registration Form'
            halign: 'center'
            bold: True                

        MDTextField:
            id: aadhar_number
            hint_text: 'Enter Government ID1 '
            multiline: False
            helper_text: 'Enter valid number'
            helper_text_mode: 'on_focus'
            size_hint_y: None
            height: self.minimum_height
            hint_text_color: 0, 0, 0, 1


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

            MDIcon:
                icon: 'upload'
                theme_text_color: "Custom"
                text_color: 0, 0, 0, 1  # Black text color
                size_hint_x: None
                width: dp(24)
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            MDLabel:
                text: 'Upload Govt ID1'
                halign: 'left'
                theme_text_color: "Custom"
                text_color: 0, 0, 0, 1  # Black text color
                size_hint_y: None
                height: dp(36)
                valign: 'middle'  # Align the label text vertically in the center
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
 

        MDTextField:
            id: pan_number
            hint_text: 'Enter Government ID2 '
            multiline: False
            helper_text: 'Enter valid number'
            helper_text_mode: 'on_focus'
            size_hint_y: None
            height: self.minimum_height
            hint_text_color: 0, 0, 0, 1

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


            MDIcon:
                icon: 'upload'
                theme_text_color: "Custom"
                text_color: 0, 0, 0, 1  # Black text color
                size_hint_x: None
                width: dp(24)
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            MDLabel:
                text: 'Upload Govt ID2'
                halign: 'left'
                theme_text_color: "Custom"
                text_color: 0, 0, 0, 1  # Black text color
                size_hint_y: None
                height: dp(36)
                valign: 'middle'  # Align the label text vertically in the center
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}


        GridLayout:
            cols: 2
            spacing: 30

            MDRaisedButton:
                text: "Back"
                on_release: app.root.current = 'LenderScreen1'
                md_bg_color: 0.031, 0.463, 0.91, 1
                theme_text_color: 'Custom'
                text_color: 0, 0, 0, 1
                size_hint: 1, None
                height: "50dp"
                font_name: "Roboto-Bold"

            MDRaisedButton:
                text: "Next"
                on_release: app.root.current = 'LenderScreen3'
                md_bg_color: 0.031, 0.463, 0.91, 1
                pos_hint: {'right': 1, 'y': 0.5}
                text_color: 0, 0, 0, 1
                size_hint: 1, None
                height: "50dp"
                font_name: "Roboto-Bold"

<LenderScreen3>:
    MDRectangleFlatButton:
        text: 'HOME'
        text_color: 0, 0, 0, 1  # Black text color
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        md_bg_color: 0.031, 0.463, 0.91, 1
        pos_hint: {'right': 1, 'top': 1}
        on_release: app.go_home()
        size_hint: (0.1, 0.03)
        font_size: "13sp"

    BoxLayout:
        orientation: 'vertical'
        spacing: dp(30)
        padding: dp(50)
        MDLabel:
            text: ""
            size_hint_y: None
            height: 100

        MDLabel:
            text: 'Lender Registration Form'
            halign: 'center'
            bold: True
            size_hint_y: None
            height: 50 

        MDLabel:
            text: 'Education Details'
            halign: 'center'
            bold: True

        Spinner:
            id: spinner_id
            text: "select education details"
            values: ["Select Education Details", "10th class", "Intermediate", "Bachelors", "Masters", "PHD"]
            multiline:False
            size_hint_y: (None)
            background_color: (0,0,0,0)
            background_normal: ''
            color: 0,0,0,1
            canvas.before:
                Color:
                    rgba: 0, 0, 0, 1  # Border color (black in this example)
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

        GridLayout:
            cols: 2
            spacing: 30

            MDRaisedButton:
                text: "Back"
                on_release: app.root.current = 'LenderScreen2'
                md_bg_color: 0.031, 0.463, 0.91, 1
                theme_text_color: 'Custom'
                text_color: 0, 0, 0, 1
                size_hint: 1, None
                height: "50dp"
                font_name: "Roboto-Bold"

            MDRaisedButton:
                text: "Next"
                on_press: root.next_pressed(spinner_id.text)
                md_bg_color: 0.031, 0.463, 0.91, 1
                pos_hint: {'right': 1, 'y': 0.5}
                text_color: 0, 0, 0, 1
                size_hint: 1, None
                height: "50dp"
                font_name: "Roboto-Bold"

        MDLabel:
            text: ""

<LenderScreen_Edu_10th>:
    MDRectangleFlatButton:
        text: 'HOME'
        text_color: 0, 0, 0, 1  # Black text color
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        md_bg_color: 0.031, 0.463, 0.91, 1
        pos_hint: {'right': 1, 'top': 1}
        on_release: app.go_home()
        size_hint: (0.1, 0.03)
        font_size: "13sp"


    BoxLayout:
        orientation: 'vertical'
        spacing: dp(30)
        padding: dp(20)
        MDLabel:
            text: ""


        MDLabel:
            text: 'Education Details'

            halign: 'center'
            bold: True
            size_hint_y: None
            height: 50

        MDLabel:
            text: "Upload 10th class certificate"

            halign: 'center'
            bold:True
            size_hint_y: None
            height: 50


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


            MDIcon:
                icon: 'upload'
                theme_text_color: "Custom"
                text_color: 0, 0, 0, 1  # Black text color
                size_hint_x: None
                width: dp(24)
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            MDLabel:
                text: 'Upload Certificate'
                halign: 'left'
                theme_text_color: "Custom"
                text_color: 0, 0, 0, 1  # Black text color
                size_hint_y: None
                height: dp(36)
                valign: 'middle'  # Align the label text vertically in the center
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}


        GridLayout:
            cols: 2
            spacing: 30

            MDRaisedButton:
                text: "Back"
                on_release: app.root.current = 'LenderScreen3'
                md_bg_color: 0.031, 0.463, 0.91, 1
                theme_text_color: 'Custom'
                text_color: 0, 0, 0, 1
                size_hint: 1, None
                height: "50dp"
                font_name: "Roboto-Bold"

            MDRaisedButton:
                text: "Next"
                on_release: app.root.current = 'LenderScreen4'
                md_bg_color: 0.031, 0.463, 0.91, 1
                pos_hint: {'right': 1, 'y': 0.5}
                text_color: 0, 0, 0, 1
                size_hint: 1, None
                height: "50dp"
                font_name: "Roboto-Bold"

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


                MDIcon:
                    icon: 'upload'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_x: None
                    width: dp(24)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}

                MDLabel:
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


                MDIcon:
                    icon: 'upload'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_x: None
                    width: dp(24)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}

                MDLabel:
                    text: 'Upload Certificate'
                    halign: 'left'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_y: None
                    height: dp(36)
                    valign: 'middle'  # Align the label text vertically in the center
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            GridLayout:
                cols: 2
                spacing: 30
                padding: [0, "30dp", 0, 0]

                MDRaisedButton:
                    text: "Back"
                    on_release: app.root.current = 'LenderScreen3'
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    theme_text_color: 'Custom'
                    text_color: 0, 0, 0, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"

                MDRaisedButton:
                    text: "Next"
                    on_release: app.root.current = 'LenderScreen4'
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 0, 0, 0, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"

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


                MDIcon:
                    icon: 'upload'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_x: None
                    width: dp(24)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}

                MDLabel:
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


                MDIcon:
                    icon: 'upload'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_x: None
                    width: dp(24)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}

                MDLabel:
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


                MDIcon:
                    icon: 'upload'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_x: None
                    width: dp(24)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}

                MDLabel:
                    text: 'Upload Certificate'
                    halign: 'left'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_y: None
                    height: dp(36)
                    valign: 'middle'  # Align the label text vertically in the center
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            GridLayout:
                cols: 2
                spacing: 30
                padding: [0, "30dp", 0, 0]

                MDRaisedButton:
                    text: "Back"
                    on_release: app.root.current = 'LenderScreen3'
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    theme_text_color: 'Custom'
                    text_color: 0, 0, 0, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"

                MDRaisedButton:
                    text: "Next"
                    on_release: app.root.current = 'LenderScreen4'
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 0, 0, 0, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"

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


                MDIcon:
                    icon: 'upload'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_x: None
                    width: dp(24)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}

                MDLabel:
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


                MDIcon:
                    icon: 'upload'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_x: None
                    width: dp(24)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}

                MDLabel:
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


                MDIcon:
                    icon: 'upload'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_x: None
                    width: dp(24)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}

                MDLabel:
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

                MDIcon:
                    icon: 'upload'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_x: None
                    width: dp(24)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}

                MDLabel:
                    text: 'Upload Certificate'
                    halign: 'left'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_y: None
                    height: dp(36)
                    valign: 'middle'  # Align the label text vertically in the center
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            GridLayout:
                cols: 2
                spacing: 30
                padding: [0, "30dp", 0, 0]

                MDRaisedButton:
                    text: "Back"
                    on_release: app.root.current = 'LenderScreen3'
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    theme_text_color: 'Custom'
                    text_color: 0, 0, 0, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"

                MDRaisedButton:
                    text: "Next"
                    on_release: app.root.current = 'LenderScreen4'
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 0, 0, 0, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"

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

                MDIcon:
                    icon: 'upload'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_x: None
                    width: dp(24)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}

                MDLabel:
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

                MDIcon:
                    icon: 'upload'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_x: None
                    width: dp(24)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}

                MDLabel:
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

                MDIcon:
                    icon: 'upload'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_x: None
                    width: dp(24)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}

                MDLabel:
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


                MDIcon:
                    icon: 'upload'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_x: None
                    width: dp(24)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}

                MDLabel:
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

                MDIcon:
                    icon: 'upload'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_x: None
                    width: dp(24)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}

                MDLabel:
                    text: 'Upload Certificate'
                    halign: 'left'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_y: None
                    height: dp(36)
                    valign: 'middle'  # Align the label text vertically in the center
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            GridLayout:
                cols: 2
                spacing: 30
                padding: [0, "30dp", 0, 0]

                MDRaisedButton:
                    text: "Back"
                    on_release: app.root.current = 'LenderScreen3'
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    theme_text_color: 'Custom'
                    text_color: 0, 0, 0, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"

                MDRaisedButton:
                    text: "Next"
                    on_release: app.root.current = 'LenderScreen4'
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 0, 0, 0, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"
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
        padding: dp(50)
        

        MDLabel:
            text: 'Lender Registration Form'
            halign: 'center'
            bold: True
        MDLabel:
            text: 'Address'
            halign: 'center'
            bold: True

        MDTextField:
            id: street_address
            hint_text: 'Enter Street Name'
            multiline: False
            helper_text: 'Enter valid address'
            helper_text_mode: 'on_focus'
            


        MDTextField:
            id: city
            hint_text: 'Enter City Name'
            multiline: False
            helper_text_mode: 'on_focus'
            size_hint_y: None
            
        MDTextField:
            id: Zip_code
            hint_text: 'Enter postal/zipcode '
            multiline: False

            helper_text_mode: 'on_focus'
            size_hint_y: None
            
        MDTextField:
            id: state
            hint_text: 'Enter State Name'
            multiline: False

            helper_text_mode: 'on_focus'
            size_hint_y: None
            
        MDTextField:
            id: country
            hint_text: 'Enter Country Name'
            multiline: False
            helper_text_mode: 'on_focus'

        GridLayout:
            cols: 2
            spacing: 30
            padding: [0, "30dp", 0, 0]

            MDRaisedButton:
                text: "Back"
                on_release: app.root.current = 'LenderScreen3'
                md_bg_color: 0.031, 0.463, 0.91, 1
                theme_text_color: 'Custom'
                text_color: 0, 0, 0, 1
                size_hint: 1, None
                height: "50dp"
                font_name: "Roboto-Bold"

            MDRaisedButton:
                text: "Next"
                on_release: app.root.current = 'LenderScreen5'
                md_bg_color: 0.031, 0.463, 0.91, 1
                pos_hint: {'right': 1, 'y': 0.5}
                text_color: 0, 0, 0, 1
                size_hint: 1, None
                height: "50dp"
                font_name: "Roboto-Bold"

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
        spacing: dp(30)
        padding: dp(50)

        MDLabel:
            text: 'Lender Registration Form'
            halign: 'center'
            bold: True

        Spinner:
            id: spinner_id
            text: "Select Loan Type"
            values: ["Select Loan Type", "Individual", "Institutional"]
            multiline:False
            size_hint_y: (None)
            background_color: (0,0,0,0)
            background_normal: ''
            color: 0,0,0,1
            canvas.before:
                Color:
                    rgba: 0, 0, 0, 1  # Border color (black in this example)
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

        MDTextField:
            id: investment
            hint_text: 'Enter investment '
            multiline: False
            helper_text: 'Enter above 10000'
            helper_text_mode: 'on_focus'

        Spinner:
            id: spinner2
            text: "Select Lending Period"
            values: ["Select Lending Period","1year", "1-2years", "2-3years", "3-4years", "above 5years"]
            multiline:False
            size_hint_y: (None)
            background_color: (0,0,0,0)
            background_normal: ''
            color: 0,0,0,1
            canvas.before:
                Color:
                    rgba: 0, 0, 0, 1  # Border color (black in this example)
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

        GridLayout:
            cols: 2
            spacing: 30
            padding: [0, "30dp", 0, 0]

            MDRaisedButton:
                text: "Back"
                on_release: app.root.current = 'LenderScreen4'
                md_bg_color: 0.031, 0.463, 0.91, 1
                theme_text_color: 'Custom'
                text_color: 0, 0, 0, 1
                size_hint: 1, None
                height: "50dp"
                font_name: "Roboto-Bold"

            MDRaisedButton:
                text: "Next"
                on_press: root.next_pressed(spinner_id.text)
                md_bg_color: 0.031, 0.463, 0.91, 1
                pos_hint: {'right': 1, 'y': 0.5}
                text_color: 0, 0, 0, 1
                size_hint: 1, None
                height: "50dp"
                font_name: "Roboto-Bold"

<LenderScreenInstitutionalForm1>:
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
        padding: dp(50)

        MDLabel:
            text: ""
            size_hint_y: None
            height: 50

        MDLabel:
            text: 'Institutional Type'
            halign: 'center'
            bold: True
            size_hint_y: None
            height: 50


        MDLabel:
            text: 'Step-1'
            halign: 'center'
            bold: True
            
        MDTextField:
            id: business_name
            hint_text: 'Enter business name '
            multiline: False
            helper_text_mode: 'on_focus'
            size_hint_y: None
            


        MDTextField:
            id: business_location
            hint_text: 'Enter business location'
            multiline: False                   
            helper_text_mode: 'on_focus'
            size_hint_y: None
            
        MDTextField:
            id:  business_address
            hint_text: 'Enter business full address'
            multiline: False

            helper_text_mode: 'on_focus'
            size_hint_y: None
            
        MDTextField:
            id:branch_name
            hint_text: 'Enter branch name'
            multiline: False                        
            helper_text_mode: 'on_focus'
            size_hint_y: None
            
        GridLayout:
            cols: 2
            spacing: 30
            padding: [0, "30dp", 0, 0]

            MDRaisedButton:
                text: "Back"
                on_release: app.root.current = 'LenderScreen5'
                md_bg_color: 0.031, 0.463, 0.91, 1
                theme_text_color: 'Custom'
                text_color: 0, 0, 0, 1
                size_hint: 1, None
                height: "50dp"
                font_name: "Roboto-Bold"

            MDRaisedButton:
                text: "Next"
                on_release: app.root.current = 'LenderScreenInstitutionalForm2'
                md_bg_color: 0.031, 0.463, 0.91, 1
                pos_hint: {'right': 1, 'y': 0.5}
                text_color: 0, 0, 0, 1
                size_hint: 1, None
                height: "50dp"
                font_name: "Roboto-Bold"

<LenderScreenInstitutionalForm2>:

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
        padding: dp(50)
        
        
        MDLabel:
            text: 'Step-2'
            halign: 'center'
            bold: True

        Spinner:
            id: spin
            text: "Select Business Type"
            values: ["Select Business Type","Partnership", "Cooperation", "Cooperative", "Solo Proprietorship", "Cash", "Cheque", "Online Transaction", "Limited Liability Company"]
            multiline:False
            background_color: (0,0,0,0)
            size_hint_y: None
            background_normal: ''
            color: 0,0,0,1
            canvas.before:
                Color:
                    rgba: 0, 0, 0, 1  # Border color (black in this example)
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)
        MDTextField:
            id: nearest_location
            hint_text: 'Enter nearest location '
            multiline: False
            helper_text_mode: 'on_focus'
            size_hint_y: None
            

        Spinner:
            id: spinner_id
            text: "Select No.Of Employees Working"
            values: ["Select No.Of Employees Working", "1-10", "10-50", "50-100", "100-200", "200-500", "500-100", "1000+"]
            multiline:False
            size_hint_y: (None)
            background_color: (0,0,0,0)
            background_normal: ''
            color: 0,0,0,1
            canvas.before:
                Color:
                    rgba: 0, 0, 0, 1  # Border color (black in this example)
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)
        MDTextField:
            id:year_of_estd
            hint_text: 'Enter year of estd'
            multiline: False                        
            helper_text_mode: 'on_focus'
            
        GridLayout:
            cols: 2
            spacing: 30
            padding: [0, "30dp", 0, 0]

            MDRaisedButton:
                text: "Back"
                on_release: app.root.current = 'LenderScreenInstitutionalForm1'
                md_bg_color: 0.031, 0.463, 0.91, 1
                theme_text_color: 'Custom'
                text_color: 0, 0, 0, 1
                size_hint: 1, None
                height: "50dp"
                font_name: "Roboto-Bold"

            MDRaisedButton:
                text: "Next"
                on_release: app.root.current = 'LenderScreenInstitutionalForm3'
                md_bg_color: 0.031, 0.463, 0.91, 1
                pos_hint: {'right': 1, 'y': 0.5}
                text_color: 0, 0, 0, 1
                size_hint: 1, None
                height: "50dp"
                font_name: "Roboto-Bold"


<LenderScreenInstitutionalForm3>:
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
        padding: dp(50)
        
        MDLabel:
            text: 'Step-3'
            halign: 'center'
            bold: True

        Spinner:
            id: spinner_id
            text: "Select Industry Type"
            values: ["Select Industry Type","Public", "Government"]
            multiline:False
            size_hint_y: (None)
            background_color: (0,0,0,0)
            background_normal: ''
            color: 0,0,0,1
            canvas.before:
                Color:
                    rgba: 0, 0, 0, 1  # Border color (black in this example)
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)


        MDTextField:
            id: last_six_months_turnover
            hint_text: 'Enter last 6 months turnover'
            multiline: False                   
            helper_text_mode: 'on_focus'
            size_hint_y: None
            
        MDLabel:
            text: "Last 6 months bank statements"
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


            MDIcon:
                icon: 'upload'
                theme_text_color: "Custom"
                text_color: 0, 0, 0, 1  # Black text color
                size_hint_x: None
                width: dp(24)
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            MDLabel:
                text: 'Upload Document'
                halign: 'left'
                theme_text_color: "Custom"
                text_color: 0, 0, 0, 1  # Black text color
                size_hint_y: None
                height: dp(36)
                valign: 'middle'  # Align the label text vertically in the center
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}

        GridLayout:
            cols: 2
            spacing: 30
            padding: [0, "30dp", 0, 0]

            MDRaisedButton:
                text: "Back"
                on_release: app.root.current = 'LenderScreenInstitutionalForm2'
                md_bg_color: 0.031, 0.463, 0.91, 1
                theme_text_color: 'Custom'
                text_color: 0, 0, 0, 1
                size_hint: 1, None
                height: "50dp"
                font_name: "Roboto-Bold"

            MDRaisedButton:
                text: "Next"
                on_release: app.root.current = 'LenderScreenInstitutionalForm4'
                md_bg_color: 0.031, 0.463, 0.91, 1
                pos_hint: {'right': 1, 'y': 0.5}
                text_color: 0, 0, 0, 1
                size_hint: 1, None
                height: "50dp"
                font_name: "Roboto-Bold"

<LenderScreenInstitutionalForm4>:
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
        padding: dp(50)
        
        MDLabel:
            text: 'Step-4'
            halign: 'center'
            bold: True

        MDTextField:
            id: director_name
            hint_text: 'Enter director name '
            multiline: False
            helper_text_mode: 'on_focus'
            size_hint_y: None

        MDTextField:
            id: director_mobile_number
            hint_text: 'Enter director mobile number'
            multiline: False                   
            helper_text_mode: 'on_focus'
            size_hint_y: None
            
        MDTextField:
            id:  din
            hint_text: 'Enter DIN'
            multiline: False
            helper_text_mode: 'on_focus'
            size_hint_y: None

        MDTextField:
            id:cin
            hint_text: 'Enter CIN'
            multiline: False                        
            helper_text_mode: 'on_focus'
            size_hint_y: None

        GridLayout:
            cols: 2
            spacing: 30
            padding: [0, "30dp", 0, 0]

            MDRaisedButton:
                text: "Back"
                on_release: app.root.current = 'LenderScreenInstitutionalForm3'
                md_bg_color: 0.031, 0.463, 0.91, 1
                theme_text_color: 'Custom'
                text_color: 0, 0, 0, 1
                size_hint: 1, None
                height: "50dp"
                font_name: "Roboto-Bold"

            MDRaisedButton:
                text: "Next"
                on_release: app.root.current = 'LenderScreenInstitutionalForm5'
                md_bg_color: 0.031, 0.463, 0.91, 1
                pos_hint: {'right': 1, 'y': 0.5}
                text_color: 0, 0, 0, 1
                size_hint: 1, None
                height: "50dp"
                font_name: "Roboto-Bold"

<LenderScreenInstitutionalForm5>:
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
        padding: dp(50)

        MDLabel:
            text: 'Step-5'
            halign: 'center'
            bold: True

        MDTextField:
            id: reg_office_address
            hint_text: 'Enter registered office address '
            multiline: False
            helper_text_mode: 'on_focus'
            size_hint_y: None
            
        MDLabel:
            text: "Proof of verification"
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


            MDIcon:
                icon: 'upload'
                theme_text_color: "Custom"
                text_color: 0, 0, 0, 1  # Black text color
                size_hint_x: None
                width: dp(24)
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            MDLabel:
                text: 'Upload Document'
                halign: 'left'
                theme_text_color: "Custom"
                text_color: 0, 0, 0, 1  # Black text color
                size_hint_y: None
                height: dp(36)
                valign: 'middle'  # Align the label text vertically in the center
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        MDTextField:
            id:branch_name
            hint_text: 'Enter branch name'
            multiline: False                        
            helper_text_mode: 'on_focus'
            size_hint_y: None
            
        GridLayout:
            cols: 2
            spacing: 30
            padding: [0, "30dp", 0, 0]

            MDRaisedButton:
                text: "Back"
                on_release: app.root.current = 'LenderScreenInstitutionalForm4'
                md_bg_color: 0.031, 0.463, 0.91, 1
                theme_text_color: 'Custom'
                text_color: 0, 0, 0, 1
                size_hint: 1, None
                height: "50dp"
                font_name: "Roboto-Bold"

            MDRaisedButton:
                text: "Next"
                on_release: app.root.current = 'LenderScreenInstitutionalBankForm1'
                md_bg_color: 0.031, 0.463, 0.91, 1
                pos_hint: {'right': 1, 'y': 0.5}
                text_color: 0, 0, 0, 1
                size_hint: 1, None
                height: "50dp"
                font_name: "Roboto-Bold"


<LenderScreenIndividualForm1>:

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
        spacing: dp(15)
        padding: dp(50)
        MDLabel:
            text: ""
            size_hint_y: None
            height: 50
                    
        MDLabel:
            text: 'Individual Type'
            halign: 'center'
            bold: True

        MDLabel:
            text: 'Employment Details'
            halign: 'center'
            bold: True   
            size_hint_y: None

        Spinner:
            id: spinner1
            text: "Employment Type"
            values: ["Employment Type","Intern", "Full Time", "Contract"]
            multiline:False
            size_hint_y: (None)
            background_color: (0,0,0,0)
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
            hint_text: 'Enter company_name'
            multiline: False                        
            helper_text_mode: 'on_focus'
            size_hint_y: None
            
        Spinner:
            id: spinner2
            text: "Select Organisation Type"
            values: ["Select Organisation Type","Public", "Private", "Cooperation", "Partnership"]
            multiline:False
            size_hint_y: (None)
            background_color: (0,0,0,0)
            background_normal: ''
            color: 0,0,0,1
            canvas.before:
                Color:
                    rgba: 0, 0, 0, 1  # Border color (black in this example)
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

        GridLayout:
            cols: 2
            spacing: 30
            padding: [0, "30dp", 0, 0]

            MDRaisedButton:
                text: "Back"
                on_release: app.root.current = 'LenderScreen5'
                md_bg_color: 0.031, 0.463, 0.91, 1
                theme_text_color: 'Custom'
                text_color: 0, 0, 0, 1
                size_hint: 1, None
                height: "50dp"
                font_name: "Roboto-Bold"

            MDRaisedButton:
                text: "Next"
                on_release: app.root.current = 'LenderScreenIndividualForm2'
                md_bg_color: 0.031, 0.463, 0.91, 1
                pos_hint: {'right': 1, 'y': 0.5}
                text_color: 0, 0, 0, 1
                size_hint: 1, None
                height: "50dp"
                font_name: "Roboto-Bold"     

<LenderScreenIndividualForm2>:
    name: 'len_reg_individual_form2'
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
        padding: dp(50)
        MDLabel:
            text: ""
            size_hint_y: None
            height: 50
        
        MDLabel:
            text: 'Employment Details'
            halign: 'center'
            bold: True   
        MDTextField:              
            id:company_address
            hint_text: 'Enter company address'
            multiline: False                        
            helper_text_mode: 'on_focus'
            size_hint_y: None
            
        MDTextField:              
            id:company_pin_code
            hint_text: 'Enter Company Pincode'
            multiline: False                        
            helper_text_mode: 'on_focus'
            size_hint_y: None
            
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
            id:business_phone_number
            hint_text: 'Enter business phone number'
            multiline: False                        
            helper_text_mode: 'on_focus'
            size_hint_y: None
            
        GridLayout:
            cols: 2
            spacing: 30
            padding: [0, "30dp", 0, 0]

            MDRaisedButton:
                text: "Back"
                on_release: app.root.current = 'LenderScreenIndividualForm1'
                md_bg_color: 0.031, 0.463, 0.91, 1
                theme_text_color: 'Custom'
                text_color: 0, 0, 0, 1
                size_hint: 1, None
                height: "50dp"
                font_name: "Roboto-Bold"

            MDRaisedButton:
                text: "Next"
                on_release: app.root.current = 'LenderScreenIndividualForm3'
                md_bg_color: 0.031, 0.463, 0.91, 1
                pos_hint: {'right': 1, 'y': 0.5}
                text_color: 0, 0, 0, 1
                size_hint: 1, None
                height: "50dp"
                font_name: "Roboto-Bold"

<LenderScreenIndividualForm3>:
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
        padding: dp(50)
        
        MDLabel:
            text: 'Employment Details'
            halign: 'center'
            bold: True   
        MDTextField:              
            id:annual_salary
            hint_text: 'Enter annual salary'
            multiline: False                        
            helper_text_mode: 'on_focus'
            size_hint_y: None
            
        MDTextField:              
            id:designation
            hint_text: 'Enter designation'
            multiline: False                        
            helper_text_mode: 'on_focus'
            size_hint_y: None
            
        MDLabel:
            text: "Upload Employee ID"
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


            MDIcon:
                icon: 'upload'
                theme_text_color: "Custom"
                text_color: 0, 0, 0, 1  # Black text color
                size_hint_x: None
                width: dp(24)
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            MDLabel:
                text: 'Upload Document'
                halign: 'left'
                theme_text_color: "Custom"
                text_color: 0, 0, 0, 1  # Black text color
                size_hint_y: None
                height: dp(36)
                valign: 'middle'  # Align the label text vertically in the center
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}

        MDLabel:
            text: "Upload last 6 months bank statements"
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


            MDIcon:
                icon: 'upload'
                theme_text_color: "Custom"
                text_color: 0, 0, 0, 1  # Black text color
                size_hint_x: None
                width: dp(24)
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            MDLabel:
                text: 'Upload Document'
                halign: 'left'
                theme_text_color: "Custom"
                text_color: 0, 0, 0, 1  # Black text color
                size_hint_y: None
                height: dp(36)
                valign: 'middle'  # Align the label text vertically in the center
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}

        GridLayout:
            cols: 2
            spacing: 30
            padding: [0, "30dp", 0, 0]

            MDRaisedButton:
                text: "Back"
                on_release: app.root.current = 'LenderScreenIndividualForm2'
                md_bg_color: 0.031, 0.463, 0.91, 1
                theme_text_color: 'Custom'
                text_color: 0, 0, 0, 1
                size_hint: 1, None
                height: "50dp"
                font_name: "Roboto-Bold"

            MDRaisedButton:
                text: "Next"
                on_release: app.root.current = 'LenderScreenIndividualBankForm1'
                md_bg_color: 0.031, 0.463, 0.91, 1
                pos_hint: {'right': 1, 'y': 0.5}
                text_color: 0, 0, 0, 1
                size_hint: 1, None
                height: "50dp"
                font_name: "Roboto-Bold"        


<LenderScreenIndividualBankForm1>:

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
        spacing: dp(15)
        padding: dp(50)
        
        MDLabel:
            text: 'Applicant Bank Details'
            halign: 'center'
            bold: True

        MDTextField:
            id: account_holder_name
            hint_text: 'Enter account holder name '
            multiline: False
            helper_text: 'Enter valid account holder name'
            helper_text_mode: 'on_focus'
            size_hint_y: None
            
        Spinner:
            id: spinner_id
            text: "Select Account Type"
            values: ["Select Account Type","Savings", "Current", "NRI"]
            multiline:False
            size_hint_y: (None)
            background_color: (0,0,0,0)
            background_normal: ''
            color: 0,0,0,1
            canvas.before:
                Color:
                    rgba: 0, 0, 0, 1  # Border color (black in this example)
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)


        MDTextField:
            id: account_number
            hint_text: 'Enter account number '
            multiline: False
            helper_text: 'Enter valid account number'
            helper_text_mode: 'on_focus'
            size_hint_y: None
            
        MDTextField:
            id: bank_name
            hint_text: 'Enter bank name '
            multiline: False
            helper_text_mode: 'on_focus'
            size_hint_y: None
            
        GridLayout:
            cols: 2
            spacing: 30
            padding: [0, "30dp", 0, 0]

            MDRaisedButton:
                text: "Back"
                on_release: app.root.current = 'LenderScreenIndividualForm3'
                md_bg_color: 0.031, 0.463, 0.91, 1
                theme_text_color: 'Custom'
                text_color: 0, 0, 0, 1
                size_hint: 1, None
                height: "50dp"
                font_name: "Roboto-Bold"

            MDRaisedButton:
                text: "Next"
                on_release: app.root.current = 'LenderScreenIndividualBankForm2'
                md_bg_color: 0.031, 0.463, 0.91, 1
                pos_hint: {'right': 1, 'y': 0.5}
                text_color: 0, 0, 0, 1
                size_hint: 1, None
                height: "50dp"
                font_name: "Roboto-Bold" 

<LenderScreenIndividualBankForm2>:
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
        spacing: dp(15)
        padding: dp(50)
        
        MDLabel:
            text: 'Applicant Bank Details'
            halign: 'center'
            bold: True

        MDTextField:
            id: ifsc_code
            hint_text: 'Enter Bank ID '
            multiline: False
            helper_text: 'Enter valid ifsc code'
            helper_text_mode: 'on_focus'
            size_hint_y: None
           
        MDTextField:
            id: branch_name
            hint_text: 'Enter branch name'
            multiline: False
            helper_text_mode: 'on_focus'
            size_hint_y: None
            
        GridLayout:
            cols: 2
            spacing: 30
            padding: [0, "30dp", 0, 0]

            MDRaisedButton:
                text: "Back"
                on_release: app.root.current = 'LenderScreenIndividualBankForm1'
                md_bg_color: 0.031, 0.463, 0.91, 1
                theme_text_color: 'Custom'
                text_color: 0, 0, 0, 1
                size_hint: 1, None
                height: "50dp"
                font_name: "Roboto-Bold"

            MDRaisedButton:
                text: "Submit"
                on_release: root.go_to_lender_dashboard()
                md_bg_color: 0.031, 0.463, 0.91, 1
                pos_hint: {'right': 1, 'y': 0.5}
                text_color: 0, 0, 0, 1
                size_hint: 1, None
                height: "50dp"
                font_name: "Roboto-Bold" 



<LenderScreenInstitutionalBankForm1>:
    name: 'len_reg_institutional_bank_form1'
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
        spacing: dp(15)
        padding: dp(50)
 
        MDLabel:
            text: 'Applicant Bank Details'
            halign: 'center'
            bold: True

        MDTextField:
            id: account_holder_name
            hint_text: 'Enter account holder name '
            multiline: False
            helper_text: 'Enter valid account holder name'
            helper_text_mode: 'on_focus'
            size_hint_y: None
            
        Spinner:
            id: spinner_id
            text: "Select Account Type"
            values: ["Select Account Type","Savings", "Current", "NRI"]
            multiline:False
            size_hint_y: (None)
            background_color: (0,0,0,0)
            background_normal: ''
            color: 0,0,0,1
            canvas.before:
                Color:
                    rgba: 0, 0, 0, 1  # Border color (black in this example)
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)



        MDTextField:
            id: account_number
            hint_text: 'Enter account number '
            multiline: False
            helper_text: 'Enter valid account number'
            helper_text_mode: 'on_focus'
            size_hint_y: None
            
        MDTextField:
            id: bank_name
            hint_text: 'Enter bank name '
            multiline: False
            helper_text_mode: 'on_focus'
            size_hint_y: None
            
        GridLayout:
            cols: 2
            spacing: 30
            padding: [0, "30dp", 0, 0]

            MDRaisedButton:
                text: "Back"
                on_release: app.root.current = 'LenderScreenInstitutionalForm5'
                md_bg_color: 0.031, 0.463, 0.91, 1
                theme_text_color: 'Custom'
                text_color: 0, 0, 0, 1
                size_hint: 1, None
                height: "50dp"
                font_name: "Roboto-Bold"

            MDRaisedButton:
                text: "Next"
                on_release: app.root.current = 'LenderScreenInstitutionalBankForm2'
                md_bg_color: 0.031, 0.463, 0.91, 1
                pos_hint: {'right': 1, 'y': 0.5}
                text_color: 0, 0, 0, 1
                size_hint: 1, None
                height: "50dp"
                font_name: "Roboto-Bold"   

<LenderScreenInstitutionalBankForm2>:
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
        spacing: dp(15)
        padding: dp(50)
        
        MDLabel:
            text: 'Applicant Bank Details'
            halign: 'center'
            bold: True

        MDTextField:
            id: ifsc_code
            hint_text: 'Enter Bank ID '
            multiline: False
            helper_text: 'Enter valid ifsc code'
            helper_text_mode: 'on_focus'
            size_hint_y: None
            
        MDTextField:
            id: branch_name
            hint_text: 'Enter branch name'
            multiline: False
            helper_text_mode: 'on_focus'
            size_hint_y: None
            
        GridLayout:
            cols: 2
            spacing: 30
            padding: [0, "30dp", 0, 0]

            MDRaisedButton:
                text: "Back"
                on_release: app.root.current = 'LenderScreenInstitutionalBankForm1'
                md_bg_color: 0.031, 0.463, 0.91, 1
                theme_text_color: 'Custom'
                text_color: 0, 0, 0, 1
                size_hint: 1, None
                height: "50dp"
                font_name: "Roboto-Bold"

            MDRaisedButton:
                text: "Submit"
                on_release: root.go_to_lender_dashboard()
                md_bg_color: 0.031, 0.463, 0.91, 1
                pos_hint: {'right': 1, 'y': 0.5}
                text_color: 0, 0, 0, 1
                size_hint: 1, None
                height: "50dp"
                font_name: "Roboto-Bold"


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
    def next_pressed(self, id):
        if id == 'Individual':
            self.manager.current = 'LenderScreenIndividualForm1'

        elif id == 'Institutional':
            self.manager.current = 'LenderScreenInstitutionalForm1'


class LenderScreenInstitutionalForm1(Screen):
    pass


class LenderScreenInstitutionalForm2(Screen):
    pass


class LenderScreenInstitutionalForm3(Screen):
    pass


class LenderScreenInstitutionalForm4(Screen):
    pass


class LenderScreenInstitutionalForm5(Screen):
    pass


class LenderScreenIndividualForm1(Screen):
    pass


class LenderScreenIndividualForm2(Screen):
    pass


class LenderScreenIndividualForm3(Screen):
    pass


class LenderScreenIndividualBankForm1(Screen):
    pass


class LenderScreenIndividualBankForm2(Screen):
    def go_to_lender_dashboard(self):
        self.manager.current = 'lender_dashboard'


class LenderScreenInstitutionalBankForm1(Screen):
    pass


class LenderScreenInstitutionalBankForm2(Screen):


    def go_to_lender_dashboard(self):
        self.manager.current = 'lender_dashboard'