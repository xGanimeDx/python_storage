def spell(txt):
    x = len(txt)
    if x < 1:
        return ""
    print(txt[x - 1:])
    spell(txt[:x - 1])

txt = input()
spell(txt)