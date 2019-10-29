# Common Words
#
# def checkio(first, second):
#     first_str = first.split(',')
#     second_str = second.split(',')
#
#     result = []
#
#     for el in second_str:
#         if el in first_str and el not in result:
#             result.append(el)
#
#         result.sort()
#     return str(result)
#
#
# Group Equal consecutive
#
# def group_equal(els):
#     els_set = set(els)
#     result = []
#     for el in els_set:
#         result.append([el] * els.count(el))
#     return result
#
#
# group_equal([])
