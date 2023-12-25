from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, SlideTransition

from borrower_module.borrower_registration_forms import BorrowerScreen
from lender_module.lender_registration_form import (
    LenderScreen, LenderScreen1, LenderScreen2, LenderScreen3,
    LenderScreen_Edu_10th, KV
)
from users_module.dashboard import DashScreen
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.pickers import MDDatePicker
from kivy.metrics import dp
from users_module.login import LoginScreen
from users_module.homepage import MainScreen
from users_module.signup import SignupScreen

class MyApp(MDApp):
    def build(self):
        Builder.load_string(KV)
        sm = ScreenManager(transition=SlideTransition())
        main_screen = MainScreen(name='MainScreen')
        login_screen = LoginScreen(name='LoginScreen')
        signup_screen = SignupScreen(name='SignupScreen')
        sm.add_widget(DashScreen(name='dashboard'))
        sm.add_widget(BorrowerScreen(name='borrower_registration_forms'))
        sm.add_widget(LenderScreen(name='lender_registration_form'))
        sm.add_widget(LenderScreen1(name='LenderScreen1'))
        sm.add_widget(LenderScreen2(name='LenderScreen2'))
        sm.add_widget(LenderScreen3(name='LenderScreen3'))
        sm.add_widget(LenderScreen_Edu_10th(name='LenderScreen_Edu_10th'))

        sm.add_widget(main_screen)
        sm.add_widget(login_screen)
        sm.add_widget(signup_screen)

        # Set the initial screen to the login screen
        sm.current = 'MainScreen'

        # Set the screen manager for the login screen
        main_screen.app = self

        return sm







if __name__ == '__main__':
    MyApp().run()
