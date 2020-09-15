"""
Chapter : 6 - item : 5 - Radix Sort (น้อยไปมาก)
ให้น้องๆใช้ Linked List (เขียนเป็น class)  ในการทำ Radix Sort  (มีอยู่ในสไลด์เรียน 2 หน้าสุดท้าย)  ในรูปแบบน้อยไปมาก

โดยผลลัพธ์ให้ออกมาเป็นการทำ Radix Sort แบบจำนวนรอบน้อยที่สุด และแสดงผลในแต่ละรอบว่าได้ผลลัพธ์เป็นอย่างไร  
3 บรรทัดสุดท้ายจะเป็น ( จำนวนรอบที่น้อยที่สุด , Data ก่อนทำ Radix Sort และ Data หลังทำ Radix Sort )
"""

"""
Test Cases

Testcase : #1 1
Enter Input : 64 8 216 512 27 729 0 1 343 125
------------------------------------------------------------
Round : 1
0 : 0 
1 : 1 
2 : 512 
3 : 343 
4 : 64 
5 : 125 
6 : 216 
7 : 27 
8 : 8 
9 : 729 
------------------------------------------------------------
Round : 2
0 : 0 1 8 
1 : 216 512 
2 : 27 125 729 
3 : 
4 : 343 
5 : 
6 : 64 
7 : 
8 : 
9 : 
------------------------------------------------------------
Round : 3
0 : 0 1 8 27 64 
1 : 125 
2 : 216 
3 : 343 
4 : 
5 : 512 
6 : 
7 : 729 
8 : 
9 : 
------------------------------------------------------------
Round : 4
0 : 0 1 8 27 64 125 216 343 512 729 
1 : 
2 : 
3 : 
4 : 
5 : 
6 : 
7 : 
8 : 
9 : 
------------------------------------------------------------
3 Time(s)
Before Radix Sort : 64 -> 8 -> 216 -> 512 -> 27 -> 729 -> 0 -> 1 -> 343 -> 125
After  Radix Sort : 0 -> 1 -> 8 -> 27 -> 64 -> 125 -> 216 -> 343 -> 512 -> 729

Testcase : #2 2
Enter Input : -123 456 -789 0 27 3645 133 -142 -5038594 15615 668 2 -1 72
------------------------------------------------------------
Round : 1
0 : 0 
1 : -1 
2 : -142 2 72 
3 : -123 133 
4 : -5038594 
5 : 3645 15615 
6 : 456 
7 : 27 
8 : 668 
9 : -789 
------------------------------------------------------------
Round : 2
0 : -1 0 2 
1 : 15615 
2 : -123 27 
3 : 133 
4 : -142 3645 
5 : 456 
6 : 668 
7 : 72 
8 : -789 
9 : -5038594 
------------------------------------------------------------
Round : 3
0 : -1 0 2 27 72 
1 : -142 -123 133 
2 : 
3 : 
4 : 456 
5 : -5038594 
6 : 668 3645 15615 
7 : -789 
8 : 
9 : 
------------------------------------------------------------
Round : 4
0 : -789 -142 -123 -1 0 2 27 72 133 456 668 
1 : 
2 : 
3 : 3645 
4 : 
5 : 15615 
6 : 
7 : 
8 : -5038594 
9 : 
------------------------------------------------------------
Round : 5
0 : -789 -142 -123 -1 0 2 27 72 133 456 668 3645 
1 : 15615 
2 : 
3 : -5038594 
4 : 
5 : 
6 : 
7 : 
8 : 
9 : 
------------------------------------------------------------
Round : 6
0 : -5038594 -789 -142 -123 -1 0 2 27 72 133 456 668 3645 15615 
1 : 
2 : 
3 : 
4 : 
5 : 
6 : 
7 : 
8 : 
9 : 
------------------------------------------------------------
5 Time(s)
Before Radix Sort : -123 -> 456 -> -789 -> 0 -> 27 -> 3645 -> 133 -> -142 -> -5038594 -> 15615 -> 668 -> 2 -> -1 -> 72
After  Radix Sort : -5038594 -> -789 -> -142 -> -123 -> -1 -> 0 -> 2 -> 27 -> 72 -> 133 -> 456 -> 668 -> 3645 -> 15615

Testcase : #3 3
Enter Input : -1 -9 -3 -6 -5 -4 -7 0 -8 -2 3 2 5 1 4 9 8 7 6
------------------------------------------------------------
Round : 1
0 : 0 
1 : -1 1 
2 : -2 2 
3 : -3 3 
4 : -4 4 
5 : -5 5 
6 : -6 6 
7 : -7 7 
8 : -8 8 
9 : -9 9 
------------------------------------------------------------
Round : 2
0 : -9 -8 -7 -6 -5 -4 -3 -2 -1 0 1 2 3 4 5 6 7 8 9 
1 : 
2 : 
3 : 
4 : 
5 : 
6 : 
7 : 
8 : 
9 : 
------------------------------------------------------------
1 Time(s)
Before Radix Sort : -1 -> -9 -> -3 -> -6 -> -5 -> -4 -> -7 -> 0 -> -8 -> -2 -> 3 -> 2 -> 5 -> 1 -> 4 -> 9 -> 8 -> 7 -> 6
After  Radix Sort : -9 -> -8 -> -7 -> -6 -> -5 -> -4 -> -3 -> -2 -> -1 -> 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9

Testcase : #4 4
Enter Input : 15 -15
------------------------------------------------------------
Round : 1
0 : 
1 : 
2 : 
3 : 
4 : 
5 : -15 15 
6 : 
7 : 
8 : 
9 : 
------------------------------------------------------------
Round : 2
0 : 
1 : -15 15 
2 : 
3 : 
4 : 
5 : 
6 : 
7 : 
8 : 
9 : 
------------------------------------------------------------
Round : 3
0 : -15 15 
1 : 
2 : 
3 : 
4 : 
5 : 
6 : 
7 : 
8 : 
9 : 
------------------------------------------------------------
2 Time(s)
Before Radix Sort : 15 -> -15
After  Radix Sort : -15 -> 15

Testcase : #5 ึ7
Enter Input : 100 0 10
------------------------------------------------------------
Round : 1
0 : 0 10 100 
1 : 
2 : 
3 : 
4 : 
5 : 
6 : 
7 : 
8 : 
9 : 
------------------------------------------------------------
0 Time(s)
Before Radix Sort : 100 -> 0 -> 10
After  Radix Sort : 0 -> 10 -> 100

"""