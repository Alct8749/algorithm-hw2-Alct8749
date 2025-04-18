# 모든 경우를 테스트 할 때:
#    pytest test_closestPair.py
# 개별적으로 테스트 할 때 (method=1, bin_file=tuple1000.bin 경우)
#    pytest test_closestPair.py -k "test_cp[1-tuple1000.bin]"
import pytest
import struct
from closestPair import Point, closest1, closest2, closest3

@pytest.mark.parametrize("bin_file", ["tuple1000.bin", "tuple2500.bin", "tuple10000.bin"])
@pytest.mark.parametrize("method", [1, 2, 3])
def test_cp(bin_file, method):
    err = 0.1
    points = []
    try:
        with open(bin_file, 'rb') as f:
            while True:
                data = f.read(8)  # 각 튜플 (a, b)는 두 개의 정수 (각 4바이트)
                if not data:
                    break
                a, b = struct.unpack('ii', data)
                points.append(Point(a, b))
    except FileNotFoundError:
        assert False, f"{bin_file} cannot be found."

    if bin_file == "tuple1000.bin":
        threshold = 4.473
    elif bin_file == "tuple2500.bin":
        threshold = 1.000
    elif bin_file == "tuple10000.bin":
        threshold = 1.000
    else:
        assert False, f"file {bin_file} is not allowed."

    if method == 1:    
        (p1, p2), dist = closest1(points)
    elif method == 2:
        (p1, p2), dist = closest2(points)
    elif method == 3:    
        (p1, p2), dist = closest3(points)
    else:
        assert False, f"method {method} is not allowd."

    assert threshold - err <= dist and dist <= threshold + err, f"{dist} is not the closest distance"
