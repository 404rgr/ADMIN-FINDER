#######################################
"""
	    Mau Ngapain?
	      Record ?
	  Ga tau malu kau,
	izin dulu kek su :v
	Wa : 0895320325423
"""
#######################################
#import module
import sys
import requests
import time
import random
import os

# Warna ! Color
B = '\033[1;34m'  #Blue   ! Biru
R = '\033[31m'    #Red    ! Merah
G = '\033[32m'    #Green  ! Hijau
W = '\033[0m'     #White  ! Putih
Y = '\033[33;5m'  #Yellow ! Kuning
P = '\033[95m'    #Purple ! Ungu
C = '\033[36;1m'  #Cyan   !

lo = " Masukan Target"+R+" ["+B+" Tanpa https / http"+R+" ]\n "+B+"Contoh:"+G+" raocyte.online"+C
targetgan = R+"["+C+"Target"+R+"]"+G+" => "+C

def ketik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.01)

def banner():
	os.system("clear")
	print Y+"""
	           0000000
        	 00       00
	        0"""+R+"""  ()  () """+Y+"""  0
	       0             0
	        0 """+R+"""  @@@@ """+Y+"""   0
	       0 00       00 0
	     0     0     0     00
	    0 ------------------- 0
	     0 """+G+""" Coded By Zeerx7"""+Y+"""  0
	      \  """+G+"""Rao Cyber Team """+Y+"""/
	     """+P+""" -------------------
	     | """+C+"""   Admin Finder """+P+"""  |
              ~~~~~~~~~~~~~~~~~~~
	"""+B

def go():
	banner()
	ketik(lo)
	target = raw_input(targetgan)
	print
	time.sleep(1.5)
	asu="Wlist.txt"
	f=open(asu,'r')
	kontent=f.read()
	x=kontent.split("\n")
	for i in x:
	      #cek(url+"/"+i)
	      url=target+"/"+i
	      ree=requests.get("http://"+str(url)).status_code
	      if ree == 200:
	              print G+"[+] Found | url : "+url+" | code :",ree
	              #raw_input("Press Any Key To Countinue.")
	      else:
	              print R+"[-] Not Found | url : http://"+url

try:
   go()
except KeyboardInterrupt:
   print ("      "+W+"("+R+" Ctrl + C "+W+")"+R+" Detected"+W+"")
   exit()
except EOFError:
   print ("\n      "+W+"("+R+" Ctrl + D "+W+")"+R+" Detected"+W+"")
except requests.exceptions.ConnectionError:
  print ("\n      "+W+"("+R+" No "+W+")"+R+" Conection"+W+"")
except requests.exceptions.InvalidURL:
  print ("\n      "+W+"("+R+" No "+W+")"+R+" Url"+W+"")
