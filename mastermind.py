"""bilgisayar 11 99 arası bir sayı seçer kullanıcı tahminleriyle bu sayıya yaklaşmaya çalışır
eğer kullanıcı tahmin edilen sayının 1 karakterini bilip yerini bilemezse -1 çıktısını alır
eğer sayının yerini ve değerini bilirse 1 alır
bi şey bilemezse 0 alır
eğer sayının kendisini bilirse oyun biter 
eğer sayının rakamlarını bilip yerlerini bilemezse -2 alır
bilgisayar rakamları aynı olan bir sayı seçemez
bilgisayar 10 un katları olan bir sayıyı seçemez"""


import random


s=random.randint(11,99)
s_str=str(s)



b=0
while b==0:
    e=0
    while e==0:
        a=int(input("iki basamaklı bir sayı giriniz: "))
        a_str=str(a)
        if s%11==0 or s%10==0:
            b+=1
        if len(a_str)!=2:
            print("lütfen 2 basamaklı bir sayı giriniz")
        if a%10==0 or a%11==0 or a<=10:
            print("lütfen başka bir sayı giriniz ")
        else:
            e+=1
            
    if s_str==a_str:
        print("2","tebrikler bildiniz")
        b+=1
    elif a_str[::-1]==s_str:
            print("-2")
    else:

        if a_str[0] in s_str:
            if a_str[0]==s_str[0]:
                print("1")
            else:
                print("-1")
        if a_str[1] in s_str:
            if a_str[1]==s_str[1]:
                print("1")
            else:
                print("-1")  
        if (a_str[0] in s_str)==False and (a_str[1] in s_str)==False:
            print("0")

        