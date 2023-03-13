from math import sqrt

class main:
    exit = False
    def __init__(self):
        while (self.exit == False):
            self.arayuz()
            self.islemler()
    def arayuz(self):
             print("***************HESAP MAKİNESİ***************")
             print("Hangi işlemi yapmak istersiniz ?\n"
                "1 - Toplama\n"
                "2 - Çıkarma\n"
                "3 - Çarpma\n"
                "4 - Bölme\n"
                "5 - Mod Alma\n"
                "6 - Üs Alma\n"
                "7 - Karakok Alma\n"
                "8 - Faktöriyel\n"
                "9 - Yüzde Hesaplama\n"
                "10 - Vize - Final Not Ortalaması Hesaplama\n"
                "11 - Kar Oranı Hesaplama\n"
                "12 - Karışık İşlemler\n"
                "13 - Çıkış")
    def islemler(self):
        exit = False
        while (exit == False):
            islem_no = input("Yapmak istediğiniz işlem numarası : ")
            if islem_no == "1" :
                t1 = Toplama_islemi()                
            elif islem_no == "2" :
                ci1 = Cikarma_islemi()              
            elif islem_no == "3" :
                ca1 = Carpma_islemi()                
            elif islem_no == "4" :
                b1 = Bolme_islemi()                
            elif islem_no == "5":
                m1 = Mod_alma_islemi()               
            elif islem_no == "6":
                u1 = Us_alma_islemi()               
            elif islem_no == "7":
                k1 = Karakok_alma_islemi()                
            elif islem_no == "8":
                self.f1 = Faktoriyel_islemi()   
            elif islem_no == "9":
                self.y1 = Yuzde_hesaplama_islemi()
            elif islem_no == "10":
                v1 = Vize_final_ortalama_hesaplama()
            elif islem_no == "11":
                k2 = Kar_orani_hesaplama()
            elif islem_no == "12":
                i1 = Karisik_islemler()
            elif islem_no == "13":
                self.exit = True
                print("Hesap makinesinden başarıyla çıkış yaptınız.")
                break
            else :
                print("Geçersiz giriş yaptınız !")
                input()
                self.__init__()
class Toplama_islemi(main):
    def __init__(self):
        numbers = []
        exit = False
        while (exit == False):
            try:
                adet = int(input("Toplamak istediğiniz sayı adedi : "))
            except ValueError:
                print("Lütfen bir sayı girin !")
            else :
                exit = True
        exit = False
        while (exit == False):   
            try:
                for i in range(adet):
                    nums = int(input(f"Sayı {i+1}:"))
                    numbers.append(nums)
            except ValueError:
                print("Lütfen sayı girin")   
            else : 
                exit = True
        self.toplama(numbers)
    
    def toplama(self, liste):
        print("Sonuç :",sum(liste))
        input("Devam etmek için lütfen 'Enter' tuşuna basınız")
        self.arayuz()
class Cikarma_islemi(main):
    def __init__(self):
        numbers = []
        exit = False
        while (exit == False):
            try:
                self.eksilen_sayi = float(input("Eksilen sayı :"))
            except ValueError:
                print("Lütfen bir sayı girin !")
            else :
                exit = True
        exit = False
        while (exit == False):   
            try:
                self.cikan_sayi = float(input("Çıkan sayı :"))
            except ValueError:
                print("Lütfen sayı girin")   
            else : 
                exit = True
        self.cikarma()
    def cikarma(self):
        print("Sonuç :",self.eksilen_sayi - self.cikan_sayi)
        input("Devam etmek için lütfen 'Enter' tuşuna basınız")
        self.arayuz()
class Carpma_islemi(main):
    def __init__(self):
        numbers = []
        exit = False
        while (exit == False):
            try:
                adet = int(input("Çarpmak istediğiniz sayı adedi : "))
            except ValueError:
                print("Lütfen bir sayı girin !")
            else :
                exit = True
        exit = False
        while (exit == False):   
            try:
                for i in range(adet):
                    nums = int(input(f"Sayı {i+1}:"))
                    numbers.append(nums)
            except ValueError:
                print("Lütfen sayı girin")   
            else : 
                exit = True
        self.carpma(numbers)
    def carpma(self, liste):
        sonuc = 1
        for i in liste:
            sonuc = i * sonuc
        print("Sonuç : ",sonuc)
        input("Devam etmek için lütfen 'Enter' tuşuna basınız")  
        self.arayuz()     
class Bolme_islemi(main):
    def __init__(self):
        exit = False
        while (exit == False):
            try:
                self.bolunen_sayi = float(input("Bölünen sayı :"))
            except ValueError:
                print("Lütfen bir sayı girin !")
            else :
                exit = True
        exit = False
        while (exit == False):   
            try:
                self.bolen_sayi = float(input("Bölen sayı :"))
            except ValueError:
                print("Lütfen sayı girin")   
            else : 
                exit = True
        self.bolme()
    def bolme(self):
        print("Bölüm :",self.bolunen_sayi / self.bolen_sayi)
        input("Devam etmek için lütfen 'Enter' tuşuna basınız")
        self.arayuz()
