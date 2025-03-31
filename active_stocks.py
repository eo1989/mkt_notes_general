# API_KEY_ALPHAVANTAGE='04E3CQSU4564LBDN'
# API_KEY_FINANCIALMODELINGPREP='e45b9d954f1407d6407d0bb1324bb6a0'
# API_KEY_QUANDL='hgwjCyQ2KsYot6Gsh1Vj'
# API_FRED_KEY='519365e0660f928c1ff9264b38038d85'
# API_NEWS_TOKEN='d10189f6019b42f68ebd07ce80b1bfe2'
# API_FINNHUB_KEY='brof047rh5r8qo238v4g'

import dotenv
import polars as pl
import requests as rs
from bs4 import BeautifulSoup

# dotenv.load_dotenv("C:/Users/eorlo/.openbb_terminal/.env")
# dotenv.dotenv_values(dotenv_path="C:/Users/eorlo/.openbb_terminal/.env")
fmp_key = dotenv.get_key(dotenv_path="C:/Users/eorlo/.openbb_terminal/.env", key_to_get="API_KEY_FINANCIALMODELINGPREP")

url = "https://marketbeat.com/most-active-stocks"

response = rs.get(url)
soup = BeautifulSoup(response.text, "html.parser")

table = soup.find("table", {"class": "stocksTable"})

headers = []
for th in table.find_all("th"):
	headers.append(th.text.strip())


data = []
rows = table.find_all("tr")[1:26] # top 25

for row in rows:
	cols = row.find_all("td")
	cols = [ele.text.strip() for ele in cols]
	data.append(cols)

df = pl.DataFrame(data, schema=headers)

print(df.head(25))
