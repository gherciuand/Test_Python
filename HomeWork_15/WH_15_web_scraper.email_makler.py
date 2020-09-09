from pyquery import PyQuery as pq
import json

cat_target = 'https://makler.md/ru/real-estate/real-estate-for-sale'


def decodeEmail(e):
    dec_email = ""
    k = int(e[:2], 16)
    for i in range(2, len(e) - 1, 2):
        dec_email += chr(int(e[i:i + 2], 16) ^ k)
    return dec_email


def scanOneAdMaklerPage(target_url):
    document = pq(url=target_url)
    user_id = document('.item_about').find('.item_sipmleUser').text()
    hading = document('h1').text()
    phones = document('#item_phones').text().replace(" ", "")
    cod_email = document('.hlist').find('a').attr('data-cfemail')
    email = decodeEmail(cod_email)
    # image = document('.main-image').find('img').attr('src')
    print(user_id)
    print(phones)
    print(email)
    return {
        'title': hading,
        'user': user_id,
        'email': email,
        'phone': phones
    }


def scanOneCatMaklerPage(target_url):
    prefix = 'https://makler.md'
    document = pq(url=target_url)
    adds = []

    links_to_ads = document('article').find('.ls-detail_anUrl')
    for link in links_to_ads:
        try:
            url = pq(link).attr('href')
            adds.append(scanOneAdMaklerPage(prefix + url))
        except:
            pass
    return adds


num_pages = 1
index = '?page='
for n in range(num_pages):
    adds = scanOneCatMaklerPage(cat_target + index + str(n))
    n += 1
    file_name = f'./subscribers.json'
    file = open(file_name, 'w', encoding='utf-8')
    json.dump(adds, file, indent=2, ensure_ascii=False)
