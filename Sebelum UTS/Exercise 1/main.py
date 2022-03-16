import tools

pilihan = input('Pilih menu: 1. Enkripsi, 2. Dekripsi, 3. Keluar: ')
if pilihan == '1':
    password = input('Masukkan password (maksimal 100 karakter): ')
    password_final = tools.enc(password)
    print('hasil encrypt: ', password_final)
elif pilihan == '2':
    password = input('Masukkan password yang ingin didekripsi: ')
    password_final = tools.dec(password)
    print('hasil decrypt: ', password_final)
else:
    print('Terima kasih')