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
    MDRectangleFlatButton:
        text: 'HOME'
        text_color: 0, 0, 0, 1 
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        md_bg_color: 0.031, 0.463, 0.91, 1
        pos_hint: {'right': 1, 'top': 1}
        on_release: app.root.current()
        size_hint: (0.1, 0.03)
        font_size: "13sp"
    BoxLayout:
        orientation: 'vertical'
        padding: "40dp"
        MDLabel:
            text: 'Borrower Registration Form'
            font_size: 25
            halign: 'center'
            bold: True

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

        MDTextField:
            id: email
            hint_text: 'Enter Email ID'
            halign: 'left'
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1
            multiline: False
            helper_text: "Enter Valid Email ID"
            helper_text_mode: 'on_focus'
            font_name: "Roboto-Bold"
            bold: True

        Spinner:
            padding:  10
            id: gender_id
            text: "Select Gender"
            values: ["Male", "Female", "Others"]
            multiline: False
            size_hint: 1 , None
            bold: True
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

        MDTextField:
            id: mobile_no
            hint_text: ' Enter Mobile No'
            halign: 'left'
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1
            multiline: False
            helper_text: "Enter Valid Mobile No"
            helper_text_mode: 'on_focus'
            font_name: "Roboto-Bold"
            bold: True

        BoxLayout:
            orientation: 'vertical'
            padding: "40dp"

            MDRaisedButton:
                text: 'Next'
                text_color: 0, 0, 0, 1  # Black text color
                md_bg_color: 0.031, 0.463, 0.91, 1
                size_hint: 1, None
                height: "50dp"
                on_release: app.root.current = 'BorrowerScreen1'


<BorrowerScreen1>:

    MDRectangleFlatButton:
        text: 'HOME'
        text_color: 0, 0, 0, 1
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        md_bg_color: 0.031, 0.463, 0.91, 1
        pos_hint: {'right': 1, 'top': 1}
        on_release: app.root.current()
        size_hint: (0.1, 0.03)
        font_size: "13sp"

    BoxLayout:
        orientation: 'vertical'
        padding: "50dp"

        MDLabel:
            text: 'Borrower Registration Form'
            font_size: 25
            halign: 'center'
            bold: True

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

        MDRectangleFlatButton:
            text: 'Upload Profile Image'
            text_color: 0, 0, 0, 1 
            icon: 'profile-image'
            pos_hint: {'center_x': 0.5, 'center_y': 0.37}
            on_release: app.file_manager_open()
            size_hint: 1, None
            canvas.before:
                Color:
                    rgba: 0, 0, 0, 0
                Line:
                    width: 0.7  
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)


        GridLayout:
            cols: 2
            spacing: 30
            padding: 20
            pos_hint: {'center_x': 0.50, 'center_y': 0.5}
            size_hint: 1, None
            height: "50dp"

            MDRaisedButton:
                text: "Back"
                on_release: app.root.current = 'borrower_registration_forms'
                md_bg_color: 0.031, 0.463, 0.91, 1
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                size_hint: 1, None
                height: "50dp"

            MDRaisedButton:
                text: "Next"
                on_release: app.root.current = 'BorrowerScreen2'
                md_bg_color: 0.031, 0.463, 0.91, 1
                pos_hint: {'right': 1, 'y': 0.5}
                size_hint: 1, None
                height: "50dp"
        Label:
            text: ''

<BorrowerScreen2>:

    MDRectangleFlatButton:
        text: 'HOME'
        text_color: 0, 0, 0, 1
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        md_bg_color: 0.031, 0.463, 0.91, 1
        pos_hint: {'right': 1, 'top': 1}
        on_release: app.root.current()
        size_hint: (0.1, 0.03)
        font_size: "13sp"

    BoxLayout:
        orientation: 'vertical'
        padding: "40dp"

        MDLabel:
            text: 'Borrower Registration Form'
            font_size: 25
            halign: 'center'
            bold: True

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

        MDRectangleFlatButton:
            text: 'Upload Gov ID1'
            text_color: 0, 0, 0, 1 
            pos_hint: {'center_x': 0.5, 'center_y': 0.37}
            on_release: app.file_manager_open()
            size_hint: 1, None
            canvas.before:
                Color:
                    rgba: 0, 0, 0, 0
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

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

        MDRectangleFlatButton:
            text: 'Upload Gov ID2'
            text_color: 0, 0, 0, 1 
            pos_hint: {'center_x': 0.5, 'center_y': 0.37}
            on_release: app.file_manager_open()
            size_hint: 1, None
            canvas.before:
                Color:
                    rgba: 0, 0, 0, 0
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)


        GridLayout:
            cols: 2
            spacing: 30
            padding: 20
            pos_hint: {'center_x': 0.50, 'center_y': 0.5}
            size_hint: 1, None
            height: "50dp"

            MDRaisedButton:
                text: "Back"
                on_release: app.root.current = 'BorrowerScreen1'
                md_bg_color: 0.031, 0.463, 0.91, 1
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                size_hint: 1, None
                height: "50dp"

            MDRaisedButton:
                text: "Next"
                on_release: app.root.current = 'BorrowerScreen3'
                md_bg_color: 0.031, 0.463, 0.91, 1
                pos_hint: {'right': 1, 'y': 0.5}
                size_hint: 1, None
                height: "50dp"
        Label:
            text: ""  


