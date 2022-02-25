import random
from datetime import datetime
from random import randint

#Random isim seçici
choicefile=open("isim.txt","r",encoding="utf-8")
isimlist=[]
for line in choicefile:
    isimlist.append(line)
isim=random.choice(isimlist)
isim = isim.rstrip() #isimle soyisimin arasında satır farkı olmaması için satırı siler
# print(isim)


#Random Soyisim Seçici
choicefile=open("soyisim.txt","r",encoding="utf-8")
soyisimlist=[]
for line in choicefile:
    soyisimlist.append(line)
soyisim=random.choice(soyisimlist)
# print(soyisim)

#İsim Soyisim Birleştirme

isim_soyisim = isim+' '+soyisim
print(isim_soyisim)

#Rastgele Doğum Tarihi Oluşturucu
bugun = datetime.today() #yaşın hesaplanması için bugünü veri olarak alıyoruz
yıl = random.randint(1950,2022)
ay =random.randint(1,12)
gun = random.randint(1,30)
dogumgunu = datetime(yıl, ay, gun)
fark = bugun - dogumgunu
fark = int(fark.days/360)


print(f"Dogum Tarihi: "+str(dogumgunu.day)+'-'+str(dogumgunu.month)+'-'+str(dogumgunu.year))    
print(f"Yaşı: "+str(fark))