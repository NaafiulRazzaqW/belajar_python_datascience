import pandas as pd
fileLocation= "F:/BelajarJSON/PythonLearn/news_data.csv"
dataFile = pd.read_csv(fileLocation, encoding="ISO=8859-1")

print("Menampilkan data 5 baris pertama: ")
print(dataFile.head())
print()

# menampilkan data 5 barus terakhir
print("menampilkan data 5 baris terakhir:")
print(dataFile.tail())
print()

# menampilkan data yang unique 
print("Menampilkan data yang unique:")
print(dataFile["title"].unique())
print(len(dataFile["title"].unique()))
print(len(dataFile["title"]))
print()

# merubah sebuah nama kolom
newColumns = {
    'tag' : 'hint'
}

dataFile.rename(columns=newColumns, inplace=True)
print(dataFile.head())

# merubah letak kolom

newOrder = [1,0,2,3,4]

dataFile = dataFile[dataFile.columns[newOrder]].head()
print(dataFile.head())