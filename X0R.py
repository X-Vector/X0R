import os,platform,sys
from urllib2 import *
clear = ""
if "Windows" in platform.system():
	clear = "cls"
if "Linux" in platform.system():
	clear = "clear"
os.system(clear)
is_windows = sys.platform.startswith('win')

def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(4. / 100)

# Console Colors
if is_windows:
    # Windows deserves coloring too :D
    G = '\033[92m'  # green
    Y = '\033[93m'  # yellow
    B = '\033[94m'  # blue
    R = '\033[91m'  # red
    W = '\033[0m'   # white
    try:
        import win_unicode_console , colorama
        win_unicode_console.enable()
        colorama.init()
        #Now the unicode will work ^_^
    except:
        print("[!] Error: Coloring libraries not installed, no coloring will be used")
        G = Y = B = R = W = G = Y = B = R = W = ''


else:
    G = '\033[92m'  # green
    Y = '\033[93m'  # yellow
    B = '\033[94m'  # blue
    R = '\033[91m'  # red
    W = '\033[0m'   # white


def banner():
    print("""%s

##     ##   #####   ########
 ##   ##   ##   ##  ##     ##
  ## ##   ##     ## ##     ##
   ###    ##     ## ########
  ## ##   ##     ## ##   ##
 ##   ##   ##   ##  ##    ##
##     ##   #####   ##     ##

  %s%s
[ Author  : X-Vector ]\033[96m
[ Github  : github.com/X-Vector ]\033[93m
[ Twitter : twitter.com/@XVector11 ]\033[95m
[ Facebook: facebook.com/X.Vector1 ]\033[95m
    """ % (R, W,R))

banner()

try:
	from functions import *
	print """
[1] Known Plain Text Attack
[2] Many Time Pad Attack
	"""

	check1 = int(raw_input(">>> "))
	if check1 == 1:
		os.system("clear")
		banner()
		print """
\n\033[91m[~] Known Plain Text Attack\033[95m

[1] File Xored
[2] Base64 String Xored
[3] Hex String Xored
		"""
		choose = int(raw_input(">>> "))
		if choose == 1:
			xor_file()
		elif choose == 2:
			xor_base64()
		elif choose == 3:
			xor_hex()
		else :
			print "\n\033[91m[-] invalid Choose\033[91m"
	elif check1 == 2:
		os.system("clear")
		banner()
		print """
\n\033[91m[~] Many Time Pad Attack\033[95m

[1] File Xored
[2] Base64 String Xored
[3] Hex String Xored
"""
		check = int(raw_input(">>> "))
		if check == 1:
			ciphers = []
			number_of_cipher = int(raw_input("How Many File : "))
			i = 0
			print ("[~] Enter Path of Files")
			while(i < number_of_cipher):
				c = raw_input(">>> ")
				ciphers.append(c)
				i = i+1
			target_cipher = raw_input("Enter Target File : ")
			MTP_files(ciphers,target_cipher)

		elif check == 2:
			ciphers = []
			number_of_cipher = int(raw_input("How Many Cipher : "))
			print ("[~] Enter Cipher")
			i = 0
			while(i < number_of_cipher):
				c = raw_input(">>> ")
				ciphers.append(c)
				i = i+1
			target_cipher = raw_input("Enter Target Cipher : ")
			MTP_base64(ciphers,target_cipher)

		elif check == 3:
			ciphers = []
			number_of_cipher = int(raw_input("How Many Cipher : "))
			print ("[~] Enter Cipher")
			i = 0
			while(i < number_of_cipher):
				c = raw_input(">>> ")
				ciphers.append(c)
				i = i+1
			target_cipher = raw_input("Enter Target Cipher : ")
			MTP_hex(ciphers,target_cipher)

except KeyboardInterrupt:
	print "\n\033[91m[-] GoodBye\033[91m"
except IOError:
	print "\n\033[91m[-] Files Name/Path Wrong\033[91m"
except TypeError:
	print "\n\033[91m[-] incorrect Encryption\033[91m"
except ImportError:
	slowprint("\n\033[91m[-] Module Not Installed Well \033[91m")
	slowprint("\n[~] Try \033[93msudo pip install requirement.txt")
except :
	print "\n\033[91m[-] invalid Choose\033[91m"

