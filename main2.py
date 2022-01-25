import random
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

#タイトルの追加
st.title('streamlit　超入門')

#テキストの追加
st.write('DataFrame')

#データフレームを作成
df = pd.DataFrame({
    '1列目':[1,2,3,4],
    '2列目':[10,20,30,40]
})

#データフレームの表示
#st.write(df)
#st.dataframe(df,width=100, height=100) #大きさを指定できる
"""
動的な表示
"""
st.dataframe(df.style.highlight_max(axis=0)) #動的なテーブルを使いたい時
"""
静的な表示
"""
st.table(df.style.highlight_max(axis=0)) #静的なテーブルを使いたい時

#マークダウンで書ける(マジックコマンド)
"""
# 章
## 節
### 項
```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""
#チャート作成
#データ生成
df1 = pd.DataFrame(
   np.random.rand(20,3),  #20  3の行列
   columns=["a","b","c"]
)

st.title('グラフ表示')

#折れ線グラフの作成
"""
### 折れ線グラフ
"""
st.line_chart(df1)

#棒グラフ
"""
### 棒グラフ
"""
st.bar_chart(df1)

#エリアチャート
"""
### エリアチャート
"""
st.area_chart(df1)

#マップ ※新宿近くの緯度経度にするため乱数を５０で割り、新宿辺りの緯度経度を足す
"""
### map 新宿付近
"""
df3 = pd.DataFrame(
   np.random.rand(100,2)/[50,50] + [35.69,139.7],  #緯度経度を表す乱数を調整する
   columns=["lat","lon"]) 
st.map(df3)

#画像表示
st.title('画像表示')
img = Image.open('sample.jpg')
st.image(img,caption='ひまわり',use_column_width=True) #use_column_width=Trueはサイズ自動調整

#動画表示
st.title('動画表示')
video_file = open('sample.MP4', 'rb')
video_bytes = video_file.read()
st.video(video_bytes)

#インターラクティヴなウィジェット
#st.checkbox関数を使う　if文でチェックの有無を指定する
st.title('インターラクティヴなウィジェット')

if st.checkbox('show image'):
   img = Image.open('sample.jpg')
   st.image(img, caption='ひまわり', use_column_width=True)

#セレクトボックス
option = st.selectbox(
   'あなたの好きな数字を入れてください',
   list(range(1,10))
)
'あなたの好きな数字は.',option,'です。'

#テキスト入力
text = st.text_input('あなたの趣味を教えてください')
'あなたの趣味は:', text

#スライダー
condition = st.slider('あなたの今の調子は?', 0, 100, 50)#最小値、最大値、初期値
'あなたのコンディション:', condition

#サイドバー
st.title('サイドバー')
text1 = st.sidebar.text_input('あなたの趣味を教えてください。')
condition1 = st.sidebar.slider('あなたの今の調子は？',0,100,50)
'あなたの趣味:', text1
'コンディション:', condition1

#2カラム表示
st.title('2カラム表示')
left_column, rigth_column = st.columns(2) #2カラム
button = left_column.button('右カラムに文字を入力')
if button:
   rigth_column.write('ここは右カラム')

#expanderの追加
st.title('expanderの追加')
expander = st.expander('問い合わせ')
expander.write('問い合わせを書く')

#プログレスバー
st.title('プログレスバー')
import time
'スタート!!'

latest_iter = st.empty()
bar = st.progress(0)

for i in range(100):
   latest_iter.text(f'Iter:{i+1}')
   bar.progress(i+1)
   time.sleep(0.1)

'終了!!'



