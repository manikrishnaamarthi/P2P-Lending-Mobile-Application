import anvil
from kivy.core.window import Window
from kivy.properties import ListProperty
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager, SlideTransition
from kivymd.uix.button import MDRectangleFlatButton, MDRaisedButton
from kivymd.uix.slider import MDSlider
from kivymd.uix.label import MDLabel
import sqlite3
from math import pow
from kivymd.uix.dialog import MDDialog, dialog

GROUP_CATEGORIES = {
    "Vehicle": ["2 wheeler", "3 wheeler", "4 wheeler"],
    "Personal": ["Home", "Electronics"],
    "k12": ["k12"],
    "Educational": ["Educational"],
}

user_helpers2 = """
<WindowManager>:
    NewloanScreen:
    NewloanScreen1:
    NewloanScreen2:



<NewloanScreen>:

    BoxLayout:
        id:new_loan_screen
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        elevation: 2
        padding: dp(20)
        spacing: dp(20)
        orientation: 'vertical'
        MDFloatLayout:
            MDIconButton:

                icon: 'arrow-left'
                on_release:root.go_back()
                pos_hint: {'center_x': 0.045, 'center_y': 0.90}
                theme_text_color: 'Custom'
                text_color: 0,0,0,1  # Set color to white


            Image:
                source:"LOGO.png"
                size_hint:None,None
                size:"100dp","100dp"
                pos_hint: {'center_x': 0.5, 'center_y': 0.89}
            MDLabel:

                text: "  Experience Hassle-Free Borrowing  " 
                font_size:dp(15)
                halign:"center"
                bold:True
                underline:True
                italic:True
                pos_hint: {'center_x': 0.5, 'center_y': 0.4}
        MDLabel:
            text:""


        MDGridLayout:
            cols: 2
            BoxLayout:
                orientation:"horizontal"


                pos_hint: {'center_x':0.5, 'center_y':0.5}

                padding: dp(25)
                spacing: dp(20)

                MDLabel:
                    text: "Credit Limit" 
                    color:0.031, 0.463, 0.91, 1
                    bold:True
                    font_size:dp(23)
                MDLabel:
                    id: credit_limit        
                    text: "" 
                    font_size:dp(20)



        MDGridLayout:
            cols: 2
            BoxLayout:
                orientation:"horizontal"


                pos_hint: {'center_x':0.5, 'center_y':0.5}

                padding: dp(25)
                spacing: dp(20)


                MDLabel:
                    font_size:dp(16)

                    text: "Product Group"
                    bold: True

                Spinner:
                    id: group_id1
                    text: "Select Group"
                    values: ["Select Group","Vehicle", "Personal", "k12", "Educational"]
                    width: dp(200)
                    multiline: False
                    size_hint:None,None
                    pos_hint: {'center_x':0.5, 'center_y':0.5}
                    size:"180dp","45dp"
                    background_color: 1, 1 ,1, 0 
                    color:0,0,0,1
                    canvas.before:
                        Color:
                            rgba: 0, 0, 0, 1  
                        Line:
                            width: 0.7
                            rounded_rectangle: (self.x, self.y, self.width, self.height, 15)
                    # Call the update method
                    on_text: root.update_group_categories(self.text)  # Call the update method
        MDGridLayout:
            cols: 2
            BoxLayout:
                orientation:"horizontal"


                pos_hint: {'center_x':0.5, 'center_y':0.5}

                padding: dp(25)
                spacing: dp(20)


                MDLabel:
                    font_size:dp(16)
                    text: "Product Categories"
                    bold: True

                Spinner:
                    id: group_id2
                    text: "Select Categories"
                    width: dp(200)
                    multiline: False
                    pos_hint: {'center_x':0.5, 'center_y':0.5}
                    size_hint:None,None
                    size:"180dp","45dp"
                    background_color: 1, 1 ,1, 0 
                    color: 0, 0, 0, 1
                    canvas.before:
                        Color:
                            rgba: 0, 0, 0, 1  
                        Line:
                            width: 0.7
                            rounded_rectangle: (self.x, self.y, self.width, self.height, 15)
                    values: root.group_categories
        MDGridLayout:
            cols: 2
            BoxLayout:
                orientation:"horizontal"


                pos_hint: {'center_x':0.5, 'center_y':0.5}

                padding: dp(25)
                spacing: dp(20)


                MDLabel:
                    font_size:dp(16)
                    text: "Product Name"
                    bold: True
                MDTextField:
                    id:product_name
                    hint_text: "Product Name"
                    width: dp(250)
                    multiline: False
                    pos_hint: {'center_x':0.5, 'center_y':0.5}
                    size_hint: None, None
                    size: "180dp", "45dp"
                    background_color: 1, 1, 1, 0 
                    color: 0, 0, 0, 1
                    line_color_normal: 0, 0, 0, 1  # Set the line color to black
                    color: 0, 0, 0, 1
        MDLabel:
            text: " "             

        MDFloatLayout:

            MDRaisedButton:
                text: "Next"
                md_bg_color: 0.031, 0.463, 0.91, 1
                on_release: root.go_to_newloan_screen1()
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint:0.4, None  
                font_name:"Roboto-Bold"
                font_size:dp(15)

        MDLabel:
            text: " "  


<NewloanScreen1>:
    BoxLayout:
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        elevation: 2
        padding: dp(20)
        spacing: dp(20)
        orientation: 'vertical'
        radius: [10,]

        MDFloatLayout:
            MDIconButton:

                icon: 'arrow-left'
                on_release:root.go_back()
                pos_hint: {'center_x': 0, 'center_y': 0.90}
                theme_text_color: 'Custom'
                text_color: 0,0,0,1  # Set color to white


            Image:
                source:"LOGO.png"
                size_hint:None,None
                size:"75dp","75dp"
                pos_hint: {'center_x': 0.2, 'center_y': 0.92}
        MDLabel:
            text:""






        MDGridLayout:
            cols: 2
            BoxLayout:
                orientation:"horizontal"


                pos_hint: {'center_x':0.5, 'center_y':0.5}

                padding: dp(25)
                spacing: dp(20)


                MDLabel:
                    text: "Loan Amount"
                    bold:True
                    font_size:dp(16)



                MDTextField:
                    id: text_input1
                    width: dp(250)
                    multiline: False
                    hint_text: "Enter amount"
                    size_hint: None, None
                    size: "180dp", "45dp"
                    on_text: root.validate_amount(text_input1,self.text)
                    background_color: 1, 1, 1, 0 
                    color: 0, 0, 0, 1
                    line_color_normal: 0, 0, 0, 1  # Set the line color to black
                    color: 0, 0, 0, 1
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    helper_text: ""
                    helper_text_mode: "on_error"








        MDGridLayout:
            cols: 2
            BoxLayout:
                orientation:"horizontal"


                pos_hint: {'center_x':0.5, 'center_y':0.5}

                padding: dp(25)
                spacing: dp(20)

                MDLabel:
                    text: "Loan Period (Months)"
                    font_size:dp(16)
                    bold:True



                MDTextField:
                    id: text_input2
                    size_hint_x: 0.91
                    multiline: False
                    hint_text: "Enter loan period"
                    on_text: root.validate_tenure(text_input2,self.text)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    helper_text: ""
                    helper_text_mode: "on_error"
                    size_hint: None, None
                    size: "180dp", "45dp"
                    background_color: 1, 1, 1, 0 
                    color: 0, 0, 0, 1
                    line_color_normal: 0, 0, 0, 1  # Set the line color to black
                    color: 0, 0, 0, 1
        MDGridLayout:
            cols: 2
            BoxLayout:
                orientation:"horizontal"


                pos_hint: {'center_x':0.5, 'center_y':0.5}

                padding: dp(25)
                spacing: dp(20)


                MDLabel:
                    text: "EMI Type"
                    bold: True
                    font_size:dp(16)


                Spinner:
                    id: group_id3
                    text: "Select EMI Type"
                    values: ["One-time", "Monthly", "Three months", "Six months"]
                    width: dp(150)
                    multiline: False
                    size_hint:None,None
                    pos_hint: {'center_x':0.5, 'center_y':0.5}
                    size:"180dp","45dp"
                    background_color:1,1,1,0
                    color:0,0,0,1
                    canvas.before:
                        Color:
                            rgba: 0,0,0,1
                        Line:
                            width: 0.7
                            rounded_rectangle: (self.x, self.y, self.width, self.height, 15)



        MDLabel:
            id: max_tenure 
            color:1,1,1,1      
            text: "" 
            font_size:dp(1)

        MDFloatLayout:


            MDRaisedButton:
                text: "Next"
                md_bg_color: 0.031, 0.463, 0.91, 1
                on_release:  root.go_to_newloan_screen2()
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint:0.4, None  
                font_name:"Roboto-Bold"
                font_size:dp(15)
        MDLabel:
            text: " "
<NewloanScreen2>:



    BoxLayout:
        pos_hint: {'center_x':0.5, 'center_y':0.5}

        padding: dp(20)
        spacing: dp(20)
        orientation: 'vertical'
        MDFloatLayout:
            Image:
                source:"LOGO.png"
                size_hint:None,None
                size:"75dp","75dp"
                pos_hint: {'center_x': 0.5, 'center_y': 0.90}

        MDGridLayout:
            cols: 1




            MDLabel:
                text: "Loan Summary"
                halign: "center"
                font_size:dp(20)
                bold: True
                underline:"True"


        MDGridLayout:
            cols: 2
            spacing:dp(30)
            padding:dp(50)


            MDLabel:
                text: "Loan Amount"
                bold:True




            MDLabel:
                id: loan_amount
                text: ""
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                halign:"right"

        MDGridLayout:
            cols: 2
            spacing:dp(30)
            padding:dp(50)

            MDLabel:
                text: "ROI"
                bold:True





            MDLabel:
                id: roi
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                text: " "
                halign:"right"
        MDGridLayout:
            cols: 2
            spacing:dp(30)
            padding:dp(50)

            MDLabel:
                text: "Processing Fee "
                bold:True




            MDLabel:
                id: processing_fee
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                text: ""
                halign:"right"

        MDGridLayout:
            cols: 2
            spacing:dp(30)
            padding:dp(50)

            MDLabel:
                text: "Monthly EMI"
                bold:True




            MDLabel:
                id: monthly_emi
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                text: ""
                halign:"right"
        MDGridLayout:
            cols: 2
            spacing:dp(30)
            padding:dp(50)

            MDLabel:
                text: "Tenure"
                bold:True




            MDLabel:
                id:tenure
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                text: ""
                halign:"right"


        MDGridLayout:
            cols: 2
            spacing:dp(30)
            padding:dp(50)

            MDLabel:
                text: "Total Repayment Amount"
                bold:True





            MDLabel:
                id: total
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                text: " "
                halign:"right"

        MDLabel:
            text: " "
        MDLabel:
            text: " "


        MDFloatLayout:
            GridLayout:
                cols: 2
                spacing:dp(20)
                padding:dp(20)
                pos_hint: {'center_x': 0.5, 'center_y': 1}
                size_hint: 1, None
                height: "50dp"
                MDRaisedButton:
                    text: "Back"
                    on_release: app.root.current = "NewloanScreen1"
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    theme_text_color: 'Custom'
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"
                MDRaisedButton:
                    text: "Send request"
                    on_release: root.send_request()


                    md_bg_color: 0.031, 0.463, 0.91, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"

        MDLabel:
            text: " "

"""


