import requests
import pandas as pd
import csv
import json
from bs4 import BeautifulSoup

from_date = '2020-07-01'
to_date = '2020-07-06'
url ='https://feeds.intoday.in/common/apis/lallantop/factcheck.php?key=cc9ca05dc88f191b44c54403a003809c&'+'from='+from_date+'&to='+to_date
res = requests.get(url)
jsonResponse = res.json()
df = pd.read_json(json.dumps(jsonResponse))
df.head()
df['story_excerpt'] = [BeautifulSoup(text).get_text() for text in df['story_excerpt'] ]
df['conclusion'] = [BeautifulSoup(text).get_text() for text in df['conclusion'] ]
df.to_csv('lallontop.csv')
