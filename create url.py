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

billData = {
    'bill_time': '01.01.21 / 18:50:46',
    'restaurant_name': 'БУКОВЕЛЬ',
    'items': [
        {
            'name': 'Салат "Бурячок"',
            'amount': '200г',
            'price': 130.0,
            'quantity': 1
        },
        {
            'name': 'Овочі гриль цілі',
            'amount': '100г',
            'price': 125.0,
            'quantity': 2
        },
        {
            'name': 'Kaiser 0,5л',
            'amount': '',
            'price': 135.0,
            'quantity': 1
        },
        {
            'name': 'Капучіно',
            'amount': '',
            'price': 85.0,
            'quantity': 1
        },
        {
            'name': 'Кана амерікано',
            'amount': '',
            'price': 65.0,
            'quantity': 1
        },
        {
            'name': 'Узвар 250мл',
            'amount': '',
            'price': 65.0,
            'quantity': 1
        },
        {
            'name': 'Сік в асортименті',
            'amount': '250г',
            'price': 65.0,
            'quantity': 1
        },
        {
            'name': 'Лаваш із сиром та бринзою',
            'amount': '1пор',
            'price': 110.0,
            'quantity': 1
        },
        {
            'name': 'Салат "Грецький"',
            'amount': '250г',
            'price': 210.0,
            'quantity': 1
        },
        {
            'name': 'Хліб',
            'amount': '1 кус',
            'price': 210.0,
            'quantity': 1
        },
        {
            'name': 'Шашлик курячий',
            'amount': '100г',
            'price': 125.0,
            'quantity': 1
        },
        {
            'name': 'Картопля запечена на мангалі',
            'amount': '300гр',
            'price': 250.0,
            'quantity': 1
        },
        {
            'name': 'Салат "З капусти"',
            'amount': '150г',
            'price': 3.0,
            'quantity': 1
        },
        {
            'name': 'Курячий бульйон',
            'amount': '300г',
            'price': 15.0,
            'quantity': 1
        },
        {
            'name': 'Чай Альпійський луг',
            'amount': '',
            'price': 215.0,
            'quantity': 1
        },
        {
            'name': 'Хріновуха',
            'amount': '',
            'price': 520.0,
            'quantity': 1
        },
        {
            'name': 'Картопля "По-домашньому"',
            'amount': '',
            'price': 215.0,
            'quantity': 1
        },
        {
            'name': 'Пампушка з часничком',
            'amount': '',
            'price': 95.0,
            'quantity': 1
        },
        {
            'name': 'Борщ український',
            'amount': '300г',
            'price': 95.0,
            'quantity': 1
        },
        {
            'name': 'Ребра BBQ',
            'amount': '300г',
            'price': 1000.0,
            'quantity': 0.1
        },
        {
            'name': 'Форель у прованських травах',
            'amount': '100r',
            'price': 250.0,
            'quantity': 1
        },
        {
            'name': 'Ковбаски гриль "Кайзер"',
            'amount': '',
            'price': 190.0,
            'quantity': 1
        },
        {
            'name': 'Рулька свинна з тушкованою капустою',
            'amount': '',
            'price': 130.0,
            'quantity': 1
        },
        {
            'name': 'Ціна К-ть',
            'amount': '',
            'price': 250.0,
            'quantity': 5
        },
        {
            'name': 'ПОПЕРЕДНІЙ РАХУНОК # 69',
            'amount': '',
            'price': 15.0,
            'quantity': 1
        }
    ]
}

billData = {
    "bill_time": "19.08.2023 7:53",
    "restaurant_name": "Stout",
    "items": [
        {
            "name": "\u041f\u0438\u0432\u043e \u0448\u043e \u0421\u0443\u0445\u0438\u0439 \u0427\u043e\u0440\u043d\u0438\u0439",
            "amount": "0.4",
            "price": 120.0,
            "quantity": 1.0
        },
        {
            "name": "\u041f\u0438\u0432\u043e 2085* Reberbar heles",
            "amount": "0.4",
            "price": 240.0,
            "quantity": 3.0
        },
        {
            "name": "\u041f\u0438\u0432\u043e Hopkins",
            "amount": "0.4",
            "price": 95.0,
            "quantity": 1.0
        },
        {
            "name": "\u0420\u0435\u0431\u0435\u0440 \u0441\u0435\u0442 new",
            "amount": "",
            "price": 1650.0,
            "quantity": 1.0
        },
        {
            "name": "\u041f\u0438\u0432\u043e 2085- Organic Cider",
            "amount": "0.4",
            "price": 437.5,
            "quantity": 2.5
        },
        {
            "name": "\u041f\u0438\u0432\u043e 2085* Reberbar heles",
            "amount": "0.4",
            "price": 80.0,
            "quantity": 1.0
        },
        {
            "name": "\u041f\u0438\u0432\u043e Hrew Brew Vertigo",
            "amount": "0.4",
            "price": 130.0,
            "quantity": 1.0
        }
    ]
}

