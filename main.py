import state
import events
import shop
import activities
import player         
import saver  
import auth
auth.init_db()
ORANGE = "\033[38;2;255;140;0m"  # Чистый темно-оранжевый
B_ORANGE = "\033[38;2;255;69;0m"  # Яркий красно-оранжевый
RESET = "\033[0m"
while True:
    start_choice = input(f"{B_ORANGE}Выберите вариант (вход / регистрация):{RESET} ").lower().strip()
    if start_choice == "регистрация":
        auth.register_user()
    elif start_choice == "вход":
        if auth.login_user(): 
            break
    else:
        print("Неизвестная команда, попробуйте еще раз.")
saver.load_game()
while True:
    command = input("Введите команду: ").lower().strip()
    if command == "привет":
        print(f"И тебе привет, {state.NickName}")

    elif command == "выход":
        player.exit_programm()
        break

    elif command == "статус":
        player.show_status()

    elif command == "бокс":
        player.open_box()

    elif command == "инвентарь":
        player.open_inventory()

    elif command == "охота":
        activities.hantihg()

    elif command == "магазин":
        shop.shop()

    elif command == "экипировать":
        player.equip()    

    elif command == "событие":
        events.event()

    elif command == "загрузить":
        saver.load_game()
    
    elif command == "сохранить":
        saver.save_game()
    
    elif command == "улучшение":
        player.upgade_stats()

    else:
        print("Я не знаю такой команды, попробуйте еще раз")