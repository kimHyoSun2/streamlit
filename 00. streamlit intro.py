# 01. streamlit 설치 및 테스트

# 01-1. 설치        pip install streamlit 
#       설치확인    pip list
#       설치제거    pip uninstall streamlit 

# 정상적으로 설치되었는지 확인하기 : streamlit hello

# 01-2 표출 테스트 하기 
#       다음과 같이 코드 입력 후  실행 
#       실행하는 방법 : streamlit run 파일명 [-- script args] 
#                      예) streamlit run 01_test.py
#       실행에 문제가 있을 때 : python -m streamlit run 파일명 


# 라이브러리 살펴보기 
# https://docs.streamlit.io/library/get-started



# 1. 개발방법 
#     저장하면 Streamlit은 변경을 감지하고 다시 실행할 것인지 질문함
#     소스 코드 변경시마다 앱을 자동 업데이트 하려면 오른족 상단의 '항상 다시실행'을 선택
#     개발하는 동안은 코드와 앱화면을 나란히 배치하는 것을 권장함


# 2. 데이터의 흐름
#     화면에서 업데이트해야할 때마다 Streamlit은 전체 python 코드를  위에서 아래로 다시 실행함
#     - 앱의 소스코드 수정할 때마다  
#     - 사용자가 앱의 위젯과 상호작용할 때마다
#         예) 버튼 클릭, 슬라이더 수치값 변경, 입력상자에 텍스트 입력 

# 3. Display & style data
#     테이블, 배경, 데이터 프레임을 표시가능 
#     텍스트 ~ 표까지 모두 표현가능
    


# 4. Streamlit 기본 테마 변경 가능 
# Streamlit은 기본적으로 Light 및 Dark 테마를 지원
# Streamlit은 먼저 앱을 보는 사용자가 운영 체제 및 브라우저에서 설정한 밝은 모드 또는 어두운 모드 기본 설정을 가지고 있는지 확인합니다. 그렇다면 해당 기본 설정이 사용됩니다. 그렇지 않으면 Light 테마가 기본적으로 적용됩니다.
# "⋮" → "설정"에서 활성 테마를 변경가능 






