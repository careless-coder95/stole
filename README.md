# ⚡ SparkTG Store — Telegram Store Bot

> **Version:** v7.5 (Ultimate)  
> **Framework:** [Hydrogram](https://github.com/hydrogram/hydrogram) (Python)  
> **Type:** Telegram Bot — Digital Accounts & Sessions Store

---

## 📌 Bot Kya Karta Hai?

Yeh ek **Telegram Store Bot** hai jisme users directly Telegram pe:
- 📱 Accounts kharid sakte hain
- 📂 Sessions kharid sakte hain
- 💰 Wallet mein funds add kar sakte hain
- 🎟️ Coupon redeem kar sakte hain
- 👤 Apna profile dekh sakte hain
- 💸 Referral se paise kama sakte hain

---

## 📁 Folder Structure

```
Sparktg-main/
└── sparktgstore/
    ├── main.py              ← Bot start karne ki file (entry point)
    ├── config.py            ← API keys aur settings
    ├── database.py          ← Database functions
    ├── utils.py             ← Helper/utility functions
    ├── requirements.txt     ← Required Python libraries
    │
    ├── plugins/             ← Bot ke alag alag features
    │   ├── start.py         ← /start command, main menu
    │   ├── buy.py           ← Account/Session purchase
    │   ├── deposit.py       ← Wallet funds add karna
    │   ├── stock.py         ← Stock dekhna aur manage karna
    │   ├── admin.py         ← Admin panel
    │   ├── manager.py       ← Manager features
    │   └── redeem.py        ← Coupon redeem
    │
    └── json_db/             ← JSON database files (local storage)
        ├── users.json       ← Users ka data
        ├── orders.json      ← Orders history
        ├── stock.json       ← Available stock
        ├── coupons.json     ← Coupons list
        ├── payments.json    ← Payment records
        └── settings.json    ← Bot settings
```

---

## ⚙️ Setup Guide (Bot Kaise Chalayein)

### Step 1 — Requirements Install Karo

```bash
cd sparktgstore
pip install -r requirements.txt
```

### Step 2 — `config.py` Mein Apni Details Bharo

File open karo: `sparktgstore/config.py`

```python
API_ID      = 123456              # Telegram API ID (my.telegram.org se lo)
API_HASH    = "your_api_hash"     # Telegram API Hash
BOT_TOKEN   = "your_bot_token"    # @BotFather se lo

ADMINS      = [your_telegram_id]  # Apna Telegram User ID

PAYMENT_UPI_ID   = "yourname@upi"     # UPI ID for payments
BINANCE_ID       = "your_binance_id"  # Binance ID (USDT ke liye)
TRC20_ADDRESS    = "your_trc20_addr"  # USDT TRC20 wallet address

USDT_RATE        = 90.0               # 1 USDT = INR rate

LOG_CHANNEL      = -100xxxxxxxxx      # Log channel ID
ADMIN_GROUP_ID   = -100xxxxxxxxx      # Admin group ID

DEFAULT_FSUB_ID   = -100xxxxxxxxx     # Force subscribe channel ID
DEFAULT_FSUB_LINK = "https://t.me/..." # Channel invite link
```

> ⚠️ **Important:** API keys ko GitHub pe publicly mat daalo! `.env` file use karo ya config.py ko `.gitignore` mein add karo.

### Step 3 — Bot Run Karo

```bash
python main.py
```

---

## 🔑 Telegram API Keys Kahan Se Milegi?

| Key | Source |
|-----|--------|
| `API_ID` & `API_HASH` | [my.telegram.org](https://my.telegram.org) |
| `BOT_TOKEN` | Telegram pe [@BotFather](https://t.me/BotFather) |
| `ADMINS` (User ID) | Telegram pe [@userinfobot](https://t.me/userinfobot) |

---

## 📦 Dependencies

```
hydrogram       ← Telegram bot framework
TgCrypto        ← Encryption (speed boost)
Pillow          ← Image processing
qrcode          ← QR code generation
motor           ← MongoDB async driver
dnspython       ← DNS support
pycountry       ← Country data
phonenumbers    ← Phone number validation
requests        ← HTTP requests
aiohttp         ← Async HTTP
```

---

## 💳 Payment Methods Supported

| Method | Details |
|--------|---------|
| UPI | Direct UPI ID se payment |
| USDT (TRC20) | Crypto wallet se |
| Binance Pay | Binance ID se |
| FamPay | FamPay app se |

---

## 🤖 Bot Commands (Users Ke Liye)

| Button | Kaam |
|--------|------|
| 📱 Buy Accounts | Digital accounts purchase |
| 📂 Buy Sessions | Telegram sessions purchase |
| 👛 Add Funds | Wallet recharge |
| 👤 My Profile | Balance, orders dekhna |
| 💰 Earn Money | Referral se kamaai |
| 📞 Support | Help lena |
| 📖 How to Use | Instructions |

---

## 🛡️ Admin Features

- Full stock management (add/remove/view)
- User management
- Broadcast messages
- Order management
- Coupon create/delete
- Payment verification
- Bot settings control

---

## ⚠️ Important Notes

1. **`config.py` GitHub pe mat daalo** — isme sensitive API keys hain
2. **`json_db/` folder** mein real user data hai — isko bhi private rakho
3. **`__pycache__/` folder** GitHub pe upload karne ki zaroorat nahi — `.gitignore` mein add karo

### Recommended `.gitignore`:
```
__pycache__/
*.pyc
*.pyo
config.py
json_db/
*.session
.env
```

---

## 📜 License

Private project. Redistribution allowed only with owner's permission.
