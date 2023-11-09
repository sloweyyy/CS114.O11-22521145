import re

ADJ_PATTERN = r".*(lios|liala)$"
NOUN_PATTERN = r".*(etr|etra)$"
VERB_PATTERN = r".*(initis|inites)$"


def is_adjective(word):
    return re.match(ADJ_PATTERN, word)


def is_noun(word):
    return re.match(NOUN_PATTERN, word)


def is_verb(word):
    return re.match(VERB_PATTERN, word)


def get_gender(word):
    if re.match(r".*(lios|etr|initis)$", word):
        return "M"
    else:
        return "F"


def validate_sentence(sentence):
    words = sentence.split()

    if not words:
        return False

    genders = set()
    has_noun = False

    for word in words:
        if is_adjective(word):
            genders.add(get_gender(word))
        elif is_noun(word):
            has_noun = True
            genders.add(get_gender(word))
        elif is_verb(word):
            pass
        else:
            return False

    if not has_noun:
        return False

    return len(genders) == 1


sentence = input()
if validate_sentence(sentence):
    print("YES")
else:
    print("NO")
