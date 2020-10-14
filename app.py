import requests

def input_num(number):
    while True:
        try:
            user = int(input(number))
        except ValueError:
            print("Just Number!!!")
            continue
        else:
            return user
            break

def convertAPI(my_currency, values):
    url = 'http://apilayer.net/api/'
    endpoint = 'live'
    access_key = '218f1a27039461825ab637fa634f5c45'
    my_currency = my_currency
    complete_url = url + endpoint + "?access_key=" + access_key + "&currencies=" + my_currency
    response = requests.get(complete_url)
    data = response.json()
    convert_list = list(data.values())
    get_index = convert_list[5]
    list_num = list(get_index.values())
    float_num = list_num[0]
    print(f"The Result: {float_num*values}")

#main code
print("Welcome To Money Converter")
print("Default values is USD")
user_money = input("Put Your Currency: ")
money_quantity = input_num("How many USD you want?: ")
print("loading")
convertAPI(user_money, money_quantity)