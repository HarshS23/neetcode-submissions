class Solution:
    def isPalindrome(self, s: str) -> bool:

        holder = ""
        for i in s:
            if i.isalnum():
                holder += i.lower()


        return holder == holder[::-1]
        # for i in range(len(holder)//2):
        #     forward =holder[i]
        #     backward = holder[len(holder) - 1 - i]

        #     if (forward != backward):
        #         return False
            
        # return True