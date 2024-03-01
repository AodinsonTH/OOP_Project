import streamlit as st
import pandas as pd

# ข้อมูลรถยนต์
car_data = {
    'Toyota': {'Model': ['Yaris', 'Corolla', 'Camry', 'Fortuner', 'Alphard'],
               'Price': [559000, 979000, 1599000, 1618000, 4499000],
               'Image': ['https://example.com/yaris.jpg',
                         'https://example.com/corolla.jpg',
                         'https://example.com/camry.jpg',
                         'https://example.com/fortuner.jpg',
                         'https://example.com/alphard.jpg']},
    'Honda': {'Model': ['CITY', 'Civic', 'Accord', 'CR-V', 'HR-V'],
              'Price': [799000, 3990000, 1799000, 1729000, 1179000],
              'Image': ['https://example.com/city.jpg',
                        'https://example.com/civic.jpg',
                        'https://example.com/accord.jpg',
                        'https://example.com/crv.jpg',
                        'https://example.com/hrv.jpg']},
    'Nissan': {'Model': ['Leaf', 'Terra', 'Almera', 'GT-R', 'Note'],
               'Price': [1590000, 1555000, 699000, 12200000, 595000],
               'Image': ['https://example.com/leaf.jpg',
                         'https://example.com/terra.jpg',
                         'https://example.com/almera.jpg',
                         'https://example.com/gtr.jpg',
                         'https://example.com/note.jpg']},
    'Tesla': {'Model': ['Model S', 'Model 3', 'Model X', 'Model Y'],
              'Price': [4900000, 1599000, 3900000, 2000000],
              'Image': ['https://example.com/models.jpg',
                        'https://example.com/model3.jpg',
                        'https://example.com/modelx.jpg',
                        'https://example.com/modely.jpg']}
}

# หน้าแรกของเว็บไซต์
st.title('Sornsiri Motor - เว็บขายรถยนต์')

# เลือกยี่ห้อรถยนต์
car_brand = st.sidebar.selectbox('เลือกยี่ห้อรถยนต์', list(car_data.keys()))

# แสดงรายการรถยนต์ของยี่ห้อที่เลือก
st.subheader(f'รถยนต์ยี่ห้อ {car_brand}')
car_df = pd.DataFrame(car_data[car_brand])
st.write(car_df)
