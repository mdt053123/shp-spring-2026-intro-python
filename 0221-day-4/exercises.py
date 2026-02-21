class StringAnalyzer:
    def __init__(self, s):
        self.s = s
        
    def is_palindrome(self):
        # returns True if self.s is a palindrome, False otherwise
        return self.s == self.s[::-1]
        
    def contains_only_vowels(self):
        # returns True if self.s contains only A, E, I, O, U, Y
        for char in self.s.upper():
            if char not in 'AEIOUY':
                return False
        return True
        
    def contains(self, sub):
        # returns True if sub is a substring of self.s, False otherwise
        # e.g. "abc" is a substring of "abcd"
        if not sub:
            return True
        
        starting_char = sub[0]
        for i in range(len(self.s)):
            if self.s[i] == starting_char:
                if self.s[i : i + len(sub)] == sub:
                    return True
                
        return False
        
str_analyzer = StringAnalyzer("racecar")
print(str_analyzer.is_palindrome()) # True
print(str_analyzer.contains_only_vowels()) # False
print(str_analyzer.contains("race")) # True