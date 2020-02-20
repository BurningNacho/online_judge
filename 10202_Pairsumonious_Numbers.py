# For 10 > N > 2 numbers we form N ∗ (N − 1)/2 sums by adding every pair of the
# numbers. Your task is to find the N numbers given the sums.

# Input
# Each line of input contains N followed by N ∗ (N − 1)/2 integer numbers separated by a space.
# Output
# For each line of input, output one line containing N integers in non-descending order such that the
# input numbers are pairwise sums of the N numbers. If there is more than one solution, any one will
# do; if there is no solution, print ‘Impossible’.

# Sample Input
# 3 1269 1160 1663
# 3 1 1 1
# 5 226 223 225 224 227 229 228 226 225 227
# 5 216 210 204 212 220 214 222 208 216 210
# 5 -1 0 -1 -2 1 0 -1 1 0 -1
# 5 79950 79936 79942 79962 79954 79972 79960 79968 79924 79932

# Sample Output
# 383 777 886
# Impossible
# 111 112 113 114 115
# 101 103 107 109 113
# -1 -1 0 0 1
# 39953 39971 39979 39983 39989



## Impossible
# N=7; A B C D E F G (in order) A smallest
# y1+y2-yi=2A
# Vi: (y1+y2-yi)%2 == 0 ? Impossible


if __name__ == '__main__':
    line = input().strip()
    numbers = int(line.split(' ')[0])
