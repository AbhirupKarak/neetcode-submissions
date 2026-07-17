class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            encoded_str = encoded_str + f"{len(s)}#" + f"{s}#"
        return encoded_str

    def decode(self, s: str) -> List[str]:
        pointer = 0
        decoded_strs = []
        while pointer < len(s):
            decoded_s = ""
            idx = s.find("#", pointer)
            num = int(s[pointer:idx])
            pointer += len(str(num)) + 1
            decoded_s += s[pointer:pointer + num]
            decoded_strs.append(decoded_s)
            pointer = pointer + num + 1
        return decoded_strs  



        
        
        
            



