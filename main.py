import os
import shutil
import subprocess
import telebot
from PIL import ImageGrab  # Screen capture karne ke liye

# 🔥 SECURE CONFIGURATION SETUP
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

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
        "⚡ *FRIDAY ULTIMATE SYSTEM CORE ONLINE* ⚡\n\n"
        "Oye bhai! Laptop ki aseemit shaktiyan ab aapke haath mein hain. Ye rahe direct execution commands:\n\n"
        "📸 /screenshot - Laptop ki live screen dekhne ke liye.\n"
        "🔍 /find [filename] - Poore laptop mein koi bhi file dhoondh kar mangwane ke liye.\n"
        "📊 /status - Storage logs aur health check karne ke liye.\n"
        "💻 /cmd [command] - Direct cmd execute karne ke liye.\n"
        "😴 /sleep - Laptop ko turant sleep mode mein daalne ke liye.\n"
        "🛑 /shutdown - Laptop ko band karne ke liye."
    )
    bot.reply_to(message, welcome, parse_mode="Markdown")

# 2. Live Screenshot Tool
@bot.message_handler(commands=['screenshot'])
def take_screenshot(message):
    bot.reply_to(message, "📸 *Taking live snapshot of your desktop...*", parse_mode="Markdown")
    try:
        # Screen capture karke local save karna
        screenshot_path = "friday_snap.png"
        img = ImageGrab.grab()
        img.save(screenshot_path)
        
        # Phone par send karna
        with open(screenshot_path, 'rb') as photo:
            bot.send_photo(message.chat.id, photo, caption="Le bhai, tere laptop ki live screen! 😎")
        
        # Cleanup
        os.remove(screenshot_path)
    except Exception as e:
        bot.reply_to(message, f"❌ Screenshot failed: {e}")

# 3. Deep File Hunter Tool (Searches all directories)
@bot.message_handler(commands=['find'])
def find_file(message):
    filename = message.text[5:].strip()
    if not filename:
        bot.reply_to(message, "Bhai, file ka naam toh batao! Example: /find resume.pdf")
        return
        
    bot.reply_to(message, f"🔍 *Searching for '{filename}' inside C:/Users folder...*", parse_mode="Markdown")
    
    # Dell Vostro user directory setup
    search_root = os.path.expanduser("~") 
    found_files = []
    
    # Walking through system tree structure locally
    for root, dirs, files in os.walk(search_root):
        if filename in files:
            found_files.append(os.path.join(root, filename))
            if len(found_files) >= 3: # Max 3 results to avoid flooding
                break
                
    if not found_files:
        bot.reply_to(message, "❌ Bhai, pure system mein aisi koi file nahi mili!")
        return
        
    for filepath in found_files:
        try:
            bot.reply_to(message, f"📁 File mili! Sending: `{filepath}`", parse_mode="Markdown")
            with open(filepath, 'rb') as doc:
                bot.send_document(message.chat.id, doc)
        except Exception as e:
            bot.reply_to(message, f"⚠️ File size badi hai ya access locked hai. Path: `{filepath}`", parse_mode="Markdown")

# 4. Storage Controller
@bot.message_handler(commands=['status'])
def check_status(message):
    total, used, free = shutil.disk_usage("/")
    status_text = (
        "📊 *LOCAL DRIVES ANALYSIS:*\n\n"
        f"💾 Total: {total // (2**30)} GB\n"
        f"🟢 Free: {free // (2**30)} GB\n"
        f"🔴 Used: {used // (2**30)} GB"
    )
    bot.reply_to(message, status_text, parse_mode="Markdown")

# 5. Native Command Trigger
@bot.message_handler(commands=['cmd'])
def execute_cmd(message):
    command = message.text[5:].strip()
    if not command:
        bot.reply_to(message, "Command missing! Example: /cmd dir")
        return
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=10)
        output = result.stdout if result.stdout else result.stderr
        bot.reply_to(message, f"💻 *Output:*\n```\n{output[:3000]}\n```", parse_mode="Markdown")
    except Exception as e:
        bot.reply_to(message, f"❌ Error: {str(e)}")

# 6. Windows Sleep Matrix
@bot.message_handler(commands=['sleep'])
def system_sleep(message):
    bot.reply_to(message, "😴 Laptop ko sulane ja raha hoon, bye bhai!")
    # Windows system command to trigger sleep state native utility
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

# 7. Ultimate Shutdown Trigger
@bot.message_handler(commands=['shutdown'])
def system_shutdown(message):
    bot.reply_to(message, "⚠️ *🚨 CRITICAL ORDER RECEIVED: Shutting down the laptop in 10 seconds!*", parse_mode="Markdown")
    os.system("shutdown /s /t 10")

bot.infinity_polling()
