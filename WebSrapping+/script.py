import requests
import pandas
from bs4 import BeautifulSoup

res = []
for page in range(0,300,20):
    r = requests.get("https://www.airbnb.com/s/Big-Bear/homes?flexible_trip_dates%5B%5D=april&flexible_trip_dates%5B%5D=may&adults=2&search_type=pagination&checkin=2021-03-27&refinement_paths%5B%5D=%2Fhomes&date_picker_type=calendar&flexible_trip_lengths%5B%5D=weekend_trip&checkout=2021-03-28&tab_id=home_tab&place_id=ChIJ3yNiUlOxxIARil2OT3SLF5Q&federated_search_session_id=cdc79671-a5f7-4beb-b17f-8a4044ddf3d0&items_offset={}&section_offset=3".format(page), headers={'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'})
    c = r.content

    soup = BeautifulSoup(c, "html.parser")

    all = soup.find_all("div", {"class":"_gig1e7"})
    hotel_name = []
    price_per_night = []
    reviews = []
    for item in all:
        hotel_name = item.find("a",{"class":"_gjfol0"}).get("aria-label")
        price_per_night = item.find("button",{"class": "_ebe4pze"}).text.split(" ")[0]
        try:
            reviews = item.find(name = "span",attrs = {"aria-label": True}).get("aria-label")

        except:
            reviews = "/"
        df = {}
        df["Hotel Name"] = hotel_name
        df["Price/Night"] = price_per_night
        df["Reviews"] = reviews
        res.append(df)


final_results = pandas.DataFrame(res)

final_results.to_csv("Output"+"bear"+".csv")