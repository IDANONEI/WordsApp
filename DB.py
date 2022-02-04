import sqlite3
from random import shuffle


class DataBase:

    def __init__(self):
        self.bd = sqlite3.connect("Test1")
        self.cur = self.bd.cursor()
        # self.cur.execute("""DELETE FROM WordsTable""")
        # self.fill_words_bd()

    # def fill_words_bd(self):
    #     file = open('words.txt', encoding='utf-8').readlines()
    #     for i, line in enumerate(file):
    #         line = line.strip()
    #         self.cur.execute("""INSERT INTO WordsTable VALUES (?, ?, ?, ?)""", (i + 1, line, 0, 0))
    #         self.bd.commit()
    #
    # def choose_words(self):
    #     list_words = self.cur.execute("""SELECT words FROM WordsTable""").fetchall()
    #     list_words_update = []
    #     for word_tuple in list_words:
    #         list_words_update.append(word_tuple[0])
    #     shuffle(list_words_update)
    #     return list_words_update
    #
    # def update_read(self, word, is_true_read):
    #     if is_true_read:
    #         true_read_bd = self.cur.execute("""SELECT true_read FROM WordsTable WHERE words=?""", (word,)).fetchone()[0]
    #         self.cur.execute("""UPDATE WordsTable SET true_read=? WHERE words=?""", (true_read_bd + 1, word,))
    #         self.bd.commit()
    #     if is_true_read == False:
    #         false_read_bd = self.cur.execute("""SELECT false_read FROM WordsTable WHERE words=?""", (word,)).fetchone()[
    #             0]
    #         self.cur.execute("""UPDATE WordsTable SET false_read=? WHERE words=?""", (false_read_bd + 1, word,))
    #         self.bd.commit()

    def check_user(self, login, password):
        users = self.cur.execute("""SELECT UserID FROM UserTable WHERE user_name=?""", (login,)).fetchone()
        if not users is None:
            users = self.cur.execute("""SELECT user_password FROM UserTable WHERE user_name=?""", (login,)).fetchone()[
                0]
            if not users is None:
                if str(password) == str(users):
                    return True
        else:
            mail = self.cur.execute("""SELECT UserID FROM UserTable WHERE mail=?""", (login,)).fetchone()
            if not mail is None:
                users = self.cur.execute("""SELECT user_password FROM UserTable WHERE mail=?""", (login,)).fetchone()[0]
                if not users is None:
                    if str(password) == str(users):
                        return True
        return False

    def check_not_existing_user(self, u):
        users = self.cur.execute("""SELECT UserID FROM UserTable WHERE user_name=?""", (u,)).fetchone()
        if users is None:
            users = self.cur.execute("""SELECT UserID FROM UserTable WHERE mail=?""", (u,)).fetchone()
            if users is None:
                return True
        return False

    def check_mail(self, m):
        mail = self.cur.execute("""SELECT UserID FROM UserTable WHERE mail=?""", (m,)).fetchone()
        if mail is None:
            return False
        return True

    def user_reg(self, login, password, mail):
        users = self.cur.execute("""SELECT user_name FROM UserTable""").fetchall()
        id_new_user = len(users) + 1
        self.cur.execute("""INSERT INTO UserTable VALUES (?, ?, ?, ?, ?, ?)""",
                         (id_new_user, login, password, mail, ("0|" * 318)[:-1], ("0|" * 318)[:-1]))
        self.bd.commit()

    def user_info_id(self, id):
        user = self.cur.execute("""SELECT * FROM UserTable WHERE UserID=?""", (id,)).fetchone()
        if not user is None:
            return user
        else:
            raise Exception("Пользователь не существует")

    def user_info_l_or_e(self, login):
        login = login.lower()
        user = self.cur.execute("""SELECT * FROM UserTable WHERE user_name=?""", (login,)).fetchone()
        if not user is None:
            return user
        else:
            user = self.cur.execute("""SELECT * FROM UserTable WHERE mail=?""", (login,)).fetchone()
            return user

    def take_answer(self):
        with open("answers_list_file.txt", "r", encoding='utf-8') as f:
            temp = f.readlines()
        correct_answers = list(map(int, temp[0].strip().split("|")))
        wrong_answers = list(map(int, temp[1].strip().split("|")))
        answers = {'correct': correct_answers, 'wrong': wrong_answers}
        return answers

    def give_answer(self, correct_answers, wrong_answers):
        with open("Email_login_password.txt", "r", encoding='utf-8') as f:
            id = int(f.readlines()[0].strip())
            correct_answers = "|".join(list(map(str, correct_answers)))
            wrong_answers = "|".join(list(map(str, wrong_answers)))
            self.cur.execute("""UPDATE UserTable SET correct_answers=? , wrong_answers=? WHERE UserID=?""",
                             (correct_answers, wrong_answers, id,))
            self.bd.commit()


new_db = DataBase()
