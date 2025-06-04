import random


def random_string():
    random_list = [
        "Please try speaking something more descriptive, please try again",
        "Oh! It appears you spoke something I don't understand yet, please try again",
        "Do you mind trying to rephrase that? please try again",
        "I'm terribly sorry, I didn't quite catch that, please try again",
        "I can't answer that yet, please try asking something else, please try again"
    ]

    list_count = len(random_list)
    random_item = random.randrange(list_count)

    return random_list[random_item]
