from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window


Window.size = (300, 500)

user_helpers = """
Screen:
    MDNavigationLayout:
        MDScreenManager:
            MDScreen
                MDTopAppBar:
                    title:"Lender DashBoard"
                    elevation:4
                    pos_hint:{"top":1}
                    left_action_items:
                        [['menu']]
                MDFlatButton:
                    text:"Submit"  
                               







"""


class LenderDashboard(MDApp):
    def build(self):
        return Builder.load_string(user_helpers)


LenderDashboard().run()