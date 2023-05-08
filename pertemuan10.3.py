#array of dictionary
data = [
    {"V": "S001"},
    {"V": "S002"},
    {"VI": "S001"},
    {"VI": "S005"},
    {"VII": "S005"},
    {"v": "S009"},
    {"VII": "S007"},
]

hasil = [] #membuat list
for d in data: #looping isi list
    for value in d.values(): #ambil value
        if hasil.count(value) == 0: #jika belum ada di list, maka append
            hasil.append(value) #menambahkan value ke dalam list
print (hasil)
    