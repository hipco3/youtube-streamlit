import tkinter #GUIライブラリ
import matplotlib.pyplot as plt #グラフ描画ライブラリ
from matplotlib.backends.backend_tkagg  import FigureCanvasTkAgg #tkinterとCanvasを紐づけるライブラリ
import numpy as np #数値計算ライブラリ
from functools import partial

#終了処理
def Quit():
    root.quit()
    root.destroy()

#ファイルのプロット処理
def PlotFile(canvas, ax, colors = "gray"):
    editBoxValue = FileEditBox.get()
    if editBoxValue != '':
        FileEditBox.delete(0, tkinter.END)
        ax.cla() #前の描画データの削除
        x,y = np.loadtxt("./" + editBoxValue, delimiter = ',', skiprows = 1, unpack = True) #データ読み込み
        ax.set_aspect('equal') #アスペクト比をそろえる
        ax.plot(x, y) #グラフの描画
        canvas.draw() #Canvasへ描画

if __name__ == "__main__":
    try:
        #tkinterオブジェクト生成
        root = tkinter.Tk()
        root.title("ほげほげ") #GUIタイトル
        
        #graphの設定
        fig,ax1 = plt.subplots()
        fig.gca().set_aspect('equal', adjustable = 'box')

        #Canvas設定
        Canvas = FigureCanvasTkAgg(fig, master = root) #Canvasにfigを追加
        Canvas.get_tk_widget().grid(row = 0, column = 0, rowspan = 10)

        #EditBox
        FileEditBox = tkinter.Entry(width = 15)
        FileEditBox.grid(row = 1, column = 1)

        #UPDATEボタン
        ButtonWidth = 15
        UpdateButton = tkinter.Button(text="UPDATE", width=ButtonWidth, command=partial(PlotFile, Canvas, ax1))#ボタンの生成
        UpdateButton.grid(row = 2, column = 1, columnspan = 1)#描画位置 

        #QUITボタン
        QuitButton = tkinter.Button(text = "QUIT", width = ButtonWidth, command = Quit) #QUITボタンオブジェクト生成
        QuitButton.grid(row = 4, column = 1, columnspan = 1) #Quitボタン位置設定

        #Canvasの描画
        PlotFile(Canvas, ax1)

        #描画を継続
        root.mainloop()

    except:
        import traceback
        traceback.print_exc()

    finally:
        input(">>")