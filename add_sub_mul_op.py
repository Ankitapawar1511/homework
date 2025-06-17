n1=10
n2=20
f=2.3
str1="hii"
str2="hello"
l1=[1,2,3,4]
l2=[5,6,7,8]
s1={7,1,4.5,9}
s2={"hello",4,3.5,8}
d1={1:"hii",2:23,3:5}
d2={'a':"hello",'b':4,'c':5}
t1=(1,2,3,'a')
t2=('a','b','c','d')
print("num + all types")
print("num+num : ",n1+n2) #num+num :  30
print("num+str: ",n1+str1) #unsupported operand type(s) for +: 'int' and 'str'
print("num+list : ",n1+l1) #unsupported operand type(s) for +: 'int' and 'list'
print("num+tuple : ",n1+t1)#unsupported operand type(s) for +: 'int' and 'tuple'
print("num+set : ",n1+s1)#unsupported operand type(s) for +: 'int' and 'set'
print("num+dict : ",n1+d1)#unsupported operand type(s) for +: 'int' and 'dictionary'


print("str + all types")

print("str+str: ",str2+str1) #str+str:  hellohii
print("str+list : ",str1+l1) #can only concatenate str (not "list") to str
print("str+tuple : ",str1+t1) #can only concatenate str (not "tuple") to str
print("str+set : ",str1+s1)#can only concatenate str (not "set") to str
print("str+dict : ",str1+d1)#can only concatenate str (not "dict") to str


print("list + all types")


print("list+str: ",l1+str1)#can only concatenate list (not "str") to list
print("list+list : ",l1+l1)#list+list :  [1, 2, 3, 4, 1, 2, 3, 4]
print("list+tuple : ",l1+t1)#can only concatenate list (not "tuple") to list
print("list+set : ",l1+s1)#can only concatenate list (not "set") to list
print("list+dict : ",l1+d1)#can only concatenate list (not "dict") to list

print("tuple + all types")

print("tuple+str: ",t1+str1)#can only concatenate tuple (not "str") to tuple
print("tuple+list : ",t1+l1)#can only concatenate tuple (not "list") to tuple
print("tuple+tuple : ",t2+t1)#tuple+tuple :  ('a', 'b', 'c', 'd', 1, 2, 3, 'a')
print("tuple+set : ",t1+s1)#can only concatenate tuple (not "set") to tuple
print("tuple+dict : ",t1+d1)#can only concatenate tuple (not "dict") to tuple

print("set + all types")


print("set+str: ",s1+str1)#unsupported operand type(s) for +: 'set' and 'str'
print("set+list : ",s1+l1)#unsupported operand type(s) for +: 'set' and 'list'
print("set+tuple : ",s1+t1)#unsupported operand type(s) for +: 'set' and 'tuple'
print("set+set : ",s2+s1)#unsupported operand type(s) for +: 'set' and 'set'
print("set+dict : ",s1+d1)#unsupported operand type(s) for +: 'set' and 'dictionary'


print("dict + all types")


print("dict+str: ",d1+str1)# unsupported operand type(s) for +: 'dict' and 'str'
print("dict+list : ",d1+l1)# unsupported operand type(s) for +: 'dict' and 'list'
print("dict+tuple : ",d1+t1)# unsupported operand type(s) for +: 'dict' and 'tuple'
print("dict+set : ",d1+s1)# unsupported operand type(s) for +: 'dict' and 'set'
print("dict+dict : ",d2+d1)#



print("num - all types")
print("num-num : ",n1-n2) #num-num :  -10
print("num-str: ",n1-str1) #unsupported operand type(s) for -: 'int' and 'str'
print("num-list : ",n1-l1) #unsupported operand type(s) for -: 'int' and 'list'
print("num-tuple : ",n1-t1)#unsupported operand type(s) for -: 'int' and 'tuple'
print("num-set : ",n1-s1)#unsupported operand type(s) for -: 'int' and 'set'
print("num-dict : ",n1-d1)#unsupported operand type(s) for -: 'int' and 'dictionary'


print("str - all types")

print("str-str: ",str2-str1) # unsupported operand type(s) for -: 'str' and 'str'
print("str-list : ",str1-l1) # unsupported operand type(s) for -: 'str' and 'list'
print("str-tuple : ",str1-t1) #unsupported operand type(s) for -: 'str' and 'tuple'
print("str-set : ",str1-s1)#set-set :  {8, 'hello', 3.5, 4}
print("str-dict : ",str1-d1)#unsupported operand type(s) for -: 'str' and 'dict'


print("list - all types")


print("list-str: ",l1-str1)#unsupported operand type(s) for -: 'list' and 'str'  
print("list-list : ",l1-l1)#unsupported operand type(s) for -: 'list' and 'list'  
print("list-tuple : ",l1-t1)#unsupported operand type(s) for -: 'list' and 'tuple'  
print("list-set : ",l1-s1)#unsupported operand type(s) for -: 'list' and 'set'  
print("list-dict : ",l1-d1)#unsupported operand type(s) for -: 'list' and 'dict'  


