import os
import shutil
import subprocess
import telebot
import requests
from PIL import ImageGrab

# 🔥 CONFIGURATION SETUP
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "friday"  # Jo naam aapne create kiya tha

print("🤖 Starting Friday System Core...")

try:
    bot = telebot.TeleBot(BOT_TOKEN)
    bot_user = bot.get_me()
    print(f"✅ Friday System Controls Activated on @{bot_user.username}")
except Exception as e:
    print(f"❌ Connection Failed: {e}")
    exit()

# 1. Start / Help Portal
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    welcome = (
        "⚡ *FRIDAY OLLAMA SYSTEM CORE ONLINE* ⚡\n\n"
        "Oye bhai! Laptop ki shaktiyan aur Ollama AI ab dono active hain.\n"
        "Normal message bhejoge toh AI reply dega, baki commands ye rahe:\n\n"
        "📸 /screenshot - Live screen snap.\n"
        "🔍 /find [filename] - Search files.\n"
        "📊 /status - Disk space status.\n"
        "💻 /cmd [command] - Run cmd command.\n"
        "😴 /sleep - Put laptop to sleep.\n"
        "🛑 /shutdown - Close laptop."
    )
    bot.reply_to(message, welcome, parse_mode="Markdown")

# 2. Live Screenshot Tool
@bot.message_handler(commands=['screenshot'])
def take_screenshot(message):
    bot.reply_to(message, "📸 *Taking live snapshot...*", parse_mode="Markdown")
    try:
        screenshot_path = "friday_snap.png"
        img = ImageGrab.grab()
        img.save(screenshot_path)
        with open(screenshot_path, 'rb') as photo:
            bot.send_photo(message.chat.id, photo, caption="Le bhai screen! 😎")
        os.remove(screenshot_path)
    except Exception as e:
        bot.reply_to(message, f"❌ Screenshot failed: {e}")

# 3. Deep File Hunter Tool
@bot.message_handler(commands=['find'])
def find_file(message):
    filename = message.text[5:].strip()
    if not filename:
        bot.reply_to(message, "Bhai, file name? Example: /find photo.jpg")
        return
    bot.reply_to(message, f"🔍 *Searching for '{filename}'...*", parse_mode="Markdown")
    search_root = os.path.expanduser("~") 
    found_files = []
    for root, dirs, files in os.walk(search_root):
        if filename in files:
            found_files.append(os.path.join(root, filename))
            if len(found_files) >= 3: break
    if not found_files:
        bot.reply_to(message, "❌ File nahi mili!")
        return
    for filepath in found_files:
        try:
            bot.reply_to(message, f"📁 File mili! Sending: `{filepath}`", parse_mode="Markdown")
            with open(filepath, 'rb') as doc: bot.send_document(message.chat.id, doc)
        except:
            bot.reply_to(message, f"⚠️ Size issue ya access locked. Path: `{filepath}`", parse_mode="Markdown")

# 4. Storage Controller
@bot.message_handler(commands=['status'])
def check_status(message):
    total, used, free = shutil.disk_usage("/")
    status_text = f"📊 *STORAGE ANALYTICS:*\n\n💾 Total: {total // (2**30)} GB\n🟢 Free: {free // (2**30)} GB\n🔴 Used: {used // (2**30)} GB"
    bot.reply_to(message, status_text, parse_mode="Markdown")

# 5. Native Command Trigger
@bot.message_handler(commands=['cmd'])
def execute_cmd(message):
    command = message.text[5:].strip()
    if not command: return bot.reply_to(message, "Command missing!")
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=10)
        output = result.stdout if result.stdout else result.stderr
        bot.reply_to(message, f"💻 *Output:*\n```\n{output[:3000]}\n```", parse_mode="Markdown")
    except Exception as e: bot.reply_to(message, f"❌ Error: {str(e)}")

# 6. Windows Sleep Matrix
@bot.message_handler(commands=['sleep'])
def system_sleep(message):
    bot.reply_to(message, "😴 Laptop sone ja raha hai, bye bhai!")
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

# 7. Ultimate Shutdown Trigger
@bot.message_handler(commands=['shutdown'])
def system_shutdown(message):
    bot.reply_to(message, "⚠️ *🚨 Shutting down in 10 seconds!*")
    os.system("shutdown /s /t 10")

# 🤖 8. OLLAMA OFFLINE AI CHAT HANDLER (Normal text messages ke liye)
@bot.message_handler(func=lambda message: True)
def ai_chat(message):
    bot.send_chat_action(message.chat.id, 'typing')
    payload = {
        "model": MODEL_NAME,
        "prompt": message.text,
        "stream": False
    }
    try:
        response = requests.post(OLLAMA_URL, json=payload)
        ai_reply = response.json().get('response', 'Bhai, model ne khali jawab diya.')
    except Exception as e:
        ai_reply = f"⚠️ Ollama Connect Error: {str(e)}"
        
    bot.reply_to(message, ai_reply)

# 🔥 UNLIMITED POLLING - SABSE LAST ME!
print("🚀 Friday Bot Fully Operational! Press Ctrl+C to stop.")
bot.infinity_polling(timeout=20, long_polling_timeout=10)
