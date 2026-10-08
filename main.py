while True:

    text = input("Введите строку: ")
    words = text.split()
    longest = words[0]
    for word in words:
       if len(word) > len(longest):
        longest = word
    print("Самое длинное слово: ", longest)
    print("Длина слова:", len(longest))
    x = int(input("1-продолжить, иначе заверщить: "))
    if x != 1:
        break