import streamlit as st
import pandas as pd
import numpy as np
import time

# Streamlit 앱의 메인 페이지: 다양한 Streamlit 요소들을 보여주는 데모 페이지
st.title("🎈 Streamlit 요소 데모 페이지")  # 페이지 제목 설정
st.markdown("이 페이지는 Streamlit의 다양한 요소들을 단일 페이지에 모아 보여줍니다. 각 요소에 대한 코드 예시와 설명을 포함합니다.")  # 마크다운 텍스트 표시

# 1. 텍스트 요소들
st.header("1. 텍스트 요소들")  # 헤더 표시

st.subheader("제목과 부제목")  # 서브헤더
st.title("이것은 타이틀입니다")  # 타이틀
st.header("이것은 헤더입니다")  # 헤더
st.subheader("이것은 서브헤더입니다")  # 서브헤더

st.text("이것은 일반 텍스트입니다.")  # 일반 텍스트 표시
st.markdown("**이것은 마크다운 텍스트입니다.** *기울임*, `코드`")  # 마크다운 지원 텍스트
st.latex(r"E = mc^2")  # LaTeX 수식 표시
st.code("print('Hello, World!')", language='python')  # 코드 블록 표시

# 2. 입력 위젯들
st.header("2. 입력 위젯들")  # 헤더

# 버튼
if st.button("클릭하세요"):  # 버튼 위젯
    st.write("버튼이 클릭되었습니다!")  # 버튼 클릭 시 텍스트 표시

# 체크박스
agree = st.checkbox("동의합니다")  # 체크박스 위젯
if agree:
    st.write("동의하셨습니다.")  # 체크박스 선택 시

# 라디오 버튼
option = st.radio("선택하세요:", ["옵션 1", "옵션 2", "옵션 3"])  # 라디오 버튼
st.write(f"선택된 옵션: {option}")  # 선택 결과 표시

# 셀렉트박스
select = st.selectbox("선택하세요:", ["항목 1", "항목 2", "항목 3"])  # 드롭다운 셀렉트박스
st.write(f"선택된 항목: {select}")

# 멀티셀렉트
multi = st.multiselect("여러 개 선택하세요:", ["A", "B", "C", "D"])  # 다중 선택
st.write(f"선택된 항목들: {multi}")

# 슬라이더
slider_val = st.slider("값을 선택하세요:", 0, 100, 50)  # 슬라이더
st.write(f"슬라이더 값: {slider_val}")

# 텍스트 입력
text_input = st.text_input("텍스트를 입력하세요:", "기본값")  # 텍스트 입력 필드
st.write(f"입력된 텍스트: {text_input}")

# 텍스트 영역
text_area = st.text_area("긴 텍스트를 입력하세요:", "여기에 긴 텍스트를 입력하세요.")  # 텍스트 영역
st.write(f"입력된 텍스트 영역: {text_area}")

# 숫자 입력
number = st.number_input("숫자를 입력하세요:", min_value=0, max_value=100, value=10)  # 숫자 입력
st.write(f"입력된 숫자: {number}")

# 날짜 입력
date = st.date_input("날짜를 선택하세요:")  # 날짜 선택
st.write(f"선택된 날짜: {date}")

# 시간 입력
time_input = st.time_input("시간을 선택하세요:")  # 시간 선택
st.write(f"선택된 시간: {time_input}")

# 파일 업로더
uploaded_file = st.file_uploader("파일을 업로드하세요:")  # 파일 업로드
if uploaded_file is not None:
    st.write("파일이 업로드되었습니다:", uploaded_file.name)  # 업로드된 파일 정보 표시

# 3. 출력 요소들
st.header("3. 출력 요소들")  # 헤더

# 데이터프레임
df = pd.DataFrame(np.random.randn(10, 3), columns=['A', 'B', 'C'])  # 샘플 데이터프레임 생성
st.dataframe(df)  # 데이터프레임 표시

# 테이블
st.table(df.head())  # 테이블 형식으로 표시

# JSON
st.json({"key": "value", "list": [1, 2, 3]})  # JSON 데이터 표시

# 메트릭
st.metric("온도", "25°C", "1.2°C")  # 메트릭 표시 (값, 델타)

# 프로그레스 바
progress_bar = st.progress(0)  # 프로그레스 바
for i in range(100):
    time.sleep(0.01)  # 시뮬레이션
    progress_bar.progress(i + 1)  # 진행률 업데이트

# 스피너
with st.spinner("로딩 중..."):  # 스피너 표시
    time.sleep(1)  # 시뮬레이션
st.success("완료되었습니다!")  # 성공 메시지

# 알림 메시지들
st.info("정보 메시지")  # 정보
st.warning("경고 메시지")  # 경고
st.error("에러 메시지")  # 에러
st.exception(RuntimeError("예외 발생"))  # 예외 표시

# 4. 레이아웃 요소들
st.header("4. 레이아웃 요소들")  # 헤더

# 사이드바
with st.sidebar:  # 사이드바에 요소 추가
    st.write("이것은 사이드바입니다.")
    sidebar_input = st.text_input("사이드바 입력:")

# 컬럼
col1, col2, col3 = st.columns(3)  # 3개의 컬럼 생성
with col1:
    st.write("컬럼 1")
with col2:
    st.write("컬럼 2")
with col3:
    st.write("컬럼 3")

# 컨테이너
with st.container():  # 컨테이너 생성
    st.write("컨테이너 내부")
    st.button("컨테이너 버튼")

# 익스팬더
with st.expander("펼쳐보세요"):  # 익스팬더 (접을 수 있는 섹션)
    st.write("익스팬더 내부 내용")

# 탭
tab1, tab2, tab3 = st.tabs(["탭 1", "탭 2", "탭 3"])  # 탭 생성
with tab1:
    st.write("탭 1 내용")
with tab2:
    st.write("탭 2 내용")
with tab3:
    st.write("탭 3 내용")

# 5. 미디어 요소들
st.header("5. 미디어 요소들")  # 헤더

# 이미지 (샘플 이미지 URL 사용)
st.image("https://via.placeholder.com/300", caption="샘플 이미지")  # 이미지 표시

# 오디오 (샘플 오디오 URL 사용, 실제로는 파일 경로나 URL 필요)
# st.audio("path/to/audio.mp3")  # 오디오 파일 재생 (주석 처리, 실제 파일 필요)

# 비디오 (샘플 비디오 URL 사용)
st.video("https://www.w3schools.com/html/mov_bbb.mp4")  # 비디오 재생

# 6. 기타 요소들
st.header("6. 기타 요소들")  # 헤더

# 풍선 애니메이션
if st.button("풍선 터뜨리기"):
    st.balloons()  # 풍선 애니메이션

# 눈 애니메이션
if st.button("눈 내리기"):
    st.snow()  # 눈 애니메이션

# 빈 요소 (플레이스홀더)
placeholder = st.empty()  # 빈 요소 생성
if st.button("텍스트 추가"):
    placeholder.text("빈 요소에 텍스트 추가됨")  # 나중에 내용 추가

# st.write를 사용한 범용 출력
st.write("st.write는 다양한 타입의 데이터를 출력할 수 있습니다.")  # 범용 출력
st.write(df)  # 데이터프레임 출력
st.write({"딕셔너리": "값"})  # 딕셔너리 출력
