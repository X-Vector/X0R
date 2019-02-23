import sys
import platform,os
from urllib2 import *
from platform import system

clear = ""
if "Windows" in platform.system():
	clear = "cls"
if "Linux" in platform.system():
	clear = "clear"
os.system(clear)
is_windows = sys.platform.startswith('win')

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
    plaintext = raw_input("\033[94mEnter Plaintext (key) : \033[94m")
    file_name = raw_input("\033[93mEnter Encrypted File : \033[93m")
    cookies = file(file_name).read()
    cookie = bytearray()
    for i in cookies:
        cookie.append(i)

    xor_key = []
    for i in range(len(plaintext)):
        xor_key.append(chr(cookie[i] ^ ord(plaintext[i])))

    key = "".join(xor_key)

    print "\033[92m[+] Yor Key is : \033[92m",key

    for i in range(len(cookies)):
    	cookie[i] ^= ord(key[i%len(key)])
    print "\033[91m[+] Your Plaintext : \033[91m",cookie
except IOError:
    print "\n\033[91m[-] The File",file_name,"Not Exist\033[91m"
except IndexError:
    print "\n\033[91m[-] Enter Correct Plaintext (Key)\033[91m"
except KeyboardInterrupt:
    print "\n\033[91m[-] GoodBye\033[91m"
