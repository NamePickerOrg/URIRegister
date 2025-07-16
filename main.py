import tkinter as tk
from tkinter import filedialog
from tkinter.messagebox import showinfo

root = tk.Tk()
root.title("NamePicker URI协议注册")
root.geometry("400x200")
content = ""

def sel_file():
    global content
    namepicker_path = filedialog.askopenfilename(title="选择NamePicker主程序(main.exe)")
    print(namepicker_path.replace("/",r"\\"))
    content = f"""Windows Registry Editor Version 5.00

[HKEY_CURRENT_USER\Software\Classes\\namepicker]
"URL Protocol"=""
@=""

[HKEY_CURRENT_USER\Software\Classes\\namepicker\Shell]

[HKEY_CURRENT_USER\Software\Classes\\namepicker\Shell\Open]

[HKEY_CURRENT_USER\Software\Classes\\namepicker\Shell\Open\command]
@="{namepicker_path.replace("/",r"\\")} noshortcut"
    """

def gen_file():
    global content
    with open("file.reg","w",encoding="utf-8") as f:
        f.write(content)
    showinfo("完成","将file.reg导入到注册表即可通过namepicker://调起不带浮窗的NamePicker")

step1 = tk.Label(root,text="第一步：选择NamePicker主程序")
step1.grid(row=0,column=0)
select = tk.Button(root,text="点击选择",command=sel_file)
select.grid(row=0,column=1)
step2 = tk.Label(root,text="第二步：生成注册表文件")
step2.grid(row=1,column=0)
gen = tk.Button(root,text="点击生成",command=gen_file)
gen.grid(row=1,column=1)

root.mainloop()