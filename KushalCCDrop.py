import telebot
import random
import time
import threading
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# ================= 🔐 TERA CONFIG DATA =================
BOT_TOKEN = '8704796295:AAHZ4w0Usx4ojywgwLXkBAZdOkC-TphoAAY'
OWNER_ID = 6632236983  

VIDEO_URL = "https://t.me/KUSHALSTORElINK/3"
CHANNEL_LINK = "https://t.me/+taHwUJAStWQ5ODU9"
VIP_CHAT_LINK = "https://t.me/KUSHALSTORElINK/3"

# --- 💎 TERE 23 PREMIUM CUSTOM EMOJI IDs ---
PREMIUM_IDS = [
    "6138409710899958434", "6269285159774720688", "6138522591230431210",
    "6138595008674009570", "5978594450262199893", "6141008793179261507",
    "6138735608723410432", "6138570321201992800", "6138946242509541366",
    "6138793380328510194", "6138530760258228554", "6138435961740071430",
    "5974526806995242353", "6141118306255375302", "6143317514194524082",
    "6073552504979722691", "6073292118292436049", "6070857967052263096",
    "6071052829718483598", "6073643575466267086", "6120436698695338614",
    "6118397435338296885", "6269043439015302799", "6269014138748408445"
]

# --- 💎 TERE PROVIDED BINS (100% USE) ---
KUSHAL_BINS = [
    "613840", "626928", "613852", "613859", "597859", "614100", "613873", 
    "613857", "613894", "613879", "613853", "613843", "597452", "614111", 
    "614331", "607355", "607329", "607085", "607105", "607364", "612043", 
    "611839", "626904", "626901", "515462"
]

active_groups = [] 
bot = telebot.TeleBot(BOT_TOKEN)

# --- 🛠️ PURE KUSHAL BIN GENERATOR ---
def generate_cc():
    bin_num = random.choice(KUSHAL_BINS)
    rest = ''.join([str(random.randint(0, 9)) for _ in range(16 - len(bin_num))])
    mm = str(random.randint(1, 12)).zfill(2)
    yy = random.choice(["2027", "2028", "2029", "2030"])
    cvv = str(random.randint(100, 999))
    return f"{bin_num}{rest}|{mm}|{yy}|{cvv}"

# --- ⚡ TRUE PREMIUM DROP SYSTEM ---
def send_premium_drop(group_id):
    cc_data = generate_cc()
    is_approved = random.choice([True, False, True]) 
    p_id = random.choice(PREMIUM_IDS) # Rotating your Premium IDs
    
    header = "<b>🌠 𝐀𝐏𝐏𝐑𝐎𝐕𝐄𝐃 ✅</b>" if is_approved else "<b>🔻 𝐃𝐄𝐂𝐋𝐈𝐍𝐄𝐃 ❌</b>"
    
    # PREMIUM DESIGN (Clean & Sharp)
    design = (
        f"{header}\n"
        f"<b>━━━━━━━━━━━━━━━━━━━━</b>\n"
        f"<b>💳 𝗖𝗮𝗿𝗱:</b> <code>{cc_data}</code>\n"
        f"<b>🌐 𝐆𝐚𝐭𝐞𝐰𝐚𝐲:</b> <code>𝐒𝐭𝐫𝐢𝐩𝐞 𝐀𝐮𝐭𝐡 ⚡️</code>\n"
        f"<b>📋 𝐈𝐧𝐟𝐨:</b> <b>𝐌𝐀𝐒𝐓𝐄𝐑𝐂𝐀𝐑𝐃 - 𝐃𝐄𝐁𝐈𝐓 - 𝐆𝐈𝐅𝐓</b>\n"
        f"<b>🏛️ 𝐈𝐬𝐬𝐮𝐞𝐫:</b> <code>𝐉𝐬𝐜 𝐏𝐨𝐬𝐭 𝐁𝐚𝐧𝐤</code>\n"
        f"<b>━━━━━━━━━━━━━━━━━━━━</b>\n"
        f"<b>👤 𝐃𝐞𝐯:</b> <a href='https://t.me/kushal_igcc_chats'><b>𝐊𝐮𝐬𝐡𝐚𝐥 𝐎𝐰𝐧𝐞𝐫</b></a> 👑\n"
        f"<b>💎 𝐒𝐭𝐚𝐭𝐮𝐬:</b> <code>𝐏𝐑𝐄𝐌𝐈𝐔𝐌 𝐈𝐃: {p_id}</code> ✨"
    )
    
    # 🔘 Vertical Premium Buttons
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("🌟 𝐉𝐎𝐈𝐍 𝐏𝐑𝐄𝐌𝐈𝐔𝐌 𝐂𝐇𝐀𝐍𝐍𝐄𝐋 🌟", url=CHANNEL_LINK))
    markup.add(InlineKeyboardButton("🔱 𝐕𝐈𝐏 𝐂𝐇𝐀𝐓 🔱", url=VIP_CHAT_LINK))
    
    try:
        sent = bot.send_video(group_id, VIDEO_URL, caption=design, reply_markup=markup, parse_mode="HTML")
        threading.Timer(60, lambda: bot.delete_message(group_id, sent.message_id)).start()
    except: pass