<BorrowerScreen3>:
    MDRectangleFlatButton:
        text: 'HOME'
        text_color: 0, 0, 0, 1  
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        md_bg_color: 0.031, 0.463, 0.91, 1
        pos_hint: {'right': 1, 'top': 1}
        on_release: app.root.current()
        size_hint: (0.1, 0.03)
        font_size: "13sp"
        padding: dp(10)

    BoxLayout:
        orientation: 'vertical'
        padding: "40dp"

        MDLabel:
            text: 'Borrower Registration Form Address'
            font_size: 25
            halign: 'center'
            bold: True


        MDTextField:
            id: street_address
            hint_text: 'Enter Street Address '
            multiline: False
            helper_text: 'Enter Valid Address'
            helper_text_mode: 'on_focus'
            halign: 'left'
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1
            font_name: "Roboto-Bold"
            bold: True

        MDTextField:
            id: city
            hint_text: 'Enter City'
            multiline: False
            helper_text: 'Enter valid City'
            helper_text_mode: 'on_focus'
            halign: 'left'
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1
            font_name: "Roboto-Bold"
            bold: True

        MDTextField:
            id: Zip_code
            hint_text: 'Enter postal/zipcode'
            multiline: False
            helper_text: 'Enter valid postal/zipcode'
            helper_text_mode: 'on_focus'
            halign: 'left'
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1
            font_name: "Roboto-Bold"
            bold: True

        MDTextField:
            id: state
            hint_text: 'Enter State'
            multiline: False
            helper_text: 'Enter State Name'
            helper_text_mode: 'on_focus'
            halign: 'left'
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1
            font_name: "Roboto-Bold"
            bold: True

        MDTextField:
            id: country
            hint_text: 'Enter Country'
            multiline: False
            helper_text: 'Enter valid Country Name'
            helper_text_mode: 'on_focus'
            halign: 'left'
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1
            font_name: "Roboto-Bold"
            bold: True

        GridLayout:
            cols: 2
            spacing: 30
            padding: 20
            pos_hint: {'center_x': 0.50, 'center_y': 0.5}
            size_hint: 1, None
            height: "50dp"

            MDRaisedButton:
                text: "Back"
                on_release: app.root.current = 'BorrowerScreen2'
                md_bg_color: 0.031, 0.463, 0.91, 1
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                size_hint: 1, None
                height: "50dp"

            MDRaisedButton:
                text: "Next"
                on_release: app.root.current = 'BorrowerScreen4'
                md_bg_color: 0.031, 0.463, 0.91, 1
                pos_hint: {'right': 1, 'y': 0.5}
                size_hint: 1, None
                height: "50dp"
        Label:
            text: ""


<BorrowerScreen4>:
    MDRectangleFlatButton:
        text: 'HOME'
        text_color: 0, 0, 0, 1  # Black text color
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        md_bg_color: 0.031, 0.463, 0.91, 1
        pos_hint: {'right': 1, 'top': 1}
        on_release: app.root.current()
        size_hint: (0.1, 0.03)
        font_size: "13sp"
        padding: dp(10)

    BoxLayout:
        orientation: 'vertical'
        padding: "40dp"

        MDLabel:
            text: 'Borrower Registration Form Father Information'
            font_size: 25
            halign: 'center'
            bold: True


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

        GridLayout:
            cols: 2
            spacing: 30
            padding: 20
            pos_hint: {'center_x': 0.50, 'center_y': 0.5}
            size_hint: 1, None
            height: "50dp"

            MDRaisedButton:
                text: "Back"
                on_release: app.root.current = 'BorrowerScreen3'
                md_bg_color: 0.031, 0.463, 0.91, 1
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                size_hint: 1, None
                height: "50dp"

            MDRaisedButton:
                text: "Next"
                on_release: app.root.current = 'BorrowerScreen5'
                md_bg_color: 0.031, 0.463, 0.91, 1
                pos_hint: {'right': 1, 'y': 0.5}
                size_hint: 1, None
                height: "50dp"
        Label:
            text: ""

