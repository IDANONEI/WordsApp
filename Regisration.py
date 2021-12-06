from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.textinput import TextInput

# class RegistrationManager(ScreenManager):
    # def __init__(self, **kwargs):
    #     super(RegistrationManager, self).__init__(**kwargs)
        # SingUpWindow=SingUpScreen(name="SingUp")
        # ForgotPasswordWindow=ForgotPasswordScreen(name="ForgotPassword")
        # RegistrationWindow=RegistrationScreen(name="Registration")
        # self.add_widget(SingUpWindow)
        # self.add_widget(ForgotPasswordWindow)
        # self.add_widget(RegistrationWindow)
    # pass



# class SingUpScreen (Screen):
#     def __init__(self, **kwargs):
#         super(SingUpScreen, self).__init__(**kwargs)
        # self.boxl=BoxLayout(orientation='vertical', size_hint= [.6,0.6], spacing = 100)
        # self.textinputlogin=TextInput(text="Имя")
        # self.textinputpassword = TextInput(text="Пароль")
        # self.boxl.add_widget(self.textinputlogin)
        # self.boxl.add_widget(self.textinputpassword)
        # self.anchLayout=AnchorLayout(anchor_x = 'center', anchor_y = 'center')
        # self.anchLayout.add_widget(self.boxl)
        # self.add_widget(self.anchLayout)


# class ForgotPasswordScreen(Screen):
#     def __init__(self, **kwargs):
#         super(ForgotPasswordScreen, self).__init__(**kwargs)
#
# class RegistrationScreen(Screen):
#     def __init__(self, **kwargs):
#         super(RegistrationScreen, self).__init__(**kwargs)


class RegistrationApp(App):
    def build(self):
        # reg_man = RegistrationManager()
        # return reg_man
        return BoxLayout()