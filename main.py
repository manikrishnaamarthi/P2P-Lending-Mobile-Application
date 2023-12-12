from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from screens.home_screen import HomeScreen


class P2PLendingApp(App):
    def build(self):
        # Create a ScreenManager
        screen_manager = ScreenManager()

        # Add the HomeScreen to the ScreenManager
        home_screen = HomeScreen(name='home')
        screen_manager.add_widget(home_screen)

        return screen_manager


if __name__ == '__main__':
    P2PLendingApp().run()
