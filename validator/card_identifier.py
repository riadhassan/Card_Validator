def get_issuer(card_number: str) -> str:
    card_number = "".join(card_number.split())
    card_number_len = len(card_number)
    if card_number.startswith("4") and (card_number_len == 13 or card_number_len == 16):
        return "Visa"

    elif card_number.startswith("5") and card_number_len == 16:
        return "MasterCard"

    elif (card_number.startswith("34") or card_number.startswith("37")) and card_number_len == 16:
        return "American Express"

    else:
        raise ValueError("Invalid Card Number")
