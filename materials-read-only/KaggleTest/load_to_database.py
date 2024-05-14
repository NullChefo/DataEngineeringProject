import pandas as pd
import pyodbc

data = pd.read_csv (r'./resource/world-population-data/world_population_data.csv')   
df = pd.DataFrame(data)
df.columns = ['rank','cca3','country','continent','population_2023','population_2022','population_2020','population_2015','population_2010','population_2000','population_1990','population_1980','population_1970','area','density','growth_rate','world_percentage']

# print(df.columns)

server = 'database-2.c12meu6m29tl.eu-west-1.rds.amazonaws.com'
database = 'test'
username = 'admin'
password = 'password'
connection_string = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password};TrustServerCertificate=YES'

conn = pyodbc.connect(connection_string)
cursor = conn.cursor()

# Insert DataFrame to Table
for row in df.itertuples():
    print(row)
    cursor.execute('''
                INSERT INTO world_population (rank,cca3,country,continent,population_2023,population_2022,population_2020,
                                      population_2015 ,population_2010, population_2000, population_1990,                                     
                                      population_1980,population_1970,area,density,growth_rate,world_percentage)
                VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                ''',
                row.rank, 
                row.cca3,
                row.country,
                row.continent,
                row.population_2023,
                row.population_2022,
                row.population_2020,
                row.population_2015,
                row.population_2010,
                row.population_2000,
                row.population_1990,
                row.population_1980,
                row.population_1970,
                row.area,
                row.density,
                row.growth_rate,
                row.world_percentage                
                )

conn.commit()