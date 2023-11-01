import streamlit as st
import tensorflow.keras
import keras
from PIL import Image, ImageOps
import cv2
import numpy as np
def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://cdn.discordapp.com/attachments/736980877837598884/1113290898843906098/BG.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

#add_bg_from_url()
model = tensorflow.keras.models.load_model('model.h5')


st.title("BananInsight")
st.header(":yellow[AI คัดแยก โรคตายพราย และ กล้วยที่ไม่เป็นโรค จากใบกล้วย]")





uploaded_file = st.file_uploader("Choose .jpeg pic ...", type=["jpeg","jpg","PNG"])
if uploaded_file is not None:

  file_bytes = np.asarray(bytearray(uploaded_file.read()))
  image = cv2.imdecode(file_bytes, 1)

  imgori = cv2.cvtColor(image , cv2.COLOR_BGR2RGB)
  img = cv2.resize(imgori ,(224,224)) # size เดียวกับตอนทำโมเดล
  st.image(imgori, width=400) # size สำหรับแสดงผลหน้าเว็บ

  rimg = np.array(img)
  rimg = rimg.astype('float32')
  rimg /= 255
  rimg = np.reshape(rimg ,(1,224,224,3))


  st.write("")


  predict_prop = model.predict(rimg)

  result = np.argmax(predict_prop)
  if result==0:
    labelx = 'กล้วยไม่เป็นโรค'
    st.success(labelx)
  if result==1:
    labelx = 'เป็นโรคตายพราย'
    st.success(labelx)
    st.write('สามารถป้องกันได้โดย')
    st.write('1. เกษตรกรควรหมั่นตรวจและกาจัดวัชพืชในแปลงปลูกอย่างสม่ำเสมอ')
    st.write('2. กรณีพบอาการรุนแรงจนใบเหลืองและเหี่ยวตายทั้งต้น ให้ขุดต้นที่เป็นโรคออกไปเผาทำาลายนอกแปลงปลูก')
    st.write('3. เกษตรกรควรทำแปลงปลูกให้มีการระบายนำ้ที่ดี และควรระมัดระวังการให้น้า โดยไม่ให้น้าไหลผ่านจากต้นที่เป็นโรคไปสู่ ต้นปกติ หากเกษตรกรต้องการปลูกกล้วยในพื้นที่ใหม่ หลีกเลี่ยงการปลูกในพื้นที่ที่เคยมีการระบาดของโรคนี้มาก่อน')
    st.write('4. ไม่นาหน่อพันธุ์จากต้นตอที่เป็นโรคไปปลูก ให้เลือกใช้หน่อกล้วยที่มีคุณภาพดีจากแหล่งปลอดโรค')
    st.write('5. ควรสลับเปลี่ยนไปปลูกพืชชนิดอื่นหมุนเวียน เพื่อตัดวงจรการระบาดของโรค')
    st.write('6. ก่อนปลูกชุบหน่อพันธุ์ด้วยเชื้อราไตรโคเดอร์มา')
  if result==2:
    labelx = 'เป็นโรคใบจุดดำ'
    st.success(labelx)
    st.write('สามารถป้องกันได้โดย')
    st.write('1. กำจัดด้วย เบนเอฟ 20 ซีซี หรือ รัสโซล 10-15 ซีซี หรือ อะซอกซีสโตรบิน 10 ซีซี ต่อน้ำ 20 ลิตร')
    st.write('2. ถ้าเป็นโรคในระยะรุนแรงให้ตัดส่วนที่เป็นโรคออกนำไปเผาทำลายทิ้ง และกำจัดวัชพืชใต้ทรงพุ่มของต้นกล้วย')

if st.button("ข้อมูลเบื้องต้น"):
  st.header("โรคตายพราย")
  st.write("<span style='color:red'>อาการ</span>",unsafe_allow_html=True)
  st.write('1.  จะเห็นทางสีเหลืองอ่อนตามก้านใบของใบล่างหรือใบแก่ก่อน ต่อมาปลายใบหรือขอบใบจะเริ่ม เหลือง และขยายออกไปอย่างรวดเร็วจนเหลืองทั่วใบ')
  st.write('2.  ใบอ่อนจะมีอาการเหลืองไหม้หรือตายนึ่งและบิดเป็นคลื่น ใบกล้วยจะหักพับบริเวณโคนก้าน ใบ ใบยอดจะเหลืองตั้งตรงเขียวอยู่ในระยะแรก')
  st.write('3.  กล้วยจะเหี่ยว ผลเล็กไม่สม่่าเสมอ หรือแก่ก่อนกำหนด พบใบกล้วยหักพับที่โคนใบโดยไม่แสดงอาการใบเหลือง หรือเหลืองเพียงเล็กน้อย')
  st.write('4.  เนื้อในของกาบใบบางส่วนเป็นสี น้่าตาลแดง โดยอาการนี้จะขยายไปยัง กาบ ใบ เเละลามไปที่เครือ ผลกล้วย มีเส้นใยของเชื้อรา')
  st.write("<span style='color:green'>การรักษา</span>",unsafe_allow_html=True)
  st.write('1. เกษตรกรควรหมั่นตรวจและกาจัดวัชพืชในแปลงปลูกอย่างสม่ำเสมอ')
  st.write('2. กรณีพบอาการรุนแรงจนใบเหลืองและเหี่ยวตายทั้งต้น ให้ขุดต้นที่เป็นโรคออกไปเผาทำาลายนอกแปลงปลูก')
  st.write('3. เกษตรกรควรทำแปลงปลูกให้มีการระบายนำ้ที่ดี และควรระมัดระวังการให้น้า โดยไม่ให้น้าไหลผ่านจากต้นที่เป็นโรคไปสู่ ต้นปกติ หากเกษตรกรต้องการปลูกกล้วยในพื้นที่ใหม่ หลีกเลี่ยงการปลูกในพื้นที่ที่เคยมีการระบาดของโรคนี้มาก่อน')
  st.write('4. ไม่นาหน่อพันธุ์จากต้นตอที่เป็นโรคไปปลูก ให้เลือกใช้หน่อกล้วยที่มีคุณภาพดีจากแหล่งปลอดโรค')
  st.write('5. ควรสลับเปลี่ยนไปปลูกพืชชนิดอื่นหมุนเวียน เพื่อตัดวงจรการระบาดของโรค')
  st.write('6. ก่อนปลูกชุบหน่อพันธุ์ด้วยเชื้อราไตรโคเดอร์มา')

  st.header("โรคใบจุดดำ")
  st.write("<span style='color:red'>อาการ</span>",unsafe_allow_html=True)
  st.write("1. เป็นรอยจุดสีน้ำตาลหรือสีดำกระจายไปทั่วใบ")
  st.write("2. มีส่วนที่ไหม้และฉีกขาดง่าย")
  st.write("<span style='color:green'>การรักษา</span>",unsafe_allow_html=True)
  st.write('1. กำจัดด้วย เบนเอฟ 20 ซีซี หรือ รัสโซล 10-15 ซีซี หรือ อะซอกซีสโตรบิน 10 ซีซี ต่อน้ำ 20 ลิตร')
  st.write('2. ถ้าเป็นโรคในระยะรุนแรงให้ตัดส่วนที่เป็นโรคออกนำไปเผาทำลายทิ้ง และกำจัดวัชพืชใต้ทรงพุ่มของต้นกล้วย')
