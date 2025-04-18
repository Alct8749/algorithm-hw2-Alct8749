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
    min_dist = float('inf')
    pair = (None, None)
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            d = distance(points[i], points[j])
            if d < min_dist:
                min_dist = d
                pair = (points[i], points[j])
    return pair, min_dist

def closest2(points):
    def closest_pair(px):
        n = len(px)
        if n <= 3:
            return closest1(px)
        mid = n // 2
        Qx = px[:mid]
        Rx = px[mid:]

        (p1, q1), dist1 = closest_pair(Qx)
        (p2, q2), dist2 = closest_pair(Rx)

        d = min(dist1, dist2)
        pair = (p1, q1) if dist1 < dist2 else (p2, q2)

        mid_x = px[mid].x
        strip = [p for p in px if abs(p.x - mid_x) < d]
        strip.sort(key=lambda point: point.y)

        for i in range(len(strip)):
            for j in range(i + 1, len(strip)):
                if strip[j].y - strip[i].y >= d:
                    break
                d_temp = distance(strip[i], strip[j])
                if d_temp < d:
                    d = d_temp
                    pair = (strip[i], strip[j])
        return pair, d

    px = sorted(points, key=lambda p: p.x)
    return closest_pair(px)

def closest3(points):
    def closest_pair(px, py):
        n = len(px)
        if n <= 3:
            return closest1(px)

        mid = n // 2
        mid_x = px[mid].x

        Qx = px[:mid]
        Rx = px[mid:]

        Qy = list(filter(lambda p: p.x <= mid_x, py))
        Ry = list(filter(lambda p: p.x > mid_x, py))

        (p1, q1), dist1 = closest_pair(Qx, Qy)
        (p2, q2), dist2 = closest_pair(Rx, Ry)

        d = min(dist1, dist2)
        pair = (p1, q1) if dist1 < dist2 else (p2, q2)

        strip = [p for p in py if abs(p.x - mid_x) < d]

        for i in range(len(strip)):
            for j in range(i + 1, min(i + 7, len(strip))):
                d_temp = distance(strip[i], strip[j])
                if d_temp < d:
                    d = d_temp
                    pair = (strip[i], strip[j])
        return pair, d

    px = sorted(points, key=lambda p: p.x)
    py = sorted(points, key=lambda p: p.y)
    return closest_pair(px, py)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python closestPair.py <pair_bin_file>")
        sys.exit(1)

    points = []
    with open(sys.argv[1], 'rb') as f:
        while True:
            data = f.read(8)
            if not data:
                break
            a, b = struct.unpack('ii', data)
            points.append(Point(a, b))

    for i, func in enumerate([closest1, closest2, closest3], 1):
        start_time = time.perf_counter()
        (p1, p2), min_dist = func(points)
        end_time = time.perf_counter()
        print(f"[closest{i}] 가장 가까운 두 점: ({p1.x}, {p1.y})와 ({p2.x}, {p2.y})")
        print(f"[closest{i}] 거리: {min_dist:.6f}")
        print(f"[closest{i}] 실행 시간: {end_time - start_time:.6f} 초\n")
