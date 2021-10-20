#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @trojanzhex

import asyncio
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import FloodWait
from script import script
from helper_func import decode, get_messages
from config import CUSTOM_CAPTION

@Client.on_message(filters.command(["start"]) & filters.private)
async def start(client, message):
"""
    text = message.text
    if len(text)>7:
        return
        try:
            base64_string = text.split(" ", 1)[1]
        except:
            return
        string = await decode(base64_string)
        argument = string.split("-")
        if len(argument) == 3:
            try:
                ids = [int(argument[1])]
                chennelID = f"-100{int(argument[2])}"
            except:
                return
        temp_msg = await message.reply("Please wait...")
        try:
            messages = await get_messages(client, ids, chennelID)
        except:
            await message.reply_text("Somthing_Went_Wrong...!")
            return
        await temp_msg.delete()

        for msg in messages:
            if bool(CUSTOM_CAPTION) & bool(msg.document):
                caption = CUSTOM_CAPTION.format(previouscaption = "" if not msg.caption else msg.caption.html, filename = msg.document.file_name)
            else:
                caption = "" if not msg.caption else msg.caption.html


            try:
                await msg.copy(
                  chat_id=message.from_user.id, 
                  caption = caption, 
                  parse_mode = 'html', 
                  reply_markup=None
                )
                await asyncio.sleep(0.5)
            except FloodWait as e:
                await asyncio.sleep(e.x)
                await msg.copy(chat_id=message.from_user.id, caption = caption, parse_mode = 'html')
            except:
                pass
        return
"""
    
    reply_markup = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("🎬 Our Main Movie Group", url="https://t.me/joinchat/Q1uroGQ645U1OTg1"),
            ]
        ]
    )
    await message.reply_text(
        text = f"Hi, මොනවාද repo d ඕන ? විහගයා ආත්මාර්ථකාමී සොරි,ඕනනම් උබෙම කියල   එකක්  හදපන් මෙතන අනුන්ගේ ඒවා බලන් නැතුව ",
        reply_markup = reply_markup,
        disable_web_page_preview = True,
        quote = True
    )
    return

@Client.on_message(filters.command(["help"]) & filters.private)
async def help(client, message):
    try:
        await message.reply_text(
            text=script.HELP_MSG,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("BACK", callback_data="start_data"),
                        InlineKeyboardButton("ABOUT", callback_data="about_data"),
                    ],
                    [
                        InlineKeyboardButton(
                            "⭕️ SUPPORT ⭕️", url="https://t.me/TroJanzSupport")
                    ]
                ]
            ),
            reply_to_message_id=message.message_id
        )
    except:
        pass

@Client.on_message(filters.command(["about"]) & filters.private)
async def about(client, message):
    try:
        await message.reply_text(
            text=script.ABOUT_MSG,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("BACK", callback_data="help_data"),
                        InlineKeyboardButton("START", callback_data="start_data"),
                    ],
                    [
                        InlineKeyboardButton(
                            "SOURCE CODE", url="https://github.com/TroJanzHEX/Auto-Filter-Bot-V2")
                    ]
                ]
            ),
            reply_to_message_id=message.message_id
        )
    except:
        pass
