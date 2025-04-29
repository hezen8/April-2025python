def sum(*nums):
    total=0
    for x in nums:
        total=total+ x
    return total
print(sum(2,5,8,9,12,34,65,78,13))