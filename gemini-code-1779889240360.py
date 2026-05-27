import streamlit as st
from datetime import datetime

# 페이지 제목 설정
st.set_page_config(page_title="우리반 청소 당번 예측기", page_icon="🧹")
st.title("🧹 우리 반 청소 당번 예측 프로그램")
st.write("날짜를 선택하면 해당 주의 청소 당번 조와 명단을 알려줍니다.")

# 조 데이터
cleaning_groups = {
    0: ["고동화", "권진재", "김동건", "김세빈", "김혜빈", "김나연"],
    1: ["남수민", "도강건", "명서연", "서지우", "서혜성", "성시경"],
    2: ["양민성", "윤재원", "이건우", "이건욱", "이규원", "이세찬"],
    3: ["이유찬", "이준현", "이지원", "이채원", "임승", "임홍명"],
    4: ["정연수", "조민기", "최수연", "한건희", "한유찬", "황서현"]
}

START_DATE = datetime(2026, 5, 25).date()
START_GROUP_INDEX = 1 

# 웹 화면에서 날짜 달력(Input) 만들기
selected_date = st.date_input("조회할 날짜를 선택하세요:", datetime.now().date())

if selected_date:
    if selected_date < START_DATE:
        st.error("⚠️ 기준일(2026-05-25) 이후의 날짜를 선택해 주세요.")
    else:
        # 계산 로직
        days_difference = (selected_date - START_DATE).days
        weeks_passed = days_difference // 7
        group_index = (START_GROUP_INDEX + weeks_passed) % 5
        
        crew = cleaning_groups[group_index]
        
        # 웹 화면에 깔끔한 박스로 결과 출력
        st.success(f"📅 선택한 날짜: {selected_date}")
        st.metric(label="이번 주 청소 당번", value=f"{group_index + 1}조")
        st.write(f"👤 **명단:** {', '.join(crew)}")