import streamlit as st
import random

# 페이지 설정
st.set_page_config(page_title="암기박스", layout="centered")

st.title("📦 무작위 암기 박스")

# 암기할 리스트 (원하는 대로 수정 가능)
if 'origin_list' not in st.session_state:
    st.session_state.origin_list = ['A', 'b', 'c', 'd', 'e', 'f', 'g']

# 섞인 리스트와 현재 인덱스 관리
if 'shuffled_list' not in st.session_state:
    st.session_state.shuffled_list = []
    st.session_state.idx = 0

# 시작하기/다시 섞기 버튼
if st.button("목록 새로 섞기"):
    st.session_state.shuffled_list = random.sample(st.session_state.origin_list, len(st.session_state.origin_list))
    st.session_state.idx = 0
    st.rerun()

# 게임 로직
if st.session_state.shuffled_list:
    current_idx = st.session_state.idx
    total = len(st.session_state.shuffled_list)
    
    if current_idx < total:
        st.write(f"### {current_idx + 1}번째 항목 (총 {total}개)")
        
        if st.button("정답 확인"):
            st.info(f"정답은: **{st.session_state.shuffled_list[current_idx]}** 입니다!")
            
        if st.button("다음 문제 ->"):
            st.session_state.idx += 1
            st.rerun()
    else:
        st.success("모든 항목을 다 확인했습니다! 다시 하려면 위 버튼을 눌러주세요.")
else:
    st.write("위의 버튼을 눌러 암기를 시작하세요!")
