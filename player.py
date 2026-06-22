import state
import random
import time
def show_status():
    print(f"Персонаж: {state.NickName}. Уровень hp: {state.hero["hp"]}. Золото: {state.hero["gold"]}. \
          Уровень персонажа: {state.hero["lvl"]}. Свободные очки улучшения: {state.hero["stat_points"]}" )


def open_box():
    while True:
        print("Варианты: платный(5 золотых монет) или бесплатный")
        if len(state.hero["inventory"]) >= state.hero["max_slots"]:
                     print("Твой инвентарь полон. Для начала освободи инвентарь, после чего открой бокс.")
                     return
        else:
            var = input("Выберите вариант бокса: платный или бесплатный. Если хотите выйти, то введите: 'выход'. ").lower().strip()
            if var == "платный":
                if state.hero["gold"] >= 5:
                    drops = ["МЕЧ", "ВСС", "шлем", "шлак", "Combat"]
                    drop = random.choice(drops)
                    print(f"{state.NickName}, вы открыли платный бокс и получили: {drop}")
                    state.hero["inventory"].append(drop)
                    state.hero["gold"] -= 5
                else:
                    print("Не хватает средств на балансе")
            elif var == "бесплатный":
                drops_free = ["шлак", "обойма", "патрон 5.45 кол-во: 5шт", "МЕЧ"]
                drop = random.choice(drops_free)
                print(f"{state.NickName}, вы открыли бесплатный бокс и получили: {drop}")
                state.hero["inventory"].append(drop)
            elif var == "выход":
                print("Вы успешно вышли из магазина.")
                break
            else:
                print("Не известный вариант, попробуйте еще раз")
                continue
    return


def exit_programm():
    print(f"Выполняется выход...")
    time.sleep(0.5)
    print(f"Выход выполнен успешно. Ждем тебя снова, {state.NickName}")


def effect(item):
    if item == "зелье":
        if state.hero["hp"] == state.hero["max_hp"]:
            print("Здоровье уже полное!")
            return False
        elif state.hero["max_hp"] - 20 < state.hero["hp"] < state.hero["max_hp"]:
            hp_plus = state.hero["max_hp"] - state.hero["hp"]
            state.hero["hp"] = state.hero["max_hp"]
            print(f"Здоровье восстановлено на {hp_plus} единиц. Текущее состояние: {state.hero['hp']}")
        else:
             state.hero["hp"] += 20
             print(f"Здоровье восстановлено на 20 единиц. Текущее состояние: {state.hero['hp']}")             
        return True
    elif item == "шлак":
        if state.hero["hp"] == 0:
             print("Вы не можете использовать данный предмет, так как ваш персонаж мертв. Используйте предмет \
                   с эффектом восстановления здоровья")
             return False
        if state.hero["hp"] <= 10:
            print(f"Ваше здоровье было уменьшено на {state.hero['hp']}. Персонаж погиб, вы можете восстановиться \
                    с помощью предмета с эффектом восстановления здоровья.")
            state.hero["hp"] = 0
            return True
        else:
             state.hero["hp"] -= 10
             print(f"Ваше здоровье было уменьшено на 10 единиц. Текущее состояние здоровья: {state.hero['hp']}")
             return True
    else:
         print(f"Предмет {item} не может быть использован таким образом!")
         return False
    

def open_inventory():
    print(state.hero["inventory"])
    variant = input("Хотите ли вы использовать что-то(да/нет): ").lower().strip()
    if variant == "да":
        if state.hero["inventory"] == []:
            print("Инвентарь пуст. Для начала нужно обзавестись предметами")
            return
        else:
            use = input("Выберите предмет, который хотите использовать: ")
            if use in state.hero["inventory"]:
                success = effect(use)
                if success == True:
                    print(f"Использован предмет: {use}.")
                    state.hero["inventory"].remove(use)
                else:
                     print("Данный предмет не может быть использован.")
            else:
                print(f"Предмета : {use} нет в вашем инвентаре. Сначала получите его.")
                return
