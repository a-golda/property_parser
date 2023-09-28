import requests
from bs4 import BeautifulSoup


class ScraperListam:
    """
    Gett all links and all content from https://www.list.am/category/56.
    """
    headers = {
        'User-Agent': 'My User Agent 1.0',
        'From': 'golubev.anton94@mail.ru'  # This is another valid field
    }

    def __init__(self):
        pass

    def scrap(self, n):
        links = {}
        city_links = []
        page = 1
        while True:
            print(page)
            url = self.get_one_link(page)
            res = requests.get(url, headers=ScraperListam.headers)
            soup = BeautifulSoup(res.content)
            if n == page:
                break
            if not self.check_last_page(soup, self.get_one_link(page+1)):
                break
            else:
                tmp_links = self.get_links_from_page(soup)
            for link in tmp_links:
                city_links.append(link)
            page += 1
        links = city_links
        return links

    def get_one_link(self, page):
        url = f'https://www.list.am/category/56/{page}?n=1'
        return url

    def get_links_from_page(self, soup):
        res_links = [i.get("href") for i in soup.findAll("a", href=True)]
        res_links = [i for i in res_links if 'item' in i]
        return res_links

    def check_last_page(self, soup, link):
        href_url = soup.find('link').get('href')
        if href_url in link:
            return True
        else:
            return False

    def get_data_from_link(self, page_link):
        res = requests.get(page_link, headers=ScraperListam.headers)
        soup = BeautifulSoup(res.content)

        title = soup.findAll('h1')[0].text
        address = soup.findAll('div', {'class': 'loc'})[0].text
        price = soup.findAll('span', {'class': 'price x'})[0].text
        description = soup.findAll('div', {'class': 'body', 'itemprop': 'description'})[0].text
        area_dist = [i.text for i in soup.find('table').findAll("tr")]

        update_number_date = [i.text for i in soup.find('div', {'class': 'footer'})]

        data = {}
        for el in soup.findAll('div', {'class': 'c'}):
            try:
                key = el.find('div', {'class': 't'}).text
                value = el.find('div', {'class': 'i'}).text
                data[key] = value
            except:
                pass


# scraper = ScraperListam()
# general_links = scraper.scrap(12)
# print('done!')

# url = 'https://www.list.am/ru/item/19472531'
# res = requests.get(url, headers=ScraperListam.headers)
# soup = BeautifulSoup(res.content)
#
#
# title = soup.findAll('h1')[0].text
# address = soup.findAll('div', {'class':'loc'})[0].text
# price = soup.findAll('span', {'class':'price x'})[0].text
# description = soup.findAll('div', {'class':'body', 'itemprop': 'description'})[0].text
# area_dist = [i.text for i in soup.find('table').findAll("tr")]
#
#
# data = {}
# for el in soup.findAll('div', {'class':'c'}):
#     try:
#         key = el.find('div', {'class':'t'}).text
#         value = el.find('div', {'class':'i'}).text
#         data[key] = value
#     except:
#         pass
#
# update_number_date = [i.text for i in soup.find('div', {'class':'footer'})]



