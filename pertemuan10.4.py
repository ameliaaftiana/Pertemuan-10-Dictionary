
keluarga = {
    "alamat": {"Jalan Suka Suka"},
    "kepala_keluarga": {"Kim Mingyu"},
    "jumlah_anggota" : {"3"},
    "nomor": {"313333333333333333"},
    "anggota":[
        {"Nama":"Mingyu","Agama":"Kristen","Tahun":"1997","Status":"Kepala Keluarga", "Menikah":"Mingyu", "Warga":"WNA"},
        {"Nama":"Yosefa","Agama":"Kristen","Tahun":"2000", "Status":"Ibu Rumah Tangga", "Menikah":"Yosefa","Warga":"WNA"},
        {"Nama":"Louis","Agama":"Kristen","Tahun":"2012", "Status":"Anak", "Menikah":None,"Anak":"Louis","Warga":"WNA"}, 
    ],
}

print (keluarga['kepala_keluarga'])
print (str(keluarga['alamat']))
print ("Jumlah anggota keluarganya adalah: ", len(keluarga["anggota"]))
print (keluarga['nomor'])

for i in keluarga["anggota"]:
    print (f'Anggota keluarganya adalah {i["Nama"]} dan beragama {i["Agama"]}')
print ("Anggota keluarga yang sudah menikah:")
    # print (f'Anggota keluarga yang sudah menikah {i["Menikah"]}')
    # # print (f'Anaknya adalah {i["Anakk"]}')
    # print (f'Anggota keluarga yang WNA adalah {i["WNA"]}')
for i in keluarga["anggota"]:
    print (f'Anggota keluarga yang sudah menikah {i["Menikah"]}')