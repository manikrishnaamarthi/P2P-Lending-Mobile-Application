from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton, MDFlatButton, MDRoundFlatButton
from kivy.uix.screenmanager import Screen, SlideTransition, ScreenManager
from lender_dashboard import LenderDashboard

Builder.load_string(
    """
<WindowManager>:
    WalletScreen:


<WalletScreen>:
    MDTopAppBar:
        title: "GP2P-Wallet"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left',lambda x: root.go_back()]]
        right_action_items: [['wallet']]
        title_align: 'center'

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(30)
        padding: dp(30)
        MDLabel:
            text: ""
            size_hint_y: None
            height: dp(20)

        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(50)
            padding: dp(30)
            md_bg_color: 253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 0, 0, 0, 1  
                Line:
                    width: 0.5  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 10)

            MDLabel:
                text: 'Available Balance'
                halign: 'left'
                bold: True
            MDBoxLayout:
                orientation: 'horizontal'
                size_hint: None, None
                width: "190dp"
                height: "10dp"
                pos_hint: {'center_x': 0.3, 'center_y': 0.2}

                MDIcon:
                    icon: 'currency-inr'
                    halign: 'left'
                    bold: True
                MDLabel:
                    halign: 'left'
                    bold: True
                    canvas.before:
                        Color:
                            rgba: 0, 0, 0, 1
                        Line:
                            width: 1
                            points: [self.x, self.y - dp(5), self.x + self.width, self.y - dp(5)]

        MDFloatLayout:
            orientation: 'vertical'
            spacing: dp(50)
            padding: dp(30)
            md_bg_color: 253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 0, 0, 0, 1  # Border color (black in this example)
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)
            GridLayout:
                id: grid1
                cols: 2
                spacing: dp(20)
                padding: dp(20)
                pos_hint: {'center_x': 0.5, 'center_y': 0.95}
                size_hint: 1, None
                height: "10dp"
                MDRoundFlatButton:
                    text: "Deposit"
                    id: deposit_button_grid
                    md_bg_color: 6/255, 143/255, 236/255, 1
                    theme_text_color: 'Custom'
                    text_color: 0, 0, 0, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"
                    on_release: root.highlight_button('deposit')
                MDRoundFlatButton:
                    text: "Withdraw"
                    id: withdraw_button_grid
                    md_bg_color: 253/255, 254/255, 254/255, 1
                    theme_text_color: 'Custom'
                    text_color: 0, 0, 0, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"
                    on_release: root.highlight_button('withdraw')

            MDBoxLayout:
                id: box1
                orientation: 'horizontal'
                size_hint: None, None
                width: "250dp"
                height: "60dp"
                pos_hint: {'center_x': 0.5, 'center_y': 0.2}

                MDLabel:
                    text: 'Enter Amount'
                    halign: 'left'
                    bold: True 

                MDTextField:      
                    helper_text_mode: "on_focus"
                    icon_left: 'currency-inr'
                    font_name: "Roboto-Bold"  

        MDBoxLayout:
            orientation: 'horizontal'
            spacing: dp(10)
            padding: dp(10)
            md_bg_color: 253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 0, 0, 0, 1  
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)
            GridLayout:
                id: grid2
                cols: 2
                spacing: dp(5)
                padding: dp(20)
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint: 1, None
                height: "5dp"
                MDLabel:
                    text: 'View Transaction History'
                    halign: 'left'
                    bold: True
                MDIcon:
                    icon: 'chevron-right'
                    halign: 'right'
                    bold: True

        MDRoundFlatButton:
            text: "Submit"
            on_release: app.root.current ='MainScreen'
            md_bg_color: 6/255, 143/255, 236/255, 1
            theme_text_color: 'Custom'
            font_name: "Roboto-Bold" 
            text_color: 1, 1, 1, 1
            size_hint: 0.7, None
            height: "40dp"
            pos_hint: {'center_x': 0.5}

    """
)


class WalletScreen(Screen):
    def highlight_button(self, button_type):
        if button_type == 'deposit':
            self.ids.deposit_button_grid.md_bg_color = 6 / 255, 143 / 255, 236 / 255, 1
            self.ids.withdraw_button_grid.md_bg_color = 253 / 255, 254 / 255, 254 / 255, 1
        elif button_type == 'withdraw':
            self.ids.deposit_button_grid.md_bg_color = 253 / 255, 254 / 255, 254 / 255, 1
            self.ids.withdraw_button_grid.md_bg_color = 6 / 255, 143 / 255, 236 / 255, 1

    def go_back(self):
        sm = self.manager

        # Create a new instance of the LoginScreen
        login_screen = LenderDashboard(name='LenderDashboard')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(login_screen)

        # Switch to the LoginScreen
        sm.current = 'LenderDashboard'


class MyScreenManager(ScreenManager):
    pass
