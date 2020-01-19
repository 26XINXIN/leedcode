class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.dic = set([(s[0], s[-1], max(len(s) - 2, 0)) for s in dictionary])

    def isUnique(self, word: str) -> bool:
        abbr = (word[0], word[-1], max(len(word)-2, 0))
        return abbr not in self.dic
        


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)