def convert_miles_to_km(miles: float) -> float:
    return miles * 1.60934

def calculator(question: str) -> float:
    return eval(question)

def is_save_question(question: str) -> bool:
    correct_symbols = '0123456789+-*/()'
    for sym in list(question.replace(' ', '')):
        if sym not in correct_symbols:
            return False
    return True