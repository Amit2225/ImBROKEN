import os
import sys
import random
from datetime import datetime
from os import execl
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.functions.account import UpdateProfileRequest


from telethon.errors import (
    ChannelInvalidError,
    ChannelPrivateError,
    ChannelPublicGroupNaError,
)
from telethon.tl import functions
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl.functions.messages import GetFullChatRequest


from Config import STRING, SUDO, API_ID, API_HASH, STRING2, STRING3, STRING4 ,STRING5, STRING6, STRING7, STRING8 ,STRING9, STRING10, STRING11, STRING12 , STRING13 , STRING14 , STRING15 ,STRING16 , STRING17 , STRING18 , STRING19 , STRING20 , STRING21 , STRING22 , STRING23 , STRING24 , STRING25 , STRING26 , STRING27 , STRING28 , STRING29 , STRING30
import asyncio
import telethon.utils
from telethon.tl import functions
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from Utils import RAID, RRAID, MRAID, SRAID, CRAID, PORNSPAM


a = API_ID
b = API_HASH
smex = STRING
smexx = STRING2
smexxx = STRING3
smexxxx = STRING4
smexxxxx = STRING5
sixth = STRING6
seven = STRING7
eight = STRING8
ninth = STRING9
tenth = STRING10
eleve = STRING11
twelv = STRING12
thirt = STRING13
forte = STRING14
fifth = STRING15
sieee = STRING16
seeee = STRING17
eieee = STRING18
nieee = STRING19
gandu = STRING20
ekish = STRING21
baish = STRING22
teish = STRING23
tfour = STRING24
tfive = STRING25
tsix = STRING26
tseven = STRING27
teight = STRING28
tnine = STRING29
thirty = STRING30



idk = ""
ydk = ""
wdk = ""
sdk = ""
hdk = ""
adk = ""
bdk = ""
cdk = ""
edk = ""
ddk = ""
vkk = ""
kkk = ""
lkk = ""
mkk = ""
sid = ""
shy = ""
aan = ""
ake = ""
eel = ""
khu = ""
shi = ""
yaa = ""
dav = ""
raj = ""
put = ""
eag = ""
gle = ""
wal = ""
aaa = ""
boy = ""



que = {}

SMEX_USERS = []
for x in SUDO: 
    SMEX_USERS.append(x)
    
