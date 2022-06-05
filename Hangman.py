import random

word_list = ['КЛЮЧ', 'КНИГА', 'ЕНОТ', 'МАШИНКА', 'КОРОВА', 'ТЕЛЕЖКА', 'ШЛЕМ', 'КНОПКА', 'ШНУР', 'ЧЕРНЫЙ',
             'ВЛАСТЕЛИН', 'СКАЙП', 'ДУБ', 'ЧАСЫ', 'ТРУБА', 'ЕЛКА', 'ИНСТИТУТ', 'КОРОБКА', 'ТАБЛИЧКА', 'ВОДА',
             'СКОВОРОДА', 'МНОГОНОЖКА', 'ЕВРЕЙ', 'ТЕРМИТ', 'КАЧЕК', 'РУЛОН', 'МАГНИТОФОН', 'НОГА', 'СЛОН',
             'МИКРОВОЛНОВКА', 'ТОРТ', 'МАК', 'ДЫМ', 'ЧАЙКА', 'ВАЛЕТ', 'ПЛИНТУС', 'ШАПКА', 'ДИНОЗАВР', 'ТОРШЕР',
             'БАЛАЛАЙКА', 'БАНКА', 'ЯХТА', 'ОВЦА', 'БАНАН', 'ДУБ', 'АНИМЕ', 'РАДУГА', 'БУКВА', 'ВЕЛОСИПЕД',
             'БАНДЖО', 'ГОЛУБЬ', 'ВИНТОВКА', 'КУБОК', 'ЖАСМИН', 'ТЕЛЕФОН', 'АНДРОИД', 'ГОРА', 'ХАЛАТ', 'ЖЕТОН',
             'ОБОД', 'МЫЛО', 'ЙОГ', 'ШИШКА', 'ДОЛЛАР', 'КОЛОНКА', 'КУБИК', 'ОМАР', 'РАКЕТА', 'МОРКОВКА', 'ЗЕРКАЛО',
             'МОЛОТ', 'ВОЗДУХ', 'ЗМЕЙ', 'ЁЖ', 'ПАЛЬМА', 'МАСЛО', 'ДИДЖЕЙ', 'МЕШОК', 'ТЮБИК', 'МОЗГ', 'ПОЕЗД',
             'РОЗЕТКА', 'ПАРАШЮТИСТ', 'БЕЛКА', 'ШПРОТЫ', 'САМОСВАЛ', 'ПАЗЛ', 'БУТЫЛКА', 'КРЕМЛЬ', 'ПИЦЦА',
             'МАКАРОНЫ', 'КОВЕР', 'ЗУБЫ', 'ЯРЛЫК', 'КАШАЛОТ', 'МАРС', 'ШАКАЛ', 'ПОМАДА', 'ДЖИП', 'ЛЕЩ', 'КАМЕНЬ',
             'ДИСК']


def get_word():
    return word_list[random.randint(0, len(word_list) - 1)].upper()


def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]


def play(word):
    word_completion = list('_' * len(word))
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6

    print("\tLet's play in HangMan")
    print(display_hangman(tries))
    print(f'The word with {len(word)} letters:\n\t', *word_completion, sep='')
    while not guessed:
        user_answer = input('Write a letter or a whole word:\n').upper()
        if not user_answer.isalpha():
            print('You can use only letters!')
            continue
        if user_answer in guessed_words + guessed_letters:
            print("You already wrote this some time ago. Try something new!")
            print(guessed_words + guessed_letters)
            continue

        if len(user_answer) == 1:
            guessed_letters.append(user_answer)
            if user_answer not in word:
                tries -= 1
                print(display_hangman(tries))
            else:
                for i in range(len(word)):
                    if word[i] == user_answer:
                        word_completion[i] = user_answer
        else:
            guessed_words.append(user_answer)
            if user_answer == word:
                word_completion = list(user_answer)
            else:
                tries -= 1
                print(display_hangman(tries))
        print(f'The word with {len(word)} letters:\n\t', *word_completion, sep='')
        if '_' not in word_completion:
            guessed = True
            print('\tCongratulations, you guessed right!')
        elif tries == 0:
            print(f"Sorry, You're lose. The word was\n\t {word}")
            break


while True:
    play(get_word())
    if input('\tDo you want replay this game?\n') != 'да':
        break
