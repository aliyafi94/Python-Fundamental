dataKaryawan = [
    {
        'Npk': 'Ac001',
        'Nama': 'Rahmi Z',
        'Jabatan': 'Manajer',
        'Departemen': 'Pelayanan',
    },
    {
        'Npk': 'Ac002',
        'Nama': 'Dinda Aulia',
        'Jabatan': 'Administrasi',
        'Departemen': 'Pelayanan',
    },
    {
        'Npk': 'Ac003',
        'Nama': 'Alif Taufik',
        'Jabatan': 'Supervisor',
        'Departemen': 'Pelayanan',
    }
]

# Melihat Data Karyawan
def report():
    while True:
        print('''
-------------------------------       
    Report Data Karyawan :
-------------------------------
    1. Report Seluruh Data
    2. Report Data Tertentu
    3. Kembali ke Menu Utama
            ''')

        inputReport = int(input('Silahkan Pilih Sub Menu Report Data Karyawan (1-3): '))

        if inputReport == 1:
            print('Data Karyawan\n')
            print('Npk\t Nama        \t Jabatan\t Departemen')
            for i,j in enumerate(dataKaryawan) :
                print('{}\t {}  \t {}\t {}'.format(j['Npk'],j['Nama'],j['Jabatan'],j['Departemen']))

        elif inputReport == 2:
            report2 = (input('Masukkan Npk: ')).capitalize()
            print(f'Data Karyawan dengan Npk: {report2}')

            for i,j in enumerate(dataKaryawan) :
                if report2 == j['Npk'] :
                    print('NPK\t Nama        \t Jabatan\t Departemen')
                    print('{}\t {}  \t {}\t {}'.format(j['Npk'],j['Nama'],j['Jabatan'],j['Departemen']))
                    break

                elif report2 != j['Npk'] and (i == len(dataKaryawan)-1):
                    print('Data Tidak Ada')
                    break        

        elif inputReport == 3:
            break
        
        else:
            print('Pilihan yang anda Masukkan Salah')

# Menambah Data Karyawan
def tambah():
    while True:
        print('''
-------------------------------
    Menambahkan Data Karyawan :
-------------------------------
    1. Tambah Data Karyawan
    2. Kembali ke Menu Utama
                '''
                )
        inputTambah = int(input('Silahkan Pilih Sub Menu Tambah Data Karyawan (1-2): '))

        if inputTambah == 1 :
            inputTambah2 = (input('Masukkan Npk: ')).capitalize()
            for i,j in enumerate(dataKaryawan) :
                if inputTambah2 == j['Npk'] :
                    print('Data Sudah Ada')
                    break

                elif inputTambah2 != j['Npk'] and (i == len(dataKaryawan)-1):
                    namaKaryawan = str(input('Masukkan Nama Karyawan: '))
                    jabatanKaryawan = input('Masukkan Jabatan Karyawan: ').capitalize()
                    departemenKaryawan = input('Masukkan Departemen Karyawan: ').capitalize()
                    simpanData = input('Apakah Data Akan Disimpan? (Y/N): ').upper()
                
                    if simpanData == 'Y' :
                        print('Data Tersimpan')
                        dataKaryawan.append({
                            'Npk' : inputTambah2,
                            'Nama': namaKaryawan,
                            'Jabatan': jabatanKaryawan,
                            'Departemen': departemenKaryawan,
                            })
                    elif simpanData == 'N' :
                        print('Data Tidak Tersimpan karena memilih N')
                    else:
                        print('Data Tidak Tersimpan, Hanya ada Pilihan Y atau N')
                    break
        
        elif inputTambah == 2:
            break
        
        else:
            print('Pilihan yang anda Masukkan Salah')

# Mengubah Data Karyawan
def ubah():
    while True:
        print('''
-------------------------------
    Mengubah Data Karyawan :
-------------------------------
    1. Ubah Data Karyawan
    2. Kembali ke Menu Utama
                '''
                )
        inputUbah = int(input('Silahkan Pilih Sub Menu Ubah Data Karyawan (1-2): '))

        if inputUbah == 1:
            inputUbah2 = (input('Masukkan Npk: ')).capitalize()

            for i,j in enumerate(dataKaryawan) :
                if inputUbah2 == j['Npk'] :
                    print('Npk\t Nama        \t Jabatan\t Departemen')
                    print('{}\t {}  \t {}\t {}'.format(j['Npk'],j['Nama'],j['Jabatan'],j['Departemen']))
                    
                    inputUbah3 = input('Tekan Y jika ingin lanjut ubah data atau N jika ingin cancel ubah (Y/N): ').capitalize()
                    if inputUbah3 == 'Y':
                        kolomUbah = input('Masukkan Kolom/Keterangan yang ingin diedit: ').capitalize()
                        for key in j.keys():
                            if kolomUbah == key :
                                inputUbah4 = input(f'Masukkan {kolomUbah} Baru: ').capitalize()
                                inputUbah5 = input('Apakah Data akan diupdate? (Y/N): ').upper()
                                if inputUbah5 == 'Y':
                                    j[kolomUbah] = inputUbah4
                                    print('Data Updated')
                                elif inputUbah5 == 'N':
                                    print('Data tidak diupdate karena memilih N')
                                else:
                                    print('Data tidak diupdate karena memilih Pilihan hanya Y dan N')
                                break

                    else:
                        break
                    break

                elif inputUbah2 != j['Npk'] and (i == len(dataKaryawan)-1):
                    print('Data Tidak Ada')
                    break

        elif inputUbah == 2:
            break

        else:
            print('Pilihan yang anda Masukkan Salah')

# Menghapus Data Karyawan
def hapus():
    while True:
        print('''
-------------------------------
    Menghapus Data Karyawan :
-------------------------------
    1. Hapus Data Karyawan
    2. Kembali ke Menu Utama
        '''
        )
        inputHapus = int(input('Silahkan Pilih Sub Menu Hapus Data Karyawan (1-2) :'))

        if inputHapus == 1:
            inputHapus2 = (input('Masukkan Npk: ')).capitalize()
        
            for i,j in enumerate(dataKaryawan) :
                if inputHapus2 == j['Npk'] :
                    print('NPK\t Nama        \t Jabatan\t Departemen')
                    print('{}\t {}  \t {}\t {}'.format(j['Npk'],j['Nama'],j['Jabatan'],j['Departemen']))

                    hapusData = input('Apakah Data akan dihapus? (Y/N): ').upper()
                    if hapusData == 'Y' :
                        del dataKaryawan[i]
                        print('Data Deleted')
                    elif hapusData == 'N' :
                        print('Data Tidak Terhapus karena memilih N')
                    else:
                        print('Data Tidak Terhapus, Hanya ada Pilihan Y atau N')
                    break

                elif inputHapus2 != j['Npk'] and (i == len(dataKaryawan)-1):
                    print('Data Tidak Ada')
                    break

        elif inputHapus == 2:
            break
            
        else:
            print('Pilihan yang anda Masukkan Salah')

while True:
    print('''
-----------------------------------------
  Data Karyawan PT. Afiat Holistic Care
-----------------------------------------
    1. Report Data Karyawan
    2. Menambah Data Karyawan
    3. Mengubah Data Karyawan
    4. Menghapus Data Karyawan
    5. Exit
    '''
    )
    menuNumber = int(input('Silahkan Pilih Menu Utama (1-5): '))

    if menuNumber == 1:
        report()
    elif menuNumber == 2:
        tambah()
    elif menuNumber == 3:
        ubah()
    elif menuNumber == 4:
        hapus()
    elif menuNumber == 5:
        break
    else :
        print('Pilihan yang Anda Masukkan Salah')
