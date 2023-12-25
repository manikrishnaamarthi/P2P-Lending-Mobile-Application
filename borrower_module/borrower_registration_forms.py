from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

KV = '''


<BorrowerScreen>:
    BoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(20)

        MDLabel:
            text: "Borrower"
            theme_text_color: "Primary"
            font_style: "H6"

        MDTextField:
            hint_text: "Enter your name"
            helper_text: "Name"
            helper_text_mode: "on_focus"

        MDLabel:
            text: "Age:"
            theme_text_color: "Primary"
            font_style: "H6"

        MDTextField:
            input_filter: "int"
            hint_text: "Enter your age"
            helper_text: "Age"
            helper_text_mode: "on_focus"
        MDRaisedButton:
            text: "Submit"
            size_hint: None, None
            size: "120dp", "40dp"
            pos_hint: {"center_x": .5}
            on_press: root.submit_pressed()
<BorrowerScreen2>:
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
                on_release: app.len_reg_form1_validation()


'''


class BorrowerScreen(Screen):
    Builder.load_string(KV)

    def submit_pressed(self):
        # Logic for handling the submit button in test2 screen
        print("Submit button pressed in LenderScreen")