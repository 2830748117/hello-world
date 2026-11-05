"""猜数字小游戏 —— 我的第一个 Python 程序。

运行方式：在 Git Bash 里执行  python hello.py
"""

import random
import sys

# 中文 Windows 的终端默认用 GBK，这里统一改成 UTF-8，避免中文变成乱码。
# 如果改用系统自带的 cmd 运行，需要先执行 chcp 65001 切换代码页。
if sys.platform == "win32":
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8")
        except (AttributeError, ValueError):
            pass


def play():
    """开始一局游戏，猜 1~100 之间的整数。"""
    answer = random.randint(1, 100)
    tries = 0
    print("我想好了一个 1~100 之间的整数，你来猜猜看。")
    print("输入数字回车提交，输入 q 退出。\n")

    while True:
        try:
            raw = input("你的猜测：").strip()
        except (EOFError, KeyboardInterrupt):
            # 用户按了 Ctrl+C 或 Ctrl+Z，正常退出而不是抛异常
            print("\n已退出游戏。")
            return

        if raw.lower() == "q":
            print(f"好吧，游戏结束。答案是 {answer}。")
            return

        if not raw.isdigit():
            print("只能输入整数哦，再试一次。\n")
            continue

        guess = int(raw)
        tries += 1

        if guess == answer:
            print(f"猜对了！答案就是 {answer}，你一共用了 {tries} 次。")
            return
        if guess < answer:
            print("小了，往大猜。\n")
        else:
            print("大了，往小猜。\n")


def main():
    print("=" * 30)
    print("  猜数字游戏 v1.0")
    print("=" * 30)
    play()
    print("\n感谢游玩，下次见。")


if __name__ == "__main__":
    main()