billData = {
    "bill_time": "19.08.2023 7:53",
    "restaurant_name": "Stout",
    "items": [
        {
            "name": "\u041f\u0438\u0432\u043e \u0448\u043e \u0421\u0443\u0445\u0438\u0439 \u0427\u043e\u0440\u043d\u0438\u0439",
            "amount": "0.4",
            "quantity": 1,
            "sum": 80.0
        },
        {
            "name": "\u041f\u0438\u0432\u043e 2085* Reberbar heles",
            "amount": "0.4",
            "quantity": 3,
            "sum": 240.0
        },
        {
            "name": "\u041f\u0438\u0432\u043e Hopkins",
            "amount": "0.4",
            "quantity": 1,
            "sum": 95.0
        },
        {
            "name": "\u0420\u0435\u0431\u0435\u0440 \u0441\u0435\u0442 new",
            "amount": "",
            "quantity": 1,
            "sum": 1650.0
        },
        {
            "name": "\u041f\u0438\u0432\u043e 2085- Organic Cider",
            "amount": "0.4",
            "quantity": 2.5,
            "sum": 437.5
        },
        {
            "name": "\u041f\u0438\u0432\u043e 2085* Reberbar heles",
            "amount": "0.4",
            "quantity": 1,
            "sum": 80.0
        },
        {
            "name": "\u041f\u0438\u0432\u043e Hrew Brew Vertigo",
            "amount": "0.4",
            "quantity": 1,
            "sum": 130.0
        }
    ]
}

billData = {
    "bill_time": "19:08, 19.08.2023",
    "restaurant_name": "REBERBAR",
    "items": [
        {
            "name": "Пиво Що Сухий Чорни",
            "amount": "0.4",
            "quantity": 1,
            "sum": 120.00
        },
        {
            "name": "Пиво 2085* Reberbar heles",
            "amount": "0.4",
            "quantity": 3,
            "sum": 240.00
        },
        {
            "name": "Пиво Hops ink 0.4",
            "amount": "0.4",
            "quantity": 1,
            "sum": 95.00
        },
        {
            "name": "Ребер Сет new",
            "amount": "",
            "quantity": 1,
            "sum": 650.00
        },
        {
            "name": "Пиво 2085- Organic Cider",
            "amount": "0.4",
            "quantity": 2.5,
            "sum": 437.50
        },
        {
            "name": "Пиво 2085* Reberbar heles",
            "amount": "0.4",
            "quantity": 1,
            "sum": 80.00
        },
        {
            "name": "Пиво Hrew Brew Vertigo",
            "amount": "0.4",
            "quantity": 1,
            "sum": 130.00
        }
    ]
}

billData = {'restaurant_name': 'КАФЕ "Ч1А Чін"', 'bill_time': '04.11.2023 18:20:29',
            'items': [{'name': 'ВП-Тайська локшина з куркою', 'quantity': '1.000', 'price': '154.00'},
                      {'name': 'Локшина з куркою', 'quantity': '1.000', 'price': '187.00'},
                      {'name': 'Рербі 0.33 бан', 'quantity': '1.000', 'price': '43.00'}], 'total': '384.00'}

json_data = json.dumps(billData)

if __name__=='__main__':
    # Encode the data to be URL-friendly
    encoded_data = urllib.parse.quote_plus(json_data)

    # Add the encoded data to the URL as a query parameter
    web_app_url = f"http://localhost:63342/pages/webapp.html?data={encoded_data}"
    web_app_url = f"http://localhost:63342/pages/updated_webapp.html?data={encoded_data}"
    web_app_url = f"http://localhost:63342/pages/updated_webapp_editable.html?data={encoded_data}"
    # web_app_url = f"http://localhost:63342/pages/updated_webapp_with_modern_css.html?data={encoded_data}"



    print(web_app_url)
