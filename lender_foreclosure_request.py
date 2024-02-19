from kivymd.app import MDApp
from kivymd.uix.list import *
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, SlideTransition, ScreenManager
from kivy.utils import platform
from kivy.clock import mainthread
from kivymd.uix.filemanager import MDFileManager
if platform == 'android':
    from kivy.uix.button import Button
    from kivy.uix.modalview import ModalView
    from kivy.clock import Clock
    from android import api_version, mActivity
    from android.permissions import (
        request_permissions, check_permission, Permission)


import anvil.server

anvil.server.connect("server_XMDWJM7BS6DPVJBNFH3FTXDG-GKKVNXBTBX6VWVHY")

lender_foreclouser = """

<WindowManager>:
    DashboardScreenLF:
    ApprovedLoansLF:
    ViewAllLoansLF:
    RejectedLoansLF:
    UnderProcessLoansLF:
    ClosedLoansLF:
    ViewProfileScreenLF
    
    
<DashboardScreenLF>:
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "Foreclose Dashboard"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.on_back_button_press()]]


        BoxLayout:
            orientation: 'vertical'
            size_hint: 1, 1 
            padding: dp(40)
            pos_hint: {'center_x':0.5, 'center_y':0.5}

            MDGridLayout:
                cols: 2
                padding: dp(15)
                spacing: dp(5)
                pos_hint: {'center_x': .5, 'center_y': .5}

                Button:
                    text: "New Loan request"
                    background_color: 0.529, 0.807, 0.922, 0
                    on_release: app.root.current = "ViewAllLoansLF"
                    color: 0, 0, 0, 1
                    bold: True
                    canvas.before:
                        Color:
                            rgba: 0.529, 0.807, 0.922, 1 
                        Line:
                            width: 0.9  
                            rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

                Button:
                    text: "Approved "
                    text_color: 0, 0, 0, 1
                    background_color: 0.529, 0.807, 0.922, 0
                    color: 0, 0, 0, 1
                    on_release: app.root.current = "ApprovedLoansLF"
                    bold: True
                    canvas.before:
                        Color:
                            rgba:0.529, 0.807, 0.922, 1 
                        Line:
                            width: 0.9  
                            rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

                Button:
                    text: "Rejected Loans"
                    background_color: 0.529, 0.807, 0.922, 0 
                    on_release: app.root.current = "RejectedLoansLF"
                    color: 0, 0, 0, 1
                    bold: True
                    canvas.before:
                        Color:
                            rgba: 0.529, 0.807, 0.922, 1 
                        Line:
                            width: 0.9  # Border width
                            rounded_rectangle: (self.x, self.y, self.width, self.height, 15)


                Button:
                    text: "Under Process"
                    text_color: 0, 0, 0, 1
                    on_release: app.root.current = "UnderProcessLoansLF"
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
                    text: "Closed Loans"
                    background_color: 0.529, 0.807, 0.922, 0
                    color: 0, 0, 0, 1
                    on_release: app.root.current = "ClosedLoansLF"
                    bold: True
                    canvas.before:
                        Color:
                            rgba: 0.529, 0.807, 0.922, 1 
                        Line:
                            width: 0.9  
                            rounded_rectangle: (self.x, self.y, self.width, self.height, 15)



"""
lender_foreclouser += '''
<ApprovedLoansLF>
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "Approved Loans "
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
                                text: 'Loan Extension Status'
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

a = 50

for i in range(a):
    id_label = f"label_{i}"
    amount = f"amount_{i}"
    status = f"status_{i}"
    icon = f"icon_{i}"
    lender_foreclouser += f'''
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