<BorrowerScreen5>:
    MDRectangleFlatButton:
        text: 'HOME'
        text_color: 0, 0, 0, 1  # Black text color
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        md_bg_color: 0.031, 0.463, 0.91, 1
        pos_hint: {'right': 1, 'top': 1}
        on_release: app.root.current()
        size_hint: (0.1, 0.03)
        font_size: "13sp"
        padding: dp(10)

    BoxLayout:
        orientation: 'vertical'
        padding: "40dp"

        MDLabel:
            text: 'Borrower Registration Form Mother Information'
            font_size: 25
            halign: 'center'
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


        GridLayout:
            cols: 2
            spacing: 30
            padding: 20
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
                on_release: app.root.current = 'BorrowerScreen6'
                md_bg_color: 0.031, 0.463, 0.91, 1
                pos_hint: {'right': 1, 'y': 0.5}
                size_hint: 1, None
                height: "50dp"
        Label:
            text: ""


<BorrowerScreen6>:
    MDRectangleFlatButton:
        text: 'HOME'
        text_color: 0, 0, 0, 1  # Black text color
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        md_bg_color: 0.031, 0.463, 0.91, 1
        pos_hint: {'right': 1, 'top': 1}
        on_release: app.root.current()
        size_hint: (0.1, 0.03)
        font_size: "13sp"
        padding: dp(10)

    BoxLayout:
        orientation: 'vertical'
        padding: "40dp"

        MDLabel:
            text: 'Borrower Registration Form Mother Information'
            font_size: 25
            halign: 'center'
            bold: True


        Spinner:
            id: spinner_id
            text: "Select Proficient type"
            values: ["Student", "Employee", "Business"]
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
            cols: 2
            spacing: 30
            padding: 20
            pos_hint: {'center_x': 0.50, 'center_y': 0.5}
            size_hint: 1, None
            height: "50dp"

            MDRaisedButton:
                text: "Back"
                on_release: app.root.current = 'BorrowerScreen5'
                md_bg_color: 0.031, 0.463, 0.91, 1
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                size_hint: 1, None
                height: "50dp"

            MDRaisedButton:
                text: "Next"
                on_press: root.next_pressed(spinner_id.text)
                md_bg_color: 0.031, 0.463, 0.91, 1
                pos_hint: {'right': 1, 'y': 0.5}
                size_hint: 1, None
                height: "50dp"
        Label:
            text: ""

<BorrowerScreen7>:
    MDRectangleFlatButton:
        text: 'HOME'
        text_color: 0, 0, 0, 1  # Black text color
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        md_bg_color: 0.031, 0.463, 0.91, 1
        pos_hint: {'right': 1, 'top': 1}
        on_release: app.root.current()
        size_hint: (0.1, 0.03)
        font_size: "13sp"
        padding: dp(10)

    BoxLayout:
        orientation: 'vertical'
        padding: "40dp"

        MDLabel:
            text: 'Student Type'
            font_size: 25
            halign: 'center'
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
            halign: 'center'
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1
            multiline: True
            helper_text: "Enter valid Collage ID"
            helper_text_mode: 'on_focus'
            font_name: "Roboto-Bold"
            bold: True

        MDRectangleFlatButton:
            text: 'Upload Collage Proof '
            text_color: 0, 0, 0, 1 
            pos_hint: {'center_x': 0.5, 'center_y': 0.37}
            on_release: app.file_manager_open()
            size_hint: 1, None
            canvas.before:
                Color:
                    rgba: 0, 0, 0, 0  
                Line:
                    width: 0.4  
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

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
            cols: 2
            spacing: 30
            padding: 20
            pos_hint: {'center_x': 0.50, 'center_y': 0.5}
            size_hint: 1, None
            height: "50dp"

            MDRaisedButton:
                text: "Back"
                on_release: app.root.current = 'BorrowerScreen6'
                md_bg_color: 0.031, 0.463, 0.91, 1
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                size_hint: 1, None
                height: "50dp"

            MDRaisedButton:
                text: "Next"
                on_release: app.root.current='BorrowerScreen15'
                md_bg_color: 0.031, 0.463, 0.91, 1
                pos_hint: {'right': 1, 'y': 0.5}
                size_hint: 1, None
                height: "50dp"
        Label:
            text: ""

