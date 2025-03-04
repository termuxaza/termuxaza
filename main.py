import os, sys, time, random , json, requests,  itertools, pyfiglet, pwinput, socket
from colorama import Fore, Style, init
from termcolor import colored
from colorama import init
from itertools import cycle
# Colorama-ni ishga tushiramiz
# Har bir qatorni boshqa rangda chiqaramiz
def logo():
    init()
    colors = cycle(["red", "yellow", "green", "cyan", "blue", "magenta"])
    text = "DEPUTAT CPM"
    ascii_art = pyfiglet.figlet_format(text, font="slant")
    for line in ascii_art.split("\n"):
        print(colored(line, next(colors)))
#UI functions
ip_response = requests.get("https://api64.ipify.org?format=json")
ip = ip_response.json()["ip"]
local_ip = socket.gethostbyname(socket.gethostname())
local_ip = socket.gethostbyname(socket.gethostname())
# IP bo'yicha joylashuvni aniqlash
geo_response = requests.get(f"https://ipapi.co/{ip}/json/")
geo_data = geo_response.json()
def print_colored_text(text, hex_color):
    # Hex rangni RGB ga aylantirish
    hex_color = hex_color.lstrip('#')
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)

    # ANSI kodini yaratish
    ansi_code = f"\033[38;2;{r};{g};{b}m{text}\033[0m"
    print(ansi_code)
def get_real_ip():
    response = requests.get("https://api64.ipify.org?format=json")
    ip = response.json()["ip"]
    return ip
def loader():
    animation = [Fore.BLACK+"0%  ━━━━━━━━━━━━━━━━━━━━" ,
                 Fore.LIGHTBLUE_EX+"10%  ━━"+Fore.LIGHTBLACK_EX+"━━━━━━━━━━━━━━━━━━",
                 Fore.LIGHTBLUE_EX+"20%  ━━━━"+Fore.LIGHTBLACK_EX+"━━━━━━━━━━━━━━━━",
                 Fore.LIGHTBLUE_EX+"30%  ━━━━━━"+Fore.LIGHTBLACK_EX+"━━━━━━━━━━━━━━",
                 Fore.LIGHTBLUE_EX+"50%  ━━━━━━━━━━"+Fore.LIGHTBLACK_EX+"━━━━━━━━━━",
                 Fore.LIGHTBLUE_EX+"60%  ━━━━━━━━━━━━"+Fore.LIGHTBLACK_EX+"━━━━━━━━",
                 Fore.LIGHTBLUE_EX+"70%  ━━━━━━━━━━━━━━"+Fore.LIGHTBLACK_EX+"━━━━━━",
                 Fore.LIGHTBLUE_EX+"80%  ━━━━━━━━━━━━━━━━"+Fore.LIGHTBLACK_EX+"━━━━",
                 Fore.LIGHTBLUE_EX+"90%  ━━━━━━━━━━━━━━━━━━"+Fore.LIGHTBLACK_EX+"━━",
                 Fore.LIGHTBLUE_EX+"100%  ━━━━━━━━━━━━━━━━━━━━",
                 ]
    for i in range(len(animation)):
        sys.stdout.write("\r" + Fore.GREEN + animation[i] + Style.RESET_ALL)
        sys.stdout.flush()
        time.sleep(0.1)
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear') 
def success():
    print_colored_text("Success ☆", "#FFDD33")
