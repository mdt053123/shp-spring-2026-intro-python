class StringAnalyzer:
    def __init__(self, s):
        self.s = s
        
    def is_palindrome(self):
        # returns True if self.s is a palindrome, False otherwise
        
    def contains_only_vowels(self):
        # returns True if self.s contains only A, E, I, O, U, Y
        
    def contains(self, sub):
        # returns True if sub is a substring of self.s, False otherwise
        # e.g. "abc" is a substring of "abcd"
        
str_analyzer = StringAnalyzer("racecar")
print(str_analyzer.is_palindrome()) # True
print(str_analyzer.contains_only_vowels()) # False
print(str_analyzer.contains("ar")) # True