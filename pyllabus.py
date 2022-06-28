import datetime, locale, sys, os, time
from turtle import clear



#Dokunma
locale.setlocale(locale.LC_ALL, 'tr_TR')
x = datetime.datetime.now()
tarih = (x.strftime("%A"))
#Dokunma


ders_programi = {
#Kendine göre Ayarla
    'pazartesi': "Matematik, Matematik, Edebiyat, Edebiyat",
    'sali': "Biyoloji, Biyoloji, Kimya, Kimya",
    'carsamba': "Beden, Beden, Felsefe, Felsefe",
    'persembe': "Fizik, Fizik, Din, Din",
    'cuma': "Ingilizce, Ingilizce, Almanca, Almanca"
#Kendine göre Ayarla
}

if tarih == "Pazartesi":
    print("\033[31m Bugün günlerden:\033[32m",tarih)
    print("\033[34m Çalışma Programın:\033[35m", ders_programi["pazartesi"], "\033[0m")
    
elif tarih == "Salı":
    print("\033[31m Bugün günlerden:\033[32m",tarih)
    print("\033[34m Çalışma Programın:\033[35m", ders_programi["sali"], "\033[0m")

elif tarih == "Çarşamba":
    print("\033[31m Bugün günlerden:\033[32m",tarih)
    print("\033[34m Çalışma Programın:\033[35m", ders_programi["carsamba"], "\033[0m")

elif tarih == "Perşembe":
    print("\033[31m Bugün günlerden:\033[32m",tarih)
    print("\033[34m Çalışma Programın:\033[35m", ders_programi["persembe"], "\033[0m")

elif tarih == "Cuma":
    print("\033[31m Bugün günlerden:\033[32m",tarih)
    print("\033[34m Çalışma Programın:\033[35m", ders_programi["cuma"], "\033[0m")



def clear():
  if os.name == "nt":
    os.system("cls")
  else:
    os.system("clear")

if ("-t" in sys.argv):
 clear()
 print("\033[35mTüm Çalışma Programın:")
 print("\033[31m Pazartesi:\033[34m", ders_programi["pazartesi"])
 print("\033[31m Salı:\033[34m", ders_programi["sali"])
 print("\033[31m Çarşamba:\033[34m", ders_programi["carsamba"])
 print("\033[31m Perşembe:\033[34m", ders_programi["persembe"])
 print("\033[31m Cuma:\033[34m", ders_programi["cuma"], "\033[0m")