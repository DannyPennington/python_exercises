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


print (censor("We do not say shit", "shit"))