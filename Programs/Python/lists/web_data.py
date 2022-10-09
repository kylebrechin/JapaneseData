import requests, csv, time, json
from bs4 import BeautifulSoup as bs
from KKLC import KODANSHA_LEARNERS_LIST as kklc_list
# get the URL
with open('kanji_map.csv', 'w') as out_file:
    writer = csv.writer(out_file, quoting=csv.QUOTE_ALL)
    for idx, kj in enumerate(kklc_list[:1], start=1):
        # parse the JSON information for all of the kanji in the KKLC list
        url_start = "https://thekanjimap.com/"
        url = url_start + str(kj)
        page = requests.get(url)
        soup = bs(page.text, "html.parser")
        found = soup.find("script", {"id": "__NEXT_DATA__"})
        found_json = json.loads(found.text)
        data = found_json.get("props").get("pageProps").get("kanjiInfo")
        data = [idx, kj, data]
        # debug line
        print("#" + str(idx) + " " + kj + " > " + str(data))
        writer.writerow(data)
        time.sleep(2)














# # assign the URL
# #URL = "https://thekanjimap.com/%E4%BA%AC"
# URL = "https://thekanjimap.com/京"
# # get the page information from the URL
# page = requests.get(URL)
# # parse the received data from the URL
# soup = bs(page.text, "html.parser")
# # single out the JSON from the web page
# found = soup.find("script", {"id": "__NEXT_DATA__"})
# # throw it into a jsdon container
# found_json = json.loads(found.text)
# # get the specific data
# data = found_json.get("props").get("pageProps").get("kanjiInfo")
# # print(found_json)
# print(data)