<BorrowerScreen8>:
    MDRectangleFlatButton:
        text: 'HOME'
        text_color: 0, 0, 0, 1 
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        md_bg_color: 0.031, 0.463, 0.91, 1
        pos_hint: {'right': 1, 'top': 1}
        on_release: app.root.current()
        size_hint: (0.1, 0.03)
        font_size: "13sp"
        padding: dp(10)

    BoxLayout:
        orientation: 'vertical'
        padding: "40dp"

        MDLabel:
            text: 'Business Type'
            font_size: 25
            halign: 'center'
            bold: True

        MDLabel:
            text: 'STEP-1'
            font_size: 25
            halign: 'center'
            bold: True

        MDTextField:
            id: business_name
            hint_text: 'Enter Business Name '
            halign: 'center'
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
            halign: 'center'
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
            halign: 'center'
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1
            multiline: False
            helper_text: "Enter valid Business Address"
            helper_text_mode: 'on_focus'
            font_name: "Roboto-Bold"
            bold: True
            markup: True

        MDTextField:
            id: branch_name
            hint_text: 'Enter Branch Name'
            halign: 'center'
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1
            multiline: False
            helper_text:" Enter valid Branch Name"
            helper_text_mode: 'on_focus'
            font_name: "Roboto-Bold"
            bold: True
            markup: True
        GridLayout:
            cols: 2
            spacing: 30
            padding: 20
            pos_hint: {'center_x': 0.50, 'center_y': 0.5}
            size_hint: 1, None
            height: "50dp"

            MDRaisedButton:
                text: "Back"
                on_release: app.root.current = 'BorrowerScreen6'
                md_bg_color: 0.031, 0.463, 0.91, 1
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                size_hint: 1, None
                height: "50dp"

            MDRaisedButton:
                text: "Next"
                on_release: app.root.current = 'BorrowerScreen9'
                md_bg_color: 0.031, 0.463, 0.91, 1
                pos_hint: {'right': 1, 'y': 0.5}
                size_hint: 1, None
                height: "50dp"
        Label:
            text: ""

<BorrowerScreen9>:
    MDRectangleFlatButton:
        text: 'HOME'
        text_color: 0, 0, 0, 1  
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        md_bg_color: 0.031, 0.463, 0.91, 1
        pos_hint: {'right': 1, 'top': 1}
        on_release: app.root.current()
        size_hint: (0.1, 0.03)
        font_size: "13sp"
        padding: dp(10)

    BoxLayout:
        orientation: 'vertical'
        padding: "40dp"

        MDLabel:
            text: 'STEP-2'
            font_size: 25
            halign: 'center'
            bold: True

        MDTextField:
            id: nearest_location
            hint_text: 'Enter Nearest Location '
            halign: 'left'
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1
            multiline: False
            helper_text: "Enter Valid Nearest location"
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
            id: employee_id
            text: "No of Employees Working"
            values: ["<50", "50-100", "100-150", "150-200", ">200"]
            multiline: False
            size_hint: 1 , None
            height: 50
            background_color: 1, 1 ,1, 0 
            color: 0, 0, 0, 1
            canvas.before:
                Color:
                    rgba: 0, 0, 0, 1  
                Line:
                    width: 0.7  
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

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
            cols: 2
            spacing: 30
            padding: 20
            pos_hint: {'center_x': 0.50, 'center_y': 0.5}
            size_hint: 1, None
            height: "50dp"

            MDRaisedButton:
                text: "Back"
                on_release: app.root.current = 'BorrowerScreen8'
                md_bg_color: 0.031, 0.463, 0.91, 1
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                size_hint: 1, None
                height: "50dp"

            MDRaisedButton:
                text: "Next"
                on_release: app.root.current = 'BorrowerScreen10'
                md_bg_color: 0.031, 0.463, 0.91, 1
                pos_hint: {'right': 1, 'y': 0.5}
                size_hint: 1, None
                height: "50dp"
        Label:
            text: ""


