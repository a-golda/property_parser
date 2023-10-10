import requests
from bs4 import BeautifulSoup


r = requests.get(f"https://krisha.kz/a/show/685339926")
soup = BeautifulSoup(r.content)


try:
    title = soup.find('h1').text
except:
    title = None

try:
    price = soup.find('div', 'offer__price').text
except:
    price = None

try:
    city_area = soup.find('div', 'offer__location offer__advert-short-info').text
except:
    city_area = None

try:
    residential_complex = soup.find('div', {'data-name': 'map.complex'}).find('div', 'offer__advert-short-info').text
except:
    residential_complex = None

try:
    area_sq_m = soup.find('div', {'data-name':'live.square'}).find('div', 'offer__advert-short-info').text
except:
    area_sq_m = None

try:
    renovation = next([soup.find('div', {'data-name':'flat.rent_renovation'}).find('div', 'offer__advert-short-info').text,
                       soup.find('dt', {'data-name':'flat.rent_renovation'}).text])
except:
    renovation = None

try:
    security = next([soup.find('div', {'data-name': 'flat.security'}).find('div', 'offer__advert-short-info').text,
                     soup.find('dt', {'data-name': 'flat.security'}).text])
except:
    security = None

try:
    priv_dorm = next([soup.find('div', {'data-name': 'flat.priv_dorm'}).find('div', 'offer__advert-short-info').text,
                     soup.find('dt', {'data-name': 'flat.priv_dorm'}).text])
except:
    priv_dorm = None

try:
    furniture = next([soup.find('div', {'data-name': 'flat.furniture'}).find('div', 'offer__advert-short-info').text,
                      soup.find('dt', {'data-name': 'flat.furniture'}).text])
except:
    furniture = None

try:
    live_furniture = next([soup.find('div', {'data-name': 'live.furniture'}).find('div', 'offer__advert-short-info').text,
                           soup.find('dt', {'data-name': 'live.furniture'}).text])
except:
    live_furniture = None

try:
    kitchen_studio_flag = next([soup.find('div', {'data-name': 'kitchen_studio'}).find('div', 'offer__advert-short-info').text,
                                soup.find('dt', {'data-name': 'kitchen_studio'}).text])
except:
    kitchen_studio_flag = None

try:
    floor = next([soup.find('div', {'data-name': 'flat.floor'}).find('div', 'offer__advert-short-info').text,
                  soup.find('dt', {'data-name': 'flat.floor'}).text])
except:
    floor = None

try:
    building = next([soup.find('div', {'data-name': 'flat.building'}).find('div', 'offer__advert-short-info').text,
                     soup.find('dt', {'data-name': 'flat.building'}).text])
except:
    building = None

try:
    house_year = next([soup.find('div', {'data-name': 'house.year'}).find('div', 'offer__advert-short-info').text,
                       soup.find('dt', {'data-name': 'house.year'}).text])
except:
    house_year = None

try:
    inet_type = next([soup.find('div', {'data-name': 'inet.type'}).find('div', 'offer__advert-short-info').text,
                      soup.find('dt', {'data-name': 'inet.type'}).text])
except:
    inet_type = None

try:
    flat_toilet = next([soup.find('div', {'data-name': 'flat.toilet'}).find('div', 'offer__advert-short-info').text,
                        soup.find('dt', {'data-name': 'flat.toilet'}).text])
except:
    flat_toilet = None

try:
    flat_balcony = next([soup.find('div', {'data-name': 'flat.balcony'}).find('div', 'offer__advert-short-info').text,
                         soup.find('dt', {'data-name': 'flat.balcony'}).text])
except:
    flat_balcony = None

try:
    flat_balcony_g = next([soup.find('div', {'data-name': 'flat.balcony_g'}).find('div', 'offer__advert-short-info').text,
                           soup.find('dt', {'data-name': 'flat.balcony_g'}).text])
except:
    flat_balcony_g = None

try:
    flat_door = next([soup.find('div', {'data-name': 'flat.door'}).find('div', 'offer__advert-short-info').text,
                      soup.find('dt', {'data-name': 'flat.door'}).text])
except:
    flat_door = None

