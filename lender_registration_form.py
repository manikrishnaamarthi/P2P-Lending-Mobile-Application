from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.lang import Builder
from kivymd.uix.button import MDRectangleFlatButton
from kivy.metrics import dp
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.pickers import MDDatePicker

KV = '''
<LenderScreen>:

    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: root.go_to_dashboard()]]
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
                text: 'Lender Registration Form'
                halign: 'center'
                font_size: "20dp"
                font_name: "Roboto-Bold"
                size_hint_y: None
                height:dp(50)
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
                size_hint: 1, None
                height: "40dp"
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



            MDRectangleFlatButton:
                text: 'Next'
                md_bg_color: 0.031, 0.463, 0.91, 1
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                size_hint: 1, None
                height: "50dp"
                font_name: "Roboto-Bold"
                on_release: app.root.current = 'LenderScreen1'


<LenderScreen1>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'lender_registration_form')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard]]
        title_align: 'center'  # Center-align the title

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(30)
        padding: dp(30)
        MDLabel:
            text: ""
            size_hint_y: None
            height:dp(50)
        MDLabel:
            text: ""
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
                text: 'Lender Registration Form'
                halign: 'center'
                font_size: "20sp"
                font_name: "Roboto-Bold"
                size_hint_y: None
                height:dp(50)

            MDTextField:
                id: username
                hint_text: 'Enter mobile number'
                multiline: False
                helper_text: 'Enter valid number'
                helper_text_mode: 'on_focus'
                font_name: "Roboto-Bold"
                hint_text_color: 0,0,0, 1

            MDTextField:
                id: username
                hint_text: 'Enter your alternate email'
                multiline: False
                helper_text: 'Enter your valid email_id'
                helper_text_mode: 'on_focus'
                hint_text_color: 0, 0, 0, 1
                font_name: "Roboto-Bold"

            Spinner:
                id: spinner_id
                text: "Please Select your References"
                values: ["Select your References" ,"Google", "Facebook", "Ads","Electronic media","Others"]
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
                cols: 1
                spacing:dp(30)



                MDRectangleFlatButton:
                    text: "Next"
                    on_release: app.root.current = 'LenderScreen2'
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"

<LenderScreen2>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'LenderScreen1')]]
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
                text: 'Lender Registration Form'
                halign: 'center'
                font_size: "20sp"
                font_name: "Roboto-Bold"               

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


            MDRectangleFlatButton:
                text: "Next"
                on_release: app.root.current = 'LenderScreen3'
                md_bg_color: 0.031, 0.463, 0.91, 1
                pos_hint: {'right': 1, 'y': 0.5}
                text_color: 1, 1, 1, 1
                size_hint: 1, None
                height: "50dp"
                font_name: "Roboto-Bold"

<LenderScreen3>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'LenderScreen2')]]
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
                text: 'Lender Registration Form'
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
                cols: 1
                spacing:dp(30)

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

<LenderScreen_Edu_10th>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'LenderScreen3')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(30)
        padding: dp(30)
        MDLabel:
            text: ""
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
                text: 'Education Details'

                halign: 'center'
                bold: True
                size_hint_y: None
                height:dp(50)

            MDLabel:
                text: "Upload 10th class certificate"

                halign: 'center'
                bold:True
                size_hint_y: None
                height:dp(50)


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
                cols: 1
                spacing:dp(30)

                MDRectangleFlatButton:
                    text: "Next"
                    on_release: app.root.current = 'LenderScreen4'
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"

<LenderScreen_Edu_Intermediate>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'LenderScreen3')]]
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
                cols: 1
                spacing:dp(30)
                padding: [0, "30dp", 0, 0]


                MDRectangleFlatButton:
                    text: "Next"
                    on_release: app.root.current = 'LenderScreen4'
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"

<LenderScreen_Edu_Bachelors>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'LenderScreen3')]]
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
                cols: 1
                spacing:dp(30)
                padding: [0, "30dp", 0, 0]


                MDRectangleFlatButton:
                    text: "Next"
                    on_release: app.root.current = 'LenderScreen4'
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"

<LenderScreen_Edu_Masters>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'LenderScreen3')]]
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
                cols: 1
                spacing:dp(30)
                padding: [0, "30dp", 0, 0]

                MDRectangleFlatButton:
                    text: "Next"
                    on_release: app.root.current = 'LenderScreen4'
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"

<LenderScreen_Edu_PHD>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'LenderScreen3')]]
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
                cols: 1
                spacing:dp(30)
                padding: [0, "30dp", 0, 0]


                MDRectangleFlatButton:
                    text: "Next"
                    on_release: app.root.current = 'LenderScreen4'
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"
<LenderScreen4>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'LenderScreen3')]]
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
                text: 'Lender Registration Form'
                halign: 'center'
                font_name: "Roboto-Bold"
                font_size: "20dp"
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
                id: Zip_code
                hint_text: 'Enter postal/zipcode '
                multiline: False
                helper_text_mode: 'on_focus'
                size_hint_y: None  
            MDTextField:
                id: street_address
                hint_text: 'Enter Street Name'
                multiline: False
                helper_text: 'Enter valid address'
                helper_text_mode: 'on_focus'

            GridLayout:
                cols: 1
                spacing: dp(30)
                padding: [0, "30dp", 0, 0]


                MDRectangleFlatButton:
                    text: "Next"
                    on_release: app.root.current = 'LenderScreen5'
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"
<LenderScreen5>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'LenderScreen4')]]
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
                text: 'Lender Registration Form'
                font_size: "20dp"
                halign: 'center'
                font_name: "Roboto-Bold"

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
                hint_text: 'Enter investment Amount '
                multiline: False
                helper_text: 'Enter above 100000'
                helper_text_mode: 'on_focus'

            Spinner:
                id: spinner2
                text: "Select Lending Period"
                values: ["Select Lending Period","1-year", "1-2 years", "2-3 years", "3-4 years", "5-years Above"]
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
                cols: 1
                spacing:dp(30)
                padding: [0, "30dp", 0, 0]



                MDRaisedButton:
                    text: "Next"
                    on_press: root.next_pressed(spinner_id.text)
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"
<LenderScreenInstitutionalForm1>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'LenderScreen5')]]
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
                text: 'Institutional Type'
                halign: 'center'
                bold: True
                size_hint_y: None
                height:dp(50)


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
                cols: 1
                spacing:dp(30)
                padding: [0, "30dp", 0, 0]



                MDRaisedButton:
                    text: "Next"
                    on_release: app.root.current = 'LenderScreenInstitutionalForm2'
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"

<LenderScreenInstitutionalForm2>:

    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'LenderScreenInstitutionalForm1')]]
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
                text: 'Step-2'
                halign: 'center'
                bold: True

            Spinner:
                id: spin
                text: "Please Select Business Type"
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
                cols: 1
                spacing:dp(30)
                padding: [0, "30dp", 0, 0]

                MDRaisedButton:
                    text: "Next"
                    on_release: app.root.current = 'LenderScreenInstitutionalForm3'
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"


<LenderScreenInstitutionalForm3>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'LenderScreenInstitutionalForm2')]]
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
                cols: 1
                spacing:dp(30)
                padding: [0, "30dp", 0, 0]



                MDRaisedButton:
                    text: "Next"
                    on_release: app.root.current = 'LenderScreenInstitutionalForm4'
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"

<LenderScreenInstitutionalForm4>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'LenderScreenInstitutionalForm3')]]
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
                cols: 1
                spacing:dp(30)
                padding: [0, "30dp", 0, 0]



                MDRaisedButton:
                    text: "Next"
                    on_release: app.root.current = 'LenderScreenInstitutionalForm5'
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"

<LenderScreenInstitutionalForm5>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'LenderScreenInstitutionalForm4')]]
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
                cols: 1
                spacing:dp(30)
                padding: [0, "30dp", 0, 0]

                MDRaisedButton:
                    text: "Next"
                    on_release: app.root.current = 'LenderScreenInstitutionalBankForm1'
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"


<LenderScreenIndividualForm1>:

    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'LenderScreen5')]]
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
                text: ""
                size_hint_y: None
                height:dp(50)

            MDLabel:
                text: 'Individual Type'
                halign: 'center'
                font_size: "20dp"
                font_name: "Roboto-Bold"

            MDLabel:
                text: 'Employment Details'
                halign: 'center'
                bold: True   
                size_hint_y: None

            Spinner:
                id: spinner1
                text: "Please Select Employment Type"
                values: ["Employment Type","Full-Time", "Part-Time","Contract","Freelance","Intern"]
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
                hint_text: 'Enter company name'
                multiline: False                        
                helper_text_mode: 'on_focus'
                size_hint_y: None

            Spinner:
                id: spinner2
                text: "Please Select Organisation Type"
                values: ["Select Organisation Type","Cooperation","Partnership","Sole proprietorship","Hierarchical Organization"]
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
                cols: 1
                spacing:dp(30)
                padding: [0, "30dp", 0, 0]


                MDRaisedButton:
                    text: "Next"
                    on_release: app.root.current = 'LenderScreenIndividualForm2'
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"
<LenderScreenIndividualForm2>:
    name: 'len_reg_individual_form2'
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'LenderScreenIndividualForm1')]]
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
                cols: 1
                spacing:dp(30)
                padding: [0, "30dp", 0, 0]


                MDRaisedButton:
                    text: "Next"
                    on_release: app.root.current = 'LenderScreenIndividualForm3'
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"

<LenderScreenIndividualForm3>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'LenderScreenIndividualForm2')]]
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
                halign: 'center'
                font_name: "Roboto-Bold"
                font_size: "20dp"   
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
                cols: 1
                spacing:dp(30)
                padding: [0, "30dp", 0, 0]

                MDRaisedButton:
                    text: "Next"
                    on_release: app.root.current = 'LenderScreenIndividualBankForm1'
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"        


<LenderScreenIndividualBankForm1>:

    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'LenderScreenIndividualForm3')]]
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
                text: 'Applicant Bank Details'
                halign: 'center'
                font_size: "20dp"
                font_name: "Roboto-Bold"

            MDTextField:
                id: account_holder_name
                hint_text: 'Enter account holder name '
                multiline: False
                helper_text: 'Enter valid account holder name'
                helper_text_mode: 'on_focus'
                size_hint_y: None

            Spinner:
                id: spinner_id
                text: "Please Select Account Type"
                values: ["Select Account Type","Savings", "Current", "NRI","Joint Account","Salary"]
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
                cols: 1
                spacing:dp(30)
                padding: [0, "30dp", 0, 0]



                MDRaisedButton:
                    text: "Next"
                    on_release: app.root.current = 'LenderScreenIndividualBankForm2'
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold" 

<LenderScreenIndividualBankForm2>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'LenderScreenIndividualBankForm1')]]
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
                text: 'Applicant Bank Details'
                halign: 'center'
                font_size: "20dp"
                font_name: "Roboto-Bold"
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
                cols: 1
                spacing:dp(30)
                padding: [0, "30dp", 0, 0]



                MDRaisedButton:
                    text: "Submit"
                    on_release: root.go_to_lender_dashboard()
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold" 



<LenderScreenInstitutionalBankForm1>:
    name: 'len_reg_institutional_bank_form1'
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'LenderScreenInstitutionalForm5')]]
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
                text: 'Applicant Bank Details'
                halign: 'center'
                font_size: "20dp"
                font_name: "Roboto-Bold"
            MDTextField:
                id: account_holder_name
                hint_text: 'Enter account holder name '
                multiline: False
                helper_text: 'Enter valid account holder name'
                helper_text_mode: 'on_focus'
                size_hint_y: None

            Spinner:
                id: spinner_id
                text: "Please Select Account Type"
                values: ["Select Account Type", "Current","Escrow Account","Payroll Account"]
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
                cols: 1
                spacing:dp(30)
                padding: [0, "30dp", 0, 0]

                MDRaisedButton:
                    text: "Next"
                    on_release: app.root.current = 'LenderScreenInstitutionalBankForm2'
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"   

<LenderScreenInstitutionalBankForm2>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'LenderScreenInstitutionalBankForm1')]]
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
                text: 'Applicant Bank Details'
                halign: 'center'
                font_size: "20dp"
                font_name: "Roboto-Bold"

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
                cols: 1
                spacing:dp(30)
                padding: [0, "30dp", 0, 0]


                MDRaisedButton:
                    text: "Submit"
                    on_release: root.go_to_lender_dashboard()
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"


'''


