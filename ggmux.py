import time
import sys

d='\033[1;31m'

def jam(s):
  for c in s + '\n':
   sys.stdout.write(c)
   sys.stdout.flush()
   time.sleep(1./10)

jam( '\033[1;37m ORANG BAIK BERAWAL DARI ORANG JAHAT YANG DI SEPELEKAN')
jam( '\033[1;37m sfx: Lay Lay Lay Panggil Aku Si Jablay:v')
jam('Text Berjalan Ye Gaes')
jam('Jangan Lupa SubsBrekk:v')
