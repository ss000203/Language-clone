import tkinter as tk
from tkinter import scrolledtext
import subprocess
import threading
import os
import ctypes
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(CURRENT_DIR)

class WeCloneLauncher:
    def __init__(self, root):
        self.root = root
        self.root.title("WeClone")
        self.root.geometry("680x500")
        self.root.configure(bg="#f0f2f5")  # 极简浅灰背景

        # 1. 顶部标题
        title_label = tk.Label(root, text="克隆AI", font=("微软雅黑", 18, "bold"), bg="#f0f2f5",
                               fg="#333333")
        title_label.pack(pady=15)

        # 2. 按钮操作区
        btn_frame = tk.Frame(root, bg="#f0f2f5")
        btn_frame.pack(pady=5)

        # 检查环境按钮
        self.btn_env = tk.Button(btn_frame, text="⚙️ 1. 检查虚拟环境", font=("微软雅黑", 11), bg="#ffffff",
                                 relief="ridge", command=self.check_env)
        self.btn_env.grid(row=0, column=0, padx=10)

        # 启动演示按钮 (微信绿)
        self.btn_start = tk.Button(btn_frame, text="🚀 2. 启动推理演示", font=("微软雅黑", 11, "bold"), bg="#07c160",
                                   fg="white", relief="flat", command=self.start_demo)
        self.btn_start.grid(row=0, column=1, padx=10)

        # 停止运行按钮 (警告红)
        self.btn_stop = tk.Button(btn_frame, text="🛑 停止运行", font=("微软雅黑", 11), bg="#ff4d4f", fg="white",
                                  relief="flat", command=self.stop_demo, state=tk.DISABLED)
        self.btn_stop.grid(row=0, column=2, padx=10)

        # 3. 日志显示区 (模拟黑客终端)
        log_label = tk.Label(root, text="运行日志 (实时输出):", font=("微软雅黑", 10), bg="#f0f2f5", fg="#666666")
        log_label.pack(anchor="w", padx=20, pady=(15, 0))

        self.log_box = scrolledtext.ScrolledText(root, width=80, height=16, font=("Consolas", 10), bg="#1e1e1e",
                                                 fg="#00ff00")
        self.log_box.pack(padx=20, pady=5, fill=tk.BOTH, expand=True)

        self.process = None

        # 启动时自动检查一下环境
        self.check_env()

    def log(self, message):
        """往黑框框里写日志"""
        self.log_box.insert(tk.END, message + "\n")
        self.log_box.see(tk.END)  # 自动滚动到最底端

    def check_env(self):
        self.log("=====================================")
        self.log("正在检查运行环境...")
        if os.path.exists(".venv"):
            self.log("[OK] 虚拟环境 (.venv) 状态正常！")
            self.log("提示：图形界面无需手动输入 activate，点击【启动】即可自动调用。")
        else:
            self.log("[ERROR] 未找到虚拟环境！请确认路径是否正确。")
        self.log("=====================================")

    def read_output(self, pipe):
        """后台线程：不断读取程序的输出并显示到界面上"""
        with pipe:
            for line in iter(pipe.readline, b''):
                try:
                    text = line.decode('utf-8').strip()
                except:
                    try:
                        text = line.decode('gbk').strip()
                    except:
                        text = str(line)
                if text:
                    self.log(text)

    def start_demo(self):
        if self.process is not None and self.process.poll() is None:
            self.log("⚠️ 程序已经在运行中了，请先停止！")
            return

        self.log("🚀 正在下达启动指令...")
        self.log("正在加载 7B 大模型，您的显存为 4GB，预计需要 15-30 秒，请耐心等待...")
        self.log("当看到 'Running on local URL' 时即可点击链接。")
        self.log("-------------------------------------")

        self.btn_start.config(state=tk.DISABLED, bg="#cccccc")
        self.btn_stop.config(state=tk.NORMAL)

        # 使用 uv run 自动在虚拟环境中执行，隐藏弹出的黑框
        # 直接调用虚拟环境里的程序，彻底绕过 uv 的网络更新检查！
        exe_path = os.path.join(CURRENT_DIR, ".venv", "Scripts", "weclone-cli.exe")
        cmd = [exe_path, "webchat-demo"]
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

        self.process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            startupinfo=startupinfo
        )

        # 开启新线程读取日志，这样主界面就不会卡死！
        threading.Thread(target=self.read_output, args=(self.process.stdout,), daemon=True).start()

    def stop_demo(self):
        if self.process:
            self.log("🛑 正在强制切断电源，关闭服务...")
            startupinfo = subprocess.STARTUPINFO()
            startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            # Windows 下强制杀掉进程树（释放显存）
            subprocess.call(['taskkill', '/F', '/T', '/PID', str(self.process.pid)], startupinfo=startupinfo)
            self.process = None
            self.log("[OK] 服务已完全停止，显存已释放。")

        self.btn_start.config(state=tk.NORMAL, bg="#07c160")
        self.btn_stop.config(state=tk.DISABLED)


if __name__ == "__main__":
    # 让 Windows 高分屏下字体不模糊
    try:
        ctypes.windll.shcore.SetProcessDpiAwareness(1)
    except:
        pass

    root = tk.Tk()
    app = WeCloneLauncher(root)
    root.mainloop()