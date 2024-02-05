

import anvil.server
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, SlideTransition,ScreenManager
import sqlite3
import anvil.server
from kivy.uix.screenmanager import Screen, SlideTransition
from kivymd.app import MDApp

anvil.server.connect('server_BQ6Z7GHPS3ZH5TPKQJBHTYJI-ZVMP6VAENIF2GORT')

lender_view_extension = """
<WindowManager>:
    NewExtension:
    NewLoansE:
    ApprovedLoansE:
    RejectedLoansE:
    UnderProcessLoansE:
    ViewProfileE:
    
<NewExtension>
    BoxLayout:
        orientation: 'vertical'
        size_hint: 1, 1 
        pos_hint: {'center_x':0.5, 'center_y':0.5}

        MDTopAppBar:
            title: "View Extension Request"
            elevation: 2
            left_action_items: [['arrow-left', lambda x: root.on_back_button_press()]]

        MDGridLayout:
            cols: 2
            padding: dp(15)
            spacing: dp(5)
            pos_hint: {'center_x': .5, 'center_y': .5}

            Button:
                text: "New Loans Extension"
                text_color: 0, 0, 0, 1
                background_color: 0.529, 0.807, 0.922, 0
                on_release: app.root.current = 'NewLoansE'
                color: 0, 0, 0, 1
                bold: True
                canvas.before:
                    Color:
                        rgba:0.529, 0.807, 0.922, 1 
                    Line:
                        width: 0.9  
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)


            Button:
                text: "Approved Loans"
                background_color: 0.529, 0.807, 0.922, 0 
                color: 0, 0, 0, 1
                on_release: app.root.current = 'ApprovedLoansE'
                bold: True
                canvas.before:
                    Color:
                        rgba: 0.529, 0.807, 0.922, 1 
                    Line:
                        width: 0.9  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)
            Button:
                text: "View All Loans"
                background_color: 0.529, 0.807, 0.922, 0
                on_release: app.root.current = 'ViewAllLoansE'
                color: 0, 0, 0, 1
                bold: True
                canvas.before:
                    Color:
                        rgba: 0.529, 0.807, 0.922, 1 
                    Line:
                        width: 
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)
            Button:
                text: "Rejected Loans"
                background_color: 0.529, 0.807, 0.922, 0
                on_release: app.root.current = 'RejectedLoansE'
                color: 0, 0, 0, 1
                bold: True
                canvas.before:
                    Color:
                        rgba: 0.529, 0.807, 0.922, 1 
                    Line:
                        width: 0.9  
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)



            Button:
                text: "UnderProcess Loans"
                text_color: 0, 0, 0, 1
                on_release: app.root.current = 'UnderProcessLoansE'
                background_color: 0.529, 0.807, 0.922, 0
                color: 0, 0, 0, 1
                bold: True
                canvas.before:
                    Color:
                        rgba:0.529, 0.807, 0.922, 1 
                    Line:
                        width: 0.9  
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

<NewLoansE>
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "New Loans "
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
                                rgba: 0, 0, 1, 1  # Blue color for the box
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
                                text: 'Borrower Name'
                                size_hint_y: None
                                height: dp(50)  
                                bold: True

                            MDLabel:
                                text: 'Loan Amount'
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
                                    width: dp(0.6)  # Set the width of the line to make it bold
                                    points: self.x, self.y, self.x + self.width, self.y


"""

a = 10

for i in range(a):
    id_label = f"label_{i}"
    amount = f"amount_{i}"
    status = f"status_{i}"
    icon = f"icon_{i}"
    lender_view_extension += f'''
                        GridLayout:
                            cols: 4
                            spacing: dp(20)
                            MDLabel:
                                id: {id_label}
                                text: ''
                                size_hint_y: None
                                height: dp(50)  # Adjust the height as needed

                            MDLabel:
                                id: {amount}
                                text: ''
                                size_hint_y: None
                                height: dp(50)  # Adjust the height as needed


                            MDLabel:
                                id: {status}
                                text: ''
                                size_hint_y: None
                                height: dp(50)  # Adjust the height as needed


                            MDIconButton:
                                id: {icon}
                                icon: 'arrow-right-thick'
                                size_hint_y: None
                                height: dp(50)  # Adjust the height as needed
                                on_release: root.icon_button_clicked({id_label}.text)
                                opacity: 0

    '''

lender_view_extension += '''
<ApprovedLoansE>
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
                                text: 'Borroer Name'
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

a = 8

for i in range(a):
    id_label = f"label_{i}"
    amount = f"amount_{i}"
    status = f"status_{i}"
    icon = f"icon_{i}"
    lender_view_extension += f'''
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
                                on_release: app.root.current = 'ViewProfileE'
                                opacity: 0
'''

lender_view_extension += '''
<ViewAllLoansE>
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
                                text: 'Borrower Name'
                                size_hint_y: None
                                height: dp(50)  
                                bold: True

                            MDLabel:
                                text: 'Loan Amount'
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
    lender_view_extension += f'''
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
                                on_release: app.root.current = 'ViewProfileE'
                                opacity: 0
'''
lender_view_extension += '''
<RejectedLoansE>
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
                                text: 'Borrower Name'
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

a = 8

for i in range(a):
    id_label = f"label_{i}"
    amount = f"amount_{i}"
    status = f"status_{i}"
    icon = f"icon_{i}"
    lender_view_extension += f'''
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
                                on_release: app.root.current = 'ViewProfileE'
                                opacity: 0
'''
lender_view_extension += '''
<UnderProcessLoansE>
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "Under Process Loans"
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

a = 8

