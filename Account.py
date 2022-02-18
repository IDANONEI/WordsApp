from kivy.app import App
from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
from kivy.utils import get_color_from_hex
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.list import MDList, ThreeLineListItem
from kivy.core.window import Window


from Regisration import change_current_info

from random import randint, choice, shuffle
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton, MDRoundFlatButton, MDRaisedButton, MDFillRoundFlatButton, \
    MDIconButton, MDFloatingActionButton
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.textfield import MDTextFieldRound


import Regisration
from Constans import VOWELS
from Regisration import PopWindow




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
            on_press=self.man.switch_to_training_left,
            size_hint=(0.5, 0.07)
        )

        self.add_widget(MDFillRoundFlatButton(
            text='Теория',
            text_color=(1, 1, 1, 1),
            md_bg_color=(120 / 255, 0, 120 / 255),
            pos_hint={'center_x': 0.5, 'center_y': 0.6},
            on_press=manager.switch_to_theory,
            size_hint=(0.5, 0.07)
        ))

        self.statistics_btn = MDFillRoundFlatButton(
            text='Статистика',
            text_color=(1, 1, 1, 1),
            md_bg_color=(120 / 255, 0, 120 / 255),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            on_press=self.man.switch_to_statistic,
            size_hint=(0.5, 0.07)
        )

        self.rating_btn = MDFillRoundFlatButton(
            text='Рейтинг',
            text_color=(1, 1, 1, 1),
            md_bg_color=(120 / 255, 0, 120 / 255),
            pos_hint={'center_x': 0.5, 'center_y': 0.4},
            on_press=manager.switch_rating,
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
            on_press=manager.switch_to_home_right,
            size_hint=(0.5, 0.07)
        )

        self.add_widget(self.lbl)
        self.add_widget(self.practice_btn)
        self.add_widget(self.test_btn)
        self.add_widget(self.move_back_btn)


class About_AppScreen(Screen):
    def __init__(self, manager, **kwargs):
        super().__init__(**kwargs)


        self.add_widget(MDFillRoundFlatButton(
            text='Назад',
            text_color=(1, 1, 1, 1),
            md_bg_color=(120 / 255, 0, 120 / 255),
            pos_hint={'center_x': 0.5, 'center_y': 0.2},
            on_press=manager.switch_to_settings_right,
            size_hint=(0.5, 0.07)
        ))


class Settings_AppScreen(Screen):
    def __init__(self, manager, **kwargs):
        super().__init__(**kwargs)
        self.man = manager

        self.lbl = MDLabel(
            text="Настройки",
            font_style="H3",
            halign="center",
            pos_hint={'center_x': 0.5, 'center_y': 0.85},
            theme_text_color="Custom",
            text_color=(147 / 255, 7 / 255, 200 / 255)
        )


        self.list_letter_button = MDFillRoundFlatButton(
            text="Выйти из аккаунта",
            md_bg_color=(120 / 255, 0, 120 / 255),
            text_color=(1, 1, 1, 1),
            size_hint=(0.5, 0.07),
            on_press=self.leave_a,
            pos_hint={'center_x': 0.5, 'center_y': 0.6}, )

        self.add_widget(MDFillRoundFlatButton(
            text="Изменить данные",
            md_bg_color=(120 / 255, 0, 120 / 255),
            text_color=(1, 1, 1, 1),
            size_hint=(0.5, 0.07),
            on_press=self.man.switch_change_information,
            pos_hint={'center_x': 0.5, 'center_y': 0.7}, ))

        self.about_app = MDFillRoundFlatButton(
            text='О приложении',
            text_color=(1, 1, 1, 1),
            md_bg_color=(120 / 255, 0, 120 / 255),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            on_press=self.man.switch_about_app,
            size_hint=(0.5, 0.07)
        )

        self.back = MDFillRoundFlatButton(
            text="Назад",
            md_bg_color=(120 / 255, 0, 120 / 255),
            text_color=(1, 1, 1, 1),
            size_hint=(0.5, 0.07),
            pos_hint={'center_x': 0.5, 'center_y': 0.2},
            on_press=manager.switch_to_home_right,
        )



        self.add_widget(self.list_letter_button)
        self.add_widget(self.back)
        self.add_widget(self.lbl)
        self.add_widget(self.about_app)
    def leave_a(self, button):
        self.man.switch_to_singup()
        self.man.RegistrationWindow.clear_textinput()
        self.man.SingUpWindow.clear_textinput()
        with open("Email_login_password.txt", "w", encoding='utf-8') as f:
            f.truncate(0)

