def cut_text(word):
    find_h = word.index('h')
    cut = word[find_h::]
    return cut


text = input('Введите текст: ')
text_list = list(text)
back_text = cut_text(text_list)[::-1]
print('Ответ:', ''.join(cut_text(back_text)[1:-1:]))
# TODO: Какой должен быть результат если ввести humanhumanhuman?:)
#Думаю должно быть hnamuhnamuh, или h не должен быть включен? Если так, то добавил [1:-1:]
