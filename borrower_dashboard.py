from kivymd.app import MDApp
from kivy.lang import Builder

user_helpers = """
MDScreen:
    BoxLayout:
        orientation: 'vertical'

        MDTopAppBar:
            title: "Borrower DashBoard"
            elevation:4
            left_action_items:[['menu']]

        MDGridLayout:
            cols: 2
            spacing: dp(10)
            padding: dp(10)

            Button:
                text: "View Profile"
                size_hint_y: None
                height: dp(40)

            Button:
                text: "View Opening Balance"
                size_hint_y: None
                height: dp(40)

            Button:
                text: "View Available Balance"
                size_hint_y: None
                height: dp(40)

            Button:
                text: "Request Top-up Amount"
                size_hint_y: None
                height: dp(40)

            Button:
                text: "View Loan Request"
                size_hint_y: None
                height: dp(40)

            Button:
                text: "Button - 6"
                size_hint_y: None
                height: dp(40)

            Button:
                text: "Button - 7"
                size_hint_y: None
                height: dp(40)

            Button:
                text: "Button - 8"
                size_hint_y: None
                height: dp(40)

            Button:
                text: "Button - 9"
                size_hint_y: None
                height: dp(40)

            Button:
                text: "Button - 10"
                size_hint_y: None
                height: dp(40)
"""

class BorrowerDashboard(MDApp):
    def build(self):
        return Builder.load_string(user_helpers)

BorrowerDashboard().run()
