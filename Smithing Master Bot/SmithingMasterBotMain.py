from itertools import repeat
import keyboard
import mss
import numpy as np
import time
import pyautogui
import pygetwindow as gw
import win32api, win32con

# Quality of můj program :D
sleep = time.sleep

# Název aplikace, na kterou chcete aplikovat akce (název okna)
app_name = "Main"

# Získání objektu okna aplikace pomocí názvu aplikace
app_window = gw.getWindowsWithTitle(app_name)[0]

# Inicializace
sct = mss.mss()
RUSure = 0

# Metoda Click 
def Click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

# Metoda pro souboj                - Challenge
def Challenge():
    sleep(1)
    app_screenshot = np.array(sct.grab((left, top, right, bottom)))
    locationOfChallengeButton = pyautogui.locate('ChallengeButton.PNG', app_screenshot, grayscale=True, confidence=0.6)
    if locationOfChallengeButton is not None:
        x, y = locationOfChallengeButton.left, locationOfChallengeButton.top
        Click(x+10,y+10)
        print("1. Započal jsem SOUBOJ")
        time.sleep(2)
    else:
        print("1. Nenašel jsem Challenge Button")

    app_screenshot = np.array(sct.grab((left, top, right, bottom)))
    locationOfSkipButton = pyautogui.locate('SkipButton.PNG', app_screenshot, grayscale=True, confidence=0.6)
    if locationOfSkipButton is not None:
        x, y = locationOfSkipButton.left, locationOfSkipButton.top
        Click(x+20,y+20)
        print("2. Souboj úspěšně SKIPNUT!")
        sleep(1.5)
    else:
        print("2. Nenašel jsem Skip Button")

    app_screenshot = np.array(sct.grab((left, top, right, bottom))) 
    locationOfVictory = pyautogui.locate('Victory.PNG', app_screenshot, grayscale=True, confidence=0.6)
    if locationOfVictory is not None:
        x, y = locationOfVictory.left, locationOfVictory.top
        Click(x,y)
        print("3. Souboj úspěšně DOKONČEN!")
        sleep(1.5)
    else:
        print("3. Nenašel jsem Victory")

# Metoda pro hledání protiváka >:( - SearchingEnemy
def SearchingEnemy(obj):
    print("Jsem u", obj)
    location_of_obj = pyautogui.locate(f'{obj}.PNG', app_screenshot, grayscale=True, confidence=0.6)
    if location_of_obj is not None:
        x, y = location_of_obj.left, location_of_obj.top
        Click(x + 20, y + 20)
        print("Našel jsem {0} na {1}, {2}".format(obj, x, y))
        time.sleep(1)
        Challenge()
        return True

    return False
        
# Metoda pro hledání Objektu :)    - SearchingBlock
def SearchingBlock(obj):
    print("Hledám", obj)
    location_of_obj = pyautogui.locate(f'{obj}.PNG', app_screenshot, confidence=0.7)
    if location_of_obj is not None:
        x, y = location_of_obj.left, location_of_obj.top
        Click(x + 20, y + 20)
        print("Našel jsem {0} na {1}, {2}".format(obj, x, y))
        time.sleep(1)
        return True

    return False


# Metoda pro hledání Knížek etc. :D- SearchingExtra
def SearchingExtra(obj):
    print("Hledám", obj)
    app_screenshot = np.array(sct.grab((left, top, right, bottom)))
    location_of_obj = pyautogui.locate(f'{obj}.PNG', app_screenshot, grayscale=True, confidence=0.7)
    if location_of_obj is not None:
        x, y = location_of_obj.left, location_of_obj.top
        Click(x + 20, y + 20)
        print("Našel jsem {0} na {1}, {2}".format(obj, x, y))
        time.sleep(1)
        sleep(1.5)
        Click(261,470)
        sleep(1.5)
        app_screenshot = np.array(sct.grab((left, top, right, bottom)))
        locationOfConfirmButton = pyautogui.locate('ConfirmButton.PNG', app_screenshot, confidence=0.6)
        if locationOfConfirmButton is not None:
            x, y = locationOfConfirmButton.left, locationOfConfirmButton.top
            Click(x,y)
            sleep(1.5)
            Click(x,y)
            sleep(1.5)
        else:
            print("Nenašel jsem ConfirmButton")
            keyboard.press('ESC') 
        return True

    return False

# Hlavní Script LOOP
while keyboard.is_pressed('q') == False:
    # Získání souřadnic rohu okna aplikace
    left, top, right, bottom = app_window.left, app_window.top, app_window.right, app_window.bottom

    # Čeká 1 sekundu
    time.sleep(1)

    # Zachytit snímek pouze z okna aplikace
    app_screenshot = np.array(sct.grab((left, top, right, bottom)))
    print("Hledám :D")

    #Hledá klasické políčka
    locationOfNormalBlock = pyautogui.locate('NormalBlock.PNG', app_screenshot, grayscale=True, confidence=0.8)
    if locationOfNormalBlock is not None:
        x, y = locationOfNormalBlock.left, locationOfNormalBlock.top
        Click(x+20, y+20)
        print("Našel jsem NormalBlock na {0}, {1}".format(x, y))
        time.sleep(0.2)
        continue
        
    

    #Hledá strašidla >:(
    if SearchingEnemy("BigEnemy"):
        continue

    if SearchingEnemy("EyeEnemy"):
        continue

    if SearchingEnemy("MainBossEnemy"):
        continue

    if SearchingEnemy("NormalEnemy"):
        continue

    #Hledá Knížku :D
    if SearchingExtra("Book"):
        continue

    #Hledá Pillar :D
    SearchingExtra("SealingPillar")

    #Hledá bonusky :)
    if SearchingBlock("BronzeChest"):
        Click(100,100)
        continue
    
    if SearchingBlock("SilverChest"):
        Click(100,100)
        continue

    if SearchingBlock("GoldenChest"):
        Click(100,100)
        continue

    if SearchingBlock("VelkaChestka"):
        sleep(3)
        Click(100, 100)
        sleep(3)
        continue

    #Ujistí se, že se program třeba jenom nestihl updatnout. Tohle zajišťuje, že bude muset všechno checknout ještě jednou
    RUSure = RUSure + 1
    print(RUSure)
    if RUSure != 2:
        continue

    RUSure = 0
    SearchingBlock("GoNext")

    #Chestky, Pillar
    #Auto chest deployer
    #Memory která bude storovat sealnutý effekty (1,2,3)
    #Nějaká memory kam se bude storovat počet chestek

    #TODO!!!
    #Přidání funkce, aby se to neklikalo mou myší, ale ono samo interně
    #Přidání funkce, abych to mohl mít překryté ostatníma programama a ono to furt fungovalo.

    #Přidání více funkcí, automatickej crafting, zabíjení bossů, Adventure, Taboo
    #Možnost více relací zaráz

