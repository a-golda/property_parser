import requests
from bs4 import BeautifulSoup

r = requests.get(f"https://krisha.kz/a/show/56146318")
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
    is_active_attribute = bool(soup.find('div', 'offer__price').text)
except:
    is_active_attribute = False

try:
    city_area = soup.find('div', 'offer__location offer__advert-short-info').text
except:
    city_area = None

try:
    residential_complex = soup.find('div', {'data-name': 'map.complex'}).find('div', 'offer__advert-short-info').text
except:
    residential_complex = None

try:
    area_sq_m = soup.find('div', {'data-name': 'live.square'}).find('div', 'offer__advert-short-info').text
except:
    area_sq_m = None

try:
    renovation_1 = soup.find('div', {'data-name': 'flat.rent_renovation'}).find('div', 'offer__advert-short-info').text
except:
    renovation_1 = None

try:
    renovation_2 = soup.find('dt', {'data-name': 'flat.rent_renovation'}).text
except:
    renovation_2 = None

renovation = renovation_1 or renovation_2


try:
    security_1 = soup.find('div', {'data-name': 'flat.security'}).find('div', 'offer__advert-short-info').text
except:
    security_1 = None

try:
    security_2 = soup.find('dt', {'data-name': 'flat.security'}).text
except:
    security_2 = None

security = security_1 or security_2


try:
    priv_dorm_1 = soup.find('div', {'data-name': 'flat.priv_dorm'}).find('div', 'offer__advert-short-info').text
except:
    priv_dorm_1 = None

try:
    priv_dorm_2 = soup.find('dt', {'data-name': 'flat.priv_dorm'}).text
except:
    priv_dorm_2 = None

priv_dorm = priv_dorm_1 or priv_dorm_2


try:
    furniture_1 = soup.find('div', {'data-name': 'flat.furniture'}).find('div', 'offer__advert-short-info').text
except:
    furniture_1 = None

try:
    furniture_2 = soup.find('dt', {'data-name': 'flat.furniture'}).text
except:
    furniture_2 = None

furniture = furniture_1 or furniture_2

try:
    live_furniture_1 = soup.find('div', {'data-name': 'live.furniture'}).find('div', 'offer__advert-short-info').text
except:
    live_furniture_1 = None

try:
    live_furniture_2 = soup.find('dt', {'data-name': 'live.furniture'}).text
except:
    live_furniture_2 = None

live_furniture = live_furniture_1 or live_furniture_2

try:
    kitchen_studio_flag_1 = soup.find('div', {'data-name': 'kitchen_studio'}).find('div', 'offer__advert-short-info').text
except:
    kitchen_studio_flag_1 = None

try:
    kitchen_studio_flag_2 = soup.find('dt', {'data-name': 'kitchen_studio'}).text
except:
    kitchen_studio_flag_2 = None

kitchen_studio_flag = kitchen_studio_flag_1 or kitchen_studio_flag_2

try:
    floor_1 = soup.find('div', {'data-name': 'flat.floor'}).find('div', 'offer__advert-short-info').text
except:
    floor_1 = None

try:
    floor_2 = soup.find('dt', {'data-name': 'flat.floor'}).text
except:
    floor_2 = None

floor = floor_1 or floor_2


try:
    building_1 = soup.find('div', {'data-name': 'flat.building'}).find('div', 'offer__advert-short-info').text
except:
    building_1 = None

try:
    building_2 = soup.find('dt', {'data-name': 'flat.building'}).text
except:
    building_2 = None

building = building_1 or building_2


try:
    house_year_1 = soup.find('div', {'data-name': 'house.year'}).find('div', 'offer__advert-short-info').text
except:
    house_year_1 = None

try:
    house_year_2 = soup.find('dt', {'data-name': 'house.year'}).text
except:
    house_year_2 = None

house_year = house_year_1 or house_year_2


try:
    inet_type_1 = soup.find('div', {'data-name': 'inet.type'}).find('div', 'offer__advert-short-info').text
except:
    inet_type_1 = None

try:
    inet_type_2 = soup.find('dt', {'data-name': 'inet.type'}).text
except:
    inet_type_2 = None

inet_type = inet_type_1 or inet_type_2

try:
    flat_toilet_1 = soup.find('div', {'data-name': 'flat.toilet'}).find('div', 'offer__advert-short-info').text
except:
    flat_toilet_1 = None

try:
    flat_toilet_2 = soup.find('dt', {'data-name': 'flat.toilet'}).text
except:
    flat_toilet_2 = None

flat_toilet = flat_toilet_1 or flat_toilet_2

try:
    flat_balcony_1 = soup.find('div', {'data-name': 'flat.balcony'}).find('div', 'offer__advert-short-info').text
except:
    flat_balcony_1 = None

try:
    flat_balcony_2 = soup.find('dt', {'data-name': 'flat.balcony'}).text
except:
    flat_balcony_2 = None

flat_balcony = flat_balcony_1 or flat_balcony_2


try:
    flat_balcony_g_1 = soup.find('div', {'data-name': 'flat.balcony_g'}).find('div', 'offer__advert-short-info').text
except:
    flat_balcony_g_1 = None

try:
    flat_balcony_g_2 = soup.find('dt', {'data-name': 'flat.balcony_g'}).text
except:
    flat_balcony_g_2 = None

flat_balcony_g = flat_balcony_g_1 or flat_balcony_g_1

try:
    flat_door_1 = soup.find('div', {'data-name': 'flat.door'}).find('div', 'offer__advert-short-info').text
except:
    flat_door_1 = None

