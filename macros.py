import keyboard
import pyautogui as pg
import time

# button BUY
constX = 1744
constY = 182

# button OK
okX = 962
okY = 576

pg.PAUSE = 0.04

def run():
    print('Press "q" to quit.')
    while True:
        try:
            if keyboard.is_pressed('q'):
                print('Finished')
                break
            else:
                pg.press('f5')
                time.sleep(1.5)
               
                i=0
                while i < 158:
                    if keyboard.is_pressed('q'):
                        print('Finished for click')
                        break
                    
                    pg.click(constX, constY)
                    
                    time.sleep(0.018)
                    pg.press(['Y','Y'], interval=0.01)
                    
                    time.sleep(0.08)
                    pg.click(okX, okY)
                    i=i+1

        except:
            break

if __name__ == "__main__":
    time.sleep(5)
    run()

    # while True:
    #     print(pg.position())
    #     if keyboard.is_pressed('q'):
    #         print('Finished for click')
    #         break