import sqlite3

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, SlideTransition, ScreenManager
from kivy.utils import platform
from kivy.clock import mainthread
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.spinner import MDSpinner
from borrower_extend_loan import ExtensionLoansRequest
from borrower_application_tracker import ApplicationTrackerScreen
from new_loan_request import NewloanScreen
from borrower_viewloan import DashboardScreenVLB
from borrower_foreclosure import LoansDetailsB
from kivy.uix.modalview import ModalView
from kivymd.uix.spinner import MDSpinner
from kivy.clock import Clock

if platform == 'android':
    from kivy.uix.button import Button
    from kivy.uix.modalview import ModalView
    from kivy.clock import Clock
    from android import api_version, mActivity
    from android.permissions import (
        request_permissions, check_permission, Permission)

user_helpers = """
<WindowManager>:
    DashboardScreen:
    ProfileScreen:
    LoansDetails:
    Foreclosure:
    ForecloseDetails:

<DashboardScreen>:
    MDFloatLayout:
        md_bg_color:1,1,1,1
        size_hint: 1, 1 

        MDTopAppBar:
            md_bg_color:1,1,1,1
            specific_text_color:1/255, 26/255, 51/255, 1
            elevation: 3
            left_action_items: [['account', lambda x: root.go_to_profile()]]
            right_action_items: [['wallet', lambda x:root.go_to_wallet()],['logout', lambda x: root.logout()]]
            pos_hint: {'center_x': 0.5, 'center_y': 0.96}
        Image:
            source:"LOGO.png"
            pos_hint: {'center_x': 0.5, 'center_y': 0.96555}        
            md_bg_color:0,0,0,1
            size_hint: None,None 
            height: dp(50)
            width: dp(60)
        MDGridLayout:
            cols: 3

            spacing: dp(15)
            size_hint_y: None
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            height: self.minimum_height
            width: self.minimum_width
            size_hint_x: None

            MDFlatButton:
                size_hint: None, None

                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                md_bg_color: 0.031, 0.463, 0.91, 1 

                size_hint_y: None
                height: dp(60)
                size_hint_x: None
                width: dp(110)
                on_release: root.go_to_newloan_screen()
                BoxLayout:
                    orientation: 'horizontal'
                    spacing:dp(10)
                    MDLabel:
                        text: "New Loan Requests"
                        font_size:dp(14)
                        bold:True
                        theme_text_color: 'Custom'
                        halign: "center"
                        text_color:1,1,1,1
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            MDFlatButton:
                size_hint: None, None

                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                md_bg_color: 0.031, 0.463, 0.91, 1 
                on_release: root.go_to_view_loan_screen()
                size_hint_y: None
                height: dp(60)
                size_hint_x: None
                width: dp(110)

                BoxLayout:
                    orientation: 'horizontal'
                    spacing:dp(10)
                    MDLabel:
                        text: "View Loans"
                        font_size:dp(14)
                        bold:True
                        theme_text_color: 'Custom'
                        halign: "center"
                        text_color:1,1,1,1
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            MDFlatButton:
                size_hint: None, None

                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                md_bg_color: 0.031, 0.463, 0.91, 1 

                size_hint_y: None
                height: dp(60)
                size_hint_x: None
                width: dp(110)

                BoxLayout:
                    orientation: 'horizontal'
                    spacing:dp(10)
                    MDLabel:
                        text: "Today's Dues"
                        font_size:dp(14)
                        bold:True
                        theme_text_color: 'Custom'
                        halign: "center"
                        text_color:1,1,1,1
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            MDFlatButton:
                size_hint: None, None

                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                md_bg_color: 0.031, 0.463, 0.91, 1 

                size_hint_y: None
                height: dp(60)
                size_hint_x: None
                width: dp(110)
                on_release: root.go_to_app_tracker()
                BoxLayout:
                    orientation: 'horizontal'
                    spacing:dp(10)
                    MDLabel:
                        text: "Application Tracker"
                        font_size:dp(14)
                        bold:True
                        theme_text_color: 'Custom'
                        halign: "center"
                        text_color:1,1,1,1
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}



            MDFlatButton:
                size_hint: None, None

                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                md_bg_color: 0.031, 0.463, 0.91, 1 

                size_hint_y: None
                height: dp(60)
                size_hint_x: None
                width: dp(110)

                BoxLayout:
                    orientation: 'horizontal'
                    spacing:dp(10)
                    MDLabel:
                        text: "Discount Coupons"
                        font_size:dp(14)
                        bold:True
                        theme_text_color: 'Custom'
                        halign: "center"
                        text_color:1,1,1,1
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            MDFlatButton:
                size_hint: None, None

                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                md_bg_color: 0.031, 0.463, 0.91, 1 
                on_release: root.go_to_fore_closer_details()
                size_hint_y: None
                height: dp(60)
                size_hint_x: None
                width: dp(110)

                BoxLayout:
                    orientation: 'horizontal'
                    spacing:dp(10)
                    MDLabel:
                        text: "Loan Foreclose"
                        font_size:dp(14)

                        bold:True
                        theme_text_color: 'Custom'
                        halign: "center"
                        text_color:1,1,1,1
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            MDLabel:
                text:""
            MDFlatButton:
                size_hint: None, None
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                md_bg_color: 0.031, 0.463, 0.91, 1 
                on_release:root.go_to_extend()
                size_hint_y: None
                height: dp(60)
                size_hint_x: None
                width: dp(110)

                BoxLayout:
                    orientation: 'horizontal'
                    spacing:dp(10)
                    MDLabel:
                        text: "Extended Loan Request"
                        font_size:dp(14)
                        bold:True
                        theme_text_color: 'Custom'
                        halign: "center"
                        text_color:1,1,1,1
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}


        MDIconButton:
            icon:'help-circle'
            theme_text_color: 'Custom'
            text_color: 1,1,1,1
            pos_hint: {'center_x': 0.92, 'center_y': 0.1}
            md_bg_color: 0.031, 0.463, 0.91, 1     

<ProfileScreen>
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            size: self.size
            pos: self.pos

    BoxLayout:
        orientation: 'vertical'
        size_hint: 1, 1
        pos_hint: {'center_x':0.5, 'center_y':0.5}

        MDTopAppBar:
            title: "View Profile"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.on_back_button_press()]]
        ScrollView:  # Add ScrollView here
            do_scroll_x: False
            BoxLayout:
                orientation: "vertical"
                padding:dp(35)
                spacing:dp(20)
                size_hint_y: None
                height: self.minimum_height



                MDRectangleFlatButton:

                    line_color:1,1,1,1
                    size_hint: None, None
                    size: dp(120), dp(120)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    canvas.before:
                        Color:
                            rgba: 174/255, 214/255, 241/255, 1
                        Ellipse:
                            size: self.size
                            pos: self.pos 

                    Image:
                        id: selected_image1
                        source: "profile.png"


                    MDFloatLayout:

                        size_hint:(None,None)
                        spacing:0
                        padding:0
                        pos_hint: {'center_x': 0, 'center_y': 0}
                        MDIconButton:
                            icon: 'camera-plus'
                            on_release: app.root.get_screen('ProfileScreen').check_and_open_file_manager1()
                            pos_hint: {'center_x':1.2, 'center_y':0}
                Label:
                    id: selected_file_label
                    text: 'Selected File: None'
                    size_hint_y: None
                    height: 30
                MDLabel:
                    text: ' Customer ID '
                    color: 0, 0, 0, 1
                    halign: 'left'
                    size_hint_x: 1
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    bold: True
                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width


                    MDTextField:
                        id: text_input1
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]
                        line_color_focus: [1, 1, 1, 1]
                        readonly: True
                MDLabel:
                    text: ' Full Name '
                    color: 0, 0, 0, 1
                    halign: 'left'
                    size_hint_x: 1
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    bold: True
                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDFlatButton:
                        text: "EDIT"
                        id: edit_button
                        size_hint: None, None
                        pos_hint: {'center_x': 0.9, 'center_y': 0.5}
                        theme_text_color: "Custom"
                        text_color: 6/255, 143/255, 236/255, 1
                        font_name: "Roboto-Bold"


                    MDTextField:
                        id: text_input2
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"

                MDLabel:
                    text: ' Date of Birth '
                    color: 0, 0, 0, 1
                    halign: 'left'
                    size_hint_x: 1
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    bold: True
                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDTextField:
                        id: text_input4
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"
                MDLabel:
                    text: ' Gender '
                    color: 0, 0, 0, 1
                    halign: 'left'
                    size_hint_x: 1
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    bold: True
                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDTextField:
                        id: text_input5
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"

                MDLabel:
                    text: ' Mobile Number '
                    color: 0, 0, 0, 1
                    halign: 'left'
                    size_hint_x: 1
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    bold: True

                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDFlatButton:
                        text: "EDIT"
                        pos_hint: {'center_x': 0.9, 'center_y': 0.5}
                        theme_text_color: "Custom"
                        text_color:6/255, 143/255, 236/255, 1
                        font_name: "Roboto-Bold"

                    MDTextField:
                        id: text_input7
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"

                MDLabel:
                    text: ' Government ID '
                    color: 0, 0, 0, 1
                    halign: 'left'
                    size_hint_x: 1
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    bold: True

                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width



                    MDTextField:
                        id: text_input8
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"
                        readonly: True
                MDLabel:
                    text: ' PAN Number '
                    color: 0, 0, 0, 1
                    halign: 'left'
                    size_hint_x: 1
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    bold: True

                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width



                    MDTextField:
                        id: text_input9
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"
                        readonly: True
                MDLabel:
                    text: ' City '
                    color: 0, 0, 0, 1
                    halign: 'left'
                    size_hint_x: 1
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    bold: True

                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDFlatButton:
                        text: "EDIT"
                        pos_hint: {'center_x': 0.9, 'center_y': 0.5}
                        theme_text_color: "Custom"
                        text_color:6/255, 143/255, 236/255, 1
                        font_name: "Roboto-Bold"

                    MDTextField:
                        id: text_input10
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"

                MDLabel:
                    text: ' Spouse Name '
                    color: 0, 0, 0, 1
                    halign: 'left'
                    size_hint_x: 1
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    bold: True

                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDFlatButton:
                        text: "EDIT"
                        pos_hint: {'center_x': 0.9, 'center_y': 0.5}
                        theme_text_color: "Custom"
                        text_color:6/255, 143/255, 236/255, 1
                        font_name: "Roboto-Bold"

                    MDTextField:
                        id: text_input13
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"
                MDLabel:
                    text: ' Spouse Mobile '
                    color: 0, 0, 0, 1
                    halign: 'left'
                    size_hint_x: 1
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    bold: True

                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDFlatButton:
                        text: "EDIT"
                        pos_hint: {'center_x': 0.9, 'center_y': 0.5}
                        theme_text_color: "Custom"
                        text_color:6/255, 143/255, 236/255, 1
                        font_name: "Roboto-Bold"

                    MDTextField:
                        id: text_input14
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"

                MDLabel:
                    text: ' Spouse Company Name '
                    color: 0, 0, 0, 1
                    halign: 'left'
                    size_hint_x: 1
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    bold: True

                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDFlatButton:
                        text: "EDIT"
                        pos_hint: {'center_x': 0.9, 'center_y': 0.5}
                        theme_text_color: "Custom"
                        text_color:6/255, 143/255, 236/255, 1
                        font_name: "Roboto-Bold"

                    MDTextField:
                        id: text_input15
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"

                MDLabel:
                    text: ' Spouse Company Address '
                    color: 0, 0, 0, 1
                    halign: 'left'
                    size_hint_x: 1
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    bold: True

                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDFlatButton:
                        text: "EDIT"
                        pos_hint: {'center_x': 0.9, 'center_y': 0.5}
                        theme_text_color: "Custom"
                        text_color:6/255, 143/255, 236/255, 1
                        font_name: "Roboto-Bold"

                    MDTextField:
                        id: text_input16
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"

                MDLabel:
                    text: ' Spouse Profession '
                    color: 0, 0, 0, 1
                    halign: 'left'
                    size_hint_x: 1
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    bold: True

                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDFlatButton:
                        text: "EDIT"
                        pos_hint: {'center_x': 0.9, 'center_y': 0.5}
                        theme_text_color: "Custom"
                        text_color:6/255, 143/255, 236/255, 1
                        font_name: "Roboto-Bold"

                    MDTextField:
                        id: text_input17
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"

                MDLabel:
                    text: ' User Type '
                    color: 0, 0, 0, 1
                    halign: 'left'
                    size_hint_x: 1
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    bold: True

                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDTextField:
                        id: text_input19
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"

                MDLabel:
                    text: ' Registration Approve Date '
                    color: 0, 0, 0, 1
                    halign: 'left'
                    size_hint_x: 1
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    bold: True

                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width



                    MDTextField:
                        id: text_input20
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"



                MDLabel:
                    text: ' Pincode '
                    color: 0, 0, 0, 1
                    halign: 'left'
                    size_hint_x: 1
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    bold: True

                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDFlatButton:
                        text: "EDIT"
                        pos_hint: {'center_x': 0.9, 'center_y': 0.5}
                        theme_text_color: "Custom"
                        text_color:6/255, 143/255, 236/255, 1
                        font_name: "Roboto-Bold"

                    MDTextField:
                        id: text_input26
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"

                MDLabel:
                    text: ' Qualification '
                    color: 0, 0, 0, 1
                    halign: 'left'
                    size_hint_x: 1
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    bold: True

                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDTextField:
                        id: text_input27
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"

                MDLabel:
                    text: ' State '
                    color: 0, 0, 0, 1
                    halign: 'left'
                    size_hint_x: 1
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    bold: True

                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDFlatButton:
                        text: "EDIT"
                        pos_hint: {'center_x': 0.9, 'center_y': 0.5}
                        theme_text_color: "Custom"
                        text_color:6/255, 143/255, 236/255, 1
                        font_name: "Roboto-Bold"

                    MDTextField:
                        id: text_input28
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"

                MDLabel:
                    text: ' Another Email '
                    color: 0, 0, 0, 1
                    halign: 'left'
                    size_hint_x: 1
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    bold: True
                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDFlatButton:
                        text: "EDIT"
                        pos_hint: {'center_x': 0.9, 'center_y': 0.5}
                        theme_text_color: "Custom"
                        text_color:6/255, 143/255, 236/255, 1
                        font_name: "Roboto-Bold"

                    MDTextField:
                        id: text_input30
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"
                MDLabel:
                    text: ' Company Name '
                    color: 0, 0, 0, 1
                    halign: 'left'
                    size_hint_x: 1
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    bold: True

                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDFlatButton:
                        text: "EDIT"
                        pos_hint: {'center_x': 0.9, 'center_y': 0.5}
                        theme_text_color: "Custom"
                        text_color:6/255, 143/255, 236/255, 1
                        font_name: "Roboto-Bold"

                    MDTextField:
                        id: text_input31
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"
                MDLabel:
                    text: ' Organization Type '
                    color: 0, 0, 0, 1
                    halign: 'left'
                    size_hint_x: 1
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    bold: True

                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDFlatButton:
                        text: "EDIT"
                        pos_hint: {'center_x': 0.9, 'center_y': 0.5}
                        theme_text_color: "Custom"
                        text_color:6/255, 143/255, 236/255, 1
                        font_name: "Roboto-Bold"

                    MDTextField:
                        id: text_input32
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"

                MDLabel:
                    text: ' Employment Type '
                    color: 0, 0, 0, 1
                    halign: 'left'
                    size_hint_x: 1
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    bold: True

                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDFlatButton:
                        text: "EDIT"
                        pos_hint: {'center_x': 0.9, 'center_y': 0.5}
                        theme_text_color: "Custom"
                        text_color:6/255, 143/255, 236/255, 1
                        font_name: "Roboto-Bold"

                    MDTextField:
                        id: text_input33
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"

                MDLabel:
                    text: ' Business no '
                    color: 0, 0, 0, 1
                    halign: 'left'
                    size_hint_x: 1
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    bold: True

                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDFlatButton:
                        text: "EDIT"
                        pos_hint: {'center_x': 0.9, 'center_y': 0.5}
                        theme_text_color: "Custom"
                        text_color:6/255, 143/255, 236/255, 1
                        font_name: "Roboto-Bold"

                    MDTextField:
                        id: text_input34
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"

                MDLabel:
                    text: ' Company Landmark '
                    color: 0, 0, 0, 1
                    halign: 'left'
                    size_hint_x: 1
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    bold: True

                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDFlatButton:
                        text: "EDIT"
                        pos_hint: {'center_x': 0.9, 'center_y': 0.5}
                        theme_text_color: "Custom"
                        text_color:6/255, 143/255, 236/255, 1
                        font_name: "Roboto-Bold"

                    MDTextField:
                        id: text_input35
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"

                MDLabel:
                    text: ' Company Address '
                    color: 0, 0, 0, 1
                    halign: 'left'
                    size_hint_x: 1
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    bold: True

                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDFlatButton:
                        text: "EDIT"
                        pos_hint: {'center_x': 0.9, 'center_y': 0.5}
                        theme_text_color: "Custom"
                        text_color:6/255, 143/255, 236/255, 1
                        font_name: "Roboto-Bold"

                    MDTextField:
                        id: text_input36
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"

                MDLabel:
                    text: ' Annual Salary '
                    color: 0, 0, 0, 1
                    halign: 'left'
                    size_hint_x: 1
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    bold: True

                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDFlatButton:
                        text: "EDIT"
                        pos_hint: {'center_x': 0.9, 'center_y': 0.5}
                        theme_text_color: "Custom"
                        text_color:6/255, 143/255, 236/255, 1
                        font_name: "Roboto-Bold"

                    MDTextField:
                        id: text_input37
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"

                MDLabel:
                    text: ' Designation '
                    color: 0, 0, 0, 1
                    halign: 'left'
                    size_hint_x: 1
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    bold: True

                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDFlatButton:
                        text: "EDIT"
                        pos_hint: {'center_x': 0.9, 'center_y': 0.5}
                        theme_text_color: "Custom"
                        text_color:6/255, 143/255, 236/255, 1
                        font_name: "Roboto-Bold"

                    MDTextField:
                        id: text_input38
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"

                MDLabel:
                    text: ' Account Name '
                    color: 0, 0, 0, 1
                    halign: 'left'
                    size_hint_x: 1
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    bold: True

                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDTextField:
                        id: text_input39
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"

                MDLabel:
                    text: ' Account Type '
                    color: 0, 0, 0, 1
                    halign: 'left'
                    size_hint_x: 1
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    bold: True

                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDTextField:
                        id: text_input40
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"

                MDLabel:
                    text: ' Account Number '
                    color: 0, 0, 0, 1
                    halign: 'left'
                    size_hint_x: 1
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    bold: True

                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width


                    MDTextField:
                        id: text_input41
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"


                MDLabel:
                    text: ' Bank Name'
                    color: 0, 0, 0, 1
                    halign: 'left'
                    size_hint_x: 1
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    bold: True


                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDFlatButton:
                        text: "EDIT"
                        pos_hint: {'center_x': 0.9, 'center_y': 0.5}
                        theme_text_color: "Custom"
                        text_color:6/255, 143/255, 236/255, 1
                        font_name: "Roboto-Bold"

                    MDTextField:
                        id: text_input43
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"

                MDLabel:
                    text: ' Select Bank '
                    color: 0, 0, 0, 1
                    halign: 'left'
                    size_hint_x: 1
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    bold: True


                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDTextField:
                        id: text_input45
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"



                MDLabel:
                    text: ' Father Name '
                    color: 0, 0, 0, 1
                    halign: 'left'
                    size_hint_x: 1
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    bold: True


                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDTextField:
                        id: text_input47
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"

                MDLabel:
                    text: ' Father Age '
                    color: 0, 0, 0, 1
                    halign: 'left'
                    size_hint_x: 1
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    bold: True


                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDTextField:
                        id: text_input48
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"

                MDLabel:
                    text: ' Mother Name '
                    color: 0, 0, 0, 1
                    halign: 'left'
                    size_hint_x: 1
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    bold: True


                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDTextField:
                        id: text_input49
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"


                MDLabel:
                    text: ' Mother Age '
                    color: 0, 0, 0, 1
                    halign: 'left'
                    size_hint_x: 1
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    bold: True


                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDTextField:
                        id: text_input50
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"

                MDLabel:
                    text: ' College Name '
                    color: 0, 0, 0, 1
                    halign: 'left'
                    size_hint_x: 1
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    bold: True


                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDTextField:
                        id: text_input51
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"

                MDLabel:
                    text: ' College ID '
                    color: 0, 0, 0, 1
                    halign: 'left'
                    size_hint_x: 1
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    bold: True


                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDTextField:
                        id: text_input52
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"

                MDLabel:
                    text: ' College Address '
                    color: 0, 0, 0, 1
                    halign: 'left'
                    size_hint_x: 1
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    bold: True


                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDTextField:
                        id: text_input53
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"


<LoansDetails>:
    BoxLayout:
        orientation: 'vertical'
        size_hint: 1, 1
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}

        MDTopAppBar:
            title: "All Loans"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.on_back_button_press()]]

        BoxLayout:
            orientation: 'vertical'
            size_hint: 1, 1 
            padding: dp(10)  

            GridLayout:
                cols: 4
                spacing: dp(7)
                padding: dp(5)  
                size_hint: 1, None
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}  

                MDLabel:
                    text: "Loan Amount" 
                MDLabel:
                    text: "Loan Status" 
                MDLabel:
                    text: "Tenure" 
                MDLabel:
                    text: "View   Status"


            Widget:
                size_hint_y: None
                height: dp(2)  
                canvas:
                    Color:
                        rgba: 0, 0, 0, 1 
                    Line:
                        points: self.x, self.y, self.x + self.width, self.y

            GridLayout:
                cols: 4
                spacing: dp(5)
                padding: dp(5)  
                size_hint: 1, None
                height: dp(40) 
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}

                MDLabel:
                    text: "50000"  
                MDLabel:
                    text: "Approved"
                MDLabel:
                    text: "  12"
                Button:
                    text: "View Profile "
                    text_color: 0, 0, 0, 1
                    background_color: 0.529, 0.807, 0.922, 0
                    on_release: root.go_to_foreclose()
                    color: 0, 0, 0, 1
                    bold: True
                    canvas.before:
                        Color:
                            rgba:0.529, 0.807, 0.922, 1 

        MDLabel:
            text: ""
        MDLabel:
            text: ""
        MDLabel:
            text:""
        MDLabel:
        	text:""
        MDLabel:
        	text:""
<Foreclosure>:
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
        padding: [40, 0]
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
                    id: text_input1
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
                text: "Loan Available Date"

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
                    id: text_input1
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
                    id: text_input1
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
                text: "Interest"

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
                    id: text_input1
                    size_hint: None, None
                    size_hint_x: 0.81
                    multiline: False
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    line_color_normal: [1, 1, 1, 1]  
                    line_color_focus: [1, 1, 1, 1]
                    font_name: "Roboto-Bold"
        MDGridLayout:
            cols: 2
            spacing: 60

            MDLabel:
                text: "Precessing Fee"

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
                    id: text_input
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
                text: "Loan Repayment Amount"

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
                    id: text_input1
                    size_hint: None, None
                    size_hint_x: 0.81
                    multiline: False
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    line_color_normal: [1, 1, 1, 1]  
                    line_color_focus: [1, 1, 1, 1]
                    font_name: "Roboto-Bold"
        MDGridLayout:
            cols: 2
            spacing: 60

            MDLabel:
                text: "Loan Due Date"

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
                    id: text_input1
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
                size_hint: ( None, 1)
                width: 50
                bold: True
                color: (195/255,110/255,108/255,1)

            MDLabel:
                text: "I Agree Terms and Conditions"
                multiline: False



        MDGridLayout:
            cols: 2
            spacing: 30
            padding: [20, 0]
            size_hint: 1, None
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
                on_release: root.go_to_foreclose_details()
                size_hint: 1, 1

<ForecloseDetails>:
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
                    size_hint: 1, None
                    height: dp(5)  
                    canvas:
                        Color:
                            rgba: 0, 0, 0, 1 
                        Line:
                            points: self.x, self.y, self.x + self.width, self.y
                MDLabel:
                    text: "Amount Paid"
                    bold: True
                GridLayout:
                    cols: 2
                    size_hint_y: None
                    height: self.minimum_height
                    padding: dp(10)
                    spacing: dp(35)

                    MDLabel:
                        text: "Total Amount paid"
                        bold: True

                    MDLabel:
                        id: totallamount
                        text: "Total amount"
                    MDLabel:
                        text: "Monthly Installments  "

                    MDLabel:
                        id: monthlyinterest
                        text: "Monthly Installments"

                    MDLabel:
                        text: "Interest Amount"

                    MDLabel:
                        id: interestamount
                        text: "interest amount"
                    MDLabel:
                        text: "Monthly EMI"

                    MDLabel:
                        id: monthlyamount
                        text: "Monthly amount"

                Widget:
                    size_hint: 1, None
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
                    height: self.minimum_height
                    padding: dp(10)
                    spacing: dp(50)

                    MDLabel:
                        text: " Overall Outstanding Amount"
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
                    size_hint: 1, None
                    canvas:
                        Color:
                            rgba: 0, 0, 0, 1 
                        Line:
                            points: self.x, self.y, self.x + self.width, self.y

                MDLabel:
                    text: "Amount Due"
                    bold: True
                GridLayout:
                    cols: 2
                    size_hint_y: None
                    height: self.minimum_height
                    padding: dp(10)
                    spacing: dp(35)

                    MDLabel:
                        text: "Outstanding Amount"
                        bold: True

                    MDLabel:
                        id: outstandingamount
                        text: "Outstanding amount"
                    MDLabel:
                        text: "Foreclosure fee"

                    MDLabel:
                        id: foreclouser
                        text: "Foreclosure fee"

                    MDLabel:
                        text: "Foreclosure Amount"

                    MDLabel:
                        id: foreclosureamount
                        text: "Foreclosure Amount"

                BoxLayout:
                    orientation: "vertical"
                    size_hint_y: None
                    height: self.minimum_height

                    MDLabel:
                        text: 'Reason for Foreclosure '
                        valign: 'top'
                        bold: True

                    MDTextField:
                        hint_text: 'Enter text here'

                BoxLayout:
                    orientation: "horizontal"
                    size_hint_y: None
                    height: self.minimum_height


                    CheckBox:
                        size_hint: None, None
                        width: dp(30) 
                        color: (195/255, 110/255, 108/255, 1)

                    MDLabel:
                        text: "I Agree Terms and Conditions"
                        multiline: False  

                MDGridLayout:
                    cols: 2
                    spacing: dp(10)
                    padding: dp(5)
                    size_hint: 1, None

                    MDRaisedButton:
                        text: "CANCEL"
                        md_bg_color: 0.031, 0.463, 0.91, 1
                        theme_text_color: 'Custom'
                        on_release: app.root.current = 'LoansDetails'
                        text_color: 1, 1, 1, 1
                        size_hint: 1, None

                    MDRaisedButton:
                        text: "SUBMIT"
                        md_bg_color: 0.031, 0.463, 0.91, 1
                        size_hint: 1, None
"""
conn = sqlite3.connect('fin_user_profile.db')
cursor = conn.cursor()


