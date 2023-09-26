def is_adjective(word):
    return word.endswith(("lios", "liala"))


def is_noun(word):
    return word.endswith(("etr", "etra"))


def is_verb(word):
    return word.endswith(("initis", "inites"))


def is_valid_word(word):
    return (is_adjective(word) or
            is_noun(word) or
            is_verb(word))


def have_same_gender(words):
    genders = set()
    for word in words:
        if word.endswith(("lios", "etr", "initis")):
            genders.add("M")
        else:
            genders.add("F")
    return len(genders) == 1


def has_valid_word_order(words):
    adjectives = []
    nouns = []
    verbs = []

    for word in words:
        if is_adjective(word):
            adjectives.append(word)
        elif is_noun(word):
            nouns.append(word)
        elif is_verb(word):
            verbs.append(word)

    if not nouns:
        return False

    if adjectives:
        if nouns[0] not in adjectives:
            return False

    if verbs:
        if nouns[-1] not in verbs:
            return False

    return True


def is_valid_sentence(sentence):
    if not sentence:
        return False

    words = sentence.split()
    return (is_valid_word(sentence) and
            have_same_gender(words) and
            has_valid_word_order(words))


sentence = input()
if is_valid_sentence(sentence):
    print("YES")
else:
    print("NO")
