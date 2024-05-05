import pandas as pd

tsv_file1 = 'name.basics.tsv'
csv_table1 = pd.read_table(tsv_file1,sep = '\t')
csv_table1.to_csv('name.basics.csv',index = False)

tsv_file2 = 'title.akas.tsv'
csv_table2 = pd.read_table(tsv_file2,sep = '\t')
csv_table2.to_csv('title.akas.csv',index = False)

tsv_file3='title.basics.tsv'
csv_table3=pd.read_table(tsv_file3,sep = '\t')
csv_table3.to_csv('title.basics.csv',index = False)

tsv_file4='title.crew.tsv'
csv_table4=pd.read_table(tsv_file4,sep = '\t')
csv_table4.to_csv('title.crew.csv',index = False)

tsv_file5='title.episode.tsv'
csv_table5=pd.read_table(tsv_file5,sep = '\t')
csv_table5.to_csv('title.episode.csv',index = False)

tsv_file6='title.principals.tsv'
csv_table6=pd.read_table(tsv_file6,sep = '\t')
csv_table6.to_csv('title.principals.csv',index = False)

tsv_file7='name.ratings.tsv'
csv_table7=pd.read_table(tsv_file7,sep = '\t')
csv_table7.to_csv('name.ratings.csv',index = False)