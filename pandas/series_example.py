import pandas
s = pandas.Series(range(4), index=['a', 'b', 'c', 'd'])
print(s)
print(s > 1)
s_gt_1 = s[s > 1]
print(s_gt_1)
print(s_gt_1.mean())