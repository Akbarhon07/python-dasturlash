# listga harflar chiqarish
ism = input("Ismingizni kiriting:> ")
letters = []
for i in ism:
    letters.append(i)
print(letters)    



# listdagi o'xshash narsalarni o'chirish
lst = [1, 2, 3, 3, 4, 5, 5, 6, 7]

new_list = []

for i in lst:
    if i not in new_list:
        new_list.append(i)
print(new_list)        
