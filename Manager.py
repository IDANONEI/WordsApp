from kivy.app import App
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout

from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton, MDRoundFlatButton, MDRaisedButton, MDFillRoundFlatButton
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextFieldRound

from Regisration import *
from Account import *


class AppManager(ScreenManager):
    def __init__(self, db, is_authorized, **kwargs):
        super().__init__(**kwargs)

        self.db = db

        self.SingUpWindow = SingUpScreen(self, name="SingUp")
        self.ForgotPasswordWindow = ForgotPasswordScreen(self, name="ForgotPassword")
        self.RegistrationWindow = RegistrationScreen(self, name="Registration")

        self.HomeWindow = HomeScreen(self, name="Home")
        self.TrainingWindow = TrainingScreen(self, name="Training")
        self.About_AppWindow = About_AppScreen(self, name="About_App")
        self.StatisticWindow = StatisticScreen(self, name="Statistic")
        self.TheoryWindow = TheoryScreen(self, name="Theory")
        self.RatingWindow = RatingScreen(self, name="Rating")
        self.PracticeWindow = PracticeScreen(self, name="Practice")
        self.TestWindow = TestScreen(self, name="Test")
        self.About_AppWindow =About_AppScreen(self, name="About_App")

        if not is_authorized:
            self.add_widget(self.SingUpWindow)
            self.add_widget(self.ForgotPasswordWindow)
            self.add_widget(self.RegistrationWindow)

            self.add_widget(self.HomeWindow)
            self.add_widget(self.TrainingWindow)
            self.add_widget(self.StatisticWindow)
            self.add_widget(self.TheoryWindow)
            self.add_widget(self.RatingWindow)
            self.add_widget(self.PracticeWindow)
            self.add_widget(self.TestWindow)

        else:
            self.add_widget(self.HomeWindow)
            self.add_widget(self.TrainingWindow)
            self.add_widget(self.StatisticWindow)
            self.add_widget(self.TheoryWindow)
            self.add_widget(self.RatingWindow)
            self.add_widget(self.PracticeWindow)
            self.add_widget(self.TestWindow)

            self.add_widget(self.SingUpWindow)
            self.add_widget(self.ForgotPasswordWindow)
            self.add_widget(self.RegistrationWindow)

    def switch_to_registration(self, button):
        self.switch_to(self.RegistrationWindow, direction='left')

    def switch_to_forgot_password(self, button):
        self.switch_to(self.ForgotPasswordWindow, direction='left')

    def swith_to_singup(self, button):
        self.switch_to(self.SingUpWindow, direction='right')

    def swith_to_app_screen(self, button):
        self.switch_to(self.About_AppScreen, direction='right')



    def switch_to_home_left(self, button = None):
        self.switch_to(self.HomeWindow, direction='left')

    def switch_to_home_right(self, button=None):
        self.switch_to(self.HomeWindow, direction='right')

    def switch_to_training(self, button):
        self.switch_to(self.TrainingWindow, direction='left')

    def switch_to_dictionary(self, button):
        self.switch_to(self.My_dictionaryWindow, direction='left')

    def switch_to_statistic(self, button):
        self.switch_to(self.StatisticWindow, direction='left')

    def switch_to_theory(self, button):
        self.switch_to(self.TheoryWindow, direction='left')

    def switch_to_practice(self, button):
        self.switch_to(self.PracticeWindow, direction='left')

    def switch_to_test(self, button):
        self.switch_to(self.TestWindow, direction='left')


    def cleen_text(self, instance, value):
        if instance.text == "Логин":
            if value:
                instance.text = ""
            else:
                instance.foreground_color = (192 / 255, 192 / 255, 192 / 255, 1)

    def change_icon_color(self, instance, value):
        if value:
            instance.icon_left_color = (147 / 255, 7 / 255, 200 / 255)
        else:
            instance.icon_left_color = (1, 1, 1, 1)


class ManagerApp(MDApp):
    def __init__(self, db, is_authorized, **kwargs):
        super().__init__(**kwargs)
        self.db = db
        self.is_authorized = is_authorized
        self.theme_cls.theme_style = "Dark"

    def build(self):
        reg_man = AppManager(self.db, self.is_authorized)

        return reg_man
