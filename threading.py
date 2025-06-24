import threading
import requests
import time

def get_data_sync(urlss):
    start_time=time.time()#zaman modulünden başlangıç zamanını aldık
    json_array=[]#json formatındaki dosyaları buraya atcaz
    for url in urlss:
        json_array.append(requests.get(url).json())#attığımız reguestlerden gelen responsları alıp json formatında sakladık
    endtime=time.time()#bitiş zamanı
    elapsedtime=endtime-start_time#geçen zaman
    print("Execution time" ,elapsedtime)#
    return json_array
urls=["https://postman-echo.com/delay/4"]*5#bu site test amaçlı siteye verdiğimiz süre doğrultusunda açılan bir site
#şu an 4 saniyeye ayarladım 5 kerede bu siteden cevap alacağım 5*4 ten toplam 20 saniye geçer,kodda harcanan zamanı saymazsak
get_data_sync(urls)
