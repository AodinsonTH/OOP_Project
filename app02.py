import streamlit as st
st.title (':red[สะดวกปาก.....?]')
st.header ('บริการจัดส่งอาหารถึงที่')
total_price = []

    
bg = """
<style>
[data-testid="stAppViewContainer"]{
background-image: url("https://img.freepik.com/free-photo/abstract-blur-table-set-dinning-table_1339-6442.jpg?w=1380&t=st=1710168225~exp=1710168825~hmac=b2c9d4b4c729fdf95943e364eaa013fbf8a0c145e40b739741778e84f7397e9e");
background-size: cover;
}

}
</style>
"""
st.markdown(bg, unsafe_allow_html=True)         #กำหนด BG 

def _Food():
    st.title("เมนูอาหาร")

    # สร้างเมนูอาหาร
    menu_food = {
        "ไม่รับอาหาร": 0,
        "ข้าวผัด": 50,
        "ส้มตำ": 40,
        "ผัดไทย": 45,
        "ต้มยำกุ้ง": 60,
        "ข้าวมันไก่": 55,
        "กะเพราหมูสับ": 55,
        "กะเพราหมูกรอบ": 60,
    }
    st.image('https://1.bp.blogspot.com/-GOxfBj1mPnE/XEU8y0D8SSI/AAAAAAAAABY/zPV4rfdPT6YzB5XrBEWe3ctgOa2QipxSACLcBGAs/s1600/51.jpg')
    st.image('https://th.bing.com/th/id/OIP.KjZ8g4Ac0Q9WuoeYbKYsOQHaE8?rs=1&pid=ImgDetMain')
    st.image('https://th.bing.com/th/id/OIP.YV6bh7Ch55mv_VaWwT0PwQHaE8?rs=1&pid=ImgDetMain')
    st.image('https://almocooking.com/wp-content/uploads/2019/03/a0000460_parts_5800718482520.jpg')
    st.image('https://th.bing.com/th/id/R.721010d77b1919648e5cb926662b0705?rik=YDbQdP3DbB%2boFQ&pid=ImgRaw&r=0')
    st.image('https://fit-d.com/uploads/food/ce53316bba21f1adcd2419d81d22e216.jpg')
    st.image('https://th.bing.com/th/id/OIP.v4mfLHQGRMfLaylH8B92hgHaEK?rs=1&pid=ImgDetMain')
    # เลือกจำนวนแต่ละเมนู
    selected_item = st.selectbox("เลือกเมนู", options=list(menu_food.keys()))
    if selected_item:
        st.write(f"คุณเลือก {selected_item}")
        st.write(f"ราคา: {menu_food[selected_item]} บาท")
        total_price.append(int(menu_food[selected_item]))
if __name__ == "__main__":
    _Food()

# เพิ่มเติมอาหาร
st.write('เพิ่มตัวเลือกอย่างละ + 10 บาท')
if st.checkbox('เพิ่มข้าว') :
    total_price.append(10)
if st.checkbox('เพิ่มไข่ดาว') :
    total_price.append(10)
if st.checkbox('เพิ่มไข่ต้ม') :
    total_price.append(10)
if st.checkbox('เพิ่มไข่ลวกยางมะตูม') :
    total_price.append(10)
if st.text_input('เขียนรายละเอียด') :
    total_price.append(10)
def _Drink():
    st.title("เมนูเครื่องดื่ม")

    # เมนูเครื่องดื่ม
    menu_drink = {
        "ไม่รับเครื่องดื่ม":0,
        "กาแฟ": 50,
        "ชาไทย": 40,
        "ชาเขียว": 45,
        "น้ำอัดลม": 60
    }
    st.image('https://img.freepik.com/vrije-photo/kopje-koffie-en-specerijen_146936-107.jpg?size=626&ext=jpg')
    st.image('https://sp-ao.shortpixel.ai/client/to_auto,q_lossy,ret_img,w_2560,h_1708/https://www.thaibicusa.com/wp-content/uploads/2021/04/iced-thai-milk-tea-cup-1-scaled.jpg')
    st.image('https://th.bing.com/th/id/OIP.laDHWY0gZqFMxoyaLQvBEQHaHb?rs=1&pid=ImgDetMain')
    st.image('https://th.bing.com/th/id/OIP.06LTVRoiTFHDF8mFOapd-QAAAA?w=283&h=424&rs=1&pid=ImgDetMain')

    # เลือกจำนวนแต่ละเมนู
    selected_item = st.selectbox("เลือกเมนู", options=list(menu_drink.keys()))

    if selected_item:
        st.write(f"คุณเลือก: {selected_item}")
        st.write(f"ราคา: {menu_drink[selected_item]} บาท")
        total_price.append(menu_drink[selected_item])

if __name__ == "__main__":
    _Drink()


# st.write("ราคาอาหาร",food_price)
# st.write ('ราคารวม', total_price)
if st.button ('ยืนยันการสั่งอาหาร'):
    st.write('ขอบคุณที่ใช้บริการค่ะ')
    st.write('เราจะจัดส่งอาหารของท่านให้เร็วที่สุด')
    st.write(f'ราคารวม: {sum(total_price)}') 