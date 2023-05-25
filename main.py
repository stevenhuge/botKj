from telegram import Bot
from telegram.ext import Updater, CommandHandler
import os

# Fungsi penanganan perintah /start
def start_command(update, context):
    chat_id = update.message.chat_id
    folder_path = 'Rahasia'  # Ganti dengan nama folder yang berisi file-file Anda
    base_path = os.getcwd()  # Dapatkan path direktori saat ini

    folder_dir = os.path.join(base_path, folder_path)  # Gabungkan path folder dengan path direktori saat ini

    bot = context.bot
    for file_name in os.listdir(folder_dir):
        file_path = os.path.join(folder_dir, file_name)  # Gabungkan path file dengan path folder
        bot.send_document(chat_id=chat_id, document=open(file_path, 'rb'))


# Fungsi utama untuk menjalankan bot
def main():
    bot_token = '5588275758:AAEqskINZc9UQ2V9fYlo9nwwJn1gd1szWP4'  # Ganti dengan token bot Anda
    updater = Updater(bot_token)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start_command)
    dispatcher.add_handler(start_handler)

    updater.start_polling()
    updater.idle()

# Jalankan bot
if __name__ == '__main__':
    main()
