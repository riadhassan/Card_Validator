from bottle import route, run, template, request, response, view
from validator.card_identifier import get_issuer


@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)


@route('/')
@view('index')
def validator():
    try:
        card_number = request.query["cardNumber"]
    except KeyError:
        response.status = 400
        card_number = ""

    try:
        if card_number == "":
            return {
                "result": "None",
                "cardNumber": "Card number not found."
            }
        issuer = get_issuer(card_number)
        return {"result": issuer,
                "cardNumber": card_number
                }
    except ValueError:
        response.status = 400
        return {"result": "Card number is not valid.",
                "cardNumber": card_number
                }


run(host='localhost', port=8080)