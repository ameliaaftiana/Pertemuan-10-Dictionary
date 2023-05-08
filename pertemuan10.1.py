# #Menambahkan data ke dict
# bu = dict()

# bu = {'book':'buku','fish':'ikan','horse':'kuda'}
# print (bu)
# print (bu['book'])


#lain
khs = {
    "71220000":["Tekkom","Jarkom","Logmat"],
    "71200001":["Pak","Tekkom","Logmat"],
    #sebelah kiri (key) berisikan str atau int
    #sebelah kanan (value) bebas
    # kunci hanya bisa 1 value, sedangkan 2 kunci memiliki 1 value bisa
}

#looping
for key in khs.keys():
    print (f"NIM: {key}, Matkul: {khs[key]}")
    
#menambahkan matkul IMK ke dalam angkatan 20
khs["71200001"].append("IMK") #append menambahkan di belakang sedangkan insert menambahkan di depan
print(khs)

#supaya turun
print()

#Menghapus PAK
del khs["71200001"][0]
print (khs)