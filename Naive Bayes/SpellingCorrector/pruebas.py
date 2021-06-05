import re
import pandas as pd
#numero = "111,245,954"
#numero = int(re.sub(",","",numero))
#print(numero-1)
#numero ="737799456456498797987979.	él"
#numero = re.sub("[0-9]+.\s","",numero)
#print(numero)
#words = open('CREA_total.txt', encoding='utf-8',errors='ignore').read()


df = pd.read_csv('prueba.TXT', sep='\t', encoding='latin-1',low_memory=False)
df.columns = ['palabra','frecuenciaAbsoluta','frecuenciaNormalizada']
df = df.drop(['frecuenciaNormalizada'], axis=1)
df['palabra'] = df['palabra'].str.replace(' ','')
#df = df.set_index('palabra')
df['frecuenciaAbsoluta'] = df['frecuenciaAbsoluta'].str.replace(',','')
df['frecuenciaAbsoluta'] = pd.to_numeric(df['frecuenciaAbsoluta'])
d1 = dict(zip(df['palabra'],df['frecuenciaAbsoluta']))
