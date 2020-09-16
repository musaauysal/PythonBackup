import os, shutil

def backup():
    kaynak = "/Users/CRYPTON/Desktop/a/"
    hedef = "/Users/CRYPTON/Desktop/a_copy/"
    files = os.listdir(kaynak)
    files.sort()
    dosya_sayisi = 0
    for f in files:
        print(f)
        dosya_sayisi += 1
        k = kaynak + f
        h = hedef + f
        shutil.copy(k, h)

    print("%d adet dosya kopyalandı" % dosya_sayisi)


def re_backup():
    kaynak = "/Users/CRYPTON/Desktop/a_copy/"
    hedef = "/Users/CRYPTON/Desktop/a/"
    files = os.listdir(kaynak)
    files.sort()
    dosya_sayisi = 0
    for f in files:
        print(f)
        dosya_sayisi += 1
        k = kaynak + f
        h = hedef + f
        shutil.copy(k, h)

    print("%d adet dosya kopyalandı" % dosya_sayisi)



print("---------Merhabalar Backup işlemine hosgeldiniz--------")
print("yedekleme yapmak istiyorsanız 1'i")
print("yedekten geri almak istiyorsanız 2'i")
print("Seçiniz...")
islem = int(input("İsleme numarası seciniz: "))
while islem!=1 or islem!=2:
    islem = int(input('lütfen yeni değer giriniz:'))
    if (islem == 1 or islem == 2):
        break
if islem == 1:
    backup()
elif islem == 2:
    re_backup()
else:
    print("lütfen 1 veya 2 girin...")
