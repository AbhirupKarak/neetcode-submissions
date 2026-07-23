class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        valid = {")" : "(", "}" : "{", "]" : "["}
        for char in s:
            if char in ["{", "[", "("]:
                st.append(char)
            elif char in ["}", ")", "]"]:
                if not st or valid.get(char) != st[-1]:
                    return False
                st.pop()
        if not st:
            return True
        else:
            return False
        