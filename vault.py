#!/usr/bin/python3
import requests, os, time, platform
from getpass import getpass

url = "https://anikin-api.herokuapp.com/AL104_hash/al104_hash_api.php"

dds = {'a':'<->','b':'<|>','c':'<#>','d':'<h>','e':'<!>','f':'<X>','g':'<+>','h':'<&>','i':'<_>','j':'<@>','k':'<.>','l':'<*>','m':'<z>','n':'<^>','o':'<%>','p':'<~>','q':'<=>','r':'</>','s':'<?>','t':'<[>','u':'<]>','v':'<{>','w':'<}>','x':'<(>','y':'<)>','z':'<$>',' ':'###','1':'>5<','2':'>0<','3':'>7<','4':'>9<','5':'>6<','6':'>8<','7':'>3<','8':'>4<','9':'>1<','0':'>2<','!':'x-x','#':'k-k','@':'y>p','$':'4-A','%':'i~n','^':'ala','&':'kyu','*':'nin','(':'jaz',')':'y~~','-':'&ko','+':'&ka','{':'uwu','}':'owo','[':'Y.Y',']':'T.T','\\':')X(','/':'(x)','~':'exe','`':'det','.':'t%t',',':'bee','?':'que','<':'-l-','>':'-r-',"'":'~wu','"':'~~w','=':'*6*','_':';-;',':':'^*^',';':'@=@','A':'=->','B':'=|>','C':'=#>','D':'=H>','E':'=!>','F':'=X>','G':'=+>','H':'=&>','I':'=_>','J':'=@>','K':'=.>','L':'=*>','M':'=Z>','N':'=^>','O':'=%>','P':'=~>','Q':'==>','R':'=/>','S':'=?>','T':'=[>','U':'=]>','V':'={>','W':'=}>','X':'=(>','Y':'=)>','Z':'=$>'}
ddz = {'<->':'a','<|>':'b','<#>':'c','<h>':'d','<!>':'e','<X>':'f','<+>':'g','<&>':'h','<_>':'i','<@>':'j','<.>':'k','<*>':'l','<z>':'m','<^>':'n','<%>':'o','<~>':'p','<=>':'q','</>':'r','<?>':'s','<[>':'t','<]>':'u','<{>':'v','<}>':'w','<(>':'x','<)>':'y','<$>':'z','###':' ','>5<':'1','>0<':'2','>7<':'3','>9<':'4','>6<':'5','>8<':'6','>3<':'7','>4<':'8','>1<':'9','>2<':'0','~~w':'"','~wu':"'",'-r-':'>','-l-':'<','que':'?','bee':',','t%t':'.','det':'`','exe':'~',')X(':'\\','(x)':'/','T.T':']','Y.Y':'[','owo':'}','uwu':'{','&ka':'+','&ko':'-','y~~':')','jaz':'(','nin':'*','kyu':'&','ala':'^','i~n':'%','4-A':'$','y>p':'@','k-k':'#','x-x':'!','*6*':'=',';-;':'_','^*^':':','@=@':';','=->':'A','=|>':'B','=#>':'C','=H>':'D','=!>':'E','=X>':'F','=+>':'G','=&>':'H','=_>':'I','=@>':'J','=.>':'K','=*>':'L','=Z>':'M','=^>':'N','=%>':'O','=~>':'P','==>':'Q','=/>':'R','=?>':'S','=[>':'T','=]>':'U','={>':'V','=}>':'W','=(>':'X','=)>':'Y','=$>':'Z'}

def encode(ui):
	msg_all = ''
	for charz in ui:
		x = dds.get(charz)
		msg_all+=x
	return msg_all


def decode(x):
	msg_all=''
	code=[]
	s_code=''
	count=3
	x+=' '
	for charz in x:
		if count<1:
			count=3
			code.append(s_code)
			s_code=''
		count-=1
		s_code+=charz
	for sym in code:
		decoded = ddz.get(sym)
		msg_all+=str(decoded)

	return msg_all


def al104(string, hazsh):
	r = requests.post(url, data={'string':string,'hash':hazsh})
	if(r.text=='true'):
		return True
	else:
		return False


def clear():
	if('Windows' in platform.platform()):
		os.system('cls')
	else:
		os.system('clear')


def add_dat():
	name = input('Enter data name: ')
	value = input('Enter value: ')
	data = open('./.datz.dat','a')
	content = encode(f"{name}:{value}")
	data.write(content+'\n')
	data.close()
	print('='*30)
	print('Done!')
	time.sleep(.7)
	clear()


def view_dat():
	clear()
	data = open('./.datz.dat').read().splitlines()
	for values in data:
		print(f'{decode(values)}')
	print('='*30)

def menu():
	while True:
		print("""
 [1] == Add data
 [2] == View data
 [0] == Exit
			""")
		ui = input('~> ')
		if(ui=='1'):
			add_dat()
		elif(ui=='2'):
			view_dat()
		elif(ui=='0'):
			clear()
			os._exit(0)
			break
		else:
			print('Err!')
			time.sleep(.7)
			clear()


def login():
	while True:
		clear()
		ui = getpass('Enter password: ')
		vault_lock = open('.vault_.lock').read().strip()
		status = al104(ui, vault_lock)
		if(status):
			clear()
			menu()
			break
		else:
			print('Incorrect!')
			time.sleep(.7)


def check():
	clear()
	if(os.path.exists('.vault_.lock')):
		login()
	else:
		while True:
			print('Pls setup a new vault password')
			password = getpass('New password: ')
			passwordc = getpass('Retype new password: ')
			if(password==passwordc):
				r = requests.post(url, data={'encode':password})
				if(r.status_code==200):
					lock = open('.vault_.lock','w')
					lock.write(str(r.text))
					login()
			else:
				print('\nError! retype password does not match!\n[Try again!]\n')


if(__name__=="__main__"):
	check()

