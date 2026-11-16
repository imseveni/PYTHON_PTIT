class Phim:
    def __init__(self, ma_phim, the_loai, ngay_khoi_chieu, ten_phim, so_tap):
        self.ma_phim = 'P{:03d}'.format(ma_phim)
        self.the_loai = the_loai
        self.ten_phim = ten_phim
        self.ngay_khoi_chieu = ngay_khoi_chieu
        self.ngay = int(ngay_khoi_chieu[:2:])
        self.thang = int(ngay_khoi_chieu[3:5:])
        self.nam = int(ngay_khoi_chieu[6::])
        self.so_tap = so_tap

    def __str__(self):
        return self.ma_phim + ' ' + self.the_loai + ' ' + self.ngay_khoi_chieu + ' ' + self.ten_phim + ' ' + str(self.so_tap)

n, m = map(int, input().split())

tl = []
p = []

for i in range(n): tl.append(input())

for i in range(m):
    the_loai = input()
    ngay_khoi_chieu = input()
    ten_phim = input()
    so_tap = int(input())

    p.append(Phim(i + 1, tl[int(the_loai[2::]) - 1], ngay_khoi_chieu, ten_phim, so_tap))

p = sorted(p, key = lambda x : (x.nam, x.thang, x.ngay, x.ten_phim, -x.so_tap))

for i in range(m) :
    print(p[i])