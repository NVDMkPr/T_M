print("Importing Bot")
import time,json,sys,os,re
from telegram import (
    InlineKeyboardMarkup as IKM,
    InlineKeyboardButton as IKB)
from telegram.ext import (
    Updater,CommandHandler,CallbackQueryHandler)
print("Imported Bot")
from Bot.database import *
from Bot.blockchain import *
bot = Updater("1139627872:AAEewEHKerI6c6ITdq7YLCiCQi4oqWW8wY4",use_context=True)
disp = bot.dispatcher
test = "Đang Thử Nghiệm!"
channel_link = "t.me/TokenTradersOfficial"
group_link = "t.me/joinchat/AAAAAEveStK-MMyiaOgCuQ"

def Send(text,rm,u,c):
    chat_id = u.effective_chat.id
    if rm is None:
        c.bot.send_message(chat_id,text)
    else:
        c.bot.send_message(chat_id,text,reply_markup=rm)
def Edit(text,rm,u,c):
    chat_id = u.effective_chat.id
    message_id = u.effective_message.message_id
    if rm is None:
        c.bot.edit_message(chat_id,message_id,text)
    else:
        c.bot.edit_message(chat_id,message_id,text,reply_markup=rm)

def Start(u,c):
    print("Start Calling")
    reply_markup = IKM([
        [IKB("Danh Sách Airdrop",None,11)],
        [   IKB("Thông Báo Mới Nhất",channel_link),
            IKB("Hỗ Trợ",group_link)    ],
        [IKB("Thông Tin Tài Khoản",None,14)]
        ])
    Send(test,reply_markup,u,c)
    if u.effective_message.text == "/start":
        c.bot.delete_message(u.effective_chat.id,u.effective_message.message_id)
def Set(u,c):
    reply_markup = IKM([
        [IKB("Menu Chính",None,1)]
        ])
    Addr = re.split("^/set ",u.effective_message.text)
    if len(Addr) == 2:
        InsertData("AddrByUser","",f"{u.effective_user.id},'{Addr[1]}'")
    else :
        Send("Địa Chỉ Bạn Vừa Nhập Sai Hoặc Lỗi Gì Đó!",reply_markup,u,c)
        return None
    Send(f"Địa Chỉ Rút Tiền Của Bạn Sẽ Được Lưu Sau 2-60 giây Nữa!\nĐể Tránh Tình Trạng Quá Tải!",reply_markup,u,c)
def AirdropList(u,c):
    print("AirdropList Calling",end="\r")
    reply_markup = IKM([
        [IKB("Airdrop Link",channel_link)],
        [IKB("Trở Lại",None,1)]
        ])
    Send(test,reply_markup,u,c)
def Account(u,c):
    print("Account Calling")
    SearchData = SearchUserID(u.effective_user.id,"AddrGenByUser")
    reply_markup = IKM([
        [IKB("Địa Chỉ Nhận Tiền",None,141)],
        [IKB("Trở Lại",None,1)]
        ])
    if SearchData != None:
        if GetBalance(SearchData[0][1]) == False:
            verified = "Chưa Xác Minh"
        else:
            verified = "Đã Xác Minh" 
        if SearchData[0][2] == 0.0:
            text = f"Địa Chỉ Token: {SearchData[0][1]}\nSố Dư TRX: {SearchData[0][2]} ( ❗ Không Đủ Số Dư Để Chuyển Token )\nTình Trạng Xác Minh: {verified}"
        else:
            text = f"Địa Chỉ Token: {SearchData[0][1]}\nSố Dư TRX: {GetBalance(SearchData[0][1])}\nTình Trạng Xác Minh: {verified}"
        Send(text,reply_markup,u,c)
    elif SearchData == None:
        text = "Đang Tạo Địa Chỉ Token Cho Bạn, Có Thể Mất Tối Đa 1 Phút"
        reply_markup = IKM([[IKB("Trở Lại",None,1)]])
        Send(text,reply_markup,u,c)
        New = GenAddr()
        user_id = u.effective_user.id
        InsertData("AddrGenByUser","",f'''{user_id},"{New[0]}",0.0,"{New[1]}",False''')
        time.sleep(5)
        c.bot.delete_message(u.effective_chat.id,u.effective_message.message_id + 1)
        Account(u,c)
def WithdrawAddr(u,c):
    print("WithdrawAddr Calling")
    Data = "Hãy Nhập Theo Mẫu '/set <Địa Chỉ Của Bạn>' Để Đặt Địa Chỉ Rút Tiền!"
    reply_markup = IKM([
        [IKB("Trở Lại",None,14)]
        ])
    Send(Data,reply_markup,u,c)

def CallbackHandler(u,c):
    u.callback_query.answer()
    c.bot.delete_message(u.effective_chat.id,u.effective_message.message_id)
    data = int(u.callback_query.data)
    if data == 1    : Start(u,c)
    if data == 11   : AirdropList(u,c)
    if data == 14   : Account(u,c)
    if data == 141  : WithdrawAddr(u,c)
    else: pass

disp.add_handler(CommandHandler("set",Set))
disp.add_handler(CommandHandler("start",Start))
disp.add_handler(CallbackQueryHandler(CallbackHandler))

bot.start_polling(clean=True)
print("Starting Bot")