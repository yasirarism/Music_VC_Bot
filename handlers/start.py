from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn




@Client.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        f"""Hello 👋 there!\nI can play music in voice chats of Telegeam Groups. I have a lot of cool feature that will amaze you!\n\nDo you want me to play music in your Telegram groups'voice chats? Please click the \' User Manual \' button below to know how you can use me.\n\nThe [Assistant](https://t.me/MusicVCAssistant) must be in your group to play music in the voice chat of your group.\n\nMore info & commands mentioned in the [User Manual](https://telegra.ph/Bemro-VC-Plus-04-09)""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "User Manual", url="https://telegra.ph/Bemro-VC-Plus-04-09")
                  ],[
                    InlineKeyboardButton(
                        "Channel", url="https://t.me/HayakaRyuUpdates"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "Support Chat", url="https://t.me/MusicVCChat"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**🔴 Music player is online**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Support Group", url="https://t.me/MusicVCChat")
                ]
            ]
        )
   )

