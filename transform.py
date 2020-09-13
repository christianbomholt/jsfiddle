import pandas as pd
import json
data = pd.read_csv("data.csv")

df = data.T
df.columns = list(data.T.loc['Unnamed: 0'])
df = df.drop('Unnamed: 0',axis=0)
dc = df.cumsum().to_dict('index')
rres= []
for key,value in dc.items():
    res = []
    for k,v in value.items():
        d = {"key":k,"value":v}
        res.append(d)
    rres.append(res)
with open('here.json', 'w') as outfile:
    json.dump(rres, outfile)