def firstNotRepeatingCharacter(a):
    for i in range(len(a)):
        while a[i] not in a[i + 1:] and a[i] not in a[:i]:
            return a[i]
    return "_"