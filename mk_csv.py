import pandas as pd
import csv

with open('xsb.csv','w')as csv_file:
  fieldnames = ['note', 'statue']
  writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
  writer.writeheader()
  writer.writerow({'note':' '})
  writer.writerow({'statue':' '})

df = pd.read_csv('xsb.csv')
df.drop(df.index[0:len(df)],inplace=True)

df.to_csv('xsb.csv')
