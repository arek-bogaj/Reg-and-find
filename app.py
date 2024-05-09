import sqlite3
from users import User


# Tworzenie bazy danych, kursora SQL i tablicy z userami
conn = sqlite3.connect(':memory:')
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS users(
            id INTEGER UNIQUE NOT NULL,
            login TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL)""")


# SQlite3
def insert_user(user):
    with conn:
        c.execute("INSERT INTO users VALUES(?, ?, ?)",
                  (user.id, user.login, user.password))


def get_user_by_login(login):
    c.execute("SELECT * FROM users WHERE login=:login", {'login': login})
    return c.fetchall()


# Stwórz usera
def create_user(id, login, password):
    user = User(id, login, password)
    insert_user(user)


# Wprowadź dane usera
def input_user_data():
    id = 1
    while True:
        i = input('Utworzyć nowego użytkownika? (t/n): ')
        if i == 't':
            login = input('Utwórz login: ')
            password = input('Utwórz hasło: ')
            create_user(id, login, password)
            id += 1
            print()
        elif i == 'n':
            print()
            break
        else:
            print('"t" = tak, "n" = nie')


# Znajdź usera
def find_user():
    while True:
        i = input('Wyszukać użytkownika? (t/n): ')
        if i == 't':
            login = input('Login: ')
            user = get_user_by_login(login)
            user = [dict(zip(['id', 'login', 'password'], row)) for row in user]
            print(user)
            print()
        elif i == 'n':
            print()
            break
        else:
            print('"t" = tak, "n" = nie')


print('>>>  r e g  &  f i n d  <<<')
print()
input_user_data()
find_user()
conn.close()