<BorrowerScreen10>:
    MDRectangleFlatButton:
        text: 'HOME'
        text_color: 0, 0, 0, 1  
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        md_bg_color: 0.031, 0.463, 0.91, 1
        pos_hint: {'right': 1, 'top': 1}
        on_release: app.root.current()
        size_hint: (0.1, 0.03)
        font_size: "13sp"
        padding: dp(10)

    BoxLayout:
        orientation: 'vertical'
        padding: "40dp"

        MDLabel:
            text: 'Step-3'
            font_size: 25
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
            halign: 'center'
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1
            multiline: False
            helper_text: "Enter valid 6 months Turnover"
            helper_text_mode: 'on_focus'
            font_name: "Roboto-Bold"
            bold: True

        MDLabel:
            text: "Last 6 months Bank Statements"
            font_size: 22
            halign: 'center'

        MDRectangleFlatButton:
            text: 'Upload Statement Proof'
            text_color: 0, 0, 0, 1 
            pos_hint: {'center_x': 0.5, 'center_y': 0.37}
            on_release: app.file_manager_open()
            size_hint: 1, None
            canvas.before:
                Color:
                    rgba: 0, 0, 0, 0 
                Line:
                    width: 0.7
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)


        GridLayout:
            cols: 2
            spacing: 30
            padding: 20
            pos_hint: {'center_x': 0.50, 'center_y': 0.5}
            size_hint: 1, None
            height: "50dp"

            MDRaisedButton:
                text: "Back"
                on_release: app.root.current = 'BorrowerScreen9'
                md_bg_color: 0.031, 0.463, 0.91, 1
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                size_hint: 1, None
                height: "50dp"

            MDRaisedButton:
                text: "Next"
                on_release: app.root.current = 'BorrowerScreen11'
                md_bg_color: 0.031, 0.463, 0.91, 1
                pos_hint: {'right': 1, 'y': 0.5}
                size_hint: 1, None
                height: "50dp"
        Label:
            text: ""


<BorrowerScreen11>:
    MDRectangleFlatButton:
        text: 'HOME'
        text_color: 0, 0, 0, 1 
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        md_bg_color: 0.031, 0.463, 0.91, 1
        pos_hint: {'right': 1, 'top': 1}
        on_release: app.root.current()
        size_hint: (0.1, 0.03)
        font_size: "13sp"
        padding: dp(10)

    BoxLayout:
        orientation: 'vertical'
        padding: "40dp"

        MDLabel:
            text: 'Step-4'
            font_size: 25
            halign: 'center'
            bold: True

        MDTextField:
            id: director_name
            hint_text: 'Enter Director Name '
            halign: 'left'
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1
            multiline: False
            helper_text: "Enter valid Director Name"
            helper_text_mode: 'on_focus'
            font_name: "Roboto-Bold"
            bold: True

        MDTextField:
            id: director_mobile_number
            hint_text: 'Enter Director Mobile Number'
            halign: 'left'
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1
            multiline: False
            helper_text: "Enter valid Director Mobile Number"
            helper_text_mode: 'on_focus'
            font_name: "Roboto-Bold"
            bold: True

        MDTextField:
            id: din
            hint_text: 'Enter DIN'
            halign: 'left'
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1
            multiline: False
            helper_text: "Enter valid DIN"
            helper_text_mode: 'on_focus'
            font_name: "Roboto-Bold"
            bold: True

        MDTextField:
            id: cin
            hint_text: 'Enter CIN'
            halign: 'left'
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1
            multiline: False
            helper_text: "Enter valid CIN"
            helper_text_mode: 'on_focus'
            font_name: "Roboto-Bold"
            bold: True

        GridLayout:
            cols: 2
            spacing: 30
            padding: 20
            pos_hint: {'center_x': 0.50, 'center_y': 0.5}
            size_hint: 1, None
            height: "50dp"

            MDRaisedButton:
                text: "Back"
                on_release: app.root.current = 'BorrowerScreen10'
                md_bg_color: 0.031, 0.463, 0.91, 1
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                size_hint: 1, None
                height: "50dp"

            MDRaisedButton:
                text: "Next"
                on_release: app.root.current = 'BorrowerScreen12'
                md_bg_color: 0.031, 0.463, 0.91, 1
                pos_hint: {'right': 1, 'y': 0.5}
                size_hint: 1, None
                height: "50dp"
        Label:
            text: ""


