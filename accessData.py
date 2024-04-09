file_in = open("./python/test.txt")
arr = list(map(lambda lit: lit.strip('\n'), file_in.readlines()))
# Another arr writing method
# arr = [data.strip('\n') for data in file_in.readlines()]
print("讀取資料:")
for line in arr:
    print(line)
file_in.close()
#--------------------------插入資料--------------------------#
arr.append("ffff")  # 插入資料
print("插入後的資料:")
for line in arr:
    print(line)
#--------------------------輸出資料--------------------------#
file_out = open("./python/test.txt","w")    # 寫入指定檔案
for line in arr:
    print(line, file=file_out)
file_out.close()    # 關檔



# verson two
with open("./python/test.txt", "r") as file_in:
    arr = [data.strip('\n') for data in file_in.readlines()]
print("讀取資料:")
for line in arr:
    print(line)
#--------------------------插入資料--------------------------#
arr.append("ffff")      # 插入資料到arr列表中
print("插入後的資料:")
for line in arr:
    print(line)
#--------------------------輸出資料--------------------------#
with open("./python/test.txt", "w") as file_out:    # 寫入指定檔案
    for line in arr:
        print(line, file=file_out)