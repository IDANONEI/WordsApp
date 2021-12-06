import sqlite3
from random import shuffle

class DataBase:
    user_of_number=1
    def  __init__(self):
        self.bd= sqlite3.connect("Test1")
        self.cur = self.bd.cursor()
        self.cur.execute("""DELETE FROM UserTable""")
        self.cur.execute("""DELETE FROM WordsTable""")

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
    def user_reg(self,login,password):
        self.cur.execute("""INSERT INTO UserTable VALUES (?, ?, ?)""", (DataBase.user_of_number,login,password))
        DataBase.user_of_number=DataBase.user_of_number+1
        self.bd.commit()




new_db = DataBase()
new_db.fill_words_bd()
# word = new_db.choose_words()[0]
# print(word)
# new_db.update_read(word, True)
new_db.user_reg('Рафаил',123)
new_db.user_reg('Даниил',123321)
new_db.user_reg('Никита','1wsx2wsx')


