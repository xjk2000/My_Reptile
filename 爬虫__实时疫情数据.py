import requests
from lxml import etree
import json

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                         'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

url="https://gwpre.sina.cn/interface/news/ncp/data.d.json?mod=province&province=hunan&callback=_aProvinceFunction&_=1590321853162"
def data(url):
    html=requests.get(url,headers=headers)
    start=html.text.find('{"status":')
    end=html.text.find(',"econNum":"4","asymptomNum":0}]}}')+len(',"econNum":"4","asymptomNum":0}]}}')
    json_Data=json.loads(html.text[start:end])
    get_data=json_Data['data']
    print('时间:',get_data['times'],end='    ')
    print('地点:',get_data['province'],end='\n')
    print('现存确诊:',get_data['conadd'],end='\n')
    print('累计确诊:',get_data['contotal'],end='\n')
    print('累计死亡:', get_data['deathtotal'], end='\n')
    print('累计治愈:', get_data['curetotal'], end='\n')

def city_data():
    html = requests.get(url, headers=headers)
    start = html.text.find('{"status":')
    end = html.text.find(',"econNum":"4","asymptomNum":0}]}}') + len(',"econNum":"4","asymptomNum":0}]}}')
    json_Data = json.loads(html.text[start:end])
    name = input("请输入城市(xx市/湘西自治州/境外输入):")
    for i in range(15):
        if name == json_Data['data']['city'][i]['name']:
            print(json_Data['data']['city'][i]['name'])
            print("累计确诊:",json_Data['data']['city'][i]['conNum'])
            print("新增确诊:", json_Data['data']['city'][i]['conadd'])
            print("累计治愈:", json_Data['data']['city'][i]['cureNum'])
            print("累计死亡:", json_Data['data']['city'][i]['deathNum'])


if __name__ == '__main__':
    data(url)
    city_data()
