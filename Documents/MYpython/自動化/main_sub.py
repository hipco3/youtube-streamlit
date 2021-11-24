from pandas.io.parsers import PythonParser
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time



st.title('steamlit超入門')
st.title('プログレスバーの表示')
'start!'
latest_iteration=st.empty()
bar=st.progress(0)
for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

st.write('Dataframe')
#left_column, right_column=st.beta_columns(2)
#button=left_column.button('右カラムにもじを表示')
#if button:
#    right_column.write('ここは右カラム')
#

df=pd.DataFrame({
    '1 列目':[1, 2, 3, 4],
    '2 列目':[10, 20, 30, 40]
})

st.dataframe(df.style.highlight_max(axis=0),width=200, height=500)
st.table(df.style.highlight_max(axis=0))

"""
# 章
## 節
### 項項

```python
import streamlit as st 
import numpy as np  
import pandas as pd  
```
"""
#コードの挿入の基本は```(バッククオート3つ)でコードをくくることです。
#` はバッククオートです。クォーテーション '　ではありません。ご注意を。
df=pd.DataFrame(
    np.random.rand(20,3),
    columns=["a","b","c"]

)
st.line_chart(df)
st.area_chart(df)
df=pd.DataFrame(
    np.random.rand(100,2)/[50,50]+[35.69,139.70],
    columns=['lat','lon']

)
st.map(df)

st.write('Display Image')
option=st.selectbox(
    '好きな数字を教えて',
    list(range(1,11))
)
'あなたの好きな数字は',option,'です'
st.write('interactive widgets')
text=st.text_input('あたなの趣味は')
#text=st.sidebar.text_input('あたなの趣味は') #サイドバー表示
'あなたの趣味は',text,'です'
condition=st.slider('あなたの今の調子は？',0,100,50)
'コンディション:',condition
#if st.checkbox('Show image'):
#    img=Image.open('taniku.jpg')
#    st.image(img,caption='多肉植物',use_column_width=True) 

#web アプリの公開から
#5分ぐらい