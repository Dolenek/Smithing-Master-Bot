import keyboard
import mss
import numpy as np
import time
import pyautogui
import pygetwindow as gw
import win32api, win32con

# Quality of m�j program :D
sleep = time.sleep

# N�zev aplikace, na kterou chcete aplikovat akce (n�zev okna)
app_name = "Main"

# Z�sk�n� objektu okna aplikace pomoc� n�zvu aplikace
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
        print("1. Zapo�al jsem SOUBOJ")
        time.sleep(2)
    else:
        print("1. Nena�el jsem Challenge Button")

    app_screenshot = np.array(sct.grab((left, top, right, bottom)))
    locationOfSkipButton = pyautogui.locate('SkipButton.PNG', app_screenshot, grayscale=True, confidence=0.6)
    if locationOfSkipButton is not None:
        x, y = locationOfSkipButton.left, locationOfSkipButton.top
        Click(x+20,y+20)
        print("2. Souboj �sp�n� SKIPNUT!")
        sleep(1.5)
    else:
        print("2. Nena�el jsem Skip Button")

    app_screenshot = np.array(sct.grab((left, top, right, bottom))) 
    locationOfVictory = pyautogui.locate('Victory.PNG', app_screenshot, grayscale=True, confidence=0.6)
    if locationOfVictory is not None:
        x, y = locationOfVictory.left, locationOfVictory.top
        Click(x,y)
        print("3. Souboj �sp�n� DOKON�EN!")
        sleep(1.5)
    else:
        print("3. Nena�el jsem Victory")

# Metoda pro hled�n� protiv�ka >:( - SearchingEnemy
def SearchingEnemy(obj):
    print("Jsem u", obj)
    location_of_obj = pyautogui.locate(f'{obj}.PNG', app_screenshot, grayscale=True, confidence=0.6)
    if location_of_obj is not None:
        x, y = location_of_obj.left, location_of_obj.top
        Click(x + 20, y + 20)
        print("Na�el jsem {0} na {1}, {2}".format(obj, x, y))
        time.sleep(1)
        Challenge()
        return True

    return False
        
# Metoda pro hled�n� Objektu :)    - SearchingBlock
def SearchingBlock(obj):
    print("Hled�m", obj)
    location_of_obj = pyautogui.locate(f'{obj}.PNG', app_screenshot, confidence=0.7)
    if location_of_obj is not None:
        x, y = location_of_obj.left, location_of_obj.top
        Click(x + 20, y + 20)
        print("Na�el jsem {0} na {1}, {2}".format(obj, x, y))
        time.sleep(1)
        return True

    return False


# Metoda pro hled�n� Kn�ek etc. :D- SearchingExtra
def SearchingExtra(obj):
    print("Hled�m", obj)
    app_screenshot = np.array(sct.grab((left, top, right, bottom)))
    location_of_obj = pyautogui.locate(f'{obj}.PNG', app_screenshot, grayscale=True, confidence=0.7)
    if location_of_obj is not None:
        x, y = location_of_obj.left, location_of_obj.top
        Click(x + 20, y + 20)
        print("Na�el jsem {0} na {1}, {2}".format(obj, x, y))
        time.sleep(1)
        sleep(1.5)
        Click(261,545)
        sleep(1.5)
        app_screenshot = np.array(sct.grab((left, top, right, bottom)))
        locationOfConfirmButton = pyautogui.locate('ConfirmButton.PNG', app_screenshot, grayscale=True, confidence=0.6)
        if locationOfConfirmButton is not None:
            x, y = locationOfConfirmButton.left, locationOfConfirmButton.top
            Click(x,y)
            sleep(1.5)
            Click(x,y)
            sleep(1.5)
        else:
            print("Nena�el jsem ConfirmButton")
            keyboard.press('ESC') 
        return True

    return False

# Hlavn� Script LOOP
while keyboard.is_pressed('q') == False:
    # Z�sk�n� sou�adnic rohu okna aplikace
    left, top, right, bottom = app_window.left, app_window.top, app_window.right, app_window.bottom

    # �ek� 1 sekundu
    time.sleep(1)

    # Zachytit sn�mek pouze z okna aplikace
    app_screenshot = np.array(sct.grab((left, top, right, bottom)))
    print("Hled�m :D")

    #Hled� klasick� pol��ka
    locationOfNormalBlock = pyautogui.locate('NormalBlock.PNG', app_screenshot, grayscale=True, confidence=0.8)
    if locationOfNormalBlock is not None:
        x, y = locationOfNormalBlock.left, locationOfNormalBlock.top
        Click(x+20, y+20)
        print("Na�el jsem NormalBlock na {0}, {1}".format(x, y))
        time.sleep(0.1)
        continue
    

    #Hled� stra�idla >:(
    if SearchingEnemy("BigEnemy"):
        continue

    if SearchingEnemy("EyeEnemy"):
        continue

    if SearchingEnemy("MainBossEnemy"):
        continue

    if SearchingEnemy("NormalEnemy"):
        continue

    #Hled� Kn�ku :D
    if SearchingExtra("Book"):
        continue

    #Hled� Pillar :D
    SearchingExtra("SealingPillar")

    #Hled� bonusky :)
    if SearchingBlock("BronzeChest"):
        Click(100,100)
        continue
    
    if SearchingBlock("SilverChest"):
        Click(100,100)
        continue

    #if SearchingBlock("GoldenChest"):
    #    Click(100,100)
    #    continue

    if SearchingBlock("VelkaChestka"):
        sleep(3)
        Click(100, 100)
        sleep(3)
        continue

    #Ujist� se, �e se program t�eba jenom nestihl updatnout. Tohle zaji��uje, �e bude muset v�echno checknout je�t� jednou
    RUSure = RUSure + 1
    print(RUSure)
    if RUSure != 2:
        continue

    RUSure = 0
    SearchingBlock("GoNext")

    #Chestky, Pillar
    #Auto chest deployer
    #Memory kter� bude storovat sealnut� effekty (1,2,3)
    #N�jak� memory kam se bude storovat po�et chestek

    #TODO!!!
    #P�id�n� funkce, aby se to neklikalo mou my��, ale ono samo intern�
    #P�id�n� funkce, abych to mohl m�t p�ekryt� ostatn�ma programama a ono to furt fungovalo.

    #P�id�n� v�ce funkc�, automatickej crafting, zab�jen� boss�, Adventure, Taboo
    #Mo�nost v�ce relac� zar�z