async def start_yukki():
    global idk
    global ydk
    global wdk
    global sdk
    global hdk
    global adk
    global bdk
    global cdk
    global ddk
    global edk
    global vkk
    global kkk
    global lkk
    global mkk
    global sid
    global shy
    global aan
    global ake
    global eel
    global khu
    global shi
    global yaa
    global dav
    global raj
    global put
    global eag
    global gle
    global wal
    global aaa
    global boy
    if smex:
        session_name = str(smex)
        print("String 1 Found")
        idk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 1")
            await idk.start()
            botme = await idk.get_me()
            await idk(functions.channels.JoinChannelRequest(channel="@TheMKHackerX131"))
            await idk(functions.channels.JoinChannelRequest(channel="@HELL_X_CHATS"))
            await idk(functions.channels.JoinChannelRequest(channel="@TheMKHackerX131"))
            await idk(functions.channels.JoinChannelRequest(channel="@HELL_X_CHATS"))
            await idk(functions.channels.JoinChannelRequest(channel="@TheMKHackerX131"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 1 not Found")
        session_name = "startup"
        idk = TelegramClient(session_name, a, b)
        try:
            await idk.start()
        except Exception as e:
            pass
   
    if smexx:
        session_name = str(smexx)
        print("String 2 Found")
        ydk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 2")
            await ydk.start()
            await ydk(functions.channels.JoinChannelRequest(channel="@TheMKHackerX131"))
            await ydk(functions.channels.JoinChannelRequest(channel="@HELL_X_CHATS"))
            await ydk(functions.channels.JoinChannelRequest(channel="@TheMKHackerX131"))
            await ydk(functions.channels.JoinChannelRequest(channel="@HELL_X_CHATS"))
            await ydk(functions.channels.JoinChannelRequest(channel="@TheMKHackerX131"))
            botme = await ydk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 2 not Found")
        pass
        session_name = "startup"
        ydk = TelegramClient(session_name, a, b)
        try:
            await ydk.start()
        except Exception as e:
            pass

    if smexxx:
        session_name = str(smexxx)
        print("String 3 Found")
        wdk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 3")
            await  wdk.start()
            await wdk(functions.channels.JoinChannelRequest(channel="@TheMKHackerX131"))
            await wdk(functions.channels.JoinChannelRequest(channel="@HELL_X_CHATS"))
            await wdk(functions.channels.JoinChannelRequest(channel="@TheMKHackerX131"))
            await wdk(functions.channels.JoinChannelRequest(channel="@HELL_X_CHATS"))
            await wdk(functions.channels.JoinChannelRequest(channel="@TheMKHackerX131"))
            botme = await wdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 3 not Found")
        pass
        session_name = "startup"
        wdk = TelegramClient(session_name, a, b)
        try:
            await wdk.start()
        except Exception as e:
            pass

    if smexxxx:
        session_name = str(smexxxx)
        print("String 4 Found")
        hdk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 4")
            await hdk.start()
            await hdk(functions.channels.JoinChannelRequest(channel="@TheMKHackerX131"))
            await hdk(functions.channels.JoinChannelRequest(channel="@HELL_X_CHATS"))
            await hdk(functions.channels.JoinChannelRequest(channel="@TheMKHackerX131"))
            await hdk(functions.channels.JoinChannelRequest(channel="@HELL_X_CHATS"))
            await hdk(functions.channels.JoinChannelRequest(channel="@TheMKHackerX131"))
            botme = await hdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 4 not Found")
        pass
        session_name = "startup"
        hdk = TelegramClient(session_name, a, b)
        try:
            await hdk.start()
        except Exception as e:
            pass

    if smexxxxx:
        session_name = str(smexxxxx)
        print("String 5 Found")
        sdk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 5")
            await sdk.start()
            await sdk(functions.channels.JoinChannelRequest(channel="@TheMKHackerX131"))
            await sdk(functions.channels.JoinChannelRequest(channel="@HELL_X_CHATS"))
            await sdk(functions.channels.JoinChannelRequest(channel="@TheMKHackerX131"))
            await sdk(functions.channels.JoinChannelRequest(channel="@HELL_X_CHATS"))
            await sdk(functions.channels.JoinChannelRequest(channel="@TheMKHackerX131"))
            botme = await sdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 5 not Found")
        pass
        session_name = "startup"
        sdk = TelegramClient(session_name, a, b)
        try:
            await sdk.start()
        except Exception as e:
            pass
                  
    if sixth:
        session_name = str(sixth)
        print("String 6 Found")
        adk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 6")
            await adk.start()
            await adk(functions.channels.JoinChannelRequest(channel="@TheMKHackerX131"))
            await adk(functions.channels.JoinChannelRequest(channel="@HELL_X_CHATS"))
            await adk(functions.channels.JoinChannelRequest(channel="@TheMKHackerX131"))
            await adk(functions.channels.JoinChannelRequest(channel="@HELL_X_CHATS"))
            await adk(functions.channels.JoinChannelRequest(channel="@TheMKHackerX131"))
            botme = await adk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 6 not Found")
        pass
        session_name = "startup"
        adk = TelegramClient(session_name, a, b)
        try:
            await adk.start()
        except Exception as e:
            pass

    if seven:
        session_name = str(seven)
        print("String 7 Found")
        bdk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 7")
            await bdk.start()
            await bdk(functions.channels.JoinChannelRequest(channel="@TheMKHackerX131"))
            await bdk(functions.channels.JoinChannelRequest(channel="@HELL_X_CHATS"))
            await bdk(functions.channels.JoinChannelRequest(channel="@TheMKHackerX131"))
            await bdk(functions.channels.JoinChannelRequest(channel="@HELL_X_CHATS"))
            await bdk(functions.channels.JoinChannelRequest(channel="@TheMKHackerX131"))
            botme = await bdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 7 not Found")
        pass
        session_name = "startup"
        bdk = TelegramClient(session_name, a, b)
        try:
            await bdk.start()
        except Exception as e:
            pass    
        
    
    if eight:
        session_name = str(eight)
        print("String 8 Found")
        cdk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 8")
            await cdk.start()
            await cdk(functions.channels.JoinChannelRequest(channel="@TheMKHackerX131"))
            await cdk(functions.channels.JoinChannelRequest(channel="@HELL_X_CHATS"))
            await cdk(functions.channels.JoinChannelRequest(channel="@TheMKHackerX131"))
            await cdk(functions.channels.JoinChannelRequest(channel="@HELL_X_CHATS"))
            await cdk(functions.channels.JoinChannelRequest(channel="@TheMKHackerX131"))
            botme = await cdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 8 not Found")
        pass
        session_name = "startup"
        cdk = TelegramClient(session_name, a, b)
        try:
            await cdk.start()
        except Exception as e:
            pass   
        
    if ninth:
        session_name = str(ninth)
        print("String 9 Found")
        ddk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 9")
            await ddk.start()
            await ddk(functions.channels.JoinChannelRequest(channel="@TheMKHackerX131"))
            await ddk(functions.channels.JoinChannelRequest(channel="@HELL_X_CHATS"))
            await ddk(functions.channels.JoinChannelRequest(channel="@TheMKHackerX131"))
            await ddk(functions.channels.JoinChannelRequest(channel="@HELL_X_CHATS"))
            await ddk(functions.channels.JoinChannelRequest(channel="@TheMKHackerX131"))
            botme = await ddk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 9 not Found")
        pass
        session_name = "startup"
        ddk = TelegramClient(session_name, a, b)
        try:
            await ddk.start()
        except Exception as e:
            pass   
    
  
    if tenth:
        session_name = str(tenth)
        print("String 10 Found")
        edk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 10")
            await edk.start()
            await edk(functions.channels.JoinChannelRequest(channel="@TheMKHackerX131"))
            await edk(functions.channels.JoinChannelRequest(channel="@HELL_X_CHATS"))
            await edk(functions.channels.JoinChannelRequest(channel="@TheMKHackerX131"))
            await edk(functions.channels.JoinChannelRequest(channel="@HELL_X_CHATS"))
            await edk(functions.channels.JoinChannelRequest(channel="@TheMKHackerX131"))
            botme = await edk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 10 not Found")
        pass
        session_name = "startup"
        edk = TelegramClient(session_name, a, b)
        try:
            await edk.start()
        except Exception as e:
            pass 
        
    
    if eleve:
        session_name = str(eleve)
        print("String 11 Found")
        vkk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 11")
            await vkk.start()
            await vkk(functions.channels.JoinChannelRequest(channel="@TheMKHackerX131"))
            await vkk(functions.channels.JoinChannelRequest(channel="@HELL_X_CHATS"))
            await vkk(functions.channels.JoinChannelRequest(channel="@TheMKHackerX131"))
            await vkk(functions.channels.JoinChannelRequest(channel="@HELL_X_CHATS"))
            await vkk(functions.channels.JoinChannelRequest(channel="@TheMKHackerX131"))
            botme = await vkk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 11 not Found")
        pass
        session_name = "startup"
        vkk = TelegramClient(session_name, a, b)
        try:
            await vkk.start()
        except Exception as e:
            pass
        
    
    if twelv:
        session_name = str(twelv)
        print("String 12 Found")
        kkk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 12")
            await kkk.start()
            await kkk(functions.channels.JoinChannelRequest(channel="@TheMKHackerX131"))
            await kkk(functions.channels.JoinChannelRequest(channel="@HELL_X_CHATS"))
            await kkk(functions.channels.JoinChannelRequest(channel="@TheMKHackerX131"))
            await kkk(functions.channels.JoinChannelRequest(channel="@HELL_X_CHATS"))
            await kkk(functions.channels.JoinChannelRequest(channel="@TheMKHackerX131"))
            botme = await kkk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 12 not Found")
        pass
        session_name = "startup"
        kkk = TelegramClient(session_name, a, b)
        try:
            await kkk.start()
        except Exception as e:
            pass   
    
  
    if thirt:
        session_name = str(thirt)
        print("String 13  Found")
        lkk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 13")
            await lkk.start()
            await lkk(functions.channels.JoinChannelRequest(channel="@TheMKHackerX131"))
            await lkk(functions.channels.JoinChannelRequest(channel="@HELL_X_CHATS"))
            await lkk(functions.channels.JoinChannelRequest(channel="@TheMKHackerX131"))
            await lkk(functions.channels.JoinChannelRequest(channel="@HELL_X_CHATS"))
            await lkk(functions.channels.JoinChannelRequest(channel="@TheMKHackerX131"))
            botme = await lkk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 13 not Found")
        pass
        session_name = "startup"
        lkk = TelegramClient(session_name, a, b)
        try:
            await lkk.start()
        except Exception as e:
            pass 
        
    
    if forte:
        session_name = str(forte)
        print("String 14 Found")
        mkk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 14")
            await mkk.start()
            await mkk(functions.channels.JoinChannelRequest(channel="@TheMKHackerX131"))
            await mkk(functions.channels.JoinChannelRequest(channel="@HELL_X_CHATS"))
            await mkk(functions.channels.JoinChannelRequest(channel="@TheMKHackerX131"))
            await mkk(functions.channels.JoinChannelRequest(channel="@HELL_X_CHATS"))
            await mkk(functions.channels.JoinChannelRequest(channel="@TheMKHackerX131"))
            botme = await mkk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 14 not Found")
        pass
        session_name = "startup"
        mkk = TelegramClient(session_name, a, b)
        try:
            await mkk.start()
        except Exception as e:
            pass
        
    
    if fifth:
        session_name = str(fifth)
        print("String 15 Found")
        sid = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 15")
            await sid.start()
            await sid(functions.channels.JoinChannelRequest(channel="@TheMKHackerX131"))
            await sid(functions.channels.JoinChannelRequest(channel="@HELL_X_CHATS"))
            await sid(functions.channels.JoinChannelRequest(channel="@TheMKHackerX131"))
            await sid(functions.channels.JoinChannelRequest(channel="@HELL_X_CHATS"))
            await sid(functions.channels.JoinChannelRequest(channel="@TheMKHackerX131"))
            botme = await sid.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 15 not Found")
        pass
        session_name = "startup"
        sid = TelegramClient(session_name, a, b)
        try:
            await sid.start()
        except Exception as e:
            pass


    if sieee:
        session_name = str(sieee)
        print("String 16 Found")
        shy = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 16")
            await shy.start()
            botme = await shy.get_me()
            await shy(functions.channels.JoinChannelRequest(channel="@TheMKHackerX131"))
            await shy(functions.channels.JoinChannelRequest(channel="@HELL_X_CHATS"))
            await shy(functions.channels.JoinChannelRequest(channel="@TheMKHackerX131"))
            await shy(functions.channels.JoinChannelRequest(channel="@HELL_X_CHATS"))
            await shy(functions.channels.JoinChannelRequest(channel="@TheMKHackerX131"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 16 not Found")
        session_name = "startup"
        shy = TelegramClient(session_name, a, b)
        try:
            await shy.start()
        except Exception as e:
            pass
   
    if seeee:
        session_name = str(seeee)
        print("String 17 Found")
        aan = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 17")
            await aan.start()
            botme = await aan.get_me()
            await aan(functions.channels.JoinChannelRequest(channel="@TheMKHackerX131"))
            await aan(functions.channels.JoinChannelRequest(channel="@HELL_X_CHATS"))
            await aan(functions.channels.JoinChannelRequest(channel="@TheMKHackerX131"))
            await aan(functions.channels.JoinChannelRequest(channel="@HELL_X_CHATS"))
            await aan(functions.channels.JoinChannelRequest(channel="@TheMKHackerX131"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 17 not Found")
        session_name = "startup"
        aan = TelegramClient(session_name, a, b)
        try:
            await aan.start()
        except Exception as e:
            pass
   
    if eieee:
        session_name = str(eieee)
        print("String 18 Found")
        ake = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 18")
            await ake.start()
            botme = await ake.get_me()
            await ake(functions.channels.JoinChannelRequest(channel="@TheMKHackerX131"))
            await ake(functions.channels.JoinChannelRequest(channel="@HELL_X_CHATS"))
            await ake(functions.channels.JoinChannelRequest(channel="@TheMKHackerX131"))
            await ake(functions.channels.JoinChannelRequest(channel="@HELL_X_CHATS"))
            await ake(functions.channels.JoinChannelRequest(channel="@TheMKHackerX131"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 18 not Found")
        session_name = "startup"
        ake = TelegramClient(session_name, a, b)
        try:
            await ake.start()
        except Exception as e:
            pass
   
    if nieee:
        session_name = str(nieee)
        print("String 19 Found")
        eel = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 19")
            await eel.start()
            botme = await eel.get_me()
            await eel(functions.channels.JoinChannelRequest(channel="@TheMKHackerX131"))
            await eel(functions.channels.JoinChannelRequest(channel="@HELL_X_CHATS"))
            await eel(functions.channels.JoinChannelRequest(channel="@TheMKHackerX131"))
            await eel(functions.channels.JoinChannelRequest(channel="@HELL_X_CHATS"))
            await eel(functions.channels.JoinChannelRequest(channel="@TheMKHackerX131"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 19 not Found")
        session_name = "startup"
        eel = TelegramClient(session_name, a, b)
        try:
            await idk.start()
        except Exception as e:
            pass
   
    if gandu:
        session_name = str(gandu)
        print("String 20 Found")
        khu = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 20")
            await khu.start()
            botme = await khu.get_me()
            await khu(functions.channels.JoinChannelRequest(channel="@TheMKHackerX131"))
            await khu(functions.channels.JoinChannelRequest(channel="@HELL_X_CHATS"))
            await khu(functions.channels.JoinChannelRequest(channel="@TheMKHackerX131"))
            await khu(functions.channels.JoinChannelRequest(channel="@HELL_X_CHATS"))
            await khu(functions.channels.JoinChannelRequest(channel="@TheMKHackerX131"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 20 not Found")
        session_name = "startup"
        khu = TelegramClient(session_name, a, b)
        try:
            await khu.start()
        except Exception as e:
            pass
   
    if ekish:
        session_name = str(ekish)
        print("String 21 Found")
        shi = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 21")
            await shi.start()
            botme = await shi.get_me()
            await shi(functions.channels.JoinChannelRequest(channel="@TheMKHackerX131"))
            await shi(functions.channels.JoinChannelRequest(channel="@HELL_X_CHATS"))
            await shi(functions.channels.JoinChannelRequest(channel="@TheMKHackerX131"))
            await shi(functions.channels.JoinChannelRequest(channel="@HELL_X_CHATS"))
            await shi(functions.channels.JoinChannelRequest(channel="@TheMKHackerX131"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 21 not Found")
        session_name = "startup"
        shi = TelegramClient(session_name, a, b)
        try:
            await shi.start()
        except Exception as e:
            pass
   
    if baish:
        session_name = str(baish)
        print("String 22 Found")
        yaa = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 22")
            await yaa.start()
            botme = await yaa.get_me()
            await yaa(functions.channels.JoinChannelRequest(channel="@TheMKHackerX131"))
            await yaa(functions.channels.JoinChannelRequest(channel="@HELL_X_CHATS"))
            await yaa(functions.channels.JoinChannelRequest(channel="@TheMKHackerX131"))
            await yaa(functions.channels.JoinChannelRequest(channel="@HELL_X_CHATS"))
            await yaa(functions.channels.JoinChannelRequest(channel="@TheMKHackerX131"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 22 not Found")
        session_name = "startup"
        yaa = TelegramClient(session_name, a, b)
        try:
            await yaa.start()
        except Exception as e:
            pass
   
    if teish:
        session_name = str(teish)
        print("String 23 Found")
        dav = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 23")
            await dav.start()
            botme = await dav.get_me()
            await dav(functions.channels.JoinChannelRequest(channel="@TheMKHackerX131"))
            await dav(functions.channels.JoinChannelRequest(channel="@HELL_X_CHATS"))
            await dav(functions.channels.JoinChannelRequest(channel="@TheMKHackerX131"))
            await dav(functions.channels.JoinChannelRequest(channel="@HELL_X_CHATS"))
            await dav(functions.channels.JoinChannelRequest(channel="@TheMKHackerX131"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 23 not Found")
        session_name = "startup"
        dav = TelegramClient(session_name, a, b)
        try:
            await dav.start()
        except Exception as e:
            pass
   
    if tfour:
        session_name = str(tfour)
        print("String 24 Found")
        raj = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 24")
            await raj.start()
            botme = await raj.get_me()
            await raj(functions.channels.JoinChannelRequest(channel="@TheMKHackerX131"))
            await raj(functions.channels.JoinChannelRequest(channel="@HELL_X_CHATS"))
            await raj(functions.channels.JoinChannelRequest(channel="@TheMKHackerX131"))
            await raj(functions.channels.JoinChannelRequest(channel="@HELL_X_CHATS"))
            await raj(functions.channels.JoinChannelRequest(channel="@TheMKHackerX131"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 24 not Found")
        session_name = "startup"
        raj = TelegramClient(session_name, a, b)
        try:
            await raj.start()
        except Exception as e:
            pass
   
    if tfive:
        session_name = str(tfive)
        print("String 25 Found")
        put = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 25")
            await put.start()
            botme = await put.get_me()
            await put(functions.channels.JoinChannelRequest(channel="@TheMKHackerX131"))
            await put(functions.channels.JoinChannelRequest(channel="@HELL_X_CHATS"))
            await put(functions.channels.JoinChannelRequest(channel="@TheMKHackerX131"))
            await put(functions.channels.JoinChannelRequest(channel="@HELL_X_CHATS"))
            await put(functions.channels.JoinChannelRequest(channel="@TheMKHackerX131"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 25 not Found")
        session_name = "startup"
        put = TelegramClient(session_name, a, b)
        try:
            await put.start()
        except Exception as e:
            pass
   
    if tsix:
        session_name = str(tsix)
        print("String 26 Found")
        eag = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 26")
            await eag.start()
            botme = await eag.get_me()
            await eag(functions.channels.JoinChannelRequest(channel="@TheMKHackerX131"))
            await eag(functions.channels.JoinChannelRequest(channel="@HELL_X_CHATS"))
            await eag(functions.channels.JoinChannelRequest(channel="@TheMKHackerX131"))
            await eag(functions.channels.JoinChannelRequest(channel="@HELL_X_CHATS"))
            await eag(functions.channels.JoinChannelRequest(channel="@TheMKHackerX131"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 26 not Found")
        session_name = "startup"
        eag = TelegramClient(session_name, a, b)
        try:
            await eag.start()
        except Exception as e:
            pass
   
    if tseven:
        session_name = str(tseven)
        print("String 27 Found")
        ydk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 27")
            await gle.start()
            await gle(functions.channels.JoinChannelRequest(channel="@TheMKHackerX131"))
            await gle(functions.channels.JoinChannelRequest(channel="@HELL_X_CHATS"))
            await gle(functions.channels.JoinChannelRequest(channel="@TheMKHackerX131"))
            await gle(functions.channels.JoinChannelRequest(channel="@HELL_X_CHATS"))
            await gle(functions.channels.JoinChannelRequest(channel="@TheMKHackerX131"))
            botme = await gle.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 27 not Found")
        pass
        session_name = "startup"
        gle = TelegramClient(session_name, a, b)
        try:
            await gle.start()
        except Exception as e:
            pass

    if teight:
        session_name = str(teight)
        print("String 28 Found")
        wal = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 28")
            await wal.start()
            await wal(functions.channels.JoinChannelRequest(channel="@TheMKHackerX131"))
            await wal(functions.channels.JoinChannelRequest(channel="@HELL_X_CHATS"))
            await wal(functions.channels.JoinChannelRequest(channel="@TheMKHackerX131"))
            await wal(functions.channels.JoinChannelRequest(channel="@HELL_X_CHATS"))
            await wal(functions.channels.JoinChannelReques          (channel
                ="@SAB_KAA_KATEGA"))
            botme = await wal.get_me()
            botid = telethon.jutils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 28 not Found")
        pass
        session_name = "startup"
        wal = TelegramClient(session_name, a, b)
        try:
            await wal.start()
        except Exception as e:
            pass

    if tnine:
        session_name = str(tnine)
        print("String 29 Found")
        aaa = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 29")
            await aaa.start()
            await aaa(functions.channels.JoinChannelRequest(channel="@TheMKHackerX131"))
            await aaa(functions.channels.JoinChannelRequest(channel="@HELL_X_CHATS"))
            await aaa(functions.channels.JoinChannelRequest(channel="@TheMKHackerX131"))
            await aaa(functions.channels.JoinChannelRequest(channel="@HELL_X_CHATS"))
            await aaa(functions.channels.JoinChannelRequest(channel="@TheMKHackerX131"))
            botme = await aaa.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 29 not Found")
        pass
        session_name = "startup"
        aaa = TelegramClient(session_name, a, b)
        try:
            await aaa.start()
        except Exception as e:
            pass

    if thirty:
        session_name = str(thirty)
        print("String 30 Found")
        boy = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 30")
            await boy.start()
            await boy(functions.channels.JoinChannelRequest(channel="@TheMKHackerX131"))
            await boy(functions.channels.JoinChannelRequest(channel="@HELL_X_CHATS"))
            await boy(functions.channels.JoinChannelRequest(channel="@TheMKHackerX131"))
            await boy(functions.channels.JoinChannelRequest(channel="@HELL_X_CHATS"))
            await boy(functions.channels.JoinChannelRequest(channel="@TheMKHackerX131"))
            botme = await boy.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 30 not Found")
        pass
        session_name = "startup"
        boy = TelegramClient(session_name, a, b)
        try:
            await boy.start()
        except Exception as e:
            pass
                  
   
loop = asyncio.get_event_loop()
loop.run_until_complete(start_yukki())       

async def gifspam(e, smex):
    try:
        await e.client(
            functions.messages.SaveGifRequest(
                id=types.InputDocument(
                    id=sandy.media.document.id,
                    access_hash=smex.media.document.access_hash,
                    file_reference=smex.media.document.file_reference,
                ),
                unsave=True,
            )
        )
    except Exception as e:
        pass


@idk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@eag.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@gle.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@wal.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@aaa.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@boy.on(events.NewMessage(incoming=True, pattern=r"\.bio"))

async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗕𝗶𝗼\n\nCommand:\n\n.bio <Message to set Bio of Userbot accounts>"
    if e.sender_id in SMEX_USERS:
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)     
        if len(e.text) > 5:
            bio = str(yukki[0])
            text = "Changing Bio"
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await e.client(functions.account.UpdateProfileRequest(about=bio))
                await event.edit("Succesfully Changed Bio By BROKEN SPAMBOT")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
            
@idk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.join")) 
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.join")) 
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.join")) 
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.join")) 
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.join")) 
@sid.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@eag.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@gle.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@wal.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@aaa.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@boy.on(events.NewMessage(incoming=True, pattern=r"\.join"))


async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗝𝗼𝗶𝗻\n\nCommand:\n\n.join <Public Channel or Group Link/Username>"
    if e.sender_id in SMEX_USERS:
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 6:
            bc = yukki[0]
            text = "Joining..."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await e.client(functions.channels.JoinChannelRequest(channel=bc))
                await event.edit("🇦 jj 🇸 ᎪbᏦᎥ 🇲 Ꭺ 🇨 huᎠᎬᎶᎥ 🇸 ᎪᏁᏦᎥ 🇰 Ꭼ 🇱 ᎪuᎠᎬ 🇵 Ꭼ🔥🔥🔥🔥")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
            
@idk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.pjoin")) 
@ake.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@eag.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@gle.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@wal.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@aaa.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@boy.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))



async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗣𝗿𝗶𝘃𝗮𝘁𝗲 𝗝𝗼𝗶𝗻\n\nCommand:\n\n.pjoin <Private Channel or Group's access hash>\n\nExample :\nLink = https://t.me/joinchat/HGYs1wvsPUplMmM1\n\n.pjoin HGYs1wvsPUplMmM1"
    if e.sender_id in SMEX_USERS:
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 7:
            bc = yukki[0]
            text = "Joining...."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await e.client(ImportChatInviteRequest(bc))
                await event.edit("🇵 ᏒᎥᏉᎪᏆᎬ 🇲 Ꭼ 🇨 hᎾᎠuᏁᎶᎪ 🇦 jj")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
            
        
@idk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@eag.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@gle.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@wal.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@aaa.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@boy.on(events.NewMessage(incoming=True, pattern=r"\.leave"))


async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗟𝗲𝗮𝘃𝗲\n\nCommand:\n\n.leave <Channel or Chat ID>"
    if e.sender_id in SMEX_USERS:
        mk = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 7:
            bc = mk[0]
            bc = int(bc)
            text = "Bye"
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await event.client(LeaveChannelRequest(bc))
                await event.edit("🇲 ᗩ ᑕᕼᑌᗪ ᘜYI ᗷᗩᑕᕼO KI 🔥🔥")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
            
                

@idk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@eag.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@gle.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@wal.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@aaa.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@boy.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))


async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗗𝗲𝗹𝗮𝘆𝗦𝗽𝗮𝗺\n\nCommand:\n\n.delayspam <sleep time> <count> <message to spam>\n\n.delayspam <sleep time> <count> <reply to a message>\n\nCount and Sleeptime must be a integer."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        smex = await e.get_reply_message()
        yukki = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
        yukkisexy = yukki[1:]
        if len(yukkisexy) == 2:
            message = str(yukkisexy[1])
            counter = int(yukkisexy[0])
            sleeptime = float(yukki[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    if e.reply_to_msg_id:
                        await smex.reply(message)
                    else:
                        await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(sleeptime)
        elif e.reply_to_msg_id and smex.media:  
            counter = int(yukkisexy[0])
            sleeptime = float(yukki[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "document"):
                    smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                    await gifspam(e, smex) 
                await asyncio.sleep(sleeptime)
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(yukkisexy[0])
            sleeptime = float(yukki[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(sleeptime)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )


@idk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@eag.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@gle.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@wal.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@aaa.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@boy.on(events.NewMessage(incoming=True, pattern=r"\.spam"))


async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗕𝗶𝗴𝗦𝗽𝗮𝗺\n\nCommand:\n\n.bigspam <count> <message to spam>\n\n.bigspam <count> <reply to a message>\n\nCount must be a integer."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        aries = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(aries) == 2:
            message = str(aries[1])
            counter = int(aries[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    if e.reply_to_msg_id:
                        await smex.reply(message)
                    else:
                        await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(0.1)
        elif e.reply_to_msg_id and smex.media:  
            counter = int(aries[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "document"):
                    smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                    await gifspam(e, smex) 
                await asyncio.sleep(0.1)  
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(aries[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(0.1)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )



@idk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@eag.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@gle.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@wal.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@aaa.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@boy.on(events.NewMessage(incoming=True, pattern=r"\.raid"))

async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗥𝗮𝗶𝗱\n\nCommand:\n\n.raid <count> <Username of User>\n\n.raid <count> <reply to a User>\n\nCount must be a integer."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        aries = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(aries) == 2:
            message = str(aries[1])
            print(message)
            a = await e.client.get_entity(message)
            g = a.id
            c = a.first_name
            username = f"[{c}](tg://user?id={g})"
            counter = int(aries[0])
            for _ in range(counter):
                reply = random.choice(RAID)
                caption = f"{username} {reply}"
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.1)
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            c = b.first_name
            counter = int(aries[0])
            username = f"[{c}](tg://user?id={g})"
            for _ in range(counter):
                reply = random.choice(RAID)
                caption = f"{username} {reply}"
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.1)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )



@idk.on(events.NewMessage(incoming=True, pattern=r"\.mraid"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.mraid"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.mraid"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.mraid"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.mraid"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.mraid"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.mraid"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.mraid"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.mraid"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.mraid"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.mraid"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.mraid"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.mraid"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.mraid"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.mraid"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.mraid"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.mraid"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.mraid"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.mraid"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.mraid"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.mraid"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.mraid"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.mraid"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.mraid"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.mraid"))
@eag.on(events.NewMessage(incoming=True, pattern=r"\.mraid"))
@gle.on(events.NewMessage(incoming=True, pattern=r"\.mraid"))
@wal.on(events.NewMessage(incoming=True, pattern=r"\.mraid"))
@aaa.on(events.NewMessage(incoming=True, pattern=r"\.mraid"))
@boy.on(events.NewMessage(incoming=True, pattern=r"\.mraid"))

async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗠𝗥𝗮𝗶𝗱\n\nCommand:\n\n.mraid <count> <Username of User>\n\n.mraid <count> <reply to a User>\n\nCount must be a integer."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(yukki) == 2:
            message = str(yukki[1])
            a = await e.client.get_entity(message)
            g = a.id
            c = a.first_name
            username = f"[{c}](tg://user?id={g})"
            counter = int(yukki[0])
            for _ in range(counter):
                reply = random.choice(MRAID)
                caption = f"{username} {reply}"
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.3)
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            c = b.first_name
            counter = int(yukki[0])
            username = f"[{c}](tg://user?id={g})"
            for _ in range(counter):
                reply = random.choice(MRAID)
                caption = f"{username} {reply}"
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.1)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )


@idk.on(events.NewMessage(incoming=True, pattern=r"\.craid"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.craid"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.craid"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.craid"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.craid"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.craid"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.craid"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.craid"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.craid"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.craid"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.craid"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.craid"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.craid"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.craid"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.craid"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.craid"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.craid"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.craid"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.craid"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.craid"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.craid"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.craid"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.craid"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.craid"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.craid"))
@eag.on(events.NewMessage(incoming=True, pattern=r"\.craid"))
@gle.on(events.NewMessage(incoming=True, pattern=r"\.craid"))
@wal.on(events.NewMessage(incoming=True, pattern=r"\.craid"))
@aaa.on(events.NewMessage(incoming=True, pattern=r"\.craid"))
@boy.on(events.NewMessage(incoming=True, pattern=r"\.craid"))

async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = C𝗥𝗮𝗶𝗱\n\nCommand:\n\n.craid <count> <Username of User>\n\n.craid <count> <reply to a User>\n\nCount must be a integer."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(yukki) == 2:
            message = str(yukki[1])
            a = await e.client.get_entity(message)
            g = a.id
            c = a.first_name
            username = f"[{c}](tg://user?id={g})"
            counter = int(yukki[0])
            for _ in range(counter):
                reply = random.choice(CRAID)
                caption = f"{username} {reply}"
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.3)
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            c = b.first_name
            counter = int(yukki[0])
            username = f"[{c}](tg://user?id={g})"
            for _ in range(counter):
                reply = random.choice(CRAID)
                caption = f"{username} {reply}"
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.1)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )           
       
    
@idk.on(events.NewMessage(incoming=True, pattern=r"\.sraid"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.sraid"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.sraid"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.sraid"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.sraid"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.sraid"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.sraid"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.sraid"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.sraid"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.sraid"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.sraid"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.sraid"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.sraid"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.sraid"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.sraid"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.sraid"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.sraid"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.sraid"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.sraid"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.sraid"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.sraid"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.sraid"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.sraid"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.sraid"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.sraid"))
@eag.on(events.NewMessage(incoming=True, pattern=r"\.sraid"))
@gle.on(events.NewMessage(incoming=True, pattern=r"\.sraid"))
@wal.on(events.NewMessage(incoming=True, pattern=r"\.sraid"))
@aaa.on(events.NewMessage(incoming=True, pattern=r"\.sraid"))
@boy.on(events.NewMessage(incoming=True, pattern=r"\.sraid"))

async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗦𝗥𝗮𝗶𝗱\n\nCommand:\n\n.sraid <count> <Username of User>\n\n.sraid <count> <reply to a User>\n\nCount must be a integer."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(yukki) == 2:
            message = str(yukki[1])
            print(message)
            a = await e.client.get_entity(message)
            g = a.id
            c = a.first_name
            username = f"[{c}](tg://user?id={g})"
            counter = int(yukki[0])
            for _ in range(counter):
                reply = random.choice(SRAID)
                caption = f"{username} {reply}"
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.3)
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            c = b.first_name
            counter = int(yukki[0])
            username = f"[{c}](tg://user?id={g})"
            for _ in range(counter):
                reply = random.choice(SRAID)
                caption = f"{username} {reply}"
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.1)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )







@idk.on(events.NewMessage(incoming=True, pattern=r"\.repo"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.repo"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.repo"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.repo"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.repo"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.repo"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.repo"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.repo"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.repo"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.repo"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.repo"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.repo"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.repo"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.repo"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.repo"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.repo"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.repo"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.repo"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.repo"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.repo"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.repo"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.repo"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.repo"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.repo"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.repo"))
@eag.on(events.NewMessage(incoming=True, pattern=r"\.repo"))
@gle.on(events.NewMessage(incoming=True, pattern=r"\.repo"))
@wal.on(events.NewMessage(incoming=True, pattern=r"\.repo"))
@aaa.on(events.NewMessage(incoming=True, pattern=r"\.repo"))
@boy.on(events.NewMessage(incoming=True, pattern=r"\.repo"))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = RUDRA\n\nCommand:\n\n.rudra <count> <Username of User>\n\n.rudra <count> <reply to a User>\n\nCount must be a integer."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(yukki) == 2:
            message = str(yukki[1])
            print(message)
            a = await e.client.get_entity(message)
            g = a.id
            c = a.first_name
            username = f"[{c}](tg://user?id={g})"
            counter = int(yukki[0])
            for _ in range(counter):
                reply = random.choice(EAGLE)
                caption = f"{username} {reply}"
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.2)
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            c = b.first_name
            counter = int(yukki[0])
            username = f"[{c}](tg://user?id={g})"
            for _ in range(counter):
                reply = random.choice(EAGLE)
                caption = f"{username} {reply}"
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.2)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )




@idk.on(events.NewMessage(incoming=True))
@ydk.on(events.NewMessage(incoming=True))
@wdk.on(events.NewMessage(incoming=True))
@hdk.on(events.NewMessage(incoming=True))
@sdk.on(events.NewMessage(incoming=True))
@adk.on(events.NewMessage(incoming=True))
@bdk.on(events.NewMessage(incoming=True))
@cdk.on(events.NewMessage(incoming=True))
@edk.on(events.NewMessage(incoming=True))
@ddk.on(events.NewMessage(incoming=True))
@vkk.on(events.NewMessage(incoming=True))
@kkk.on(events.NewMessage(incoming=True))
@lkk.on(events.NewMessage(incoming=True))
@mkk.on(events.NewMessage(incoming=True))
@sid.on(events.NewMessage(incoming=True))
@shy.on(events.NewMessage(incoming=True))
@aan.on(events.NewMessage(incoming=True))
@ake.on(events.NewMessage(incoming=True))
@eel.on(events.NewMessage(incoming=True))
@khu.on(events.NewMessage(incoming=True))
@shi.on(events.NewMessage(incoming=True))
@yaa.on(events.NewMessage(incoming=True))
@dav.on(events.NewMessage(incoming=True))
@raj.on(events.NewMessage(incoming=True))
@put.on(events.NewMessage(incoming=True))
@eag.on(events.NewMessage(incoming=True))
@gle.on(events.NewMessage(incoming=True))
@wal.on(events.NewMessage(incoming=True))
@aaa.on(events.NewMessage(incoming=True))
@boy.on(events.NewMessage(incoming=True))


async def _(event):
    global que
    queue = que.get(event.sender_id)
    if not queue:
        return
    async with event.client.action(event.chat_id, "typing"):
        await asyncio.sleep(0.2)
    async with event.client.action(event.chat_id, "typing"):
        await event.client.send_message(
            entity=event.chat_id,
            message="""{}""".format(random.choice(RRAID)),
            reply_to=event.message.id,
        )               


async def get_chatinfo(event):
    chat = event.pattern_match.group(1)
    chat_info = None
    if chat:
        try:
            chat = int(chat)
        except ValueError:
            pass
    if not chat:
        if event.reply_to_msg_id:
            replied_msg = await event.get_reply_message()
            if replied_msg.fwd_from and replied_msg.fwd_from.channel_id is not None:
                chat = replied_msg.fwd_from.channel_id
        else:
            chat = event.chat_id
    try:
        chat_info = await event.client(GetFullChatRequest(chat))
    except:
        try:
            chat_info = await event.client(GetFullChannelRequest(chat))
        except ChannelInvalidError:
            await event.reply("`Invalid channel/group`")
            return None
        except ChannelPrivateError:
            await event.reply(
                "`This is a private channel/group or I am banned from there`"
            )
            return None
        except ChannelPublicGroupNaError:
            await event.reply("`Channel or supergroup doesn't exist`")
            return None
        except (TypeError, ValueError):
            await event.reply("`Invalid channel/group`")
            return None
    return chat_info


def user_full_name(user):
    names = [user.first_name, user.last_name]
    names = [i for i in list(names) if i]
    full_name = " ".join(names)
    return full_name


@idk.on(events.NewMessage(incoming=True, pattern=r"\.sudo"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.sudo"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.sudo"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.sudo"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.sudo"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.sudo"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.sudo"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.sudo"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.sudo"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.sudo"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.sudo"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.sudo"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.sudo"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.sudo"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.sudo"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.sudo"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.sudo"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.sudo"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.sudo"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.sudo"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.sudo"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.sudo"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.sudo"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.sudo"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.sudo"))
@eag.on(events.NewMessage(incoming=True, pattern=r"\.sudo"))
@gle.on(events.NewMessage(incoming=True, pattern=r"\.sudo"))
@wal.on(events.NewMessage(incoming=True, pattern=r"\.sudo"))
@aaa.on(events.NewMessage(incoming=True, pattern=r"\.sudo"))
@boy.on(events.NewMessage(incoming=True, pattern=r"\.sudo"))


async def get_users(event):
    sender = await event.get_sender()
    me = await event.client.get_me()
    if not sender.id == me.id:
        mafia = await event.edit(f"`Processing...`")
    else:
        h1m4n5hu0p = await get_chatinfo(event)
        chat = await event.get_chat()
        
    if event.is_private:
        return await event.edit("`Sorry, Cant add users here`")
    s = 0
    f = 0
    error = "None"

    await event.edit("**TerminalStatus**\n\n`Collecting Users.......`")
    async for user in event.client.iter_participants(h1m4n5hu0p.full_chat.id):
        try:
            if error.startswith("Too"):
                return await event.edit(
                    f"**Terminal Finished With Error**\n(`May Got Limit Error from telethon Please try agin Later`)\n**Error** : \n`{error}`\n\n• Invited `{s}` people \n• Failed to Invite `{f}` people"
                )
            await event.client(
                functions.channels.InviteToChannelRequest(channel=chat, users=[user.id])
            )
            s = s + 1
            await event.edit(
                f"**Terminal Running...**\n\n• Invited `{s}` people \n• Failed to Invite `{f}` people\n\n**× LastError:** `{error}`"
            )
        except Exception as e:
            error = str(e)
            f = f + 1
    return await event.edit(
        f"**Terminal Finished** \n\n• Successfully Invited `{s}` people \n• failed to invite `{f}` people"
    )









@idk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@eag.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@gle.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@wal.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@aaa.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@boy.on(events.NewMessage(incoming=True, pattern=r"\.ping"))

async def ping(e):
    if e.sender_id in SMEX_USERS:
        start = datetime.now()
        text = "RUK JA PING PONG KAR RAHA HU 🥵"
        event = await e.reply(text, parse_mode=None, link_preview=None )
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await event.edit(f"𖤍🇮 'Ꭺm °•✮•°🇧 ᏒᎾᏦᎬᏁ 𖤍  𓀠\n◤◢◣◥◤◢◣◥◤◢◣◥◤◢◣◥ ✘ 🇸 ᏢᎪm !\n\n`{ms}` 𝗺𝘀\n💥💥Տᑭᗴᗴᗪ ᑭᗩKKᗩᗪ ᗷᗩᗩᑭ KI ᑕᕼOᗪᗪᗴ💥💥")



        
        

@idk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@eag.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@gle.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@wal.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@aaa.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@boy.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
async def restart(e):
    if e.sender_id in SMEX_USERS:
        text = "𝙍𝙚𝙨𝙩𝙖𝙧𝙩𝙚𝙙\n\nPlease wait till it reboots..."
        await e.reply(text, parse_mode=None, link_preview=None )
        try:
            await idk.disconnect()
        except Exception as e:
            pass
        try:
            await ydk.disconnect()
        except Exception as e:
            pass
        try:
            await wdk.disconnect()
        except Exception as e:
            pass
        try:
            await hdk.disconnect()
        except Exception as e:
            pass
        try:
            await sdk.disconnect()
        except Exception as e:
            pass
        try:
            await adk.disconnect()
        except Exception as e:
            pass
        try:
            await bdk.disconnect()
        except Exception as e:
            pass
        try:
            await cdk.disconnect()
        except Exception as e:
            pass
        try:
            await ddk.disconnect()
        except Exception as e:
            pass
        try:
            await edk.disconnect()
        except Exception as e:
            pass
        try:
            await vkk.disconnect()
        except Exception as e:
            pass
        try:
            await kkk.disconnect()
        except Exception as e:
            pass
        try:
            await lkk.disconnect()
        except Exception as e:
            pass
        try:
            await mkk.disconnect()
        except Exception as e:
            pass
        try:
            await sid.disconnect()
        except Exception as e:
            pass
        try:
            await shy.disconnect()
        except Exception as e:
            pass
        try:
            await aan.disconnect()
        except Exception as e:
            pass
        try:
            await ake.disconnect()
        except Exception as e:
            pass
        try:
            await eel.disconnect()
        except Exception as e:
            pass
        try:
            await khu.disconnect()
        except Exception as e:
            pass
        try:
            await shi.disconnect()
        except Exception as e:
            pass
        try:
            await yaa.disconnect()
        except Exception as e:
            pass
        try:
            await dav.disconnect()
        except Exception as e:
            pass
        try:
            await raj.disconnect()
        except Exception as e:
            pass
        try:
            await put.disconnect()
        except Exception as e:
            pass
        try:
            await eag.disconnect()
        except Exception as e:
            pass
        try:
            await gle.disconnect()
        except Exception as e:
            pass
        try:
            await wal.disconnect()
        except Exception as e:
            pass
        try:
            await aaa.disconnect()
        except Exception as e:
            pass
        try:
            await boy.disconnect()
        except Exception as e:
            pass
        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()

        
        
        
        
        
@idk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@eag.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@gle.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@wal.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@aaa.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@boy.on(events.NewMessage(incoming=True, pattern=r"\.help"))

async def help(e):
    if e.sender_id in SMEX_USERS:
       text = "𝗔𝘃𝗮𝗶𝗹𝗮𝗯𝗹𝗲 𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀\n\n𝙐𝙩𝙞𝙡𝙨 𝘾𝙤𝙢𝙢𝙖𝙣𝙙:\n*ping\n*restart\n\n𝙐𝙨𝙚𝙧𝙗𝙤𝙩 𝘾𝙤𝙢𝙢𝙖𝙣𝙙:\n*bio\n*join\n*pjoin\n*leave\n\n𝙎𝙥𝙖𝙢 𝘾𝙤𝙢𝙢𝙖𝙣𝙙:\n*delayspam\n*bigspam\n*raid\n*mraid\n*sraid\n*craid\n\n\n©️ @RUDRA_XD_BAAP"
       await e.reply(text, parse_mode=None, link_preview=None )


print("BROKEN SPAM BOTS DEPLOY HO GAYE !!")
print("My Master ~ @RUDRA_XD_BAAP")
if len(sys.argv) not in (1, 3, 4):
    try:
        idk.disconnect()
    except Exception as e:
        pass
    try:
        ydk.disconnect()
    except Exception as e:
        pass
    try:
        wdk.disconnect()
    except Exception as e:
        pass
    try:
        hdk.disconnect()
    except Exception as e:
        pass
    try:
        sdk.disconnect()
    except Exception as e:
        pass
    try:
        adk.disconnect()
    except Exception as e:
        pass
    try:
        bdk.disconnect()
    except Exception as e:
        pass
    try:
        cdk.disconnect()
    except Exception as e:
        pass
    try:
        edk.disconnect()
    except Exception as e:
        pass
    try:
        ddk.disconnect()
    except Exception as e:
        pass
    try:
        vkk.disconnect()
    except Exception as e:
        pass 
    try:
        kkk.disconnect()
    except Exception as e:
        pass
    try:
        lkk.disconnect()
    except Exception as e:
        pass 
    try:
        mkk.disconnect()
    except Exception as e:
        pass
    try:
        sid.disconnect()
    except Exception as e:
        pass
    try:
        shy.disconnect()
    except Exception as e:
        pass
    try:
        aan.disconnect()
    except Exception as e:
        pass
    try:
        ake.disconnect()
    except Exception as e:
        pass
    try:
        eel.disconnect()
    except Exception as e:
        pass
    try:
        khu.disconnect()
    except Exception as e:
        pass
    try:
        shi.disconnect()
    except Exception as e:
        pass
    try:
        yaa.disconnect()
    except Exception as e:
        pass
    try:
        dav.disconnect()
    except Exception as e:
        pass
    try:
        raj.disconnect()
    except Exception as e:
        pass
    try:
        put.disconnect()
    except Exception as e:
        pass
    try:
        eag.disconnect()
    except Exception as e:
        pass
    try:
        gle.disconnect()
    except Exception as e:
        pass
    try:
        wal.disconnect()
    except Exception as e:
        pass
    try:
        aaa.disconnect()
    except Exception as e:
        pass
    try:
        boy.disconnect()
    except Exception as e:
        pass
else:
    try:
        idk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        ydk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        wdk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        hdk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        sdk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        adk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        bdk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        cdk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        edk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        ddk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        vkk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        kkk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        lkk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        mkk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        sid.run_until_disconnected()
    except Exception as e:
        pass
    try:
        shy.run_until_disconnected()
    except Exception as e:
        pass
    try:
        aan.run_until_disconnected()
    except Exception as e:
        pass
    try:
        ake.run_until_disconnected()
    except Exception as e:
        pass
    try:
        eel.run_until_disconnected()
    except Exception as e:
        pass
    try:
        khu.run_until_disconnected()
    except Exception as e:
        pass
    try:
        shi.run_until_disconnected()
    except Exception as e:
        pass
    try:
        yaa.run_until_disconnected()
    except Exception as e:
        pass
    try:
        dav.run_until_disconnected()
    except Exception as e:
        pass
    try:
        raj.run_until_disconnected()
    except Exception as e:
        pass
    try:
        put.run_until_disconnected()
    except Exception as e:
        pass
    try:
        eag.run_until_disconnected()
    except Exception as e:
        pass
    try:
        gle.run_until_disconnected()
    except Exception as e:
        pass
    try:
        wal.run_until_disconnected()
    except Exception as e:
        pass
    try:
        aaa.run_until_disconnected()
    except Exception as e:
        pass
    try:
        boy.run_until_disconnected()
    except Exception as e:
        pass