class Change_information(Screen):
    def __init__(self, manager, **kwargs):
        super().__init__(**kwargs)
        self.man = manager

        self.add_widget(MDLabel(
            text="Изменить данные",
            font_style="H3",
            halign="center",
            pos_hint={'center_x': 0.5, 'center_y': 0.85},
            theme_text_color="Custom",
            text_color=(147 / 255, 7 / 255, 200 / 255)
        ))
        self.add_widget(MDFillRoundFlatButton(
            text="Изменить логин",
            md_bg_color=(120 / 255, 0, 120 / 255),
            text_color=(1, 1, 1, 1),
            size_hint=(0.5, 0.07),
            on_press=self.man.switch_change_name,
            pos_hint={'center_x': 0.5, 'center_y': 0.5}, ))
        self.add_widget(MDFillRoundFlatButton(
            text="Изменить пароль",
            text_color=(1, 1, 1, 1),
            md_bg_color=(120 / 255, 0, 120 / 255),
            size_hint=(0.5, 0.07),
            pos_hint={'center_x': 0.5, 'center_y': 0.7},
            on_press=manager.switch_change_password,

        ))
        self.add_widget(MDFillRoundFlatButton(
            text="Изменить почту",
            text_color=(1, 1, 1, 1),
            md_bg_color=(120 / 255, 0, 120 / 255),
            size_hint=(0.5, 0.07),
            pos_hint={'center_x': 0.5, 'center_y': 0.6},
            on_press=manager.switch_change_mail,
        ))
        self.add_widget(MDFillRoundFlatButton(
            text='Назад',
            text_color=(1, 1, 1, 1),
            md_bg_color=(120 / 255, 0, 120 / 255),
            pos_hint={'center_x': 0.5, 'center_y': 0.2},
            on_press=manager.switch_to_settings_right,
            size_hint=(0.5, 0.07)
        ))
