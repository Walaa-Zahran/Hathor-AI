from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

TOKEN = "8373328768:AAHALe_a00uEYZCRh2ShHGZtgb9KiakWJcE"

# Example mock transaction history
transactions = [
    {"id": "TX1A2B3C", "amount": "5 HTR", "status": "Confirmed", "date": "2025-08-10"},
    {"id": "TX4D5E6F", "amount": "2 HTR", "status": "Pending", "date": "2025-08-09"}
]

async def start(update, context):
    await update.message.reply_text("Hello! I’m your HathorAI bot 🤖")

async def handle_message(update, context):
    text = update.message.text.lower()
    if "what is hathor network" in text:
        await update.message.reply_text(
            "Hathor Network is a scalable blockchain that combines DAG and blockchain tech, "
            "allowing easy token creation, low fees, and lightweight smart contracts."
        )
    else:
        await update.message.reply_text("I’m not sure about that yet 🤔")

async def test_payment(update, context):
    await update.message.reply_text(
        "✅ Test Payment Successful!\n"
        "Amount: 1 HTR (Testnet)\n"
        "TX ID: TEST123456"
    )

async def transaction_history(update, context):
    history_text = "📜 Transaction History:\n"
    for tx in transactions:
        history_text += f"🔹 {tx['date']} | {tx['amount']} | {tx['status']} | ID: {tx['id']}\n"
    await update.message.reply_text(history_text)

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("test_payment", test_payment))
    app.add_handler(CommandHandler("history", transaction_history))  # ✅ Added this
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    app.run_polling()

if __name__ == "__main__":
    main()
