class Card:
    _symbols = {
        "Spades": "\u2660",
        "Diamonds": "\u2666",
        "Hearts": "\u2665",
        "Clubs": "\u2663"
    }

    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def __repr__(self):
        return f"{self.value}{self._symbols[self.suit]}"

    def to_str(self):
        return f"{self.value}{self._symbols[self.suit]}"

    def get_suit(self, suit):
        if suit not in self._symbols:
            raise KeyError("Такой масти нет")
        return self._symbols[suit]

    def equal_suit(self, other_card):
        return self.suit == other_card.suit

# Задание: Теперь создадим колоду из 52-ух карт и реализуем все методы
class Deck:
    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        suits = ["Hearts", "Diamonds","Clubs", "Spades"]
        common_deck = list(map(str, range(2, 11))) + ["J", "Q", "K", "A"]
        self.cards = []
        for suit in suits:
            for value in common_deck:
                #cards.append(Card(card, suit))
                card = Card(value, suit)
                self.cards.append(card)



    def show(self):
        # Принцип работы данного метода прописан в 00_task_deck.md
        return f"cards[{len(self.cards)}]", ', '.join([card.to_str() for card in self.cards])

    def draw(self, x):
        # Принцип работы данного метода прописан в 00_task_deck.md
        pass

    def shuffle(self):
        # Обратите внимание на: https://www.w3schools.com/python/ref_random_shuffle.asp
        pass


# Создаем колоду
deck = Deck()
# Выводим колоду в формате указанном в основном задании
print(deck.show())
# # Тусуем колоду
# deck.shuffle()
# print(deck.show())
#
# # Возьмем 5 карт "в руку"
# hand = deck.draw(5)
# # Выводим колоду, чтобы убедиться что 5 верхних карт отсутствуют
# print(deck.show())
# # Выводим список карт "в руке"(список hand)
# print(...)
