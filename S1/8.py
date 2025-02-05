import pandas as pd
dict = {'Name' : ['Sumit Tyagi', 'Sukritin','Akriti Goel', 'Sanskriti','Abhishek Jain'],'Age':[22, 20, 45, 21, 22],'Marks':[90, 84, 33, 87, 82]}
df = pd.DataFrame(dict)
df_first_3 = df.head(3)
print(df_first_3)
