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

    def _is_word_exist(self, word):
        current_node = self.root
        for letter in word:
            if not current_node.get(letter):
                return False
            current_node = current_node.get(letter)
        return current_node.get(Trie.is_word)

    def has_word(self, word: str) -> bool:
        return self._is_word_valid(word) and self._is_word_exist(word)

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
            pop_letter = None
            current_node = self.root
            for idx, letter in enumerate(word):
                if len(current_node.get(letter)) <= 2:
                    if not pop_letter and (not current_node.get(letter).get(Trie.is_word) or idx == len(word)-1):
                        pop_letter = letter
                else:
                    pop_letter = None
                current_node = current_node.get(letter)
            if pop_letter:
                current_node = self.root
                for letter in word:
                    if letter == pop_letter:
                        current_node.pop(letter)
                        break
                    current_node = current_node.get(letter)
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
