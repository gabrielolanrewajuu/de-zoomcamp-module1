import sys  
print("arguments", sys.argv)

month= int(sys.argv[1])
print(f"Running pipeline for month {month}")

import pandas as pd
df= pd.DataFrame({'day':[1,2], 'num_passenger':[14,7]})
df['month']= month
print(df.head())

df.to_parquet(f'output_{month}.parquet')
