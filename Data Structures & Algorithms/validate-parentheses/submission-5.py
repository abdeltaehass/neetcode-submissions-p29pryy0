class Solution:
    def isValid(self, s: str) -> bool:
        
        temp = []
        for i in s:
            if i == '(' or i == '{' or i == '[':
                temp.append(i)
            else:
                if len(temp) == 0:
                    return False 
                if i == ')' and temp[-1] != '(':
                    return False
                if i == '}' and temp[-1] != '{':
                    return False
                if i == ']' and temp[-1] != '[':
                    return False

                temp.pop()

        if len(temp) == 0:
            return True
        else:
            return False
        