for i in range(a):
    id_label = f"label_{i}"
    amount = f"amount_{i}"
    status = f"status_{i}"
    icon = f"icon_{i}"
    lender_view_extension += f'''
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
                                on_release: app.root.current = 'ViewProfileE'
                                opacity: 0

'''
lender_view_extension += f'''
<ViewProfileE>
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "All Loans"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.on_back_button_press()]]
        ScrollView:

            MDBoxLayout:
                orientation: 'vertical'
                size_hint_y: None
                height: self.minimum_height
                BoxLayout:
                    id: box1
                    orientation: 'vertical'
                    size_hint_y: None
                    MDLabel:
                        text: "Loan Extension details"
                        halign: "center"
                        bold: True
                MDBoxLayout:
                    orientation: 'vertical'
                    size_hint_y: None
                    height: self.minimum_height
                    padding: dp(20)

                    BoxLayout:
                        id: box1
                        orientation: 'vertical'
                        size_hint_y: None
                        height: dp(900)

                        padding: [10, 0,0,0]
                        canvas.before:
                            Color:
                                rgba: 0, 0, 0, 1 
                            Line:
                                rectangle: self.pos[0], self.pos[1], self.size[0], self.size[1]

                        GridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)
                            MDLabel:
                                text: "Borrower Name" 
                                size_hint_y:None
                                height:dp(50)
                            MDLabel:
                                id: user1
                                text: "" 
                            MDLabel:
                                text: "Loan Amount" 
                                size_hint_y:None
                                height:dp(50)
                            MDLabel:
                                id: name
                                text: "" 
                            MDLabel:
                                text: "Extension Fee(%)" 
                                size_hint_y:None
                                height:dp(50)
                            MDLabel:
                                id: beseem
                                text: "" 
                            MDLabel:
                                text: "Extension Amount" 
                                size_hint_y:None
                                height:dp(50)
                            MDLabel:
                                id: tenure
                                text: "" 
                            MDLabel:
                                text: "Total Extension Amount" 
                                size_hint_y:None
                                height:dp(50)
                            MDLabel:
                                id: rome
                                text: "" 
                            MDLabel:
                                text: "Remaining Amount" 
                                size_hint_y:None
                                height:dp(50)
                            MDLabel:
                                id: since
                                text: "" 
                            MDLabel:
                                text: "Reason For Extension" 
                                size_hint_y:None
                                height:dp(50)
                            MDLabel:
                                id: limit
                                text: "" 
                            MDLabel:
                                text: "New EMI" 
                                size_hint_y:None
                                height:dp(50)
                            MDLabel:
                                id: interest
                                text: "" 

                            MDRaisedButton:
                                text: "Reject"
                                md_bg_color: 194/255, 2/255, 21/255, 1
                                theme_text_color: 'Primary'
                                on_release: app.root.current = 'LoansDetails'
                                text_color: 0, 0, 0, 1
                                font_name: "Roboto-Bold.ttf"
                                size_hint: 1, None

                            MDRaisedButton:
                                text: "Accept"
                                md_bg_color: 194/255, 2/255, 21/255, 1
                                theme_text_color: 'Primary'
                                font_name: "Roboto-Bold.ttf"
                                text_color: 0, 0, 0, 1
                                size_hint: 1, None
'''
Builder.load_string(lender_view_extension)


class NewExtension(Screen):
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
        self.manager.current = 'borrower_dashboard'

    def on_back_button_press(self):
        self.manager.current = 'lender_dashboard'


class NewLoansE(Screen):
    def init(self, **kwargs):
        super().init(**kwargs)
        h = self.ids.box1.height

        for i in range(a + 1):
            h += 150
        self.ids.box1.height = h
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
    def on_back_button_press(self):
        self.manager.current = 'NewExtension'


class ApprovedLoansE(Screen):
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
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        data = self.get_table_data()
        customer_id = []
        loan_id = []
        loan_amount = []
        loan_status = []
        s = 0
        for i in data:
            s += 1
            customer_id.append(i['borrower_full_name'])
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

    def on_back_button_press(self):
        self.manager.current = 'NewExtension'

    def get_table_data(self):
        # Make a call to the Anvil server function
        # Replace 'YourAnvilFunction' with the actual name of your Anvil server function
        return anvil.server.call('get_extension_data')
class ViewAllLoansE(Screen):
    def init(self, **kwargs):
        super().init(**kwargs)
        h = self.ids.box1.height

        for i in range(a + 1):
            h += 150
        self.ids.box1.height = h
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
    def on_back_button_press(self):
        self.manager.current = 'NewExtension'
    def get_table_data(self):
        # Make a call to the Anvil server function
        # Replace 'YourAnvilFunction' with the actual name of your Anvil server function
        return anvil.server.call('get_extension_data')
class RejectedLoansE(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        data = self.get_table_data()
        customer_id = []
        loan_id = []
        loan_amount = []
        loan_status = []
        s = 0
        for i in data:
            s += 1
            customer_id.append(i['borrower_full_name'])
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
    def on_back_button_press(self):
        self.manager.current = 'NewExtension'
    def get_table_data(self):
        # Make a call to the Anvil server function
        # Replace 'YourAnvilFunction' with the actual name of your Anvil server function
        return anvil.server.call('get_extension_data')


class UnderProcessLoansE(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        data = self.get_table_data()
        customer_id = []
        loan_id = []
        loan_amount = []
        loan_status = []
        s = 0
        for i in data:
            s += 1
            customer_id.append(i['borrower_full_name'])
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
        return anvil.server.call('get_extension_data')

    def icon_button_clicked(self, value):
        self.manager.current = 'ViewProfileE'
        self.manager.get_screen('ViewProfileE').initialize_with_value(value)
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
    def on_back_button_press(self):
        self.manager.current = 'NewExtension'


class ViewProfileE(Screen):
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
    def on_back_button_press(self):
        self.manager.current = 'NewExtension'

class MyScreenManager(ScreenManager):
    pass