class NewloanScreen(Screen):
    group_categories = ListProperty([])
    selected_group = ""
    selected_category = ""

    Builder.load_string(user_helpers2)

    def update_group_categories(self, selected_group):
        # Update the group_categories property based on the selected group
        self.ids.group_id2.text = "Select Categories"

        # Assuming GROUP_CATEGORIES is defined somewhere in your code
        self.group_categories = GROUP_CATEGORIES.get(selected_group, [])

    def on_pre_enter(self, *args):
        Window.bind(on_keyboard=self.on_back_button)

        # Specify the customer_id for which you want to fetch the credit_limit
        customer_id = "1000"

        try:
            # Call the Anvil server function to get the latest credit limit for the specified customer_id
            credit_limit = anvil.server.call('get_credit_limit', customer_id)

            # Update the credit_limit MDLabel with the fetched data
            self.ids.credit_limit.text = str(credit_limit)
        except anvil._server.AnvilWrappedError as e:
            print(f"Anvil error: {e}")

    def reset_fields(self):
        self.ids.group_id1.text = "Select Group"
        self.ids.group_id2.text = "Select Categories"
        self.ids.product_name.text = ""

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

    def current(self):
        self.manager.current = 'DashboardScreen'

    def go_to_newloan_screen1(self):
        selected_group = self.ids.group_id1.text
        selected_category = self.ids.group_id2.text
        self.selected_category = selected_category
        self.selected_group = selected_group
        # Get the existing ScreenManager
        product_name = self.ids.product_name.text

        sm = self.manager

        # Create a new instance of the LoginScreen
        login_screen = NewloanScreen1(name='NewloanScreen1')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(login_screen)

        # Switch to the LoginScreen
        sm.current = 'NewloanScreen1'
        print(self.selected_category)
        print(product_name)


