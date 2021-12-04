from tkinter import *
import time

root = Tk()
root.config(bg="black")
root.resizable(1, 0)
root.title("Sistem Bilgi Giris")
root.geometry("450x400")
bilgi_say = 1
sorular = ["Bilgisayarınızın ram (GB) miktarı\nÖrnek: (2,4,6...)",
           "Bilgisayarınızın ram hz'si\nÖrnek: (1600,1400,1200...)",
           "Bilgisayarınızın ekran kartı GB'ı\nÖrnek: (1,2,3...)",
           "Bilgisayarınızın ekran kartı markası\nÖrnek: (amd,nvdia,intel...)",
           "Bilgisayarınızın işlemci çekirdek sayısı\nÖrnek: (1,2,3,4...)",
           "Bilgisayarınızın işlemci markası\nÖrnek: (intel,amd)",
           "Bilgisayarınızın işemci nesili\nÖrnek: (2,3,4,5...)",
           "Bilgisayarınızın depolama türü\nÖrnek: (ssd,hdd,hdd,ssd)",
           "Bilgisayarınızın ssd miktarı (GB)\nÖrnek: (yoksa:0,200,300,400...)",
           "Bilgisayarınızın hdd miktarı (GB)\nÖrnek: (yoksa:0,200,300,400...)",
           "Bilgisayarınızın veri yolu miktarı (bit)\nÖrnek: (32,64)",
           "Bilgisayarınızın işletim sistemi\nÖrnek: (windows10,linux...)"]

kontrol_yazı = ["Ram (GB) miktarı",
                "Ram hz'si",
                "Ekran kartı GB'ı",
                "Ekran kartı markası",
                "İşlemci çekirdek sayısı",
                "İşlemci markası",
                "İşemci nesili",
                "Depolama türü",
                "Ssd miktarı (GB)",
                "Hdd miktarı (GB)",
                "Veri yolu miktarı (bit)",
                "İşletim sistemi"]


def kontrol():
    print("Bu analiz 2020 programlarına göre hesaplanmaktadır.\nKontrol sistemi başlatıldı.")
    time.sleep(2)
    u = 0
    puan = ""
    puan_list = []
    orantı = [8, 1400, 3,
              ("gtx", "nvdia", "intel"),
              4, "intel", 5,
              ("ssd,hdd", "hdd,ssd", "ssd"),
              450, 1000, 64,
              ("windows10", "linux", "mac")]

    for k in bilgiler:
        print(
            """
        > {} = [ {} ] < ({})
        """.format(k, kontrol_yazı[u], "-"), end="-----------------------------------------")
        u += 1


soru_say = 0
global bilgiler
bilgiler = []


def devam():
    try:
        global soru_say
        global bilgi_say

        bilgi = inp.get()
        bilgi = str(bilgi)
        bilgiler.append(bilgi)

        bilgi_say += 1

        try:

            text1.config(text="{}".format(sorular[soru_say]))
            text2.config(text="\n{}.Bilgi İşlem;".format(bilgi_say))
            soru_say += 1
        except:
            pass

        if bilgi_say == 14:
            print("\nCLOSED")
            root.destroy()
            kontrol()


    except:
        pass


reklam = Label()
reklam.config(text="\nYapımcı: Mertcan Balcı\n", bg="black", fg="white", font=("Calibri", 15))
reklam.pack()

text1 = Label()
text1.config(bg="white",
             fg="black",
             text="Lütfen bilgisayarınızın markasını giriniz.\nÖrnek: (hp,lenova,monster...)",
             font=("Calibri", 16))
text1.pack()

text2 = Label()
text2.config(text="\n{}.Bilgi İşlem;".format(bilgi_say), bg="black", fg="white", font=("Calibri", 17))
text2.pack()

inp = Entry()
inp.config(font=("Calibri", 17))
inp.pack()

bos = Label()
bos.config(bg="black", font=("Calibri", 16))
bos.pack()

buton = "Devam"
btn = Button()
btn.config(command=devam, bg="white", fg="black", text="{}".format(buton), font=("Calibri", 16))
btn.pack()

root.mainloop()
