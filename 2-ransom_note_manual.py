def RNConstructorCheck(ransomNote: str, Magazine: str) -> bool:
    if len(ransomNote) > len(Magazine):
        return False

    counts = {}

    for ch in Magazine:
        counts[ch] = counts.get(ch, 0) + 1

    for ch in ransomNote:
        if counts[ch] == 0:
            return False
        counts[ch] -= 1

    return True


ransomNote = "aab"
Magazine = "baca"

print(RNConstructorCheck(ransomNote, Magazine))