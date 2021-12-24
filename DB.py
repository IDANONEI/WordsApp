import sqlite3
from random import shuffle

class DataBase:
    user_of_number=3
    def  __init__(self):
        self.bd= sqlite3.connect("Test1")
        self.cur = self.bd.cursor()
        self.cur.execute("""DELETE FROM WordsTable""")
        self.fill_words_bd()

    def fill_words_bd(self):
        file = open('words.txt', encoding='utf-8').readlines()
        for i, line in enumerate(file):
            line = line.strip()
            self.cur.execute("""INSERT INTO WordsTable VALUES (?, ?, ?, ?)""", (i+1, line, 0, 0))
            self.bd.commit()
    def choose_words(self):
        list_words=self.cur.execute("""SELECT words FROM WordsTable""").fetchall()
        list_words_update = []
        for word_tuple in list_words:
            list_words_update.append(word_tuple[0])
        shuffle(list_words_update)
        return list_words_update
    def update_read(self,word,is_true_read):
        if is_true_read :
            true_read_bd=self.cur.execute("""SELECT true_read FROM WordsTable WHERE words=?""", (word,)).fetchone()[0]
            self.cur.execute("""UPDATE WordsTable SET true_read=? WHERE words=?""", (true_read_bd+1, word,))
            self.bd.commit()
        if is_true_read==False :
            false_read_bd=self.cur.execute("""SELECT false_read FROM WordsTable WHERE words=?""", (word,)).fetchone()[0]
            self.cur.execute("""UPDATE WordsTable SET false_read=? WHERE words=?""", (false_read_bd+1, word,))
            self.bd.commit()
    def check_user(self,login,password):
        users = None
        users = self.cur.execute("""SELECT user_password FROM UserTable WHERE user_name=?""", (login,)).fetchone()[0]
        if not users is None:
            if str(password) == str(users):
                return True
        return False
    def check_existing_user(self,u):
        users = None
        users=self.cur.execute("""SELECT UserID FROM UserTable WHERE user_name=?""", (u,)).fetchone()[0]
        if users is None:
            return True
        return False
    def phone(self,number):
        i=0
        while i != len(number):
            if not number[i].isdigit():
                number = number[0:i]+number[i+1:]







    def user_reg(self,login,password,number,question,answer):
        users = self.cur.execute("""SELECT user_name FROM UserTable""").fetchall()
        id_new_user = len(users) + 1
        self.cur.execute("""INSERT INTO UserTable VALUES (?, ?, ?, ?, ?, ?)""", (id_new_user,login,password,number,question,answer))
        self.bd.commit()




new_db = DataBase()
# word = new_db.choose_words()[0]
# print(word)
# new_db.update_read(word, True)
# new_db.user_reg('Рафаил',123)
# new_db.user_reg('Даниил',123321)