class Mod_alma_islemi(main):
    def __init__(self):
        exit = False
        while (exit == False):
            try:
                self.bolunen_sayi = float(input("Bölünen sayı :"))
            except ValueError:
                print("Lütfen bir sayı girin !")
            else :
                exit = True
        exit = False
        while (exit == False):   
            try:
                self.bolen_sayi = float(input("Bölen sayı :"))
            except ValueError:
                print("Lütfen sayı girin")   
            else : 
                exit = True
        self.mod_alma()
    def mod_alma(self):
        print("Mod :",self.bolunen_sayi % self.bolen_sayi)
        input("Devam etmek için lütfen 'Enter' tuşuna basınız")
        self.arayuz()
class Us_alma_islemi(main):
    def __init__(self):
        exit = False
        while (exit == False):
            try:
                self.taban_sayi = int(input("Taban sayı :"))
            except ValueError:
                print("Lütfen bir sayı girin !")
            else :
                exit = True
        exit = False
        while (exit == False):   
            try:
                self.kuvvet = int(input("Kuvvet :"))
            except ValueError:
                print("Lütfen sayı girin")   
            else : 
                exit = True
        self.us_alma()
    def us_alma(self):
        print("Sonuç : ",self.taban_sayi ** self.kuvvet)
        input("Devam etmek için lütfen 'Enter' tuşuna basınız")
        self.arayuz()
class Karakok_alma_islemi(main):
    def __init__(self):
        exit = False
        while (exit == False):
            try:
                self.karakok_alinan_sayi = int(input("Karakök alınacak sayı :"))
            except ValueError:
                print("Lütfen bir sayı girin !")
            else :
                exit = True
        exit = False
        
        self.Karakok_alma()
    def Karakok_alma(self):
        print("Sonuç : ",sqrt(self.karakok_alinan_sayi))
        input("Devam etmek için lütfen 'Enter' tuşuna basınız")
        self.arayuz()
class Faktoriyel_islemi(main):
    def __init__(self):
        exit = False
        while (exit == False):
            try:
                self.faktoriyel = int(input("Faktöriyeli alınacak sayı :"))
            except ValueError:
                print("Lütfen bir sayı girin !")
            else :
                exit = True
        exit = False   
        self.faktoriyel_alma()
    def faktoriyel_alma(self):
        sonuc = 1
        for i in range(1,self.faktoriyel+1):
            sonuc = i * sonuc
        print("Sonuç : ",sonuc)
        input("Devam etmek için lütfen 'Enter' tuşuna basınız")
        self.arayuz()
class Yuzde_hesaplama_islemi(main):
    def __init__(self):
        exit = False
        while (exit == False):
            print("-------- Yapmak istediğiniz işlemi seçin --------\n"
                    "1 - A sayısının %B'si kaçtır ?\n"
                    "2 - A sayısı, B sayısının % kaçıdır?\n"
                    "3 - A sayısından B sayısına değişim oranı yüzde kaçtır ?\n"
                    "4 - A sayısı, %B kadar arttırılırsa kaç olur?\n"
                    "5 - A sayısı, %B kadar azaltılırsa kaç olur?\n"
                    "6 - Geri")        
            islem_no = input("Yapmak istediğiniz işlem numarası : ")
            if islem_no == "1":
                self.deger_alma()
                self.yuzde_hesaplama1()
            elif islem_no == "2":
                self.deger_alma()
                self.yuzde_hesaplama2()
            elif islem_no == "3":
                self.deger_alma()
                self.yuzde_hesaplama3()
            elif islem_no == "4":
                self.deger_alma()
                self.yuzde_hesaplama4()
            elif islem_no == "5":
                self.deger_alma()
                self.yuzde_hesaplama5()
            elif islem_no == "6":
                self.arayuz()
                break
            else:
                print("Geçersiz bir işlem yaptınız")
                input()
    def deger_alma(self):
        exit = False
        while (exit == False):
                try:
                    self.a_sayisi = int(input("A :"))
                except ValueError:
                    print("Lütfen bir sayı girin !")
                else :
                    exit = True
        exit = False
        while (exit == False):   
                try:
                    self.b_sayisi = int(input("B :"))
                except ValueError:
                    print("Lütfen sayı girin")   
                else : 
                    exit = True
    def yuzde_hesaplama1(self):
        sonuc = self.a_sayisi * self.b_sayisi/100
        print("Sonuç : ",sonuc)
        input("Devam etmek için lütfen 'Enter' tuşuna basınız")
    def yuzde_hesaplama2(self):
        sonuc = (self.a_sayisi / self.b_sayisi) * 100
        print("Sonuç : ",sonuc)
        input("Devam etmek için lütfen 'Enter' tuşuna basınız")
    def yuzde_hesaplama3(self):
        sonuc = ((self.b_sayisi - self.a_sayisi) / self.a_sayisi) * 100
        print("Sonuç : ",sonuc)
        input("Devam etmek için lütfen 'Enter' tuşuna basınız")
    def yuzde_hesaplama4(self):
        sonuc = ((self.a_sayisi / 100) * self.b_sayisi) + self.a_sayisi
        print("Sonuç : ",sonuc)
        input("Devam etmek için lütfen 'Enter' tuşuna basınız")
    def yuzde_hesaplama5(self):
        sonuc =  self.a_sayisi - ((self.a_sayisi / 100) * self.b_sayisi)
        print("Sonuç : ",sonuc)
        input("Devam etmek için lütfen 'Enter' tuşuna basınız")
