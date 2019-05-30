import json
import pandas as pd
import ast
from pandas.io.json import json_normalize
import sys

reload(sys)
sys.setdefaultencoding('utf8')

def flatten_json(y):
    out = {}
    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '_')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x
    flatten(y)
    return out

data = []
for line in open('C:\Users\Edna i Anesa\Desktop\ABH internship\yelp_business.json', 'r'):
    data.append(json.loads(line))



flat_data = []
for json_line in data:
    flat_json = flatten_json(json_line)
    flat_data.append(flat_json)


#csv
tabela = pd.DataFrame.from_dict(flat_data)
tabela.dropna(axis='columns', how='all', inplace=True)
print tabela
tabela.to_csv('C:\Users\Edna i Anesa\Desktop\yelp_business.csv', sep ='|', na_rep='None', index=False)
