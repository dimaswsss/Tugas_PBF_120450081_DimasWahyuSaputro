# author : Dimas Wahyu Saputro
# NIM : 120450081
# Affiliation : Sains Data ITERA
# Date : 07 March 2022
# Program Description : Program to solve simple encryption password problem

import spetools_120450081 as tools

password = input("Masukkan password (maksimal 100 karakter): ")
print('hasil encrypt: ', tools.enkrip(password))