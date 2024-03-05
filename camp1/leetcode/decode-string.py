class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        num = 0
        letter = ""

        for i in range(len(s)):
            
            print(stack)
            if s[i].isnumeric():
                
                stack.append(letter)
                letter = ""

                num = num*10+int(s[i])
                # print(num)
            
            elif s[i] == "[":
                stack.append(num)
                num = 0

            elif s[i] == "]":
                word = letter
                letter = ""
                
                while not type(stack[-1]) == int:
                    word = stack.pop()+(word)
                stack.append(word*stack.pop())

            else:
                letter+=s[i]
        stack.append(letter)
        print(stack)
        
        return "".join(stack)

