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
            text='Треннировка',
            text_color=(1, 1, 1, 1),
            md_bg_color=(120 / 255, 0, 120 / 255),
            pos_hint={'center_x': 0.5, 'center_y': 0.7},
            on_press=self.man.switch_to_training,
            size_hint=(0.44, 0.05)
        )

        self.my_dict_btn = MDFillRoundFlatButton(
            text='Мой словарь',
            text_color=(1, 1, 1, 1),
            md_bg_color=(120 / 255, 0, 120 / 255),
            pos_hint={'center_x': 0.5, 'center_y': 0.6},
            on_press=self.man.switch_to_dictionary ,
            size_hint=(0.44, 0.05)
        )

        self.statistics_btn = MDFillRoundFlatButton(
            text='Статистика',
            text_color=(1, 1, 1, 1),
            md_bg_color=(120 / 255, 0, 120 / 255),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            # on_press=
            size_hint=(0.44, 0.05)
        )

        self.theory_btn = MDFillRoundFlatButton(
            text='Теория',
            text_color=(1, 1, 1, 1),
            md_bg_color=(120 / 255, 0, 120 / 255),
            pos_hint={'center_x': 0.5, 'center_y': 0.4},
            # on_press=
            size_hint=(0.44, 0.05)
        )

        self.rating_btn = MDFillRoundFlatButton(
            text='Рэйтинг',
            text_color=(1, 1, 1, 1),
            md_bg_color=(120 / 255, 0, 120 / 255),
            pos_hint={'center_x': 0.5, 'center_y': 0.3},
            # on_press=
            size_hint=(0.44, 0.05)
        )

        self.add_widget(self.lbl)
        self.add_widget(self.training_btn)
        self.add_widget(self.my_dict_btn)
        self.add_widget(self.statistics_btn)
        self.add_widget(self.theory_btn)
        self.add_widget(self.rating_btn)


class TrainingScreen(Screen):
    def __init__(self, manager, **kwargs):
        super().__init__(**kwargs)

class My_dictionaryScreen(Screen):
    def __init__(self,manager, **kwargs):
        super().__init__(**kwargs)


class StatisticScreen(Screen):
    def __init__(self,manager, **kwargs):
        super().__init__(**kwargs)


class TheoryScreen(Screen):
    def __init__(self,manager, **kwargs):
        super().__init__(**kwargs)
        pass

class RatingScreen(Screen):
    def __init__(self,manager, **kwargs):
        super().__init__(**kwargs)
        pass