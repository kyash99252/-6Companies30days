class Solution:
    def foo(self, price, special, needs, required, memo):
        if tuple(required) in memo:
            return memo[tuple(required)]
        
        if sum(required) == 0:
            return 0

        total = float('inf')
        for offer in special:
            new_req = []
            for i in range(len(needs)):
                if required[i] < offer[i]:
                    break
                new_req.append(required[i] - offer[i])
            else:
                total = min(total, offer[-1] + self.foo(price, special, needs, new_req, memo))
        
        no_offer_cost = sum(price[i] * required[i] for i in range(len(needs)))
        result = min(total, no_offer_cost)
        memo[tuple(required)] = result
        return result

    def shoppingOffers(self, price, special, needs):
        memo = {}
        return self.foo(price, special, needs, needs, memo)