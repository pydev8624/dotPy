num = 10.9
int_num = int(num)  # تبدیل به عدد صحیح

print(int_num)  # خروجی: 10
print(type(int_num))  # خروجی: <class 'int'>

num = 123
str_num = str(num)

print(str_num)  # خروجی: "123"
print(type(str_num))  # خروجی: <class 'str'>

num_str = "456"
num_int = int(num_str)

print(num_int)  # خروجی: 456
print(type(num_int))  # خروجی: <class 'int'>

num_str = "123abc"
num_int = int(num_str)  # خطا: ValueError

my_list = [1, 2, 2, 3, 4, 4, 5]
my_set = set(my_list)

print(my_set)  # خروجی: {1, 2, 3, 4, 5}

print(int(True))  # خروجی: 1
print(int(False))  # خروجی: 0

num = "3.14"
int_num = int(num)  # خطا: ValueError، چون مقدار شامل نقطه (اعشار) است!

int_num = int(float(num))  # تبدیل موفق
print(int_num)  # خروجی: 3
