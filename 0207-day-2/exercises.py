import random

def divisible_by_3(n):
    """
    return True if n is divisible by 3,
    return False if not
    """
    
    return n % 3 == 0
    
def sqrt(x):
    """
    Return the sqrt of x.
    DO NOT use x**(1/2)
    """
    
    if x < 0:
        return None  # or raise ValueError

    if x == 0:
        return 0

    guess = x
    while abs(guess * guess - x) > 1e-6:
        guess = (guess + x / guess) / 2

    return guess
    
def guess_the_number():
    """
    Generate a random number between 1 and 100,
    repeatedly ask the user to guess the number;
    if wrong guess, tell them if higher or lower,
    if right, print "Success" and end the game
    
    Hint: Use random.randint(a, b)
    """
    
    guessed = False
    n = random.randint(1, 100)
    
    while not guessed:
        guess = int(input("Enter a guess (i.e. 3): "))
        
        if guess == n:
            print("You guessed it!")
            guessed = True
        elif guess <= 100 and guess > n:
            print("Too high!")
        elif guess >= 1 and guess < n:
            print("Too low!")
        else:
            print("Out of bounds!")
                    
print(divisible_by_3(6)) # True
print(divisible_by_3(2)) # False
print(sqrt(4)) # 2.0
print(sqrt(5)) # ~2.236
guess_the_number() # Play the game