try:
    flat_parking = next([soup.find('div', {'data-name': 'flat.parking'}).find('div', 'offer__advert-short-info').text,
                         soup.find('dt', {'data-name': 'flat.parking'}).text])
except:
    flat_parking = None

try:
    flat_flooring = next([soup.find('div', {'data-name': 'flat.flooring'}).find('div', 'offer__advert-short-info').text,
                          soup.find('dt', {'data-name': 'flat.flooring'}).text])
except:
    flat_flooring = None

try:
    flat_facilities = next([soup.find('div', {'data-name': 'flat.balcony'}).find('div', 'offer__advert-short-info').text,
                            soup.find('dt', {'data-name': 'flat.furniture'}).text])
except:
    flat_facilities = None

try:
    who_match = next([soup.find('div', {'data-name': 'who_match'}).find('div', 'offer__advert-short-info').text,
                      soup.find('dt', {'data-name': 'who_match'}).text])
except:
    who_match = None

try:
    separated_toilet = next([
        soup.find('div', {'data-name': 'separated_toilet'}).find('div', 'offer__advert-short-info').text,
        soup.find('dt', {'data-name': 'separated_toilet'}).text])
except:
    separated_toilet = None

try:
    toilet_count = next([soup.find('div', {'data-name': 'toilet_count'}).find('div', 'offer__advert-short-info').text,
                         soup.find('dt', {'data-name': 'toilet_count'}).text])
except:
    toilet_count = None

try:
    bathroom = next([soup.find('div', {'data-name': 'bathroom'}).find('div', 'offer__advert-short-info').text,
                     soup.find('dt', {'data-name': 'bathroom'}).text])
except:
    bathroom = None

try:
    window_side = next([soup.find('div', {'data-name': 'window_side'}).find('div', 'offer__advert-short-info').text,
                        soup.find('dt', {'data-name': 'window_side'}).text])
except:
    window_side = None

try:
    balcony_count = next([soup.find('div', {'data-name': 'balcony_count'}).find('div', 'offer__advert-short-info').text,
                          soup.find('dt', {'data-name': 'balcony_count'}).text])
except:
    balcony_count = None

try:
    loggia_count = next([soup.find('div', {'data-name': 'loggia_count'}).find('div', 'offer__advert-short-info').text,
                         soup.find('dt', {'data-name': 'loggia_count'}).text])
except:
    loggia_count = None

try:
    ceiling = next([soup.find('div', {'data-name': 'ceiling'}).find('div', 'offer__advert-short-info').text,
                    soup.find('dt', {'data-name': 'ceiling'}).text])
except:
    ceiling = None

try:
    photos = [picture.attrs.get('src') for picture in soup.find_all('img')]
except:
    photos = None

try:
    owners_name = soup.find('div', 'owners__name').text
except:
    owners_name = None

try:
    owner_type = soup.find('div', 'owners__label owners__label--transparent label-user-identified-company').text
except:
    owner_type = None

try:
    description = soup.find('div', 'a-text a-text-white-spaces').text
except:
    description = None

try:
    since = soup.find('div', 'offer__views').text
except:
    since = None

final = \
    {
        'title':title,
        'price':price,
        'city_area':city_area,
        'residential_complex':residential_complex,
        'area_sq_m':area_sq_m,
        'renovation':renovation,
        'security':security,
        'priv_dorm':priv_dorm,
        'furniture':furniture,
        'live_furniture':live_furniture,
        'kitchen_studio_flag':kitchen_studio_flag,
        'floor':floor,
        'building':building,
        'house_year':house_year,
        'inet_type':inet_type,
        'flat_toilet':flat_toilet,
        'flat_balcony':flat_balcony,
        'flat_balcony_g':flat_balcony_g,
        'flat_door':flat_door,
        'flat_parking':flat_parking,
        'flat_flooring':flat_flooring,
        'flat_facilities':flat_facilities,
        'who_match':who_match,
        'separated_toilet':separated_toilet,
        'toilet_count':toilet_count,
        'bathroom':bathroom,
        'window_side':window_side,
        'balcony_count':balcony_count,
        'loggia_count':loggia_count,
        'ceiling':ceiling,
        'photos':photos,
        'owners_name':owners_name,
        'owner_type':owner_type,
        'description':description,
        'since':since
    }

print(final)