class Change_NameScreen(Screen):
    def __init__(self, manager, **kwargs):
        super().__init__(**kwargs)
        self.man = manager

        self.lbl = MDLabel(
            text="Изменение логина",
            font_style="H3",
            halign="center",
            pos_hint={'center_x': 0.5, 'center_y': 0.85},
            theme_text_color="Custom",
            text_color=(147 / 255, 7 / 255, 200 / 255)
        )

        self.textinputname= MDTextFieldRound(
            hint_text="Новый логин",
            icon_left="key-variant",
            color_active=(1, 1, 1, 1),
            pos_hint={'center_x': 0.5, 'center_y': 0.7},
            normal_color=(120 / 255, 0, 120 / 255),
            line_color=(1, 0, 1, 1),
            size_hint=(0.45, 0.07),
        )
        self.textinputname.bind(focus=manager.change_icon_color)

        self.textinputpassword = MDTextFieldRound(
            hint_text="Ваш пароль",
            icon_left="key-variant",
            color_active=(1, 1, 1, 1),
            pos_hint={'center_x': 0.5, 'center_y': 0.6},
            normal_color=(120 / 255, 0, 120 / 255),
            line_color=(1, 0, 1, 1),
            size_hint=(0.45, 0.07),
        )
        self.textinputpassword.bind(focus=manager.change_icon_color)

        self.change_btn = MDFillRoundFlatButton(
            text='Изменить',
            text_color=(1, 1, 1, 1),
            md_bg_color=(120 / 255, 0, 120 / 255),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            on_press=self.password_check,
            size_hint=(0.5, 0.07)
        )
        self.back = MDFillRoundFlatButton(
            text="Назад",
            md_bg_color=(120 / 255, 0, 120 / 255),
            text_color=(1, 1, 1, 1),
            size_hint=(0.5, 0.07),
            pos_hint={'center_x': 0.5, 'center_y': 0.2},
            on_press=self.man.switch_change_information_rigth,
        )
        self.add_widget(self.lbl)
        self.add_widget(self.textinputname)
        self.add_widget(self.textinputpassword)
        self.add_widget(self.change_btn)
        self.add_widget(self.back)

    def password_check(self,button):
        with open("Email_login_password.txt", "r", encoding='utf-8') as f:
            f = f.readlines()
        if f[2].strip() != self.textinputpassword.text:
            self.pop = Popup(title="Ошибка", content=PopWindow("Неверный пароль", "Продолжить", self.man),
                             size_hint=(None, None), size=(dp(400), dp(400)))
            self.pop.content.btn.bind(on_press=self.pop.dismiss)
            self.pop.open()
        else:
            self.man.db.change_name(f[0].strip(),self.textinputname.text.strip())
            change_current_info([f[0].strip(),self.textinputname.text.strip(),f[2].strip(),f[3].strip()])
            self.man.db.change_name(f[0].strip(), self.textinputname.text)
            change_current_info([f[0].strip(), self.textinputname.text, f[2].strip(), f[3].strip()])
            self.textinputname.text=""
            self.textinputpassword.text=""
            self.man.switch_change_information_rigth()

class Change_passwordScreen(Screen):
    def __init__(self, manager, **kwargs):
        super().__init__(**kwargs)
        self.man = manager

        self.lbl = MDLabel(
            text="Изменение пароля",
            font_style="H3",
            halign="center",
            pos_hint={'center_x': 0.5, 'center_y': 0.85},
            theme_text_color="Custom",
            text_color=(147 / 255, 7 / 255, 200 / 255)
        )

        self.textinputpasswordold = MDTextFieldRound(
            hint_text="Старый пароль",
            icon_left="key-variant",
            color_active=(1, 1, 1, 1),
            pos_hint={'center_x': 0.5, 'center_y': 0.7},
            normal_color=(120 / 255, 0, 120 / 255),
            line_color=(1, 0, 1, 1),
            size_hint=(0.45, 0.07),
        )
        self.textinputpasswordold.bind(focus=manager.change_icon_color)

        self.textinputpassword = MDTextFieldRound(
            hint_text="Новый пароль",
            icon_left="key-variant",
            color_active=(1, 1, 1, 1),
            pos_hint={'center_x': 0.5, 'center_y': 0.6},
            normal_color=(120 / 255, 0, 120 / 255),
            line_color=(1, 0, 1, 1),
            size_hint=(0.45, 0.07),
        )
        self.textinputpassword.bind(focus=manager.change_icon_color)

        self.change_btn = MDFillRoundFlatButton(
            text='Изменить',
            text_color=(1, 1, 1, 1),
            md_bg_color=(120 / 255, 0, 120 / 255),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            on_press=self.password_check,
            size_hint=(0.5, 0.07)
        )
        self.back = MDFillRoundFlatButton(
            text="Назад",
            md_bg_color=(120 / 255, 0, 120 / 255),
            text_color=(1, 1, 1, 1),
            size_hint=(0.5, 0.07),
            pos_hint={'center_x': 0.5, 'center_y': 0.2},
            on_press=self.man.switch_change_information_rigth,
        )


        self.add_widget(self.lbl)
        self.add_widget(self.textinputpasswordold)
        self.add_widget(self.textinputpassword)
        self.add_widget(self.change_btn)
        self.add_widget(self.back)


    def password_check(self,button):
        with open("Email_login_password.txt", "r", encoding='utf-8') as f:
            f = f.readlines()
        if f[2].strip() != self.textinputpasswordold.text:
            self.pop = Popup(title="Ошибка", content=PopWindow("Неверный старый пароль", "Продолжить", self.man),
                             size_hint=(None, None), size=(dp(400), dp(400)))
            self.pop.content.btn.bind(on_press=self.pop.dismiss)
            self.pop.open()
        else:
            self.man.db.change_password(f[0].strip(),self.textinputpassword.text)
            change_current_info([f[0].strip(),f[1].strip(),self.textinputpassword.text,f[3].strip()])
            self.textinputpasswordold.text=""
            self.textinputpassword.text=""
            self.man.switch_change_information_rigth()

