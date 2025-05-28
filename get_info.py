from xml.etree import ElementTree as ET
import requests
import os
import pathlib
import pandas as pd
import requests
"""
https://m.stock.naver.com/front-api/external/chart/domestic/notice?symbol=290650&startTime=20221128&endTime=20230726&requestType=0
"""

def recomand(symbol,start,end,path=""):
    url = f"https://m.stock.naver.com/front-api/external/chart/domestic/notice?symbol={symbol}&startTime={start}&endTime={end}&requestType=0"

    data = requests.get(url).text
    root = ET.fromstring(data)

    items = root.iter(tag='item')
    total = []
    for i in items:
        for x in i:
            total.append({'date' : i.get('date'), 'information' : x.text})

    total = pd.DataFrame(total)
    if path == "":
        path = symbol
    pathlib.Path(f"./{path}").mkdir(parents=True, exist_ok=True)
    return total
    total.to_csv(f"./{path}/{path}.csv", index=False, encoding="utf-8-sig") # csv 저장하는 방법.. 까먹지 않기.

def get_name_to_code(target):
    url = "http://data.krx.co.kr/comm/bldAttendant/getJsonData.cmd"


    payload={"bld":"dbms/MDC/STAT/standard/MDCSTAT01901",
    "locale":"ko_KR",
    "mktId":"ALL",
    "share":"1",
    "csvxls_isNo":"false",}


    request_headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
        "Connection": "keep-alive",
        "Content-Length": "88",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Host": "data.krx.co.kr",
        "Origin": "http://data.krx.co.kr",
        "Referer": "http://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201020201",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
    }
    r= requests.post(url, data=payload, headers=request_headers)
    data = r.json()['OutBlock_1']
    rt = [y['ISU_SRT_CD'] for y in [ x for x in data if x['ISU_ABBRV'].find(f"{target}") > -1] if y['ISU_ABBRV'].find(target + '우') == -1]
    if len(rt) > 0:
        return rt[0]
    else:
        return '종목 코드가 존재하지 않음'



if __name__ == "__main__": # 테스트용 독단적으로 사용
    recomand(290650,20221128,20230726,"엘엔씨바이오")