#Service functions
import socket
import time
def register(email, password):
    clear_screen()
    logo()
    print_colored_text("╭─────────────────────────────────────────────────────────────╮", "#fc2c03")
    print_colored_text("│                      CREATE CPM ACCOUNT                     │","#c72404")
    print_colored_text("╰─────────────────────────────────────────────────────────────╯", "#fc2c03")
    print_colored_text("      ╭───────────────────────────────────────────────────────╮", "#fc2c03"),
    email=input(Fore.LIGHTRED_EX+"Email │ "+Fore.WHITE+"")
    print_colored_text("      ╰───────────────────────────────────────────────────────╯", "#c72404")
    print_colored_text("      ╭───────────────────────────────────────────────────────╮", "#fc2c03")
    password=pwinput.pwinput(prompt=""+Fore.LIGHTRED_EX+"Pass  │ "+Fore.WHITE+"")
    print_colored_text("      ╰───────────────────────────────────────────────────────╯", "#c72404")
    url = 'https://identitytoolkit.googleapis.com/v1/accounts:signUp?key=AIzaSyAe_aOVT1gSfmHKBrorFvX4fRwN5nODXVA'
    payload = {'email': email, 'password': password, 'returnSecureToken': True}
    try:
        response = requests.post(url, json=payload)
        response_data = response.json()
        if response.status_code == 200 and "idToken" in response_data:
            print("Successfuly created ✅")
            return response_data.get('idToken', None)
        else:
            print(f"❌ Error: {response_data.get('error', {}).get('message', 'Noma’lum xatolik')}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"⚠️ Error 2: {e}")
        return None
    register(email, password)
    xtoken = register(email, password)
API_KEY = "AIzaSyAe_aOVT1gSfmHKBrorFvX4fRwN5nODXVA"
FIREBASE_SIGNUP_URL = f"https://identitytoolkit.googleapis.com/v1/accounts:signUp?key={API_KEY}"
def login(email, password):
    url = 'https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key=AIzaSyAe_aOVT1gSfmHKBrorFvX4fRwN5nODXVA'
    payload = {'email': email, 'password': password, 'returnSecureToken': True}
    response = requests.post(url, json=payload)

    if response.status_code == 200:
        return response.json().get('idToken', None)
    return None  
#add_money
def add_money(request):
    url = 'https://us-central1-cp-multiplayer.cloudfunctions.net/SavePlayerRecordsPartially5'
    headers = {"authorization": f"Bearer {request}", "content-type": "application/json"}

    data = {
        "money": 50000000
    }
    response = requests.post(url, headers=headers, json={"data": json.dumps(data)})
    return response.json() if response.status_code == 200 else response.status_code
    clear_screen()
#addcoin
def add_coin(request):
    coin = input(Fore.YELLOW+"[✙]"+Fore.LIGHTYELLOW_EX+" ➤ ENTER"+Fore.RED+" COIN "+Fore.YELLOW+"VALUE"+ ": ")
    url = 'https://us-central1-cp-multiplayer.cloudfunctions.net/SavePlayerRecordsPartially5'
    headers = {"authorization": f"Bearer {request}", "content-type": "application/json"}

    data = {
        "coin": coin,
    }
    response = requests.post(url, headers=headers, json={"data": json.dumps(data)})
    return response.json() if response.status_code == 200 else response.status_code
    clear_screen()
def add_fcoin(request):
    url = 'https://us-central1-cp-multiplayer.cloudfunctions.net/SavePlayerRecordsPartially5'
    headers = {"authorization": f"Bearer {request}", "content-type": "application/json"}

    data = {
        "coin": 30000,
    }
    response = requests.post(url, headers=headers, json={"data": json.dumps(data)})
    return response.json() if response.status_code == 200 else response.status_code
    clear_screen()
#get_king
def get_king(request):
    url = "https://us-central1-cp-multiplayer.cloudfunctions.net/SetUserRating4"
    url_2 = "https://us-central1-cpm-2-7cea1.cloudfunctions.net/SetUserRating4_AppI"
    headers = {
        "accept": "*/*",
        "content-type": "application/json",
        "accept-language": "ru",
        "user-agent": "com.aidana.cardriving.ios/4.8.9 iPhone/16.7.6 hw/iPhone10_6",
        "authorization": f"Bearer {request}",
        "accept-encoding": "gzip, deflate, br"
    }
    dd = {
    "data": "{\"RatingData\" : {\"t_distance\" : 2000000000,\"time\" : 2000000000,\"speed_banner\" : 2000000000,\"gifts\" : 2000000000,\"treasure\" : 2000000000,\"cars\" : 2000000000,\"race_win\" : 999,\"levels\" : 2000000000,\"drift\" : 2000000000,\"run\" : 2000000000,\"police\" : 2000000000,\"block_post\" : 2000000000,\"real_estate\" : 2000000000,\"fuel\" : 2000000000,\"car_trade\" : 2000000000,\"car_exchange\" : 2000000000,\"burnt_tire\" : 2000000000,\"car_fix\" : 2000000000,\"car_wash\" : 2000000000,\"offroad\" : 2000000000,\"passanger_distance\" : 2000000000,\"reactions\" : 2000000000,\"drift_max\" : 2000000000,\"taxi\" : 2000000000,\"delivery\" : 2000000000,\"cargo\" : 2000000000,\"push_ups\" : 2000000000,\"slicer_cut\" : 2000000000,\"car_collided\" : 2000000000,\"new_type\" : 2000000000}}"}
    data = {
        "data":"{\"RatingData\" : {\"t_distance\" : 2000000000,\"time\" : 2000000000,\"speed_banner\": 2000000000,\"gifts\": 2000000000,\"treasure\": 2000000000,\"cars\": 137,\"race_win\" : 999,\"levels\": 82,\"drift\": 2000000000,\"run\": 2000000000,\"police\": 2000000000,\"block_post\": 2000000000,\"real_estate\": 12,\"fuel\": 2000000000,\"car_trade\": 2000000000,\"car_exchange\": 2000000000,\"burnt_tire\": 2000000000,\"car_fix\": 2000000000,\"car_wash\": 2000000000,\"offroad\": 2000000000,\"passanger_distance\": 2000000000,\"reactions\": 2000000000,\"drift_max\": 2000000000,\"texi\": 2000000000,\"delivery\": 2000000000,\"cargo\": 2000000000,\"push_ups\": 2000000000,\"slicer_cut\":1,\"car_collided\":2000,\"new_type\": 2000}"
    }
    clear_screen()
    a = requests.post(url, headers=headers, json=dd)
    return a.text
#custom_id
def custom_id(request):
    custom_input = input(Fore.YELLOW+"[✙]"+Fore.LIGHTYELLOW_EX+" ➤ ENTER"+Fore.YELLOW+" NEW "+Fore.RED+"ID"+ ": ")
    url = 'https://us-central1-cp-multiplayer.cloudfunctions.net/SavePlayerRecordsPartially5'
    headers = {"authorization": f"Bearer {request}", "content-type": "application/json"}

    data = {
        "LocalID": custom_input,
    }
    response = requests.post(url, headers=headers, json={"data": json.dumps(data)})
    return response.json() if response.status_code == 200 else response.status_code
    clear_screen()
def get_all(request):
    url = 'https://us-central1-cp-multiplayer.cloudfunctions.net/SavePlayerRecordsPartially5'
    headers = {
        "accept": "*/*",
        "content-type": "application/json",
        "content-length": "4686",
        "accept-language": "ru",
        "user-agent": "com.aidana.cardriving.ios/4.8.9 iPhone/16.7.6 hw/iPhone10_6",
        "authorization": f"Bearer {request}",
        "accept-encoding": "gzip, deflate, br"
    } 
    xx = {"data":"{\"allData\":\"ios7\",\"boughtFsos\":[1],\"floats\":[169.0,188.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],\"integers\":[1,1,1,1,1,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,15,0,0,0,0,0,0],\"wheels\":[-1,73,74,79,88,84,87,97,98,101]}"}

    a = requests.post(url, headers=headers, json=xx)
    return a
def delete_account(id_token):
    """ Firebase orqali akkauntni o‘chirish """
    url = 'https://identitytoolkit.googleapis.com/v1/accounts:delete?key=AIzaSyAe_aOVT1gSfmHKBrorFvX4fRwN5nODXVA'
    payload = {'idToken': id_token}

    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print("Deleted ✅")
            return True
        else:
            error_message = response.json().get('error', {}).get('message', 'Noma’lum xatolik')
            print(f"❌ Error: {error_message}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"⚠️ Error 2: {e}")
        return False
clear_screen()
logo()
correct_password = "DPTT99"
print(
    Fore.RED+"MANAGER:"+Fore.BLUE+"\nTELEGRAM: "+Fore.CYAN+"@AAF_1000"+Fore.MAGENTA
    )
password = pwinput.pwinput(prompt=""+Fore.LIGHTRED_EX+"ACCESS CODE: "+Fore.LIGHTCYAN_EX, mask="•")
loader()
if password != correct_password:
    clear_screen()
    print("Password incorrect!\nProgramm finished. ❌")
    sys.exit()
else:
    print("Success ✅")
    clear_screen()
""""""
""""""
#Main functions
while True:
 logo()
 print_colored_text("╭─────────────────────────────────────────────────────────────╮", "#fc2c03")
 print_colored_text("│                    LOGIN - CPM ACCOUNT                      │","#c72404")
 print_colored_text("╰─────────────────────────────────────────────────────────────╯", "#fc2c03")
 print_colored_text("      ╭───────────────────────────────────────────────────────╮", "#fc2c03"),
 email=input(Fore.LIGHTRED_EX+"Email │ "+Fore.WHITE+"")
 print_colored_text("      ╰───────────────────────────────────────────────────────╯", "#c72404")
 print_colored_text("      ╭───────────────────────────────────────────────────────╮", "#fc2c03")
 password=pwinput.pwinput(prompt=""+Fore.LIGHTRED_EX+"Pass  │ "+Fore.WHITE+"")
 print_colored_text("      ╰───────────────────────────────────────────────────────╯", "#c72404")
 token = login(email, password)
 time.sleep(2)
 clear_screen()
 print(Fore.LIGHTWHITE_EX+"Login! \n")
 loader()
 if not token:
        clear_screen()
        print(Fore.RED+"Email or Password incorrec!"+Fore.LIGHTWHITE_EX+"\nTry again.")
        time.sleep(1.5)
        clear_screen()
 else:
        print(Fore.GREEN+"Login successful! ✅")
        break
clear_screen()

balance = Fore.GREEN+"UNLIMITED"
status = Fore.GREEN+"DEPUTAT"
while True:
    clear_screen()
    logo()
    print_colored_text(f" - Email: {Fore.RED+email}","#f79900")
    print_colored_text(f" - Password: {Fore.RED+password}","#f79900")
    print_colored_text(f" - Real IP adrress: {Fore.GREEN+get_real_ip()}","#f79900")
    print_colored_text(f" - Country: {Fore.GREEN+geo_data.get('country_name', 'Unknown')}"+f", {Fore.GREEN+geo_data.get('city','Unknown')}", "#d18100")
    print_colored_text(f" - Balance: {balance} "+Fore.WHITE+"│"+f" {status}","#f79900")
    print_colored_text("╭─────────────────────────────────────────────────────────────╮", "#d18100")
    print_colored_text("│                        CPM SERVICES                         │","#cc7e00")
    print_colored_text("├──────────────────────────────┬┬─────────────────────────────┤","#804f00")
    print_colored_text("│ [1] ➤ INJECT MONEY           ││  [2] ➤ INJECT COIN          │","#694102")
    print_colored_text("│ [3] ➤ KING RANK              ││  [4] ➤ CUSTOM ID            │","#694102")
    print_colored_text("│ [5] ➤ UNLOCK ALL             ││  [6] ➤ REGISTER ACCOUNT     │","#875403")
    print_colored_text("│ [7] ➤ DELETE ACCOUNT         ││  [0] ➤ EXIT                 │","#875403")
    print_colored_text("├──────────────────────────────┴┴─────────────────────────────┤","#804f00")
    print_colored_text("│                    CARS WILL NOT OPEN!                      │","#cc7e00")
    print_colored_text("╰─────────────────────────────────────────────────────────────╯", "#d18100")
    command=input(Fore.YELLOW+"[✙]"+Fore.LIGHTYELLOW_EX+" ➤  YOUR CHOICE: ")
    if command.lower() == "0":
        print(Fore.RED + "Programm finished")
        clear_screen()
        break
    if command.lower() == "1":
        add_money(token)
        success()
        time.sleep(2)
        clear_screen()
    if command.lower() == "2":
        add_coin(token)
        success()
        time.sleep(2)
        clear_screen()
    if command.lower() == "3":
        get_king(token)
        success()
        time.sleep(2)
        clear_screen()
    if command.lower() == "4":
        custom_id(token)
        success()
        time.sleep(2)
        clear_screen()
    if command.lower() == "5":
        get_all(token)
        success()
        time.sleep(2)
        clear_screen()
    if command.lower() == "6":
        xtoken = register(email,password)
        add_money(xtoken)
        add_fcoin(xtoken)
        get_king(xtoken)
        get_all(xtoken)
    if command.lower() == "7":
        delete_account(token)
        success()
