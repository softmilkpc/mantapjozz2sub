# (©)Codexbotz
# Recode by @mrismanaziz
# t.me/SharingUserbot & t.me/Lunatic0de

from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from bot import Bot
from config import OWNER


@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text=f"<b>Join Group dan Channel Mantapjozz:\n============\n1. @Mantapvids\n2. @mantapjozzarea\n4. @mantapfilestorage\n============\nJika ingin bot seperti ini silahkan Deploy pada Link dibawah secara gratis\nSource Code: <a href='https://github.com/softmilkpc/Mantapjozz2Sub'>Mantapjozz File Sharing</a>\n============\nThanks Too: @mrismanaziz\n</b>\n",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("Close", callback_data="close")]]
            ),
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except BaseException:
            pass
