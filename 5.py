def letterCombinations(self, digits: str) -> List[str]:
        res = []
        numpad = {"2":"abc",
                  "3":"def",
                  "4":"ghi",
                  "5":"jkl",
                  "6":"mno",
                  "7":"pqrs",
                  "8":"tuv",
                  "9":"wxyz"}
        
        def backtrack(i, curStr):
            if len(curStr) == len(digits):
                res.append(curStr)
                return
            
            for c in numpad[digits[i]]:
                backtrack(i+1,curStr+c)
                
        if digits:
            backtrack(0,"")
            
        return res
