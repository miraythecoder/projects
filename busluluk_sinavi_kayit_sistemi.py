#Bursluluk sınavına girmek isteyenlerin kişisel bilgilerini girerek kayıt olabileceği ve 
#kullanıcı adı-şifre ve sınav bilgilerini öğrenebileceği bir modül.

#Her kullanıcıya özel kullanıcı adı ve şifre atanıyor.
#*Şifreler daima birbirinden bağımsız (=> birebir fonksiyon)
#*Sınav bilgileri (=> örten fonksiyon)

isim= str(input('İsminiz: '))
soyisim= str(input ('Soyisminiz: '))
kimlikNo= int(input('Kimlik numaranız: '))
sınıf= int(input('Şu anki sınıf seviyeniz: '))

def kullanıcıAdıOlustur(isim,sınıf):                                 #küçültsün
    kullanıcıAdı = (isim.lower()).replace(' ','')+str(kimlikNo%10)   #boşlukları kaldırsın
    return kullanıcıAdı                                             #kimlik no son rakamı eklesin
    
def sifreOlustur(kimlikNo):
    sifre= int(kimlikNo/7 )                                      #şifreyi virgüllü vermesin
    return sifre    
                                              
def kayıtOlustur(ad,soyad):
    print(f'Merhaba, ',ad , soyad, ' adına bursluluk sınavı kaydı oluşturulmuştur.')
    print('Kullanıcı adınız: ', kullanıcıAdıOlustur(isim,sınıf))
    print('Şifreniz: ',str(sifreOlustur(kimlikNo)))
    
def sınavBilgilendirme(sınıf):
            if sınıf in range(4,8):
                print("Ortaokul sınavları 24 Nisan Cumartesi günü saat 13.30'da yapılacaktır.")
            if sınıf in range (8,12):
                print("Lise sınavları 25 Nisan Pazar günü saat 14.30'da yapılacaktır.")         
while True:
    if len(str(kimlikNo))!=11:
        print("Geçersiz kimlik numarası girdiniz.")
        break

    if sınıf in range (4,12):                                  #4 dahil ama 12 dahil değil
        kayıtOlustur(isim,soyisim)
        sınavBilgilendirme(sınıf)
        break
    else:
        print('Sınıf seviyenizi kontrol edin lütfen. Bu sınav yalnızca ortaokul ve lise seviyesindeki öğrenciler içindir.')
        break
    