class NewloanScreen1(Screen):
    selected_category = ""

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)
        self.root_screen = self.manager.get_screen('NewloanScreen')
        selected_category = self.root_screen.ids.group_id2.text

        try:
            # Call the Anvil server function to get the latest credit limit for the specified customer_id
            max_tenure = anvil.server.call('get_max_tenure', selected_category)

            # Update the credit_limit MDLabel with the fetched data
            self.ids.max_tenure.text = str(max_tenure)
        except anvil._server.AnvilWrappedError as e:
            print(f"Anvil error: {e}")

    def validate_amount(self, text_input, text):
        try:
            if not text:
                text_input.helper_text = ""
                text_input.error = False
                return

            amount = float(text)
            text_input.helper_text = ""

            if amount > float(self.root_screen.ids.credit_limit.text):
                text_input.helper_text = f"Amount exceeds credit limit ({self.root_screen.ids.credit_limit.text})"
                text_input.error = True
            else:
                text_input.error = False

        except ValueError:
            text_input.helper_text = " Please enter a valid number "
            text_input.error = True

        def reset_helper_text(instance_textfield, value):
            instance_textfield.helper_text = ""
            instance_textfield.error = False

        text_input.bind(on_focus=reset_helper_text)

    def reset_fields(self):
        self.ids.text_input1.text = ""
        self.ids.text_input2.text = ""
        self.ids.group_id3.text = "Select EMI Type"

    def validate_tenure(self, text_input, text):
        try:
            if not text:
                text_input.helper_text = ""
                text_input.error = False
                return

            tenure = float(text)
            text_input.helper_text = ""

            if tenure > float(self.ids.max_tenure.text):
                text_input.helper_text = f"maximum tenure limit: ({self.ids.max_tenure.text})"
                text_input.error = True
            else:
                text_input.error = False

        except ValueError:
            text_input.helper_text = " Please enter a valid number "
            text_input.error = True

        def reset_helper_text(instance_textfield, value):
            instance_textfield.helper_text = ""
            instance_textfield.error = False

        text_input.bind(on_focus=reset_helper_text)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'NewloanScreen'

    def current(self):
        self.manager.current = 'NewloanScreen'

    def go_to_newloan_screen2(self):
        loan_amount = self.ids.text_input1.text
        loan_tenure = self.ids.text_input2.text
        # Get the existing ScreenManager
        sm = self.manager
        self.selected_category = self.root_screen.ids.group_id2.text
        # Create a new instance of the LoginScreen
        login_screen = NewloanScreen2(name='NewloanScreen2')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(login_screen)

        # Switch to the LoginScreen
        sm.current = 'NewloanScreen2'


