import pandas as pd

sample_data = pd.read_csv('__sample/snp_daily_trimmed.csv')

firstRow = sample_data.head(1)


type(firstRow)
