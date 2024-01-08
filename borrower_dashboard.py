from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
user_helpers = """
<DashboardScreen>:
    BoxLayout:
        orientation: 'vertical'
        size_hint: 1, 1  # Make the size stretchable

        MDTopAppBar:
            title: "Borrower DashBoard"
            elevation:4
            left_action_items: [['menu', lambda x: app.navigation_draw()]]
            right_action_items: [['clock', lambda x: app.navigation_draw()]]

        MDGridLayout:
            cols: 2
            padding: dp(15)
            spacing: dp(5)
            height: 60
            pos_hint: {'center_x': .5, 'center_y': .5}

            Button:
                text: "New Loan Request"
                size_hint_y: None
                width: dp(150)
                height: dp(135)
                background_color: 1, 1 ,1, 0 
                color: 0, 0, 0, 1
                bold: True
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.4  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)
                on_release: root.open_balance()


            Button:
                text: "View Loan"
                size_hint_y: None
                width: dp(150)
                height: dp(135)
                background_color: 1, 1 ,1, 0 
                color: 0, 0, 0, 1
                bold: True
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.4  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)
                on_release: app.open_balance()
            Button:
                text: "Today's Due"
                size_hint_y: None
                width: dp(150)
                height: dp(135)
                background_color: 1, 1 ,1, 0 
                color: 0, 0, 0, 1
                bold: True
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.4  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)
                on_release: app.open_balance()

            Button:
                text: "App Tracker"
                size_hint_y: None
                width: dp(150)
                height: dp(135)
                background_color: 1, 1 ,1, 0 
                color: 0, 0, 0, 1
                bold: True
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.4  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)
                on_release: app.open_balance()

            Button:
                text: "Discount Coupons"
                size_hint_y: None
                width: dp(150)
                height: dp(135)
                background_color: 1, 1 ,1, 0 
                color: 0, 0, 0, 1
                bold: True
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.4  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)
                on_release: app.open_balance()

            Button:
                text: "Loan Foreclose"
                size_hint_y: None
                width: dp(150)
                height: dp(135)
                background_color: 1, 1 ,1, 0 
                color: 0, 0, 0, 1
                bold: True
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.4  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)
                on_release: app.open_balance()
            
            Button:
                text: "View/Edit Profile"
                size_hint_y: None
                width: dp(150)
                height: dp(135)
                background_color: 1, 1 ,1, 0 
                color: 0, 0, 0, 1
                bold: True
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.4  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)
                on_release: app.open_balance()

        MDTopAppBar:
            title:"FAQ" 
            custom_action_items:[['help']]          

"""


class DashboardScreen(Screen):
    def open_balance(self):
        self.manager.current='new_loan_request'


