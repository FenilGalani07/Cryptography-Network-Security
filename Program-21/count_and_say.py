# count_and_say.py

def count_and_say(number):
    number_str = str(number)
    result = []
    count = 1

    for i in range(1, len(number_str)):
        if number_str[i] == number_str[i - 1]:
            count += 1
        else:
            result.append(f"{count} {number_str[i - 1]}'s")
            count = 1


    result.append(f"{count} {number_str[-1]}'s")

    return ', '.join(result)

if __name__ == "__main__":
    input_number = input("Enter a number: ")
    result_description = count_and_say(input_number)
    print(f"Count and say result: {result_description}")