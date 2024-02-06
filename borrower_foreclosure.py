import anvil.server
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, SlideTransition ,ScreenManager
import sqlite3
import anvil.server
from kivy.uix.screenmanager import Screen, SlideTransition
from kivymd.app import MDApp

anvil.server.connect('server_BQ6Z7GHPS3ZH5TPKQJBHTYJI-ZVMP6VAENIF2GORT')

loan_foreclose = """
<WindowManager>:
    DashboardScreen:
    LoansDetails:
    ViewProfileScreenFB:
    ForecloseDetails:
<DashboardScreenFB>:

    BoxLayout:
        orientation: 'vertical'
        size_hint: 1, 1 
        pos_hint: {'center_x':0.5, 'center_y':0.5}

        MDTopAppBar:
            title: "Borrower DashBoard"
            elevation: 2
            left_action_items: [['menu', lambda x: app.on_menu_button_press()]]
            right_action_items: [['account', lambda x: root.on_profile_button_press()]]

        MDGridLayout:
            cols: 2
            padding: dp(15)
            spacing: dp(5)
            pos_hint: {'center_x': .5, 'center_y': .5}

            Button:
                text: "My Commitments"
                text_color: 0, 0, 0, 1
                background_color: 0.529, 0.807, 0.922, 0
                color: 0, 0, 0, 1
                bold: True
                canvas.before:
                    Color:
                        rgba:0.529, 0.807, 0.922, 1 
                    Line:
                        width: 0.9  
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)


            Button:
                text: "Opening Balance"
                background_color: 0.529, 0.807, 0.922, 0 
                color: 0, 0, 0, 1
                bold: True
                canvas.before:
                    Color:
                        rgba: 0.529, 0.807, 0.922, 1 
                    Line:
                        width: 0.9  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)
            Button:
                text: "My Returns"
                background_color: 0.529, 0.807, 0.922, 0
                color: 0, 0, 0, 1
                bold: True
                canvas.before:
                    Color:
                        rgba: 0.529, 0.807, 0.922, 1 
                    Line:
                        width: 
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)
            Button:
                text: "New Loan requests"
                background_color: 0.529, 0.807, 0.922, 0
                color: 0, 0, 0, 1
                bold: True
                canvas.before:
                    Color:
                        rgba: 0.529, 0.807, 0.922, 1 
                    Line:
                        width: 0.9  
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)
                on_release: app.open_balance()


            Button:
                text: "View Loan"
                text_color: 0, 0, 0, 1
                background_color: 0.529, 0.807, 0.922, 0
                color: 0, 0, 0, 1
                bold: True
                canvas.before:
                    Color:
                        rgba:0.529, 0.807, 0.922, 1 
                    Line:
                        width: 0.9  
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)
            Button:
                text: "Today's Due"
                text_color: 0, 0, 0, 1
                background_color: 0.529, 0.807, 0.922, 0
                color: 0, 0, 0, 1
                bold: True
                canvas.before:
                    Color:
                        rgba:0.529, 0.807, 0.922, 1 
                    Line:
                        width: 0.9  
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            Button:
                text: "App Tracker"
                text_color: 0, 0, 0, 1
                background_color: 0.529, 0.807, 0.922, 0
                color: 0, 0, 0, 1
                bold: True
                canvas.before:
                    Color:
                        rgba:0.529, 0.807, 0.922, 1 
                    Line:
                        width: 0.9  
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            Button:
                text: "Discount Coupons"
                text_color: 0, 0, 0, 1
                background_color: 0.529, 0.807, 0.922, 0
                color: 0, 0, 0, 1
                bold: True
                canvas.before:
                    Color:
                        rgba:0.529, 0.807, 0.922, 1 
                    Line:
                        width: 0.9  
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            Button:
                text: "Loan Foreclose"
                text_color: 0, 0, 0, 1
                background_color: 0.529, 0.807, 0.922, 0
                on_release: app.root.current = "LoansDetails"
                color: 0, 0, 0, 1
                bold: True
                canvas.before:
                    Color:
                        rgba:0.529, 0.807, 0.922, 1 
                    Line:
                        width: 0.9  
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            Button:
                text: "View Profile"
                text_color: 0, 0, 0, 1
                background_color: 0.529, 0.807, 0.922, 0
                color: 0, 0, 0, 1
                bold: True
                canvas.before:
                    Color:
                        rgba:0.529, 0.807, 0.922, 1 
                    Line:
                        width: 0.9  
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

        MDTopAppBar:
            title:"FAQ" 
            custom_action_items:[['help']]
"""
loan_foreclose += '''
<LoansDetailsFB>
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "Foreclose Loans"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.on_back_button_press()]]

        ScrollView:

            MDBoxLayout:
                orientation: 'vertical'
                size_hint_y: None
                height: self.minimum_height


                MDBoxLayout:
                    orientation: 'vertical'
                    size_hint_y: None
                    height: self.minimum_height
                    padding: dp(20)

                    BoxLayout:
                        id: box1
                        orientation: 'vertical'
                        size_hint_y: None
                        height: 0

                        padding: [10, 0,0,0]
                        canvas.before:
                            Color:
                                rgba: 0, 0, 1, 1 
                            Line:
                                rectangle: self.pos[0], self.pos[1], self.size[0], self.size[1]


                        GridLayout:
                            cols: 4
                            spacing: dp(20)
                            MDLabel:
                                text: 'Loan ID'
                                size_hint_y: None
                                height: dp(50)  
                                bold: True


                            MDLabel:
                                text: 'Loan Amount'
                                size_hint_y: None
                                height: dp(50) 
                                bold: True

                            MDLabel:
                                text: 'Tenure'
                                size_hint_y: None
                                height: dp(50) 
                                bold: True
                            MDLabel:
                                text: ''
                                size_hint_y: None
                                height: dp(50) 
                                size_hint_x: None
                                width: dp(20)
                                bold: True
                        Widget:
                            size_hint_y: None
                            height: dp(2) 
                            canvas:
                                Color:
                                    rgba: 0, 0, 1, 1
                                Line:
                                    width: dp(0.6)  
                                    points: self.x, self.y, self.x + self.width, self.y


'''

