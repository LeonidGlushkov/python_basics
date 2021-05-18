from random import choice, randrange


def get_jokes(n: int, repeat=True) -> list:
    if repeat:
        for i in range(n):
            jokes.append(f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}')
        return jokes
    elif not repeat:
        if n <= len(nouns):
            nouns_2 = nouns.copy()
            adverbs_2 = adverbs.copy()
            adjectives_2 = adjectives.copy()
            for i in range(n):
                jokes.append(nouns_2.pop(randrange(len(nouns_2))) + ' ' +
                             adverbs_2.pop(randrange(len(adverbs_2))) + ' ' +
                             adjectives_2.pop(randrange(len(adjectives_2))))
            return jokes
        else:
            return 'Повторяешься!'


jokes = []
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

print(get_jokes(6, False))
