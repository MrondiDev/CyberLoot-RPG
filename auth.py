import sqlite3
import hashlib
import secrets
import json
import state
ORANGE = "\033[38;2;255;140;0m"  # Чистый темно-оранжевый
B_ORANGE = "\033[38;2;255;69;0m"  # Яркий красно-оранжевый
RESET = "\033[0m"
LIME = "\033[38;2;50;205;50m"  # салатовый  
RED = "\033[38;2;220;20;60m"  # красный
def init_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL,
        password_salt TEXT NOT NULL
    )
    """)
    conn.commit()
    conn.close()

def register_user():
    print(f"\n{B_ORANGE}--- РЕГИСТРАЦИЯ НОВОГО ИГРОКА ---{RESET}")
    username = input(f"{B_ORANGE}Придумайте логин:{RESET} ").strip().lower()
    password = input(f"{B_ORANGE}Придумайте пароль (от 6 символов):{RESET} ").strip()
    
    if len(password) < 6:
        print("❌ Ошибка: Пароль слишком короткий!")
        return False
        
    if username in password:
        print("❌ Ошибка: Пароль не должен содержать логин!")
        return False

    salt = secrets.token_hex(8)
    password_raw = (salt + password).encode()
    pwd_hash = hashlib.sha256(password_raw).hexdigest()

    try:
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT INTO users (username, password_hash, password_salt) 
            VALUES (?, ?, ?)
        """, (username, pwd_hash, salt))
        
        conn.commit()
        conn.close()
        print(f"🎉 Аккаунт {username} успешно зарегистрирован!")
        return True
        
    except sqlite3.IntegrityError:
        print("❌ Ошибка: Этот логин уже занят другим сталкером!")
        return False

def login_user():
    print(f"\n{LIME}--- ВХОД В АККАУНТ ---{RESET}")
    username = input(f"{B_ORANGE}Введите логин:{RESET} ").strip().lower()
    password = input(f"{B_ORANGE}Введите пароль:{RESET} ").strip()

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT password_hash, password_salt FROM users WHERE username = ?", (username,))
    row = cursor.fetchone()
    conn.close()

    if row is None:
        print(f"{RED}❌ Ошибка: Пользователь с таким логином не найден!{RESET}")
        return False

    db_hash, db_salt = row


    password_raw = (db_salt + password).encode()
    pwd_hash = hashlib.sha256(password_raw).hexdigest()


    if pwd_hash == db_hash:
        state.NickName = username  
        print(f"🎉{LIME} Добро пожаловать, {state.NickName}! Успешный вход.{RESET}")
        return True
    else:
        print(f"❌{RED} Ошибка: Неверный логин или пароль!{RESET}")
        return False
