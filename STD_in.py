import sys

def beauty(x, y, n, a):
    count = 0
    length = n
    for i in range(0,length):
        for j in range(i+1, length):
            if(i !=j ):
                sum =  a[i] + a[j]
                diff = a[i] - a[j]
                if sum % x == 0 and diff % y == 0 :
                    count = count + 1
            # print(a[i], a[j])         
    return count


# Inputter Block

index = 0
for line in sys.stdin:
    if 'q' == line.rstrip():
        break
    index = index + 1
    if index == 1:
        t = str(line)
    if((index-1) % 2 == 1 and index!= 1):
        [n, x, y] = [int(x) for x in line.split()]
    if((index-1) % 2 == 0 and index!= 1):
        a = [int(x) for x in line.split()]

        # use the function here 
        ans = beauty(x, y, n, a)

        sys.stdout.write(str(ans) +'\n')


