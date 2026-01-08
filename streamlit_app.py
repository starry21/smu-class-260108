import streamlit as st

# 세션 상태 초기화 (앱 재시작 시 유지)
if 'num1' not in st.session_state:
    st.session_state.num1 = 1
if 'num2' not in st.session_state:
    st.session_state.num2 = 1
if 'shape' not in st.session_state:
    st.session_state.shape = '사과'
if 'visualized' not in st.session_state:
    st.session_state.visualized = False
if 'user_answer' not in st.session_state:
    st.session_state.user_answer = 0
if 'checked' not in st.session_state:
    st.session_state.checked = False

# 앱 제목
st.title("🍎 초등학교 곱셈 학습 앱")

# 설명
st.markdown("두 개의 숫자를 입력하고, 선택한 그림으로 곱셈 결과를 시각화해보세요!")

# 숫자 입력 섹션
st.header("1. 숫자 입력")
col1, col2 = st.columns(2)
with col1:
    num1 = st.number_input("첫 번째 숫자 (1-10):", min_value=1, max_value=10, value=st.session_state.num1, key='num1_input')
with col2:
    num2 = st.number_input("두 번째 숫자 (1-10):", min_value=1, max_value=10, value=st.session_state.num2, key='num2_input')

# 그림 선택
shape_options = {'사과': '🍎', '별': '⭐', '동그라미': '🔵', '하트': '❤️', '네모': '🔲'}
selected_shape = st.selectbox("시각화할 그림 선택:", list(shape_options.keys()), index=list(shape_options.keys()).index(st.session_state.shape), key='shape_select')

# 시각화 버튼
if st.button("시각화하기"):
    st.session_state.num1 = num1
    st.session_state.num2 = num2
    st.session_state.shape = selected_shape
    st.session_state.visualized = True
    st.session_state.checked = False  # 시각화 시 체크 초기화

# 시각화 결과 표시
if st.session_state.visualized:
    st.header("2. 시각화 결과")
    total = st.session_state.num1 * st.session_state.num2
    shape_emoji = shape_options[st.session_state.shape]
    st.write(f"{st.session_state.num1} × {st.session_state.num2} = ?")

    # 그림 반복 표시 (한 줄에 10개씩)
    for i in range(0, total, 10):
        st.write(shape_emoji * min(10, total - i))

    st.write(f"총 {total}개의 {st.session_state.shape}가 있습니다.")

    # 결과 입력 섹션
    st.header("3. 계산 결과 입력")
    user_answer = st.number_input("계산 결과를 입력하세요:", min_value=0, value=st.session_state.user_answer, key='answer_input')

    # 확인 버튼
    if st.button("정답 확인"):
        st.session_state.user_answer = user_answer
        st.session_state.checked = True

    # 정답 여부 표시
    if st.session_state.checked:
        if st.session_state.user_answer == total:
            st.success("정답입니다! 🎉")
        else:
            st.error(f"틀렸습니다. 정답은 {total}입니다. 😢")

# 초기화 버튼
if st.button("초기화"):
    st.session_state.num1 = 1
    st.session_state.num2 = 1
    st.session_state.shape = '사과'
    st.session_state.visualized = False
    st.session_state.user_answer = 0
    st.session_state.checked = False
    st.rerun()  # 페이지 새로고침
