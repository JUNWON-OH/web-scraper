import os
import requests
from bs4 import BeautifulSoup

URL = "https://www.iban.com/currency-codes"
currency = ["from", "to"]


def ask_amount():
    try:
        user_amount = int(
            input(f"\nHow many{currency[0]} do you want to convert to {currency[1]}?"))
        exchange_URL = f"https://transferwise.com/gb/currency-converter/{currency[0]}-to-{currency[1]}-rate?amount={user_amount}"
        exchange_status = requests.get(exchange_URL)
        if exchange_status.status_code != 200:
            print("\nYour Country or Chosen Country doesn't support.\nInput again.")
            ask_from(country)
        result = requests.get(exchange_URL)
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class": "input-group"})
        for result in results:
            result_input = result.find("input")
            if "js-TargetAmount" in result_input["class"]:
                print(
                    f'{currency[0]} {user_amount} is {currency[1]} {result_input["value"]}')
    except ValueError:
        print("That wasn't a number")
        ask_amount()


def ask_to(country):
    try:
        user_to = int(input("\nNow choose another country\n\n#: "))
        if user_to not in range(1, len(country)):
            print("Choose a number from the list.")
            ask_to(country)
        else:
            print(country[user_to][0])
            currency[1] = country[user_to][1]
            ask_amount()
    except ValueError:
        print("That wasn't a number.")
        ask_to(country)


def ask_from(country):
    try:
        user_from = int(
            input("\nwhere are you from? Choose a country by number.\n\n#: "))
        if user_from not in range(1, len(country)):
            print("Choose a number from the list.")
            ask_from(country)
        else:
            print(country[user_from][0])
            currency[0] = country[user_from][1]
            ask_to(country)
    except ValueError:
        print("That wasn't a number.")
        ask_from(country)


print("Hello! Please choose select a country by number:")
URL_request = requests.get(URL)
soup = BeautifulSoup(URL_request.text, "html.parser")
trs = soup.find_all("tr")
country = {}
i = 0
for tr in trs[1:]:
    tds = tr.find_all("td")
    if tds[1].string != "No universal currency":
        i += 1
        country[i] = [tds[0].string, tds[2].string]
for i in range(1, len(country)+1):
    print(f"# {i} {country[i][0]}")

ask_from(country)
