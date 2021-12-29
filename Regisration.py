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
from kivymd.uix.textfield import MDTextFieldRound



class RegistrationManager(ScreenManager):
    def __init__(self, db, **kwargs):
        super(RegistrationManager, self).__init__(**kwargs)

        self.db = db

        self.SingUpWindow=SingUpScreen(self, name="SingUp")
        self.ForgotPasswordWindow=ForgotPasswordScreen(self, name="ForgotPassword")
        self.RegistrationWindow=RegistrationScreen(self, name="Registration")
        self.HomeWindow=HomeScreen(self,name="Home")

        self.add_widget(self.SingUpWindow)
        self.add_widget(self.ForgotPasswordWindow)
        self.add_widget(self.RegistrationWindow)
        self.add_widget(self.HomeWindow)

    def switch_to_registration(self,button):
        self.switch_to(self.RegistrationWindow, direction = 'left')

    def switch_to_forgot_password(self, button):
        self.switch_to(self.ForgotPasswordWindow, direction='left')

    def switch_to_home(self):
        self.switch_to(self.HomeWindow, direction='left')

    def swith_to_singup(self, button):
        self.switch_to(self.SingUpWindow, direction = 'right')

    def cleen_text(self, instance,value):
        if instance.text == "Логин":
            if value:
                instance.text = ""
            else:
                instance.foreground_color = (192/255, 192/255, 192/255, 1)




class SingUpScreen (Screen):
    def __init__(self, manager, **kwargs):
        super(SingUpScreen, self).__init__(**kwargs)

        self.man = manager

        self.lbl = Label(text="СВЁКЛА", font_size=50 , color=(147/255, 7/255, 200/255))
        self.lbl2 = Label(text="Вход", font_size=25,color=(147/255, 7/255, 200/255))

        # self.textinputlogin=TextInput(text="Логин", multiline = False)

        self.textinputlogin = MDTextFieldRound(
            hint_text="Логин или почта",
            icon_left="email",

            color_active=(1, 1, 1, 1),
            # pos_hint = {'center_x':0.5, 'center_y':0.55},
            normal_color=(120/255, 0, 120/255),
            line_color=(1/255, 1/255, 1/255, 1),
            # size_hint = (0.5,0.05),
        )


        # self.textinputlogin.bind(focus=manager.cleen_text)

        self.textinputpassword =MDTextFieldRound(
            hint_text="Введите пароль",
            icon_left="key-variant",
            color_active=(1, 1, 1, 1),
            # pos_hint={'center_x': 0.5, 'center_y': 0.45},
            normal_color=(120/255, 0, 120/255),
            line_color=(1, 0, 1, 1),
            # size_hint=(0.5, 0.05),
        )

        # self.textinputpassword = TextInput(text="Пароль", multiline=False)
        self.sing_up=MDFillRoundFlatButton(text='Авторизоваться',text_color=(1, 1, 1, 1), md_bg_color=(120/255, 0, 120/255), pos_hint={'center_x': 0.5},on_press = self.check_user)

        self.registrate=MDFillRoundFlatButton(text='Регистрация',text_color=(1, 1,1, 1), md_bg_color=(120/255, 0, 120/255), pos_hint={'center_x': 0.5}, on_press = manager.switch_to_registration)
        self.forgotpassword = MDFillRoundFlatButton(text='Забыл(а) логин или пароль',text_color=(1, 1, 1, 1), md_bg_color=(120/255, 0, 120/255), pos_hint={'center_x': 0.5}, on_press=manager.switch_to_forgot_password)

        self.boxl = BoxLayout(orientation='vertical', size_hint=[.6, 0.6], spacing=20)
        self.anchLayout = AnchorLayout(anchor_x='center', anchor_y='center')

        self.boxl.add_widget(self.lbl)
        self.boxl.add_widget(self.lbl2)

        self.boxl.add_widget(self.textinputlogin)
        self.boxl.add_widget(self.textinputpassword)

        self.boxl.add_widget(self.sing_up)
        self.boxl.add_widget(self.registrate)
        self.boxl.add_widget(self.forgotpassword)

        self.anchLayout.add_widget(self.boxl)
        self.add_widget(self.anchLayout)

    def check_user(self, button):
        st = self.textinputlogin.text
        st = st.lower()
        if self.man.db.check_existing_user(st):
            self.pop = Popup(title="Ошибка", content=PopWindow("Неверный логин или пароль", "Продолжить", self.man),size_hint=(None, None), size=(dp(400), dp(400)))
            self.pop.open()

        elif self.man.db.check_user(st, self.textinputpassword.text):
            self.man.switch_to_home()
        else:
            self.pop = Popup(title = "Ошибка", content = PopWindow("Неверный логин или пароль", "Продолжить",self.man), size_hint = (None, None), size = (dp(400), dp(400)))
            self.pop.open()



