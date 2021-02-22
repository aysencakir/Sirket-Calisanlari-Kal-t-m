class temelBilgiler():
    adi=' '
    soyadi=' '
    kimlikNo=0

class muhasebeBilgileri():
    maas=0
    sgkNo=0

class departmanBilgileri():
    departman=' '
    mudurAdi=' '

class calisan(temelBilgiler,muhasebeBilgileri,departmanBilgileri):

    def _init_(self):
        printf()

   
       

obje=calisan()

obje.adi="Aysen"
obje.soyadi="Cakir"
obje.kimlikNo=12345
obje.maas=18000
obje.sgkNo=123
obje.departman="IT"
obje.mudurAdi="Mete"

print("Adi= ",obje.adi)
print("Soyadi= ",obje.soyadi)
print("Kimlik No= ",obje.kimlikNo)
print("Maas= ",obje.maas)
print("SGK No= ",obje.sgkNo)
print("Departman= ",obje.departman)
print("MudurAdi= ",obje.mudurAdi)




