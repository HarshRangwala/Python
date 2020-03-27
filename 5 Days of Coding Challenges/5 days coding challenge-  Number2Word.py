def as_words(n):
    """Convert an integer n (+ve or -ve) to English words."""
    # lookups
    ones = ['zero', 'one', 'two', 'three', 'four',
            'five', 'six', 'seven', 'eight', 'nine', 
            'ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
            'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    tens = ['zero', 'ten', 'twenty', 'thirty', 'forty',
            'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    # negative case
    if n < 0:
        return "negative {0}".format(as_words(abs(n)))
    # 1000+
    for order, word in [(10**12, "trillion"), (10**9, "billion"),
                        (10**6, "million"), (10**3, "thousand")]:
        if n >= order:
            return "{0} {1}{2}".format(as_words(n // order), word,
                                       " {0}".format(as_words(n % order))
                                       if n % order else "")
    # 100-999
    if n >= 100:
        if n % 100:
            return "{0} hundred and {1}".format(as_words(n // 100), 
                                                as_words(n % 100))
        else:
            return "{0} hundred".format(as_words(n // 100))
    # 0-99
    if n < 20:
        return ones[n]
    else:
        return "{0}{1}".format(tens[n // 10],
                               "-{0}".format(as_words(n % 10)) 
                               if n % 10 else "")   
print(as_words(-5))
print(as_words(1200))
print(as_words(123000123))

#Second solution to this prolem
#Run the command pip install inflect on terminal
#run following code
import inflect
p = inflect.engine()
wordedint = p.number_to_words(-5)
wordedint1 = p.number_to_words(1200)
wordedint2 = p.number_to_words(123000123)
print()
print("Second solution output: \n", wordedint)
print("Second solution output: \n", wordedint1)
print("Second solution output: \n", wordedint2)