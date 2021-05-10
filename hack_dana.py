import random, time
d = "\033[90;1m"
m = "\033[91;1m"
h = "\033[92;1m"
k = "\033[93;1m"
b = "\033[94;1m"
j = "\033[95;1m"
a = "\033[96;1m"
p = "\033[97;1m"
print a+"""
  ___ ___                __     ________                        
 /   |   \_____    ____ |  | __ \______ \ _____    ____ _____   
/    ~    \__  \ _/ ___\|  |/ /  |    |  \\__   \  /    \\__   \\  
\    Y    // __ \\  \___|    <    |    `   \/ __ \|   |  \/ __ \\_
 \___|_  /(____  /\___  >__|_ \  /______  (____  /___|  (____  /
       \/      \/     \/     \/         \/     \/     \/     \/ """+h+"""
  Author:"""+p+""" IvanFz
  """
d_ = raw_input(p+" [$] Input No DANA"+k+": ")
jm = input(p+" [$] Input Limit"+k+": ")
print h+"\n Tunggu Prosess"+p+"..../"
time.sleep(5)
print ""
for c in range(jm):
	nominal = random.choice(["10.000", "gagal", "3000", "20.000", "100.000", "50.000", "200.000", "500.000"])
	time.sleep(2)
	if nominal == "gagal":
		print m+" [Info]"+k+" Gagal menerima...."
		continue
	print h+" ["+p+"Info"+h+"] "+p+" Berhasil Menerima Rp"+h+nominal
	
