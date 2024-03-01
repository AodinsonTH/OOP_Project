import streamlit as st

# เพิ่มภาพพื้นหลังเว็บไซต์
st.markdown(
    """
    <style>
        body {
            background-image:https://www.pexels.com/th-th/photo/547114/");
            background-size: cover;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# หน้าแรก (Home Page)
def home():
# องค์การนักศึกษามหาวิทยาลัยอุบลราชธานี
    st.markdown(
    """
    <div style="text-align: left;">
        <h1>องค์การนักศึกษามหาวิทยาลัยอุบลราชธานี</h1>
        <p>ข้อมูลทั่วไปเกี่ยวกับองค์การนักศึกษา</p>
    </div>
    """,
    unsafe_allow_html=True
)

# เกี่ยวกับเรา (About Us)
def about():
    st.title('เกี่ยวกับเรา')
    st.write('ข้อมูลเกี่ยวกับองค์การนักศึกษามหาวิทยาลัยอุบลราชธานี')
    st.write('ตัวแทนของนักศึกษาในการดำเนินกิจกรรมของนักศึกษาภายนอกและภายในมหาวิทยาลัยอุบลราชธานี')
    st.write("องค์การนักศึกษา มหาวิทยาลัยอุบลราชธานี คือองค์กรกิจกรรมนักศึกษาในการดำเนินกิจกรรมของนักศึกษา โดยมีองค์กรกิจกรรมต่างๆดังนี้ "
             "\n- องค์กรกิจกรรมส่วนกลางประกอบด้วยสโมสรนักศึกษา มหาวิทยาลัยอุบลราชธานี และสภานักศึกษา มหาวิทยาลัยอุบลราชธานี"
             "\n- องค์กรกิจกรรมส่วนคณะสโมสรนักศึกษาสังกัดคณะ/วิทยาลัย")
    st.page_link("http://www.google.com", label="Google", icon="🌎")

# บริการ (Services)
def services():
    st.title('บริการ')
    st.write('บริการที่องค์การนักศึกษามีให้')

# ข่าวสาร (News)
def news():
    st.title('ข่าวสาร')
    st.write('ข่าวสารและกิจกรรมขององค์การนักศึกษา')
    st.page_link("http://www.google.com", label="Google",)

# ติดต่อเรา (Contact Us)
def contact():
    st.title('ติดต่อเรา')
    st.write('ข้อมูลการติดต่อองค์การนักศึกษา')
    st.page_link("https://www.facebook.com/ubu.su.org", label="FaceBook")

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
