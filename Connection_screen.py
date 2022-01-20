from Connection import Connection
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


class ConnectionWindow(Screen):
    pass


class PasswordWindow(Screen):
    pass


class CreateAccountWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass

def show_popup():
    pass

connection_kv = Builder.load_file("connection.kv")


class MyMainApp(App):
    def build(self):
        return connection_kv


if __name__ == '__main__':
    MyMainApp().run()
