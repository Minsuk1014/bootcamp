import requests
from bs4 import BeautifulSoup 
from xml.etree import ElementTree as ET
import requests
import os
import pathlib
import pandas as pd


def get_symbol(name) -> list :
    """
    주식 이름 입력하면 주식 코드 발행
    """ 
    url = "https://www.ktb.co.kr/trading/popup/itemPop.jspx"
    data = { # 왜 data로 잡은거야? -> 기본 문법이셔
        "searchText": f"{name}",  # 검색어
    }

    r = requests.post(url, data=data)
    r = BeautifulSoup(r.text)  # 서버로부터 받은 HTML 응답 출력
    #find_all ("태그","속성")

    compare = []
    symbol_all = str(r.find("tbody", class_ ="tbody_content").find_all("td"))
    for i in range(1,len(symbol_all),2):
        try:
            code,title = str(r.find("tbody", class_ ="tbody_content").find_all("td")[i]).split(',')[1:3] # 홀수
            title = title.replace(" ",'')[1:-1]
            if name == title:
                c_sum = [code[1:-1]]
                compare.append(c_sum)
                return compare
        except:
            break


def recomand(title : str ,start : int, end : int, path=""):
    symbol = get_symbol(title)
    if symbol == None or len(start) != 8 or len(end) != 8:
        print("해당 종목은 없습니다. 혹은 영어로 검색해주세요.")
        return "입력값을 다시 확인해주세요."
    url = f"https://m.stock.naver.com/front-api/external/chart/domestic/notice?symbol={symbol[0][0]}&startTime={start}&endTime={end}&requestType=0"

    data = requests.get(url).text
    root = ET.fromstring(data) # BuatifulSoop 같은 파싱
    items = root.iter(tag="item") # find처럼 찾기. (전체적으로 찾음 이를테면 item 이 있는 전부)

    total = []
    for i in items: # 첫 item 블록부터 마지막 item블록까지 전달 (크게보면 부모)
        for j in i: #거기중에서 item에서 자식찾는거니까
            total.append({"date" : i.get("date") ,"information" : j.text})

    if path == "":
        path = title

    total = pd.DataFrame(total)
    return total
    pathlib.Path(f"./{path}").mkdir(parents=True, exist_ok=True)
    total.to_csv(f"./{path}/{path}.csv", index=False, encoding="utf-8-sig") # csv 저장하는 방법.. 까먹지 않기.


if __name__ == "__main__": # 테스트용 독단적으로 사용
    recomand("삼성전자",20221128,20230726)