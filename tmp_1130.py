class Trie:
    is_word = "is_word"

    def __init__(self):
        self.root = self._get_default_node()

    @staticmethod
    def _get_default_node() -> dict:
        return {Trie.is_word: False}

    @staticmethod
    def _is_word_valid(word):
        return isinstance(word, str) and word.isalpha() and word.islower()

    def has_word(self, word: str) -> bool:
        if not self._is_word_valid(word):
            return False

        current_node = self.root
        for letter in word:
            if not current_node.get(letter):
                return False
            current_node = current_node.get(letter)
        return current_node.get(Trie.is_word)

    def add_word(self, word: str) -> None:
        if self._is_word_valid(word):
            current_node = self.root
            for letter in word:
                if not current_node.get(letter):
                    current_node.update({letter: self._get_default_node()})
                current_node = current_node.get(letter)
            current_node.update({Trie.is_word: True})

    def remove_word(self, word: str) -> None:
        if self.has_word(word):
            target_node = None
            pop_letter = None
            current_node = self.root
            for idx, letter in enumerate(word):
                if idx != len(word) - 1:
                    if current_node.get(Trie.is_word):
                        target_node = current_node
                        pop_letter = letter
                else:
                    if current_node.get(Trie.is_word):
                        pop_letter = None
                current_node = current_node.get(letter)
            if target_node and pop_letter:
                target_node.pop(pop_letter)
            else:
                current_node.update({Trie.is_word: False})

    def _get_all_words(self, node: dict, result: [str, ...], prefix: str="") -> None:
        for k, v in node.items():
            if k == Trie.is_word:
                if v is True:
                    result.append(prefix)
            else:
                self._get_all_words(v, result, prefix + k)

    def enumerate_words(self, prefix: str="") -> [str, ...]:
        """
        :param prefix: only "" and lowercase alpha are valid
        :return: all words with prefix, all words in trie if prefix is "", [] otherwise
        """
        result = []
        if self._is_word_valid(prefix) or prefix == "":
            current_node = self.root
            for letter in prefix:
                current_node = current_node.get(letter)
                if not current_node:
                    break
            if current_node:
                self._get_all_words(current_node, result, prefix)
        return result


if __name__ == "__main__":
    w1 = "apple"
    w2 = "apply"
    w3 = "art"
    w4 = "task"
    w5 = "teach"
    w6 = "flash"

    words = [w1, w2, w3, w4, w5, w6]
    trie = Trie()
    for w in words:
        trie.add_word(w)
    print(trie.enumerate_words())
    trie.add_word("")
    trie.remove_word("c")
    print(trie.enumerate_words())
    print(trie.has_word(""))

