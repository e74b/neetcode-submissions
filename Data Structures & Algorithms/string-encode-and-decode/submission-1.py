class Solution:

    def encode(self, strs: List[str]) -> str:
        return f"{len(strs)}:" + "<,".join(strs)

    def decode(self, s: str) -> List[str]:
        semicolonIdx = s.index(":")
        noOfItems = int(s[:semicolonIdx])
        return [str.replace("<<", "<") for str in s[(semicolonIdx + 1):].split("<,")][:noOfItems]