class NewloanScreen2(Screen):
    loan_amount = ""

    loan_tenure = ""

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)
        self.root_screen = self.manager.get_screen('NewloanScreen1')
        loan_amount = float(self.root_screen.ids.text_input1.text)
        self.loan_tenure = float(self.root_screen.ids.text_input2.text)
        self.ids.loan_amount.text = str(loan_amount)
        selected_category = self.root_screen.selected_category
        self.ids.tenure.text = str(self.loan_tenure)

        try:
            details = anvil.server.call('get_details', selected_category)
            roi = details.get('roi', '')
            processing_fee = details.get('processing_fee', '')
            self.ids.roi.text = str(roi)
            self.ids.processing_fee.text = str(processing_fee)

            # Call the Anvil server function to get details for the specified category
            selected_category = self.root_screen.selected_category
            loan_amount = self.root_screen.ids.text_input1.text
            loan_tenure = self.root_screen.ids.text_input2.text

            emi = anvil.server.call('calculate_emi', selected_category, loan_amount, loan_tenure)
            total_repayment = anvil.server.call('calculate_total_repayment', selected_category, loan_amount,
                                                loan_tenure)
            # Update the MDLabels with the calculated values
            self.ids.monthly_emi.text = f"{float(emi):.2f}"
            self.ids.total.text = f"{total_repayment:.2f}"

        except anvil._server.AnvilWrappedError as e:
            print(f"Anvil error: {e}")

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'NewloanScreen1'

    def current(self):
        self.manager.current = 'NewloanScreen1'

    def generate_loan_id(self):
        # Call the Anvil server function to generate the loan ID
        loan_id = anvil.server.call('generate_loan_id')
        return loan_id

    def send_request(self):
        loan_amount = float(self.ids.loan_amount.text)
        loan_tenure = float(self.root_screen.ids.text_input2.text)
        selected_category = self.root_screen.selected_category
        roi = float(self.ids.roi.text)
        total_repayment = float(self.ids.total.text)

        # Call the Anvil server function to add loan data
        try:
            loan_id = anvil.server.call(
                'add_loan_data',
                loan_amount,
                loan_tenure,
                roi,
                total_repayment
            )
            self.show_success_dialog(f"Loan details added successfully! Loan ID: {loan_id}")
        except anvil._server.AnvilWrappedError as e:
            # Show error notification
            print(f"Anvil error: {e}")

    def show_success_dialog(self, text):
        dialog = MDDialog(
            text=text,
            size_hint=(0.8, 0.3),
            buttons=[
                MDRaisedButton(
                    text="OK",
                    on_release=lambda *args: self.open_dashboard_screen(dialog),
                    theme_text_color="Custom",
                    text_color=(1, 1, 1, 1),  # Black color
                )
            ]
        )
        dialog.open()

    def open_dashboard_screen(self, dialog):
        self.manager.get_screen('NewloanScreen').reset_fields()
        self.manager.get_screen('NewloanScreen1').reset_fields()

        dialog.dismiss()
        # Implement the logic to switch to the DashboardScreen
        # For example:
        self.manager.current = 'DashboardScreen'


class MyScreenManager(ScreenManager):
    pass