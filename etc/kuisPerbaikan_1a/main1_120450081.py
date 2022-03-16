# author : Dimas Wahyu Saputro
# NIM : 120450081
# Affiliation : Sains Data ITERA
# Date : 04 March 2022
# Program Description : Program to solve simple encryption password problem

import spetools_120450081

password = input("Masukkan password (maksimal 100 karakter): ")
password_final = spetools_120450081.enc(password)
print('hasil encrypt: ', password_final)