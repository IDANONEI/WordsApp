from Regisration import RegistrationApp
from kivy.config import Config
Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '480')
Config.set('graphics', 'height', '700')

if __name__ == "__main__":
    RegistrationApp().run()