<BorrowerScreen12>:
    MDRectangleFlatButton:
        text: 'HOME'
        text_color: 0, 0, 0, 1  
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        md_bg_color: 0.031, 0.463, 0.91, 1
        pos_hint: {'right': 1, 'top': 1}
        on_release: app.root.current()
        size_hint: (0.1, 0.03)
        font_size: "13sp"
        padding: dp(10)

    BoxLayout:
        orientation: 'vertical'
        padding: "40dp"

        MDLabel:
            text: 'Step-5'
            font_size: 25
            halign: 'center'
            bold: True

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
            id: office_address_proof
            hint_text: 'Enter Office Address Proof'
            halign: 'left'
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1
            multiline: False
            helper_text: "Enter Valid Office Address Proof"
            helper_text_mode: 'on_focus'
            font_name: "Roboto-Bold"
            bold: True

        MDLabel:
            text: "Proof of verification"
            font_size: 22
            halign: 'center'

        MDRectangleFlatButton:
            text: 'Upload Address Proof'
            text_color: 0, 0, 0, 1 
            pos_hint: {'center_x': 0.5, 'center_y': 0.37}
            on_release: app.file_manager_open()
            size_hint: 1, None
            canvas.before:
                Color:
                    rgba: 0, 0, 0, 0
                Line:
                    width: 0.7  
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

        MDTextField:
            id: branch_name
            hint_text: 'Enter Branch Name'
            halign: 'left'
            helper_text: "Enter Branch Name"
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1
            multiline: False
            helper_text_mode: 'on_focus'
            font_name: "Roboto-Bold"
            bold: True

        GridLayout:
            cols: 2
            spacing: 30
            padding: 20
            pos_hint: {'center_x': 0.50, 'center_y': 0.5}
            size_hint: 1, None
            height: "50dp"

            MDRaisedButton:
                text: "Back"
                on_release: app.root.current = 'BorrowerScreen11'
                md_bg_color: 0.031, 0.463, 0.91, 1
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                size_hint: 1, None
                height: "50dp"

            MDRaisedButton:
                text: "Next"
                on_release: app.root.current = 'BorrowerScreen15'
                md_bg_color: 0.031, 0.463, 0.91, 1
                pos_hint: {'right': 1, 'y': 0.5}
                size_hint: 1, None
                height: "50dp"
        Label:
            text: ""

<BorrowerScreen13>:
    MDRectangleFlatButton:
        text: 'HOME'
        text_color: 0, 0, 0, 1  
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        md_bg_color: 0.031, 0.463, 0.91, 1
        pos_hint: {'right': 1, 'top': 1}
        on_release: app.root.current()
        size_hint: (0.1, 0.03)
        font_size: "13sp"
        padding: dp(10)

    BoxLayout:
        orientation: 'vertical'
        padding: "40dp"

        MDLabel:
            text: 'Employment Details'
            font_size: 25
            halign: 'center'
            bold: True
        MDTextField:
            id: company_name
            hint_text: 'Enter Company Name'
            halign: 'left'
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1
            multiline: False
            helper_text: "Enter valid Company Name"
            helper_text_mode: 'on_focus'
            font_name: "Roboto-Bold"
            bold: True

        MDTextField:              
            id: pincode
            hint_text: 'Enter Pincode'
            halign: 'left'
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1
            multiline: False
            helper_text: "Enter valid Pincode"
            helper_text_mode: 'on_focus'
            font_name: "Roboto-Bold"
            bold: True

        MDTextField:              
            id: country
            hint_text: 'Enter Country'
            halign: 'left'
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1
            multiline: False
            helper_text: "Enter valid Country"
            helper_text_mode: 'on_focus'
            font_name: "Roboto-Bold"
            bold: True

        MDTextField:              
            id: landmark
            hint_text: 'Enter Landmark'
            halign: 'left'
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1
            multiline: False
            helper_text: "Enter valid Landmark"
            helper_text_mode: 'on_focus'
            font_name: "Roboto-Bold"
            bold: True

        MDTextField:              
            id: business_phone_number
            hint_text: 'Enter Business Phone Number'
            halign: 'left'
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1
            multiline: False
            helper_text: "Enter valid Business Phone Number"
            helper_text_mode: 'on_focus'
            font_name: "Roboto-Bold"
            bold: True

        GridLayout:
            cols: 2
            spacing: 30
            padding: 20
            pos_hint: {'center_x': 0.50, 'center_y': 0.5}
            size_hint: 1, None
            height: "50dp"

            MDRaisedButton:
                text: "Back"
                on_release: app.root.current = 'BorrowerScreen7'
                md_bg_color: 0.031, 0.463, 0.91, 1
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                size_hint: 1, None
                height: "50dp"

            MDRaisedButton:
                text: "Next"
                on_release: app.root.current = 'BorrowerScreen14'
                md_bg_color: 0.031, 0.463, 0.91, 1
                pos_hint: {'right': 1, 'y': 0.5}
                size_hint: 1, None
                height: "50dp"
        Label:
            text: ""


