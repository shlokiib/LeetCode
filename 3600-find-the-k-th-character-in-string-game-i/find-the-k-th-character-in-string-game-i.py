class Solution:
    def kthCharacter(self, k: int) -> str:
        def next_char(c):
            if c == 'z':
                return 'a'
            else:
                return chr(ord(c) + 1)

        word = "a"
        while len(word) < k:
            transformed = ''
            for ch in word:
                transformed += next_char(ch)
            word += transformed

        result = word[k - 1]
        return result