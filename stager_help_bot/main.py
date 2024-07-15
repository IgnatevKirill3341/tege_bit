from telebot import types
import telebot

BOT_TOKEN = '7315736947:AAH56zj9qJ8mZFVVBisrv-6x_5QEKr5d5HI'
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message, res=False):
    start_menu(message)
def start_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    price = types.KeyboardButton('💸 Ценники')
    diaga = types.KeyboardButton('⚒️ Диагностика')
    rout = types.KeyboardButton('🎹 Настройка роутеров')
    lk = types.KeyboardButton('👤 Личный кабинет')
    recs= types.KeyboardButton('🏦 Реквизиты')
    markup.add(price, rout, recs).row(diaga, lk)

    bot.send_message(message.chat.id, 'Начальное меню 🏠\nТыкни на нужное, пожалуйста 🥺\n', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def handle(message):
    if message.text.strip() == '💸 Ценники' :
        price_menu(message)
    elif message.text.strip() in ['🎰 Тарифы', '🛜 Подключение', '▶️ Возобновление', '🚚 Переезд']:
        price_handler(message)
    elif message.text.strip() in ['💯 Действующие Тарифы', '👨‍🦳 Архивные тарифы', '🤑 Акционные тарифы', '📺 Тарифы для кинчика']:
        handle_tarifs(message)
    elif message.text.strip() == '🔙 Назад':
        price_menu(message)
    elif message.text.strip() == "Домой 🏠":
        start_menu(message)
    elif message.text.strip() == "🎹 Настройка роутеров":
        rout_menu(message)
    elif message.text.strip() in [
    "ASUS",
    "Belkin",
    "D-link",
    "Huawei",
    "Level One",
    "LinkSys",
    "Mercusys",
    "MicroTik",
    "Netis",
    "SNR(InterZet)",
    "Tenda",
    "Totolink",
    "Tp-Link",
    "TRENDnet",
    "ZyXEL(Keenetic)",
    "UPVEL",
    "Xiaomi",
]:
        rout_handler(message)
    elif message.text.strip() == '⚒️ Диагностика':
        f=open('img/diag.png', 'rb')
        bot.send_document(chat_id=message.chat.id, document=f,caption='⚒️Диагностика вот\nПо ней делай, тимлид люлей не даст')
        f.close()
    elif message.text.strip() == "👤 Личный кабинет":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(types.InlineKeyboardButton('Ссылка на ЛК', url='https://lk.sknt.ru/login?back_url=/'))
        bot.send_message(message.chat.id, "👤 Личный кабинет \n🔒 ID: 63000 \n🔑 Пароль: 123\n‼️ Это тестовый аккаунт для ЛК\nЕго можно использовать, чтобы вести пользователя по ЛК\nВ ЛК НИЧЕГО НЕ МЕНЯТЬ!!!", reply_markup=keyboard)
    elif message.text.strip()=="🏦 Реквизиты":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(types.InlineKeyboardButton('Наш сайт', url='https://skynet.ru'))
        bot.send_message(message.chat.id, "🏦 SkyNet - делаем хорошо\n👨‍⚖️ ООО «СкайНэт» ИНН 7816223580\n📍 Репищева 20, БЦ «SkyTrade» (4 этаж), ежедневно 10-21", reply_markup=keyboard)

def price_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
    tar=types.KeyboardButton('🎰 Тарифы')
    podkluch=types.KeyboardButton('🛜 Подключение')
    pereezd=types.KeyboardButton('🚚 Переезд')
    vozob=types.KeyboardButton('▶️ Возобновление')
    back_button=types.KeyboardButton('Домой 🏠')
    markup.add(tar, pereezd,back_button).row(podkluch, vozob)
    bot.send_message(message.chat.id, "Дорого 💸", reply_markup=markup)

def price_handler(message):
    if message.text.strip()=='🎰 Тарифы':
        tarifs_menu(message)
    elif message.text.strip()=="🛜 Подключение":
        bot.send_message(message.chat.id, "🛜Подключение\nБесплатно: акционные тарифы, 100мбит/с любой абонемент, скоростные 180/360 дн.\n250р: 100мбит/с 30 дн.\n1500р: 8ми жилка при 100, скоростные 30/90 дн.")
    elif message.text.strip()=="🚚 Переезд":
        bot.send_message(message.chat.id, "🚚 Переезд\n250р: всегда\n1500р: не было 8ми жилки, скоростные 30/90 дн.")
    elif message.text.strip()=="▶️ Возобновление":
        bot.send_message(message.chat.id, "▶️ Возобновление\nБесплатно: акционные тарифы, 100мбит/с любой абонемент, скоростные 180/360 дн. (нет 8)\n250р: 100мбит/с 30 дн., скоростные 180/360 дн. (есть 8)\n1500р: 8ми жилка при 100, скоростные 30/90 дн.")

def tarifs_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    now_tar = types.KeyboardButton('💯 Действующие Тарифы')
    old_tar = types.KeyboardButton('👨‍🦳 Архивные тарифы')
    akc_tar = types.KeyboardButton('🤑 Акционные тарифы')
    tv_tar = types.KeyboardButton('📺 Тарифы для кинчика')
    back_button = types.KeyboardButton('Домой 🏠')
    back_button1=types.KeyboardButton('🔙 Назад')
    markup.add(now_tar, akc_tar).row(old_tar, tv_tar).row(back_button, back_button1)
    bot.send_message(message.chat.id, "А надобно какие? 🤔", reply_markup=markup)
def handle_tarifs(message):
    if message.text.strip() == '💯 Действующие Тарифы':
        f = open('img/Tarifs.png', 'rb')
        tarfs = f.read()
        f.close()
        bot.send_photo(message.chat.id, tarfs, caption='Действующие')
        bot.send_message(message.chat.id,
                         "При абонементах выгода 50 РУБ В МЕСЯЦ‼️\nт.е. Т-100 на месяц 650 руб.\n на 90 дней 600 \n на 180 - 550 \n на 365 - 500")
    elif message.text.strip() == '👨‍🦳 Архивные тарифы':
        f = open('img/old_tarifs.png', 'rb')
        old_tarfs = f.read()
        f.close()
        bot.send_photo(message.chat.id, old_tarfs, caption='Архивные(их поставить НИЗЯ)👨‍🦳')
        bot.send_message(message.chat.id,
                         "‼️Для тарифов, введенных в 2015 году («Вода», «Вода HD», «Огонь» и «Огонь HD») а также на тарифе «T-200 Pro.2023» по окончании оплаченного периода изменится стоимость, можно оставаться на старых тарифах либо выбрать актуальный в Личном кабинете ")
    elif message.text.strip() == '🤑 Акционные тарифы':
        f = open('img/Akcii.png', 'rb')
        akcii = f.read()
        f.close()
        bot.send_photo(message.chat.id, akcii,caption='🤑 Акционные тарифы. ТОЛЬКО ДЛЯ НОВЫХ ПОЛЬЗОВАТЕЛЕЙ‼️\n Если будут вопросы по типу: \"A если я заключу договор на кого-то еще, то будет мне доступен акционный тариф?\"\n Говори, что по акционные тарифы у нас закрепляются за адресом и вопросов наверна не будет \n¯\\_(ツ)_/¯ ')
    elif message.text.strip() == '📺 Тарифы для кинчика':
        f = open('img/Media.png', 'rb')
        f1 = open('img/TV.png', 'rb')
        f3 = open('img/dop_tv.png', 'rb')
        media = f.read()
        tv = f1.read()
        dop_tv=f3.read()
        f.close()
        f1.close()
        photos = [types.InputMediaPhoto(media), types.InputMediaPhoto(tv), types.InputMediaPhoto(dop_tv)]
        bot.send_media_group(message.chat.id, photos)
        bot.send_message(message.chat.id, "Вот все тарифы для просмотра ТВхи 📺")

def rout_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    asus=types.KeyboardButton('ASUS')
    belkin=types.KeyboardButton('Belkin')
    dlink=types.KeyboardButton('D-link')
    huawei=types.KeyboardButton('Huawei')
    lvlone=types.KeyboardButton('Level One')
    linksys=types.KeyboardButton('LinkSys')
    mercusys=types.KeyboardButton('Mercusys')
    microtik=types.KeyboardButton('MicroTik')
    netis=types.KeyboardButton('Netis')
    snr=types.KeyboardButton('SNR(InterZet)')
    tenda=types.KeyboardButton('Tenda')
    Totolink=types.KeyboardButton('Totolink')
    tplink=types.KeyboardButton('Tp-Link')
    trendnet=types.KeyboardButton('TRENDnet')
    keenetic=types.KeyboardButton('ZyXEL(Keenetic)')
    upvel=types.KeyboardButton('UPVEL')
    xiaomi=types.KeyboardButton('Xiaomi')
    back_button = types.KeyboardButton('Домой 🏠')
    markup.add(asus,belkin, dlink, huawei, lvlone, linksys, mercusys, microtik, netis, snr,  tenda, Totolink, tplink, trendnet, keenetic, upvel, xiaomi).row(back_button)
    bot.send_message(message.chat.id, "🎹 Настройка роутеров\nТут много эмуляторов: https://borisenkonikolay.ru/\nПодробнее по кнопочкам", reply_markup=markup)

def rout_handler(message):
    if message.text.strip()=="ASUS":
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton('Чёрная', url='https://demoui.asus.com/RU/'),types.InlineKeyboardButton('Синяя',url='https://event.asus.com/2009/networks/dummy_ui/ru/index.html'))
        bot.send_message(message.chat.id, "Шлюз: 192. 168.1.1\nЛогин: admin\nПароль: admin\nЭмуляторы:", reply_markup=keyboard)
    elif message.text.strip()=="Belkin":
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton('Эмулятор', url='https://ui.belkin.com/'))
        bot.send_message(message.chat.id, "Шлюз: 192. 168.1.1\nПароль: пустой (без пароля)",reply_markup=keyboard)
    elif message.text.strip()=="D-link":
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton('Эмуляторы', url='https://www.dlink.ru/ru/arts/84.html'))
        bot.send_message(message.chat.id, "Шлюз: 192.168.0.1 или 192.168.1.1\nЛогин: admin\nПароль: admin или пустой (без пароля)\nMac-адрес: указан на наклейке, на корпусе роутера.", reply_markup=keyboard)
    elif message.text.strip()=="Huawei":
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton('Экспертка', url='https://skygrade.skynet.ru/mod/glossary/showentry.php?courseid=11&eid=403&displayformat=dictionary#h5pbookid=298&chapter=h5p-interactive-book-chapter-e36236ca-307a-45a2-b56b-398de12e67ae&section=0'))
        bot.send_message(message.chat.id, "Писать много, смотри в ЭС тут: ", reply_markup=keyboard)
    elif message.text.strip()=="Level One":
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton('Эмулятор1', url='https://www.dlink.ru/ru/arts/84.html'),types.InlineKeyboardButton('Эмулятор2', url='http://support.smile-net.ru/internet_help/configuring_cpe/levelone/wbr_3408_wbr_6002/'))

        bot.send_message(message.chat.id, "Шлюз: 192.168.0.1\nЛогин: admin\nПароль: password", reply_markup=keyboard)
    elif message.text.strip()=="LinkSys":
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton('Эмулятор', url='https://ui.linksys.com/'))
        bot.send_message(message.chat.id, "Шлюз: 192.168.1.1\nЛогин: admin\nПароль: admin", reply_markup=keyboard)
    elif message.text.strip()=="Mercusys":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(types.InlineKeyboardButton('Инструкция', url='https://help-wifi.com/mercusys/kak-podklyuchit-i-nastroit-router-mercusys-mw325r/'),types.InlineKeyboardButton('Эмуляторы', url='https://www.mercusys.com/ru/support/simulator'))
        bot.send_message(message.chat.id, "Шлюз: 192.168.1.1 или https://mwlogin.net/\nЛогин: \nПароль: ", reply_markup=keyboard)
    elif message.text.strip()=="MicroTik":
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton('Эмулятор', url='https://demo.mt.lv/'))
        keyboard.add(types.InlineKeyboardButton('Инстуркция по лёгкой прошивке', url='https://spw.ru/educate/articles/new_user/'))
        keyboard.add(types.InlineKeyboardButton('Инструкция по тяжелой прошивке', url='https://habr.com/ru/articles/227913/'))
        bot.send_message(message.chat.id, "Шлюз: 192.168.88.1\nСтандартная авторизация по логину и паролю отсутствует", reply_markup=keyboard)
    elif message.text.strip()=="Netis":
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton('Эмулятор', url='https://www.netisru.com/Suppory/emulators.html'))
        bot.send_message(message.chat.id, "Шлюз: 192.168.1.1 или https://netis.cc/ \n на новых устройствах может быть 192.168.1.254\nЛогин: guest\nПароль: guest@XXXX, где ХХХХ последние четыре цифры MAC- адреса роутера.", reply_markup=keyboard)
    elif message.text.strip()=="SNR(InterZet)":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(types.InlineKeyboardButton('Эмулятор', url='https://routers.wtf/emul/SNRM%20OFFLINE/SNR/home.html'),
        types.InlineKeyboardButton('Эмулятор InterZet', url='https://routers.wtf/emul/SNR%20OFFLINE/SNR/home.html'),
                     )
        keyboard.add(types.InlineKeyboardButton('Инструкция', url='https://netintel.ru/index.php?id=76'))
        bot.send_message(message.chat.id, "Шлюз: 172.16.172.1\nЛогин Admin/root\nПароль: whOoOwd2", reply_markup=keyboard)
    elif message.text.strip()=="Tenda":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(types.InlineKeyboardButton('Эмуляторы', url='https://www.tendacn.com/ru/simulator/default.html'))
        keyboard.add(types.InlineKeyboardButton('Инструкция1(новая прошивка)', url='https://help-wifi.com/tenda/bystraya-nastrojka-marshrutizatora-tenda-ac9-ac1200/'))
        keyboard.add(types.InlineKeyboardButton('Инструкция2(старая прошивка)', url='https://help-wifi.com/tenda/nastrojka-routera-tenda-n301/'))
        keyboard.add(types.InlineKeyboardButton('Инструкция3(очень старая прошивка)', url='https://help-wifi.com/tenda/nastrojka-routera-tenda-n3-podklyuchaem-internet-nastraivaem-wi-fi-set-i-parol/'))
        bot.send_message(message.chat.id, "Шлюз: 192.168.0.1\nЛогин admin\nПароль: admin", reply_markup=keyboard)
    elif message.text.strip()=="Totolink":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(types.InlineKeyboardButton('Эмулятор', url='https://totolink.ru/texpodderzhka/web-emulyator.html?ysclid=lyiuqbr3hp120087651'),
                     types.InlineKeyboardButton('Инструкция', url='https://help-wifi.com/totolink/nastrojka-routera-totolink-n150rt-poshagovaya-instrukciya/')
        )
        bot.send_message(message.chat.id, "Шлюз: 192.168.1.1\nЛогин admin\nПароль: admin", reply_markup=keyboard)
    elif message.text.strip()=="Tp-Link":
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton('Эмулятор', url='https://www.tp-link.com/ru/support/emulator/'))
        bot.send_message(message.chat.id, "Шлюз: 192.168.1.1 или 192.168.0.1\nЛогин admin\nПароль: admin", reply_markup=keyboard)
    elif message.text.strip()=="TRENDnet":
        bot.send_message(message.chat.id, "Шлюз: 192.168.10.1\nЛогин admin\nПароль: admin")
    elif message.text.strip()=="ZyXEL(Keenetic)":
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton('Эмулятор1', url='https://routers.wtf/emul/ZUXEL%20OFFLINE/index.html'),
                     types.InlineKeyboardButton('Эмулятор2', url='https://routers.wtf/emul/ZUXEL%20v2%20OFFLINE/index.html'),
                     types.InlineKeyboardButton('Эмулятор3', url='https://routers.nvbs.ru/zyxel/NDMSv2_by_Anna/status.html'),
                     types.InlineKeyboardButton('Эмулятор4', url='https://routers.wtf/emul/Zyxel_nbg334wee/index.html')
                     )
        keyboard1 = types.InlineKeyboardMarkup()
        keyboard1.add(types.InlineKeyboardButton('Эмулятор', url='http://46.55.21.66/login#goto=%2Fdashboard'))
        bot.send_message(message.chat.id, "Шлюз: 192.168.1.1\nЛогин admin\nПароль: 1234", reply_markup=keyboard)
        bot.send_message(message.chat.id, "Для Keenetic ultra(новый)\n Логин: user \n Пароль: user12345678", reply_markup=keyboard1)
        bot.send_message(message.chat.id, "У некоторых новых роутеров Keenetic определение линка по индикаторам можно назвать интересным квестом. У них нет индикатора \"0\". На некоторых моделях есть \"планета\", которая загорается только тогда, когда есть интернет. Наличие линка можно проверить на порту самого роутера (со стороны, где подведены интернет-кабель и питание). А на Keenetic Start, к примеру, на портах индикации нет. На более дорогих моделях - есть.  Для правильной диагностики внимательно смотри на статусы в биллинге. Можно зайти в интерфейс роутера и посмотреть состояние соединения там (в том числе проверить mac, приходит ли ip и так далее).")
    elif message.text.strip() == "UPVEL":
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton('Эмулятор', url='http://linserv.ru/?ysclid=lyiv6kdpan81895634#'))
        bot.send_message(message.chat.id, "Шлюз: 192. 168.10.1\nЛогин: admin \n Пароль: admin", reply_markup=keyboard)
    elif message.text.strip() == "Xiaomi":
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton('Инструкция', url='https://help-wifi.com/xiaomi/nastrojka-routera-xiaomi-mini-wifi-podrobnaya-instrukciya/'))
        keyboard.add(types.InlineKeyboardButton('Инструкция (прошивка на англ.яз)', url='https://help-wifi.com/xiaomi/podklyuchenie-i-nastrojka-xiaomi-mi-wi-fi-router-3/'))
        bot.send_message(message.chat.id, "Шлюз: 192.168.31.1 или miwifi.com\nЛогин и пароль задаются при первой настройке, задается далее", reply_markup=keyboard)

bot.polling(none_stop=True, interval=0)