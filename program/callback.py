

from driver.queues import QUEUE
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **Xoş gəldin [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**\n
💭 **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) Yeni Telegram video çatları vasitəsilə qruplarda musiqi və video oynatmağa imkan verir!**

💡 **» 📚 Əmrlər düyməsini klikləməklə Botun bütün əmrlərini və onların necə işlədiyini öyrənin!**

🔖 **Bu botdan necə istifadə edəcəyinizi bilmək üçün lütfən, » ❓ Əsas Bələdçi düyməsini klikləyin!**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ Məni Qrupunuza əlavə edin ➕",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("❓ Basic bələdçisi", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton("📚 Əmrlər", callback_data="cbcmds"),
                    InlineKeyboardButton("❤ Sahib", url=f"https://t.me/{OWNER_NAME}"),
                ],
                [
                    InlineKeyboardButton(
                        "👥 Official Group", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "📣 ŞƏXSİ KANAL", url=f"https://t.me/gunes_isigi_33"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "Kömək", url="https://t.me/nihat_33"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""❓ **Bu botdan istifadə üçün əsas əmrlər:**

1.) **Əvvəlcə məni öz qrupuna əlavə et.**
 2.) **Sonra, məni administrator kimi təşviq edin və Anonim Admindən başqa bütün icazələri verin.**
 3.) **Məni təbliğ etdikdən sonra admin məlumatlarını yeniləmək üçün qrupa yazın /reload yükləyin.**
3.) **@{ASSISTANT_NAME} adlı şəxsi qrupunuza əlavə edin və ya onu dəvət etmək üçün /userbotjoin yazın.**
4.) **Video/musiqi oxutmağa başlamazdan əvvəl video söhbəti yandırın.**
5.) **Bəzən /reload əmrindən istifadə edərək botu yenidən yükləmək bəzi problemləri həll etməyə kömək edə bilər.**

📌 **Əgər userbot video çata qoşulmayıbsa, video çatın artıq aktiv olub olmadığına əmin olun və ya /userbot leave yazın, sonra yenidən /userbot join yazın.**

💡 **Bu bot haqqında əlavə suallarınız varsa, onu buradakı dəstək söhbətimdə deyə bilərsiniz: @{GROUP_SUPPORT}**

👑 __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **Salam [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**

» **izahatı oxumaq və mövcud əmrlərin siyahısına baxmaq üçün aşağıdakı düyməni basın!**

👑 __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("👷🏻 Admin Cmd", callback_data="cbadmin"),
                    InlineKeyboardButton("🧙🏻 Sudo Cmd", callback_data="cbsudo"),
                ],[
                    InlineKeyboardButton("📚 Basic Cmd", callback_data="cbbasic")
                ],[
                    InlineKeyboardButton("🔙 Go Back", callback_data="cbstart")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 Burada əsas əmrlər var:

» /mplay (song name/link) - video söhbətdə musiqi çalın
» /stream (query/link) - yt canlı/radio canlı musiqini yayımlayın
» /vplay (video name/link) - video söhbətdə video oynayın
» /vstream - yt live/m3u8-dən canlı video oynayın
» /playlist - sizə pleylist göstərin
» /video (query) - youtubedan video yukle
» /song (query) - youtube-dan mahnı yükləmək
» /lyric (query) - Mahnının sözlərini sil
» /search (query) - youtube video linkini axtarın

» /ping - bot ping statusunu göstərin
» /uptime - botun işləmə müddətini göstərin
» /alive - botun canlı məlumatını göstərin (qrupda)

👑 __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 Bütün admin əmrləri:

» /pause - Mahnını müvəqqəti dayandırın
» /resume - Mahnını davam etdirin
» /skip - Növbəti mahnıya keçin
» /stop - Mahnını dayandırın
» /vmute - Səsli söhbətdə istifadəçi robotunun səsini söndürün
» /vunmute - Səsli söhbətdə istifadəçi robotunun səsini açın
» /volume `1-200` - musiqinin səsini tənzimləyin (userbot admin olmalıdır)
» /reload - botu yenidən yükləyin və admin məlumatlarını yeniləyin
» /userbotjoin - istifadəçi robotunu qrupa qoşulmağa dəvət edin
» /userbotleave - userbot-a qrupdan çıxmağı əmr edin

👑 __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 Sudo əmrləri budur:

» /rmw - Bütün xam faylları təmizləyin
» /rmd - Bütün yüklənmiş faylları təmizləyin
» /sysinfo - Sistem məlumatlarını göstərin
» /update - Botunuzu ən son versiyaya yeniləyin
» /restart - Botunuzu yenidən başladın
» /leaveall - Userbotun bütün qrupdan çıxmasını əmr edin

👑 __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbmenu"))
async def cbmenu(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("you're an Anonymous Admin !\n\n» revert back to user account from admin rights.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 only admin with manage voice chats permission that can tap this button !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
          await query.edit_message_text(
              f"⚙️ **settings of** {query.message.chat.title}\n\n⏸ : pause stream\n▶️ : resume stream\n🔇 : mute userbot\n🔊 : unmute userbot\n⏹ : stop stream",
              reply_markup=InlineKeyboardMarkup(
                  [[
                      InlineKeyboardButton("⏹", callback_data="cbstop"),
                      InlineKeyboardButton("⏸", callback_data="cbpause"),
                      InlineKeyboardButton("▶️", callback_data="cbresume"),
                  ],[
                      InlineKeyboardButton("🔇", callback_data="cbmute"),
                      InlineKeyboardButton("🔊", callback_data="cbunmute"),
                  ],[
                      InlineKeyboardButton("🗑 Close", callback_data="cls")],
                  ]
             ),
         )
    else:
        await query.answer("❌ nothing is currently streaming", show_alert=True)


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 only admin with manage voice chats permission that can tap this button !", show_alert=True)
    await query.message.delete()
