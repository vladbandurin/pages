import json
import urllib.parse

billData = {
    "restaurant": {
        "name": "BLUSH",
        "INN": "7703400647"
    },
    "bank_guarantees": {
        "name": "БАНКОВСКИЕ ГАРАНТИИ",
        "number": "24",
        "capital": "СТОЛИЦА"
    },
    "guest_bill": {
        "table": "14",
        "order_number": "20512",
        "hall": "1. Основной зал",
        "opened": "16.11.2019 16:20",
        "waiter": "ЛюбЧУК Д.",
        "items": [
            {
                "name": "Velvet Season Саперави",
                "amount": "150 мл",
                "price": "230.00",
                "quantity": "1"
            },
            {
                "name": "Домен Гобельсбург Грюнер Ве",
                "amount": "150 мл",
                "price": "390.00",
                "quantity": "1"
            },
            {
                "name": "Плато сыров",
                "price": "990.00",
                "quantity": "1"
            },
            {
                "name": "Белая треска с пюре из сель",
                "price": "690.00",
                "quantity": "1"
            },
            {
                "name": "Паста с кроликом",
                "price": "430.00",
                "quantity": "1"
            }
        ],
        "total": "2730.00",
        "tip_suggestions": {
            "satisfactory": "52 РУБ.",
            "good": "273 РУБ.",
            "excellent": "410 РУБ."
        },
        "suggestions_email": "guestblush2@gmail.com",
        "thank_you_note": "СПАСИБО! ЖДЕМ ВАС СНОВА!"
    }

}

# Convert the data to a JSON string
json_data = json.dumps(billData)

# Encode the data to be URL-friendly
encoded_data = urllib.parse.quote_plus(json_data)

# Add the encoded data to the URL as a query parameter
web_app_url = f"http://localhost:63342/pages/webapp.html?data={encoded_data}"

print(web_app_url)