class PopWindow(FloatLayout):
    def __init__(self, lbl_text, btn_text,manager, **kwargs):
        super().__init__(**kwargs)
        self.man=manager
        self.lbl = Label(text = lbl_text, size_hint=[0.6, 0.2], pos_hint={"x": 0.2, "top": 1})
        self.btn = Button(text = btn_text, size_hint=[0.8, 0.2], pos_hint={"x": 0.1, "y": 0.2})


        self.add_widget(self.lbl)
        self.add_widget(self.btn)


class ForgotPasswordScreen(Screen):
    def __init__(self, manager,  **kwargs):
        super(ForgotPasswordScreen, self).__init__(**kwargs)

        self.forgot_lbl = Label(text="Забыли пароль?", font_size=30,color=(147/255, 7/255, 200/255))
        self.lbl1 = Label(text="Пожалуйста, введите адрес электронной почты.", font_size=20,color=(120/255, 0, 120/255))
        self.lbl2 = Label(text="Вы получите код для изменения пароля", font_size=20,color=(120/255, 0, 120/255))


        self.mail= MDTextFieldRound(
            hint_text="Введите почту",
            icon_left="email",
            color_active=(1, 1, 1, 1),
            # pos_hint={'center_x': 0.5, 'center_y': 0.45},
            normal_color=(120/255, 0, 120/255),
            line_color=(1, 0, 1, 1),
            # size_hint=(0.5, 0.05),
        )

        self.btn=MDFillRoundFlatButton(text='Восстановить',text_color=(1, 1, 1, 1), md_bg_color=(120/255, 0, 120/255), pos_hint={'center_x': 0.5})
        self.back_btn = MDFillRoundFlatButton(text='Назад',text_color=(1, 1, 1, 1), md_bg_color=(120/255, 0, 120/255), pos_hint={'center_x': 0.5}, on_press=manager.swith_to_singup)

        self.boxl=BoxLayout(orientation='vertical', size_hint= [.6,0.6], spacing = 20)
        self.anchLayout=AnchorLayout(anchor_x = 'center', anchor_y = 'center')

        self.boxl.add_widget(self.forgot_lbl)
        self.boxl.add_widget(self.lbl1)
        self.boxl.add_widget(self.lbl2)
        self.boxl.add_widget(self.mail)
        self.boxl.add_widget(self.btn)
        self.boxl.add_widget(self.back_btn)

        self.anchLayout.add_widget(self.boxl)
        self.add_widget(self.anchLayout)

