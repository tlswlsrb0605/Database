import requests
import bs4
city = ['강남 MICE 관광특구', '동대문 관광특구', '명동 관광특구', '이태원 관광특구', '잠실 관광특구',
'종로·청계 관광특구', '홍대 관광특구', '경복궁·서촌마을', '광화문·덕수궁', '창덕궁·종묘',
'가산디지털단지역', '강남역', '건대입구역', '고속터미널역', '교대역',
'구로디지털단지역', '서울역', '선릉역', '신도림역', '신림역',
'신촌·이대역', '역삼역', '연신내역', '용산역', '왕십리역',
'DMC(디지털미디어시티)', '창동 신경제 중심지', '노량진', '낙산공원·이화마을', '북촌한옥마을',
'가로수길', '성수카페거리', '수유리 먹자골목', '쌍문동 맛집거리', '압구정로데오거리',
'여의도', '영등포 타임스퀘어', '인사동·익선동', '국립중앙박물관·용산가족공원', '남산공원',
'뚝섬한강공원', '망원한강공원', '반포한강공원', '북서울꿈의숲', '서울대공원',
'서울숲공원', '월드컵공원', '이촌한강공원', '잠실종합운동장', '잠실한강공원']

key = '5172665055746c733534474b6d576a'
def state_weather(xml_obj):
    
    weather_data = xml_obj.findAll('WEATHER_STTS')

    for data in weather_data:
        pcpmsg = data.find('PCP_MSG').get_text()
        temp = data.find('TEMP').get_text()
        sentemp = data.find('SENSIBLE_TEMP').get_text()
        pm10idx = data.find('PM10_INDEX').get_text()
        pm25idx = data.find('PM25_INDEX').get_text()
    print('날씨 : ' + pcpmsg)
    print('현재온도 : '+ temp)
    print('체감온도 : ' + sentemp)
    print('미세먼지 : '+ pm10idx)
    print('초미세먼지 : '+ pm25idx)

def state_congestion(xml_obj):
    congestion_data = xml_obj.findAll('LIVE_PPLTN_STTS')
    
    for data in congestion_data:
        conlvl = data.find('AREA_CONGEST_LVL').get_text()
        conmsg = data.find('AREA_CONGEST_MSG').get_text()
    
    print('혼잡도 : ' + conmsg)
    print('혼잡도 : ' + conlvl)

def state_subway(xml_obj):
    subway_data = xml_obj.findAll('SUB_STTS')
    flag = 0
    for data in subway_data:
        if flag == 0:
            flag = flag+1
        else:
            subname = data.find('SUB_STN_NM').get_text()
            print('지하철역 : ' + subname)
            subLine = data.find('SUB_STN_LINE').get_text()
            print(subLine + '호선')
        
def state_bike(xml_obj):
    bike_data = xml_obj.findAll('SBIKE_STTS')
    flag = 0
    for data in bike_data:
        if flag == 0:
            flag = flag+1
        else:
            bikespot = data.find('SBIKE_SPOT_NM').get_text()
            print(bikespot)
            bikecnt = data.find('SBIKE_PARKING_CNT').get_text()
            print('주차된 따릉이 수: '+bikecnt)

def end():
    print('------------------------------------------------------')
    print('더 알아보기')
    print('1.날씨 2.혼잡도 3.가까운 지하철역 4.따릉이 정류장 및 현황')
    print ('5. 다른지역 검색하기')
    a = int(input())
    print('------------------------------------------------------')
    return a

def state_0():
    print('------------------지역을 입력해주세요-------------------')
    area = input()
    url = 'http://openapi.seoul.go.kr:8088/'+key+'/xml/citydata/1/2/' + area
    result = requests.get(url)
    xml_obj = bs4.BeautifulSoup(result.text,'lxml-xml')
    print('정보 선택')
    print('1.날씨 2.혼잡도 3.가까운 지하철역 4.따릉이 정류장 및 현황')
    return xml_obj

for i in city:
        print(i)

mode = 0

while(True):
    if mode == 1:
        state_weather(xml_obj)
        mode = end()
    elif mode == 2:
        state_congestion(xml_obj)
        mode = end()
    elif mode == 3:
        state_subway(xml_obj)
        mode = end()
    elif mode == 4:
        state_bike(xml_obj)
        mode = end()
    else :
        xml_obj = state_0()
        mode = int(input())
    


