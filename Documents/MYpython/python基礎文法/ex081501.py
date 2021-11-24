import pathlib
import pandas as pd

my_path =pathlib.path(r'\sample')

df=pd.dataframe()
for p in my_path.glob('*.csv'):
    de_current=pd.read_csv(p)
    df=de.append(df_current, ignore_index=true)

df.to_excel(r'sample\data.xlsx') 