a = 8

for i in range(a):
    id_label = f"label_{i}"
    amount = f"amount_{i}"
    status = f"status_{i}"
    icon = f"icon_{i}"
    loan_foreclose += f'''
                        GridLayout:
                            cols: 4
                            spacing: dp(20)
                            MDLabel:
                                id: {id_label}
                                text: ''
                                size_hint_y: None
                                height: dp(50)

                            MDLabel:
                                id: {amount}
                                text: ''
                                size_hint_y: None
                                height: dp(50) 


                            MDLabel:
                                id: {status}
                                text: ''
                                size_hint_y: None
                                height: dp(50) 


                            MDIconButton:
                                id: {icon}
                                icon: 'arrow-right-thick'
                                size_hint_y: None
                                height: dp(50) 
                                on_release: root.icon_button_clicked({id_label}.text)
                                opacity: 0
'''
loan_foreclose += '''
<ViewProfileScreenFB>
    name:'Foreclosure'
    MDRectangleFlatButton:
        text: 'HOME'
        text_color: 0, 0, 0, 1 
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        md_bg_color: 0.031, 0.463, 0.91, 1
        pos_hint: {'right': 1, 'top': 1}
        on_release: app.root.current()
        size_hint: (0.1, 0.03)
        font_size: "13sp"
        on_press: root.manager.current = 'main'

    BoxLayout:
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        elevation: 2
        padding: 40
        spacing: 25
        orientation: 'vertical'
        radius: [10,]

        MDLabel:
            text: "Loan Foreclosure for Loan A/C: EX-ATL9820"
            bold: True
        Widget:
            size_hint_y: None
            height: 5

            canvas:
                Color:
                    rgba: 0, 0, 0, 1  
                Line:
                    points: self.x, self.y, self.x + self.width, self.y
        
        MDGridLayout:
            cols: 2
            spacing: 60

            MDLabel:
                text: "Loan ID"

            MDFloatLayout:
                size_hint: None, None
                size: dp(200), dp(40)
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x: 1
                canvas.before:
                    Color:
                        rgba: 1, 1, 1, 1 
                    RoundedRectangle:
                        pos: self.pos
                        size: self.size
                        radius: [10, 10, 10, 10]

                    Color:
                        rgba: 0, 0, 0, 1  

                    Line:
                        rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                        width: 1  # Border line width

                MDTextField:
                    id: loanid
                    size_hint: None, None
                    size_hint_x: 0.91
                    multiline: False
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    line_color_normal: [1, 1, 1, 1]  
                    line_color_focus: [1, 1, 1, 1]
                    font_name: "Roboto-Bold"
                    
                    
        MDGridLayout:
            cols: 2
            spacing: 60

            MDLabel:
                text: "Loan Amount"

            MDFloatLayout:
                size_hint: None, None
                size: dp(200), dp(40)
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x: 1
                canvas.before:
                    Color:
                        rgba: 1, 1, 1, 1 
                    RoundedRectangle:
                        pos: self.pos
                        size: self.size
                        radius: [10, 10, 10, 10]

                    Color:
                        rgba: 0, 0, 0, 1  

                    Line:
                        rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                        width: 1  # Border line width

                MDTextField:
                    id: amount
                    size_hint: None, None
                    size_hint_x: 0.91
                    multiline: False
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    line_color_normal: [1, 1, 1, 1]  
                    line_color_focus: [1, 1, 1, 1]
                    font_name: "Roboto-Bold"
        MDGridLayout:
            cols: 2
            spacing: 60

            MDLabel:
                text: "Name"

            MDFloatLayout:
                size_hint: None, None
                size: dp(200), dp(40)
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x: 1
                canvas.before:
                    Color:
                        rgba: 1, 1, 1, 1 
                    RoundedRectangle:
                        pos: self.pos
                        size: self.size
                        radius: [10, 10, 10, 10]

                    Color:
                        rgba: 0, 0, 0, 1  

                    Line:
                        rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                        width: 1  # Border line width

                MDTextField:
                    id: name
                    size_hint: None, None
                    size_hint_x: 0.91
                    multiline: False
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    line_color_normal: [1, 1, 1, 1]  
                    line_color_focus: [1, 1, 1, 1]
                    font_name: "Roboto-Bold"
        MDGridLayout:
            cols: 2
            spacing: 60

            MDLabel:
                text: "Tenure"

            MDFloatLayout:
                size_hint: None, None
                size: dp(200), dp(40)
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x: 1
                canvas.before:
                    Color:
                        rgba: 1, 1, 1, 1  
                    RoundedRectangle:
                        pos: self.pos
                        size: self.size
                        radius: [10, 10, 10, 10]

                    Color:
                        rgba: 0, 0, 0, 1  

                    Line:
                        rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                        width: 1  

                MDTextField:
                    id: tenure
                    size_hint: None, None
                    size_hint_x: 0.91
                    multiline: False
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    line_color_normal: [1, 1, 1, 1]  
                    line_color_focus: [1, 1, 1, 1]
                    font_name: "Roboto-Bold"
        MDGridLayout:
            cols: 2
            spacing: 60

            MDLabel:
                text: "Interest Rate"

            MDFloatLayout:
                size_hint: None, None
                size: dp(200), dp(40)
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x: 1
                canvas.before:
                    Color:
                        rgba: 1, 1, 1, 1  
                    RoundedRectangle:
                        pos: self.pos
                        size: self.size
                        radius: [10, 10, 10, 10]

                    Color:
                        rgba: 0, 0, 0, 1  

                    Line:
                        rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                        width: 1  # Border line width

                MDTextField:
                    id: interest
                    size_hint: None, None
                    size_hint_x: 0.91
                    multiline: False
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    line_color_normal: [1, 1, 1, 1]  
                    line_color_focus: [1, 1, 1, 1]
                    font_name: "Roboto-Bold"
        MDGridLayout:
            cols: 2
            spacing: 60

            MDLabel:
                text: "Credit limit"

            MDFloatLayout:
                size_hint: None, None
                size: dp(200), dp(40)
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x: 1
                canvas.before:
                    Color:
                        rgba: 1, 1, 1, 1 
                    RoundedRectangle:
                        pos: self.pos
                        size: self.size
                        radius: [10, 10, 10, 10]

                    Color:
                        rgba: 0, 0, 0, 1  

                    Line:
                        rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                        width: 1  

                MDTextField:
                    id: limit
                    size_hint: None, None
                    size_hint_x: 0.91
                    multiline: False
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    line_color_normal: [1, 1, 1, 1]  
                    line_color_focus: [1, 1, 1, 1]
                    font_name: "Roboto-Bold"
        MDGridLayout:
            cols: 2
            spacing: 60

            MDLabel:
                text: "Total Payment Made"

            MDFloatLayout:
                size_hint: None, None
                size: dp(200), dp(40)
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x: 1
                canvas.before:
                    Color:
                        rgba: 1, 1, 1, 1  
                    RoundedRectangle:
                        pos: self.pos
                        size: self.size
                        radius: [10, 10, 10, 10]

                    Color:
                        rgba: 0, 0, 0, 1  

                    Line:
                        rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                        width: 1  

                MDTextField:
                    id: total_payment
                    size_hint: None, None
                    size_hint_x: 0.91
                    multiline: False
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    line_color_normal: [1, 1, 1, 1]  
                    line_color_focus: [1, 1, 1, 1]
                    font_name: "Roboto-Bold"
        MDGridLayout:
            cols: 2
            spacing: 60

            MDLabel:
                text: "Foreclosure Type "

            MDFloatLayout:
                size_hint: None, None
                size: dp(200), dp(40)
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x: 1
                canvas.before:
                    Color:
                        rgba: 1, 1, 1, 1  
                    RoundedRectangle:
                        pos: self.pos
                        size: self.size
                        radius: [10, 10, 10, 10]

                    Color:
                        rgba: 0, 0, 0, 1  

                    Line:
                        rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                        width: 1  

                MDTextField:
                    id: closer_type
                    size_hint: None, None
                    size_hint_x: 0.91
                    multiline: False
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    line_color_normal: [1, 1, 1, 1]  
                    line_color_focus: [1, 1, 1, 1]
                    font_name: "Roboto-Bold"
        MDGridLayout:
            cols: 2
            spacing: 10

            CheckBox:
                size_hint: (None, None)
                width: 50
                bold: True
                color: (195/255,110/255,108/255,1)

            MDLabel:
                text: "I Agree Terms and Conditions"
                multiline: False


        MDGridLayout:
            cols: 2
            spacing: 30
            padding: 20
            size_hint: 1, 1
            pos_hint: {'center_x': 0.48, 'center_y': 0.5}

            MDRaisedButton:
                text: "BACK"
                md_bg_color: 0.031, 0.463, 0.91, 1
                theme_text_color: 'Custom'
                on_release: app.root.current = 'LoansDetails'
                text_color: 1, 1, 1, 1
                size_hint: 1, 1

            MDRaisedButton:
                text: "FORECLOSE"
                md_bg_color: 0.031, 0.463, 0.91, 1
                on_release: app.root.current = "ForecloseDetails"
                size_hint: 1, None
'''
loan_foreclose += '''

<ForecloseDetailsFB>
    BoxLayout:
        orientation: 'vertical'
        padding: dp(10)  
        spacing: dp(20) 
        ScrollView:
            do_scroll_x: False
            BoxLayout:
                orientation: "vertical"
                padding: dp(10) 
                spacing: dp(25)   
                size_hint_y: None
                height: self.minimum_height

                MDLabel:
                    text: "Loan Foreclosure For LoanA/C: EX-ATL9820"
                    bold: True

                MDLabel:
                    text: "Loan Foreclosure Payment Details :"

                Widget:
                    size_hint_y: None
                    height: dp(2)  
                    canvas:
                        Color:
                            rgba: 0, 0, 0, 1 
                        Line:
                            points: self.x, self.y, self.x + self.width, self.y
                MDLabel:
                    text: "Amount paid"
                    bold: True

                GridLayout:
                    cols: 2
                    size_hint_y: None
                    padding: dp(10)
                    spacing: dp(33)  

                    MDLabel:
                        text: "Total amount Paid "
                        bold: True

                    MDLabel:
                        id: totalamount
                        text: "loanid"

                    MDLabel:
                        text: "Monthly installment"

                    MDLabel:
                        id: monthlyinstallment
                        text: "monthly amount"

                    MDLabel:
                        text: "Interest Amount"

                    MDLabel:
                        id: interestamount
                        text: "interest amount"

                    MDLabel:
                        text: "Monthly EMI"

                    MDLabel:
                        id: monthlyemi
                        text: "Monthly emi"
                Widget:
                    size_hint_y: None
                    canvas:
                        Color:
                            rgba: 0, 0, 0, 1 
                        Line:
                            points: self.x, self.y, self.x + self.width, self.y

                MDLabel:
                    text: "Loan Closure Amount"
                    bold: True
                GridLayout:
                    cols: 2
                    size_hint_y: None
                    padding: dp(10)
                    spacing: dp(52)

                    MDLabel:
                        text: "Outstanding Amount"
                        bold: True

                    MDLabel:
                        id: overallamount
                        text: "Outstanding amount"
                    MDLabel:
                        text: "Overall Interest Amount "

                    MDLabel:
                        id: overallinterest
                        text: "overall interest amount"

                    MDLabel:
                        text: "Total Amount"

                    MDLabel:
                        id: totalamount
                        text: "total amount"

                Widget:
                    size_hint_y: None
                    canvas:
                        Color:
                            rgba: 0, 0, 0, 1 
                        Line:
                            points: self.x, self.y, self.x + self.width, self.y

                MDLabel:
                    text: "Loan Closure Amount"
                    bold: True

                GridLayout:
                    cols: 2
                    size_hint_y: None
                    padding: dp(10)
                    spacing: dp(45)

                    MDLabel:
                        text: "Outstanding Amount"
                        bold: True

                    MDLabel:
                        id: standingamount
                        text: "outstanding amount"

                    MDLabel:
                        text: "Foreclosure Fee "

                    MDLabel:
                        id: foreclosure
                        text: "Foreclosure Fee"

                    MDLabel:
                        text: "Foreclosure Amount"

                    MDLabel:
                        id: foreclosure
                        text: "Foreclosure Amount"

                Widget:
                    size_hint_y: None
                    canvas:
                        Color:
                            rgba: 0, 0, 0, 0 
                        Line:
                            points: self.x, self.y, self.x + self.width, self.y

                BoxLayout:
                    orientation: "vertical"
                    size_hint_y: None

                    MDLabel:
                        text: 'Reason for Foreclosure '
                        valign: 'top'
                        bold: True

                    MDTextField:
                        hint_text: 'Enter text here'

                BoxLayout:
                    orientation: "horizontal"
                    size_hint_y: None
                    spacing: dp(10)

                    CheckBox:
                        size_hint: None, None
                        width: dp(30) 
                        color: (195/255, 110/255, 108/255, 1)

                    MDLabel:
                        text: "I Agree Terms and Conditions"
                        multiline: False  

                MDLabel:
                    text: ""

                MDGridLayout:
                    cols: 2
                    spacing: dp(10)
                    padding: dp(5)
                    size_hint: 1, None

                    MDRaisedButton:
                        text: "CANCEL"
                        md_bg_color: 0.031, 0.463, 0.91, 1
                        theme_text_color: 'Custom'
                        on_release: app.root.current = 'ViewProfileScreenFB'
                        text_color: 1, 1, 1, 1
                        size_hint: 1, None

                    MDRaisedButton:
                        text: "SUBMIT"
                        md_bg_color: 0.031, 0.463, 0.91, 1
                        size_hint: 1, None
'''
Builder.load_string(loan_foreclose)


