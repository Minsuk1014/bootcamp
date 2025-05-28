import streamlit as st
from recomand import recomand


st.title("공시정보 보여주기")

st.header("공시정보 조회")

input_code = st.text_input(label='이름과 시작 날짜와 끝나는 날짜를 입력해주세요.', placeholder="예) 이름 005930 20250521{시작} 20250525{끝나는 날짜} 숫자만 입력")
input_code = input_code.split()

if input_code:
    input_code[0] = str(input_code[0])
    rt = recomand(input_code[0], input_code[1], input_code[2])
    st.write(rt)
    