class RegistrationScreen(Screen):
    def __init__(self, manager,  **kwargs):


        self.man = manager

        super(RegistrationScreen, self).__init__(**kwargs)
        self.lbl = Label(text="Регистрация", font_size=50,color=(147/255, 7/255, 200/255))

        self.textinputlogin=MDTextFieldRound(
            hint_text="Введите логин",
            icon_left="account-box",
            color_active=(1, 1, 1, 1),
            # pos_hint={'center_x': 0.5, 'center_y': 0.45},
            normal_color=(120/255, 0, 120/255),
            line_color=(1, 0, 1, 1),
            # size_hint=(0.5, 0.05),
        )

        self.textinputmail = MDTextFieldRound(
            hint_text="Введите почту",
            icon_left="email",
            color_active=(1, 1, 1, 1),
            # pos_hint={'center_x': 0.5, 'center_y': 0.45},
            normal_color=(120/255, 0, 120/255),
            line_color=(1, 0, 1, 1),
            # size_hint=(0.5, 0.05),
        )

        self.textinputpassword=MDTextFieldRound(
            hint_text="Придумайте пароль",
            icon_left="key-variant",
            color_active=(1, 1, 1, 1),
            # pos_hint={'center_x': 0.5, 'center_y': 0.45},
            normal_color=(120/255, 0, 120/255),
            line_color=(1, 0, 1, 1),
            # size_hint=(0.5, 0.05),
        )

        self.textinputpasswordtoo=MDTextFieldRound(
            hint_text="Повторите пароль",
            icon_left="key-variant",
            color_active=(1, 1, 1, 1),
            # pos_hint={'center_x': 0.5, 'center_y': 0.45},
            normal_color=(120/255, 0, 120/255),
            line_color=(1, 0, 1, 1),
            # size_hint=(0.5, 0.05),
        )

        self.reg_btn=MDFillRoundFlatButton(text='Регистрация',text_color=(1, 1, 1, 1), md_bg_color=(120/255, 0, 120/255), pos_hint={'center_x': 0.5},on_press = self.check_reg)
        self.back_btn=MDFillRoundFlatButton(text='Назад',text_color=(1, 1, 1, 1), md_bg_color=(120/255, 0, 120/255), pos_hint={'center_x': 0.5},on_press = manager.swith_to_singup)

        self.boxl=BoxLayout(orientation='vertical', size_hint= [.6,0.6], spacing = 10)
        self.anchLayout=AnchorLayout(anchor_x = 'center', anchor_y = 'center')

        self.boxl.add_widget(self.lbl)
        self.boxl.add_widget(self.textinputlogin)
        self.boxl.add_widget(self.textinputmail)
        self.boxl.add_widget(self.textinputpassword)
        self.boxl.add_widget(self.textinputpasswordtoo)
        self.boxl.add_widget(self.reg_btn)
        self.boxl.add_widget(self.back_btn)

        self.anchLayout.add_widget(self.boxl)
        self.add_widget(self.anchLayout)

    def check_reg(self,button):
        st_user = self.textinputlogin.text
        st_user = st_user.lower()
        st_mail = self.textinputmail.text

        if self.textinputpassword.text != self.textinputpasswordtoo.text or self.textinputpassword.text =="" :
            self.pop = Popup(title="Ошибка", content=PopWindow("Неверный повтор пароля", "Продолжить", self.man),size_hint=(None, None), size=(dp(400), dp(400)))
            self.pop.open()

        elif self.textinputlogin.text =="":
            self.pop = Popup(title="Ошибка",content=PopWindow("Логин обязательное поле", "Продолжить", self.man),size_hint=(None, None), size=(dp(400), dp(400)))
            self.pop.open()

        elif self.textinputmail.text =="":
            self.pop = Popup(title="Ошибка",content=PopWindow("Почта обязательное поле", "Продолжить", self.man),size_hint=(None, None), size=(dp(400), dp(400)))
            self.pop.open()

        elif self.man.db.check_mail(st_mail):
            self.pop = Popup(title="Ошибка", content=PopWindow("Пользователь с такой почтой уже существует", "Продолжить", self.man),size_hint=(None, None), size=(dp(400), dp(400)))
            self.pop.open()

        elif self.man.db.check_existing_user(st_user):
            self.man.db.user_reg(st_user, self.textinputpassword.text,self.textinputmail.text)
            self.man.switch_to_home()

        else:
            self.pop = Popup(title="Ошибка", content=PopWindow("Такой логин занят", "Продолжить", self.man),size_hint=(None, None), size=(dp(400), dp(400)))
            self.pop.open()


class HomeScreen(Screen):
    def __init__(self, manager, **kwargs):
        super(HomeScreen, self).__init__()
        self.boxl = BoxLayout(orientation='vertical', size_hint=[.6, 0.6], spacing=30)
        self.anchLayout = AnchorLayout(anchor_x='center', anchor_y='center')

        self.lbl = Label(text = "СВЁКЛА", font_size = 50,color=(147/255, 7/255, 200/255))

        self.training_btn = MDFillRoundFlatButton(text='Треннировка',text_color=(1, 1, 1, 1), md_bg_color=(120/255, 0, 120/255), pos_hint={'center_x': 0.5})
        self.my_dict_btn = MDFillRoundFlatButton(text='Мой словарь',text_color=(1, 1, 1, 1), md_bg_color=(120/255, 0, 120/255), pos_hint={'center_x': 0.5})
        self.statistics_btn = MDFillRoundFlatButton(text='Статистика',text_color=(1, 1, 1, 1), md_bg_color=(120/255, 0, 120/255), pos_hint={'center_x': 0.5})
        self.theory_btn = MDFillRoundFlatButton(text='Теория ',text_color=(1, 1, 1, 1), md_bg_color=(120/255, 0, 120/255), pos_hint={'center_x': 0.5})
        self.rating_btn = MDFillRoundFlatButton(text='Рэйтинг',text_color=(1, 1, 1, 1), md_bg_color=(120/255, 0, 120/255), pos_hint={'center_x': 0.5})

        self.boxl.add_widget(self.lbl)
        self.boxl.add_widget(self.training_btn)
        self.boxl.add_widget(self.my_dict_btn)
        self.boxl.add_widget(self.statistics_btn)
        self.boxl.add_widget(self.theory_btn)
        self.boxl.add_widget(self.rating_btn)

        self.anchLayout.add_widget(self.boxl)
        self.add_widget(self.anchLayout)


class RegistrationApp(MDApp):
    def __init__(self, db, **kwargs):
        super().__init__(**kwargs)
        self.db = db
        self.theme_cls.theme_style = "Dark"


    def build(self):
        reg_man = RegistrationManager(self.db)

        return reg_man
        # return BoxLayout()
