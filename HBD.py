import streamlit as st
# กำหนดสีข้อความเป็นสีชมพู
st.markdown(
    f"""
    <style>
    .st-ct {{

        color: purple;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# กำหนดสีพื้นหลังเป็นสีชมพู
st.markdown(
    """
    <style>
    body {
        background-color: pink;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# เพิ่มเนื้อหาอื่น ๆ ที่คุณต้องการในเว็บ Streamlit ต่อจากนี้
st.header(":red[Happy Birthday to Thiyaporn]:heart: " ) 
st.write("มีความสุขมากๆ ยิ่มเยอะๆแบบนี้ตลอดไปนะครับ :star2: :heart:")
st.image('https://i.imgur.com/FKVPifE.jpeg')
st.write("พี่รู้ไหม ว่ารอยยิ้มของพี่ ทำให้ผมมีความสุขมากแค่ไหน :star2: :heart:")
st.image ('https://i.imgur.com/2gNcBRs.jpeg')
st.write("ขอให้มีแต่เรื่องดีๆเข้ามาตลอดทั้งปี ขอให้ทุกวันเป็นวันที่ดีนะครับ  :heart_eyes: :heart:")
st.image ('https://i.imgur.com/gSOgi2v.jpeg')
st.write("ขอบคุณที่เกิดมาเพื่อมอบรอยยิ้มที่งดงามนี้ให้ผม 	:blush: :star2: :heart:")
st.image ('https://i.imgur.com/sWbfm9F.jpeg')
st.write("สุดท้ายนี้ ไม่มีอะไรจะพูดเพราะพูดไม่ค่อยเก่ง 	:blush:  :heart:")
st.write("เลยตัดวิดีโอนี้ให้พี่ อาจจะไม่ได้ดีมากนัก เพราะไม่มีเวลาได้ถ่ายเลย :blush: :star2: :heart:")
st.write("แต่ก็อยากทำสุดๆ หวังว่าพี่จะชอบนะครับ  :joy: ")
st.video('https://youtu.be/fSmMkBm9l98?si=w-rAq5gEAC0UECaj')
