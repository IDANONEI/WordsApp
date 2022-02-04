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
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout

from random import randint, choice
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton, MDRoundFlatButton, MDRaisedButton, MDFillRoundFlatButton, \
    MDIconButton, MDFloatingActionButton
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.textfield import MDTextFieldRound

from Regisration import PopWindow

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
            on_press=self.man.switch_to_training_left,
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
            on_press=manager.switch_to_home_right,
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
            pos_hint={'center_x': 0.5, 'center_y': 0.4}, )
        self.password = MDFillRoundFlatButton(
            text="Сменить пароль",
            text_color=(1, 1, 1, 1),
            md_bg_color=(120 / 255, 0, 120 / 255),
            size_hint=(0.5, 0.07),
            pos_hint={'center_x': 0.5, 'center_y': 0.6},
            on_press=manager.switch_change_password,
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
        self.add_widget(self.password)
        self.add_widget(self.back)
        self.add_widget(self.lbl)
    def leave_a(self, button):
        self.man.swith_to_singup()
        with open("Email_login_password.txt", "w", encoding='utf-8') as f:
            f.truncate(0)





class Change_passwordScreen(Screen):
    def __init__(self, manager, **kwargs):
        super().__init__(**kwargs)
        self.man = manager

        self.lbl = MDLabel(
            text="Смена пароля",
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
            pos_hint={'center_x': 0.5, 'center_y': 0.46},
            normal_color=(120 / 255, 0, 120 / 255),
            line_color=(1, 0, 1, 1),
            size_hint=(0.45, 0.07),
        )
        self.textinputpasswordold.bind(focus=manager.change_icon_color)

        self.textinputpassword = MDTextFieldRound(
            hint_text="Новый пароль",
            icon_left="key-variant",
            color_active=(1, 1, 1, 1),
            pos_hint={'center_x': 0.5, 'center_y': 0.34},
            normal_color=(120 / 255, 0, 120 / 255),
            line_color=(1, 0, 1, 1),
            size_hint=(0.45, 0.07),
        )
        self.textinputpassword.bind(focus=manager.change_icon_color)

        self.change_btn = MDFillRoundFlatButton(
            text='Сменить',
            text_color=(1, 1, 1, 1),
            md_bg_color=(120 / 255, 0, 120 / 255),
            pos_hint={'center_x': 0.5, 'center_y': 0.22},
            on_press=self.password_check,
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


        self.add_widget(self.lbl)
        self.add_widget(self.textinputpasswordold)
        self.add_widget(self.textinputpassword)
        self.add_widget(self.change_btn)
        self.add_widget(self.back)


    def password_check(self,button):
        with open("Email_login_password.txt", "r", encoding='utf-8') as f:
            f.readlines()
        if f[3].strip()!= self.textinputpasswordold:
            self.pop = Popup(title="Ошибка", content=PopWindow("Неверный старый пароль", "Продолжить", self.man),
                             size_hint=(None, None), size=(dp(400), dp(400)))
            self.pop.content.btn.bind(on_press=self.pop.dismiss)
            self.pop.open()


    def change_password(self,button):
        with open("Email_login_password.txt", "w", encoding='utf-8') as f:
            f.truncate(0)








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
            if self.word[i] in vowels:
                self.accented.append(i)

        self.word = self.word.upper()
        self.is_faild = 0

    def end_practice(self, button):
        self.give_answers_list()
        self.man.switch_to_training_right()

    def give_answers_list(self):
        with open("answers_list_file.txt", "w", encoding='utf-8') as f:
            f.write("|".join(list(map(str, self.man.answers_list["correct"]))) + "\n")
            f.write("|".join(list(map(str, self.man.answers_list["wrong"]))))

    def add_word(self):
        self.list_letter_button = [MDFillRoundFlatButton(text=str(letter),
                                                         font_size=30,
                                                         size_hint=(None, None),
                                                         size=(10, 10),
                                                         md_bg_color=(120 / 255, 0, 120 / 255),
                                                         md_bg_color_disabled=(120 / 255, 0, 120 / 255))
                                   for letter in self.word]

        for i in range(len(self.list_letter_button)):
            if self.list_letter_button[i].text in vowels:
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
            # on_press=,
        ))

        answers = dict()
        #{key: value}
        random_word_ind = randint(0,317)
        with open("words.txt", "r", encoding='utf-8') as f:
            temp = f.readlines()[random_word_ind]
        self.word = temp.strip()

        check_box_list = []
        for i in range(5):
            check_box_list.append(
                MDCheckbox(
                    group='group',
                    size_hint=(0.1, 0.1),
                    pos_hint={'center_x': 0.32, 'center_y': i * 0.1 + 0.3})
            )
            self.add_widget(check_box_list[i])



    def end_test(self, button):
        self.man.switch_to_training_right()
