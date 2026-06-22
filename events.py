import state
import random
def event():
    if state.hero["gun"] == "КУЛАКИ":
        dmg_boost = 0
    elif state.hero["gun"] == "ВСС":
        dmg_boost = 10
    elif state.hero["gun"] == "ПМ":
        dmg_boost = 3
    if state.hero["armour"] == "КУРТКА":
        state.hero["armour_shild"] = 1.0
    elif state.hero["armour"] == "6Б3":
        state.hero["armour_shild"] = 0.95
    elif state.hero["armour"] == "6Б12":
        state.hero["armour_shild"] = 0.85
    elif state.hero["armour"] == "6Б13":
        state.hero["armour_shild"] = 0.8
    print("Вы спуситились в пещеру данжей. Выберите вариант для проихождения")
    event_var = input("Варианты: Робот(от 1 lvl персонажа) \n \
        Пешера с пауками(от 10 lvl персонажа). \n \
        Улей(доступно от 12 lvl персонажа): ").lower().strip()
    if event_var == "робот":
        print("Вы спустились в пещеру Робота. Бой начинается")
        robot_hp = 50
        while robot_hp > 0:
            if state.hero["hp"] <= 0:
                print("Персонаж убит. Событие провалено.")
                break
            print("Робот атакует!")    
            attack_var_robot = input("Что будете делать?(атака или отступление): ").lower().strip()
            if attack_var_robot == "атака":
                attack = int((random.randint(1, 10) + dmg_boost) * state.hero["damage_bonus"])
                robot_attack = int(random.randint(1, 6) * state.hero["defend_bonus"] * state.hero["armour_shild"])
                robot_hp -= attack
                print(f"Вы произвели атаку. Вы нанесли роботу урон в количестве: {attack}. Здоровье робота: {robot_hp}")
                state.hero["hp"] -= robot_attack
                print(f"Робот вас атаковал. Вам нанесен урон в размере: {robot_attack}. Ваше здоровье: {state.hero["hp"]}")
                continue
            elif attack_var_robot == "отступление":
                print("Вы начали отступление.")
                robot_attack_var = random.choice([True, False])
                if robot_attack_var == True:
                    robot_attack = int(random.randint(1, 6) * state.hero["defend_bonus"] * state.hero["armour_shild"])
                    state.hero["hp"] -= robot_attack
                    print(f"Робот догнал вас! Ваше здоровье уменьшено на: {robot_attack}. Ваше здоровье: {state.hero["hp"]}")
                else:
                    print("Отступление произведено успешно.")
                continue
            else:
                print("Неизвестная команда.")
                continue
        if robot_hp <= 0:
                    state.hero["lvl"] += 1
                    state.hero["stat_points"] += 1
                    print(f"Робот убит! Вы успешно прошли событие. Ваш уровень был повышен на 1. Ваш уровень: \
                    {state.hero["lvl"]}. Свободные очки улучшения: {state.hero["stat_points"]}")
    if event_var == "пещера с пауками":
        spider_hp = 100
        if state.hero["lvl"] < 10:
            print("Персонажу с вашим уровнем нельзя проходить данное событие.")
            return
        else:
            print("Вы спустились в пещеру с пауками!")
            while spider_hp > 0:
                if state.hero["hp"] <= 0:
                    print("Персонаж убит. Событие провалено.")
                    break
                print("Пауки вас атакуют!")
                attack_var_spider = input("Что будете делать?(атака или отступление): ").lower().strip()
                if attack_var_spider == "атака":
                    spider_attack = int(random.randint(1, 15) * state.hero["defend_bonus"] * state.hero["armour_shid"])
                    attack = int((random.randint(1, 20) + dmg_boost) * state.hero["damage_bonus"])
                    spider_hp -= attack
                    print(f"Вы произвели атаку. Вы нанесли паукам урон в количестве: {attack}. Здоровье пауков: {spider_hp}")
                    state.hero["hp"] -= spider_attack
                    print(f"Пауки атаковали вас. Вам нанесен урон в размере: {spider_attack}. Ваше здоровье: {state.hero["hp"]}")
                    continue
                elif attack_var_spider == "отступление":
                    print("Вы начали отступление.")
                    spider_attack_var = random.choice([True, False])
                    if spider_attack_var == True:
                        spider_attack = int(random.randint(1, 15) * state.hero["defend_bonus"] * state.hero["armour_shild"])
                        state.hero["hp"] -= spider_attack
                        print(f"Пауки догнали вас! Ваше здоровье уменьшено на: {spider_attack}. Ваше здоровье: {state.hero["hp"]}")
                    else:
                        print("Отступление произведено успешно.")
                        continue
                else:
                    print("Неизвестная команда.")
                    continue
            if spider_hp <= 0:
                state.hero["lvl"] += 3
                state.hero["stat_points"] += 3
                print(f"Пауки убиты! Вы успешно прошли событие. Ваш уровень был повышен на 3. Ваш уровень: \
                {state.hero["lvl"]}. Свободные очки улучшения: {state.hero["stat_points"]}")        
    if event_var == "улей":
        bee_hp = 200
        if state.hero["lvl"] < 12:
             print("Для вашего уровня данное событие не доступно")
             return
        else:    
         print("Вы спустились в Улей. Бой начинается")
         while bee_hp > 0:
            if state.hero["hp"] <= 0:
                print("Персонаж убит. Событие провалено.")
                break
            print("Пчелинный рой атакует!")    
            attack_var_bee = input("Что будете делать?(атака или отступление): ").lower().strip()
            if attack_var_bee == "атака":
                attack = int((random.randint(1, 30) + dmg_boost) * state.hero["damage_bonus"])
                bee_attack = int(random.randint(2, 30) * state.hero["defend_bonus"] * state.hero["armour_shild"])
                bee_hp -= attack
                print(f"Вы произвели атаку. Вы нанесли роботу урон в количестве: {attack}. Здоровье пчелинного роя: {bee_hp}")
                state.hero["hp"] -= bee_attack
                print(f"Пчелинный рой атаковал вас. Вам нанесен урон в размере: {bee_attack}. Ваше здоровье: {state.hero["hp"]}")
                continue
            elif attack_var_bee == "отступление":
                print("Вы начали отступление.")
                bee_attack_var = random.choice([True, False])
                if bee_attack_var == True:
                    bee_attack = int(random.randint(2, 30) * state.hero["defend_bonus"] * state.hero["armour_shild"])
                    state.hero["hp"] -= bee_attack
                    print(f"Пчелинный рой догнал вас! Ваше здоровье уменьшено на: {bee_attack}. Ваше здоровье: {state.hero["hp"]}")
                else:
                    print("Отступление произведено успешно.")
                continue
            else:
                print("Неизвестная команда.")
                continue
        if bee_hp <= 0:
                    state.hero["lvl"] += 5
                    state.hero["stat_points"] += 5
                    print(f"Робот убит! Вы успешно прошли событие. Ваш уровень был повышен на 5. Ваш уровень: \
                    {state.hero["lvl"]}. Свободные очки улучшения: {state.hero["stat_points"]}")