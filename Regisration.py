
from kivy.metrics import dp
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextFieldRound

from Constans import NUM_WORDS

def change_current_info(info):
    with open("Email_login_password.txt", "w", encoding='utf-8') as f:
        f.write(str(info[0]) + "\n")
        f.write(str(info[1]) + "\n")
        f.write(str(info[2]) + "\n")
        f.write(str(info[3]) + "\n")

class SingUpScreen(Screen):
    def __init__(self, manager, **kwargs):
        super(SingUpScreen, self).__init__(**kwargs)

        self.man = manager

        self.lbl = MDLabel(
            text="СВЁКЛА",
            font_style="H3",
            halign="center",
            pos_hint={'center_x': 0.5, 'center_y': 0.85},
            theme_text_color="Custom",
            text_color=(100 / 255, 0 / 255, 100 / 255)
        )
        self.lbl.font_size = 65

        self.lbl2 = MDLabel(
            text="ВХОД",
            font_style="H6",
            halign="center",
            font_size=25,
            pos_hint={'center_x': 0.5, 'center_y': 0.75},
            theme_text_color="Custom",
            text_color=(100 / 255, 0 / 255, 100 / 255)
        )
        self.lbl2.font_size=30

        self.textinputlogin = MDTextFieldRound(
            hint_text="Логин или почта",
            icon_left="email",
            color_active=(1, 1, 1, 1),
            pos_hint={'center_x': 0.5, 'center_y': 0.6},
            normal_color=(120 / 255, 0, 120 / 255),
            line_color=(1 / 255, 1 / 255, 1 / 255, 1),
            size_hint=(0.45, 0.07),
        )
        self.textinputlogin.text = ""


        self.textinputlogin.bind(focus=manager.change_icon_color)

        self.textinputpassword = MDTextFieldRound(
            hint_text="Введите пароль",
            icon_left="key-variant",
            icon_left_color=(0, 0, 0, 1),
            color_active=(1, 1, 1, 1),
            pos_hint={'center_x': 0.5, 'center_y': 0.50},
            normal_color=(120 / 255, 0, 120 / 255),
            line_color=(1, 0, 1, 1),
            size_hint=(0.45, 0.07),
        )

        self.textinputpassword.bind(focus=manager.change_icon_color)

        self.sing_up = MDFillRoundFlatButton(text='Авторизоваться',
                                             text_color=(1, 1, 1, 1),
                                             md_bg_color=(120 / 255, 0, 120 / 255),
                                             pos_hint={'center_x': 0.5, 'center_y': 0.38},
                                             on_press=self.check_user,
                                             size_hint=(0.5, 0.07)
                                             )

        self.registrate = MDFillRoundFlatButton(
            text='Регистрация',
            text_color=(1, 1, 1, 1),
            md_bg_color=(120 / 255, 0, 120 / 255),
            pos_hint={'center_x': 0.5, 'center_y': 0.22},
            on_press=manager.switch_to_registration,
            size_hint=(0.5, 0.07)
        )
        self.forgotpassword = MDFillRoundFlatButton(
            text='Забыл(а) логин или пароль',
            text_color=(1, 1, 1, 1),
            md_bg_color=(120 / 255, 0, 120 / 255),
            pos_hint={'center_x': 0.5, 'center_y': 0.12},
            on_press=manager.switch_to_forgot_password,
            size_hint=(0.5, 0.07)
        )

        self.add_widget(self.lbl)
        self.add_widget(self.lbl2)
        self.add_widget(self.textinputlogin)
        self.add_widget(self.textinputpassword)
        self.add_widget(self.sing_up)
        self.add_widget(self.registrate)
        self.add_widget(self.forgotpassword)



    def check_user(self, button):
        st = self.textinputlogin.text
        st = st.strip()
        if self.man.db.check_not_existing_user(st):
            self.pop = Popup(
                title="Ошибка",
                content=PopWindow("Неверный логин или пароль", "Продолжить", self.man),
                separator_color=(147 / 255, 7 / 255, 200 / 255),
                title_color=(147 / 255, 7 / 255, 200 / 255),
                size_hint=(0.5, 0.5))
            self.pop.content.btn.bind(on_press=self.pop.dismiss)
            self.pop.open()

        elif self.man.db.check_user(st, self.textinputpassword.text):
            change_current_info(self.man.db.user_info_l_or_e(self.textinputlogin.text))
            with open("Email_login_password.txt", "r", encoding='utf-8') as f:
                info = f.readlines()
            self.man.db.take_answers_db(int(info[0].strip()))
            self.man.answers_list = self.man.db.take_answer()
            self.man.switch_to_home_left()

        else:
            self.pop = Popup(
                title="Ошибка",
                content=PopWindow("Неверный логин или пароль", "Продолжить", self.man),
                separator_color=(147 / 255, 7 / 255, 200 / 255),
                title_color=(147 / 255, 7 / 255, 200 / 255),
                size_hint=(0.5, 0.5),
            )
            self.pop.content.btn.bind(on_press=self.pop.dismiss)
            self.pop.open()

    def clear_textinput(self):
        self.textinputpassword.text = ""
        self.textinputlogin.text = ""





