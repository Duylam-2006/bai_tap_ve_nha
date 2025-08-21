import time

# 1. Hàm đệ quy
def dequy(n):
    if n == 0:
        return 2
    return 3 * dequy(n - 1) - 4

# 2. Hàm công thức nghiệm tổng quát
def congthuc(n):
    return 4 * (3 ** n) - 2

# 3. So sánh tốc độ với n = 30
n = 30

# Đệ quy
start = time.time()
kq1 = dequy(n)
end = time.time()
print("Kết quả (Đệ quy):", kq1, " | Thời gian:", end - start)

# Công thức
start = time.time()
kq2 = congthuc(n)
end = time.time()
print("Kết quả (Công thức):", kq2, " | Thời gian:", end - start)
