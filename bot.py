from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# ===============================
# BOT TOKEN
# ===============================
TOKEN = "8314480292:AAG9YCIjT1YTX58_gwHDfSIChUuHmx9YwtQ"

# ===============================
# PHOTO DATABASE
# ===============================
PHOTO_MAP = {
    "vintage photo": ("love1.jpg", "i would forever kiss u proudly like this"),
    "cool photo": ("love2.jpg", "we look to cool here,definitely meant for each other"),
    "cheeky photo": ("love3.jpg", "looking at this makes me have baby fever, can't wait to start a family with you!"),
    "lovely photo": ("love4.jpg", "forever receiving hearts from u even when we are far apart,lets never let the spark in us die"),
    "crazy photo": ("love5.jpg", "can't believe i actually found someone that can make me a passenger princess too️"),
    "photo of the prettiest women": ("love6.jpg", "in my eyes,you are the prettiest, always and forever"),
    "aesthetic photo": ("love7.jpg", "we look so good here,no comments but 100/10!"),
    "happy photo": ("love8.jpg", "whenever i see you smile,i'm 10 times happier️"),
    "beautiful photo": ("love9.jpg", "u probably thought i type beautiful cause of the view,thats right because YOU are the view!"),
    "cute photo": ("love10.jpg", "our late night supper vibes are just the best lets have it again soon!"),
    "stunning photo": ("love11.jpg", "just look at us again,we look so beautiful together️"),
    "sprakling photo": ("love12.jpg", "see that spark? thats how much u light up my world everyday"),
    "favourite photo": ("love13.jpg", "this got to be the best, A KISS FROM YOU? i'm glad its ME that get it"),
    "shy photo": ("love14.jpg", "this photo just make us look like kiddos playing with the camera HAHA"),
    "kiddy photo": ("love15.jpg", "aww what a little child,maybe i should call u baby️"),
    "first photo": ("love16.jpg", "still remember this? when history starts"),
    "golden photo": ("love17.jpg", "my greatest and most expensive present for 2025"),
    "memorable photo": ("love18.jpg", "me lowkey trying not to blush because im standing beside the prettiest women️"),
    "blurry photo": ("love19.jpg", "thanks to this ride,you once again rest your head on my shoulders (please do that more often)"),
    "morning photo": ("love20.jpg", "our first morning breakfast together before u kickstart intern"),
    "sleepy photo": ("love21.jpg", "HAHA gotcha, bet you didnt find out i have these huh️"),
    "cafe photo": ("love22.jpg", "i think we are both a foodie, eat anything and everything but sometimes cant finish HAHA"),
    "SURPRISE": ("love.jpg", "Babe,all i want to say is no words can describe how thankful and grateful i am for you. I hope we will never give up on each other,every relationship has their ups and down and this is probably one of the downside we have but i want to remind u that thats just minority of the time, majority of the time we are happy together.")
}

# ===============================
# START COMMAND
# ===============================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hi ❤️")

# ===============================
# MENU COMMAND
# ===============================
async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = []

    for key in PHOTO_MAP:
        keyboard.append([InlineKeyboardButton(key, callback_data=key)])

    await update.message.reply_text(
        "Choose a photo ❤️",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

# ===============================
# BUTTON HANDLER
# ===============================
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    if query.data in PHOTO_MAP:

        filename, caption = PHOTO_MAP[query.data]

        await query.message.reply_photo(
            photo=open(filename, "rb"),
            caption=caption
        )

# ===============================
# MAIN PROGRAM
# ===============================
def main():

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("menu", menu))
    app.add_handler(CallbackQueryHandler(button))

    app.run_polling()

if __name__ == "__main__":
    main()
