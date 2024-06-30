import time

def hesaplama(tarih="yıl", payda=100): 
    anaPara = float(input("Faize koyacağınız Ana Paranızı giriniz :"))
    faizOrani = float(input("Faiz Oranını Giriniz :%"))
    tarihSayisi = float(input("Anaparanın faizde kalacağı {} sayısını giriniz :".format(tarih)))

    getiri = round(((anaPara * faizOrani * tarihSayisi) / payda), 2)
    sonuc = round((anaPara + getiri), 2)

    print("{} TL, %{} faizle {} {} sonunda \n{} TL faiz getirirken toplamda {} TL paran olur.".format(anaPara, faizOrani, tarihSayisi, tarih, getiri, sonuc))

def giris(sayi):
    try:
        baslik = "Faiz Hesaplama Programı"
        print("\n" * len(baslik), baslik.upper(), "\n" * len(baslik), sep="\n", end="\n\n")

        tercihYazisi = {
            "0": "Aşağıdakilerden birini tercih ediniz (Sıra numarasını giriniz) :",
            "1": "\n1) Yıllık basit faiz hesaplama",
            "2": "\n2) Aylık basit faiz hesaplama",
            "3": "\n3) Günlük basit faiz hesaplama"
        }

        tercih = input("{}{}{}{}\nTercihiniz :".format(*tercihYazisi.values()))

        if tercih == "1":
            hesaplama("yıl", 100)
        elif tercih == "2":
            hesaplama("ay", 1200)
        elif tercih == "3":
            hesaplama("gün", 36500)
        else:
            print("Anlamsız bir tercih numarası girdiniz.")
    except Exception as e:
        print("Anlaşılamayan bir hata oluştu :(\n", e)

if __name__ == "__main__":
    sayi = int(input("Lütfen bir sayı giriniz: "))
    giris(sayi)
    say = 20
    while say:
        print("\rProgram Kapatılıyor. Son {} sn...".format(say), end="")
        time.sleep(1)
        say -= 1
    print("\nProgram kapatıldı.")
