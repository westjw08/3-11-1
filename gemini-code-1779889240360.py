import streamlit as st
from datetime import datetime, date

# 페이지 제목 설정
st.set_page_config(page_title="우리반 청소 당번 예측기", page_icon="🧹")
st.title("🧹 우리 반 청소 당번 예측 프로그램")
st.write("날짜를 선택하면 해당 주의 청소 당번 조와 시험 일정을 알려줍니다.")

# 1. 반 학생 명단 등록 (1조 ~ 5조)
cleaning_groups = {
    0: ["고동화", "권진재", "김동건", "김세빈", "김혜빈", "김나연"],  # 1조
    1: ["남수민", "도강건", "명서연", "서지우", "서혜성", "성시경"],  # 2조
    2: ["양민성", "윤재원", "이건우", "이건욱", "이규원", "이세찬"],  # 3조
    3: ["이유찬", "이준현", "이지원", "이채원", "임승", "임홍명"],  # 4조
    4: ["정연수", "조민기", "최수연", "한건희", "한유찬", "황서현"]   # 5조
}

# 2. 정기시험 시간표 데이터 (6/25 ~ 7/1)
exam_schedule = {
    date(2026, 6, 25): ["화법과 작문", "생활과 윤리", "경제"],
    date(2026, 6, 26): ["미적분", "생활과 과학", "지구과학2"],
    date(2026, 6, 29): ["영어", "정보", "물리학2"],
    date(2026, 6, 30): ["인공지능 기초", "세계지리", "생명과학2"],
    date(2026, 7, 1): ["기하", "화학2", "정치와 법"]
}

# 3. 기준 날짜 설정 (2026년 5월 25일 월요일 = 2조 시작일)
START_DATE = date(2026, 5, 25)
START_GROUP_INDEX = 1 

# 웹 화면에서 날짜 달력(Input) 만들기
selected_date = st.date_input("조회할 날짜를 선택하세요:", datetime.now().date())

if selected_date:
    if selected_date < START_DATE:
        st.error("⚠️ 기준일(2026-05-25) 이후의 날짜를 선택해 주세요.")
    
    # [특정 예외] 6/25 ~ 7/1 정기시험 기간 예외 처리
    elif date(2026, 6, 25) <= selected_date <= date(2026, 7, 1):
        st.warning("📝 이 날은 정기시험 기간이므로 청소가 없습니다!")
        
        # 주말(토, 일)인지 확인
        if selected_date.weekday() in [5, 6]:
            st.info("주말에는 시험이 없습니다. 남은 시험 공부 화이팅! 📖")
        # 시험 당일일 경우 과목 출력
        elif selected_date in exam_schedule:
            subjects = exam_schedule[selected_date]
            st.markdown(f"### 🗓️ **{selected_date.strftime('%m/%d')} 시험 과목**")
            for sub in subjects:
                st.write(f"- ✏️ {sub}")
                
    else:
        # 두 날짜 사이의 일 수 차이 계산
        days_difference = (selected_date - START_DATE).days
        
        # 지난 주(Week) 수 계산 (7일로 나눈 몫)
        weeks_passed = days_difference // 7
        
        # 조 인덱스 계산 (5주 무한 반복)
        group_index = (START_GROUP_INDEX + weeks_passed) % 5
        crew = cleaning_groups[group_index]
        
        # 웹 화면에 결과 출력
        st.success(f"📅 선택한 날짜: {selected_date}")
        st.metric(label="이번 주 청소 당번", value=f"{group_index + 1}조")
        st.write(f"👤 **명단:** {', '.join(crew)}")
