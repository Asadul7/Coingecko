import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.coingecko.com/'
responses = requests.get(url)
soup = BeautifulSoup(responses.content, 'html.parser')

coin_names = []
price = []
volumes = []
mrk_cap = []

coin = soup.find_all('span', attrs={"class":"lg:tw-flex font-bold tw-items-center tw-justify-between"})
for name in coin:
    coin_name = name.get_text().replace('\n', '')
    coin_names.append(coin_name + ',')

value = soup.find_all('td', attrs={"class":"td-price price text-right"})
for coin_price in value:
    prices = coin_price.get_text().replace('\n', '').replace(',', '')
    price.append(prices+ ',')

volume = soup.find_all('td', attrs={"class":"td-liquidity_score lit text-right col-market"})
for vol in volume:
    twenty_four_volume = vol.get_text().replace('\n', '').replace(',', '')
    volumes.append(twenty_four_volume+ ',')

m_cap = soup.find_all('td', attrs={"class":"td-market_cap cap col-market cap-price text-right"})
for cap in m_cap:
    market_cap = cap.get_text().replace('\n', '').replace(',', '')
    mrk_cap.append(market_cap + ',')

coingecko = {
    "coin": coin_names,
    "price": price,
    "volume": volumes,
    "market_cap": mrk_cap
}

data = pd.DataFrame(coingecko)
data.to_csv('coingecko_data.csv', index=False, sep='\t')
