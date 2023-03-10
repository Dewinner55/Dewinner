# def func(list_: list) -> list:
#     res = "".join(list(map(str, list_)))
#     res = int(res) + 1
#     res1 = list(str(res))
#     print(res1)
#     res1 = list(map(int, res1))
#     # print(res1, type(res1))
#     return res1


# print(func([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.
"""
"""
1) Input: s = "III"
Output: 3
Explanation: III = 3.

2) Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

3) Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""

# num = input()


# def func(num=input()):
#     I = 1
#     V = 5
#     X = 10
#     L = 50
#     C = 100
#     D = 500
#     M = 1000

#     return

# print(func(input()))

# def roman(s: str) -> int:

#     dict_ = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
#     s = list(s)
#     list_ = []

#     for i in s:
#         num = dict_[i]
#         list_.append(num)

#     list_new = list_[::-1]
#     i = 0
#     last = list_new[0]

#     for x in list_new:
#         if x < last:
#             i -= x
#         else:
#             i += x
#         last = x
#     return i


# print(roman("MCMXCIV"))

"""
Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.

A string is represented by an array if the array elements concatenated in order forms the string."""
"""
Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
Output: true
Explanation:
word1 represents string "ab" + "c" -> "abc"
word2 represents string "a" + "bc" -> "abc"
The strings are the same, so return true.
"""

"""
Input: word1 = ["a", "cb"], word2 = ["ab", "c"]
Output: false
"""
"""
Input: word1  = ["abc", "d", "defg"], word2 = ["abcddefg"]
Output: true
"""

# На входе имеем список строк разной длины.
# Необходимо написать функцию all_eq(lst), которая вернет новый список из строк одинаковой длины.
# Длину итоговой строки определяем исходя из самой большой из них.
# Если конкретная строка короче самой длинной, дополнить ее нижними подчеркиваниями с правого края до требуемого количества символов.
# Расположение элементов начального списка не менять.

# Input: ['a', 'aa', 'aaa', 'aaaa', 'aaaaa']
# Output: ['a____', 'aa___', 'aaa__', 'aaaa_', 'aaaaa']

# lst = ["a", "aa", "aaa", "aaaa", "aaaaa"]


# def all_eq(lst):
#     list_ = max(lst)
#     podcherkivanie2 = "_"
#     podcherkivanie = "_" * len(lst)
#     print([podcherkivanie])
#     # podcherkivanie = podcherkivanie * 2
#     for x in lst:
#         # print(len(x))
#         # print(x)
#         y = x * (podcherkivanie2 * (len(podcherkivanie) - len(x)))
#         # x = x * y
#         # z = y * x
#         # print(x)
#         print(y)
#     # print(x)
#     # return list_
#     # print(podcherkivanie)


# print(all_eq(lst))

# Дано предложение "Это короткое предложение", оно может быть перетасовано как "предложение3 короткое2 Это1" или "короткое2 предложение3 Это1".
# Учитывая перетасованные предложения, содержащие не более 9 слов, восстановите и верните исходное предложение, удалив цифры в конце слов.

# Input: s = "is2 sentence4 This1 a3"
# Output: "This is a sentence"
# """

# def func(text_: str) -> str:
#     text_ = text_.split()
#     text_.sort(key=lambda x: x[-1])
#     list_ = []
#     for x in text_:
#         x = x[:-1]
#         list_.append(x)
#     text_ = " "
#     for x in list_:
#         text_ += f"{x} "
#     text_.strip()

#     # print(type(text1))
#     return text_


# print(func("is2 sentence4 This1 a3 for1"))
