import hashlib

flag = 0
pass_hash = input("enter md5 hash: ")
wordlist = input("file name:")
try:
    pass_file = open (wordlist,"r")
except:
    print("file not found")
    quit()
for word in pass_file:
    enc_wrd = word.encode('utf-8')
    digest = hashlib.md5(enc_wrd.strip()).hexdigest()

    if digest == pass_hash:
        print("password found")
        print("password is " + word)

        break
if flag == 0:
    print("password/passphrase is not in list")