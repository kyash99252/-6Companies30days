class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []
        
        mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        result = []
        
        def backtrack(combination, next_digits):
            if not next_digits:
                result.append(combination)
                return
            
            digit = next_digits[0]
            letters = mapping.get(digit)
            if letters:
                for letter in letters:
                    backtrack(combination + letter, next_digits[1:])
                    
        backtrack("", digits)
        return result