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


#
# billData = {
#     "bill_time": "01.01.21 / 18:50:46",
#     "restaurant_name": "\u0411\u0423\u041a\u041e\u0412\u0415\u041b\u042c",
#     "items": [
#         {
#             "name": "\u0421\u0430\u043b\u0430\u0442 \"\u0411\u0443\u0440\u044f\u0447\u043e\u043a\" 200\u0433",
#             "amount": "200g",
#             "quantity": 1,
#             "sum": 130.0
#         },
#         {
#             "name": "\u041e\u0432\u043e\u0447\u0456 \u0433\u0440\u0438\u043b\u044c \u0446\u0456\u043b\u0456 100\u0433",
#             "amount": "100g",
#             "quantity": 2,
#             "sum": 260.0
#         },
#         {
#             "name": "Kaiser 0,5\u043b",
#             "amount": "0.5l",
#             "quantity": 1,
#             "sum": 135.0
#         },
#         {
#             "name": "\u041a\u0430\u043f\u0443\u0447\u0456\u043d\u043e",
#             "amount": "",
#             "quantity": 1,
#             "sum": 85.0
#         },
#         {
#             "name": "\u041a\u0430\u043d\u0430 \u0430\u043c\u0435\u0440\u0456\u043a\u0430\u043d\u043e",
#             "amount": "",
#             "quantity": 1,
#             "sum": 65.0
#         },
#         {
#             "name": "\u0423\u0437\u0432\u0430\u0440 250\u043c\u043b",
#             "amount": "250ml",
#             "quantity": 1,
#             "sum": 65.0
#         },
#         {
#             "name": "\u0421\u0456\u043a \u0432 \u0430\u0441\u043e\u0440\u0442\u0438\u043c\u0435\u043d\u0442\u0456 250\u0433",
#             "amount": "250g",
#             "quantity": 1,
#             "sum": 110.0
#         },
#         {
#             "name": "\u041b\u0430\u0432\u0430\u0448 \u0456\u0437 \u0441\u0438\u0440\u043e\u043c \u0442\u0430 \u0431\u0440\u0438\u043d\u0437\u043e\u044e 1\u043f\u043e\u0440",
#             "amount": "200g",
#             "quantity": 1,
#             "sum": 210.0
#         },
#         {
#             "name": "\u0421\u0430\u043b\u0430\u0442 \"\u0413\u0440\u0435\u0446\u044c\u043a\u0438\u0439\" 250\u0433",
#             "amount": "250g",
#             "quantity": 1,
#             "sum": 215.0
#         },
#         {
#             "name": "\u0425\u043b\u0456\u0431 1 \u043a\u0443\u0441",
#             "amount": "",
#             "quantity": 1,
#             "sum": 95.0
#         },
#         {
#             "name": "\u0428\u0430\u0448\u043b\u0438\u043a \u043a\u0443\u0440\u044f\u0447\u0438\u0439 100\u0433",
#             "amount": "100g",
#             "quantity": 1,
#             "sum": 95.0
#         },
#         {
#             "name": "\u041a\u0430\u0440\u0442\u043e\u043f\u043b\u044f \u0437\u0430\u043f\u0435\u0447\u0435\u043d\u0430 \u043d\u0430 \u043c\u0430\u043d\u0433\u0430\u043b\u0456 300\u0433\u0440",
#             "amount": "300g",
#             "quantity": 1,
#             "sum": 1000.0
#         },
#         {
#             "name": "\u0421\u0430\u043b\u0430\u0442 \"\u0417 \u043a\u0430\u043f\u0443\u0441\u0442\u0438\" 150\u0433",
#             "amount": "150g",
#             "quantity": 1,
#             "sum": 250.0
#         },
#         {
#             "name": "\u041a\u0443\u0440\u044f\u0447\u0438\u0439 \u0431\u0443\u043b\u044c\u0439\u043e\u043d 300\u0433",
#             "amount": "300g",
#             "quantity": 1,
#             "sum": 190.0
#         },
#         {
#             "name": "\u0427\u0430\u0439 \u0410\u043b\u044c\u043f\u0456\u0439\u0441\u044c\u043a\u0438\u0439 \u043b\u0443\u0433",
#             "amount": "",
#             "quantity": 1,
#             "sum": 130.0
#         },
#         {
#             "name": "\u0425\u0440\u0456\u043d\u043e\u0432\u0443\u0445\u0430",
#             "amount": "",
#             "quantity": 1,
#             "sum": 250.0
#         },
#         {
#             "name": "\u041a\u0430\u0440\u0442\u043e\u043f\u043b\u044f \"\u041f\u043e-\u0434\u043e\u043c\u0430\u0448\u043d\u044c\u043e\u043c\u0443\"",
#             "amount": "",
#             "quantity": 1,
#             "sum": 135.0
#         },
#         {
#             "name": "\u041f\u0430\u043c\u043f\u0443\u0448\u043a\u0430 \u0437 \u0447\u0430\u0441\u043d\u0438\u0447\u043a\u043e\u043c",
#             "amount": "",
#             "quantity": 1,
#             "sum": 65.0
#         },
#         {
#             "name": "\u0411\u043e\u0440\u0449 \u0443\u043a\u0440\u0430\u0457\u043d\u0441\u044c\u043a\u0438\u0439 300\u0433",
#             "amount": "300g",
#             "quantity": 1,
#             "sum": 110.0
#         },
#         {
#             "name": "\u0420\u0435\u0431\u0440\u0430 BBQ 300\u0433",
#             "amount": "300g",
#             "quantity": 2,
#             "sum": 420.0
#         },
#         {
#             "name": "\u0424\u043e\u0440\u0435\u043b\u044c \u0443 \u043f\u0440\u043e\u0432\u0430\u043d\u0441\u044c\u043a\u0438\u0445 \u0442\u0440\u0430\u0432\u0430\u0445 100g",
#             "amount": "100g",
#             "quantity": 1,
#             "sum": 210.0
#         },
#         {
#             "name": "\u041a\u043e\u0432\u0431\u0430\u0441\u043a\u0438 \u0433\u0440\u0438\u043b\u044c \"\u041a\u0430\u0439\u0437\u0435\u0440\"",
#             "amount": "",
#             "quantity": 5,
#             "sum": 250.0
#         },
#         {
#             "name": "\u0420\u0443\u043b\u044c\u043a\u0430 \u0441\u0432\u0438\u043d\u043d\u0430 \u0437 \u0442\u0443\u0448\u043a\u043e\u0432\u0430\u043d\u043e\u044e \u043a\u0430\u043f\u0443\u0441\u0442\u043e\u044e",
#             "amount": "",
#             "quantity": 15,
#             "sum": 150.0
#         }
#     ]
# }
#
# billData = {
#     "bill_time": "01.01.21 / 18:50:46",
#     "restaurant_name": "\u0411\u0423\u041a\u041e\u0412\u0415\u041b\u042c",
#     "items": [
#         {
#             "name": "\u0421\u0430\u043b\u0430\u0442 \"\u0411\u0443\u0440\u044f\u0447\u043e\u043a\" 200\u0433",
#             "amount": "130.00",
#             "quantity": 1,
#             "sum": 130.0
#         },
#         {
#             "name": "\u041e\u0432\u043e\u0447\u0456 \u0433\u0440\u0438\u043b\u044c \u0446\u0456\u043b\u0456 100\u0433",
#             "amount": "125.00",
#             "quantity": 2,
#             "sum": 250.0
#         },
#         {
#             "name": "Kaiser 0,5\u043b",
#             "amount": "135.00",
#             "quantity": 1,
#             "sum": 135.0
#         },
#         {
#             "name": "\u041a\u0430\u043f\u0443\u0447\u0456\u043d\u043e",
#             "amount": "85.00",
#             "quantity": 4,
#             "sum": 340.0
#         },
#         {
#             "name": "\u041a\u0430\u043d\u0430 \u0430\u043c\u0435\u0440\u0456\u043a\u0430\u043d\u043e",
#             "amount": "65.00",
#             "quantity": 6,
#             "sum": 390.0
#         },
#         {
#             "name": "\u0423\u0437\u0432\u0430\u0440 250\u043c\u043b",
#             "amount": "65.00",
#             "quantity": 1,
#             "sum": 65.0
#         },
#         {
#             "name": "\u0421\u0456\u043a \u0432 \u0430\u0441\u043e\u0440\u0442\u0438\u043c\u0435\u043d\u0442\u0456 250\u0433",
#             "amount": "65.00",
#             "quantity": 1,
#             "sum": 65.0
#         },
#         {
#             "name": "\u041b\u0430\u0432\u0430\u0448 \u0456\u0437 \u0441\u0438\u0440\u043e\u043c \u0442\u0430 \u0431\u0440\u0438\u043d\u0437\u043e\u044e 1\u043f\u043e\u0440",
#             "amount": "110.00",
#             "quantity": 1,
#             "sum": 110.0
#         },
#         {
#             "name": "\u0428\u0430\u0448\u043b\u0438\u043a \u043a\u0443\u0440\u044f\u0447\u0438\u0439 100\u0433",
#             "amount": "210.00",
#             "quantity": 2,
#             "sum": 420.0
#         },
#         {
#             "name": "\u041a\u0430\u0440\u0442\u043e\u043f\u043b\u044f \u0437\u0430\u043f\u0435\u0447\u0435\u043d\u0430 \u043d\u0430 \u043c\u0430\u043d\u0433\u0430\u043b\u0456 300\u0433\u0440",
#             "amount": "210.00",
#             "quantity": 1,
#             "sum": 210.0
#         },
#         {
#             "name": "\u0421\u0430\u043b\u0430\u0442 \"\u0417 \u043a\u0430\u043f\u0443\u0441\u0442\u0438\" 150\u0433",
#             "amount": "130.00",
#             "quantity": 2,
#             "sum": 260.0
#         },
#         {
#             "name": "\u041a\u0443\u0440\u044f\u0447\u0438\u0439 \u0431\u0443\u043b\u044c\u0439\u043e\u043d 300\u0433",
#             "amount": "215.00",
#             "quantity": 1,
#             "sum": 215.0
#         },
#         {
#             "name": "\u0427\u0430\u0439 \u0410\u043b\u044c\u043f\u0456\u0439\u0441\u044c\u043a\u0438\u0439 \u043b\u0443\u0433",
#             "amount": "95.00",
#             "quantity": 1,
#             "sum": 95.0
#         },
#         {
#             "name": "\u0425\u0440\u0456\u043d\u043e\u0432\u0443\u0445\u0430",
#             "amount": "1000.00",
#             "quantity": 0.1,
#             "sum": 100.0
#         },
#         {
#             "name": "\u041a\u0430\u0440\u0442\u043e\u043f\u043b\u044f \"\u041f\u043e-\u0434\u043e\u043c\u0430\u0448\u043d\u044c\u043e\u043c\u0443\" 200\u0433",
#             "amount": "125.00",
#             "quantity": 2,
#             "sum": 250.0
#         },
#         {
#             "name": "\u0421\u0430\u043b\u0430\u0442 \"\u0413\u0440\u0435\u0446\u044c\u043a\u0438\u0439\" 250\u0433",
#             "amount": "250.00",
#             "quantity": 1,
#             "sum": 250.0
#         },
#         {
#             "name": "\u0425\u043b\u0456\u0431 1 \u043a\u0443\u0441",
#             "amount": "3.00",
#             "quantity": 5,
#             "sum": 15.0
#         },
#         {
#             "name": "\u041f\u0430\u043c\u043f\u0443\u0448\u043a\u0430 \u0437 \u0447\u0430\u0441\u043d\u0438\u0447\u043a\u043e\u043c",
#             "amount": "15.00",
#             "quantity": 10,
#             "sum": 150.0
#         },
#         {
#             "name": "\u0411\u043e\u0440\u0449 \u0443\u043a\u0440\u0430\u0457\u043d\u0441\u044c\u043a\u0438\u0439 300\u0433",
#             "amount": "215.00",
#             "quantity": 3,
#             "sum": 645.0
#         },
#         {
#             "name": "\u0420\u0435\u0431\u0440\u0430 BBQ 300\u0433",
#             "amount": "520.00",
#             "quantity": 1,
#             "sum": 520.0
#         },
#         {
#             "name": "\u0424\u043e\u0440\u0435\u043b\u044c \u0443 \u043f\u0440\u043e\u0432\u0430\u043d\u0441\u044c\u043a\u0438\u0445 \u0442\u0440\u0430\u0432\u0430\u0445 100\u0433",
#             "amount": "250.00",
#             "quantity": 6.9,
#             "sum": 1725.0
#         },
#         {
#             "name": "\u041a\u043e\u0432\u0431\u0430\u0441\u043a\u0438 \u0433\u0440\u0438\u043b\u044c \"\u041a\u0430\u0439\u0437\u0435\u0440\"",
#             "amount": "190.00",
#             "quantity": 6,
#             "sum": 1140.0
#         },
#         {
#             "name": "\u0420\u0443\u043b\u044c\u043a\u0430 \u0441\u0432\u0438\u043d\u043d\u0430 \u0437 \u0442\u0443\u0448\u043a\u043e\u0432\u0430\u043d\u043e\u044e \u043a\u0430\u043f\u0443\u0441\u0442\u043e\u044e",
#             "amount": "160.00",
#             "quantity": 12.5,
#             "sum": 2000.0
#         }
#     ]
# }
#
# billData = {
#     "bill_time": "19.08.2023 19:25",
#     "restaurant_name": "\u0417\u0430\u043b",
#     "items": [
#         {
#             "name": "\u0421\u0432\u0438\u043d\u044f\u0447\u0435 \u043a\u043e\u043b\u0456\u043d\u043e \u043f\u043e-\u0447\u0435\u0441\u044c\u043a\u0438 - \u043d\u0430 \u0437 \u043c'\u044f\u0441\u0430 \u0434\u0438\u043a\u043e\u0433\u043e \u043a\u0430\u0431\u0430\u043d\u0430-\u0447\u0430\u0438",
#             "amount": "1,0",
#             "quantity": 1,
#             "sum": 120.0
#         },
#         {
#             "name": "\u041f\u0438\u0432\u043e \u0448\u043e \u0421\u0443\u0445\u0438\u0439 \u0427\u043e\u0440\u043d\u0438\u04390.4",
#             "amount": "0.4",
#             "quantity": 1,
#             "sum": 95.0
#         },
#         {
#             "name": "\u041f\u0438\u0432\u043e 2085* Reberbarheles",
#             "amount": "0.4",
#             "quantity": 1,
#             "sum": 240.0
#         },
#         {
#             "name": "\u041f\u0438\u0432\u043e Hopkins 0.4",
#             "amount": "0.4",
#             "quantity": 1,
#             "sum": 80.0
#         },
#         {
#             "name": "\u0420\u0435\u0431\u0435\u0440 \u0441\u0435\u0442 new",
#             "amount": "2,5",
#             "quantity": 1,
#             "sum": 437.5
#         },
#         {
#             "name": "\u041f\u0438\u0432\u043e 2085- Organic Cider 0.4",
#             "amount": "0.4",
#             "quantity": 3,
#             "sum": 195.0
#         },
#         {
#             "name": "\u041f\u0438\u0432\u043e 2085* Reberbarheles 0.4",
#             "amount": "0.4",
#             "quantity": 1,
#             "sum": 80.0
#         },
#         {
#             "name": "\u041f\u0438\u0432\u043e Hrew Brew Vertigo 0.4",
#             "amount": "0.4",
#             "quantity": 1,
#             "sum": 130.0
#         }
#     ]
# }

# Convert the data to a JSON string
json_data = json.dumps(billData)

# Encode the data to be URL-friendly
encoded_data = urllib.parse.quote_plus(json_data)

# Add the encoded data to the URL as a query parameter
web_app_url = f"http://localhost:63342/pages/webapp.html?data={encoded_data}"

print(web_app_url)
