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

plt.pie(populasi, labels=negara, 
    startangle=-90, 
    autopct='%1.1f%%',           # menampilkan persentase
    textprops={'color':'w'}      # text menjadi putih
) 

plt.title('Persentase Penduduk ASEAN')
plt.legend(negara, loc = 0)

plt.show()