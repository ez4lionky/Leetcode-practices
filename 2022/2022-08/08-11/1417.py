class Solution:
    def reformat(self, s: str) -> str:
        x_num, y_num = 0, 0
        for c in s:
            if c.isalpha():
                x_num += 1
            else:
                y_num += 1
        if abs(x_num - y_num) > 1:
            return ""

        flag = y_num > x_num
        t = list(s)
        j = 1
        for i in range(0, len(t), 2):
            if t[i].isdigit() != flag:
                while t[j].isdigit() != flag:
                    j += 2
                t[i], t[j] = t[j], t[i]
        return ''.join(t)

