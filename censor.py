def censor(text, word):
    list = text.split()
    new = []

    for i in list:
        if i == word:
            new.append("*" * len(word))
        else:
            new.append(i)
        final = " ".join(new)
    return final
