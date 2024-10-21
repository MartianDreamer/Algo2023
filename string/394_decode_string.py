class Solution:
    def decodeString(self, s: str) -> str:
        strings = [""]
        opens = []
        for i in range(len(s)):
            if s[i] == "[":
                opens.append(i)
                strings.append("")
            elif s[i] == "]":
                open_pos = opens.pop()
                count_str = ""
                string = strings.pop()
                for c in s[open_pos - 1::-1]:
                    if not c.isdigit():
                        break
                    count_str = c + count_str
                strings[-1] += string * int(count_str)
            elif s[i].isalpha():
                strings[-1] += s[i]
        return "".join(strings)
