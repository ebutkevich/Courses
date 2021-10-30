#1) Создать переменную типа String
a= 'Katya'
print(type(a), a)
#2) Создать переменную типа Integer
b= 21
print(type(b), b)
#3) Создать переменную типа Float
c= 2.8
print(type(c), c)
#4) Создать переменную типа Bytes
y=([50, 100, 76, 72, 41])
print(type(y), y)
#5) Создать переменную типа List
l = [a, b, c]
print(type(l), l)
#6) Создать переменную типа Tuple
t = (21, a, 2.8)
print(type(t), t)
# 7) Создать переменную типа Set
s = {21, a, 2.8}
print(type(s), s)
#8) Создать переменную типа Frozen set
z = ({21, a, 2.8})
print(type(z), z)
#9) Создать переменную типа Dict
d = {'value':1, 'key':2}
print(type(d), d)
#10)Вывести в консоль все выше перечисленные переменные с добавлением типа данных
print((type(a), a), (type(b), b), (type(c), c), (type(y), y), (type(l), l), (type(t), t), (type(s), s), (type(z), z), (type(d), d), sep=' & ')
#11) Создать 2 переменные String, создать переменную в которой сканкатенируете эти переменные. Вывести в консоль.
st1 = 'Good'
st2 = 'Luck!'
con = st1+st2
print(con)
#12) Вывести в одну строку переменные типа String и Integer используя “,” (Запятую)
print(a, b, sep = ',')
#13) Вывести в одну строку переменные типа String и Integer используя “+” (Плюс)
print(a  +  str(b))
