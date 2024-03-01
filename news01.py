import streamlit as st

st.header(":red[องค์การนักศึกษา]", divider='blue')

# การนำทางระหว่างหน้า (Navigation)
nav = st.sidebar.radio('ตัวเลือก', ['หน้าแรก', 'ข่าวสาร', 'บริการ', 'เกี่ยวกับเรา', 'ติดต่อเรา'])

if nav == 'หน้าแรก':
    home()
elif nav == 'บริการ':
    services()
elif nav == 'ข่าวสาร':
    news()
elif nav == 'เกี่ยวกับเรา':
    about()
elif nav == 'ติดต่อเรา':
    contact()
st.sidebar.markdown(
    """
    <style>
        div.stRadio > div:first-child {
            width: 30px;
        }
    </style>
    """,
    unsafe_allow_html=True
)
