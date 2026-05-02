from pyrogram import Client
from pyrogram.types import CallbackQuery
from pyrogram.enums import ParseMode
from utils.keyboards import kb_accounts_list, kb_account_detail, kb_main_menu
from database.db import get_all_accounts, delete_account, get_account


async def cb_list_accounts(client: Client, callback: CallbackQuery):
    uid = callback.from_user.id
    accounts = get_all_accounts(uid)

    if not accounts:
        await callback.message.edit_text(
            "<blockquote>📂 <u>𝗔𝗖𝗖𝗢𝗨𝗡𝗧𝗦</u></blockquote>\n\n"
            "<blockquote><b>🚫 No account is saved.</b>\n"
            "<b>➤ Add your account first.</b></blockquote>",
            parse_mode=ParseMode.HTML,
            reply_markup=kb_main_menu(uid)
        )
        return

    phones = list(accounts.keys())
    await callback.message.edit_text(
        f"<blockquote>📂 <u>𝗬𝗢𝗨𝗥 𝗦𝗔𝗩𝗘𝗗 𝗔𝗖𝗖𝗢𝗨𝗡𝗧𝗦</u> ({len(phones)})</blockquote>\n\n"
        "<blockquote><b>➤ Click on any account to view details.</b></blockquote>",
        parse_mode=ParseMode.HTML,
        reply_markup=kb_accounts_list(phones)
    )


async def cb_account_detail(client: Client, callback: CallbackQuery):
    uid = callback.from_user.id
    phone = callback.data.split(":", 1)[1]
    acc = get_account(uid, phone)

    if not acc:
        await callback.answer("Account nahi mila!", show_alert=True)
        return

    password_display = "✅ Set hai" if acc.get("password") else "❌ Nahi hai"

    await callback.message.edit_text(
        "<blockquote>📱 <u>𝗔𝗖𝗖𝗢𝗨𝗡𝗧 𝗗𝗘𝗧𝗔𝗜𝗟𝗦</u></blockquote>\n\n"
        f"<blockquote><b>📱 Number: <code>{acc['phone']}</code></b>\n"
        f"<b>🔑 2FA: {password_display}</b>\n"
        "<b>🔒 Session: Saved ✅</b></blockquote>",
        parse_mode=ParseMode.HTML,
        reply_markup=kb_account_detail(phone)
    )


async def cb_delete_account(client: Client, callback: CallbackQuery):
    uid = callback.from_user.id
    phone = callback.data.split(":", 1)[1]
    delete_account(uid, phone)
    await callback.answer("✅ Account deleted!", show_alert=True)

    accounts = get_all_accounts(uid)
    phones = list(accounts.keys())

    if not phones:
        await callback.message.edit_text(
            "<blockquote>📂 <u>𝗔𝗖𝗖𝗢𝗨𝗡𝗧𝗦</u></blockquote>\n\n"
            "<blockquote><b>🚫 No account left.</b></blockquote>",
            parse_mode=ParseMode.HTML,
            reply_markup=kb_main_menu(uid)
        )
    else:
        await callback.message.edit_text(
            f"<blockquote>📂 <u>𝗬𝗢𝗨𝗥 𝗦𝗔𝗩𝗘𝗗 𝗔𝗖𝗖𝗢𝗨𝗡𝗧𝗦</u> ({len(phones)})</blockquote>\n\n"
            "<blockquote><b>➤ Click on any account to view details.</b></blockquote>",
            parse_mode=ParseMode.HTML,
            reply_markup=kb_accounts_list(phones)
        )
