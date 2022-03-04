import sqlite3
import pymysql
from random import shuffle

from Constans import NUM_WORDS


class DataBase:

    def __init__(self):
        self.connection()
        # self.cur.execute("""DELETE FROM WordsTable""")
        # self.fill_words_bd()

    def connection(self):
        self.bd = pymysql.connect(
            host="maskinhz.beget.tech",
            user="maskinhz_appword",
            password="Qwerty123",
            database="maskinhz_appword")
        self.cur = self.bd.cursor()

    def check_user(self, login, password):
        self.connection()
        self.cur.execute("""SELECT UserID FROM UserTable WHERE user_name=%s""", (login,))
        users = self.cur.fetchone()
        if not users is None:
            self.cur.execute("""SELECT user_password FROM UserTable WHERE user_name=%s""", (login,))
            users = self.cur.fetchone()[0]
            if not users is None:
                if str(password) == str(users):
                    return True
        else:
            self.cur.execute("""SELECT UserID FROM UserTable WHERE mail=%s""", (login,))
            mail = self.cur.fetchone()
            if not mail is None:
                self.cur.execute("""SELECT user_password FROM UserTable WHERE mail=%s""", (login,))
                users = self.cur.fetchone()[0]
                if not users is None:
                    if str(password) == str(users):
                        return True
        return False

    def check_not_existing_user(self, u):
        self.connection()
        users = self.cur.execute("""SELECT UserID FROM UserTable WHERE user_name=%s""", (u,))
        if not users:
            users = self.cur.execute("""SELECT UserID FROM UserTable WHERE mail=%s""", (u,))
            if not users is None:
                return True
        return False

    def check_mail(self, m):
        self.connection()
        mail = self.cur.execute("""SELECT UserID FROM UserTable WHERE mail=%s""", (m,))
        if not mail:
            return False
        return True

    def user_reg(self, login, password, mail):
        self.connection()
        self.cur.execute("""INSERT INTO UserTable (user_name, user_password, mail, correct_answers, wrong_answers, rating) VALUES (%s, %s, %s, %s, %s, %s)""",
                         (login, password, mail, ("0|" * NUM_WORDS)[:-1], ("0|" * NUM_WORDS)[:-1], 0))
        self.bd.commit()

    def user_info_id(self, id):
        self.connection()
        self.cur.execute("""SELECT * FROM UserTable WHERE UserID=%s""", (id,))
        user =self.cur.fetchone()
        if not user is None:
            return user
        else:
            raise Exception("Пользователь не существует")

    def user_info_l_or_e(self, login):
        self.connection()
        login = login.strip()
        self.cur.execute("SELECT * FROM UserTable")
        users = self.cur.fetchall()
        for user in users:
            if user[1] == login or user[3] == login:
                return user

    def take_answer(self):
        with open("answers_list_file.txt", "r", encoding='utf-8') as f:
            temp = f.readlines()
        if not temp:
            temp.append(("0|" * NUM_WORDS)[:-1] + "\n")
            temp.append(("0|" * NUM_WORDS)[:-1] + "\n")
        correct_answers = list(map(int, temp[0].strip().split("|")))
        wrong_answers = list(map(int, temp[1].strip().split("|")))
        answers = {'correct': correct_answers, 'wrong': wrong_answers}
        return answers

    def give_answer(self, correct_answers, wrong_answers):
        self.connection()
        with open("Email_login_password.txt", "r", encoding='utf-8') as f:
            info = f.readlines()
        if info:
            id = int(info[0].strip())
            if sum(correct_answers) + sum(wrong_answers) >= 100:
                rating = round(sum(correct_answers) / (sum(correct_answers) + sum(wrong_answers)), 2)
            else:
                rating = 0.0
            correct_answers = "|".join(list(map(str, correct_answers)))
            wrong_answers = "|".join(list(map(str, wrong_answers)))

            self.cur.execute("""UPDATE UserTable SET correct_answers=%s , wrong_answers=%s, rating=%s WHERE UserID=%s""",
                             (correct_answers, wrong_answers, rating, id,))
            self.bd.commit()

    def take_answers_db(self, id):
        self.connection()
        self.cur.execute("""SELECT correct_answers,wrong_answers FROM UserTable WHERE UserID=%s""", (id,))

        temp = self.cur.fetchone()
        with open("answers_list_file.txt", "w", encoding='utf-8') as f:
            f.write(temp[0] + "\n")
            f.write(temp[1] + "\n")

    def change_password(self, id_user, password):
        self.connection()
        self.cur.execute("""UPDATE UserTable SET user_password=%s WHERE UserID=%s""",
                         (password, int(id_user),))
        self.bd.commit()

    def change_name(self, id_user, name):
        self.connection()
        self.cur.execute("""UPDATE UserTable SET user_name=%s WHERE UserID=%s""",
                         (name, int(id_user),))
        self.bd.commit()

    def change_mail(self, id_user, mail):
        self.connection()
        self.cur.execute("""UPDATE UserTable SET mail=%s WHERE UserID=%s""",
                         (mail, int(id_user),))
        self.bd.commit()

    def get_users_rating(self):
        self.connection()
        with open("Email_login_password.txt", "r", encoding='utf-8') as f:
            cur_user = f.readlines()
            if cur_user:
                cur_user = cur_user[1].strip()
            else:
                cur_user = ""
        cur_user_info = ("-", "-", "-")
        self.cur.execute("""SELECT user_name, rating FROM UserTable""")
        users =self.cur.fetchall()
        sorted_info = sorted(users, key=lambda x: x[1], reverse=True)
        res = []
        for i in range(0, len(sorted_info)):
            if sorted_info[i][0] == cur_user:
                if sorted_info[i][1] == 0:
                    cur_user_info = ("-", cur_user, "-")
                else:
                    if i != 0 and res[-1][2] == sorted_info[i][1]:
                        cur_user_info = (res[-1][0], sorted_info[i][0], sorted_info[i][1])
                    else:
                        cur_user_info = (i + 1, sorted_info[i][0], sorted_info[i][1])
            if sorted_info[i][1] == 0:
                continue
            if i == 0:
                res.append([1, sorted_info[0][0], sorted_info[0][1]])
                continue
            if res[i - 1][2] == sorted_info[i][1]:
                res.append([res[-1][0], sorted_info[i][0], sorted_info[i][1]])
            else:
                res.append([i + 1, sorted_info[i][0], sorted_info[i][1]])
        return cur_user_info, res

    def check_bad_name(self, name):
        self.connection()
        with open("bed_words.txt", "r", encoding='utf-8') as f:
            words = [word.strip().lower() for word in f.readlines()]

        # print("Фильтруемые слова:", words)

        # Фраза, которую будем проверять.
        phrase = name

        def distance(a, b):
            # "Calculates the Levenshtein distance between a and b."
            n, m = len(a), len(b)
            if n > m:
                # Make sure n <= m, to use O(min(n, m)) space
                a, b = b, a
                n, m = m, n

            current_row = range(n + 1)  # Keep current and previous row, not entire matrix
            for i in range(1, m + 1):
                previous_row, current_row = current_row, [i] + [0] * n
                for j in range(1, n + 1):
                    add, delete, change = previous_row[j] + 1, current_row[j - 1] + 1, previous_row[j - 1]
                    if a[j - 1] != b[i - 1]:
                        change += 1
                    current_row[j] = min(add, delete, change)

            return current_row[n]

        d = {'а': ['а', 'a', '@'],
             'б': ['б', '6', 'b'],
             'в': ['в', 'b', 'v'],
             'г': ['г', 'r', 'g'],
             'д': ['д', 'd'],
             'е': ['е', 'e'],
             'ё': ['ё', 'e'],
             'ж': ['ж', 'zh', '*'],
             'з': ['з', '3', 'z'],
             'и': ['и', 'u', 'i'],
             'й': ['й', 'u', 'i'],
             'к': ['к', 'k', 'i{', '|{'],
             'л': ['л', 'l', 'ji'],
             'м': ['м', 'm'],
             'н': ['н', 'h', 'n'],
             'о': ['о', 'o', '0'],
             'п': ['п', 'n', 'p'],
             'р': ['р', 'r', 'p'],
             'с': ['с', 'c', 's'],
             'т': ['т', 'm', 't'],
             'у': ['у', 'y', 'u'],
             'ф': ['ф', 'f'],
             'х': ['х', 'x', 'h', '}{'],
             'ц': ['ц', 'c', 'u,'],
             'ч': ['ч', 'ch'],
             'ш': ['ш', 'sh'],
             'щ': ['щ', 'sch'],
             'ь': ['ь', 'b'],
             'ы': ['ы', 'bi'],
             'ъ': ['ъ'],
             'э': ['э', 'e'],
             'ю': ['ю', 'io'],
             'я': ['я', 'ya']
             }

        for key, value in d.items():
            # Проходимся по каждой букве в значении словаря. То есть по вот этим спискам ['а', 'a', '@'].
            for letter in value:
                # Проходимся по каждой букве в нашей фразе.
                for phr in phrase:
                    # Если буква совпадает с буквой в нашем списке.
                    if letter == phr:
                        # Заменяем эту букву на ключ словаря.
                        phrase = phrase.replace(phr, key)

        t = False
        for word in words:
            # Разбиваем слово на части, и проходимся по ним.
            if t:
                break
            for part in range(len(phrase)):
                if t:
                    break
                # Вот сам наш фрагмент.
                fragment = phrase[part: part + len(word)]
                # Если отличие этого фрагмента меньше или равно 25% этого слова, то считаем, что они равны.
                if distance(fragment, word) <= len(word) * 0.25:
                    t = True
                    # Если они равны, выводим надпись о их нахождении.
                    return (True)
        return (False)
