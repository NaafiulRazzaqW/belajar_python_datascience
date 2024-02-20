import pandas as pd

file_location = "F:/BelajarJSON/PythonLearn/news_data.csv"
dataFile = pd.read_csv(file_location)
# ini untuk mengecek data yang diambil dari excel, 5 baris pertama
print("Menampilkan Data Excel Baris Pertama:")
print(dataFile.head())
print()
# customisasi data yang diambil
print("mengambil 10 data:")
print(dataFile.head(10))
print()
# check column data
print("mengecek nama kolom:")
print(dataFile.columns)
print()
# melihat spesifik column
print("mencari spesifik data kolom, disini saya mencari title:")
print(dataFile['title'])
print()
# slicing spesifik column
print("melakukan slicing terhadap kolom tertentu:")
print(dataFile.loc[:, ["title", "author"]])
print()
# filtering data berdasarkan tanggal rilis
print("mencari data berdasarkan kondisi yang ditentukan:")
print(dataFile[dataFile['publish_date'] > "2023-12-01"])
print()
# filtering data mencari data kosong
print("mencari data dengan kolom yang kosong:")
print(dataFile[dataFile["main_image"].isnull()] )
