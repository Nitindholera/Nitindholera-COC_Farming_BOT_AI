import pyautogui
import time

class coc_bot:
    def __init__(self):
        self.attack_coordinates = (100, 975)
        self.find_now_coordinates = (1422, 712)
        self.troop_coordinates = (330, 990)
        self.deploy_coordinates = (1665, 835)
        self.surrender_coordinates = (105, 800)
        self.confirm_surrender_coordinates = (1140, 670)
        self.return_home_coordinates = (960, 900)

        self.mid_coordinates = (1920/2, 1080/2)
        self.cart_coordinates = (1220, 70)
        self.cart_collect_coordinates = (1422, 912)

    def attack(self):
        for _ in range(8):
            pyautogui.click(self.attack_coordinates)
            time.sleep(0.2)
            pyautogui.click(self.find_now_coordinates)
            time.sleep(5)
            pyautogui.click(self.troop_coordinates)
            time.sleep(.2)
            pyautogui.click(self.deploy_coordinates)
            time.sleep(.2)
            pyautogui.click(self.surrender_coordinates)
            time.sleep(.2)
            pyautogui.click(self.confirm_surrender_coordinates)
            time.sleep(.2)
            pyautogui.click(self.return_home_coordinates)
            time.sleep(3)
        
    def collect(self):
        for _ in range(5):
            pyautogui.moveTo(self.mid_coordinates)
            pyautogui.scroll(-500)
        
        time.sleep(.2)
        pyautogui.click(self.cart_coordinates)
        time.sleep(.2)
        pyautogui.click(self.cart_collect_coordinates)
        time.sleep(.2)
        pyautogui.click(self.attack_coordinates)
        time.sleep(.2)



if __name__ == '__main__':
    time.sleep(2)
    bot = coc_bot()
    while True:
        bot.attack()
        bot.collect()
    # while True:
    #     print(pyautogui.position())