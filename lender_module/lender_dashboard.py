from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,Screen


user_helpers = """
WindowManager:
    MainScreen:
    ViewprofileScreen:
    
<MainScreen>:
    BoxLayout:
        orientation: 'vertical'
        spacing: dp(5)

        MDTopAppBar:
            title: "Lender DashBoard"
            elevation: 4
            left_action_items: [['menu',lambda x: nav_drawer.set_state("open")]]

        MDGridLayout:
            cols: 2
            spacing: dp(2)
            padding: dp(2)
            

            Button:
                text: "View Profile"  
                on_press: root.manager.current = 'profile' 

            Button:
                text: "View Opening Balance"
                
            Button:
                text: "View Available Balance"
                
            Button:
                text: "Request Top-up Amount"
                
            Button:
                text: "View Loan Request"
                
            Button:
                text: "View Closed Loans"
                
            Button:
                text: "View Loan Extension Request"
                
            Button:
                text: "View Loan Foreclosure Request"
                
            Button:
                text: "Loan Disbursement"
                
            Button:
                text: "View Lost Opportunities"
        MDTopAppBar:
            title:"FAQ" 
            custom_action_items:[['help']]      
                
<ViewprofileScreen>:
    name:'profile'
    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(10)
        padding: dp(10)
        size_hint_y: None
        height: self.minimum_height
        pos_hint: {'center_x': 0.5,'center_y': 0.5}
        size_hint_x: None
        width: 300
        MDCard:
            orientation: "vertical"
            size_hint: None, None
            size: "280dp", "480dp"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            MDLabel:
                text:'Full name'
                
            MDLabel:
                text:"Email ID" 
                    
            MDLabel:
                text:"Phone number"
                    
            MDLabel:
                text:"PAN Number"     
            MDLabel:
                text:"Aadhaar Number"

            
            
        
        
                
                
"""
class MainScreen(Screen):
    pass
class ViewprofileScreen(Screen):
    pass

class WindowManager(ScreenManager):
    pass
class LenderDashboard(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Blue'
        return Builder.load_string(user_helpers)

    def nav_drawer (self):
        pass
        # Replace with the functionality you want to execute when the bottom app bar button is pressed
        #print("Bottom App Bar Button Pressed")

LenderDashboard().run()
