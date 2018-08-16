class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip(" ")
        words = s.split(" ")
        word_list = list()
        for word in words[::-1]:
            if len(word) > 0:
                word_list.append(word)
        return " ".join(word_list)