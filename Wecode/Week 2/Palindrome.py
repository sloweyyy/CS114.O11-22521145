def is_palindrome(s):
    return s == s[::-1]


def count_palindromic_substrings(s):
    count = 0

    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substring = s[i:j]

            if is_palindrome(substring):
                count += 1

    return count


input_string = input().strip()

result = count_palindromic_substrings(input_string)
print(result)
