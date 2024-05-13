import requests
import smtplib
import time
from bs4 import BeautifulSoup

url = 'https://www.hepsiburada.com/apple-macbook-pro-m3-pro-18gb-512gb-ssd-macos-14-tasinabilir-bilgisayar-uzay-siyahi-mrx33tu-a-pm-HBC00005AIAHF'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}

def check_price():
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    # Ürün adını al
    title = soup.find(id='product-name').get_text().strip()
    title = title[:18]  # İlk 18 karakteri al
    print("Ürün Adı:", title)
    
    # Fiyatı al
    price_span = soup.find(id="offering-price").find("span", {"data-bind": "markupText:'currentPriceBeforePoint'"})
    price_text = price_span.get_text() if price_span else None
    if price_text:
        price = float(price_text.replace(".", "").replace(",", "."))  # Metin fiyatını sayıya dönüştür
        print("Fiyat:", price)
        
        if price < 84000:  # Fiyatı karşılaştır
            send_mail(title)

def send_mail(title):
    sender = 'ssumeyycakir@gmail.com'
    receiver = 'ssumeyycakir@hotmail.com'
    try:
        server = smtplib.SMTP('smtp.gmail.com' ,587)
        server.ehlo() 
        server.starttls()
        server.login(sender,'fuzk reof lzgo sl..') #Gmail uygulama şifresi al
        subject = title + ' istediğin fiyata düştü!!!'
        body = 'Bu linkten ulasabilirsin => ' + url
        mailContent = f"To:{receiver}\nFrom:{sender}\nSubject:{subject}\n\n{body}"
        mailContent = mailContent.encode('utf-8')  # UTF-8'ye dönüştür
        server.sendmail(sender,receiver,mailContent)
        print('Mail gönderildi')
    except smtplib.SMTPException as e:
        print(e)
    finally:
        server.quit()

while True:
    check_price()
    time.sleep(60*60)
