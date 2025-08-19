# streamlit_app.py

import streamlit as st
import random

# --- 페이지 설정 ---
st.set_page_config(
    page_title="우리반 역할 랜덤 배정",
    page_icon="🎲"
)

# --- 앱 제목 및 설명 ---
st.title("🎲 우리반 역할 랜덤 배정")
st.write("버튼을 눌러 우리 반 학생들의 역할을 무작위로 배정해 보세요!")

# --- 역할 목록 정의 ---
# 선생님께서 원하시는 역할로 자유롭게 수정하거나 추가/삭제할 수 있습니다.
roles = [
    "👑 리더", "📢 발표 담당", "✍️ 기록 담당", "⏰ 시간 관리",
    "💻 자료 조사", "🧹 정리 담당", "😊 격려 담당", "🧐 품질 관리"
]

# --- 세션 상태 초기화 ---
# st.session_state는 앱이 재실행되어도 데이터를 유지하는 특별한 공간입니다.
# 'assigned_role' 이라는 변수가 아직 없으면 None (값 없음)으로 만들어 둡니다.
if 'assigned_role' not in st.session_state:
    st.session_state.assigned_role = None

# --- 입력 위젯 ---
# st.text_input으로 학생 이름을 입력받는 칸을 만듭니다.
student_name = st.text_input("이름을 입력하세요 (선택 사항):")

# --- 메인 기능: 버튼 클릭 시 역할 배정 ---
# st.button은 클릭 가능한 버튼을 만듭니다. 버튼이 클릭되면 True를 반환합니다.
if st.button("🍀 역할 뽑기!"):
    # random.choice() 함수를 이용해 roles 리스트에서 무작위로 하나를 선택합니다.
    chosen_role = random.choice(roles)
    # 선택된 역할을 세션 상태에 저장합니다.
    st.session_state.assigned_role = chosen_role

# --- 결과 출력 ---
# 세션 상태에 배정된 역할이 있을 경우에만 결과를 화면에 보여줍니다.
if st.session_state.assigned_role:
    st.markdown("---") # 구분선 추가
    # st.success()를 사용해 결과를 강조해서 보여줍니다.
    if student_name:
        st.success(f"🎉 **{student_name}** 학생의 역할은 **'{st.session_state.assigned_role}'** 입니다!")
    else:
        st.success(f"🎉 뽑힌 역할은 **'{st.session_state.assigned_role}'** 입니다!")

# --- 앱 하단 설명 (선택 사항) ---
st.info("새로고침(F5)하면 모든 내용이 초기화됩니다.")