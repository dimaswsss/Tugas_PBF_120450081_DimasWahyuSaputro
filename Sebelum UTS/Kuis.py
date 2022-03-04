# author : Dimas Wahyu Saputro
# NIM : 120450081
# Affiliation : Sains Data ITERA
# Date : 04 March 2022
# Program Description : Program to solve simple encryption password problem

'''
Entah kenapa saat saya import spetools_120450081.py, mengalami error pak. 
Saya sudah berusaha, namun masih kesusahan. Agak kaget karena kuisnya begini.
Apabila waktunya lebih, saya yakin bisa mengerjakan kuis ini.
Sangat seru, terima kasih Pak! :)
'''


# simple password encryption
password = input("Masukkan password (maksimal 100 karakter): ")
if len(password) > 100:
    print("Password terlalu panjang, masukkan password yang lebih pendek")
    password = input("Masukkan password (maksimal 100 karakter): ")
else:
    pass

# convert string to list
password_list = list(password)
print(password_list)

temp_password = []
for i in range(len(password_list)):
    temp_password.append(chr(((ord(password_list[i]))//26) + 80))
    temp_password.append(chr(((ord(password_list[i]))%26) + 80))
    if temp_password[i] >= temp_password[i+1]:
        temp_password.append('-')
    else:
        temp_password.append('+')

# convert list to string
password_final = ''.join(temp_password)
print(password_final)