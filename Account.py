from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout

from random import randint
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton, MDRoundFlatButton, MDRaisedButton, MDFillRoundFlatButton, \
    MDIconButton, MDFloatingActionButton
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.textfield import MDTextFieldRound

vowels = "АОЭЕИЫУЁЮЯ"

class HomeScreen(Screen):
    def __init__(self, manager, **kwargs):
        super(HomeScreen, self).__init__()


        self.man = manager

        self.lbl = MDLabel(
            text="СВЁКЛА",
            font_style="H3",
            halign="center",
            pos_hint={'center_x': 0.5, 'center_y': 0.85},
            theme_text_color="Custom",
            text_color=(147 / 255, 7 / 255, 200 / 255)
        )

        self.training_btn = MDFillRoundFlatButton(
            text='Тренировка',
            text_color=(1, 1, 1, 1),
            md_bg_color=(120 / 255, 0, 120 / 255),
            pos_hint={'center_x': 0.5, 'center_y': 0.7},
            on_press=self.man.switch_to_training,
            size_hint=(0.5, 0.07)
        )

        self.statistics_btn = MDFillRoundFlatButton(
            text='Статистика',
            text_color=(1, 1, 1, 1),
            md_bg_color=(120 / 255, 0, 120 / 255),
            pos_hint={'center_x': 0.5, 'center_y': 0.58},
            # on_press=
            size_hint=(0.5, 0.07)
        )

        self.rating_btn = MDFillRoundFlatButton(
            text='Рейтинг',
            text_color=(1, 1, 1, 1),
            md_bg_color=(120 / 255, 0, 120 / 255),
            pos_hint={'center_x': 0.5, 'center_y': 0.46},
            # on_press=
            size_hint=(0.5, 0.07)
        )

        self.about_app = MDFillRoundFlatButton(
            text='О приложении',
            text_color=(1, 1, 1, 1),
            md_bg_color=(120 / 255, 0, 120 / 255),
            pos_hint={'center_x': 0.5, 'center_y': 0.34},
            # on_press=self.man.,
            size_hint=(0.5, 0.07)
        )

        self.settings_button = MDIconButton(
            icon="cog-outline",
            theme_text_color="Custom",
            text_color=(120 / 255, 0, 120 / 255, 1),
            pos_hint={'center_x': 0.9, 'center_y': 0.9},
            user_font_size="40sp",
            on_press=manager.switch_to_settings
        )

        self.add_widget(self.lbl)
        self.add_widget(self.training_btn)
        self.add_widget(self.statistics_btn)
        self.add_widget(self.rating_btn)
        self.add_widget(self.settings_button)
        self.add_widget(self.about_app)


class TrainingScreen(Screen):
    def __init__(self, manager, **kwargs):
        super().__init__(**kwargs)

        self.lbl = MDLabel(
            text="Тренировка",
            font_style="H3",
            halign="center",
            pos_hint={'center_x': 0.5, 'center_y': 0.85},
            theme_text_color="Custom",
            text_color=(147 / 255, 7 / 255, 200 / 255)
        )

        self.theory_btn = MDFillRoundFlatButton(
            text='Теория',
            text_color=(1, 1, 1, 1),
            md_bg_color=(120 / 255, 0, 120 / 255),
            pos_hint={'center_x': 0.5, 'center_y': 0.7},
            on_press=manager.switch_to_theory,
            size_hint=(0.5, 0.07)
        )

        self.practice_btn = MDFillRoundFlatButton(
            text='Практика',
            text_color=(1, 1, 1, 1),
            md_bg_color=(120 / 255, 0, 120 / 255),
            pos_hint={'center_x': 0.5, 'center_y': 0.6},
            on_press=manager.switch_to_practice,
            size_hint=(0.5, 0.07)
        )

        self.test_btn = MDFillRoundFlatButton(
            text='Тест',
            text_color=(1, 1, 1, 1),
            md_bg_color=(120 / 255, 0, 120 / 255),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            on_press=manager.switch_to_test,
            size_hint=(0.5, 0.07)
        )

        self.move_back_btn = MDFillRoundFlatButton(
            text='Назад',
            text_color=(1, 1, 1, 1),
            md_bg_color=(120 / 255, 0, 120 / 255),
            pos_hint={'center_x': 0.5, 'center_y': 0.2},
            on_press=manager.switch_to_home_left,
            size_hint=(0.5, 0.07)
        )

        self.add_widget(self.lbl)
        self.add_widget(self.theory_btn)
        self.add_widget(self.practice_btn)
        self.add_widget(self.test_btn)
        self.add_widget(self.move_back_btn)


class About_AppScreen(Screen):
    def __init__(self, manager, **kwargs):
        super().__init__(**kwargs)


