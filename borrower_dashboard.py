from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen

user_helpers = """
<DashboardScreen>:
    MDFloatLayout:
        md_bg_color:1,1,1,1
        size_hint: 1, 1 
        
        MDTopAppBar:
            md_bg_color:1,1,1,1
            specific_text_color:1/255, 26/255, 51/255, 1
            elevation: 2
            left_action_items: [['menu', lambda x: root.profile()]]
            right_action_items: [['logout', lambda x: root.logout()]]
            pos_hint: {'center_x': 0.5, 'center_y': 0.96}
        Image:
            source:"C:\\P2P-Lending-Mobile-Application\\LOGO.png"
            pos_hint: {'center_x': 0.5, 'center_y': 0.96555}        
            md_bg_color:0,0,0,1
            size_hint: None,None 
            height: dp(64)
            width: dp(64)
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
                
                BoxLayout:
                    orientation: 'horizontal'
                    spacing:dp(10)
                    MDLabel:
                        text: "My Commitments"
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
                        text: "Opening Balance"
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
                        text: "My Returns"
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
                        text: "View Loan Requests"
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
               
                size_hint_y: None
                height: dp(60)
                size_hint_x: None
                width: dp(110)
                
                BoxLayout:
                    orientation: 'horizontal'
                    spacing:dp(10)
                    MDLabel:
                        text: "View Profile "
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
                padding: 35
                spacing: 20
                size_hint_y: None
                height: self.minimum_height



                CustomIconButton:
                    id: selected_image_button
                    on_release: app.file_manager_open()
                    selected_image_source: "path/to/your/default/image.jpg"
                    size_hint: None, None
                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_x: None
                    height: dp(40) 
                    padding:70   
                    Label:
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
                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_x: None
                    height: dp(40) 
                    padding:60   
                    Label:
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

                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_x: None
                    height: dp(40) 
                    padding:70   
                    Label:
                        text: ' Date Of Birth '
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
                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_x: None
                    height: dp(40) 
                    padding:20   
                    Label:
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

                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_x: None
                    height: dp(40) 
                    padding:80   
                    Label:
                        text: ' Mobile number '
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

                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_x: None
                    height: dp(40) 
                    padding:80   
                    Label:
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
                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_x: None
                    height: dp(40) 
                    padding:60   
                    Label:
                        text: ' Pan Number'
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
                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_x: None
                    height: dp(40) 
                    padding:5   
                    Label:
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

                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_x: None
                    height: dp(40) 
                    padding:80   
                    Label:
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

                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_x: None
                    height: dp(40) 
                    padding:80   
                    Label:
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

                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_x: None
                    height: dp(40) 
                    padding:120   
                    Label:
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

                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_x: None
                    height: dp(40) 
                    padding:130   
                    Label:
                        text: ' Spouse Company Address'
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

                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_x: None
                    height: dp(40) 
                    padding:100   
                    Label:
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

                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_x: None
                    height: dp(40) 
                    padding:40   
                    Label:
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

                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_x: None
                    height: dp(40) 
                    padding:130   
                    Label:
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

                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_x: None
                    height: dp(40) 
                    padding:80   
                    Label:
                        text: ' Address Type '
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
                        id: text_input22
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"

                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_x: None
                    height: dp(40) 
                    padding:90   
                    Label:
                        text: ' House Landmark '
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
                        id: text_input24
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"

                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_x: None
                    height: dp(40) 
                    padding:50   
                    Label:
                        text: ' House No '
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
                        id: text_input25
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"

                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_x: None
                    height: dp(40) 
                    padding:50   
                    Label:
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

                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_x: None
                    height: dp(40) 
                    padding:70   
                    Label:
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

                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_x: None
                    height: dp(40) 
                    padding:1
                    Label:
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

                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_x: None
                    height: dp(40) 
                    padding:70   
                    Label:
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
                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_x: None
                    height: dp(40) 
                    padding:80   
                    Label:
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

                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_x: None
                    height: dp(40) 
                    padding:90   
                    Label:
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

                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_x: None
                    height: dp(40) 
                    padding:90   
                    Label:
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

                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_x: None
                    height: dp(40) 
                    padding:70   
                    Label:
                        text: ' Business No '
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

                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_x: None
                    height: dp(40) 
                    padding:100   
                    Label:
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

                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_x: None
                    height: dp(40) 
                    padding:90   
                    Label:
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

                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_x: None
                    height: dp(40) 
                    padding:75   
                    Label:
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

                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_x: None
                    height: dp(40) 
                    padding:75   
                    Label:
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

                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_x: None
                    height: dp(40) 
                    padding:80   
                    Label:
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

                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_x: None
                    height: dp(40) 
                    padding:70   
                    Label:
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

                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_x: None
                    height: dp(40) 
                    padding:90   
                    Label:
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

                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_x: None
                    height: dp(40) 
                    padding:70   
                    Label:
                        text: ' Branch Name '
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
                        id: text_input42
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"

                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_x: None
                    height: dp(40) 
                    padding:60   
                    Label:
                        text: ' IFSC Code '
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

                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_x: None
                    height: dp(40) 
                    padding:65   
                    Label:
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

                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_x: None
                    height: dp(40) 
                    padding:55   
                    Label:
                        text: ' Net Bank '
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
                        id: text_input46
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"

                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_x: None
                    height: dp(40) 
                    padding:70   
                    Label:
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

                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_x: None
                    height: dp(40) 
                    padding:60   
                    Label:
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

                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_x: None
                    height: dp(40) 
                    padding:70   
                    Label:
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


                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_x: None
                    height: dp(40) 
                    padding:60   
                    Label:
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

                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_x: None
                    height: dp(40) 
                    padding:70   
                    Label:
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

                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_x: None
                    height: dp(40) 
                    padding:50   
                    Label:
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

                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_x: None
                    height: dp(40) 
                    padding:88   
                    Label:
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

<CustomIconButton@MDRectangleFlatButton>:
    selected_image_source: ""
    size_hint: None, None
    size: dp(100), dp(100)
    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    canvas.before:
        Color:
            rgba: 174/255, 214/255, 241/255, 1
        Ellipse:
            size: self.size
            pos: self.pos 
    MDIconButton:
        icon: 'camera-plus'
        on_release: app.file_manager_open()




"""


class DashboardScreen(Screen):
    def open_balance(self):
        self.manager.current = 'new_loan_request'

    def app_tracker(self):
        self.manager.current = 'borrower_application_tracker'

    def logout(self):
        self.manager.current = 'MainScreen'

    def profile(self):
        self.manager.current = 'ProfileScreen'


class ProfileScreen(Screen):

    def on_back_button_press(self):
        self.manager.current = 'borrower_dashboard'