import requests
import pandas as pd

data_url ="https://data.cdc.gov/resource/g4jn-64pd.json"

data_file = requests.get(data_url)
data_file = data_file.json()



df = pd.DataFrame(data_file)

print(df)