class DashboardScreen(Screen):
    Builder.load_string(user_helpers)

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'BorrowerLanding'

    def go_to_newloan_screen(self):
        # Show modal view with spinner
        modal_view = ModalView(size_hint=(None, None), size=(100, 100), background_color=[0, 0, 0, 0])
        spinner = MDSpinner()
        modal_view.add_widget(spinner)
        modal_view.open()

        # Perform the actual action (e.g., fetching loan requests)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(lambda dt: self.perform_loan_request_action(modal_view), 2)

    def perform_loan_request_action(self, modal_view):
        # Close the modal view after performing the action
        modal_view.dismiss()
        # Get the existing ScreenManager
        sm = self.manager

        # Create a new instance of the LoginScreen
        login_screen = NewloanScreen(name='NewloanScreen')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(login_screen)

        # Switch to the LoginScreen
        sm.current = 'NewloanScreen'

    def go_to_view_loan_screen(self):
        # Show modal view with spinner
        modal_view = ModalView(size_hint=(None, None), size=(100, 100), background_color=[0, 0, 0, 0])
        spinner = MDSpinner()
        modal_view.add_widget(spinner)
        modal_view.open()

        # Perform the actual action (e.g., fetching loan requests)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(lambda dt: self.perform_view_loan_screen_action(modal_view), 2)

    def perform_view_loan_screen_action(self, modal_view):
        # Close the modal view after performing the action
        modal_view.dismiss()
        sm = self.manager

        # Create a new instance of the LoginScreen
        login_screen = DashboardScreenVLB(name='DashboardScreenVLB')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(login_screen)

        # Switch to the LoginScreen
        sm.current = 'DashboardScreenVLB'

    def go_to_app_tracker(self):
        modal_view = ModalView(size_hint=(None, None), size=(100, 100), background_color=[0, 0, 0, 0])
        spinner = MDSpinner()
        modal_view.add_widget(spinner)
        modal_view.open()

        # Perform the actual action (e.g., fetching loan requests)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(lambda dt: self.perform_app_tracker_action(modal_view), 2)

    def perform_app_tracker_action(self, modal_view):
        # Close the modal view after performing the action
        modal_view.dismiss()
        # Get the existing ScreenManager
        sm = self.manager

        # Create a new instance of the LoginScreen
        login_screen = ApplicationTrackerScreen(name='ApplicationTrackerScreen')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(login_screen)

        # Switch to the LoginScreen
        sm.current = 'ApplicationTrackerScreen'

    def go_to_extend(self):
        modal_view = ModalView(size_hint=(None, None), size=(100, 100), background_color=[0, 0, 0, 0])
        spinner = MDSpinner()
        modal_view.add_widget(spinner)
        modal_view.open()

        # Perform the actual action (e.g., fetching loan requests)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(lambda dt: self.perform_extend_action(modal_view), 2)

    def perform_extend_action(self, modal_view):
        # Close the modal view after performing the action
        modal_view.dismiss()
        sm = self.manager
        # Create a new instance of the LoginScreen
        login_screen = ExtensionLoansRequest(name='ExtensionLoansRequest')
        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(login_screen)
        # Switch to the LoginScreen
        sm.current = 'ExtensionLoansRequest'

    def go_to_fore_closer_details(self):
        modal_view = ModalView(size_hint=(None, None), size=(100, 100), background_color=[0, 0, 0, 0])
        spinner = MDSpinner()
        modal_view.add_widget(spinner)
        modal_view.open()

        # Perform the actual action (e.g., fetching loan requests)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(lambda dt: self.perform_fore_closer_details_action(modal_view), 2)

    def perform_fore_closer_details_action(self, modal_view):
        # Close the modal view after performing the action
        modal_view.dismiss()
        sm = self.manager

        # Create a new instance of the LoginScreen
        login_screen = LoansDetailsB(name='LoansDetailsB')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(login_screen)

        # Switch to the LoginScreen
        sm.current = 'LoansDetailsB'

    def go_to_loan_details(self):
        modal_view = ModalView(size_hint=(None, None), size=(100, 100), background_color=[0, 0, 0, 0])
        spinner = MDSpinner()
        modal_view.add_widget(spinner)
        modal_view.open()

        # Perform the actual action (e.g., fetching loan requests)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(lambda dt: self.perform_loan_details_action(modal_view), 2)

    def perform_loan_details_action(self, modal_view):
        # Close the modal view after performing the action
        modal_view.dismiss()
        # Get the existing ScreenManager
        sm = self.manager

        # Create a new instance of the LoginScreen
        login_screen = LoansDetails(name='LoansDetails')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(login_screen)

        # Switch to the LoginScreen
        sm.current = 'LoansDetails'

    def logout(self):
        self.manager.current = 'MainScreen'

    def go_to_profile(self):
        modal_view = ModalView(size_hint=(None, None), size=(100, 100), background_color=[0, 0, 0, 0])
        spinner = MDSpinner()
        modal_view.add_widget(spinner)
        modal_view.open()

        # Perform the actual action (e.g., fetching loan requests)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(lambda dt: self.perform_profile_action(modal_view), 2)

    def perform_profile_action(self, modal_view):
        # Close the modal view after performing the action
        modal_view.dismiss()
        # Get the existing ScreenManager
        sm = self.manager

        # Create a new instance of the LoginScreen
        login_screen = ProfileScreen(name='ProfileScreen')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(login_screen)

        # Switch to the LoginScreen
        sm.current = 'ProfileScreen'


    def go_to_wallet(self):
        modal_view = ModalView(size_hint=(None, None), size=(100, 100), background_color=[0, 0, 0, 0])
        spinner = MDSpinner()
        modal_view.add_widget(spinner)
        modal_view.open()

        # Perform the actual action (e.g., fetching loan requests)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(lambda dt: self.perform_wallet(modal_view), 2)

    def perform_wallet(self, modal_view):
        from borrower_wallet import WalletScreen
        modal_view.dismiss()
        # Get the existing ScreenManager
        sm = self.manager

        # Create a new instance of the LoginScreen
        login_screen = WalletScreen(name='WalletScreen')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(login_screen)

        # Switch to the LoginScreen
        sm.current = 'WalletScreen'





class ProfileScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        cursor.execute('select * from fin_users')
        users = cursor.fetchall()

        status = []
        customer = []

        for i in users:
            status.append(i[-1])
            customer.append(i[0])

        log_index = status.index('logged')

        cursor.execute('select * from fin_registration_table')
        rows = cursor.fetchall()
        row_id_list = []
        name_list = []
        dateofbirth_list = []
        gender_list = []
        mobile_list = []
        aadhar_list = []
        pan_list = []
        city_list = []
        sname_list = []
        smobile_list = []
        scompanyname_list = []
        scompanyaddress_list = []
        sprofession_list = []
        usertype_list = []
        sdatafiled_list = []
        pincode_list = []
        qualification_list = []
        state_list = []
        anothermail_list = []
        company_list = []
        organization_list = []
        employmenttype_list = []
        businessno_list = []
        companylandmark_list = []
        companyaddress_list = []
        cannualsalary_list = []
        designation_list = []
        accountname_list = []
        accounttype_list = []
        accountnumber_list = []
        branchname_list = []
        ifsccode_list = []
        sbank_list = []
        fathername_list = []
        fatherage_list = []
        mothername_list = []
        motherage_list = []
        collegename_list = []
        collageid_list = []
        collageaddress_list = []

        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
            name_list.append(row[1])
            dateofbirth_list.append(row[3])
            gender_list.append(row[2])
            mobile_list.append(row[4])
            aadhar_list.append(row[8])
            pan_list.append(row[9])
            city_list.append(row[19])
            sname_list.append(row[76])
            smobile_list.append(row[78])
            scompanyname_list.append(row[80])
            scompanyaddress_list.append(row[81])
            sprofession_list.append(row[79])
            usertype_list.append(row[84])
            sdatafiled_list.append(row[77])
            pincode_list.append(row[20])
            qualification_list.append(row[12])
            state_list.append(row[21])
            anothermail_list.append(row[6])
            company_list.append(row[40])
            organization_list.append(row[41])
            employmenttype_list.append(row[39])
            businessno_list.append(row[46])
            companylandmark_list.append(row[45])
            companyaddress_list.append(row[41])
            cannualsalary_list.append(row[47])
            designation_list.append(row[48])
            accountname_list.append(row[51])
            accounttype_list.append(row[52])
            accountnumber_list.append(row[53])
            branchname_list.append(row[56])
            ifsccode_list.append(row[54])
            sbank_list.append(row[53])
            fathername_list.append(row[23])
            fatherage_list.append(row[24])
            mothername_list.append(row[27])
            motherage_list.append(row[28])
            collegename_list.append(row[33])
            collageid_list.append(row[32])
            collageaddress_list.append(row[34])
        if customer[log_index] in row_id_list:
            index = row_id_list.index(customer[log_index])
            self.ids.text_input1.text = str(row_id_list[index])
            self.ids.text_input2.text = name_list[index]
            self.ids.text_input4.text = str(dateofbirth_list[index])
            self.ids.text_input5.text = str(gender_list[index])
            self.ids.text_input7.text = str(mobile_list[index])
            self.ids.text_input8.text = str(aadhar_list[index])
            self.ids.text_input9.text = str(pan_list[index])
            self.ids.text_input10.text = str(city_list[index])
            self.ids.text_input13.text = str(sname_list[index])
            self.ids.text_input14.text = str(smobile_list[index])
            self.ids.text_input15.text = str(scompanyname_list[index])
            self.ids.text_input16.text = str(scompanyaddress_list[index])
            self.ids.text_input17.text = str(sprofession_list[index])
            self.ids.text_input19.text = usertype_list[index]
            self.ids.text_input20.text = str(sdatafiled_list[index])
            self.ids.text_input26.text = str(pincode_list[index])
            self.ids.text_input28.text = str(state_list[index])
            self.ids.text_input27.text = str(qualification_list[index])
            self.ids.text_input30.text = str(anothermail_list[index])
            self.ids.text_input31.text = str(company_list[index])
            self.ids.text_input32.text = str(organization_list[index])
            self.ids.text_input33.text = str(employmenttype_list[index])
            self.ids.text_input34.text = str(businessno_list[index])
            self.ids.text_input35.text = str(companylandmark_list[index])
            self.ids.text_input36.text = str(collageaddress_list[index])
            self.ids.text_input37.text = str(cannualsalary_list[index])
            self.ids.text_input38.text = str(designation_list[index])
            self.ids.text_input39.text = str(accountname_list[index])
            self.ids.text_input40.text = str(accounttype_list[index])
            self.ids.text_input41.text = str(accountnumber_list[index])
            # self.ids.text_input42.text = str(branchname_list[index])
            self.ids.text_input43.text = str(ifsccode_list[index])
            self.ids.text_input45.text = str(sbank_list[index])
            self.ids.text_input47.text = str(fathername_list[index])
            self.ids.text_input48.text = str(fatherage_list[index])
            self.ids.text_input49.text = str(mothername_list[index])
            self.ids.text_input50.text = str(motherage_list[index])
            self.ids.text_input51.text = str(collegename_list[index])
            self.ids.text_input52.text = str(collageid_list[index])
            self.ids.text_input53.text = str(collageaddress_list[index])
        else:
            print('coustomer id not fount ')

    def check_and_open_file_manager1(self):
        self.check_and_open_file_manager("upload_icon1", "upload_label1", "selected_file_label1", "selected_image1")

    def check_and_open_file_manager(self, icon_id, label_id, file_label_id, image_id):
        if platform == 'android':
            if check_permission(Permission.READ_MEDIA_IMAGES):
                self.file_manager_open(icon_id, label_id, file_label_id, image_id)
            else:
                self.request_media_images_permission()
        else:
            # For non-Android platforms, directly open the file manager
            self.file_manager_open(icon_id, label_id, file_label_id, image_id)

    def file_manager_open(self, icon_id, label_id, file_label_id, image_id):
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=lambda path: self.select_path1(path, icon_id, label_id, file_label_id, image_id),
        )
        if platform == 'android':
            primary_external_storage = "/storage/emulated/0"
            self.file_manager.show(primary_external_storage)
        else:
            # For other platforms, show the file manager from the root directory
            self.file_manager.show('/')

    def select_path1(self, path, icon_id, label_id, file_label_id, image_id):
        self.ids[image_id].source = path  # Set the source of the Image widget
        self.file_manager.close()

    def exit_manager(self, *args):
        self.file_manager.close()

    def request_media_images_permission(self):
        request_permissions([Permission.READ_MEDIA_IMAGES], self.permission_callback)

    def permission_callback(self, permissions, grants):
        if all(grants.values()):
            # Permission granted, open the file manager
            self.file_manager_open()
        else:
            # Permission denied, show a modal view
            self.show_permission_denied()

    def show_permission_denied(self):
        view = ModalView()
        view.add_widget(Button(
            text='Permission NOT granted.\n\n' +
                 'Tap to quit app.\n\n\n' +
                 'If you selected "Don\'t Allow",\n' +
                 'enable permission with App Settings.',
            on_press=self.bye)
        )
        view.open()

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'DashboardScreen'

    def on_back_button_press(self):
        self.manager.current = 'DashboardScreen'


