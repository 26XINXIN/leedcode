class Solution:
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        result = list()
        i = 0
        while i < len(words):
            line = [words[i]]
            length = len(words[i])
            i += 1
            while i < len(words) and len(words[i]) + 1 + length <= maxWidth:
                line.append(" "); line.append(words[i])
                length += 1 + len(words[i])
                i += 1
            result.append(line)
        # print(result)
        
        for i in range(len(result) - 1):
            if len(result[i]) == 1:
                line = result[i][0] + " " * (maxWidth - len(result[i][0]))
                result[i] = line
                continue
            words_length = sum([len(result[i][j]) for j in range(0, len(result[i]), 2)])
            num_spaces = len(result[i]) // 2
            space_length = (maxWidth - words_length) // num_spaces
            plus_one = (maxWidth - words_length) % num_spaces
            print("{},{},{},{}".format(words_length, num_spaces, space_length, plus_one))
            for j in range(1, len(result[i]), 2):
                if j // 2 < plus_one:
                    result[i][j] = " " * (space_length + 1)
                else:
                    result[i][j] = " " * space_length
            line = ""
            for word in result[i]:
                line += word
            result[i] = line
        line = ""
        for word in result[-1]:
            line += word
        line = line.strip(" ")
        line += " " * (maxWidth - len(line))
        result[-1] = line
        return result

print(Solution().fullJustify(["What","must","be","acknowledgment","shall","be"], 16))