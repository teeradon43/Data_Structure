"""
Chapter : 7 - item : 5 - Expression Tree
 ส่งมาแล้ว 0 ครั้ง
ให้น้องๆรับ input เป็น postfix จากนั้นให้แปลงเป็น Expression Tree , Infix และ Prefix  โดย Operator จะมีแค่ + - * /

Testcase : #1 1
Enter Postfix : ab+cde+**
Tree :
                e
           +
                d
      *
           c
 *
           b
      +
           a
--------------------------------------------------
Infix : ((a+b)*(c*(d+e)))
Prefix : *+ab*c+de

Testcase : #2 2
Enter Postfix : abc*+de*f+g*+
Tree :
           g
      *
                f
           +
                     e
                *
                     d
 +
                c
           *
                b
      +
           a
--------------------------------------------------
Infix : ((a+(b*c))+(((d*e)+f)*g))
Prefix : ++a*bc*+*defg

Testcase : #3 3
Enter Postfix : ab+c*de-fg+*-
Tree :
                g
           +
                f
      *
                e
           -
                d
 -
           c
      *
                b
           +
                a
--------------------------------------------------
Infix : (((a+b)*c)-((d-e)*(f+g)))
Prefix : -*+abc*-de+fg

"""