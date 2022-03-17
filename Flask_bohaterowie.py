@app.route('/Brudnopis')
def Brudnopis():
    character_list =[
        'Mieszko I',
        'Donald',
        'Iron Man',
        'Julia Wieniawa'
    ] #lista postaci jaka ma się wyświetlać na stronie randomowo
    character_list2 = [] #tu na czysto będą lądować wyniki kodu poniżej

    for i in range(3):
        interesting_character = choice(character_list) # zmienna która ma wybierać konkretną postać
        character_indeks = character_list.index(interesting_character) 
        character_list.pop(character_indeks) #robimy indeksowanie i potem popa żeby postaci się nie powtarzały 

        character_desc = character(interesting_character) #tu załącza się kod z osobnego pliku funkcja /character

        word_list = character_desc.split(' ') #dzieli wyrazy do późniejszego podliczenia
        word_list_len = len(word_list) #liczy długość wyrazów

        content = [interesting_character, character_desc, word_list_len] #wrzuca listę w listę wyżej
        content_list.append(content) #łączy listę z kontentem

    def my_func (e):
        return e[:][2]

    content_list.sort(reverse=True,key=my_func)

    return render_template("Brudnopis.html", hero=content_list,) #poem_lines=poem_lines #hero=hero jakby przekazuje z pythona do htmla informacje