<BorrowerScreen14>:
    MDRectangleFlatButton:
        text: 'HOME'
        text_color: 0, 0, 0, 1  
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        md_bg_color: 0.031, 0.463, 0.91, 1
        pos_hint: {'right': 1, 'top': 1}
        on_release: app.root.current()
        size_hint: (0.1, 0.03)
        font_size: "13sp"
        padding: dp(10)

    BoxLayout:
        orientation: 'vertical'
        padding: "40dp"

        MDLabel:
            text: 'Employment Details'
            font_size: 25
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
            font_size: 18
            halign: 'center'

        MDRectangleFlatButton:
            text: 'Upload ID'
            text_color: 0, 0, 0, 1 
            pos_hint: {'center_x': 0.5, 'center_y': 0.37}
            on_release: app.file_manager_open()
            size_hint: 1, None
            canvas.before:
                Color:
                    rgba: 0, 0, 0, 0
                Line:
                    width: 0.7  
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

        MDLabel:
            text: "Upload Last 6 months Bank Statements"
            font_size: 18
            halign: 'center'

        MDRectangleFlatButton:
            text: 'Upload Statement'
            text_color: 0, 0, 0, 1 
            pos_hint: {'center_x': 0.5, 'center_y': 0.37}
            on_release: app.file_manager_open()
            size_hint: 1, None
            canvas.before:
                Color:
                    rgba: 0, 0, 0, 0
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

        GridLayout:
            cols: 2
            spacing: 30
            padding: 20
            pos_hint: {'center_x': 0.50, 'center_y': 0.5}
            size_hint: 1, None
            height: "50dp"

            MDRaisedButton:
                text: "Back"
                on_release: app.root.current = 'BorrowerScreen13'
                md_bg_color: 0.031, 0.463, 0.91, 1
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                size_hint: 1, None
                height: "50dp"

            MDRaisedButton:
                text: "Next"
                on_release: app.root.current = 'BorrowerScreen15'
                md_bg_color: 0.031, 0.463, 0.91, 1
                pos_hint: {'right': 1, 'y': 0.5}
                size_hint: 1, None
                height: "50dp"
        Label:
            text: ""

<BorrowerScreen15>:
    MDRectangleFlatButton:
        text: 'HOME'
        text_color: 0, 0, 0, 1  
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        md_bg_color: 0.031, 0.463, 0.91, 1
        pos_hint: {'right': 1, 'top': 1}
        on_release: app.root.current()
        size_hint: (0.1, 0.03)
        font_size: "13sp"
        padding: dp(10)

    BoxLayout:
        orientation: 'vertical'
        padding: "40dp"

        MDLabel:
            text: 'Borrower Registration Form'
            font_size: 25
            halign: 'center'
            bold: True

        Spinner:
            id: marital_status_id
            text: "Please Select Marital Status"
            values: ["Married", "Un-Married", "Divorced"]
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
            cols: 2
            spacing: 30
            padding: 20
            pos_hint: {'center_x': 0.50, 'center_y': 0.5}
            size_hint: 1, None
            height: "50dp"

            MDRaisedButton:
                text: "Back"
                on_release: app.root.current = 'BorrowerScreen14'
                md_bg_color: 0.031, 0.463, 0.91, 1
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                size_hint: 1, None
                height: "50dp"

            MDRaisedButton:
                text: "Next"
                on_release: root.next_button(marital_status_id.text)
                md_bg_color: 0.031, 0.463, 0.91, 1
                pos_hint: {'right': 1, 'y': 0.5}
                size_hint: 1, None
                height: "50dp"
        Label:
            text: ""

<BorrowerScreen16>:
    MDRectangleFlatButton:
        text: 'HOME'
        text_color: 0, 0, 0, 1  
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        md_bg_color: 0.031, 0.463, 0.91, 1
        pos_hint: {'right': 1, 'top': 1}
        on_release: app.root.current()
        size_hint: (0.1, 0.03)
        font_size: "13sp"
        padding: dp(10)

    BoxLayout:
        orientation: 'vertical'
        padding: "40dp"

        MDLabel:
            text: 'Step-1'
            font_size: 25
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
            cols: 2
            spacing: 30
            padding: 20
            pos_hint: {'center_x': 0.50, 'center_y': 0.5}
            size_hint: 1, None
            height: "50dp"

            MDRaisedButton:
                text: "Back"
                on_release: app.root.current = 'BorrowerScreen15'
                md_bg_color: 0.031, 0.463, 0.91, 1
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                size_hint: 1, None
                height: "50dp"

            MDRaisedButton:
                text: "Next"
                on_release: app.root.current = 'BorrowerScreen17'
                md_bg_color: 0.031, 0.463, 0.91, 1
                pos_hint: {'right': 1, 'y': 0.5}
                size_hint: 1, None
                height: "50dp"
        Label:
            text: ""