class Settings_AppScreen(Screen):
    def __init__(self, manager, **kwargs):
        super().__init__(**kwargs)
        self.list_letter_button = MDFillRoundFlatButton(
            text="Выйти из аккаунта",
            font_size=30,
            size_hint=(None, None),
            size=(10, 10),
            md_bg_color=(120 / 255, 0, 120 / 255),
            on_press=self.leave_a,
            md_bg_color_disabled=(120 / 255, 0, 120 / 255))
        self.password = MDFillRoundFlatButton(
            text="Сменить пароль",
            font_size=30,
            size_hint=(None, None),
            size=(10, 10),
            md_bg_color=(120 / 255, 0, 120 / 255),
            # on_press=,
            md_bg_color_disabled=(120 / 255, 0, 120 / 255))
        self.back = MDFillRoundFlatButton(
            text="Назад",
            font_size=30,
            size_hint=(None, None),
            size=(10, 10),
            md_bg_color=(120 / 255, 0, 120 / 255),
            on_press=manager.switch_to_home_right,
            md_bg_color_disabled=(120 / 255, 0, 120 / 255))

        self.add_widget(self.list_letter_button)
        self.add_widget(self.password)
        self.add_widget(self.back)

    def leave_a(self, button):
        pass


class StatisticScreen(Screen):
    def __init__(self, manager, **kwargs):
        super().__init__(**kwargs)


class TheoryScreen(Screen):
    def __init__(self, manager, **kwargs):
        super().__init__(**kwargs)


class RatingScreen(Screen):
    def __init__(self, manager, **kwargs):
        super().__init__(**kwargs)
        pass


class PracticeScreen(Screen):
    def __init__(self, manager, **kwargs):
        super().__init__(**kwargs)

        self.man = manager

        self.count_right_words = 0
        self.count_wrong_words = 0

        self.add_widget(MDIconButton(
            icon="check-bold",
            theme_text_color="Custom",
            text_color=(0, 200 / 255, 0, 1),
            pos_hint={"center_x": 0.1, 'center_y': 0.9},
            user_font_size="40sp",
        ))

        self.add_widget(MDIconButton(
            icon="close-thick",
            theme_text_color="Custom",
            text_color=(200 / 255, 0, 0, 1),
            pos_hint={"center_x": 0.1, 'center_y': 0.8},
            user_font_size="40sp",
        ))

        self.new_word()
        self.add_word()

    def new_word(self):
        self.word_ind = randint(0, len(self.man.word_groups['new']) - 1)

        with open("words.txt", "r", encoding='utf-8') as f:
            temp = f.readlines()[self.word_ind]
        self.word = temp.strip()

        self.accented = []
        for i in range(len(self.word)):
            if self.word[i] in vowels:
                self.accented.append(i)

        self.word = self.word.upper()

    def add_word(self):
        self.list_letter_button = [MDFillRoundFlatButton(text=str(letter),
                                   font_size=30,
                                   size_hint=(None, None),
                                   size = (10,10),
                                   md_bg_color=(120 / 255, 0, 120 / 255),
                                   md_bg_color_disabled = (120 / 255, 0, 120 / 255))
                                   for letter in self.word]


        for i in range(len(self.list_letter_button)):
            if self.list_letter_button[i].text in vowels:
                if self.accented.count(i) > 0:
                    self.list_letter_button[i].accented = True
                else:
                    self.list_letter_button[i].accented = False
                self.list_letter_button[i].bind(on_press = self.check_variable)


        num_rows = len(self.list_letter_button) // 5
        if len(self.list_letter_button) % 5 != 0:
            num_rows += 1
            space_btw_rows = 0.5 / (num_rows + 1)
            for i in range(num_rows - 1):
                temp = self.placement_in_row(5)
                for j in range(5):
                    self.list_letter_button[i * 5 + j].pos_hint = {'center_x': temp[j],
                                                                   'center_y': 0.7 - space_btw_rows * (i + 1)}
            temp = self.placement_in_row(len(self.list_letter_button) % 5)
            for j in range(len(self.list_letter_button) % 5):
                self.list_letter_button[-(len(self.list_letter_button) % 5) + j].pos_hint = {'center_x': temp[j],
                                                                                             'center_y': 0.2 + space_btw_rows}
        else:
            space_btw_rows = 0.4 / (num_rows)
            for i in range(num_rows):
                temp = self.placement_in_row(5)
                for j in range(5):
                    self.list_letter_button[i * 5 + j].pos_hint = {'center_x': temp[j],
                                                                   'center_y': 0.7 - space_btw_rows * (i + 1)}
        for button in self.list_letter_button:
            self.add_widget(button)


    def check_variable (self,button):
        if button.accented:
            button.md_bg_color=(0, 200 / 255, 0, 1)
            Clock.schedule_once(self.remove_words,1)
        else: button.md_bg_color=(200 / 255, 0, 0, 1)

    def remove_words(self, value):
        for button in self.list_letter_button:
            self.remove_widget(button)
        self.new_word()
        self.add_word()

    def placement_in_row(self, num):
        if num == 5:
            return [0.15, 0.325, 0.5, 0.675, 0.85]
        if num == 4:
            return [0.2, 0.4, 0.6, 0.8]
        if num == 3:
            return [0.325, 0.5, 0.675]
        if num == 2:
            return [0.4, 0.6]
        else:
            return [0.5]


class TestScreen(Screen):
    def __init__(self, manager, **kwargs):
        super().__init__(**kwargs)
