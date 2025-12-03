# listga harflar chiqarish
# ism = input("Ismingizni kiriting:> ")
# letters = []
# for i in ism:
#     letters.append(i)
# print(letters)    



# listdagi o'xshash narsalarni o'chirish
# lst = [1, 2, 3, 3, 4, 5, 5, 6, 7]

# new_list = []

# for i in lst:
#     if i not in new_list:
#         new_list.append(i)
# print(new_list)        

#wqazi12www4045:owo

# talaba_id = {"Ali": 101, "Vali": 102, "Hasan": 103}
# for key, value in talaba_id.items():
#     print(value, key)


# talaba = {"ism": "Ali", "yosh": 18, "kurs": 1}
# manzil = {"shahar": "Toshkent", "tuman": "Yunusobod"}
# talaba.update(manzil)
# print(talaba)

# magazin = {
#     "mahsulotlar": [
#         {"nomi": "Olma", "kategoriya": "mevalar", "narxi": 15000, "sotuvdami": True},
#         {"nomi": "Banan", "kategoriya": "mevalar", "narxi": 20000, "sotuvdami": True},
#         {"nomi": "Sabzi", "kategoriya": "sabzavotlar", "narxi": 10000, "sotuvdami": True},
#     ],
#     "xodimlar": [
#         {"ismi": "Abdulloh", "lavozim": "direktor", "maosh": 0},
#         {"ismi": "Ubaydulloh", "lavozim": "sotuvchi", "maosh": 1000000},
#     ]
# }


# print("""
#     Assalomu alaykum! Xush kelibsiz
#     Oshxona boshqaruv tizimi
#     Amallar:
#     1) Mahsulotlarni ko'rish
#     2) Mahsulot qo'shish
#     3) Mahsulot sotuvdan olib tashlash/qo'yish
#     4) Xodimlarni ko'rish
#     5) Xodimlarni o'chirish    

# """)

# while True:
#     print("Amalni tanlang:>")
#     amal = input()

#     if amal == "1":
#         for mahsulot in magazin["mahsulotlar"]:
#             if mahsulot["sotuvdami"]:
#                 sotuvdami = "Sotuvda"
#             else:
#                 sotuvdami = "Sotuvda emas"
#             print(f"{magazin["mahsulotlar"].index(mahsulot) + 1}) {mahsulot["nomi"]} - {mahsulot["narxi"]} - {sotuvdami}")
#     if amal == "2":
#         for mahsulot in magazin["mahsulotlar"]:
#             if mahsulot["sotuvdami"]:
#                 sotuvdami = "Sotuvda"
#             else:
#                 sotuvdami = "Sotuvda emas"
#             print(f"{magazin["mahsulotlar"].index(mahsulot) + 1}) {mahsulot["nomi"]} {sotuvdami}")
#     if amal == "3":
#         for mahsulot in magazin["mahsulotlar"]:
#             print(f"{magazin["mahsulotlar"].index(mahsulot) + 1})Bizda hozir: {mahsulot["nomi"]} shular bor.")
#     if amal == "4":
#         for hodimlar in magazin["xodimlar"]:
#             print(f"{magazin["xodimlar"].index(hodimlar) + 1} {hodimlar["ismi"]}")




# 1-topshiriq
# ro'yxatdagi unli harf bilan boshlanadigan so'zlarni yangi ro'yxatga joylashtiring
# natija = ['olma', 'anor', 'uzum']
# def unli_harf():
#     sozlar = ['olma', 'anor', 'banan', 'shaftoli', 'uzum', 'nok', 'gilos']
#     unli = 'aeiou'
#     yangi_royhat = []
#     for soz in sozlar:
#         if soz[0] in unli:
#             yangi_royhat.append(soz)
#     return yangi_royhat
#     print(yangi_royhat)
# unli_harf()




# 2-topshiriq
# berilgan ro'yxatdagi juft sonlarni yangi ro'yxatga joylashtiring
# natija = [2, 4, 6, 8, 10]
# sonlar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# def juft_sonlar():
#     sonlar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     juft_sonla = []
#     for son in sonlar:
#         if son % 2 == 0:
#             juft_sonla.append(son)
#     print(juft_sonla)       
# juft_sonlar()




# 3-topshiriq
# berilgan matndagi so'zlarni sonini hisoblang. Bunda bir xil so'zlar soni qo'shib hisoblanadi
# salom: 2, dunyo: 2, odamlar: 1
# matn = "salom dunyo salom odamlar dunyo"
# def soz_soni(matn):
#     sozlar = matn.split()
#     sanog = {}
#     for soz in sozlar:
#         if soz in sanog:
#             sanog[soz] += 1
#         else:
#             sanog[soz] = 1
#     for soz, son in sanog.items():
#         print(f"{soz}: {son}")
# soz_soni(matn)        