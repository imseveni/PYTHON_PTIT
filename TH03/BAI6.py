# Có N thùng nước được đánh số từ 1 đến N, 
# giữa 2 thùng bất kỳ đều có một ống nối có một van có thể khóa hoặc mở. 
# Ở trạng thái ban đầu tất cả các van đều đóng.
# Bạn được cho một số yêu cầu, trong đó mỗi yêu cầu có 2 dạng:
# Dạng X Y 1 có ý nghĩa là bạn cần mở van nối giữa 2 thùng X và Y.
# Dạng X Y 2 có ý nghĩa là bạn cần cho biết với trạng thái các van 
# đang mở / khóa như hiện tại thì 2 thùng X và Y có thuộc cùng một nhóm bình thông nhau hay không?
# Hai thùng được coi là thuộc cùng một nhóm bình thông nhau nếu nước từ bình này
# có thể chảy đến được bình kia qua một số ống có van đang mở.I
# 
# nput:
# Dòng đầu tiên là số lượng truy vấn Q (Q <= 100 000).
# Mỗi truy vấn gồm 3 số nguyên X, Y, Z (X, Y <= 100 000).
# 
# Output:
# Với mỗi truy vấn, in ra đáp án tìm được trên một dòng.

MAX = 100000

par = list(range(MAX + 1))
size = [1] * (MAX + 1)

def findroot(x):
    if par[x] != x:
        par[x] = findroot(par[x])
    return par[x]

def Union(a, b):
    a = findroot(a)
    b = findroot(b)

    if a == b:
        return

    if size[a] < size[b]:
        a, b = b, a

    par[b] = a
    size[a] += size[b]

for _ in range(int(input())):
    x, y, z = map(int, input().split())

    if z == 1:
        Union(x, y)
    else:
        if findroot(x) == findroot(y):
            print(1)
        else:
            print(0)