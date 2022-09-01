import pyautogui as m
import random
import time

chrome_button = {
    'top_left' : {'x' : 50, 'y' :27},
    'bottom_right' : {'x' : 1800, 'y' :1000}
}
while True:
    #random.uniform(src, dst) = src < (float) random_value <dst
    x = random.uniform(chrome_button['top_left']['x'], chrome_button['bottom_right']['x'])
    y = random.uniform(chrome_button['top_left']['y'], chrome_button['bottom_right']['y'])


    m.moveTo(x, y,2) #~동안에 = 2초 간 x와 y의 좌표로 이동
    # m.typewrite('naver.com')
    
    m.press('ctrl')
    time.sleep(5)
