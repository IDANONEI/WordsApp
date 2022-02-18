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

from kivy.core.window import Window

from Regisration import *
from Account import *

class AppManager(ScreenManager):
    def __init__(self, db, is_authorized, **kwargs):
        super().__init__(**kwargs)

        self.db = db
        self.answers_list = self.db.take_answer()
        self.divide_into_groups()

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
        self.SettingsWindow = Settings_AppScreen(self, name="Settings_App")

        self.Change_informationWindow =Change_information(self,name="change_information")
        self.Change_passwordWindow = Change_passwordScreen(self, name="change_password")
        self.Change_nameWindow = Change_NameScreen(self, name="change_name")
        self.Change_mailWindow = Change_mailScreen(self, name="change_login")

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
            self.add_widget(self.SettingsWindow)
            self.add_widget(self.Change_passwordWindow)
            self.add_widget(self.About_AppWindow)
            self.add_widget(self.Change_informationWindow)
            self.add_widget(self.Change_mailWindow)
            self.add_widget(self.Change_nameWindow)

        else:
            self.add_widget(self.HomeWindow)
            self.add_widget(self.TrainingWindow)
            self.add_widget(self.StatisticWindow)
            self.add_widget(self.TheoryWindow)
            self.add_widget(self.RatingWindow)
            self.add_widget(self.PracticeWindow)
            self.add_widget(self.TestWindow)
            self.add_widget(self.SettingsWindow)
            self.add_widget(self.Change_informationWindow)
            self.add_widget(self.Change_nameWindow)
            self.add_widget(self.Change_mailWindow)
            self.add_widget(self.Change_passwordWindow)
            self.add_widget(self.About_AppWindow)

            self.add_widget(self.SingUpWindow)
            self.add_widget(self.ForgotPasswordWindow)
            self.add_widget(self.RegistrationWindow)

    def __del__(self):
        print("Вызвался деструктор")
        self.PracticeWindow.give_answers_list()
        self.db.give_answer(self.answers_list['correct'], self.answers_list['wrong'])

    def divide_into_groups(self):
        self.word_groups = {"new": [], "red": [], "yellow": [], "green": []}
        for i in range(len(self.answers_list['correct'])):
            total_answers = self.answers_list['correct'][i] + self.answers_list['wrong'][i]
            if total_answers == 0:
                self.word_groups["new"].append(i)
            elif self.answers_list['correct'][i] / total_answers < 1 / 3:
                self.word_groups["red"].append(i)
            elif 1 / 3 <= self.answers_list['correct'][i] / total_answers <= 2 / 3:
                self.word_groups["yellow"].append(i)
            else:
                self.word_groups["green"].append(i)

    def switch_to_registration(self, button):
        self.switch_to(self.RegistrationWindow, direction='left')

    def switch_to_forgot_password(self, button):
        self.switch_to(self.ForgotPasswordWindow, direction='left')

    def switch_to_singup(self, button=None):

        self.switch_to(self.SingUpWindow, direction='right')

    def switch_to_app_screen(self, button):
        self.switch_to(self.About_AppScreen, direction='right')

    def switch_to_home_left(self, button=None):
        self.switch_to(self.HomeWindow, direction='left')

    def switch_to_home_right(self, button=None):
        self.switch_to(self.HomeWindow, direction='right')

    def switch_to_training_left(self, button):
        self.answers_list = self.db.take_answer()
        self.switch_to(self.TrainingWindow, direction='left')

    def switch_to_training_right(self, button=None):
        self.switch_to(self.TrainingWindow, direction='right')

    def switch_to_dictionary(self, button):
        self.switch_to(self.My_dictionaryWindow, direction='left')

    def switch_to_statistic(self, button):
        self.switch_to(self.StatisticWindow, direction='left')

    def switch_to_statistic_right(self, button):
        self.switch_to(self.StatisticWindow, direction='right')

    def switch_to_theory(self, button):
        self.switch_to(self.TheoryWindow, direction='left')

    def switch_to_practice(self, button):
        self.PracticeWindow = PracticeScreen(self, name="Practice")
        self.switch_to(self.PracticeWindow, direction='left')

    def switch_to_test(self, button):
        self.TestWindow.add_on_screen()
        self.switch_to(self.TestWindow, direction='left')


    def switch_to_settings(self, button):
        self.switch_to(self.SettingsWindow, direction='left')

    def switch_to_settings_right(self, button):
        self.switch_to(self.SettingsWindow, direction='right')

    def switch_change_information(self,button):
        self.switch_to(self.Change_informationWindow, direction='left')
    def switch_change_information_rigth(self,button=None):
        self.switch_to(self.Change_informationWindow, direction='right')

    def switch_change_name(self,button):
        self.switch_to(self.Change_nameWindow, direction='left')

    def switch_change_password(self,button):
        self.switch_to(self.Change_passwordWindow, direction='left')

    def switch_change_mail(self,button):
        self.switch_to(self.Change_mailWindow, direction='left')

    def switch_about_app(self,button):
        self.switch_to(self.About_AppWindow, direction='left')

    def switch_rating(self, button):
        self.PracticeWindow.give_answers_list()
        self.db.give_answer(self.answers_list['correct'], self.answers_list['wrong'])
        self.RatingWindow = RatingScreen(self, name="Rating")
        self.switch_to(self.RatingWindow, direction='left')


    def switch_to_statistic_word(self, button):

        if button.text == "Хорошо усвоенные":
            self.StatisticWordsWindow = StatisticWordsScreen(self, "green", name = "Statistic_words")

        elif button.text == "Средне усвоенные":
            self.StatisticWordsWindow = StatisticWordsScreen(self, "yellow", name = "Statistic_words")

        elif button.text == "Не усвоенные":
            self.StatisticWordsWindow = StatisticWordsScreen(self, "red", name = "Statistic_words")

        self.switch_to(self.StatisticWordsWindow, direction = 'left')

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