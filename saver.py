import json
import state
import os

def save_game():
    filename = f"{state.NickName}_save.json"
    with open(filename, "w") as file:
        json.dump(state.hero, file)
    print(f"💾 Прогресс аккаунта {state.NickName} успешно сохранен!")

def load_game():
    filename = f"{state.NickName}_save.json"
    
    if os.path.exists(filename):
        with open(filename, "r") as file:
            state.hero = json.load(file)
        print(f"📂 Прогресс игрока {state.NickName} успешно загружен!")
    else:
        state.hero["name"] = state.NickName
        print(f"🆕 Сохранение для {state.NickName} не найдено. Начинаем новую историю!")
