# author : Dimas Wahyu Saputro
# NIM : 120450081
# Affiliation : Sains Data ITERA
# Date : 04 March 2022
# Program Description : Program to solve simple encryption password problem

# belum final

def check_password(password):
    if len(password) > 100:
        return "Password terlalu panjang, masukkan password yang lebih pendek"
    else:
        return password

def convert_string_to_list(password):
    password_list = list(password)
    return password_list

def encrypt(password_list):
    temp_password = []
    for i in range(len(password_list)):
        temp_password.append(chr(((ord(password_list[i]))//26) + 80))
        temp_password.append(chr(((ord(password_list[i]))%26) + 80))
        if temp_password[i] >= temp_password[i+1]:
            temp_password.append('-')
        else:
            temp_password.append('+')
    password_final = ''.join(temp_password)
    return password_final    