#表达式
#1、由值表达式
print(8)
#2、字符串表达式
print("hello")

#3、计算表达式 （值和运算符）
print(25+7)

#4、赋值表达式和变量表达式
a=67
print(a)

# is 运算符
#==用来判断俩个对象是否相等，is判定是否是同一个对象
#避免将is运算符用于比较类似数值和字符串这类不可变值，使用is运算符的结果是不可预测的
x=y=[1,2,3]
z=[1,2,3]
print(x==y)
print(x==z)
print(x is y)
print(x is z)