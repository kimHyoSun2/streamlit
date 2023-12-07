# 페이지
# 앱이 커지면 여러 페이지로 구성하는 것이 유용해집니다. 이를 통해 개발자는 앱을 더 쉽게 관리하고 사용자는 더 쉽게 탐색할 수 있습니다. Streamlit은 다중 페이지 앱을 만드는 마찰 없는 방법을 제공합니다.

# 우리는 다중 페이지 앱을 구축하는 것이 단일 페이지 앱을 구축하는 것만큼 쉽도록 이 기능을 설계했습니다! 다음과 같이 기존 앱에 더 많은 페이지를 추가하면 됩니다.

# 기본 스크립트가 포함된 폴더에 새 pages폴더를 만듭니다. 기본 스크립트의 이름이 이라고 가정해 보겠습니다 main_page.py.
# 앱에 더 많은 페이지를 추가하려면 폴더 .py에 새 파일을 추가하세요 .pages
# streamlit run main_page.py
# 이제 스크립트 main_page.py는 앱의 기본 페이지에 해당합니다. pages그리고 사이드바 페이지 선택기의 폴더 에 있는 다른 스크립트를 볼 수 있습니다 . 
# 예를 들어:
import streamlit as st

st.sidebar.markdown("# SideBar")
st.markdown("# Main page 🎈")

# '''
# main_page.py
# import streamlit as st

# st.markdown("# Main page 🎈")
# st.sidebar.markdown("# Main page 🎈")




# pages/page_2.py
# import streamlit as st

# st.markdown("# Page 2 ❄️")
# st.sidebar.markdown("# Page 2 ❄️")

# '''