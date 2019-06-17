import matplotlib.pyplot as plt
import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'furqon',
    passwd = '0987654321',
    database = 'world'
)
asean = "select country.name as Negara_ASEAN, country.Population as Populasi_Negara, country.GNP, city.Name as Ibukota, city.population from city, countrylanguage, country  where countrylanguage.CountryCode = country.Code and city.id = country.Capital and country.region = 'Southeast Asia' group by country.name order by country.name;"

df = pd.read_sql(asean, con=mydb)
negara = df['Negara_ASEAN'].values
populasi = df['Populasi_Negara'].values

warna = ['blue', 'orange', 'green', 'red', 'purple', 'brown', 'gray', 'yellow', 'pink', 'black', 'darkblue']

plt.bar(negara,populasi, color=warna, yerr=.2)  

plt.title('Populasi Negara ASEAN')
plt.xlabel('Negara')
plt.ylabel('Populasi(x 100jt jiwa)')

plt.xticks(rotation = 60)               # atur rotasi dari value x dan y
# plt.yticks(rotation = 60)
for x in range(len(negara)):
    plt.text(negara[x], populasi[x] + 1000000, populasi[x])

plt.show()