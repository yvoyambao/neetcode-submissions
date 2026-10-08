class Solution:
    def countSeniors(self, details: List[str]) -> int:
        senior = 0
        for i in details:
            age = int(i[11:13])
            if age > 60:
                senior += 1
        return senior