class DashboardScreenFB(Screen):
    pass


class LoansDetailsFB(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        data = self.get_table_data()
        customer_id = []
        loan_id = []
        loan_amount = []
        loan_status = []
        tenure = []
        s = 0
        for i in data:
            s += 1
            customer_id.append(i['borrower_full_name'])
            loan_id.append(i['loan_id'])
            loan_amount.append(i['loan_amount'])
            tenure.append(i['tenure'])
            loan_status.append(i['loan_updated_status'])

        c = -1
        index_list = []
        for i in range(s):
            c += 1
            if loan_status[i] == 'approved':
                index_list.append(c)

        b = 1
        k = -1
        for i in index_list:
            b += 1
            k += 1
            id_label = f"label_{k}"
            amount = f"amount_{k}"
            status = f"status_{k}"
            icon = f"icon_{k}"  # Fix the variable name here

            label_1 = self.ids[id_label]
            label_1.text = loan_id[i]
            label_2 = self.ids[amount]
            label_2.text = str(loan_amount[i])
            label_3 = self.ids[status]
            label_3.text = str(tenure[i])
            icon = self.ids[icon]  # Fix the variable name here
            icon.opacity = 1

        h = self.ids.box1.height

        for i in range(a + 1):
            h += 150
        self.ids.box1.height = h

    def get_table_data(self):
        # Make a call to the Anvil server function
        # Replace 'YourAnvilFunction' with the actual name of your Anvil server function
        return anvil.server.call('get_table_data')
    def icon_button_clicked(self, value):
        data = self.get_table_data()  # Fetch data here
        self.manager.current = 'ViewProfileScreenFB'
        view_profile_screen = self.manager.get_screen('ViewProfileScreenFB')
        view_profile_screen.initialize_with_value(value, data)
    def on_back_button_press(self):
        self.manager.current = 'DashboardScreen'

class ViewProfileScreenFB(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def initialize_with_value(self, value, data):
        loan_id = []
        loan_amount = []
        name = []
        tenure = []
        interest = []
        credit = []
        payment_made = []
        foreclose_type = []

        for i in data:
            loan_id.append(i['loan_id'])
            loan_amount.append(i['loan_amount'])
            name.append(i['borrower_full_name'])
            tenure.append(i['tenure'])
            interest.append(i['interest_rate'])
            credit.append(i['credit_limit'])
            payment_made.append(i['total_payments_made'])
            foreclose_type.append(i['foreclosure_type'])
        if value in loan_id:
            index = loan_id.index(value)
            self.ids.loanid.text = str(loan_id[index])
            self.ids.amount.text = str(loan_amount[index])
            self.ids.name.text = str(name[index])
            self.ids.tenure.text = str(tenure[index])
            self.ids.interest.text = str(interest[index])
            self.ids.limit.text = str(credit[index])
            self.ids.total_payment.text = str(payment_made[index])
            self.ids.closer_type.text = str(foreclose_type[index])


    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_keyboard)
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_keyboard)
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):

        if key == 27:
            self.go_back()
            return True
        return False

    def on_keyboard(self, window, key, *args):
        if key == 27:  # Key code for the 'Escape' key
            # Keyboard is closed, move the screen down
            self.screen_manager.y = 0
        return True

    def on_start(self):
        Window.softinput_mode = "below_target"

class ForecloseDetailsFB(Screen):
    pass
class MyScreenManager(ScreenManager):
    pass
    
