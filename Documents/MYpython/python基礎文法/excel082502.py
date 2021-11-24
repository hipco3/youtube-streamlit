import win32com.client

file_path=r"C:\Users\polif\Documents\VBA\フィルター検索"
exce=win32com.client.dispath("Excel.application")
wb= exce.workbooks.open()