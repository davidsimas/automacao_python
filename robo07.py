import pyautogui as p


p.hotkey('win', 'r')
p.sleep(1)
p.write('C://python//RPA.pbix')
p.sleep(1)
p.press("enter")
p.sleep(30)
p.click(x=875, y=129)
p.sleep(5)
p.click(x=999, y=880)
p.sleep(10)