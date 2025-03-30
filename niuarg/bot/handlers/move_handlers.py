from bot import bot
from lexicon import lexicon
from keyboards import get_expence_categoriers_kb, get_main_menu_kb, get_transaction_type_kb,get_main_menu_kb,get_back_to_category_kb,get_income_categories_kb
from telebot import TeleBot
from service.transaction import create_transaction,set_type_transaction,set_category_transaction,can_set_amount_transaction,set_amount_transaction,get_category
def register_move_handlers(bot: TeleBot):
    
    @bot.callback_query_handler(
        func=lambda call: call.data == lexicon.to_fix_transaction.data
    )
    def to_fix_transaction(callback):
        chat_id = callback.message.chat.id
        bot.edit_message_text(
            chat_id=chat_id,
            text="123", 
            message_id=callback.message.message_id,
            reply_markup=get_transaction_type_kb()
        )
        create_transaction(chat_id)
    @bot.callback_query_handler(
        func=lambda call: call.data == lexicon.select_income.data
    )
    def to_select_income_categoria(callback):
        chat_id = callback.message.chat.id
        bot.edit_message_text(
            chat_id=chat_id,
            text='123',
            message_id=callback.message.message_id,
            reply_markup=get_expence_categoriers_kb()
        )
        set_type_transaction(chat_id, lexicon.select_income.text)

    @bot.callback_query_handler(
        func=lambda call: call.data == lexicon.select_expence.data
    )
    def to_select_expence_categoria(callback):
        chat_id = callback.message.chat.id
        bot.edit_message_text(
            chat_id=chat_id,
            text='123',
            message_id=callback.message.message_id,
            reply_markup=get_expence_categoriers_kb()
        )
        print(chat_id)
        set_type_transaction(chat_id,lexicon.select_expence.text)
    @bot.callback_query_handler(
        func=lambda call: call.data == lexicon.from_select_transaction_type.data
    )
    def from_select_transaction_type(callback):
        bot.edit_message_text(
            chat_id=callback.message.chat.id,
            message_id=callback.message.chat.id,
            text=lexicon.start,
            reply_markup=get_main_menu_kb() 
        )

    @bot.callback_query_handler(
        func=lambda call: call.data in (lexicon.gift_income.data,
                                        lexicon.pocket_income.data,
                                        lexicon.salary_income.data,
                                        lexicon.another_income.data,
                                        lexicon.food_expence.data,
                                        lexicon.gift_expence.data,
                                        lexicon.another_expence.data,
                                        lexicon.clothes_expence.data,
                                        lexicon.transport_expence.data,
                                        lexicon.attractions_expence.data,
                                        lexicon.philanthropy_expence.data)
        )
        
    def from_category_to_amout(callback):
        print(1)
        set_category_transaction(callback.message.chat.id, callback.data)
        print(2)
        bot.edit_message_text(
            chat_id=callback.message.chat.id,
            message_id=callback.message.message_id,
            text='Напишите сумму',
            reply_markup=get_back_to_category_kb()
        )

    @bot.message_handler(
        func=lambda msg: can_set_amount_transaction(msg.chat.id) and msg.text.isdigit()
    )
    def fron_amount_to_main_menu(message):
        amount = int(message.text)
        set_amount_transaction(message.chat.id, amount)

    @bot.message_handler(
        func=lambda msg: can_set_amount_transaction(msg.chat.id) and not msg.text.isdigit()
    )
    def error_input_amount(message):
        bot.delete_message(
            chat_id=message.chat.id,
            message_id=message.message_id
        )
    @bot.callback_query_handler(
        func=lambda call: call.data == lexicon.from_amount_to_category.data
    )
    def from_amount_to_category(callback):
        category = get_category(callback.message.chat.id)
        if category.endswith('income'):
            kb = get_income_categories_kb()
        elif category.endswith('expence'):
            kb = get_expence_categoriers_kb()
        bot.edit_message_text(
            chat_id = callback.message.chat.id,
            message_id = callback.message.message_id,
            text='123',
            reply_markup=kb
        )