lender_foreclouser += '''
<ViewAllLoansLF>
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "View All Loans "
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
                                text: 'Loan Extension status'
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

a = 50

for i in range(a):
    id_label = f"label_{i}"
    amount = f"amount_{i}"
    status = f"status_{i}"
    icon = f"icon_{i}"
    lender_foreclouser += f'''
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
lender_foreclouser += '''
<RejectedLoansLF>
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "Rejected Loans "
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
                                text: 'Loan Extension Status'
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

a = 50

for i in range(a):
    id_label = f"label_{i}"
    amount = f"amount_{i}"
    status = f"status_{i}"
    icon = f"icon_{i}"
    lender_foreclouser += f'''
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
lender_foreclouser += '''
<UnderProcessLoansLF>
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "UnderProcess Loans"
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
                                text: 'Loan Extension Status'
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

a = 50

for i in range(a):
    id_label = f"label_{i}"
    amount = f"amount_{i}"
    status = f"status_{i}"
    icon = f"icon_{i}"
    lender_foreclouser += f'''
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
lender_foreclouser += '''
<ClosedLoansLF>
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "Closed Loans"
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
                                text: 'Loan Extension Status'
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

a = 50

for i in range(a):
    id_label = f"label_{i}"
    amount = f"amount_{i}"
    status = f"status_{i}"
    icon = f"icon_{i}"
    lender_foreclouser += f'''
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
lender_foreclouser += '''
<ViewProfileScreenLF>:


    BoxLayout:
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        elevation: 2
        padding: 40
        spacing: 25
        orientation: 'vertical'
        radius: [10,]

        MDGridLayout:
            cols: 2
            spacing: 5
            MDLabel:
                text: "Loan Foreclosure for Loan A/C:"
                bold: True
            MDLabel:
                id : loan1
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
                text: "Borrower Name"

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
                    id: rate
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
                text: "Foreclosure Fee"

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
                    id: fee
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
                text: "Foreclosure Amount"

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
                    id: famount
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
                text: "Total Paid Amount"

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
                    id: total_paid
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
                text: "Outstanding Amount"

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
                    id: samount
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
                text: "Reason For Foreclosure"

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
                    id: reason
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
                text: "Total Due Amount"

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
                    id: due_amount
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
                text: "Decline"
                md_bg_color: 0.031, 0.463, 0.91, 1
                on_release: root.rejected_click()
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                size_hint: 1, 1

            MDRaisedButton:
                text: "Approve"
                theme_text_color: 'Custom'
                on_release: root.approved_click() 
                text_color: 1, 1, 1, 1
                md_bg_color: 0.031, 0.463, 0.91, 1
                size_hint: 1, 1



'''
Builder.load_string(lender_foreclouser)


class DashboardScreenLF(Screen):
    pass