class Change_mailScreen(Screen):
    def __init__(self, manager, **kwargs):
        super().__init__(**kwargs)
        self.man = manager

        self.lbl = MDLabel(
            text="Изменение почты",
            font_style="H3",
            halign="center",
            pos_hint={'center_x': 0.5, 'center_y': 0.85},
            theme_text_color="Custom",
            text_color=(147 / 255, 7 / 255, 200 / 255)
        )

        self.textinputmail = MDTextFieldRound(
            hint_text="Другая почта",
            icon_left="key-variant",
            color_active=(1, 1, 1, 1),
            pos_hint={'center_x': 0.5, 'center_y': 0.7},
            normal_color=(120 / 255, 0, 120 / 255),
            line_color=(1, 0, 1, 1),
            size_hint=(0.45, 0.07),
        )
        self.textinputmail.bind(focus=manager.change_icon_color)

        self.textinputpassword = MDTextFieldRound(
            hint_text="Ваш пароль",
            icon_left="key-variant",
            color_active=(1, 1, 1, 1),
            pos_hint={'center_x': 0.5, 'center_y': 0.6},
            normal_color=(120 / 255, 0, 120 / 255),
            line_color=(1, 0, 1, 1),
            size_hint=(0.45, 0.07),
        )
        self.textinputpassword.bind(focus=manager.change_icon_color)

        self.change_btn = MDFillRoundFlatButton(
            text='Изменить',
            text_color=(1, 1, 1, 1),
            md_bg_color=(120 / 255, 0, 120 / 255),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            on_press=self.password_check,
            size_hint=(0.5, 0.07)
        )
        self.back = MDFillRoundFlatButton(
            text="Назад",
            md_bg_color=(120 / 255, 0, 120 / 255),
            text_color=(1, 1, 1, 1),
            size_hint=(0.5, 0.07),
            pos_hint={'center_x': 0.5, 'center_y': 0.2},
            on_press=self.man.switch_change_information_rigth,
        )
        self.add_widget(self.lbl)
        self.add_widget(self.textinputmail)
        self.add_widget(self.textinputpassword)
        self.add_widget(self.change_btn)
        self.add_widget(self.back)

    def password_check(self, button):
        with open("Email_login_password.txt", "r", encoding='utf-8') as f:
            f = f.readlines()
        if f[2].strip() != self.textinputpassword.text:
            self.pop = Popup(title="Ошибка", content=PopWindow("Неверный пароль", "Продолжить", self.man),
                             size_hint=(None, None), size=(dp(400), dp(400)))
            self.pop.content.btn.bind(on_press=self.pop.dismiss)
            self.pop.open()
        else:
            self.man.db.change_mail(f[0].strip(), self.textinputmail.text.strip()())
            change_current_info([f[0].strip(), f[1].strip(),f[2].strip(),self.textinputmail.text.strip()() ])
            self.textinputmail.text = ""
            self.textinputpassword.text = ""
            self.man.switch_change_information_rigth()





