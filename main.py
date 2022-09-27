

import os
from pyrogram import Client, filters
from pyrogram.errors import QueryIdInvalid
from pyrogram.types import InlineKeyboardButton
from pyrogram.types import InlineKeyboardMarkup
from pyrogram.types import InputTextMessageContent
from pyrogram.types import InlineQueryResultArticle


Bot = Client(
    "Donate",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)


START_TEXT = """Hᴇʏ! {}

💫 इस Group को जीवित रखने के लिए, हमें कुछ दान Monthly चाहिए।

💫 Admins , Bot Hosting Server 24 hrs. सेवा को कवर करने के लिए, हमें वास्तव में इस दान की आवश्यकता है।🥺

❤️Minimum दान प्रति माह 3 /- रु। हमें इससे ज्यादा की जरूरत नहीं है 🙏🏻

हमने हमेशा मुफ्त में सेवा प्रदान की कोशिश की है लेकिन अब हमें सेवा बनाए रखने के लिए आपके समर्थन की बहुत आवश्यकता है।
यदि आप AK-Imax Family में होना महसूस करते हैं तो कृपया हमारी Help करे ।🥺

अगर आप दान करना चाहते हो  तो यहाँ पे Join करे और Screenshot Group में भेज दे ! धन्यवाद🙏🏻

Join Now

💰 (https://t.me/+3KJ5VM9b5ihlOTVl)

Team - AK Imax Movies🙏❤️

========================================

💫 To keep this group alive, we need some donations monthly.

💫 Admins, bot hosting server, to cover 24hrs service, we really need this donation.

❤️Minumin donation Rs 3 /- Rs. We do not need more than this.

We have always tried to provide service for free but now we need a lot of support to maintain service.
If you feel to be in AK-Imax Family, please help us.
🥺

If you want to donate, then join here and send it to the screenshot group! Thank you

Join now (https://t.me/+3KJ5VM9b5ihlOTVl)

Team - AK IMAX Movies🙏 ❤️
☞ Vᴇʀʏ Hᴀᴘᴘʏ ᴛᴏ Kɴᴏᴡ Tʜᴀᴛ Yᴏᴜ ᴀʀᴇ Dᴏɴᴀᴛɪɴɢ Uꜱ.

Tʜᴀɴᴋꜱ Fᴏʀ Uꜱɪɴɢ [Oᴜʀ Bᴏᴛꜱ](https://t.me/+KYLCdC4XfcdmNGVl).

Mᴀᴅᴇ Wɪᴛʜ Lᴏᴠᴇ Fᴏʀ [Yᴏᴜ](tg://settings)"""

DONATE_BUTTONS =[
        InlineKeyboardButton(text="⚡️AK IMAX HUB⚡️", url=f"https://t.me/akimaxmovies"),
        InlineKeyboardButton(text="💬 Discussion - Support 👥", url=f"https://t.me/AkImaxSupport"),
    ], [
    InlineKeyboardButton(
        text='Dᴏɴᴀᴛᴇ 💳',
        callback_data='donateme'
    )
]

DONATE_TEXT = """Hᴇʏ! {}
Yᴏᴜ Cᴀɴ Dᴏɴᴀᴛᴇ Uꜱ Uꜱɪɴɢ UPI.

PayTm/PhonePe/GooglePay - `💰Pay Here [👉 UPI 👈](newprime@ybl)"""

Oʀ Cᴏɴᴛᴀcᴛ Uꜱ :- [BATMAN](https://telegram.me/BATMAN_0). """

BUTTON_TEXT = """ Click the Below Buttons To Donate Us. """

UPI_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(" Back ", callback_data="back"),
            InlineKeyboardButton(" PayPal ", url="https://paypal.me/")
        ],
        [
            InlineKeyboardButton('Close', callback_data='close')
        ]
    ]
)

PAY_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(" UPI ", callback_data="upidata"),
            InlineKeyboardButton(" PayPal ", url="https://paypal.me/")
        ],
        [
            InlineKeyboardButton('Close', callback_data='close')
        ]
    ]
)

@Bot.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    await update.reply_text(
        text=START_TEXT.format(update.from_user.mention),
        reply_markup=InlineKeyboardMarkup([DONATE_BUTTONS]),
        disable_web_page_preview=True,
        quote=True
    )


@Bot.on_message(filters.private & filters.command(["donate"]))
async def donate(bot, update):
    await bot.send_message(
        text="Click the Following Button to Donate Us.",
        reply_markup=InlineKeyboardMarkup([PAY_BUTTONS]),
        disable_web_page_preview=True,
        quote=True
    )

@Bot.on_message(filters.private & filters.command(["bots"]))
async def bots(bot, update):
    await bot.send_message(
        text="https://t.me/+t1ko_FOJxhFiOThl",
        reply_markup=InlineKeyboardMarkup([PAY_BUTTONS]),
        disable_web_page_preview=True,
        quote=True
    )

@Bot.on_inline_query()
async def answerX(bot, update):

    answer = list()
    answer.append(InlineQueryResultArticle(title="This is My Donation Or Payment Bot", description="You Can Donate Us Using Inline.",
    input_message_content=InputTextMessageContent(message_text="Please donate us any amount you like, to support the services."),
    reply_markup=InlineKeyboardMarkup( [ [ InlineKeyboardButton("Dᴏɴᴀᴛᴇ 💳", url="https://upayi.ml/sk7062563@okhdfcbank/10") ] ] ),
    thumb_url="https://telegra.ph/file/330bd070950b8ef775ca9.jpg") )
    try:
        await update.answer(results=answer, cache_time=0)
    except Exception as e:
        print(f"🚸 ERROR : {e}")
    except QueryIdInvalid:
        pass

@Bot.on_callback_query()
async def cb_handler(bot, update):
    if update.data == "donateme":
        await update.message.edit_text(
            text=BUTTON_TEXT.format(update.from_user.mention),
            reply_markup=PAY_BUTTONS,
            disable_web_page_preview=True
        )
    elif update.data == "upidata":
        await update.message.edit_text(
            text=DONATE_TEXT.format(update.from_user.mention),
            reply_markup=UPI_BUTTONS,
            disable_web_page_preview=True
        )
    elif update.data == "back":
        await update.message.edit_text(
            text=BUTTON_TEXT.format(update.from_user.mention),
            reply_markup=PAY_BUTTONS,
            disable_web_page_preview=True
        )
    else:
        await update.message.delete()

Bot.run()
