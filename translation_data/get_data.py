import os, json, time, codecs
import datetime
import pandas as pd 
import numpy as np 

path = "de-en_txt_data/"
de_file = "EMEA.de-en.de"
en_file = "EMEA.de-en.en"

print(datetime.datetime.now())
file = open(path+de_file,'r')

os.system("rm -rf {}".format(path+"german_data.txt"))
os.system("rm -rf {}".format(path+"english_data.txt"))

german_list = []
english_list = []

for count, line in enumerate(file.readlines()):
    german_list.append(line.rstrip("\n"))

file = open(path+en_file,'r')
for count, line in enumerate(file.readlines()):
    english_list.append(line.rstrip("\n"))

print(len(german_list), len(english_list))

data_frame = pd.DataFrame({"german": german_list,"english": english_list})
print(data_frame.head())
mask = (data_frame['german'].str.split().str.len() >= 7) & (data_frame['german'].str.split().str.len() <= 10)
filtered = data_frame.loc[mask]
mask2 = (filtered['german'].str.endswith("."))
filtered = filtered.loc[mask2]
filtered = filtered.iloc[0:40000]
filtered.reset_index(inplace=True, drop=True)

print(filtered.head(), filtered.shape)

german_list_final = filtered["german"].to_list()
english_list_final = filtered["english"].to_list()
print(len(german_list_final), len(english_list_final))

with open(path+"german_data.txt", "w") as f:
    for line in german_list_final:
        f.write(line+"\n")
    f.close()

with open(path+"english_data.txt", "w") as f:
    for line in english_list_final:
        f.write(line+"\n")
    f.close()

print(datetime.datetime.now())