class Vize_final_ortalama_hesaplama(main):
   def __init__(self):
        exit = False
        while (exit == False):   
            try:
                self.vize = int(input("Vize :"))
            except ValueError:
                print("Lütfen sayı girin")   
            else : 
                exit = True
        exit = False
        while (exit == False):   
            try:
                self.final = int(input("Final :"))
            except ValueError:
                print("Lütfen sayı girin")   
            else : 
                exit = True
        self.vize_final()
   def vize_final(self):
        print("Sonuç :",(self.vize * 40/100) + (self.final * 60/100))
        input("Devam etmek için lütfen 'Enter' tuşuna basınız") 
        self.arayuz()
class Kar_orani_hesaplama(main):
    def __init__(self):
        exit = False
        while (exit == False):
            print("-------- Yapmak istediğiniz işlemi seçin --------\n"
                    "1 - Alış fiyatı hesaplama\n"
                    "2 - Satış fiyatı hesaplama\n"
                    "3 - Kar oranı hesaplama\n"
                    "4 - Geri")
            islem_no = input("Yapmak istediğiniz işlem numarası : ")
            if islem_no == "1":
                self.alis_deger_alma()
                self.alis_hesaplama()
            elif islem_no == "2":
                self.satis_deger_alma()
                self.satis_hesaplama()
            elif islem_no == "3":
                self.kar_deger_alma()
                self.kar_orani_hesaplama()
            elif islem_no == "4":
                self.arayuz()
                break
            else:
                print("Geçersiz bir işlem yaptınız")
                input()
    def alis_deger_alma(self):
        exit = False
        while (exit == False):
                try:
                    self.satis_fiyati = int(input("Satış Fiyatı :"))
                except ValueError:
                    print("Lütfen bir sayı girin !")
                else :
                    exit = True
        exit = False
        while (exit == False):   
                try:
                    self.kar_orani = int(input("Kar oranı :"))
                except ValueError:
                    print("Lütfen sayı girin")   
                else : 
                    exit = True
    def satis_deger_alma(self):
        exit = False
        while (exit == False):
                try:
                    self.alis_fiyati = int(input("Alış Fiyatı :"))
                except ValueError:
                    print("Lütfen bir sayı girin !")
                else :
                    exit = True
        exit = False
        while (exit == False):   
                try:
                    self.kar_orani = int(input("Kar oranı :"))
                except ValueError:
                    print("Lütfen sayı girin")   
                else : 
                    exit = True
    def kar_deger_alma(self):
        exit = False
        while (exit == False):
                try:
                    self.alis_fiyati = int(input("Alış Fiyatı :"))
                except ValueError:
                    print("Lütfen bir sayı girin !")
                else :
                    exit = True
        exit = False
        while (exit == False):   
                try:
                    self.satis_fiyati = int(input("Satış Fiyatı:"))
                except ValueError:
                    print("Lütfen sayı girin")   
                else : 
                    exit = True
    def alis_hesaplama(self):
        sonuc = (self.satis_fiyati * 100) / (self.kar_orani + 100)
        print("Sonuç : ",sonuc)
        input("Devam etmek için lütfen 'Enter' tuşuna basınız")
    def satis_hesaplama(self):
        sonuc = self.alis_fiyati * (100 + self.kar_orani) / 100
        print("Sonuç : ",sonuc)
        input("Devam etmek için lütfen 'Enter' tuşuna basınız")
    def kar_orani_hesaplama(self):
        sonuc =  (self.satis_fiyati - self.alis_fiyati) * (100 / self.alis_fiyati)
        print("Sonuç : %",sonuc)
        input("Devam etmek için lütfen 'Enter' tuşuna basınız")
class Karisik_islemler(main):
    def __init__(self):
        exit = False
        while (exit == False):
            print("-------- Yapmak istediğiniz işlemi seçin --------\n"
                    "1 - Karışık işlem yap\n"
                    "2 - Geri")
            islem_no = input("Yapmak istediğiniz işlem numarası : ")
            if islem_no == "1":
                self.karisik_islem()
            elif islem_no == "2":
                self.arayuz()
                break
            else:
                print("Geçersiz bir işlem yaptınız")
                input()
    def karisik_islem(self):
        y = 0
        exit = False
        while(exit == False):
            try:
                print("\nÖrnek İşlem : (3 * 7) + (15 / 3) - 12\n")
                islem = input("İşlem giriniz :")
                sonuc = eval(islem)
            except:
                print("Lütfen geçerli bir söz dizimi kullanın.")
                input("Devam etmek için lütfen 'Enter' tuşuna basınız")
            else:
                print("Sonuç :",sonuc)
                input("Devam etmek için lütfen 'Enter' tuşuna basınız")
                break
                
m1 = main()
