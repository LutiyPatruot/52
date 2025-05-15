from lexicon import lexicon
from service.report import pie_chart, trend_chart
from service.database import read_database
from keyboards import get_main_menu_kb




def register_report_handlers(bot):

    @bot.callback_query_handler(
        func=lambda call: call.data == lexicon.to_reports.data
    )
    
    def send_report(callback):
        chat_id = callback.message.chat.id
        data = read_database(chat_id)
        pie = pie_chart(data)
        bot.send_photo(
            chat_id = chat_id,
            photo = pie
        )
        trend = trend_chart(data)
        bot.send_photo(
            chat_id = chat_id,
            photo = trend
        )
        bot.send_message(
            chat_id = chat_id,
            text = lexicon.start,
            reply_markup = get_main_menu_kb()
        )
