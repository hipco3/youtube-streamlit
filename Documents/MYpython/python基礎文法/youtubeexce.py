import pandas as pd
from glob import glob #ファイルのパスを取得する
filepaths= glob('MYpython/*.csv')
print(filepaths)