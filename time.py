import time
#Units of Time
days = int(input("How many days: "))
hours = int(input("How many hours: "))
minutes = int(input("How many minutes: "))
second = int(input("How many seconds: "))

DtoS = days * 86400
HtoS = hours * 3600
MtoS = minutes * 60

timepassed = DtoS + HtoS + MtoS + second
print("that is ", timepassed , " seconds")

#Units of Time (Again)
seconds = int(input("How many seconds: "))
D = 0
HH = 00
MM = 00
SS = 00


D = D + seconds // 86400
seconds = seconds % 86400
HH = HH + seconds // 3600
seconds = seconds % 3600
MM = MM + seconds // 60
seconds = seconds % 60
SS = SS + seconds
print(D,":",(str(HH).zfill(2)),":",(str(MM).zfill(2)),":",(str(SS).zfill(2)))

#Current time
thetime = time.asctime()
print(thetime)