# # про tuple 
# num = (1,2,3,4,5,6)
# ls = [1,2,3,4,5]

# tp = (1,8,3,4,5,8,8,9,2)
# target = 8
# tp1 = tp.index(8)
# tp2 = tp.index(8, 2)
# if tp.count(8)>1:
#     first = tp.index(8)
#     second = tp.index(8, 2)
#     print(first, second)
# result = tp[first: second]
# result2 = tp[tp1: tp2]
# print(result2)

# print(tp4)
# print((tp1, tp2))
# print(dir(tuple))
# tp1 = len(tp)
# print(tp1)
# outup (8,3,4,5,8)


# tp = (1,2,3,8,5,1,2)
# target = 2
# tp1 = tp.index(target)
# tp2 = tp.index(target, 2 + 1)
# result = tp[tp1:]
# print(result)

# output = (8,5,1,2)


# tp = (1,2,3,8,5,1,2)
# target = 2
# if tp.count(8)>1:
#     first = tp.index(target)
#     second = tp.index(target, first + 1)
#     result = tp[first: second + 1]
# else:
#     first = tp.index(target)
#     result = tp[first:]
# print(tp, target)
# print(result)

# nums = [2,7,11,15]
# target = 18
# nums1 = tuple(nums)
# nums2 = sum(nums1)
# nums3 = nums[0]
# nums4 = nums[1]
# nums5 = nums[2]
# nums6 = nums[3]
# if nums3 + nums4 == target:
#     print(nums3, "+", nums4, target)
# elif nums3 + nums5 == target:
#     print(nums3, "+", nums5, target)
# elif nums3 + nums6 == target:
#     print(nums3, "+", nums6, target)
# elif nums4 + nums5 == target:
#     print(nums4, "+", nums5, target)
# elif nums4 + nums6 == target:
#     print(nums4, "+", nums6, target)
# elif nums5 + nums6 == target:
#     print(nums5, "+", nums6, target)
# else:
#     print("no")


# nums = [2,7,11,15]
# target = 18

# for x in nums:
#     num = target - x
#     if num in nums:
#         if num == x:
#             continue
#         print(nums.index(x), nums.index(num))
#         break
# num = (24,21,17,16)
# Мурат = num[1]
# Эранжу = num[2]
# Алтынай = num[3]
# Айбек = num[4]
# # if num >= 21:
#   print(Мурат)num = [24,21,17,16]
# Мурат = num[1]
# print(Мурат)

# a = {'Jane', 'Eyre', 22}
# a2 = {'Hello world!'}
# print(a+a2)

# a = {'a': 1, 'b': 2, 'c': 1}
# a = a.keys()
# a = list(a)
# print(a)

# a = {'a': 1, 'b': 2, 'c': 1}
# for x in a:
#     print(x)

# a = {'a': 1, 'b': 4, 'c': 1, 'd': 5, 'e': 6} 
# for k, v in a.items():
#     if v % 2 != 0:
      
#       print(a)