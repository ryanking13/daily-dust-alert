import json
import requests
try:
    from .config import api_key
except:
    api_key = ''

api_url = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty'

grade2str = {
    1: '좋음',
    2: '보통',
    3: '나쁨',
    4: '매우나쁨',
}


def get_dust_information(station_name='관악구'):
    # '?stationName=종로구&dataTerm=month&pageNo=1&numOfRows=10&ServiceKey=서비스키&ver=1.3'
    params = {
        'stationName': station_name,
        'dataTerm': 'daily',
        'pageNo': '1',
        'numOfRows': '5',
        'ServiceKey': api_key,
        'ver': '1.3',
        '_returnType': 'json',
    }

    r = requests.get(url=api_url, params=params)
    data = r.json()

    # pm10: 미세먼지
    # pm2.5: 초미세먼지
    pm10 = int(data['list'][0]['pm10Value'])
    pm25 = int(data['list'][0]['pm25Value'])
    pm10_grade = int(data['list'][0]['pm10Grade'])
    pm25_grade = int(data['list'][0]['pm25Grade'])

    return {
        'pm10': pm10,
        'pm10_grade': pm10_grade,
        'pm10_grade_str': grade2str[pm10_grade],
        'pm25': pm25,
        'pm25_grade': pm25_grade,
        'pm25_grade_str': grade2str[pm25_grade],
    }


def get_dust_information_dummy():
    return {
        'pm10': 72,
        'pm10_grade': 2,
        'pm10_grade_str': grade2str[2],
        'pm25': 37,
        'pm25_grade': 2,
        'pm25_grade_str': grade2str[2],
    }


if __name__ == '__main__':
    print(get_dust_information())
