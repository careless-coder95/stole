from pyrogram import Client
from pyrogram.types import Message, CallbackQuery, InputMediaPhoto
from pyrogram.enums import ParseMode
from utils.keyboards import kb_start, kb_main_menu, kb_setup_guide
from utils.state import clear_state

WELCOME_TEXT = """
<blockquote expandable>🔐 <u>𝗧𝗘𝗟𝗘𝗚𝗥𝗔𝗠 𝗩𝗔𝗨𝗟𝗧 𝗕𝗢𝗧</u></blockquote>

<blockquote><b>💼 𝐀 sᴇᴄᴜʀᴇ sʏsᴛᴇᴍ ᴛᴏ ᴍᴀɴᴀɢᴇ ʏᴏᴜʀ ᴍᴜʟᴛɪᴘʟᴇ ᴛᴇʟᴇɢʀᴀᴍ ᴀᴄᴄᴏᴜɴᴛs ɪɴ ᴏɴᴇ ᴘʟᴀᴄᴇ.</b></blockquote>

<blockquote expandable><b>⚡ ꜰᴀsᴛ • ᴏʀɢᴀɴɪᴢᴇᴅ • ᴇꜰꜰɪᴄɪᴇɴᴛ</b>
<b>🔒 sᴇᴄᴜʀᴇ &amp; ᴘʀɪᴠᴀᴛᴇ sᴇssɪᴏɴs</b>
<b>📊 ᴄʟᴇᴀɴ • sɪᴍᴘʟᴇ • ᴜsᴇʀ-ꜰʀɪᴇɴᴅʟʏ</b></blockquote>

<blockquote expandable><b>⚠️ 𝚂𝚎𝚜𝚜𝚒𝚘𝚗𝚜 𝚜𝚊𝚟𝚎𝚍 𝚕𝚘𝚌𝚊𝚕𝚕𝚢 — 𝚗𝚎𝚟𝚎𝚛 𝚜𝚑𝚊𝚛𝚎𝚍 𝚊𝚗𝚢𝚠𝚑𝚎𝚛𝚎.</b></blockquote>
"""

MAIN_MENU_TEXT = """
<blockquote expandable><b>❖ <u>𝙼𝙰𝙸𝙽 𝙼𝙴𝙽𝚄</u> :</b></blockquote>

<blockquote expandable><b>➥ 𝐀ᴅᴅ ʏᴏᴜʀ ᴀᴄᴄᴏᴜɴᴛs ᴜsɪɴɢ ᴘʜᴏɴᴇ + ᴏᴛᴘ.</b>
<b>➥ 𝐌ᴀɴᴀɢᴇ ᴀɴᴅ ᴠɪᴇᴡ ᴀʟʟ sᴀᴠᴇᴅ ᴀᴄᴄᴏᴜɴᴛs.</b></blockquote>
"""

SETUP_GUIDE_TEXT = """
<blockquote expandable>📘 <u>𝗨𝗦𝗔𝗚𝗘 𝗚𝗨𝗜𝗗𝗘</u> :</blockquote>

<blockquote>1️⃣ <u>𝗔𝗗𝗗 𝗔𝗖𝗖𝗢𝗨𝗡𝗧𝗦</u>
<b>➤ Add your Telegram accounts using phone number + OTP.</b></blockquote>

<blockquote>2️⃣ <u>𝗩𝗜𝗘𝗪 𝗔𝗖𝗖𝗢𝗨𝗡𝗧𝗦</u>
<b>➤ See all your saved accounts in one place.</b></blockquote>

<blockquote>3️⃣ <u>𝗦𝗘𝗧 𝗧𝗔𝗥𝗚𝗘𝗧</u>
<b>➤ Save a user's info by username or user ID.</b></blockquote>

<blockquote>4️⃣ <u>𝗦𝗧𝗔𝗥𝗧 𝗟𝗢𝗩𝗘</u>
<b>➤ Print love messages with reason and count.</b></blockquote>

<blockquote>5️⃣ <u>𝗦𝗘𝗖𝗨𝗥𝗜𝗧𝗬</u>
<b>➤ All sessions stored locally on your server only.</b></blockquote>

<b><i>🚀 Your data. Your control.</i></b>
"""

PHOTO_URL = "https://imghosting.in/host/z8lk74"


async def cmd_start(client: Client, message: Message):
    clear_state(message.from_user.id)
    await message.reply_photo(
        photo=PHOTO_URL,
        caption=WELCOME_TEXT,
        parse_mode=ParseMode.HTML,
        reply_markup=kb_start()
    )


async def cb_main_menu(client: Client, callback: CallbackQuery):
    uid = callback.from_user.id
    clear_state(uid)
    await callback.message.edit_text(
        MAIN_MENU_TEXT,
        parse_mode=ParseMode.HTML,
        reply_markup=kb_main_menu(uid)
    )


async def cb_setup_guide(client: Client, callback: CallbackQuery):
    await callback.message.edit_text(
        SETUP_GUIDE_TEXT,
        parse_mode=ParseMode.HTML,
        reply_markup=kb_setup_guide()
    )


async def cb_back_to_start(client: Client, callback: CallbackQuery):
    await callback.message.edit_media(
        media=InputMediaPhoto(
            media=PHOTO_URL,
            caption=WELCOME_TEXT,
            parse_mode=ParseMode.HTML
        ),
        reply_markup=kb_start()
    )
