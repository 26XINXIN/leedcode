class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) < 4 or len(s) > 12:
            return []
        result = list()
        self.split_ip([], s, result)
        return result

    def split_ip(self, prefix, s, result):
        if len(prefix) == 3:
            if self.valid_field(s):
                ip = ""
                for field in prefix:
                    ip += field + "."
                ip += s
                result.append(ip)
                return 
            else:
                return
        
        for i in range(1, 4):
            field = s[:i]
            if self.valid_field(field):
                new_prefix = list(prefix) + [field]
                self.split_ip(new_prefix, s[i:], result)
    
    def valid_field(self, s):
        if len(s) == 1:
            return True
        elif len(s) == 2 and s[0] != "0":
            return True
        elif len(s) == 3 and s[0] != "0":
            if s[0] == "1":
                return True
            elif s[0] == "2":
                if int(s[1:]) < 56:
                    return True
            else:
                return False
        return False
        
string = "25525511135"
result = Solution().restoreIpAddresses(string)
print(result)