class PopWindow(FloatLayout):
    def __init__(self, lbl_text, btn_text, manager, **kwargs):
        super().__init__(**kwargs)
        self.man = manager

        self.lbl = MDLabel(
            text=lbl_text,
            font_style="H6",
            halign="center",
            pos_hint={"x": 0.2, "y": 0.7},
            theme_text_color="Custom",
            text_color=(100 / 255, 0 / 255, 100 / 255),
            size_hint=[0.6, 0.2]
        )
        self.lbl.font_size=15

        self.btn = MDFillRoundFlatButton(
            text=btn_text,
            text_color=(1, 1, 1, 1),
            md_bg_color=(120 / 255, 0, 120 / 255),
            pos_hint={"x": 0.1, "y": 0.2},
            size_hint=[0.8, 0.2]
        )

        self.add_widget(self.lbl)
        self.add_widget(self.btn)


class ForgotPasswordScreen(Screen):
    def __init__(self, manager, **kwargs):
        self.man = manager

        super(ForgotPasswordScreen, self).__init__(**kwargs)

        self.forgot_lbl = MDLabel(
            text="Забыли пароль?",
            font_style="H6",
            halign="center",
            pos_hint={'center_x': 0.5, 'center_y': 0.75},
            theme_text_color="Custom",
            text_color=(100 / 255, 0 / 255, 100 / 255)
        )
        self.forgot_lbl.font_size=45

        self.lbl1 = MDLabel(
            text="Пожалуйста, введите адрес электронной почты.Вы получите код для изменения пароля.",
            font_style="H6",
            halign="center",
            pos_hint={'center_x': 0.5, 'center_y': 0.62},
            theme_text_color="Custom",
            text_color=(147 / 255, 7 / 255, 200 / 255),
            size_hint=(0.6, 1)
        )

        self.mail = MDTextFieldRound(
            hint_text="Введите почту",
            icon_left="email",
            color_active=(1, 1, 1, 1),
            pos_hint={'center_x': 0.5, 'center_y': 0.45},
            normal_color=(120 / 255, 0, 120 / 255),
            line_color=(1, 0, 1, 1),
            size_hint=(0.45, 0.07),
        )

        self.mail.bind(focus=manager.change_icon_color)

        self.btn = MDFillRoundFlatButton(
            text='Восстановить',
            text_color=(1, 1, 1, 1),
            md_bg_color=(120 / 255, 0, 120 / 255),
            pos_hint={'center_x': 0.5, 'center_y': 0.35},
            on_press=self.restore,
            size_hint=(0.5, 0.07)
        )
        self.back_btn = MDFillRoundFlatButton(
            text='Назад',
            text_color=(1, 1, 1, 1),
            md_bg_color=(120 / 255, 0, 120 / 255),
            pos_hint={'center_x': 0.5, 'center_y': 0.20},
            on_press=manager.switch_to_singup,
            size_hint=(0.5, 0.07)
        )

        self.add_widget(self.forgot_lbl)
        self.add_widget(self.lbl1)
        self.add_widget(self.mail)
        self.add_widget(self.btn)
        self.add_widget(self.back_btn)

    def restore(self, button):
        st_user = self.mail.text

        if self.man.db.check_not_existing_user(st_user):
            self.pop = Popup(title="Ошибка", content=PopWindow(
                "Неверная почта", "Продолжить", self.man), size_hint=(None, None), size=(dp(400), dp(400)))
            self.pop.content.btn.bind(on_press=self.pop.dismiss)
            self.pop.open()


