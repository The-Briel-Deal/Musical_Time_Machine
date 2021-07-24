import bs4
import requests
class MusicScrape:
    def __init__(self):
        date = input('What year would you like to get the top 100 songs from YYYY-MM-DD\n')
        top_100 = requests.get(url=f'https://www.billboard.com/charts/hot-100/{date}')
        musical_soup = bs4.BeautifulSoup(top_100.text, features='html.parser')

        self.lots_of_noodles = musical_soup.find_all('span', {"class": "chart-element__information__song "
                                                                       "text--truncate "
                                                                       "color--primary"})

    def return_noods(self):
        _ = []
        for item in self.lots_of_noodles:
            _.append(item.string)
        return _