class StatisticScreen(Screen):
    def __init__(self, manager, **kwargs):
        super().__init__(**kwargs)
        self.man=manager

        self.add_widget( MDLabel(
            text="Cтатистика слов",
            font_style="H3",
            halign="center",
            pos_hint={'center_x': 0.5, 'center_y': 0.85},
            theme_text_color="Custom",
            text_color=(147 / 255, 7 / 255, 200 / 255)
        ))

        self.add_widget(MDFillRoundFlatButton(
            text="Хорошо усвоенные",
            md_bg_color=(120 / 255, 0, 120 / 255),
            text_color=(1, 1, 1, 1),
            size_hint=(0.5, 0.07),
            pos_hint={'center_x': 0.5, 'center_y': 0.7},
            on_press=self.man.switch_to_statistic_word,
        ))

        self.add_widget(MDFillRoundFlatButton(
            text="Средне усвоенные",
            md_bg_color=(120 / 255, 0, 120 / 255),
            text_color=(1, 1, 1, 1),
            size_hint=(0.5, 0.07),
            pos_hint={'center_x': 0.5, 'center_y': 0.6},
            on_press=self.man.switch_to_statistic_word,
        ))

        self.add_widget(MDFillRoundFlatButton(
            text="Не усвоенные",
            md_bg_color=(120 / 255, 0, 120 / 255),
            text_color=(1, 1, 1, 1),
            size_hint=(0.5, 0.07),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            on_press=self.man.switch_to_statistic_word,
        ))

        self.add_widget(MDFillRoundFlatButton(
            text="Назад",
            md_bg_color=(120 / 255, 0, 120 / 255),
            text_color=(1, 1, 1, 1),
            size_hint=(0.5, 0.07),
            pos_hint={'center_x': 0.5, 'center_y': 0.1},
            on_press=self.man.switch_to_home_right,
        ))

class StatisticWordsScreen(Screen):
    def __init__(self,manager,group_name, **kwargs):
        super().__init__(**kwargs)
        self.man=manager
        self.add_widget(MDLabel(
            text="Слова:",
            font_style="H3",
            halign="center",
            pos_hint={'center_x': 0.5, 'center_y': 0.9},
            theme_text_color="Custom",
            text_color=(147 / 255, 7 / 255, 200 / 255)
        ))

        sv = ScrollView(
            size_hint = (0.7,0.7),
            pos_hint = {'center_x':0.5, 'center_y':0.5},
            bar_color=(147 / 255, 7 / 255, 200 / 255)
        )

        ml = MDList()

        self.words = self.list_words()
        self.man.divide_into_groups()
        for word_ind in self.man.word_groups[group_name]:
            ml.add_widget(ThreeLineListItem(
                text = self.words[word_ind][0].upper() + self.words[word_ind][1:],
                font_style = "H6",
                theme_text_color = 'Custom',
                text_color = (147 / 255, 7 / 255, 200 / 255),
                secondary_text = f"Количество правильных ответов: {self.man.answers_list['correct'][word_ind]}",
                secondary_theme_text_color = 'Custom',
                secondary_text_color=(120 / 255, 0, 120 / 255),
                secondary_font_style ='Body2',
                tertiary_text = f"Количество не правильных ответов: {self.man.answers_list['wrong'][word_ind]}",
                tertiary_theme_text_color = 'Custom',
                tertiary_text_color = (120 / 255, 0, 120 / 255),
                tertiary_font_style ='Body2'
            ))

        self.add_widget(MDFillRoundFlatButton(
            text="Назад",
            md_bg_color=(120 / 255, 0, 120 / 255),
            text_color=(1, 1, 1, 1),
            size_hint=(0.5, 0.07),
            pos_hint={'center_x': 0.5, 'center_y': 0.1},
            on_press=self.man.switch_to_statistic_right,
        ))

        sv.add_widget(ml)
        self.add_widget(sv)


    def list_words(self):
        with open("words.txt", "r", encoding='utf-8') as f:
            words=[word.strip().lower() for word in f.readlines()]
        return words



