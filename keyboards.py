from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

kb_about = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="next", callback_data="button_next_pressed")
        ]
    ]
)
