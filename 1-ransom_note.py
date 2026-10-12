from collections import Counter

def RNConstructerChecker(ransomNote: str, magazine: str) -> bool:
    if len(ransomNote) > len(magazine):
        return False

    counts = Counter(magazine)

    for ch in ransomNote:
        if counts[ch] == 0:
            return False
        counts[ch] -= 1

    return True



ransomNote = "aab"
magazine = "baca"
print(RNConstructerChecker(ransomNote, magazine))