class LoansDetails(Screen):
    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'DashboardScreen'

    def go_to_foreclose(self):
        modal_view = ModalView(size_hint=(None, None), size=(100, 100), background_color=[0, 0, 0, 0])
        spinner = MDSpinner()
        modal_view.add_widget(spinner)
        modal_view.open()

        # Perform the actual action (e.g., fetching loan requests)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(lambda dt: self.perform_foreclose_action(modal_view), 2)

    def perform_foreclose_action(self, modal_view):
        # Close the modal view after performing the action
        modal_view.dismiss()
        # Get the existing ScreenManager
        sm = self.manager

        # Create a new instance of the LoginScreen
        login_screen = Foreclosure(name='Foreclosure')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(login_screen)

        # Switch to the LoginScreen
        sm.current = 'Foreclosure'


class Foreclosure(Screen):
    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'LoansDetails'

    def go_to_foreclose_details(self):
        modal_view = ModalView(size_hint=(None, None), size=(100, 100), background_color=[0, 0, 0, 0])
        spinner = MDSpinner()
        modal_view.add_widget(spinner)
        modal_view.open()

        # Perform the actual action (e.g., fetching loan requests)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(lambda dt: self.perform_foreclose_details_action(modal_view), 2)

    def perform_foreclose_details_action(self, modal_view):
        # Close the modal view after performing the action
        modal_view.dismiss()
        # Get the existing ScreenManager
        sm = self.manager

        # Create a new instance of the LoginScreen
        login_screen = ForecloseDetails(name='ForecloseDetails')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(login_screen)

        # Switch to the LoginScreen
        sm.current = 'ForecloseDetails'


class ForecloseDetails(Screen):
    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'Foreclosure'


class MyScreenManager(ScreenManager):
    pass
