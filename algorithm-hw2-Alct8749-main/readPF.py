# 이진 파일에서 튜플 읽기
import struct
import sys

if len(sys.argv) != 2:
    print("Usage: python readPF.py <pf_file>")
    sys.exit(1)

random_tuples = []
with open(sys.argv[1], 'rb') as f:
    while True:
        data = f.read(8)  # 각 튜플 (a, b)는 두 개의 정수 (각 4바이트)로 저장됨
        if not data:
            break
        a, b = struct.unpack('ii', data)
        if a < 0 or b < 0:
            print("a:", a, "b:", b)
            break
        if a >= 10000 or b >= 10000:
            print("a:", a, "b:", b)
            break
        random_tuples.append((a, b))

# 첫 10개의 튜플을 출력하여 확인
print("이진 파일에서 읽은 첫 10개의 튜플:")
for i in range(min(10, len(random_tuples))):
    print(random_tuples[i])
