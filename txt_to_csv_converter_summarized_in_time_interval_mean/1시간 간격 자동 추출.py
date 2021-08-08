import pandas as pd

import numpy as np

import os



print(os.getcwd())
print('위에거 \를 전부 /로 바꾸고 마지막에 /(파일이름.txt)하면 됨')
f=input("파일경로와 이름입력:")
#주소를 텍스트로 복사해서 입력

df = pd.read_csv(f, delimiter = '\t',encoding='cp949')

#df = pd.read_csv(csv, encoding='cp949')
df.columns = ['time', '공조온도', '공조급기', 'x', '상부온도', '품온', '품온1', '품온2', '하부온도']
df = df.drop('x', axis=1)
#print(df.head())
print(df)
print('\n')
df['new_time'] = pd.to_datetime(df['time'], format='%Y-%m-%d %H:%M:%S', errors='raise')

df.index = pd.DatetimeIndex(df['new_time'])

#df = df.drop('time', axis=1)

#dfa = df['a'].dropna(axis=0)


#print(dfa)

#dfa_summary = dfa.resample('H').first()
df_summary = df.resample('H').mean()

print(df_summary)

df_summary.to_excel(excel_writer='/content/drive/MyDrive/평균.xlsx')