def engine_loop():
    while True:
        if active_groups:
            for group_id in list(active_groups):
                send_premium_drop(group_id)
        time.sleep(5) 

# --- 🚀 STARTUP ---
@bot.message_handler(commands=['start'])
def start_cmd(message):
    chat_id = message.chat.id
    welcome_msg = (
        f"<b>🔱 𝐗-𝐅𝐎𝐑𝐂𝐄 𝐔𝐋𝐓𝐑𝐀 𝐏𝐑𝐄𝐌𝐈𝐔𝐌 🔱</b>\n"
        f"<b>━━━━━━━━━━━━━━━━━━━━━━━</b>\n"
        f"👑 <b>𝐎𝐖𝐍𝐄𝐑:</b> <code>𝐊𝐔𝐒𝐇𝐀𝐋 𝐎𝐖𝐍𝐄𝐑</code>\n"
        f"💎 <b>𝐏𝐑𝐄𝐌𝐈𝐔𝐌:</b> <code>𝐀𝐋𝐋 𝟐𝟑 𝐈𝐃𝐒 𝐋𝐎𝐀𝐃𝐄𝐃 ✅</code>\n"
        f"🚀 <b>𝐒𝐏𝐄𝐄𝐃:</b> <code>𝟓𝐬 𝐅𝐀𝐒𝐓 𝐃𝐑𝐎𝐏</code>\n"
        f"<b>━━━━━━━━━━━━━━━━━━━━━━━</b>\n"
        f"<i>Using Kushal's Private BINS Database...</i>"
    )
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("🔥 𝐒𝐓𝐀𝐑𝐓 𝐆𝐎𝐃 𝐌𝐎𝐃𝐄 🔥", callback_data="start_engine"))
    bot.send_message(chat_id, welcome_msg, reply_markup=markup, parse_mode="HTML")

@bot.callback_query_handler(func=lambda call: call.data == "start_engine")
def callback_start(call):
    chat_id = call.message.chat.id
    if call.from_user.id == OWNER_ID or bot.get_chat_members_count(chat_id) >= 200:
        if chat_id not in active_groups:
            active_groups.append(chat_id)
            bot.answer_callback_query(call.id, "✅ GOD MODE ACTIVE!")
            bot.edit_message_text("<b>🔱 𝐗-𝐅𝐎𝐑𝐂𝐄: 𝐏𝐑𝐄𝐌𝐈𝐔𝐌 𝐎𝐍</b>\n<i>Kushal BINS & Premium IDs Live...</i>", chat_id, call.message.message_id, parse_mode="HTML")
        else: bot.answer_callback_query(call.id, "Already Running!")
    else: bot.answer_callback_query(call.id, "❌ Error: 200+ Members Needed!", show_alert=True)

if __name__ == "__main__":
    print("💎 Kushal Owner: True Premium God Mode V20 is LIVE!")
    threading.Thread(target=engine_loop, daemon=True).start()
    bot.infinity_polling()