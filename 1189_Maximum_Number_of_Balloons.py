class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon = {c: 0 for c in 'balon'}
        for c in text:
            if c in balloon:
                balloon[c] += 1
        return min([(v//2 if k == 'l' or k == 'o' else v) for k, v in balloon.items()])