<BorrowerScreen17>:
    MDRectangleFlatButton:
        text: 'HOME'
        text_color: 0, 0, 0, 1  
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        md_bg_color: 0.031, 0.463, 0.91, 1
        pos_hint: {'right': 1, 'top': 1}
        on_release: app.root.current()
        size_hint: (0.1, 0.03)
        font_size: "13sp"
        padding: dp(10)

    BoxLayout:
        orientation: 'vertical'
        padding: "40dp"

        MDLabel:
            text: 'Step-2'
            font_size: 25
            halign: 'center'
            bold: True

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
            id:  spouse_annual_salary
            hint_text: 'Enter Annual Salary'
            halign: 'left'
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1
            multiline: False
            helper_text: 'Enter valid Annual Salary'
            helper_text_mode: 'on_focus'
            font_name: "Roboto-Bold"
            bold: True
        MDTextField:
            id:spouse_office_no
            hint_text: 'Enter Spouse Office Number'
            halign: 'left'
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1
            multiline: False
            helper_text: "Enter valid Spouse Office No"
            helper_text_mode: 'on_focus'
            font_name: "Roboto-Bold"
            bold: True

        GridLayout:
            cols: 2
            spacing: 30
            padding: 20
            pos_hint: {'center_x': 0.50, 'center_y': 0.5}
            size_hint: 1, None
            height: "50dp"

            MDRaisedButton:
                text: "Back"
                on_release: app.root.current = 'BorrowerScreen16'
                md_bg_color: 0.031, 0.463, 0.91, 1
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                size_hint: 1, None
                height: "50dp"

            MDRaisedButton:
                text: "Next"
                on_release: app.root.current = 'BorrowerScreen18'
                md_bg_color: 0.031, 0.463, 0.91, 1
                pos_hint: {'right': 1, 'y': 0.5}
                size_hint: 1, None
                height: "50dp"
        Label:
            text: ""


<BorrowerScreen18>:
    MDRectangleFlatButton:
        text: 'HOME'
        text_color: 0, 0, 0, 1  
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        md_bg_color: 0.031, 0.463, 0.91, 1
        pos_hint: {'right': 1, 'top': 1}
        on_release: app.root.current()
        size_hint: (0.1, 0.03)
        font_size: "13sp"
        padding: dp(10)

    BoxLayout:
        orientation: 'vertical'
        padding: "40dp"

        MDLabel:
            text: 'Applicant Bank Details'
            font_size: 25
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
            text: "Select Account Type Option"
            values: ["Savings Account", "Salary Account", "Current Account", "NRI Account", "Re-Curing Account"]
            size_hint: 1 , None
            height: 50
            background_color: 1, 1 ,1, 0 
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
            cols: 2
            spacing: 30
            padding: 20
            pos_hint: {'center_x': 0.50, 'center_y': 0.5}
            size_hint: 1, None
            height: "50dp"

            MDRaisedButton:
                text: "Back"
                on_release: app.root.current = 'BorrowerScreen15'
                md_bg_color: 0.031, 0.463, 0.91, 1
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                size_hint: 1, None
                height: "50dp"

            MDRaisedButton:
                text: "Next"
                on_release: app.root.current = 'BorrowerScreen19'
                md_bg_color: 0.031, 0.463, 0.91, 1
                pos_hint: {'right': 1, 'y': 0.5}
                size_hint: 1, None
                height: "50dp"
        Label:
            text: ""

<BorrowerScreen19>:
    MDRectangleFlatButton:
        text: 'HOME'
        text_color: 0, 0, 0, 1  
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        md_bg_color: 0.031, 0.463, 0.91, 1
        pos_hint: {'right': 1, 'top': 1}
        on_release: app.root.current()
        size_hint: (0.1, 0.03)
        font_size: "13sp"
        padding: dp(10)

    BoxLayout:
        orientation: 'vertical'
        padding: "40dp"

        MDLabel:
            text: 'Applicant Bank Details'
            font_size: 25
            halign: 'center'
            bold: True

        MDTextField:
            id: bank_id
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
            text: "select Salary Paid Option"
            values: ["Cash", "Online"]
            multiline: False
            size_hint: 1 , None
            height: 50
            background_color: (0, 0, 0, 0)
            background_normal: ''
            background_color: 1, 1 ,1, 0 
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
            spacing: 30
            padding: 20
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
                text: "Next"
                on_release: root.go_to_borrower_dashboard()
                md_bg_color: 0.031, 0.463, 0.91, 1
                pos_hint: {'right': 1, 'y': 0.5}
                size_hint: 1, None
                height: "50dp"
        Label:
            text: ""


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
        if id == 'Un-Married':
            self.manager.current = 'BorrowerScreen18'

        elif id == 'Married':
            self.manager.current = 'BorrowerScreen16'

        elif id == 'Divorced':
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
