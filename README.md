# 🤖 TeleController: AI-Powered Remote PC Controller Bot

TeleController ek powerful Python-based Telegram Bot hai jo aapko kahin se bhi aapke laptop/PC ko poori tarah control karne ki azaadi deta hai. Isme advanced remote automation ke sath-sath **Ollama** ka use karke ek offline AI Model bhi integrated hai, jisse aap bina internet ke chatbot se baatein kar sakte hain.

---

## 🔥 Key Features

- 📊 **Storage Monitor:** Ek single command se apne PC ke saare drives ka available aur used storage check karein.
- 📸 **Live Screenshot:** Apne laptop ki current screen ka screenshot instantly Telegram chat par receive karein.
- 🔍 **File Searcher:** PC me kisi bhi file ko khojein, bot us file ko dhoondh kar seedhe chat me bhej dega.
- 💻 **CMD Execution:** Telegram chat se hi apne PC par koi bhi Command Prompt (CMD) command run karein.
- ⚡ **Power Control:** Apne laptop ko kahin se bhi remotely **Shutdown** ya **Sleep** mode me daalein.
- 🧠 **Offline AI Chat (Ollama):** Local AI model se chat karein jo bina internet ke aapke laptop par hi chalta hai.

---

## 🛠️ Tech Stack Used

- **Language:** Python 3.x
- **Bot Framework:** python-telegram-bot / Telebot
- **System Utilities:** OS, Subprocess, Shutil, PyAutoGUI (for screenshots)
- **Local AI Engine:** [Ollama](https://ollama.com) (e.g., Llama3 / Mistral)

---

## 🚀 Getting Started

### 1. Prerequisites
- Python 3.x installed on your system.
- A Telegram Bot Token from [@BotFather](https://t.me).
- **Ollama** installed on your PC. Download it from [ollama.com](https://ollama.com).

### 2. Setup Ollama
Make sure your preferred local model is downloaded and running:
```bash
ollama run llama3
```

### 3. Installation

Clone this repository:
```bash
git clone https://github.com/krishnashauryayadav-svg
cd AI_TELBOT
```

Install the required dependencies:
```bash
pip install -r requirements.txt
```

### 4. Configuration
Create a `.env` file in the root directory and add your credentials:
```env
TELEGRAM_BOT_TOKEN=your_bot_token_here
ALLOWED_USER_ID=your_telegram_user_id_here
OLLAMA_MODEL=llama3
```
*(Note: Adding your specific Telegram User ID ensures that only YOU can control your laptop.)*

### 5. Running the Bot
```bash
python main.py
```

---

## 🎮 Available Commands


| Command | Description |
| :--- | :--- |
| `/start` | Bot ko initialize aur welcome message show karta hai. |
| `/storage` | PC ke saare disk drives ka status dikhata hai. |
| `/screenshot` | Laptop ki current screen ka image bhejta hai. |
| `/find <filename>` | PC me file search karke bhejta hai. |
| `/cmd <command>` | Remote machine par CMD command run karta hai. |
| `/shutdown` | Laptop ko turant turn-off kar deta hai. |
| `/sleep` | PC ko low-power sleep mode me daal deta. |
| `prompt` | Ollama offline AI model se chat karne ke liye. |

---

## ⚖️ Disclaimer & Security Note

> [!WARNING]
> **Educational Purposes Only:** This tool grants full administrative access to your local machine via Telegram. The developer is not responsible for any misuse, data loss, or unauthorized access caused by sharing credentials.

- **Never** share your bot token or environment variables.
- Always strict-check the **User ID authentication** inside the code to block unauthorized users.

---

## 📄 License & Copyright

Copyright © 2026 [KRISHNA SHAURYA YADAV]. All rights reserved.

This project is licensed under the **MIT License**. You are free to use, modify, and distribute this software, provided that the original copyright notice and permission notice are included in all copies or substantial portions of the software.

---

## 🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to check the github issues page.

Made with ❤️ by [KRISHNA SHAURYA YADAV](https://github.com/krishnashauryayadav-svg)
