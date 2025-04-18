[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/Cy1PUpKd)
# Algorithm1 Homework2
3 종류의 closest pair 알고리즘을 구현한다.

### 과제 내용
 - 제공되는 closestPair.py 파일은 인자로 주어지는 이진 파일에서 2차원 평면상의 점들을 읽어 3개의 함수에서 각각 closest pair를 구하여 실행시간과 같이 출력한다. 하지만 그 내용이 제대로 구현되어 있지 않고 더미값을 반환한다. 세 함수는 아래와 같다.
   * closest1(points) : 점들의 리스트 points에서 가장 가까운 두 점을 구하는 함수이며 $O(n^2)$의 시간복잡도를 가지는 closestpair algorithm이 구현된다. 구한 두 점과 거리를 반환한다.
   * closest2(points) : $O(n \log^2{n})$의 시간복잡도를 가지는 closestpair algorithm이 구현된다.   
   * closest3(points) : $O(n \log{n})$의 시간복잡도를 가지는 closestpair algorithm이 구현된다.
 - 이 프로그램을 모두 구현하면 다음과 같이 실행할 수 있다.

   `python closestPair.py tuple5.bin`
   * 여기서 tuple5.bin 파일은 다음 5개의 점들이 저장된 이진파일이며 closestPair.py가 실행될 때 points 리스트에 저장된다.
     + (3, 3)
     + (1, 4)
     + (4, 3)
     + (4, 1)
     + (4, 4)
   * 여기서 closest pair는 (4, 3)와 (4, 4)로 그 거리가 1.0이다. 이 이진파일을 통해 구현된 프로그램의 정상 실행여부를 확인할 수 있다.
 - 또한, tuple1000.bin, tuple2500.bin, 그리고 tuple10000.bin 파일도 인자에 넣어 실행여부를 확인할 수 있다.
 - makePF.py를 통해 점의 이진 파일을 만들 수 있다. 그 작동 원리는 소스코드를 확인하기 바란다.
 - readPF.py를 통해 이진 파일의 일부를 볼 수 있다. 

### 과제 평가
 - 완성된 프로그램의 평가는 다음 명령어들로 이루어진다. 대괄호 안의 첫 번째 숫자는 세 closestPair 함수 중 어떤 것을 호출할 것인지를 결정하며, 두 번째 이진 파일명은 테스트에 사용할 이진 파일을 가리킨다. 제대로 실행된 경우 passed가 출력된다.
   
   `pytest test_closestPair.py -k "test_cp[1-tuple1000.bin]"`

   `pytest test_closestPair.py -k "test_cp[1-tuple2500.bin]"`

   `pytest test_closestPair.py -k "test_cp[1-tuple10000.bin]"`

   `pytest test_closestPair.py -k "test_cp[2-tuple1000.bin]"`

   `pytest test_closestPair.py -k "test_cp[2-tuple2500.bin]"`

   `pytest test_closestPair.py -k "test_cp[2-tuple10000.bin]"`

   `pytest test_closestPair.py -k "test_cp[3-tuple1000.bin]"`

   `pytest test_closestPair.py -k "test_cp[3-tuple2500.bin]"`

   `pytest test_closestPair.py -k "test_cp[3-tuple10000.bin]"`

   
   
