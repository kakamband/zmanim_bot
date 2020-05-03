from aiogram.types import Update

from ..misc import dp
from .redirects import *
from .warnings import *
from ..exceptions import *


@dp.errors_handler(exception=NoLocationException)
async def no_location_exception_handler(update: Update, e: NoLocationException):
    await redirect_to_request_location()
    return True


@dp.errors_handler(exception=NoLanguageException)
async def no_language_exception_handler(update: Update, e: NoLanguageException):
    await redirect_to_request_language()
    return True


@dp.errors_handler(exception=IncorrectTextException)
async def no_language_exception_handler(update: Update, e: IncorrectTextException):
    await incorrect_text_warning()
    return True


@dp.errors_handler(exception=IncorrectGregorianDateException)
async def gregorian_date_exception_handler(update: Update, e: IncorrectGregorianDateException):
    await incorrect_greg_date_warning()
    return True


@dp.errors_handler(exception=IncorrectJewishDateException)
async def jewish_date_exception_handler(update: Update, e: IncorrectJewishDateException):
    await incorrect_jew_date_warning()
    return True