class LenderScreen(Screen):
    def on_pre_enter(self):
        # Bind the back button event to the on_back_button method
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        # Unbind the back button event when leaving the screen
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        # Handle the back button event
        if key == 27:  # 27 is the keycode for the hardware back button on Android
            self.go_back()
            return True  # Consume the event, preventing further handling
        return False  # Continue handling the event

    def go_back(self):
        # Navigate to the previous screen with a slide transition
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'LenderLanding'  # Replace with the actual name of your previous screen

    def go_to_dashboard(self):
        self.manager.current = 'dashboard'


class LenderScreen1(Screen):
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
        self.manager.current = 'LenderScreen'


class LenderScreen2(Screen):
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
        self.manager.current = 'LenderScreen1'


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
        self.manager.current = 'LenderScreen2'


class LenderScreen_Edu_10th(Screen):
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
        self.manager.current = 'LenderScreen3'


class LenderScreen_Edu_Intermediate(Screen):
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
        self.manager.current = 'LenderScreen3'


class LenderScreen_Edu_Bachelors(Screen):
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
        self.manager.current = 'LenderScreen3'


class LenderScreen_Edu_Masters(Screen):
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
        self.manager.current = 'LenderScreen3'


class LenderScreen_Edu_PHD(Screen):
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
        self.manager.current = 'LenderScreen3'


