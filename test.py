import pandas as pd

zck=pd.read_excel('zck.xlsx')
print(zck.head())
print(zck.购买时间.count())