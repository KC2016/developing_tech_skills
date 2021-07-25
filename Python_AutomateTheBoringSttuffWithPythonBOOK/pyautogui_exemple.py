import pyautogui
# print(pyautogui.size())
# print(pyautogui.position())
print(pyautogui.moveTo(10,10))
print(pyautogui.moveTo(10,10, duration = 1.5))  # esta desabilitado, eu nao quis habilitar
print(pyautogui.moveRel(200,0))
print(pyautogui.moveRel(200,0, duration=2))
print(pyautogui.moveRel(0,-100))
print(pyautogui.moveRel(0,-100, duration=1))
print(pyautogui.click(339,38))
print(pyautogui.click())