class LenderScreen4(Screen):
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
        self.manager.current = 'LenderScreen3'


class LenderScreen5(Screen):
    def next_pressed(self, id):
        if id == 'Individual':
            self.manager.current = 'LenderScreenIndividualForm1'

        elif id == 'Institutional':
            self.manager.current = 'LenderScreenInstitutionalForm1'

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
        self.manager.current = 'LenderScreen4'


class LenderScreenInstitutionalForm1(Screen):
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
        self.manager.current = 'LenderScreen5'


class LenderScreenInstitutionalForm2(Screen):
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
        self.manager.current = 'LenderScreenInstitutionalForm1'


class LenderScreenInstitutionalForm3(Screen):
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
        self.manager.current = 'LenderScreenInstitutionalForm2'


class LenderScreenInstitutionalForm4(Screen):
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
        self.manager.current = 'LenderScreenInstitutionalForm3'


class LenderScreenInstitutionalForm5(Screen):
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
        self.manager.current = 'LenderScreenInstitutionalForm4'


class LenderScreenIndividualForm1(Screen):
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
        self.manager.current = 'LenderScreen5'


class LenderScreenIndividualForm2(Screen):
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
        self.manager.current = 'LenderScreenIndividualForm1'


class LenderScreenIndividualForm3(Screen):
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
        self.manager.current = 'LenderScreenIndividualForm2'


class LenderScreenIndividualBankForm1(Screen):
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
        self.manager.current = 'LenderScreenIndividualForm3'


class LenderScreenIndividualBankForm2(Screen):
    def go_to_lender_dashboard(self):
        self.manager.current = 'lender_dashboard'

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
        self.manager.current = 'LenderScreenIndividualBankForm1'


class LenderScreenInstitutionalBankForm1(Screen):
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
        self.manager.current = 'LenderScreenInstitutionalForm5'


class LenderScreenInstitutionalBankForm2(Screen):

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
        self.manager.current = 'LenderScreenInstitutionalBankForm1'

    def go_to_lender_dashboard(self):
        self.manager.current = 'lender_dashboard'

    def go_to_dashboard(self):
        self.manager.current = 'dashboard'


class MyScreenManager(ScreenManager):
    pass