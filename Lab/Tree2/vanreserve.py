"""
Chapter : 8 - item : 5 - จองรถตู้
 ส่งมาแล้ว 0 ครั้ง
บริษัทแห่งหนึ่งมีรถตู้ K คันที่ลูกค้าสามารถเช่าไปใช้งานได้ โดยรถตู้แต่ละคันมีรหัสประจำตัวรถเป็นหมายเลขจำนวนเต็มบวกตั้งแต่ 1 จนถึง K ข้อกำหนดในการเลือกรถตู้ให้ลูกค้ามีอยู่ว่า ลูกค้าจะต้องทำการจองรถตู้ก่อน โดยคำสั่งจองจะต้องระบุจำนวนวันที่จะใช้ จากนั้นผู้จองจะได้รถตู้ที่ว่างให้ใช้เร็วที่สุดเท่าที่จะหาได้จากรถตู้ทั้งหมด

ในกรณีที่มีรถตู้ว่างให้ใช้เร็วที่สุดมากกว่า 1 คัน คันที่มีรหัสประจำรถน้อยกว่าจะถูกเลือกก่อน เช่นถ้าหากมีรถตู้ที่ว่างให้ใช้เร็วที่สุด 3 คัน  ซึ่งมีรหัสประจำรถเป็น 5 , 7 และ 20 รถตู้ที่มีหมายเลข 5 จะถูกเลือกก่อน นอกจากนี้การจองจะให้ความสำคัญกับคำสั่งจองที่มาก่อนเสมอ สำหรับการจองแต่ละครั้ง ผู้จองจะได้รับคำตอบกลับมาว่าได้ใช้รถตู้หมายเลขใด  โดยในตอนแรกรถตู้ทุกคันจะว่างและพร้อมใช้งานทั้งหมด

อธิบาย Input โดย Input จะแบ่งเป็น 2 ฝั่งด้วย /
-  ฝั่งซ้ายเป็น K ซึ่งหมายถึงเลขประจำตัวรถ โดยเริ่มตั้งแต่ 1 ถึง K
-  ฝั่งขวาเป็น List จำนวนวันที่จองรถตู้ของลูกค้าที่สั่งจองเข้ามา



คำใบ้ :  Min Heap

Testcase : #1 1
Enter Input : 3/3 1 2 2 2 1
Customer 1 Booking Van 1 | 3 day(s)
Customer 2 Booking Van 2 | 1 day(s)
Customer 3 Booking Van 3 | 2 day(s)
Customer 4 Booking Van 2 | 2 day(s)
Customer 5 Booking Van 3 | 2 day(s)
Customer 6 Booking Van 1 | 1 day(s)

Testcase : #2 2
Enter Input : 5/1 1 1 1 1 1 1 1 1
Customer 1 Booking Van 1 | 1 day(s)
Customer 2 Booking Van 2 | 1 day(s)
Customer 3 Booking Van 3 | 1 day(s)
Customer 4 Booking Van 4 | 1 day(s)
Customer 5 Booking Van 5 | 1 day(s)
Customer 6 Booking Van 1 | 1 day(s)
Customer 7 Booking Van 2 | 1 day(s)
Customer 8 Booking Van 3 | 1 day(s)
Customer 9 Booking Van 4 | 1 day(s)


"""
