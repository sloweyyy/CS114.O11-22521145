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


def is_same_gender(word1, word2):
    if word1.endswith(("lios", "etr", "initis")):
        return word2.endswith(("lios", "etr", "initis"))
    else:
        return word2.endswith(("liala", "etra", "inites"))


def is_valid_clause(clause):
    words = clause.split()

    has_adjective = False
    has_noun = False
    has_verb = False

    for i, word in enumerate(words):
        if not is_valid_word(word):
            return False

        if is_adjective(word):
            has_adjective = True

        if is_noun(word):
            if has_noun:
                return False
            has_noun = True

        if is_verb(word):
            has_verb = True

        if i > 0 and not is_same_gender(words[i - 1], word):
            return False

    return has_adjective and has_noun and has_verb


def is_valid_sentence(sentence):
    if not sentence:
        return False

    if is_valid_word(sentence):
        return True

    clauses = sentence.split(',')

    for clause in clauses:
        if not is_valid_clause(clause):
            return False

    return True


sentence = input()
if is_valid_sentence(sentence):
    print("YES")
else:
    print("NO")