class TheoryScreen(Screen):
    def __init__(self, manager, **kwargs):
        super().__init__(**kwargs)



        self.back = MDFillRoundFlatButton(
            text="Назад",
            md_bg_color=(120 / 255, 0, 120 / 255),
            text_color=(1, 1, 1, 1),
            size_hint=(0.5, 0.07),
            pos_hint={'center_x': 0.5, 'center_y': 0.2},
            on_press=manager.switch_to_home_right,
        )


class RatingScreen(Screen):
    def __init__(self, manager, **kwargs):
        super().__init__(**kwargs)
        cur_user, rates = manager.db.get_users_rating()
        dataTable = MDDataTable(
            column_data = [
                ('[color=#C042B8][size=24]№[/size][/color]', dp((Window.size[0]/530))*20),
                ("[color=#C042B8][size=24]Имя пользователя[/size][/color]", dp((Window.size[0]/530))*60),
                ("[color=#C042B8][size=24]?[/size][/color]",dp((Window.size[0]/530))*20),

            ],
            row_data = [
                # (
                #     f"[color=#C042B8]{i}[/color]",
                #     f"[color=#C042B8]{name}[/color]",
                #     f"[color=#C042B8]{rates}[/color]",
                # ) for i,name,rates in rates if rates != 0
                (
                        f"[size=20][color=#C042B8]{cur_user[0]}[/size][/color]",
                        f"[size=20][color=#C042B8]{cur_user[1]} (Я)[/size][/color]",
                        f"[size=20][color=#C042B8]{cur_user[2]}[/size][/color]"
                ) for i in range(10)
            ]
        )
        # for i,name,rates in rates:
        #     if rates != 0:
        #         dataTable.row_data.append((
        #             f"[color=#C042B8]{i}[/color]",
        #             f"[color=#C042B8]{name}[/color]",
        #             f"[color=#C042B8]{rates}[/color]",
        #         ))
        # for i in range(10):
        #     dataTable.row_data.append((
        #         f"[color=#C042B8]{i+1}[/color]",
        #         f"[color=#C042B8]aaaa[/color]",
        #         f"[color=#C042B8]bbbb[/color]",
        #     ))
        # dataTable.row_data.append(("","",""))
        # dataTable.row_data.append(("", "", ""))
        # dataTable.rows_num=50
        self.add_widget(dataTable)
        self.add_widget(MDFillRoundFlatButton(
            text="Назад",
            md_bg_color=(120 / 255, 0, 120 / 255),
            text_color=(1, 1, 1, 1),
            size_hint=(0.5, 0.07),
            pos_hint={'center_x': 0.5, 'center_y': 0.1},
            on_press=manager.switch_to_home_right,
        ))


