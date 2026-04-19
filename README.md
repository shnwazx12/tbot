# MediaToTelegraphLink — TeLe TiPs

> Powerful Telegram bot to generate Telegraph links for your media files.
> Works in **private chats** and **group chats**.

---

## ✨ Features

- Upload media → get an instant Telegra.ph link
- Private & group chat support (`/tl` command)
- MongoDB-powered user stats tracking
- Render-ready deployment with health-check endpoint
- Modular codebase (easy to extend)

---

## 🚀 Deploy on Render

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)

1. Fork or push this repo to GitHub.
2. Go to [render.com](https://render.com) → **New → Web Service**.
3. Connect your GitHub repo.
4. Render auto-detects `render.yaml`. Set the **Environment Variables** below in the Render dashboard.
5. Click **Deploy**.

---

## ⚙️ Config Vars

| Variable | Description |
|----------|-------------|
| `API_ID` | From [my.telegram.org/apps](https://my.telegram.org/apps) |
| `API_HASH` | From [my.telegram.org/apps](https://my.telegram.org/apps) |
| `BOT_TOKEN` | From [@BotFather](https://t.me/BotFather) |
| `MONGO_URI` | MongoDB connection string (optional, enables stats) |

---

## 📁 Project Structure

```
├── main.py               # Entry point
├── port.py               # HTTP health-check server (required by Render)
├── render.yaml           # Render deployment config
├── Procfile              # Process file
├── requirements.txt      # Python dependencies
├── runtime.txt           # Python version
├── database/
│   ├── __init__.py
│   └── mongodb.py        # MongoDB helpers
└── modules/
    ├── __init__.py       # Auto-loads all modules
    ├── start.py          # /start & /help commands
    ├── private.py        # Private chat media handler
    ├── group.py          # Group /tl command
    └── stats.py          # /stats command
```

---

## 🤖 Commands

| Command | Where | Description |
|---------|-------|-------------|
| `/start` | Private | Welcome message |
| `/help` | Private | Help menu |
| `/stats` | Private | Your upload stats |
| `/tl` | Group (reply) | Get Telegraph link for replied media |

---

## 📝 Credits

- [MediaToTelegraphLink bot by TeLe TiPs](https://github.com/teletips/MediaToTelegraphLink-TeLeTiPs)
- [Pyrogram](https://github.com/pyrogram/pyrogram)
