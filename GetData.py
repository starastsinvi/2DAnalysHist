import os, sys
import ROOT
import pandas as pd

# Загрузка данных из txt файлов
de2 = pd.read_csv('DATA_TXT/RUN010_dE2.txt', sep='\s+', header=None)
e5 = pd.read_csv('DATA_TXT/RUN010_E5.txt', sep='\s+', header=None)

# Создание гистограммы
h = ROOT.TH1F('h', 'h', 100, 0, 100)

# Заполнение гистограммы данными
for i in range(len(de2)):
    h.Fill(de2.iloc[i][0], e5.iloc[i][0])

# Отрисовка гистограммы
c = ROOT.TCanvas('c', 'c')
h.Draw()