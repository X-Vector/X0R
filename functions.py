import string
import collections
import sets
import base64


def strxor(a, b):
    return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b)])

def from_base64_to_hex(c):
    a = base64.b64decode(c)
    return a.encode("hex").replace("0x","").replace("L","")

# Xor Function
def MTP_hex(ciphers,target_cipher):
    final_key = [None]*150
    known_key_positions = set()
    for current_index, ciphertext in enumerate(ciphers):
    	counter = collections.Counter()
    	for index, ciphertext2 in enumerate(ciphers):
    		if current_index != index:
    			for indexOfChar, char in enumerate(strxor(ciphertext.decode('hex'), ciphertext2.decode('hex'))):
    				if char in string.printable and char.isalpha(): counter[indexOfChar] += 1
    	knownSpaceIndexes = []
    	for ind, val in counter.items():
    		if val >= 7: knownSpaceIndexes.append(ind)
    	xor_with_spaces = strxor(ciphertext.decode('hex'),' '*150)
    	for index in knownSpaceIndexes:
    		final_key[index] = xor_with_spaces[index].encode('hex')
    		known_key_positions.add(index)
    final_key_hex = ''.join([val if val is not None else '00' for val in final_key])
    output = strxor(target_cipher.decode('hex'),final_key_hex.decode('hex'))
    print "\033[91m[+] Your Plaintext : \033[91m" , ''.join([char if index in known_key_positions else '*' for index, char in enumerate(output)])
def MTP_base64(cipher,target_ciphers):
	ciphers = []
	target_cipher = from_base64_to_hex(target_ciphers)
	for i in cipher:
		ciphers.append(from_base64_to_hex(i))
	MTP_hex(ciphers,target_cipher)

def MTP_files(cipher,target_ciphers):
	target_cipher = (open(target_ciphers).read()).encode("hex")
	ciphers = []
	for i in cipher:
		ciphers.append((open(i).read()).encode("hex"))
	MTP_hex(ciphers,target_cipher)

def xor_base64():
    try:
        plaintext = raw_input("\033[94mEnter Plaintext (key) : \033[94m")
        ciphertext = raw_input("\033[94mEnter Cipher : \033[94m")
        ciphertext2 = bytearray(base64.b64decode(ciphertext))

        xor_key = []
        for i in range(len(plaintext)):
            xor_key.append(chr(ciphertext2[i] ^ ord(plaintext[i])))

        key = "".join(xor_key)

        for i in range(len(ciphertext2)):
        	ciphertext2[i] ^= ord(key[i%len(key)])

        print "\033[91m[+] Your Plaintext : \033[91m",ciphertext2

    except TypeError:
        print "\n\033[91m[-] incorrect Encryption\033[91m"
    except IndexError:
        print "\n\033[91m[-] Enter A Part From Plaintext\033[91m"
    except KeyboardInterrupt:
        print "\n\033[91m[-] GoodBye\033[91m"
def xor_file():
    try:
        plaintext = raw_input("\033[94mEnter Plaintext (key) : \033[94m")
        file_name = raw_input("\033[93mEnter Encrypted File : \033[93m")
        ciphertext = file(file_name).read()
        ciphertext2 = bytearray()
        for i in ciphertext:
            ciphertext2.append(i)

        xor_key = []
        for i in range(len(plaintext)):
            xor_key.append(chr(ciphertext2[i] ^ ord(plaintext[i])))

        key = "".join(xor_key)

        for i in range(len(ciphertext)):
        	ciphertext2[i] ^= ord(key[i%len(key)])
        print "\033[91m[+] Your Plaintext : \033[91m",ciphertext2
        f = open("output","w")
        f.write(ciphertext2)
        f.close()
    except IOError:
        print "\n\033[91m[-] The File",file_name,"Not Exist\033[91m"
    except IndexError:
        print "\n\033[91m[-] Enter Correct Plaintext (Key)\033[91m"
    except KeyboardInterrupt:
        print "\n\033[91m[-] GoodBye\033[91m"
def xor_hex():
    try:
        plaintext = raw_input("\033[94mEnter Plaintext (key) : \033[94m")
        ciphertext = raw_input("\033[94mEnter Cipher : \033[94m")
        ciphertext2 = bytearray(ciphertext.decode("hex"))

        xor_key = []
        for i in range(len(plaintext)):
            xor_key.append(chr(ciphertext2[i] ^ ord(plaintext[i])))

        key = "".join(xor_key)
        for i in range(len(ciphertext2)):
        	ciphertext2[i] ^= ord(key[i%len(key)])

        print "\033[91m[+] Your Plaintext : \033[91m",ciphertext2

    except TypeError:
        print "\n\033[91m[-] incorrect Encryption\033[91m"
    except IndexError:
        print "\n\033[91m[-] Enter A Part From Plaintext\033[91m"
    except KeyboardInterrupt:
        print "\n\033[91m[-] GoodBye\033[91m"