def upgade_stats():
    print("Вы зашли в меню прокачки персонажа. Здесь вы можете расспределить очки навыков.")
    print(f"Ваш уровень: {state.hero["lvl"]}. Свободные очки расспределения: {state.hero["stat_points"]}")
    print("---ВАРИАНТЫ ДЛЯ ПРОКАЧКИ---")
    print(f"Коэфицент блокировки урона {int((1 - state.hero["defend_bonus"]) / 0.1)}")
    print(f"Максимальное здоровье {(state.hero['max_hp'] - 100) // 10}/20")
    print(f"Бонус к урону ({int((state.hero['damage_bonus'] - 1) / 0.25)}/4)")
    upgade_var = input("Что вы хотите прокачать?(урон, здоровье или броня): ").lower().strip()
    if upgade_var == "урон":
        if state.hero["stat_points"] == 0:
            print("У вас нет свободных очков прокачки.")
            return
        elif state.hero["damage_bonus"] == 2.0:
            print("Бонус урона улучшен до максимального уровня. Вы не можете больше его улучшать.")
            return
        else:
            state.hero["damage_bonus"] += 0.25
            print(f"Вы успешно улучшили бонус к урону! Текущий показатель: {state.hero["damage_bonus"]} ")
            state.hero["stat_points"] -= 1
    elif upgade_var == "здоровье":
            if state.hero["stat_points"] == 0:
                print("У вас нет свободных очков улучшения.")
                return
            elif state.hero["max_hp"] == 300:
                print("У вас максимальный уровень улучшения здоровья.")
                return
            else:
                state.hero["stat_points"] -= 1
                state.hero["max_hp"] += 10
                print(f"Вы успешно улучшили здоровье! Ваше максимальное здоровье: {state.hero["max_hp"]} \
                      Свободные очки улучшения: {state.hero["stat_points"]}")
    elif upgade_var == "броня":
         if state.hero["stat_points"] == 0:
            print("У вас нет свободных очков улучшения")
            return
         elif state.hero["defend_bonus"] == 0.5:
              print("У вас максимальный уровень улучшения брони.")
              return
         else:
              state.hero["stat_points"] -= 1
              state.hero["defend_bonus"] -= 0.1
              print(f"Вы успешно улучшили броню! Ваш коэфицент блокировки урона: {state.hero["defend_bonus"]} \
                    Свободные очки улучшения: {state.hero["stat_points"]}")
def equip():
    var_equip = input("Что вы хотите экипировать?(оружие/броня/рюкзак): ").lower().strip()
    if var_equip == "оружие":
        print(state.hero["inventory"])
        gun_equip = input("Выберите оружие, которое хотите экипировать из инвентаря: ").upper().strip()
        if gun_equip not in state.hero["inventory"]:
            print("У вас нет такого предмета.")
            return
        if state.hero["gun"] != "кулаки": 
            print(f"Оружие {state.hero['gun'].upper()} было возвращено в инвентарь.")
            state.hero["inventory"].append(state.hero["gun"])
        state.hero["gun"] = gun_equip
        state.hero["inventory"].remove(gun_equip)
        print(f"Оружие {state.hero['gun']} успешно экипировано.")
    elif var_equip == "рюкзак":
        print(state.hero["inventory"])
        bag_equip = input("Выберите рюкзак, который хотите экипировать из инвентаря: ").lower().strip()
        if bag_equip not in state.hero["inventory"]:
            print(f"Предмета {bag_equip} нет в вашем инвентаре.")
            return
        if state.hero["bag"] != "вещмешок":
            print(f"{state.hero["bag"]} был возвращен в ваш инвентарь.")
            state.hero["inventory"].append(state.hero["bag"])
        state.hero["bag"] = bag_equip
        state.hero["inventory"].remove(bag_equip)
        print(F"{state.hero["bag"]} успешно экипирован.")
        if state.hero["bag"] == "туристический рюкзак":
            state.hero["max_slots"] = 20
        elif state.hero["bag"] == "вещмешок":
            state.hero["max_slots"] = 5
        elif state.hero["bag"] == "Combat":
            state.hero["max_slots"] = 40
    elif var_equip == "бронежилет":
        print(state.hero["inventory"])
        armour_equip = input("Какой бронежилет хотите экипировать?: ").upper().strip()
        if armour_equip not in state.hero["inventory"]:
            print(f"Бронежилета {armour_equip} нет в вашем инвентаре.")
            return
        if state.hero["armour"] != "КУРТКА":
            print(f"{state.hero["armour"]} был возвращен в инвентарь")
            state.hero["inventory"].append(state.hero["armour"])
        state.hero["armour"] = armour_equip
        state.hero["inventory"].remove(armour_equip)