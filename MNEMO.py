## Mnemonic NEMO written by Wiktor ##
import os
import sys
import subprocess
import pbkdf2
import binascii
import hashlib
print('                    _,;_;/-",_,','\n','                 ,")  (  ((O) "  .`,','\n'
      ,'               ,` (    )  ;  -.,/;`}','\n','             ,"  o    (  ( (  . -_-.','\n',
      '            `.  ;      ;  ) ) \`; \;','\n','              `., )   (  ( _-`   \,','\n'
      ,"                 ","`'-,,`.jb",'\n')

print('   __  __                                  _        _   _ ','\n',
      ' |  \/  |                                (_)      | \ | |','\n',
      ' | \  / |_ __   ___ _ __ ___   ___  _ __  _  ___  |  \| | ___ _ __ ___   ___ ','\n',
      " | |\/| | '_ \ / _ \ '_ ` _ \ / _ \| '_ \| |/ __| | . ` |/ _ \ '_ ` _ \ / _ \"",'\n',
      " | |  | | | | |  __/ | | | | | (_) | | | | | (__  | |\  |  __/ | | | | | (_) |",'\n',
      " |_|  |_|_| |_|\___|_| |_| |_|\___/|_| |_|_|\___| |_| \_|\___|_| |_| |_|\___/ ",'\n',)
print('Enter up to 12 word Mnemonic phrase to get treasure')

##target p2sh adress 37XTVuaWt1zyUPRgDDpsnoo5ioHk2Da6Fs
keylist=[]
target='37XTVuaWt1zyUPRgDDpsnoo5ioHk2Da6Fs'##real target
##target='3CFPiwC5zvf7BJQkTWwKC6rGZ4eVnG4SZv'##key abandon zoo zebra 
v=''
def genkey(v):##v is output of nemo hex of secret exponent 
    come='ku '##options for Ku -a= adress 
    tamp=[come,v]
    throw=''.join(tamp)
    throw=throw.replace("'",'')
    ##print(throw) debug to print whats being thrown to ku 
    process = subprocess.Popen(throw, stdout=subprocess.PIPE)
    output, error = process.communicate()
    clean=output.split()
    fak=clean
    c=''.join(str(e)for e in clean)##fancy way to get numbers and str
    d=c.split("'")
    e=c#lenth should always be the same
    F=str(d[161:-11])##161:-11 is where the ouput of ku has the p2sh adress 
    F=F.replace("'",'')
    F=F.replace('[','')
    F=F.replace(']','')
    keylist.append(F)
    print(F)
    if F == target:
        print('FOUND KEY')
    

def Nemo(user):
    #tocomp=input()
    tocomp=user
    whole=[]
    
    def wordlist():
        
        file=open('./Bip39wordlist.txt').read().split('\n')##for some reason without .read() it skips every other line
        ##print('initializing wordlist....')
        for line in file:##this reads one line at a time and adds it to $whole
            whole.append(line)
        
        
        
    
    wordlist()
    indexes=[]
    ##print(whole)
    have=tocomp.split()##change input into list of words
    for to in have:#for words in input
        for inx, i in enumerate(whole):#compare input to wordlist
            if to == i:
                ##print(inx,i)##loop basicly ignores anything that dosent match
                indexes.append(inx)
    print(len(indexes),'Words Accepted') ##lenth of index table for accepted words= number of words that match the wordlist
    ##basicly lets u know if u spelled a word wrong 
    ##print(indexes)
    ##the entropy is made by taking the index of the word into binary then into hex
    you_seen=[]
    my_son=[]
    table=[]
    swim=[]
    for i in indexes:#word indexes used to make entropy? or the other way around idno
        j=bin(i)[2:].zfill(11)
        you_seen.append(j)
        table.append(i)

    for i in you_seen:#makes bytes for entropy
        #he_looks_like_me=hex(int(i))#works but wrong base?
        m=int(i).to_bytes(5, byteorder='big')#first arg is number of \00\00 things so 2 here any less than 5 and it cries
        #he_looks_like_me=binascii.hexlify(m)
        he_looks_like_me=m
        d=binascii.hexlify(he_looks_like_me)
        my_son.append(d)
    #print(have,you_seen,indexes,my_son)

    #u seen is binary of indexes
    #orange fish is binary of index   
    orange_fish=str(you_seen)
    orange_fish=orange_fish.replace(',','')
    orange_fish=orange_fish.replace('[','')
    orange_fish=orange_fish.replace(']','')
    orange_fish=orange_fish.replace("'",'')
    Dory=''.join(orange_fish)
    swimming=str(my_son)
    swimming=swimming.replace(',','')
    swimming=swimming.replace('[','')
    swimming=swimming.replace(']','')
    swimming=swimming.replace("'",'')
    #swimming is hex of index
    U=table
    wam=[]
    wam2=[]
    wam3=[]
    wam4=[]
    for idx,i in enumerate(U):##takes every 3 word indexes adds then to a wam 
        if idx<=3:
            wam.append(i)
        elif 3<idx<=6:
            wam2.append(i)
        elif 6<idx<=9:
            wam3.append(i)
        elif 9<idx<=12:
            wam4.append(i)
        elif idx>14:
            print('ERROR out of range')
            print(idx)
        


    chunk1=hex(sum(wam))##sums every set of wam into hex
    chunk2=hex(sum(wam2))
    chunk3=hex(sum(wam3))
    chunk4=hex(sum(wam4))
    ent=[chunk1,chunk2,chunk3,chunk4]
    toprint=ent
    printable=''
    printable=printable.join(toprint)
    printable=printable.replace('0x','')##for some reason hex outputs 0x infront of everything
    entropyhex=printable
    


    print(printable,'compressed entropy Hexadecimal')
    ##hmac sha256 hashing down there
    wallaby=list(entropyhex)
    wallaby=bytes(str(wallaby),'UTF-8')
    sydney=hashlib.pbkdf2_hmac('sha256',wallaby,b'mnemonic',2048)
    mine=binascii.hexlify(sydney)
    ##print('hex seed \n',mine)
    last=str(mine)##LAST IS OUPUT OF NEMO
    #genkey(last[1:])##PASSES VALUE OF HASH TO KU COMMAND LINE TO GENERATE A BITCOIN ADRESS
    genkey(entropyhex)##instead of hash uses raw entorpy in hex
    ##debug printouts
    ##print(entropyhex)##compressed entropy
    ##print(mine)##hmac sha256 hash of entropyhex
    
##    for idx,i in enumerate(keylist):##compare generated adresses to target
##        if i == target:
##            print('FOUND IT MUTHER FUCKER!!!!!!!!')


##    dk = hashlib.pbkdf2_hmac('sha256',he_looks_like_me, b'salt', 2048)##hashing function 
##    test=binascii.hexlify(dk)##test for hashlib
##    print(test)


##    test=bytes('test','UTF-8')
##    H=hashlib.sha256(test)
##    ##H.update(test)
##    H.hexdigest()
##    print(H)
while True:
    Nemo(user=input())
    
##Nemo(user=input())



