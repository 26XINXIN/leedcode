class Solution:
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        
        domino_list = list(dominoes)
        force_loc = list()
        force_times = [0] * len(dominoes)

        for i in range(len(domino_list)):
            if domino_list[i] != ".":
                force_loc.append(i)

        while len(force_loc) != 0:
            # result = ""
            # for s in domino_list:
            #     result += s
            # print(result)
            # loc = ""
            # for i in range(len(domino_list)):
            #     if i not in force_loc:
            #         loc += " "
            #     else:
            #         loc += "^"
            # print(loc)
            for i in range(len(force_loc)):
                if domino_list[force_loc[i]] == "R":
                    if (force_loc[i] == len(domino_list) - 1 or 
                        domino_list[force_loc[i] + 1] != "."):
                        force_loc[i] = -1
                    else:
                        force_loc[i] += 1
                        force_times[force_loc[i]] += 1
                elif domino_list[force_loc[i]] == "L":
                    if (force_loc[i] == 0 or 
                        domino_list[force_loc[i] - 1] != "."):
                        force_loc[i] = -1
                    else:
                        force_loc[i] -= 1
                        force_times[force_loc[i]] -= 1
            i = 0
            while i < len(force_loc):
                if force_loc[i] == -1:
                    force_loc.pop(i)
                elif i > 0 and force_loc[i] == force_loc[i-1]:
                    i -= 1
                    force_loc.pop(i); force_loc.pop(i)
                else:
                    i += 1

            for i in range(len(force_times)):
                if force_times[i] == 1:
                    domino_list[i] = "R"
                elif force_times[i] == -1:
                    domino_list[i] = "L"
                force_times[i] = 0

        result = ""
        for s in domino_list:
            result += s
        return result

dominoes = "RR.L"
Solution().pushDominoes(dominoes)
        


