from math import gcd


class PhanSo:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau

    def rut_gon(self):
        g = gcd(self.tu, self.mau)

        self.tu //= g
        self.mau //= g

    def __add__(self, other):
        tu_moi = self.tu * other.mau + self.mau * other.tu
        mau_moi = self.mau * other.mau

        res = PhanSo(tu_moi, mau_moi)
        res.rut_gon()

        return res

    def __str__(self):
        return f"{self.tu}/{self.mau}"

a, b, c, d = map(int, input().split())

p1 = PhanSo(a, b)
p2 = PhanSo(c, d)

tong = p1 + p2

print(tong)