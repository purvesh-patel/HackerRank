x = 1
y = 1
z = 1
n = 2

#print([[x, y] for x in [1, 2, 3] for y in [4, 5, 6]])

l = ([[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1)])
print(l, "\nlen: ", len(l))

# nl = []
#
# for i in l:
#     if sum(i) != n:
#         #print(i)
#         nl.append(i)
#
# print(nl)

f = [i for i in l if sum(i) != n]
print(sorted(f))
