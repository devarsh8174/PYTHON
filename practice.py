ls = []
n =int(input("enter no of elements "))
for i in range(n):
    m = int(input("enter elements "))
    ls.append(m)
ls1 = []
ls2 = []
ls.sort(reverse=True)
print(ls)
total = sum(ls)
print(total)
half = sum(ls) //2
print(half)

if total%2 == 0 and half <= max(ls):

    for i in ls:
        if sum(ls1)<sum(ls2):

            ls.append(i)
        else:
            ls.append(i)

    if sum(ls1) == sum(ls2):
        print(ls1)
        print(ls2)

        print(sum(ls1))
        print(sum(ls2))

    else:
        s1 = sum(ls1)
        s2 = sum(ls2)

        for i in ls1:

            for j in ls2 :

                temp1 = s1 - i + j
                temp2 = s2 - j + i

                if temp1  == temp2:
                    ls1.remove(i)
                    ls2.append(i)
                    ls2.remove(j)
                    ls1.append(j)
                    break

        print(ls1,'=',sum(ls1))
        print(ls2,'=',sum(ls2))
else:
    print("not possible for this list ")