try:
    flat_door_2 = soup.find('dt', {'data-name': 'flat.door'}).text
except:
    flat_door_2 = None

flat_door = flat_door_1 or flat_door_2

try:
    flat_parking_1 = soup.find('div', {'data-name': 'flat.parking'}).find('div', 'offer__advert-short-info').text
except:
    flat_parking_1 = None

try:
    flat_parking_2 = soup.find('dt', {'data-name': 'flat.parking'}).text
except:
    flat_parking_2 = None

flat_parking = flat_parking_1 or flat_parking_2

try:
    flat_flooring_1 = soup.find('div', {'data-name': 'flat.flooring'}).find('div', 'offer__advert-short-info').text
except:
    flat_flooring_1 = None

try:
    flat_flooring_2 =soup.find('dt', {'data-name': 'flat.flooring'}).text
except:
    flat_flooring_2 = None

flat_flooring = flat_flooring_1 or flat_flooring_2


try:
    flat_facilities_1 = soup.find('div', {'data-name': 'flat.balcony'}).find('div', 'offer__advert-short-info').text
except:
    flat_facilities_1 = None

try:
    flat_facilities_2 = soup.find('dt', {'data-name': 'flat.furniture'}).text
except:
    flat_facilities_2 = None

flat_facilities = flat_facilities_1 or flat_facilities_2

try:
    who_match_1 = soup.find('div', {'data-name': 'who_match'}).find('div', 'offer__advert-short-info').text
except:
    who_match_1 = None

try:
    who_match_2 = soup.find('dt', {'data-name': 'who_match'}).text
except:
    who_match_2 = None

who_match = who_match_1 or who_match_2

try:
    separated_toilet_1 = soup.find('div', {'data-name': 'separated_toilet'}).find('div', 'offer__advert-short-info').text
except:
    separated_toilet_1 = None

try:
    separated_toilet_2 = soup.find('dt', {'data-name': 'separated_toilet'}).text
except:
    separated_toilet_2 = None

separated_toilet = separated_toilet_1 or separated_toilet_2

try:
    toilet_count_1 = soup.find('div', {'data-name': 'toilet_count'}).find('div', 'offer__advert-short-info').text
except:
    toilet_count_1 = None

try:
    toilet_count_2 = soup.find('dt', {'data-name': 'toilet_count'}).text
except:
    toilet_count_2 = None

toilet_count = toilet_count_1 or toilet_count_2

try:
    bathroom_1 = soup.find('div', {'data-name': 'bathroom'}).find('div', 'offer__advert-short-info').text
except:
    bathroom_1 = None

try:
    bathroom_2 = soup.find('dt', {'data-name': 'bathroom'}).text
except:
    bathroom_2 = None

bathroom = bathroom_1 or bathroom_2

try:
    window_side_1 = soup.find('div', {'data-name': 'window_side'}).find('div', 'offer__advert-short-info').text
except:
    window_side_1 = None

try:
    window_side_2 = soup.find('dt', {'data-name': 'window_side'}).text
except:
    window_side_2 = None

window_side = window_side_1 or window_side_2

try:
    balcony_count_1 =soup.find('div', {'data-name': 'balcony_count'}).find('div', 'offer__advert-short-info').text
except:
    balcony_count_1 = None

try:
    balcony_count_2 =soup.find('dt', {'data-name': 'balcony_count'}).text
except:
    balcony_count_2 = None

balcony_count = balcony_count_1 or balcony_count_2

try:
    loggia_count_1 = soup.find('div', {'data-name': 'loggia_count'}).find('div', 'offer__advert-short-info').text
except:
    loggia_count_1 = None

try:
    loggia_count_2 = soup.find('dt', {'data-name': 'loggia_count'}).text
except:
    loggia_count_2 = None

loggia_count = loggia_count_1 or loggia_count_2

try:
    ceiling_1 = next([soup.find('div', {'data-name': 'ceiling'}).find('div', 'offer__advert-short-info').text,
                    soup.find('dt', {'data-name': 'ceiling'}).text])
except:
    ceiling_1 = None

try:
    ceiling_2 = next([soup.find('div', {'data-name': 'ceiling'}).find('div', 'offer__advert-short-info').text,
                    soup.find('dt', {'data-name': 'ceiling'}).text])
except:
    ceiling_2 = None

ceiling = ceiling_1 or ceiling_2

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
        'is_active_attribute' : is_active_attribute,
        'title': title,
        'price': price,
        'city_area': city_area,
        'residential_complex': residential_complex,
        'area_sq_m': area_sq_m,
        'renovation': renovation,
        'security': security,
        'priv_dorm': priv_dorm,
        'furniture': furniture,
        'live_furniture': live_furniture,
        'kitchen_studio_flag': kitchen_studio_flag,
        'floor': floor,
        'building': building,
        'house_year': house_year,
        'inet_type': inet_type,
        'flat_toilet': flat_toilet,
        'flat_balcony': flat_balcony,
        'flat_balcony_g': flat_balcony_g,
        'flat_door': flat_door,
        'flat_parking': flat_parking,
        'flat_flooring': flat_flooring,
        'flat_facilities': flat_facilities,
        'who_match': who_match,
        'separated_toilet': separated_toilet,
        'toilet_count': toilet_count,
        'bathroom': bathroom,
        'window_side': window_side,
        'balcony_count': balcony_count,
        'loggia_count': loggia_count,
        'ceiling': ceiling,
        'photos': photos,
        'owners_name': owners_name,
        'owner_type': owner_type,
        'description': description,
        'since': since
    }

print(final)
