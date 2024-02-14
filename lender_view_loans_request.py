import anvil.server
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, SlideTransition, ScreenManager
import sqlite3
import anvil.server
from kivy.uix.screenmanager import Screen, SlideTransition
from kivymd.app import MDApp
from datetime import datetime, timedelta, timezone
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.snackbar import Snackbar

anvil.server.connect("server_ANJQTKQ62KGHGX2XHC43NVOG-6JH2LHL646DIRMSE")
view_loan_request = """
<WindowManager>:
    ViewLoansRequest:
    ViewLoansProfileScreen:
    ViewLoansProfileScreenLR:
    ViewLoansProfileScreenRL:

<ViewLoansRequest> 
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "View Loans Request"
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
                                height: dp(50)  # Adjust the height as needed
                                bold: True


                            MDLabel:
                                text: 'Loan Amount'
                                size_hint_y: None
                                height: dp(50)  # Adjust the height as needed
                                bold: True

                            MDLabel:
                                text: 'Loan Status'
                                size_hint_y: None
                                height: dp(50)  # Adjust the height as needed
                                bold: True
                            MDLabel:
                                text: ''
                                size_hint_y: None
                                height: dp(50)  # Adjust the height as needed
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

a = 50

for i in range(a):
    id_label = f"label_{i}"
    amount = f"amount_{i}"
    status = f"status_{i}"
    icon = f"icon_{i}"
    view_loan_request += f'''
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

view_loan_request += '''
<ViewLoansProfileScreen>
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
                        text: " Borrower Loan details"
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
                        height: dp(950)

                        padding: [10, 0,0,0]
                        canvas.before:
                            Color:
                                rgba: 0, 0, 0, 1  # Blue color for the box
                            Line:
                                rectangle: self.pos[0], self.pos[1], self.size[0], self.size[1]

                        GridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)
                            MDLabel:
                                text: "User ID" 
                                size_hint_y:None
                                height:dp(50)
                            MDLabel:
                                id: user1
                                text: "" 
                            MDLabel:
                                text: "Name" 
                                size_hint_y:None
                                height:dp(50)
                            MDLabel:
                                id: name
                                text: "" 
                            MDLabel:
                                text: "Beseem Score" 
                                size_hint_y:None
                                height:dp(50)
                            MDLabel:
                                id: beseem
                                text: "" 
                            MDLabel:
                                text: "Loan Tenure" 
                                size_hint_y:None
                                height:dp(50)
                            MDLabel:
                                id: tenure
                                text: "" 
                            MDLabel:
                                text: "Member Rome" 
                                size_hint_y:None
                                height:dp(50)
                            MDLabel:
                                id: rome
                                text: "" 
                            MDLabel:
                                text: "Member since" 
                                size_hint_y:None
                                height:dp(50)
                            MDLabel:
                                id: since
                                text: "" 
                            MDLabel:
                                text: "Credit Limit" 
                                size_hint_y:None
                                height:dp(50)
                            MDLabel:
                                id: limit
                                text: "" 
                            MDLabel:
                                text: "Interest Rate" 
                                size_hint_y:None
                                height:dp(50)
                            MDLabel:
                                id: interest
                                text: "" 
                            MDLabel:
                                text: "Loan Amount Applied" 
                                size_hint_y:None
                                height:dp(50)
                            MDLabel:
                                id: amount_applied
                                text: "" 
                            MDLabel:
                                text: "Loan ID" 
                                size_hint_y:None
                                height:dp(50)
                            MDLabel:
                                id: loan_id
                                text: "" 
                            MDLabel:
                                text: "Bank Details" 
                                size_hint_y:None
                                height:dp(50)
                            MDLabel:
                                id: bank_details
                                text: "" 
                            MDRaisedButton:
                                text: "Reject"
                                md_bg_color: 194/255, 2/255, 21/255, 1
                                theme_text_color: 'Primary'
                                on_release: root.rejected_click()
                                text_color: 0, 0, 0, 1
                                font_name: "Roboto-Bold.ttf"
                                size_hint: 1, None

                            MDRaisedButton:
                                text: "Accept"
                                md_bg_color: 5/255, 235/255, 77/255, 1
                                on_release: root.approved_click()
                                theme_text_color: 'Primary'
                                font_name: "Roboto-Bold.ttf"
                                text_color: 0, 0, 0, 1
                                size_hint: 1, None
<ViewLoansProfileScreenLR>
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
                        text: " Borrower Loan details"
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
                        height: dp(950)

                        padding: [10, 0,0,0]
                        canvas.before:
                            Color:
                                rgba: 0, 0, 0, 1  # Blue color for the box
                            Line:
                                rectangle: self.pos[0], self.pos[1], self.size[0], self.size[1]

                        GridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)
                            MDLabel:
                                text: "User ID" 
                                size_hint_y:None
                                height:dp(50)
                            MDLabel:
                                id: user1
                                text: "" 
                            MDLabel:
                                text: "Name" 
                                size_hint_y:None
                                height:dp(50)
                            MDLabel:
                                id: name
                                text: "" 
                            MDLabel:
                                text: "Beseem Score" 
                                size_hint_y:None
                                height:dp(50)
                            MDLabel:
                                id: beseem
                                text: "" 
                            MDLabel:
                                text: "Loan Tenure" 
                                size_hint_y:None
                                height:dp(50)
                            MDLabel:
                                id: tenure
                                text: "" 
                            MDLabel:
                                text: "Member Rome" 
                                size_hint_y:None
                                height:dp(50)
                            MDLabel:
                                id: rome
                                text: "" 
                            MDLabel:
                                text: "Member since" 
                                size_hint_y:None
                                height:dp(50)
                            MDLabel:
                                id: since
                                text: "" 
                            MDLabel:
                                text: "Credit Limit" 
                                size_hint_y:None
                                height:dp(50)
                            MDLabel:
                                id: limit
                                text: "" 
                            MDLabel:
                                text: "Interest Rate" 
                                size_hint_y:None
                                height:dp(50)
                            MDLabel:
                                id: interest
                                text: "" 
                            MDLabel:
                                text: "Loan Amount Applied" 
                                size_hint_y:None
                                height:dp(50)
                            MDLabel:
                                id: amount_applied
                                text: "" 
                            MDLabel:
                                text: "Loan ID" 
                                size_hint_y:None
                                height:dp(50)
                            MDLabel:
                                id: loan_id
                                text: "" 
                            MDLabel:
                                text: "Bank Details" 
                                size_hint_y:None
                                height:dp(50)
                            MDLabel:
                                id: bank_details
                                text: "" 
                            MDRaisedButton:
                                text: "Cancel"
                                md_bg_color: 194/255, 2/255, 21/255, 1
                                theme_text_color: 'Primary'
                                on_release: app.root.current = 'ViewLoansRequest'
                                text_color: 0, 0, 0, 1
                                font_name: "Roboto-Bold.ttf"
                                size_hint: 1, None

                            MDRaisedButton:
                                text: "Pay Now"
                                md_bg_color: 5/255, 235/255, 77/255, 1
                                theme_text_color: 'Primary'
                                font_name: "Roboto-Bold.ttf"
                                text_color: 0, 0, 0, 1
                                size_hint: 1, None
                                on_release: root.paynow()

<ViewLoansProfileScreenRL>
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
                        text: " Borrower Loan details"
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
                        height: dp(950)

                        padding: [10, 0,0,0]
                        canvas.before:
                            Color:
                                rgba: 0, 0, 0, 1  # Blue color for the box
                            Line:
                                rectangle: self.pos[0], self.pos[1], self.size[0], self.size[1]

                        GridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)
                            MDLabel:
                                text: "User ID" 
                                size_hint_y:None
                                height:dp(50)
                            MDLabel:
                                id: user1
                                text: "" 
                            MDLabel:
                                text: "Name" 
                                size_hint_y:None
                                height:dp(50)
                            MDLabel:
                                id: name
                                text: "" 
                            MDLabel:
                                text: "Beseem Score" 
                                size_hint_y:None
                                height:dp(50)
                            MDLabel:
                                id: beseem
                                text: "" 
                            MDLabel:
                                text: "Loan Tenure" 
                                size_hint_y:None
                                height:dp(50)
                            MDLabel:
                                id: tenure
                                text: "" 
                            MDLabel:
                                text: "Member Rome" 
                                size_hint_y:None
                                height:dp(50)
                            MDLabel:
                                id: rome
                                text: "" 
                            MDLabel:
                                text: "Member since" 
                                size_hint_y:None
                                height:dp(50)
                            MDLabel:
                                id: since
                                text: "" 
                            MDLabel:
                                text: "Credit Limit" 
                                size_hint_y:None
                                height:dp(50)
                            MDLabel:
                                id: limit
                                text: "" 
                            MDLabel:
                                text: "Interest Rate" 
                                size_hint_y:None
                                height:dp(50)
                            MDLabel:
                                id: interest
                                text: "" 
                            MDLabel:
                                text: "Loan Amount Applied" 
                                size_hint_y:None
                                height:dp(50)
                            MDLabel:
                                id: amount_applied
                                text: "" 
                            MDLabel:
                                text: "Loan ID" 
                                size_hint_y:None
                                height:dp(50)
                            MDLabel:
                                id: loan_id
                                text: "" 
                            MDLabel:
                                text: "Bank Details" 
                                size_hint_y:None
                                height:dp(50)
                            MDLabel:
                                id: bank_details
                                text: "" 

                        MDBoxLayout:
                            orientation: "vertical"
                            MDLabel:
                                text: "Your Loan request is Rejected"    
                                bold: True  
                                halign: "center"    
'''
Builder.load_string(view_loan_request)


class ViewLoansRequest(Screen):
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
            customer_id.append(i['borrower_customer_id'])
            loan_id.append(i['loan_id'])
            loan_amount.append(i['loan_amount'])
            loan_status.append(i['loan_updated_status'])

        c = -1
        index_list = []
        for i in range(s):
            c += 1
            if loan_status[c] == 'approved' or loan_status[c] == 'rejected' or loan_status[c] == 'under process':
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
        self.manager.current = 'LenderDashboard'

    def get_table_data(self):
        # Make a call to the Anvil server function
        # Replace 'YourAnvilFunction' with the actual name of your Anvil server function
        return anvil.server.call('get_table_data')

    def icon_button_clicked(self, value):
        data = self.get_table_data()  # Fetch data here
        loan_status = None
        for loan in data:
            if loan['loan_id'] == value:
                loan_status = loan['loan_updated_status']
                break

        if loan_status == 'approved':
            # Open the screen for approved loans

            sm = self.manager

            # Create a new instance of the LoginScreen
            approved = ViewLoansProfileScreenLR(name='ViewLoansProfileScreenLR')

            # Add the LoginScreen to the existing ScreenManager
            sm.add_widget(approved)

            # Switch to the LoginScreen
            sm.current = 'ViewLoansProfileScreenLR'
            self.manager.get_screen('ViewLoansProfileScreenLR').initialize_with_value(value, data)
        elif loan_status == 'under process':
            # Open the screen for pending loans
            sm = self.manager

            # Create a new instance of the LoginScreen
            under_process = ViewLoansProfileScreen(name='ViewLoansProfileScreen')

            # Add the LoginScreen to the existing ScreenManager
            sm.add_widget(under_process)

            # Switch to the LoginScreen
            sm.current = 'ViewLoansProfileScreen'
            self.manager.get_screen('ViewLoansProfileScreen').initialize_with_value(value, data)
        elif loan_status == 'rejected':
            # Open the screen for pending loans
            sm = self.manager

            # Create a new instance of the LoginScreen
            rejected = ViewLoansProfileScreenRL(name='ViewLoansProfileScreenRL')

            # Add the LoginScreen to the existing ScreenManager
            sm.add_widget(rejected)

            # Switch to the LoginScreen
            sm.current = 'ViewLoansProfileScreenRL'
            self.manager.get_screen('ViewLoansProfileScreenRL').initialize_with_value(value, data)
        else:
            # Handle other loan statuses or show an error message
            pass

    def on_pre_enter(self):
        # Bind the back button event to the on_back_button method
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        # Unbind the back button event when leaving the screen
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        # Handle the back button event
        if key == 27:  # 27 is the keycode for the hardware back button on Android
            self.go_back()
            return True  # Consume the event, preventing further handling
        return False  # Continue handling the event

    def go_back(self):
        # Navigate to the previous screen with a slide transition
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'LenderDashboard'


class ViewLoansProfileScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_back_button_press(self):
        self.manager.current = 'ViewLoansRequest'

    def initialize_with_value(self, value, data):
        customer_id = []
        loan_id = []
        tenure = []
        interest_rate = []
        loan_amount = []
        member_rom = []
        member_since = []
        credit_limit = []
        beseem_score = []
        name = []
        for i in data:
            customer_id.append(i['borrower_customer_id'])
            loan_id.append(i['loan_id'])
            tenure.append(i['tenure'])
            interest_rate.append(i['interest_rate'])
            loan_amount.append(i['loan_amount'])
            member_rom.append(i['member_rom'])
            member_since.append(i['member_since'])
            credit_limit.append(i['credit_limit'])
            beseem_score.append(i['beseem_score'])
            name.append(i['borrower_full_name'])

        if value in loan_id:
            index = loan_id.index(value)
            self.ids.loan_id.text = str(loan_id[index])
            self.ids.user1.text = str(customer_id[index])
            self.ids.interest.text = str(interest_rate[index])
            self.ids.tenure.text = str(tenure[index])
            self.ids.amount_applied.text = str(loan_amount[index])
            self.ids.rome.text = str(member_rom[index])
            self.ids.since.text = str(member_since[index])
            self.ids.limit.text = str(credit_limit[index])
            self.ids.beseem.text = str(beseem_score[index])
            self.ids.name.text = str(name[index])

    def on_pre_enter(self):
        # Bind the back button event to the on_back_button method
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        # Unbind the back button event when leaving the screen
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        # Handle the back button event
        if key == 27:  # 27 is the keycode for the hardware back button on Android
            self.go_back()
            return True  # Consume the event, preventing further handling
        return False  # Continue handling the event

    def approved_click(self):
        approved_date = datetime.now()
        data = self.get_table_data()
        loan_id = self.ids.loan_id.text
        print(loan_id)

        loan_idlist = []
        for i in data:
            loan_idlist.append(i['loan_id'])
        print(loan_idlist)
        if loan_id in loan_idlist:
            index = loan_idlist.index(loan_id)
            data[index]['loan_updated_status'] = 'approved'
            data[index]['lender_accepted_timestamp'] = approved_date
            self.manager.current = 'ViewLoansRequest'
            self.show_snackbar(f"This Loan ID {loan_id} is Approved")
            return
        else:
            pass

    def rejected_click(self):
        data = self.get_table_data()
        loan_id = self.ids.loan_id.text
        print(loan_id)

        loan_idlist = []
        for i in data:
            loan_idlist.append(i['loan_id'])
        print(loan_idlist)
        if loan_id in loan_idlist:
            index = loan_idlist.index(loan_id)
            data[index]['loan_updated_status'] = 'rejected'
            self.manager.current = 'ViewLoansRequest'
            self.show_snackbar(f"This Loan ID {loan_id} is Rejected")
            return
        else:
            pass

    def show_snackbar(self, text):
        Snackbar(text=text, pos_hint={'top': 1}, md_bg_color=[1, 0, 0, 1]).open()

    def get_table_data(self):
        # Make a call to the Anvil server function
        # Replace 'YourAnvilFunction' with the actual name of your Anvil server function
        return anvil.server.call('get_table_data')

    def go_back(self):
        # Navigate to the previous screen with a slide transition
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'ViewLoansRequest'


class ViewLoansProfileScreenLR(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def show_alert_dialog(self, alert_text):
        if not hasattr(self, 'dialog') or not self.dialog:
            self.dialog = MDDialog(
                text=alert_text,
                buttons=[
                    MDFlatButton(
                        text="OK", on_release=self.close_dialog
                    ),
                ],
            )

        self.dialog.text = alert_text
        self.dialog.open()

    # Click Cancel Button
    def close_dialog(self, obj):
        # Close alert box
        self.dialog.dismiss()

    def get_table_data(self):
        # Make a call to the Anvil server function
        # Replace 'YourAnvilFunction' with the actual name of your Anvil server function
        return anvil.server.call('get_table_data')

    def on_back_button_press(self):
        self.manager.current = 'ViewLoansRequest'

    def initialize_with_value(self, value, data):
        customer_id = []
        loan_id = []
        tenure = []
        interest_rate = []
        loan_amount = []
        member_rom = []
        member_since = []
        credit_limit = []
        beseem_score = []
        name = []
        for i in data:
            customer_id.append(i['borrower_customer_id'])
            loan_id.append(i['loan_id'])
            tenure.append(i['tenure'])
            interest_rate.append(i['interest_rate'])
            loan_amount.append(i['loan_amount'])
            member_rom.append(i['member_rom'])
            member_since.append(i['member_since'])
            credit_limit.append(i['credit_limit'])
            beseem_score.append(i['beseem_score'])
            name.append(i['borrower_full_name'])

        if value in loan_id:
            index = loan_id.index(value)
            self.ids.loan_id.text = str(loan_id[index])
            self.ids.user1.text = str(customer_id[index])
            self.ids.interest.text = str(interest_rate[index])
            self.ids.tenure.text = str(tenure[index])
            self.ids.amount_applied.text = str(loan_amount[index])
            self.ids.rome.text = str(member_rom[index])
            self.ids.since.text = str(member_since[index])
            self.ids.limit.text = str(credit_limit[index])
            self.ids.beseem.text = str(beseem_score[index])
            self.ids.name.text = str(name[index])

    def on_pre_enter(self):
        # Bind the back button event to the on_back_button method
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        # Unbind the back button event when leaving the screen
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        # Handle the back button event
        if key == 27:  # 27 is the keycode for the hardware back button on Android
            self.go_back()
            return True  # Consume the event, preventing further handling
        return False  # Continue handling the event

    def go_back(self):
        # Navigate to the previous screen with a slide transition
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'ViewLoansRequest'

    def show_snackbar(self, text):
        Snackbar(text=text, pos_hint={'top': 1}, md_bg_color=[1, 0, 0, 1]).open()

    def paynow(self):
        data = self.get_table_data()
        disbursed_time = datetime.now()
        paid_time = datetime.now()
        loan_id = self.ids.loan_id.text
        print(loan_id)
        loan_id_list = []
        disbursed = []
        credit_limit = []
        loan_amount = []
        for i in data:
            loan_id_list.append(i['loan_id'])
            disbursed.append(i['lender_accepted_timestamp'])
            credit_limit.append(i['credit_limit'])
            loan_amount.append(i['loan_amount'])

        if loan_id in loan_id_list:
            index = loan_id_list.index(loan_id)

        datetime1 = datetime.fromisoformat(str(disbursed_time)).replace(tzinfo=timezone.utc)
        datetime2 = datetime.fromisoformat(str(disbursed[index])).replace(tzinfo=timezone.utc)

        # Calculate the time difference
        time_difference = datetime1 - datetime2

        # Extract minutes from the timedelta
        minutes_difference = round(time_difference.total_seconds() / 60)

        print(f"The difference in minutes is: {minutes_difference} minutes")

        if minutes_difference < 30 and credit_limit[index] > loan_amount[index]:
            self.show_snackbar(f"Amount Paid Successfully {loan_amount[index]} to this Loan ID {loan_id_list[index]}")
            data[index]['loan_updated_status'] = 'disbursed'
            data[index]['loan_disbursed_timestamp'] = paid_time
            self.manager.current = 'ViewLoansRequest'
            return

        elif minutes_difference > 30:
            self.show_snackbar(f"Time Out You Must Finish Before 30 Minutes")
            data[index]['loan_updated_status'] = 'lost opportunities'
            self.manager.current = 'ViewLoansRequest'
            return

        elif credit_limit[index] < loan_amount[index]:
            self.show_snackbar(f"Your Credit Limit Not Sufficient for Loan Amount {loan_amount[index]}")
            self.manager.current = 'ViewLoansRequest'
            return


class ViewLoansProfileScreenRL(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_back_button_press(self):
        self.manager.current = 'ViewLoansRequest'

    def initialize_with_value(self, value, data):
        customer_id = []
        loan_id = []
        tenure = []
        interest_rate = []
        loan_amount = []
        member_rom = []
        member_since = []
        credit_limit = []
        beseem_score = []
        name = []
        for i in data:
            customer_id.append(i['borrower_customer_id'])
            loan_id.append(i['loan_id'])
            tenure.append(i['tenure'])
            interest_rate.append(i['interest_rate'])
            loan_amount.append(i['loan_amount'])
            member_rom.append(i['member_rom'])
            member_since.append(i['member_since'])
            credit_limit.append(i['credit_limit'])
            beseem_score.append(i['beseem_score'])
            name.append(i['borrower_full_name'])

        if value in loan_id:
            index = loan_id.index(value)
            self.ids.loan_id.text = str(loan_id[index])
            self.ids.user1.text = str(customer_id[index])
            self.ids.interest.text = str(interest_rate[index])
            self.ids.tenure.text = str(tenure[index])
            self.ids.amount_applied.text = str(loan_amount[index])
            self.ids.rome.text = str(member_rom[index])
            self.ids.since.text = str(member_since[index])
            self.ids.limit.text = str(credit_limit[index])
            self.ids.beseem.text = str(beseem_score[index])
            self.ids.name.text = str(name[index])

    def on_pre_enter(self):
        # Bind the back button event to the on_back_button method
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        # Unbind the back button event when leaving the screen
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        # Handle the back button event
        if key == 27:  # 27 is the keycode for the hardware back button on Android
            self.go_back()
            return True  # Consume the event, preventing further handling
        return False  # Continue handling the event

    def go_back(self):
        # Navigate to the previous screen with a slide transition
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'ViewLoansRequest'


class MyScreenManager(ScreenManager):
    pass