class RegistrationScreen(Screen):
    def __init__(self, manager, **kwargs):

        self.man = manager

        super(RegistrationScreen, self).__init__(**kwargs)

        self.lbl = MDLabel(
            text="Регистрация",
            font_style="H6",
            halign="center",
            pos_hint={'center_x': 0.5, 'center_y': 0.85},
            theme_text_color="Custom",
            text_color=(100 / 255, 0 / 255, 100 / 255)
        )

        self.lbl.font_size=45

        self.textinputlogin = MDTextFieldRound(
            hint_text="Введите логин",
            icon_left="account-box",
            color_active=(1, 1, 1, 1),
            pos_hint={'center_x': 0.5, 'center_y': 0.7},
            normal_color=(120 / 255, 0, 120 / 255),
            line_color=(1, 0, 1, 1),
            size_hint=(0.45, 0.07),
        )

        self.textinputlogin.bind(focus=manager.change_icon_color)

        self.textinputmail = MDTextFieldRound(
            hint_text="Введите почту",
            icon_left="email",
            color_active=(1, 1, 1, 1),
            pos_hint={'center_x': 0.5, 'center_y': 0.58},
            normal_color=(120 / 255, 0, 120 / 255),
            line_color=(1, 0, 1, 1),
            size_hint=(0.45, 0.07),
        )

        self.textinputmail.bind(focus=manager.change_icon_color)

        self.textinputpassword = MDTextFieldRound(
            hint_text="Придумайте пароль",
            icon_left="key-variant",
            color_active=(1, 1, 1, 1),
            pos_hint={'center_x': 0.5, 'center_y': 0.46},
            normal_color=(120 / 255, 0, 120 / 255),
            line_color=(1, 0, 1, 1),
            size_hint=(0.45, 0.07),
        )
        self.textinputpassword.bind(focus=manager.change_icon_color)

        self.textinputpasswordtoo = MDTextFieldRound(
            hint_text="Повторите пароль",
            icon_left="key-variant",
            color_active=(1, 1, 1, 1),
            pos_hint={'center_x': 0.5, 'center_y': 0.34},
            normal_color=(120 / 255, 0, 120 / 255),
            line_color=(1, 0, 1, 1),
            size_hint=(0.45, 0.07),
        )
        self.textinputpasswordtoo.bind(focus=manager.change_icon_color)

        self.reg_btn = MDFillRoundFlatButton(
            text='Регистрация',
            text_color=(1, 1, 1, 1),
            md_bg_color=(120 / 255, 0, 120 / 255),
            pos_hint={'center_x': 0.5, 'center_y': 0.22},
            on_press=self.check_reg,
            size_hint=(0.5, 0.07)
        )
        self.back_btn = MDFillRoundFlatButton(
            text='Назад', text_color=(1, 1, 1, 1),
            md_bg_color=(120 / 255, 0, 120 / 255),
            pos_hint={'center_x': 0.5, 'center_y': 0.12},
            on_press=manager.switch_to_singup,
            size_hint=(0.5, 0.07)
        )

        self.add_widget(self.lbl)
        self.add_widget(self.textinputlogin)
        self.add_widget(self.textinputmail)
        self.add_widget(self.textinputpassword)
        self.add_widget(self.textinputpasswordtoo)
        self.add_widget(self.reg_btn)
        self.add_widget(self.back_btn)

    def check_reg(self, button):
        st_user = self.textinputlogin.text
        st_user = st_user.strip()
        st_mail = self.textinputmail.text
        if self.textinputpassword.text != self.textinputpasswordtoo.text or self.textinputpassword.text == "":
            self.pop = Popup(title="Ошибка", content=PopWindow("Неверный повтор пароля", "Продолжить", self.man),
                             size_hint=(None, None), size=(dp(400), dp(400)))
            self.pop.content.btn.bind(on_press=self.pop.dismiss)
            self.pop.open()

        elif self.textinputlogin.text == "":
            self.pop = Popup(title="Ошибка", content=PopWindow("Логин обязательное поле", "Продолжить", self.man),
                             size_hint=(None, None), size=(dp(400), dp(400)))
            self.pop.content.btn.bind(on_press=self.pop.dismiss)
            self.pop.open()

        elif self.textinputmail.text == "":
            self.pop = Popup(title="Ошибка", content=PopWindow("Почта обязательное поле", "Продолжить", self.man),
                             size_hint=(None, None), size=(dp(400), dp(400)))
            self.pop.content.btn.bind(on_press=self.pop.dismiss)
            self.pop.open()

        elif self.man.db.check_mail(st_mail):
            self.pop = Popup(title="Ошибка",
                             content=PopWindow("Пользователь с такой почтой уже существует", "Продолжить", self.man),
                             size_hint=(None, None), size=(dp(400), dp(400)))
            self.pop.content.btn.bind(on_press=self.pop.dismiss)
            self.pop.open()
        elif self.man.db.check_bad_name(self.textinputlogin.text):
            self.pop = Popup(title="Ошибка", content=PopWindow("Такой логин занят", "Продолжить", self.man),
                             size_hint=(None, None), size=(dp(400), dp(400)))
            self.pop.content.btn.bind(on_press=self.pop.dismiss)
            self.pop.open()

        elif self.man.db.check_not_existing_user(st_user):
            #TODO конект при регистрации
            self.man.db.user_reg(st_user, self.textinputpassword.text, self.textinputmail.text)
            change_current_info(self.man.db.user_info_l_or_e(self.textinputlogin.text))
            with open("answers_list_file.txt", "w", encoding='utf-8') as f:
                f.write(("0|" * NUM_WORDS)[:-1] + "\n")
                f.write(("0|" * NUM_WORDS)[:-1])
            #self.manager.answers_list()
            self.man.answers_list = self.man.db.take_answer()
            self.man.switch_to_home_left()
        else:
            self.pop = Popup(title="Ошибка", content=PopWindow("Такой логин занят", "Продолжить", self.man),
                             size_hint=(None, None), size=(dp(400), dp(400)))
            self.pop.content.btn.bind(on_press=self.pop.dismiss)
            self.pop.open()

    def clear_textinput(self):
        self.textinputlogin.text = ""
        self.textinputmail.text = ""
        self.textinputpassword.text = ""
        self.textinputpasswordtoo.text = ""
