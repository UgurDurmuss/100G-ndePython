import requests#pythonda apıler den veri çekmemizi sağlayan bir kütüphane


def get_crypto_data():
    response = requests.get(url="https://raw.githubusercontent.com/atilsamancioglu/K21-JSONDataSet/master/crypto.json")
    return response.json()#aldığımız verileri bir json formatında sakladık
    # print(response.status_code)#
    # for crypto in response.json():
    #    print(crypto["price"])
    #    print(crypto["currency"])


crypto_response = get_crypto_data()
user_input = input("Enter your favorite crypto: ")
for crypto in crypto_response:
    if crypto["currency"] == user_input:
        print(crypto["price"])
