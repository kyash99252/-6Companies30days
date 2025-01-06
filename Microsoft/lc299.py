from collections import defaultdict

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        n = len(guess)
        bulls = cows = 0
        map_secret = defaultdict(int)
        map_guess = defaultdict(int)

        for i in range(n):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                map_secret[secret[i]] += 1
                map_guess[guess[i]] += 1
        
        for key in map_secret.keys():
            cows += min(map_secret[key], map_guess[key])
        
        return f'{bulls}A{cows}B'