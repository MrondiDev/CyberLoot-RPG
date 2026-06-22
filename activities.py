import state
import random
import time
def hantihg():
     if state.hero["premium"] == False:  
        print("Вы начали охоту. Время для охоты: 30 секунд")
        time.sleep(0.5)
        mine = random.randint(0, 3)
        print(f"Охота завершилась. Ваш заработок: {mine}. Вы можете повысить свой заработок купив подписку премиум")
        state.hero["gold"] += mine
     else:
        print("Вы начали охоту. Время для охоты: 30 секунд")
        time.sleep(30)
        mine_prem = random.randint(1, 10)
        print(f"Охота завершилась. Ваш заработок: {mine_prem}. Вы можете повысить свой заработок купив подписку премиум")
        state.hero["gold"] += mine_prem