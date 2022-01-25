import streamlit as st
import time
#タイトルの追加
st.title('streamlit　超入門')

#プログレスバー
st.title('プログレスバー')
'スタート!!'

latest_iter = st.empty()
bar = st.progress(0)

for i in range(100):
   latest_iter.text(f'Iter:{i+1}')
   bar.progress(i+1)
   time.sleep(0.1)

'終了!!'



