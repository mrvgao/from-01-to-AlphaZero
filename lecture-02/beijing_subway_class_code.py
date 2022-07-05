import requests
from collections import defaultdict
from bs4 import BeautifulSoup
import pickle

# url = 'https://www.bjsubway.com/station/xltcx/'
#
# response = requests.get(url)
# response.encoding = 'gbk'
#
# print(response.text)
#
# html_file = open('subway.html', 'w')
#
# with html_file:
#     html_file.write(response.text)

html_file = open('subway.html').read()


soup = BeautifulSoup(html_file, 'html.parser')

lines = soup.find_all(attrs={'class': 'line_name'})

line_with_stations = defaultdict(list)

for line in lines:
    line_name = line.text.strip()

    for s in line.next_siblings:
        if s.string and BeautifulSoup(s.string).find_all(attrs={'class': 'line_name'}): break

        text = s.string
        if text and text.strip():
            station = text.strip()
            line_with_stations[line_name].append(station)


print(line_with_stations)

with open('line_with_station.pkl', 'wb') as f:
    pickle.dump(line_with_stations, f)
    # f.write(line_with_stations)