print("tuple - all types")

print("tuple-str: ",t1-str1)#can only concatenate tuple (not "str") to tuple
print("tuple-list : ",t1-l1)#can only concatenate tuple (not "list") to tuple
print("tuple-tuple : ",t2-t1)#tuple+tuple :  ('a', 'b', 'c', 'd', 1, 2, 3, 'a')
print("tuple-set : ",t1-s1)#can only concatenate tuple (not "set") to tuple
print("tuple-dict : ",t1-d1)#can only concatenate tuple (not "dict") to tuple

print("set -all types")


print("set-str: ",s1-str1)#unsupported operand type(s) for -: 'set' and 'str'
print("set-list : ",s1-l1)#unsupported operand type(s) for -: 'set' and 'list'
print("set-tuple : ",s1-t1)#unsupported operand type(s) for -:'set' and 'tuple'
print("set-set : ",s2-s1)#unsupported operand type(s) for -: 'set' and 'set'
print("set-dict : ",s1-d1)#unsupported operand type(s) for -: 'set' and 'dictionary'


print("dict - all types")


print("dict-str: ",d1-str1)# unsupported operand type(s) for -: 'dict' and 'str'
print("dict-list : ",d1-l1)# unsupported operand type(s) for -:'dict' and 'list'
print("dict-tuple : ",d1-t1)# unsupported operand type(s) for -: 'dict' and 'tuple'
print("dict-set : ",d1-s1)# unsupported operand type(s) for -: 'dict' and 'set'
print("dict-dict : ",d2-d1)#unsupported operand type(s) for -: 'dict' and 'dict'



print("num * all types")
print("num*num : ",n1*n2) #num*num :  200
print("num*str: ",n1*str1) # num*str:  hiihiihiihiihiihiihiihiihiihii
print("num*list : ",n1*l1) #num*list :  [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2,  3, 4, 1, 2, 3, 4]
print("num* tuple : ",n1*t1)#num* tuple :  (1, 2, 3, 'a', 1, 2, 3, 'a', 1, 2, 3, 'a', 1, 2, 3, 'a', 1, 2, 3, 'a', 1, 2, 3, 'a', 1, 2, 3, 'a', 1,, 2, 3, 'a', 1, 2, 3, 'a', 1, 2, 3, 'a')
print("num*set : ",n1*s1)#unsupported operand type(s) for *: 'int' and 'set'
print("num*dict : ",n1*d1)#unsupported operand type(s) for  'int' and 'dictionary'


print("str * all types")

print("str*str: ",str2*str1) # can't multiply sequence by non-int of type 'str'
print("str*list : ",str1*l1) # can't multiply sequence by non-int of type  'list'
print("str*tuple : ",str1*t1) #can't multiply sequence by non-int of type  'tuple'
print("str*set : ",str1*s1)#can't multiply sequence by non-int of type 'set'
print("str*dict : ",str1*d1)#can't multiply sequence by non-int of type 'dict'


print("list * all types")


print("list*str: ",l1*str1)#unsupported operand type(s) for -: 'list' and 'str'  
print("list*list : ",l1*l1)#unsupported operand type(s) for -: 'list' and 'list'  
print("list*tuple : ",l1*t1)#unsupported operand type(s) for -: 'list' and 'tuple'  
print("list*set : ",l1*s1)#unsupported operand type(s) for -: 'list' and 'set'  
print("list*dict : ",l1*d1)#unsupported operand type(s) for -: 'list' and 'dict'  


print("tuple * all types")

print("tuple*str: ",t1*str1)#can't multiply sequence by non-int of type  'str'
print("tuple*list : ",t1*l1)#can't multiply sequence by non-int of type  'list
print("tuple*tuple : ",t2*t1)#tcan't multiply sequence by non-int of type 'tuple'
print("tuple*set : ",t1*s1)#can't multiply sequence by non-int of type 'set'
print("tuple*dict : ",t1*d1)#can't multiply sequence by non-int of type 'dict'


print("set * all types")

print("set*str: ",s1*str1)#can't multiply sequence by non-int of type 'set'
print("set*list : ",s1*l1)#can't multiply sequence by non-int of type 'list'
print("set*tuple : ",s1*t1)#can't multiply sequence by non-int of type  'tuple'
print("set*set : ",s2*s1)#unsupported operand type(s) for *: 'set' and 'set'
print("set*dict : ",s1*d1)#can't multiply sequence by non-int of type  'dictionary'


print("dict * all types")


print("dict*str: ",d1*str1)# can't multiply sequence by non-int of type 'dict'
print("dict*list : ",d1*l1)# can't multiply sequence by non-int of type 'dict'
print("dict*tuple : ",d1*t1)# can't multiply sequence by non-int of type 'dict'
print("dict*set : ",d1*s1)# can't multiply sequence by non-int of type 'dict'
print("dict*dict : ",d2*d1)#unsupported operand type(s) for *: 'dict' and 'dict'

