from kivy.core.window import Window
from Manager import ManagerApp
from DB import DataBase
from kivy.config import Config

def authorization_check(db):
    with open("Email_login_password.txt","r", encoding="utf-8") as f:
        info_a=f.readlines()
        if not info_a:
            ManagerApp(db, False).run()
            return
        info_db = db.user_info_id(info_a[0].strip())
        for i in range(len(info_a)):
            if info_a[i].strip() != str(info_db[i]):
                ManagerApp(db, False).run()
                return
        ManagerApp(db, True).run()

if __name__ == "__main__":
    Config.set('graphics', 'resizable', '0')
    Config.set('graphics', 'width', '480')
    Config.set('graphics', 'height', '700')
    db = DataBase()
    authorization_check(db)
    # AccountApp(db).run()
