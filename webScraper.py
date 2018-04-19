import requests
from bs4 import BeautifulSoup
import redis

nse_url = "https://www.nseindia.com/products/dynaContent/common/productsSymbolMapping.jsp?instrumentType=FUTIDX&symbol=NIFTY&expiryDate=22-02-2018&optionType=select&strikePrice=&dateRange=3month&fromDate=&toDate=&segmentLink=9&symbolCount="

payload = {'instrumentType': 'FUTSTK', 'symbol': 'ICICIBANK', 'year': '2018', 'expiryDate': '25-01-2018',
           'optionType': 'select', 'strikePrice': '',
           'dateRange': '3month', 'fromDate': '', 'toDate': '', 'segmentLink': '9', 'symbolCount': ''}

page = requests.get(nse_url)
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())

r = redis.StrictRedis(host='redis-13025.c10.us-east-1-4.ec2.cloud.redislabs.com', port=13025,
                      password='OFoRTFqenf3ZfSGMraCqQCdtFZo8E7DZ', charset='utf-8', decode_responses=True)
r.flushall()

tableHead = soup.find("table").find_all("th")
tableData = soup.find("table").find_all("td")

headers = []
for row in tableHead:
    headers.append(row.text)
print(headers)

values = []
for row in tableData:
    values.append(row.text)
print(values)

i = 0
for val in range(len(values) // 14):
    mapping = {headers[1]: values[i], headers[2]: values[i + 1], headers[3]: values[i + 2],
               headers[4]: values[i + 3], headers[5]: values[i + 4], headers[6]: values[i + 5],
               headers[7]: values[i + 6], headers[8]: values[i + 7], headers[9]: values[i + 8],
               headers[10]: values[i + 9], headers[11]: values[i + 10], headers[12]: values[i + 11],
               headers[13]: values[i + 12], headers[14]: values[i + 13]}
    print(mapping)
    r.hmset(values[i + 1], mapping)
    i = i + 14

print('\nRetrieve from redis DB: \n')
print(r.hgetall('22-Feb-2018'))
