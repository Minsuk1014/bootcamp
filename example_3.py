"""
아이디와 비밀번호를 입력하면 데이터베이스에 저장하는 홈페이지를 만들어보자. 
"""
import pymysql
import streamlit as st
# import requests

def my_info(id,pw):
    conn = pymysql.connect(host='127.0.0.1', user = 'play', passwd = '123', database= 'sk15', port=3306) # 기본포트 3306로 연결
    cur = conn.cursor() # 내 데이터 베이스에 포인터 쏘기 / 연결
    sql = "INSERT into protics values (%s, %s)"
    cur.execute(sql,[id,pw])
    conn.commit()


st.title("아이디 비밀번호 입력하기")
st.subheader("데이터 베이스에 넘기기")

col1,col2 = st.columns(2)

with col1:
    id = st.text_input("ID 입력")
with col2:
    pw = st.text_input("PW 입력")

if st.button("버튼"):
    if id and pw :
        my_info(id,pw)
        st.write("데이터 베이스 전달 완료")





