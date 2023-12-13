from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from screens.home_screen import HomeScreen
from screens.login_screen import LoginScreen
from screens.signup_screen import SignupScreen


class P2PLendingApp(App):

    def build(self):
        self.screen_manager = ScreenManager()

        # Check if user is logged in
        is_logged_in = self.check_logged_in()

        # Add appropriate screen based on login status
        if is_logged_in:
            home_screen = HomeScreen(name='home')
            self.screen_manager.add_widget(home_screen)
        else:
            login_screen = LoginScreen(name='login')
            self.screen_manager.add_widget(login_screen)
            signup_screen = SignupScreen(name='signup')
            self.screen_manager.add_widget(signup_screen)

        return self.screen_manager


if __name__ == '__main__':
    P2PLendingApp().run()
