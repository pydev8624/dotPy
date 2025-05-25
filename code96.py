dic = {1: "11", 2: "22", 3: "33"}
for key in dic:
    print(str(key) + " " + dic[key])

# clean code
dic = {1: "11", 2: "22", 3: "33"}
for key, value in dic.items():
    print(f"{key} {value}")
