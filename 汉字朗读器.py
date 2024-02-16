import tkinter as tk
import pyttsx3

def speak_text():
    # 获取文本框中的内容
    text = text_entry.get()

    # 创建一个语音引擎实例
    engine = pyttsx3.init()

    # 设置中文本
    engine.setProperty('voice', 'zh')
    engine.setProperty('rate', 150)  # 设置语速

    # 将文本朗读出来
    engine.say(text)

    # 等待朗读完毕
    engine.runAndWait()


def on_enter(event):
    # 当用户按下 Enter 键时，触发按钮的点击事件
    speak_text()


'''以下为主程序'''

    
# 创建主窗口
root = tk.Tk()
root.title("汉字朗读器（英语好像也可以）@叮当在上")
root.geometry("400x200")  # 设置主窗口大小为宽度400像素，高度200像素
'''
# 创建Canvas组件
canvas = tk.Canvas(root, width=400, height=300)
canvas.pack()

# 加载背景图片
bg_image = tk.PhotoImage(file="1.png")  # 修改为你自己的图片路径
canvas.create_image(0, 0, anchor=tk.NW, image=bg_image)
'''
# 创建标题
title_label = tk.Label(root, text="  请 输 入 汉 字", font=("Arial", 30, "bold"), foreground="green")
title_label.place(x=50, y=10)  # 设置标题的位置
# 通过 font 参数设置了标题的字体为 Arial，字体大小为 14，同时加粗（bold）。
# 通过 foreground 参数设置了标题的字体颜色为蓝色（blue）。

# 按Enter同样触发提示字样
title_label = tk.Label(root, text="按 Enter 键可以触发", font=("Arial", 10, "bold"), foreground="orange")
title_label.place(x=250, y=160)  # 设置提示的位置


# 创建文本框
text_entry = tk.Entry(root, font=("Arial", 14))
text_entry.place(x=70, y=80, width=250, height=40)  # 设置文本框的位置和大小

# 创建按钮
speak_button = tk.Button(root, text="朗读", font=("Arial", 15, "bold"), foreground="black", command=speak_text)
speak_button.place(x=160, y=150, width=80, height=30)  # 设置按钮的位置和大小

# 将 Enter 键与按钮的点击事件绑定
root.bind("<Return>", on_enter)

# 运行主事件循环
root.mainloop()
