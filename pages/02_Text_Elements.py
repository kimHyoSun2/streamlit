# Text Elements in Streamlit (1) 
#   Different type of TextElements
#   
# 1) st.markdown
#    st.markdown(body, unsafe_allow_html=False, *, help=None)
#                str    bool                        str
#    ?? write와 markdown과의 차이점은? 

import streamlit as st

st.write('## ■ st.markdown()')
st.markdown("markdown")
st.markdown("*Streamlit* is **really** ***cool***.")
st.markdown('''
    :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
    :gray[pretty] :rainbow[colors].''')
st.markdown("Here's a bouquet &mdash;\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

multi = '''If you end a line with two spaces,
a soft return is used for the next line.

Two (or more) newline characters in a row will result in a hard return.
'''
st.markdown(multi)
st.write(multi)     

# 2) st.title
# st.title(body, anchor=None, *, help=None)
st.write('## ■ st.title()')
st.title('Text Elements title')

# 3) st.header
# st.header(body, anchor=None, *, help=None, divider=False)
st.write('## ■ st.header()')
st.header('Text Elements header')
st.header('Text Elements header', divider='rainbow')   # 옵션이 있는 것 

# 4) st.subheader
# st.subheader(body, anchor=None, *, help=None, divider=False)
#               divider (bool or “blue”, “green”, “orange”, “red”, “violet”, “gray”/"grey", or “rainbow”)
st.write('## ■ st.subheader()')
st.subheader('Text Elements subheader')
st.subheader('Text Elements subheader',divider=True) # default color : blue 
st.subheader('Text Elements subheader',divider=False)
st.subheader('Text Elements subheader',divider='red')

# 5) st.caption
#    st.caption(body, unsafe_allow_html=False, *, help=None)
st.write('## ■ st.caption()')
st.caption('Text Elements caption()')

# 6) st.code
# st.code(body, language="python", line_numbers=False)
st.write('## ■ st.code()')
st.code('''code block. 
int a = 100''', language='python', line_numbers=False)
st.code('''code block. 
int a = 100''', language='python', line_numbers=True)

# 7) st.text
#   st.text(body, *, help=None)
#   Write fixed-width and preformatted text.
#    text() vs write() vs markdown() 
st.write('## ■ st.text()')
st.text('text') 
st.write('text')
st.markdown('text')

# 8) st.latex
#   st.latex(body, *, help=None)
#   지원되는 latex 기능은 URL 참조 :  https://katex.org/docs/supported.html
st.write('## ■ st.latex()')
st.latex('text')
st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')

# 9) st.divider
#    st.write('---')와 동일
st.write('## ■ st.divider()')
st.divider()
st.write('---')






# v1 = 'hello'
# v2 = 3
# st.write('int value = ', v2)
# st.write(v1)

# st.write(3,"*",5,'=',3*5)
