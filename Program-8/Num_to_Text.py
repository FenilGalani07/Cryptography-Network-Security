# number_to_words.py

def number_to_words(n):
    if n < 0:
        return "minus " + number_to_words(-n)
    elif n == 0:
        return "zero"

    words = {
        1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
        6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
        11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
        15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen",
        20: "twenty", 30: "thirty", 40: "forty", 50: "fifty",
        60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"
    }

    if n < 100:
        if n in words:
            return words[n]
        else:
            tens = (n // 10) * 10
            units = n % 10
            return words[tens] + (" " + words[units] if units else "")
    
    elif n < 1000:
        hundreds = n // 100
        remainder = n % 100
        return words[hundreds] + " hundred" + (" and " + number_to_words(remainder) if remainder else "")
    
    else:
        return "Number out of range"

if __name__ == "__main__":
    try:
        number = int(input("Enter a number (0-999): "))
        if 0 <= number < 1000:
            print(f"{number} in words is: {number_to_words(number)}")
        else:
            print("Please enter a number between 0 and 999.")
    except ValueError:
        print("Please enter a valid integer.")