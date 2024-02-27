import anvil.server
from kivy.config import value
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen, SlideTransition, ScreenManager
import sqlite3
from kivymd.app import MDApp
from kivymd.uix.list import ThreeLineAvatarIconListItem, IconLeftWidget

anvil.server.connect("server_VRGEXX5AO24374UMBBQ24XN6-ZAWBX57M6ZDN6TBV")

extension_loan_request = """
<WindowManager>:
    ExtensionLoansRequest:
    ExtensionLoansProfileScreen2:
    ExtensionLoansProfileScreen:
    ExtensionLoansProfileScreen1:
    ExtendLoansScreen:

<ExtensionLoansRequest> 
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "Extension Loan Request"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.on_back_button_press()]]
            right_action_items: [['refresh', lambda x: root.refresh()]]
        MDScrollView:

            MDList:
                id: container1

<ExtensionLoansProfileScreen>
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "Extension Loan Request"
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
                        text: " Borrower Extension Request"
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

                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)
                            MDLabel:
                                text: "User ID" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                            MDLabel:
                                id: user1
                                text: "" 
                                height:dp(50)
                                size_hint_y:None
                                halign: "center"
                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)    
                            MDLabel:
                                text: "Loan ID" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                            MDLabel:
                                id: loan_id
                                text: "" 
                                halign: "center"
                                height:dp(50)
                                size_hint_y:None
                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)    
                            MDLabel:
                                text: "Name" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                            MDLabel:
                                id: name
                                text: "" 
                                height:dp(50)
                                size_hint_y:None
                                halign: "center"
                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)   
                            MDLabel:
                                text: "Loan Tenure" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                            MDLabel:
                                id: tenure
                                text: "" 
                                height:dp(50)
                                size_hint_y:None
                                halign: "center"
                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)    
                            MDLabel:
                                text: "Interest Rate" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                            MDLabel:
                                id: interest
                                text: "" 
                                height:dp(50)
                                size_hint_y:None
                                halign: "center"
                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)    
                            MDLabel:
                                text: "Extension Allowed" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                            MDLabel:
                                id: extension_allowed
                                text:""
                                height:dp(50)
                                size_hint_y:None
                                halign: "center"
                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)    
                            MDLabel:
                                text: "Extension Fees" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                            MDLabel:
                                id: extension_fee
                                text: "" 
                                height:dp(50)
                                size_hint_y:None
                                halign: "center"
                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)    
                            MDLabel:
                                text: "Extension Months" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                            MDTextField:
                                hint_text: ""
                                id: extension_months
                                height:dp(50)
                                size_hint_y:None
                                halign: "center"
                        MDRaisedButton:
                            id:extension_request
                            text: "Extension Request"
                            md_bg_color: 5/255, 235/255, 77/255, 1
                            theme_text_color: 'Primary'
                            font_name: "Roboto-Bold.ttf"
                            text_color: 0, 0, 0, 1
                            size_hint: 1, None
                            on_release:root.on_next()
<ExtensionLoansProfileScreen1>
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "Extension Loan Request"
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
                        text: " Borrower Extension Request"
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

                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)
                            MDLabel:
                                text: "User ID" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                            MDLabel:
                                id: user1
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)    
                            MDLabel:
                                text: "Loan ID" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                            MDLabel:
                                id: loan_id
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)    
                            MDLabel:
                                text: "Name" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                            MDLabel:
                                id: name
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)    
                            MDLabel:
                                text: "Loan Tenure" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                            MDLabel:
                                id: tenure
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)    
                            MDLabel:
                                text: "Interest Rate" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                            MDLabel:
                                id: interest
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)    
                            MDLabel:
                                text: "Extension Allowed" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                            MDLabel:
                                id: extension_allowed
                                text:""
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)    
                            MDLabel:
                                text: "Extension Fees" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                            MDLabel:
                                id: extension_fee
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)    
                            MDLabel:
                                text: "Extension Months" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                            MDLabel:
                                text: ""
                                id: extension_months
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)
                            MDLabel:
                                text: "Your Requested Extension Loan has been Underprocess" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                                bold: True           

                        MDRaisedButton:
                            text: "Extension Request"
                            md_bg_color: 5/255, 235/255, 77/255, 1
                            theme_text_color: 'Primary'
                            font_name: "Roboto-Bold.ttf"
                            text_color: 0, 0, 0, 1
                            size_hint: 1, None
                            on_release:root.on_next()

<ExtendLoansScreen>
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "Extension Loan Request"
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
                        text: " Borrower Extension Details"
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

                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)
                            MDLabel:
                                text: "Loan ID" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                            MDLabel:
                                id: loan_id
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)
                            MDLabel:
                                text: "Loan Amount" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                            MDLabel:
                                id: loan_amount
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)
                            MDLabel:
                                text: "Extension Fee" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                            MDLabel:
                                id: extension_fee
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)
                            MDLabel:
                                text: "Extension Amount" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                            MDLabel:
                                id: extension_amount
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)
                            MDLabel:
                                text: "Finial Repayment Amount" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                            MDLabel:
                                id: finial_repayment_amount
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)
                            MDLabel:
                                text: "New EMI" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                            MDLabel:
                                id: new_emi
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                        MDGridLayout:
                            cols: 1
                            spacing: dp(10)
                            padding: dp(10)
                            MDLabel:
                                text: "Reason For Extended Loan:" 
                                size_hint_y:None
                                height:dp(50)
                                bold: True
                            MDTextField:
                                hint_text: ""
                                id: reason
                                size_hint_y:None
                                height:dp(50)

                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)
                            MDCheckbox:
                                id: kyc_checkbox
                                size_hint_x: None
                                width: "20dp"
                            MDLabel:
                                text: "I Agree Terms and Conditions"
                                multiline: False
                                theme_text_color: 'Primary'
                                halign: 'left'
                                valign: 'center'

                        MDRaisedButton:
                            text: "Submit"
                            md_bg_color: 5/255, 235/255, 77/255, 1
                            theme_text_color: 'Primary'
                            font_name: "Roboto-Bold.ttf"
                            text_color: 0, 0, 0, 1
                            size_hint: 1, None
"""
Builder.load_string(extension_loan_request)


