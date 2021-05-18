def num_translate(el: str) -> str:
    translate_table = {
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять'
    }
    if el.islower() and el in translate_table:
        return translate_table.get(el)
    elif el.lower() in translate_table:
        return translate_table.get(el.lower()).capitalize()

