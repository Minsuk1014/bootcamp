import streamlit as st
from get_info import recomand as get_info, get_name_to_code
from datetime import datetime
import logging, os
import pathlib

pathlib.Path.mkdir("./log_file",parents=True,exist_ok=True)
file_name = "service_" + datetime.now().strftime("%Y%m%d%H%M%S") + ".log"
log_format = '%(asctime)s - %(levelname)s - %(name)s - %(message)s'
log_datefmt = '%Y-%m-%d %H:%M:%S' # 예: 2025-04-22 10:07:49


logging.basicConfig(filename="./logs/" + file_name,  level=logging.INFO, # INFO 레벨 이상만 기록
                    format=log_format,
                    datefmt=log_datefmt)


st.title("공시정보 보여주기")

st.header("공시정보 조회")

col1, col2, col3 = st.columns(3)

with col1:
    input_code = st.text_input(label='종목명을 입력해주세요.', placeholder="예) 삼성전자")

with col2:
    input_start = st.text_input(label='시작 날짜을 입력해주세요.', placeholder="예) 20151014")

with col3:
    input_end = st.text_input(label='종료 날짜을 입력해주세요.', placeholder="예) 20201014")

if st.button("조회"):
    logging.info(f"{input_code} - {input_start} - {input_end}")
    rt = get_info(get_name_to_code(input_code), input_start, input_end)
    st.write(rt)


