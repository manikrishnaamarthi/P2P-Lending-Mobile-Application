from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.button import MDIconButton

from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.modalview import ModalView

Landing = '''
<LenderLanding>:
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
                text: 'Use the power of P2P lending'
                font_size: 18
                font_name: r"C:\\P2P-Lending-Mobile-Application\\fonts\\static\\PlayfairDisplay-Medium.ttf"

                pos_hint: {'center_x': 0.5, 'center_y': 0.77}
                color: 0, 0, 0, 1

            Label:
                text: 'to get high returns'
                font_size: 18
                font_name: r"C:\\P2P-Lending-Mobile-Application\\fonts\\static\\PlayfairDisplay-Medium.ttf"

                pos_hint: {'center_x': 0.5, 'center_y': 0.74}
                color: 0, 0, 0, 1
                height: dp(50)

            MDGridLayout:
                cols: 2
                spacing: 10

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
                        spacing: 10
                        MDLabel:
                            text: "Diversification of Funds as low as $1   "
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
                        spacing: 10
                        MDLabel:
                            text: "Investment starting $10,000 onwards"
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
                        spacing: 10
                        MDLabel:
                            text: "Returns up to 15%"
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
                        spacing: 10
                        MDLabel:
                            text: "Invest for 1,2,3,4,5 or 6 years"
                            font_size: "14sp"

                            theme_text_color: 'Custom'
                            halign: "center"
                            text_color: 1, 1, 1, 1
                            pos_hint: {'center_x': 0.8, 'center_y': 0.5}
            MDTextButton:
                text: 'How do I get started?'
                font_size: 16
                underline: "True"
                font_name: "Roboto"
                bold:"True"
                pos_hint: {'center_x': 0.5, 'center_y': 0.32}

                color: 0, 0, 0, 1
                on_release: root.switch_screen('LenderHowScreen')
            Widget:
                # Widget to draw a line below the image
                size_hint_y: None
                height: dp(10)
                pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                canvas.before:
                    Color:
                        rgba: 155/255, 160/255, 162/255, 1  # Change the color to blue (R, G, B, A)
            MDRaisedButton:
                text: "Continue as Lender"
                font_name: "Roboto-Bold"
                font_size:17
                padding: 15
                md_bg_color: 6/255, 143/255, 236/255, 1
                pos_hint: {'center_x': 0.5, 'center_y': 0.2}
                border_radius: [1, 1, 1, 1]
                on_release: root.switch_screen('lender_registration_form')

<LenderHowScreen>:
   


    MDFloatLayout:
        md_bg_color:174/255, 214/255, 241/255, 1

        MDIconButton:
            
            icon: 'chevron-left'
            on_release: app.root.current = 'LenderLanding'
            pos_hint: {'center_x': 0.03, 'center_y': 0.95}
            theme_text_color: 'Custom'
            text_color: 0,0,0,1  # Set color to white
       
            

        MDLabel:
            text: "Here's how it works"

            underline: "True"
            font_name: r"C:\\P2P-Lending-Mobile-Application\\fonts\\static\\PlayfairDisplay-Medium.ttf"
            font_size:"16sp"
            theme_text_color: 'Custom'
            text_color:0,0,0,1
            halign:"center"
            pos_hint: {'center_x': 0.5, 'center_y': 0.81}


        MDGridLayout:
            cols: 2
            spacing: 10

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
                    spacing: 10
                    MDLabel:
                        text: "1.Registration "
                        font_size: 15
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
                    spacing: 10
                    MDLabel:
                        text: "2. Profile Evaluation"
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
                    spacing: 10
                    MDLabel:
                        text: "3. Listing On Platform"
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
                md_bg_color: 1,1,1,1
                line_color: 0, 0, 0, 1 
                size_hint_y: None
                height: dp(70)
                size_hint_x: None
                width: dp(120)
                BoxLayout:
                    orientation: 'horizontal'
                    spacing: 10
                    MDLabel:
                        text: "4.Funding"
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
                md_bg_color: 1,1,1,1
                line_color: 0, 0, 0, 1 
                size_hint_y: None
                height: dp(70)
                size_hint_x: None
                width: dp(120)
                BoxLayout:
                    orientation: 'horizontal'
                    spacing: 10
                    MDLabel:
                        text: "5.Sign Agreement With Lender"
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
                    spacing: 10
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
                    spacing: 10
                    MDLabel:
                        text: "7.EMI Repayment"
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
                md_bg_color: 1,1,1,1
                line_color: 0, 0, 0, 1 
                size_hint_y: None
                height: dp(70)
                size_hint_x: None
                width: dp(120)
                BoxLayout:
                    orientation: 'horizontal'
                    spacing: 10
                    MDLabel:
                        text: "8.Loan Closure"
                        font_size: 15
                        bold: "True"
                        theme_text_color: 'Custom'
                        halign: "center"
                        text_color:  1/255, 26/255, 51/255, 1
                        pos_hint: {'center_x': 0.8, 'center_y': 0.5}




'''




class LenderLanding(Screen):
    def build(self):
        sm = MyScreenManager()
        sm.add_widget(LenderLanding(name="LenderLanding"))

        return sm

    def LenderHowScreen(self):
        self.root.current = "LenderHowScreen"

    def lender_registration_form(self):
        self.root.current = "lender_registration_form"

    def switch_screen(self, screen_name):
        print(f"Switching to screen: {screen_name}")

        # Get the screen manager
        sm = self.manager

        sm.transition = SlideTransition(direction='left')
        sm.current = screen_name

class LenderHowScreen(Screen):
    pass
class MyScreenManager(ScreenManager):
    pass


class LenderScreen(Screen):
    pass







