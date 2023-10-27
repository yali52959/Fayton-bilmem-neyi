# Ben İBB Teknoloji atölyelerine gidiyorum. Orada çok başarılıyım. https://drive.google.com/file/d/1GXn0Ff7uqwY_VT6CsIxYI-uZRbqqhYi8/view?usp=sharing (kanıt) 
#bize yazdırdıkları bir kodu sana gostermek istiyorum:
#Bir şirket çalışanlarına mevcut maaaşlarının aralığına karşılık gelen değerler oranında zam yapacak. Örneğin;
#Maaş 11.500 ile 15.000 arasında ise %15
#Maaş 15.000 ile 20.000 arasında ise %20
#Maaş 20.000 ile 25.000 arasında ise %25 zam yapılacaktır.
#Not: bir çalışanın alabileceği minimum mmaş asgari ücrettir(11.500) Ve şirket bu sene 25.000'den fazla para alan çalışanlarına zam yapmayacaktır.
#Kullanıcı bu bilgilere göre yanlış değer girerse onu uyarın*
x = int(input("maaşı sallayınız: "))
if x >= 11500 and x <= 15000:
    print("%15 maaş artışı! artık yeni maaşınız: ",int(x*(115/100)))
elif x >= 15000 and x <= 20000:
    print("%20 maaş artışı! artık yeni maaşınız: ",int(x*(120/100)))
elif x >= 20000 and x <= 25000:
    print("%25 maaş artışı! artık yani maaşınız: ",x*(125/100))
elif x >= 25000:
    print("zam yok!")
else:
    print("düzgün maaş sallayınız!")