class ApprovedLoansLF(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        data = self.get_table_data()
        loan_id = []
        loan_amount = []
        loan_status = []
        s = 0
        for i in data:
            s += 1
            loan_id.append(i['loan_id'])
            loan_amount.append(i['loan_amount'])
            loan_status.append(i['status'])

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
            label_3.text = loan_status[i]
            icon = self.ids[icon]  # Fix the variable name here
            icon.opacity = 1

        h = self.ids.box1.height

        for i in range(a + 1):
            h += 150
        self.ids.box1.height = h

    def get_table_data(self):
        # Make a call to the Anvil server function
        # Replace 'YourAnvilFunction' with the actual name of your Anvil server function
        return anvil.server.call('foreclosure_data')

    def icon_button_clicked(self, value):
        data = self.get_table_data()  # Fetch data here
        self.manager.current = 'ViewProfileScreenLF'
        self.manager.get_screen('ViewProfileScreenLF').initialize_with_value(value, data)

    def on_back_button_press(self):
        self.manager.current = 'DashboardScreenLF'


class ClosedLoansLF(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        data = self.get_table_data()
        loan_id = []
        loan_amount = []
        loan_status = []
        s = 0
        for i in data:
            s += 1
            loan_id.append(i['loan_id'])
            loan_amount.append(i['loan_amount'])
            loan_status.append(i['status'])

        c = -1
        index_list = []
        for i in range(s):
            c += 1
            if loan_status[i] == 'closed':
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
            label_3.text = loan_status[i]
            icon = self.ids[icon]  # Fix the variable name here
            icon.opacity = 1

        h = self.ids.box1.height

        for i in range(a + 1):
            h += 150
        self.ids.box1.height = h

    def get_table_data(self):
        # Make a call to the Anvil server function
        # Replace 'YourAnvilFunction' with the actual name of your Anvil server function
        return anvil.server.call('foreclosure_data')

    def icon_button_clicked(self, value):
        data = self.get_table_data()  # Fetch data here
        self.manager.current = 'ViewProfileScreenLF'
        self.manager.get_screen('ViewProfileScreenLF').initialize_with_value(value, data)

    def on_back_button_press(self):
        self.manager.current = 'DashboardScreenLF'


class RejectedLoansLF(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        data = self.get_table_data()
        loan_id = []
        loan_amount = []
        loan_status = []
        s = 0
        for i in data:
            s += 1
            loan_id.append(i['loan_id'])
            loan_amount.append(i['loan_amount'])
            loan_status.append(i['status'])

        c = -1
        index_list = []
        for i in range(s):
            c += 1
            if loan_status[i] == 'rejected':
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
            label_3.text = loan_status[i]
            icon = self.ids[icon]  # Fix the variable name here
            icon.opacity = 1

        h = self.ids.box1.height

        for i in range(a + 1):
            h += 150
        self.ids.box1.height = h

    def get_table_data(self):
        # Make a call to the Anvil server function
        # Replace 'YourAnvilFunction' with the actual name of your Anvil server function
        return anvil.server.call('foreclosure_data')

    def icon_button_clicked(self, value):
        data = self.get_table_data()  # Fetch data here
        self.manager.current = 'ViewProfileScreenLF'
        self.manager.get_screen('ViewProfileScreenLF').initialize_with_value(value, data)

    def on_back_button_press(self):
        self.manager.current = 'DashboardScreenLF'


class UnderProcessLoansLF(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        data = self.get_table_data()
        loan_id = []
        loan_amount = []
        loan_status = []
        s = 0
        for i in data:
            s += 1
            loan_id.append(i['loan_id'])
            loan_amount.append(i['loan_amount'])
            loan_status.append(i['status'])

        c = -1
        index_list = []
        for i in range(s):
            c += 1
            if loan_status[i] == 'under process':
                index_list.append(c)

        b = 1
        k = -1
        for i, index in enumerate(index_list):
            k += 1
            id_label = f"label_{k}"
            amount = f"amount_{k}"
            status = f"status_{k}"
            icon = f"icon_{k}"

            try:
                label_1 = self.ids[id_label]
                label_1.text = str(loan_id[index])
                label_2 = self.ids[amount]
                label_2.text = str(loan_amount[index])
                label_3 = self.ids[status]
                label_3.text = loan_status[index]
                icon = self.ids[icon]
                icon.opacity = 1
            except KeyError as e:
                print(
                    f"KeyError: {e}, id_label: {id_label}, amount: {amount}, status: {status}, icon: {icon}, index: {index}, i: {i}")

        h = self.ids.box1.height

        for i in range(a + 1):
            h += 150
        self.ids.box1.height = h

    def get_table_data(self):
        # Make a call to the Anvil server function
        # Replace 'YourAnvilFunction' with the actual name of your Anvil server function
        return anvil.server.call('foreclosure_data')

    def icon_button_clicked(self, value):
        data = self.get_table_data()  # Fetch data here
        self.manager.current = 'ViewProfileScreenLF'
        self.manager.get_screen('ViewProfileScreenLF').initialize_with_value(value, data)

    def on_back_button_press(self):
        self.manager.current = 'DashboardScreenLF'


class ViewAllLoansLF(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        data = self.get_table_data()
        loan_id = []
        loan_amount = []
        loan_status = []
        s = 0
        approved_loans = []
        rejected_loans = []
        underprocess_loans = []
        closed_loans = []
        for i in data:
            s += 1
            loan_id.append(i['loan_id'])
            loan_amount.append(i['loan_amount'])
            loan_status.append(i['status'])

            if i['status'] == 'approved':
                approved_loans.append(s - 1)
            elif i['status'] == 'rejected':
                rejected_loans.append(s - 1)
            elif i['status'] == 'under process':
                underprocess_loans.append(s - 1)
            elif i['status'] == 'closed':
                closed_loans.append(s - 1)

        # Iterate over approved loans
        k = -1
        for i in approved_loans:
            k += 1
            self.populate_loan_data(i, k, loan_id, loan_amount, loan_status)

        # Iterate over rejected loans
        for i in rejected_loans:
            k += 1
            self.populate_loan_data(i, k, loan_id, loan_amount, loan_status)

        for i in underprocess_loans:
            k += 1
            self.populate_loan_data(i, k, loan_id, loan_amount, loan_status)

        for i in closed_loans:
            k += 1
            self.populate_loan_data(i, k, loan_id, loan_amount, loan_status)
        # Iterate over new loans

    def populate_loan_data(self, i, k, loan_id, loan_amount, loan_status):
        id_label = f"label_{k}"
        amount = f"amount_{k}"
        status = f"status_{k}"
        icon = f"icon_{k}"  # Fix the variable name here

        label_1 = self.ids[id_label]
        label_1.text = loan_id[i]
        label_2 = self.ids[amount]
        label_2.text = str(loan_amount[i])
        label_3 = self.ids[status]
        label_3.text = loan_status[i]
        icon = self.ids[icon]  # Fix the variable name here
        icon.opacity = 1

        h = self.ids.box1.height

        for i in range(a + 1):
            h += 5
        self.ids.box1.height = h

    def on_back_button_press(self):
        self.manager.current = 'DashboardScreenLF'

    def get_table_data(self):
        # Make a call to the Anvil server function
        # Replace 'YourAnvilFunction' with the actual name of your Anvil server function
        return anvil.server.call('foreclosure_data')

    def icon_button_clicked(self, value):
        data = self.get_table_data()  # Fetch data here
        self.manager.current = 'ViewProfileScreenLF'
        self.manager.get_screen('ViewProfileScreenLF').initialize_with_value(value, data)


class ViewProfileScreenLF(Screen):
    def initialize_with_value(self, value, data):
        loan_id = []
        borrower_name = []
        loan_amount = []
        interest = []
        forecloser_fee = []
        forecloser_amount = []
        total_amount = []
        outstanding_amount = []
        reason_foreclose = []
        total_due_amount = []

        for i in data:
            loan_id.append(i['loan_id'])
            borrower_name.append(i['borrower_name'])
            loan_amount.append(i['loan_amount'])
            forecloser_fee.append(i['foreclose_fee'])
            forecloser_amount.append(i['foreclose_amount'])
            interest.append(i['interest_rate'])
            total_amount.append(i['paid_amount'])
            outstanding_amount.append(i['outstanding_amount'])
            reason_foreclose.append(i['reason'])
            total_due_amount.append(i['total_due_amount'])
        if value in loan_id:
            index = loan_id.index(value)
            self.ids.loan1.text = str(loan_id[index])
            self.ids.amount.text = str(loan_amount[index])
            self.ids.name.text = str(borrower_name[index])
            self.ids.fee.text = str(forecloser_fee[index])
            self.ids.famount.text = str(forecloser_amount[index])
            self.ids.rate.text = str(interest[index])
            self.ids.total_paid.text = str(total_amount[index])
            self.ids.samount.text = str(outstanding_amount[index])
            self.ids.reason.text = str(reason_foreclose[index])
            self.ids.due_amount.text = str(total_due_amount[index])

    def approved_click(self):
        data = self.get_table_data()
        loan_id = self.ids.loan1.text
        print(loan_id)

        loan_idlist = []
        for i in data:
            loan_idlist.append(i['loan_id'])
        print(loan_idlist)
        if loan_id in loan_idlist:
            index = loan_idlist.index(loan_id)
            data[index]['status'] = 'approved'
            self.manager.current = 'DashboardScreenLF'

    def rejected_click(self):
        data = self.get_table_data()
        loan_id = self.ids.loan1.text
        print(loan_id)

        loan_idlist = []
        for i in data:
            loan_idlist.append(i['loan_id'])
        print(loan_idlist)
        if loan_id in loan_idlist:
            index = loan_idlist.index(loan_id)
            data[index]['status'] = 'rejected'
            self.manager.current = 'DashboardScreenLF'

    def get_table_data(self):
        # Make a call to the Anvil server function
        # Replace 'YourAnvilFunction' with the actual name of your Anvil server function
        return anvil.server.call('foreclosure_data')


class MyScreenManager(ScreenManager):
    pass