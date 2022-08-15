from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

kb_about = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="next", callback_data="button_next_pressed"),
            InlineKeyboardButton(text="cancel", callback_data="button_cancel_pressed")
        ]
    ]
)

kb_profile = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="next", callback_data="button_next_pressed"),
            InlineKeyboardButton(text="cancel", callback_data="button_cancel_pressed")
        ]
    ]
)