class ExtensionLoansRequest(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        data = self.get_table_data()
        customer_id = []
        loan_id = []
        borrower_name = []
        loan_status = []
        tenure = []
        s = 0
        for i in data:
            s += 1
            customer_id.append(i['borrower_customer_id'])
            loan_id.append(i['loan_id'])
            borrower_name.append(i['borrower_full_name'])
            loan_status.append(i['loan_updated_status'])
            tenure.append(i['tenure'])
        c = -1
        index_list = []
        for i in range(s):
            c += 1
            if loan_status[c] == 'disbursed':
                index_list.append(c)

        b = 1
        k = -1
        for i in index_list:
            b += 1
            k += 1
            item = ThreeLineAvatarIconListItem(

                IconLeftWidget(
                    icon="card-account-details-outline"
                ),
                text=f"Loan ID : {loan_id[i]}",
                secondary_text=f"Borrower Name: {borrower_name[i]}",
                tertiary_text=f"Status: {loan_status[i]}",
            )
            item.bind(on_release=self.icon_button_clicked)  # Corrected the binding
            self.ids.container1.add_widget(item)

    def on_back_button_press(self):
        self.manager.current = 'DashboardScreen'

    def get_table_data(self):
        # Make a call to the Anvil server function
        # Replace 'YourAnvilFunction' with the actual name of your Anvil server function
        return anvil.server.call('get_table_data')

    def refresh(self):
        self.ids.container1.clear_widgets()
        self.__init__()

    def icon_button_clicked(self, instance):
        value = instance.text.split(':')
        value = value[-1][1:]
        data = self.get_table_data()  # Fetch data here
        loan_status = None
        for loan in data:
            if loan['loan_id'] == value:
                loan_status = loan['loan_updated_status']
                break

        if loan_status == 'disbursed':
            # Open the screen for approved loans
            sm=self.manager
            disbursed=ExtensionLoansProfileScreen(name='ExtensionLoansProfileScreen')
            sm.add_widget(disbursed)
            sm.current = 'ExtensionLoansProfileScreen'
            self.manager.get_screen('ExtensionLoansProfileScreen').initialize_with_value(value, data)
        else:
            pass
    def on_pre_enter(self):
        # Bind the back button event to the on_back_button method
        Window.bind(on_keyboard=self.on_keyboard)
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        # Unbind the back button event when leaving the screen
        Window.bind(on_keyboard=self.on_keyboard)
        Window.bind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        # Handle the back button event
        if key == 27:  # 27 is the keycode for the hardware back button on Android
            self.go_back()
            return True  # Consume the event, preventing further handling
        return False  # Continue handling the event

    def go_back(self):
        # Navigate to the previous screen with a slide transition
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'DashboardScreen'

    def on_keyboard(self, window, key, *args):
        if key == 27:  # Key code for the 'Escape' key
            # Keyboard is closed, move the screen down
            self.screen_manager.y = 0
        return True

    def on_start(self):
        Window.softinput_mode = "below_target"

class ExtensionLoansProfileScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def initialize_with_value(self, value, data):
        customer_id = []
        loan_id = []
        name = []
        tenure = []
        interest_rate = []
        extension_allowed = []
        extension_fee = []
        extension_months = []
        for i in data:
            customer_id.append(i['borrower_customer_id'])
            loan_id.append(i['loan_id'])
            tenure.append(i['tenure'])
            interest_rate.append(i['interest_rate'])
            extension_allowed.append(i['application_status'])
            # extension_fee.append(i('extend_fee'))
            name.append(i['borrower_full_name'])

        if value in loan_id:
            index = loan_id.index(value)
            self.ids.loan_id.text = str(loan_id[index])
            self.ids.user1.text = str(customer_id[index])
            self.ids.interest.text = str(interest_rate[index])
            self.ids.tenure.text = str(tenure[index])
            # self.ids.extension_allowed.active = bool(extension_allowed[index])
            # self.ids.extension_fee.text = str(extension_fee[index])
            self.ids.name.text = str(name[index])
            print(index)
            # Check if the button exists in ids before accessing its attributes
            if int(tenure[index] >= 12):
                self.ids.extension_request.disabled = False
            else:
                self.show_popup("Tenure Warning", "Your tenure needs to be more than 12 months")
                self.ids.extension_request.disabled = True

    def show_popup(self, title, content):
        popup = Popup(title=title, content=Label(text=content), size_hint=(None, None), size=(400, 200))
        popup.open()

    def on_pre_enter(self):
        # Bind the back button event to the on_back_button method
        Window.bind(on_keyboard=self.on_keyboard)
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        # Unbind the back button event when leaving the screen
        Window.bind(on_keyboard=self.on_keyboard)
        Window.bind(on_keyboard=self.on_back_button)


    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        # Handle the back button event
        if key == 27:  # 27 is the keycode for the hardware back button on Android
            self.go_back()
            return True  # Consume the event, preventing further handling
        return False  # Continue handling the event

    def go_back(self):
        # Navigate to the previous screen with a slide transition
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'ExtensionLoansRequest'
    def on_back_button_press(self):
        self.manager.current = 'ExtensionLoansRequest'

    def on_next(self):
        self.manager.current = 'ExtensionLoansProfileScreen1'

    def on_keyboard(self, window, key, *args):
        if key == 27:  # Key code for the 'Escape' key
            # Keyboard is closed, move the screen down
            self.screen_manager.y = 0
        return True

    def on_start(self):
        Window.softinput_mode = "below_target"

    def get_table_data(self):
        # Make a call to the Anvil server function
        # Replace 'YourAnvilFunction' with the actual name of your Anvil server function
        return anvil.server.call('get_table_data')

    def extension_loans_profile_screen1(self,value):
        data=self.get_table_data()
        sm=self.manager
        profile=ExtensionLoansProfileScreen1(name='ExtensionLoansProfileScreen1')
        sm.add_widget(profile)
        sm.current='ExtensionLoansProfileScreen1'
        self.manager.get_screen('ExtensionLoansProfileScreen1').initialize_with_value(value, data)

class ExtensionLoansProfileScreen1(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def initialize_with_value(self, value, data):
        customer_id = []
        loan_id = []
        name = []
        tenure = []
        interest_rate = []
        extension_allowed = []
        extension_fee = []
        extension_months = []

        for i in data:
            customer_id.append(i['borrower_customer_id'])
            loan_id.append(i['loan_id'])
            tenure.append(i['tenure'])
            interest_rate.append(i['interest_rate'])
            extension_allowed.append(i['application_status'])
            # extension_fee.append(i('extend_fee'))
            name.append(i['borrower_full_name'])
        if value in loan_id:
            index = loan_id.index(value)
            self.ids.loan_id.text = str(loan_id[index])
            self.ids.user1.text = str(customer_id[index])
            self.ids.interest.text = str(interest_rate[index])
            self.ids.tenure.text = str(tenure[index])
            # Update the following lines for the checkbox and other fields
            # self.ids.extension_allowed.active = bool(extension_allowed[index])
            # self.ids.extension_fee.text = str(extension_fee[index])
            self.ids.name.text = str(name[index])
            print(index)

    def on_back_button_press(self):
        self.manager.current = 'ExtensionLoansProfileScreen'

    def get_table_data(self):
        # Make a call to the Anvil server function
        # Replace 'YourAnvilFunction' with the actual name of your Anvil server function
        return anvil.server.call('get_table_data')

    def on_next(self):
        self.manager.current = 'ExtendLoansScreen'

    def on_keyboard(self, window, key, *args):
        if key == 27:  # Key code for the 'Escape' key
            # Keyboard is closed, move the screen down
            self.screen_manager.y = 0
        return True

    def on_start(self):
        Window.softinput_mode = "below_target"
    def on_pre_enter(self):
        # Bind the back button event to the on_back_button method
        Window.bind(on_keyboard=self.on_keyboard)
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        # Unbind the back button event when leaving the screen
        Window.bind(on_keyboard=self.on_keyboard)
        Window.bind(on_keyboard=self.on_back_button)


    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        # Handle the back button event
        if key == 27:  # 27 is the keycode for the hardware back button on Android
            self.go_back()
            return True  # Consume the event, preventing further handling
        return False  # Continue handling the event

    def go_back(self):
        # Navigate to the previous screen with a slide transition
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'ExtensionLoansProfileScreen'

    def extend_loans_screen(self,value):
        data=self.get_table_data()
        sm=self.manager
        profile=ExtendLoansScreen(name='ExtendLoansScreen')
        sm.add_widget(profile)
        sm.current='ExtendLoansScreen'
        self.manager.get_screen('ExtendLoansScreen').initialize_with_value(value, data)

class ExtendLoansScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_back_button_press(self):
        self.manager.current = 'ExtensionLoansProfileScreen1'

    def initialize_with_value(self, value, data):
        loan_id = []
        loan_amount = []
        extension_fee = []
        extension_amount = []
        new_emi = []
        finial_repayment_amount = []
        reason = []

        for i in data:
            loan_id.append(i['loan_id'])
            loan_amount.append(i['loan_amount'])
            extension_amount.append(i['extension_amount'])
            extension_fee.append(i['extend_fee'])
            new_emi.append(i['new_emi'])
            finial_repayment_amount.append(i['final_repayment_amount'])
            reason.append(i['reason'])

        if value in loan_id:
            index = loan_id.index(value)
            self.ids.loan_id.text = str(loan_id[index])
            self.ids.loan_amount.text = str(loan_amount[index])
            self.ids.extension_fee.text = str(extension_fee[index])
            # Update the following lines for the checkbox and other fields
            self.ids.new_emi.text = str(new_emi[index])
            self.ids.finial_repayment_amount.text = str(finial_repayment_amount[index])
            self.ids.reason.text = str(reason[index])

    def on_pre_enter(self):
        # Bind the back button event to the on_back_button method
        Window.bind(on_keyboard=self.on_keyboard)
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        # Unbind the back button event when leaving the screen
        Window.bind(on_keyboard=self.on_keyboard)
        Window.bind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        # Handle the back button event
        if key == 27:  # 27 is the keycode for the hardware back button on Android
            self.go_back()
            return True  # Consume the event, preventing further handling
        return False  # Continue handling the event
    def on_keyboard(self, window, key, *args):
        if key == 27:  # Key code for the 'Escape' key
            # Keyboard is closed, move the screen down
            self.screen_manager.y = 0
        return True

    def on_start(self):
        Window.softinput_mode = "below_target"

    def go_back(self):
        # Navigate to the previous screen with a slide transition
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'ExtensionLoansProfileScreen1'

class MyScreenManager(ScreenManager):
    pass
