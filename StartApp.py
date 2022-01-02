from kivy.core.window import Window
from Regisration import RegistrationApp
from Account import AccountApp
from DB import DataBase
from kivy.config import Config


if __name__ == "__main__":

    Config.set('graphics', 'resizable', '0')
    Config.set('graphics', 'width', '480')
    Config.set('graphics', 'height', '700')
    db = DataBase()
    # RegistrationApp(db).run()
    AccountApp(db).run()

