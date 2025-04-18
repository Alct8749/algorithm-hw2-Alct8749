import math
import time
import struct
import sys

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def distance(p1, p2):
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

def closest1(points):
    # 두 점들의 거리를 모두 계산

    # 아래 코드는 더미 값을 반환함
    pair = (points[0], points[1])
    dist = 56.4
    return pair, dist

def closest2(points):
    # points를 x좌표로만 정렬

    # recursive한 closest_pair2() 함수를 호출
    
    # 아래 코드는 더미 값을 반환함
    pair = (points[0], points[1])
    dist = 123.9
    return pair, dist

def closest3(points):
    # points를 x좌표와 y좌표로 각각 정렬

    # recursive한 closest_pair3() 함수를 호출
    
    # 아래 코드는 더미 값을 반환함
    pair = (points[0], points[1])
    dist = 133.2
    return pair, dist

# 사용 예시
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python closestPair.py <pair_bin_file>")
        sys.exit(1)

    points = []
    with open(sys.argv[1], 'rb') as f:
        while True:
            data = f.read(8)  # 각 튜플 (a, b)는 두 개의 정수 (각 4바이트)
            if not data:
                break
            a, b = struct.unpack('ii', data)
            points.append(Point(a, b))

    start_time = time.perf_counter()
    (p1, p2), min_dist = closest3(points)
    end_time = time.perf_counter()
    print(f"가장 가까운 두 점: ({p1.x}, {p1.y})와 ({p2.x}, {p2.y})")
    print(f"거리: {min_dist:.6f}")
    execution_time = end_time - start_time
    print(f"평균 실행 시간 ({norep}번 실행): {execution_time:.6f} 초")

    start_time = time.perf_counter()
    (p1, p2), min_dist = closest2(points)
    end_time = time.perf_counter()
    print(f"가장 가까운 두 점: ({p1.x}, {p1.y})와 ({p2.x}, {p2.y})")
    print(f"거리: {min_dist:.6f}")
    execution_time = end_time - start_time
    print(f"평균 실행 시간 ({norep}번 실행): {execution_time:.6f} 초")

    start_time = time.perf_counter()
    (p1, p2), min_dist = closest1(points)
    end_time = time.perf_counter()
    print(f"가장 가까운 두 점: ({p1.x}, {p1.y})와 ({p2.x}, {p2.y})")
    print(f"거리: {min_dist:.6f}")
    execution_time = end_time - start_time
    print(f"평균 실행 시간 ({norep}번 실행): {execution_time:.6f} 초")

