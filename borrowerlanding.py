from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.button import MDIconButton

from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.modalview import ModalView

BorrLanding = '''
<BorrowerLanding>:
    ScrollView:
        MDFloatLayout:
            md_bg_color:1,1,1,1



            Image:
                source: "LOGO.png"
                pos_hint: {'center_x': 0.5, 'center_y': 0.91}
                size_hint_x: None
                size_hint_y: None
                height: dp(30)
                spacing: dp(40)
                size: "100dp", "100dp"
                allow_stretch: True
                keep_ratio: False

            Label:
                text: 'Welcome to P2P '
                font_size: 23
                pos_hint: {'center_x': 0.5, 'center_y': 0.81}
                color: 4/255, 104/255, 153/255, 1
                height: dp(10)
                underline: "True"
                size_hint_y: None
                font_name: "Roboto-Bold"

            Label:
                text: 'Get any type of loan for'
                font_size:dp(18)
                font_name: "Roboto-Bold"

                pos_hint: {'center_x': 0.5, 'center_y': 0.77}
                color: 0, 0, 0, 1

            Label:
                text: 'whatever you need'
                font_size:dp(18)
                font_name: "Roboto-Bold"

                pos_hint: {'center_x': 0.5, 'center_y': 0.74}
                color: 0, 0, 0, 1
                height: dp(50)

            MDGridLayout:
                cols: 2
                spacing:dp(10)

                size_hint_y: None
                pos_hint: {'center_x': 0.5, 'center_y': 0.53}
                height: self.minimum_height
                width: self.minimum_width
                size_hint_x: None
                MDRaisedButton:
                    size_hint: None, None
                    size: "150dp", "40dp"
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    md_bg_color: 1/255, 26/255, 51/255, 1
                    size_hint_y: None
                    height: dp(80)
                    size_hint_x: None
                    width: dp(130)
                    BoxLayout:
                        orientation: 'horizontal'
                        spacing:dp(10)
                        MDLabel:
                            text: "Disbursal in 2 Hours   "
                            font_size: "14sp"

                            theme_text_color: 'Custom'
                            halign: "center"
                            text_color: 1, 1, 1, 1
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                MDRaisedButton:
                    size_hint: None, None
                    size: "150dp", "40dp"
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    md_bg_color: 1/255, 26/255, 51/255, 1
                    size_hint_y: None
                    height: dp(80)
                    size_hint_x: None
                    width: dp(130)
                    BoxLayout:
                        orientation: 'horizontal'
                        spacing:dp(10)
                        MDLabel:
                            text: "Flexible Loan Tenure"
                            font_size: "14sp"

                            theme_text_color: 'Custom'
                            halign: "center"
                            text_color: 1, 1, 1, 1
                            pos_hint: {'center_x': 0.8, 'center_y': 0.5}
                MDRaisedButton:
                    size_hint: None, None
                    size: "150dp", "40dp"
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    md_bg_color: 1/255, 26/255, 51/255, 1
                    size_hint_y: None
                    height: dp(80)
                    size_hint_x: None
                    width: dp(130)
                    BoxLayout:
                        orientation: 'horizontal'
                        spacing:dp(10)
                        MDLabel:
                            text: "100% Digital Process"
                            font_size: "14sp"

                            theme_text_color: 'Custom'
                            halign: "center"
                            text_color: 1, 1, 1, 1
                            pos_hint: {'center_x': 0.8, 'center_y': 0.5}
                MDRaisedButton:
                    size_hint: None, None
                    size: "150dp", "40dp"
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    md_bg_color: 1/255, 26/255, 51/255, 1
                    size_hint_y: None
                    height: dp(80)
                    size_hint_x: None
                    width: dp(130)
                    BoxLayout:
                        orientation: 'horizontal'
                        spacing:dp(10)
                        MDLabel:
                            text: "Direct Transfer to Bank Account"
                            font_size: "14sp"

                            theme_text_color: 'Custom'
                            halign: "center"
                            text_color: 1, 1, 1, 1
                            pos_hint: {'center_x': 0.8, 'center_y': 0.5}
            MDTextButton:
                text: 'How do I get started?'
                font_size:dp(16)
                underline: "True"
                font_name: "Roboto"
                bold:"True"
                pos_hint: {'center_x': 0.5, 'center_y': 0.32}

                color: 0, 0, 0, 1
                on_release: root.switch_screen('BorrowerHowScreen')
            Widget:
                # Widget to draw a line below the image
                size_hint_y: None
                height: dp(10)
                pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                canvas.before:
                    Color:
                        rgba: 155/255, 160/255, 162/255, 1  # Change the color to blue (R, G, B, A)
            MDRaisedButton:
                text: "Continue as Borrower"
                font_name: "Roboto-Bold"
                font_size:dp(17)
                padding:dp(15)
                md_bg_color: 6/255, 143/255, 236/255, 1
                pos_hint: {'center_x': 0.5, 'center_y': 0.2}
                border_radius: [1, 1, 1, 1]
                on_release: root.switch_screen('borrower_registration_forms')

<BorrowerHowScreen>:
   


    MDFloatLayout:
        md_bg_color:174/255, 214/255, 241/255, 1

        MDIconButton:

            icon: 'chevron-left'
            on_release: app.root.current = 'BorrowerLanding'
            pos_hint: {'center_x': 0.03, 'center_y': 0.95}
            theme_text_color: 'Custom'
            text_color: 0,0,0,1  # Set color to white



        MDLabel:
            text: "Here's how it works"

            underline: "True"
            font_name: "Roboto-Bold"
            font_size:"16sp"
            theme_text_color: 'Custom'
            text_color:0,0,0,1
            halign:"center"
            pos_hint: {'center_x': 0.5, 'center_y': 0.81}


        MDGridLayout:
            cols: 2
            spacing:dp(10)

            size_hint_y: None
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            height: self.minimum_height
            width: self.minimum_width
            size_hint_x: None
            MDFlatButton
                size_hint: None, None
                size: "150dp", "40dp"
                pos_hint: {'center_x': 0.5, 'center_y': 0.55}
                md_bg_color:1,1,1,1
                line_color: 0, 0, 0, 1 
                size_hint_y: None
                height: dp(70)
                size_hint_x: None
                width: dp(120)
                BoxLayout:
                    orientation: 'horizontal'
                    spacing:dp(10)
                    MDLabel:
                        text: "1.Registration "
                        font_size:dp(15)
                        bold: "True"
                        theme_text_color: 'Custom'
                        halign: "center"
                        text_color:  1/255, 26/255, 51/255, 1
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            MDFlatButton
                size_hint: None, None
                size: "150dp", "40dp"
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                md_bg_color: 1,1,1,1
                line_color: 0, 0, 0, 1 
                size_hint_y: None
                height: dp(70)
                size_hint_x: None
                width: dp(120)
                BoxLayout:
                    orientation: 'horizontal'
                    spacing:dp(10)
                    MDLabel:
                        text: "2. Invest Profile Approval"
                        font_size:dp(15)
                        bold: "True"
                        theme_text_color: 'Custom'
                        halign: "center"
                        text_color: 1/255, 26/255, 51/255, 1
                        pos_hint: {'center_x': 0.8, 'center_y': 0.5}
            MDFlatButton
                size_hint: None, None
                size: "150dp", "40dp"
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                md_bg_color:1,1,1,1
                line_color: 0, 0, 0, 1 
                size_hint_y: None
                height: dp(70)
                size_hint_x: None
                width: dp(120)
                BoxLayout:
                    orientation: 'horizontal'
                    spacing:dp(10)
                    MDLabel:
                        text: "3. View Loan Listing"
                        font_size:dp(15)
                        bold: "True"
                        theme_text_color: 'Custom'
                        halign: "center"
                        text_color: 1/255, 26/255, 51/255, 1
                        pos_hint: {'center_x': 0.8, 'center_y': 0.5}
            MDFlatButton
                size_hint: None, None
                size: "150dp", "40dp"
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                md_bg_color: 1,1,1,1
                line_color: 0, 0, 0, 1 
                size_hint_y: None
                height: dp(70)
                size_hint_x: None
                width: dp(120)
                BoxLayout:
                    orientation: 'horizontal'
                    spacing:dp(10)
                    MDLabel:
                        text: "4.Fund Loans"
                        font_size:dp(15)
                        bold: "True"
                        theme_text_color: 'Custom'
                        halign: "center"
                        text_color: 1/255, 26/255, 51/255, 1
                        pos_hint: {'center_x': 0.8, 'center_y': 0.5}
            MDFlatButton
                size_hint: None, None
                size: "150dp", "40dp"
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                md_bg_color: 1,1,1,1
                line_color: 0, 0, 0, 1 
                size_hint_y: None
                height: dp(70)
                size_hint_x: None
                width: dp(120)
                BoxLayout:
                    orientation: 'horizontal'
                    spacing:dp(10)
                    MDLabel:
                        text: "5.Sign Agreement With Borrower"
                        font_size: 15
                        bold: "True"
                        theme_text_color: 'Custom'
                        halign: "center"
                        text_color: 1/255, 26/255, 51/255, 1
                        pos_hint: {'center_x': 0.8, 'center_y': 0.5}
            MDFlatButton
                size_hint: None, None
                size: "150dp", "40dp"
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                md_bg_color:1,1,1,1
                line_color: 0, 0, 0, 1 
                size_hint_y: None
                height: dp(70)
                size_hint_x: None
                width: dp(120)
                BoxLayout:
                    orientation: 'horizontal'
                    spacing:dp(10)
                    MDLabel:
                        text: "6.Disbursement"
                        font_size: 15
                        bold: "True"
                        theme_text_color: 'Custom'
                        halign: "center"
                        text_color:  1/255, 26/255, 51/255, 1
                        pos_hint: {'center_x': 0.8, 'center_y': 0.5}
            MDFlatButton
                size_hint: None, None
                size: "150dp", "40dp"
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                md_bg_color: 1,1,1,1
                line_color: 0, 0, 0, 1 
                size_hint_y: None
                height: dp(70)
                size_hint_x: None
                width: dp(120)
                BoxLayout:
                    orientation: 'horizontal'
                    spacing:dp(10)
                    MDLabel:
                        text: "7.EMI Profit Realization"
                        font_size:dp(15)
                        bold: "True"
                        theme_text_color: 'Custom'
                        halign: "center"
                        text_color: 1/255, 26/255, 51/255, 1
                        pos_hint: {'center_x': 0.8, 'center_y': 0.5}
            MDFlatButton
                size_hint: None, None
                size: "150dp", "40dp"
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                md_bg_color: 1,1,1,1
                line_color: 0, 0, 0, 1 
                size_hint_y: None
                height: dp(70)
                size_hint_x: None
                width: dp(120)
                BoxLayout:
                    orientation: 'horizontal'
                    spacing:dp(10)
                    MDLabel:
                        text: "8.Further Reinvestment"
                        font_size:dp(15)
                        bold: "True"
                        theme_text_color: 'Custom'
                        halign: "center"
                        text_color:  1/255, 26/255, 51/255, 1
                        pos_hint: {'center_x': 0.8, 'center_y': 0.5}





'''


class BorrowerLanding(Screen):
    def build(self):
        sm = MyScreenManager()
        sm.add_widget(BorrowerLanding(name="BorrowerLanding"))

        return sm

    def BorrowerHowScreen(self):
        self.root.current = "BorrowerHowScreen"

    def borrower_registration_form(self):
        self.root.current = "borrower_registration_forms"

    def switch_screen(self, screen_name):
        print(f"Switching to screen: {screen_name}")

        # Get the screen manager
        sm = self.manager

        sm.transition = SlideTransition(direction='left')
        sm.current = screen_name


class BorrowerHowScreen(Screen):
    pass


class MyScreenManager(ScreenManager):
    pass


class BorrowerScreen(Screen):
    pass