class PracticeScreen(Screen):
    def __init__(self, manager, **kwargs):
        super().__init__(**kwargs)

        self.man = manager

        self.count_right_words_label = MDLabel(
            text="0",
            font_style="H3",
            halign="center",
            pos_hint={"center_x": 0.2, 'center_y': 0.9},
            theme_text_color="Custom",
            text_color=(147 / 255, 7 / 255, 200 / 255)
        )

        self.count_wrong_words_label = MDLabel(
            text="0",
            font_style="H3",
            halign="center",
            pos_hint={"center_x": 0.2, 'center_y': 0.8},
            theme_text_color="Custom",
            text_color=(147 / 255, 7 / 255, 200 / 255)
        )

        self.add_widget(self.count_wrong_words_label)
        self.add_widget(self.count_right_words_label)

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

        self.add_widget(MDFillRoundFlatButton(
            text="Завершить",
            md_bg_color=(120 / 255, 0, 120 / 255),
            text_color=(1, 1, 1, 1),
            size_hint=(0.5, 0.07),
            pos_hint={'center_x': 0.5, 'center_y': 0.2},
            on_press=self.end_practice,
        ))

        self.new_word()
        self.add_word()


    def new_word(self):
        self.count_right_words_label.pos_hint = {"center_x": 0.2 + 0.033*(len(self.count_right_words_label.text) - 1), 'center_y': 0.9}
        self.count_wrong_words_label.pos_hint = {"center_x": 0.2 + 0.033*(len(self.count_wrong_words_label.text) - 1), 'center_y': 0.8}

        self.man.divide_into_groups()

        if self.man.word_groups['new']:
            self.word_ind = choice(self.man.word_groups['new'])
        elif self.man.word_groups['red']:
            self.word_ind = choice(self.man.word_groups['red'])
        elif self.man.word_groups['yellow']:
            self.word_ind = choice(self.man.word_groups['yellow'])
        else:
            self.word_ind = choice(self.man.word_groups['green'])

        with open("words.txt", "r", encoding='utf-8') as f:
            temp = f.readlines()[self.word_ind]
        self.word = temp.strip()

        self.accented = []
        for i in range(len(self.word)):
            if self.word[i] in VOWELS:
                self.accented.append(i)

        self.word = self.word.upper()
        self.is_faild = 0

    def end_practice(self, button):
        self.give_answers_list()
        self.man.switch_to_training_right()

    def give_answers_list(self):
        with open("answers_list_file.txt", "w", encoding='utf-8') as f:
            f.write("|".join(list(map(str, self.man.answers_list["correct"]))) + "\n")
            f.write("|".join(list(map(str, self.man.answers_list["wrong"])))+"\n")
            if sum(self.man.answers_list["correct"])+sum(self.man.answers_list["wrong"])>=100:
                f.write(str(round(sum(self.man.answers_list["correct"])/(sum(self.man.answers_list["correct"])+sum(self.man.answers_list["wrong"])),2)))
            else:
                f.write("0")


    def add_word(self):
        self.list_letter_button = [MDFillRoundFlatButton(text=str(letter),
                                                         font_size=30,
                                                         size_hint=(None, None),
                                                         size=(10, 10),
                                                         md_bg_color=(120 / 255, 0, 120 / 255),
                                                         md_bg_color_disabled=(120 / 255, 0, 120 / 255))
                                   for letter in self.word]

        for i in range(len(self.list_letter_button)):
            if self.list_letter_button[i].text in VOWELS:
                if self.accented.count(i) > 0:
                    self.list_letter_button[i].accented = True
                else:
                    self.list_letter_button[i].accented = False
                self.list_letter_button[i].bind(on_press=self.check_variable)

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
            space_btw_rows = 0.5 / (num_rows + 1)
            for i in range(num_rows):
                temp = self.placement_in_row(5)
                for j in range(5):
                    self.list_letter_button[i * 5 + j].pos_hint = {'center_x': temp[j],
                                                                   'center_y': 0.7 - space_btw_rows * (i + 1)}
        for button in self.list_letter_button:
            self.add_widget(button)

    def check_variable(self, button):
        if not button.accented is None:
            if button.accented:
                button.md_bg_color = (0, 200 / 255, 0, 1)
                for btn in self.list_letter_button:
                    btn.accented = None
                Clock.schedule_once(self.remove_words, 0.5)  # Таймер
            else:
                button.md_bg_color = (200 / 255, 0, 0, 1)
                if self.is_faild == 0:
                    self.count_wrong_words_label.text = str(int(self.count_wrong_words_label.text) + 1)
                    self.man.answers_list['wrong'][self.word_ind] += 1
                self.is_faild = 1

    def remove_words(self, value):
        if self.is_faild == 0:
            self.count_right_words_label.text = str(int(self.count_right_words_label.text) + 1)
            self.man.answers_list['correct'][self.word_ind] += 1
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
        self.man = manager

        self.words_check_box = dict()

        self.add_widget(MDLabel(
            text="В одном из приведённых ниже слов допущена ошибка в постановке ударения: "
                 "НЕВЕРНО выделена буква, обозначающая ударный гласный звук. "
                 "Нажмите на это слово.",
            font_style="H6",
            halign="center",
            pos_hint={'center_x': 0.5, 'center_y': 0.82},
            theme_text_color="Custom",
            text_color=(147 / 255, 7 / 255, 200 / 255),
            size_hint=(0.8, 1)
        ))

        self.add_widget(MDFillRoundFlatButton(
            text="Завершить",
            md_bg_color=(120 / 255, 0, 120 / 255),
            text_color=(1, 1, 1, 1),
            size_hint=(0.3, 0.07),
            pos_hint={'center_x': 0.32, 'center_y': 0.15},
            on_press=self.end_test,
        ))

        self.add_widget(MDFillRoundFlatButton(
            text="Ответить",
            md_bg_color=(120 / 255, 0, 120 / 255),
            text_color=(1, 1, 1, 1),
            size_hint=(0.3, 0.07),
            pos_hint={'center_x': 0.68, 'center_y': 0.15},
            on_press=self.check_answer,
        ))

    def words_generation(self):
        with open("words.txt", "r", encoding='utf-8') as f:
            words = f.readlines()
        shuffle(words)
        words = words[:5]

        for i in range(len(words)):
            words[i]=words[i].strip()

        wrong_word_ind = randint(0,4)
        ind_lower_vowels = []
        for i in range (len(words[wrong_word_ind])):
            if words[wrong_word_ind][i] in VOWELS.upper():
                ind_lower_vowels.append(i)

        rnd_ind = choice(ind_lower_vowels)
        words[wrong_word_ind] = words[wrong_word_ind][:rnd_ind].lower() + words[wrong_word_ind][rnd_ind].upper() + words[wrong_word_ind][rnd_ind+1:].lower()

        words_with_answer = dict()

        for i in range(len(words)):
            is_wrong = False
            if i == wrong_word_ind:
                is_wrong = True

            words_with_answer[
                MDLabel(
                    text=words[i],
                    font_style="H6",
                    halign="center",
                    pos_hint={'center_x': 0.53, 'center_y': i * 0.07 + 0.33},
                    theme_text_color="Custom",
                    text_color=(147 / 255, 7 / 255, 200 / 255),
                    size_hint=(0.4, 1)
                )
            ] = is_wrong
        return words_with_answer

    def add_on_screen(self):
        self.clean_screen()

        self.words_check_box = dict()
        self.words_with_answers = self.words_generation()
        for i in range(5):
            self.words_check_box[list(self.words_with_answers.keys())[i]] = \
                MDCheckbox(
                    group='group',
                    size_hint=(4, 0.07),
                    pos_hint={'center_x': 0.32, 'center_y': i * 0.07 + 0.33}
                )
            self.words_check_box[list(self.words_with_answers.keys())[i]].selected_color = (147 / 255, 7 / 255, 200 / 255)
            self.add_widget(list(self.words_with_answers.keys())[i])
            self.add_widget(self.words_check_box[list(self.words_with_answers.keys())[i]])

    def clean_screen(self):
        for word, check_box in self.words_check_box.items():
            self.remove_widget(word)
            self.remove_widget(check_box)

    def check_answer(self, button):
        has_active = False
        for check_box in self.words_check_box.values():
            if check_box.active == True:
                has_active = True
        if has_active:
            for word, check_box in self.words_check_box.items():
                if self.words_with_answers[word]:
                    word.text_color = (0, 200 / 255, 0, 1)
                if not self.words_with_answers[word] and check_box.active == True:
                    word.text_color = (200 / 255, 0, 0, 1)
            Clock.schedule_once(self.man.switch_to_test, 1)  # Таймер

    def end_test(self, button):
        has_active = False
        for check_box in self.words_check_box.values():
            if check_box.active== True:
                has_active=True
        if has_active:
            for word, check_box in self.words_check_box.items():
                if self.words_with_answers[word]:
                    word.text_color = (0, 200 / 255, 0, 1)
                if not self.words_with_answers[word] and check_box.active == True:
                    word.text_color = (200 / 255, 0, 0, 1)
            Clock.schedule_once(self.man.switch_to_training_right, 1)  # Таймер
        else:
            self.man.switch_to_training_right()



