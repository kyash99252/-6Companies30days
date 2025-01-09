class Solution:
    def displayContacts(self, n, contact, s):
        # code here
        contact = sorted(set(contact))
        result = []
        prefix = ""

        for char in s:
            prefix += char
            matches = [c for c in contact if c.startswith(prefix)]
            result.append(matches if matches else ["0"])

        return result