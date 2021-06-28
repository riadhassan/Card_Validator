from bottle import route, run, template, request, response, view
from validator.card_identifier import get_issuer


@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)


@route('/')
@view('index')
def validator():
    card_number = request.query["cardNumber"]
    try:
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