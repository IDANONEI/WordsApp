from kivy.app import App
from kivy.metrics import dp
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout


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

        self.lbl = Label(text="СВЁКЛА", font_size=50)
        self.boxl=BoxLayout(orientation='vertical', size_hint= [.6,0.6], spacing = 30)
        self.textinputlogin=TextInput(text="Логин", multiline = False)
        self.textinputlogin.bind(focus=manager.cleen_text)
        self.textinputpassword = TextInput(text="Пароль", multiline=False)
        self.sing_up=Button(text="Войти",on_press = self.check_user)
        self.registrate=Button(text="Регистрация", on_press = manager.switch_to_registration)
        self.forgotpassword = Button(text="Забыл(а) логин или пароль", on_press=manager.switch_to_forgot_password)

        self.boxl.add_widget(self.lbl)
        self.boxl.add_widget(self.textinputlogin)
        self.boxl.add_widget(self.textinputpassword)
        self.boxl.add_widget(self.sing_up)
        self.boxl.add_widget(self.registrate)
        self.boxl.add_widget(self.forgotpassword)


        self.anchLayout=AnchorLayout(anchor_x = 'center', anchor_y = 'center')

        self.anchLayout.add_widget(self.boxl)
        self.add_widget(self.anchLayout)

    def check_user(self, button):
        st = self.textinputlogin.text
        st = st.lower()
        if self.man.db.check_user(st, self.textinputpassword.text):
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

        self.forgot_lbl = Label(text="Забыли пароль?", font_size=25)
        self.lbl = Label(text="Пожалуйста, введите адрес электронной почты. Вы получите ссылку для изменения пароля", font_size=15)
        self.mail=TextInput(text="Введите почту", multiline=False)
        self.btn=Button(text="Восстановить")

        self.boxl=BoxLayout(orientation='vertical', size_hint= [.6,0.6], spacing = 20)
        self.anchLayout=AnchorLayout(anchor_x = 'center', anchor_y = 'center')

        self.boxl.add_widget(self.forgot_lbl)
        self.boxl.add_widget(self.lbl)
        self.boxl.add_widget(self.mail)
        self.boxl.add_widget(self.btn)

        self.anchLayout.add_widget(self.boxl)
        self.add_widget(self.anchLayout)

class RegistrationScreen(Screen):
    def __init__(self, manager,  **kwargs):

        self.man = manager

        super(RegistrationScreen, self).__init__(**kwargs)
        self.lbl = Label(text="Регистрация", font_size=50)
        self.textinputlogin=TextInput(text="Логин", multiline=False)
        self.textinputmail = TextInput(text="Почта", multiline=False)
        self.textinputpassword=TextInput(text="Пароль", multiline=False)
        self.textinputpasswordtoo=TextInput(text="Повторите пароль", multiline=False)
        self.reg_btn=Button(text="Регистрация",on_press = self.check_reg)
        self.back_btn=Button(text="Назад",on_press = manager.swith_to_singup)


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

        if self.textinputpassword.text != self.textinputpasswordtoo.text:
            self.pop = Popup(title="Ошибка", content=PopWindow("Неверный повтор пароля", "Продолжить", self.man),size_hint=(None, None), size=(dp(400), dp(400)))
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

        self.lbl = Label(text = "СВЁКЛА", font_size = 50)

        self.training_btn = Button(text = "Тренировка", font_size = 20)
        self.my_dict_btn = Button(text = "Мой словарь", font_size = 20)
        self.statistics_btn = Button(text="Статистика", font_size=20)
        self.theory_btn = Button(text="Теория", font_size=20)
        self.rating_btn = Button(text="Рэйтинг", font_size=20)

        self.boxl.add_widget(self.lbl)
        self.boxl.add_widget(self.training_btn)
        self.boxl.add_widget(self.my_dict_btn)
        self.boxl.add_widget(self.statistics_btn)
        self.boxl.add_widget(self.theory_btn)
        self.boxl.add_widget(self.rating_btn)

        self.anchLayout.add_widget(self.boxl)
        self.add_widget(self.anchLayout)




class RegistrationApp(App):
    def __init__(self, db, **kwargs):
        super().__init__(**kwargs)
        self.db = db

    def build(self):
        reg_man = RegistrationManager(self.db)

        return reg_man
        # return BoxLayout()
