from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.slider import MDSlider
from kivymd.uix.label import MDLabel

user_helpers2 = """
<NewloanScreen>:
    MDRectangleFlatButton:
        text: 'HOME'
        text_color: 0, 0, 0, 1 
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        md_bg_color: 0.031, 0.463, 0.91, 1
        pos_hint: {'right': 1, 'top': 1}
        on_release: app.root.current ='borrower_dashboard'
        size_hint: (0.1, 0.03)
        font_size: "13sp"

    BoxLayout:
        orientation: 'vertical'
        padding: "40dp"

        MDLabel:
            text: 'New Loan Request'
            halign: 'center'
            bold: True

        MDTextField:
            id: amount_value
            hint_text: "Amount"
            readonly: True
            helper_text_mode: "on_focus"
            font_name: "Roboto-Bold"

        Spinner:
            padding: [10,10]
            id: tenure
            text: "Select Tenure"
            values: ["3", "6", "9", "12", "16", "24"]
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
            id:interest
            hint_text: 'Interest + Other Fees'
            helper_text_mode: "on_focus"
            font_name: "Roboto-Bold"
            readonly: True

        MDTextField:
            id:processing_fee
            hint_text: 'Processing Fee'
            helper_text_mode: "on_focus"
            font_name: "Roboto-Bold"
            readonly: True

        BoxLayout:
            orientation: 'horizontal'
            size_hint_y: None
            height: "29dp"
            spacing: 5

        GridLayout:
            cols: 1
            spacing: 20
            padding: 20
            pos_hint: {'center_x': 0.50, 'center_y': 0.5}
            size_hint: 1, None
            height: "50dp"

            MDRaisedButton:
                text: 'Next'
                text_color: 0, 0, 0, 1  # Black text color
                md_bg_color: 0.031, 0.463, 0.91, 1
                size_hint: 1, None
                height: "50dp"
                on_release: app.root.current = 'new'

<NewScreen>:
    MDRectangleFlatButton:
        text: 'HOME'
        text_color: 0, 0, 0, 1 
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        md_bg_color: 0.031, 0.463, 0.91, 1
        pos_hint: {'right': 1, 'top': 1}
        on_release: root.current()
        size_hint: (0.1, 0.03)
        font_size: "13sp"

    BoxLayout:
        orientation: 'vertical'
        padding: "40dp"

        MDLabel:
            text: 'New Loan Request'
            halign: 'center'
            bold: True

        MDTextField:
            id:total_due
            hint_text: 'Total Due'
            helper_text_mode: "on_focus"
            font_name: "Roboto-Bold"
            readonly: True

        MDTextField:
            id:total_repayment_amount
            hint_text: 'Total Repayment Amount'
            helper_text_mode: "on_focus"
            font_name: "Roboto-Bold"
            readonly: True

        MDTextField:
            id: purpose of loan
            hint_text: "Purpose of loan"
            helper_text_mode: "on_focus"
            font_name: "Roboto-Bold"

        MDTextField:
            id: password
            hint_text: "Please enter your OTP"
            helper_text: "Enter your OTP"
            helper_text_mode: "on_focus"
            password: True
            font_name: "Roboto-Bold"

        BoxLayout:
            orientation: 'horizontal'
            size_hint_y: None
            height: "29dp"
            spacing: 5

        GridLayout:
            cols: 2
            spacing: 20
            padding: 20
            pos_hint: {'center_x': 0.50, 'center_y': 0.5}
            size_hint: 1, None
            height: "50dp"

            MDRaisedButton:
                text: "Submit"
                md_bg_color: 0.031, 0.463, 0.91, 1
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                size_hint: 1, None
                height: "50dp"

            MDRaisedButton:
                text: "Cancel"
                md_bg_color: 0.031, 0.463, 0.91, 1
                pos_hint: {'right': 1, 'y': 0.5}
                size_hint: 1, None
                height: "50dp"


        MDLabel:
            id: error_text
            text: ""
"""

class NewloanScreen(Screen):
    def current(self):
        self.manager.current = 'borrower_dashboard'


class NewScreen(Screen):
    pass
