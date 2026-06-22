import state
def shop():
    shop_variant = input("Что вы хотите сделать?(купить/продать): ").lower().strip()
    if shop_variant == "купить":
        print("Вы вошли в магазин. Варианты для покупки: Премиум(20 золотых), меч(5 золотых), ВСС(30 золотых), Зелье(2 золотых), \
        ПМ(10 золотых), туристический рюкзак(30 золотых)") 
        shop_var = input("Введите вариант, который вы хотите купить: ").lower().strip()
        if shop_var == "премиум":
            if state.hero["gold"] < 20:
                print("Ваш баланс меньше 20. Покупка не может быть совершена")
                return
            else:
                state.hero["premium"] = True
                state.hero["gold"] -= 20
                print(f"Премиум подписка была куплена. Ваш баланс: {state.hero["gold"]} Ваш заработок на охоте был увеличен.")
                return
        if len(state.hero["inventory"]) < state.hero["max_slots"]:
            if shop_var == "меч":
                if state.hero["gold"] < 5:
                    print("Недостаточно средств")
                    return
                else:
                    state.hero["gold"] -= 5
                    state.hero["inventory"].append("МЕЧ")
                    print(f"Вы успешно купили предмет меч. Ваш баланс: {state.hero["gold"]}")
            elif shop_var == "всс":
                if state.hero["gold"] < 30:
                    print("Недостаточно средств")
                    return
                else:
                    state.hero["gold"] -= 30
                    state.hero["inventory"].append("ВСС")
                    print(f"Вы успешно купили предмет ВСС. Ваш баланс: {state.hero["gold"]}")
            elif shop_var == "зелье":
                if state.hero["gold"] < 2:
                    print("Недостаточно средств")
                    return
                else:
                    state.hero["gold"] -= 2
                    state.hero["inventory"].append("зелье")
                    print(f"Вы успешно купили предмет зелье. Ваш баланс: {state.hero["gold"]}")
            elif shop_var == "пм":
                if state.hero["gold"] < 10:
                    print("Недостаточно средств")
                    return
                else:
                    state.hero["gold"] -= 10
                    state.hero["inventory"].append("ПМ")
                    print(f"Вы успешно купили предмет ПМ. Ваш баланс: {state.hero["gold"]}")
            elif shop_var == "туристический рюкзак":
                if state.hero["gold"] < 30:
                    print("Недостаточно средств")
                    return
                else:
                    state.hero["gold"] -= 30
                    state.hero["inventory"].append("туристический рюкзак")
                    print(f"Вы успешно купили предмет туристический рюкзак. Ваш баланс: {state.hero["gold"]}")
            else:
                print("данного предмета нет в магазине.")
                return
        else:
            print("Ваш рюкзак полон. Предмет не может быть куплен")
            return
    if shop_variant == "продать":
        print("Вы вошли в меню скупщика. Выберите предмет, который вы хотите продать")
        print(f"Ваш инвентарь: {state.hero["inventory"]}")
        sell_var = input("Введите вариант для продажи: ")
        if sell_var.upper() in state.hero["inventory"]:
            sell_var = sell_var.upper()
        elif sell_var.lower() in state.hero["inventory"]:
            sell_var = sell_var.lower()
        else:
            print("У вас нет такого предмета!")
            return
        if sell_var in state.loot_prices:
            state.hero["gold"] += state.loot_prices[sell_var]
            state.hero["inventory"].remove(sell_var)
            print(f"Вы продали скупщику предмет {sell_var} и получили за него {state.loot_prices[sell_var]} золота.")
        else:
            print("Скупщик не покупает данный предмет!")
            return