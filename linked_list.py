# 2025_05_26 
from linked import LinkedList
import streamlit as st
st.title("링크드 리스트 구현하기")
st.write("링크드 리스트 구현를 시각화")

if 'linked' not in st.session_state:
    st.session_state.linked = LinkedList()  # linked_list 연결 그리고 linked 라는 이름의 딕셔너리에 저장한거지?

st.sidebar.header("링크드 리스트 데이터 삽입")
st.sidebar.text_input("데이터 입력",key="data_input_val") # st.session_state["data_input_val"] = <입력한 값>

col1,col2,col3 = st.sidebar.columns(3) # 비율 지정

def append_data_callback():
    if st.session_state.data_input_val:     # 변수처럼 사용되지만, 딕셔너리 저장공간.
        st.session_state.linked.append(st.session_state.data_input_val)
    else:
        st.sidebar.warning("추가할 데이터를 입력")

def delete_data_callback():
    if st.session_state.data_input_val:     # 변수처럼 사용되지만, 딕셔너리 저장공간.
        st.session_state.linked.delete(st.session_state.data_input_val)
    else:
        st.sidebar.warning("추가할 데이터를 입력")

def prepend_data_callback():
    if st.session_state.data_input_val:     # 변수처럼 사용되지만, 딕셔너리 저장공간.
        st.session_state.linked.prepend(st.session_state.data_input_val)
    else:
        st.sidebar.warning("추가할 데이터를 입력")

with col1:
    if st.button("append", on_click=append_data_callback,use_container_width=True): 
        st.write("버튼클릭")

with col2:
    if st.button("delete", on_click=delete_data_callback,use_container_width=True): 
        st.write("버튼클릭")

with col3:
    if st.button("prepend", on_click=prepend_data_callback,use_container_width=True): 
        st.write("버튼클릭")
        


st.markdown("----")
st.subheader("연결리스트 출력")

list_display = st.empty() # empty? -> 공간 먼저 만들고, 나중에 거기다가 값을 넣는다 초기화 개념이라고 생각해도 괜찮아? 근데 이건 왜하는거야? 

result = st.session_state.linked.display()

list_display.markdown(f"{result}") # 아래에 새로 업데이트해도 위치는 변하지 않음.
