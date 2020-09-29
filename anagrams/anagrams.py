def reverse_words(string):
    if type(string) != str:
        raise TypeError('Only strings are allowed')
    words = string.split()
    result = []
    for word in words:
        reverse_word = []
        another_symbols = {}
        for i in range(len(word)):
            if word[i].isalpha():
                reverse_word.append(word[i])
            else:
                another_symbols[i] = word[i]
        reverse_word = reverse_word[::-1]

        for key, value in another_symbols.items():
            reverse_word.insert(key, value)

        out = ''.join(reverse_word)
        result.append(out)
    return ' '.join(result)


if __name__ == '__main__':
    cases = [
        ('abcd efgh', 'dcba hgfe'),
        ('a1bcd efg!h', 'd1cba hgf!e'),
        ('', '')
    ]

    for text, reversed_text in cases:
        assert reverse_words(text) == reversed_text
        print(reverse_words(text))
