"""
Chapter : 6 - item : 4 - หา loop ใน linked list
ให้ตรวจสอบว่า linked list มีการวนซ้ำหรือไม่ และ แสดงผลลัพธ์ตามตัวอย่าง

โดยมีการรับ input ดังนี้

1. append ->   A <int> คือ เพิ่มข้อมูลต่อท้าย linked list

2. set_next -> S <index1(int):index2(str)> คือการ set node.next ของ node index ที่1 ให้ชี้ไป node index ที่2

ซึ่งหากไม่มี  node index ที่1 ใน linked list ให้แสดง error และหากไม่มี node index ที่2 ใน linked list
ให้ทำการ append nodeใหม่เข้าไปใน linked list โดยมี value = index2
"""

"""
Test Cases
Testcase : #1
Enter input : A 0,A 1,S 2:0
0
0->1
Error! {index not in length}: 2
No Loop
0->1

Testcase : #2
Enter input : A 0,A 1,S 0:2
0
0->1
index not in length, append : 2
No Loop
0->1->2

Testcase : #3
Enter input : A 0,A 1,S 1:0
0
0->1
Set node.next complete!, index:value = 1:1 -> 0:0
Found Loop

Testcase : #4
Enter input : S 0:0
Error! {list is empty}
No Loop
Empty

Testcase : #5
Enter input : A 0,A 3,A 5,A 7,A 9,S 2:0
0
0->3
0->3->5
0->3->5->7
0->3->5->7->9
Set node.next complete!, index:value = 2:5 -> 0:0
Found Loop

Testcase : #6
Enter input : A 0,A 1,A 2,S 0:2
0
0->1
0->1->2
Set node.next complete!, index:value = 0:0 -> 2:2
No Loop
0->2

"""