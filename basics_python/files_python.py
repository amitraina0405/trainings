# print("=========== Open a file =============")
# #  Open a file
#
# f = open("test.txt")    # open file in current directory/ equivalent to 'r'

try:
    f = open("C:/Python27/README_yyyy.txt")  # specifying full path

except Exception as e:
    print(e)

finally:
    print("Entered the filnally block ... to exit cleanly")
#
# f = open("test.txt",'w')  # write in text mode
#
# f.close()

# print("=========== Write into a file =============")
# # write into a file
#
# file_data = input("Enter Data::")
#
# with open("test.txt",'w') as f:
#     f.write("+++++++++++++++++++++\n")
#     f.write("This file\n")
#     f.write("contains three lines\n")
#     f.write(file_data)
#     f.close()
#
#
# with open("test_new.txt",'w') as f:
#     f.write("my first file, This file contains three lines")
#     f.close()
#

# with open("test_new.txt",'a') as f:
#     f.write("my first file, This file contains three lines")
#     f.close()


# print("=========== Read from a file =============")
# # read from a file
#
# f = open("test.txt",'r')
# print(" ============ Read the first 8 characters ============")
# data = f.read(8)    # read the first 8 data
# print(data)
#
# print(" ============ Read next 4 characters ============")
# data = f.read(4)    # read the next 4 data
# print(data)
#
# print(" ============ Read the rest till end of file ============")
# data = f.read()     # read in the rest till end of file
# print(data)
#
# print(" ============ Further reading returns empty sting ============")
# data = f.read()  # further reading returns empty sting
# print(data)
# print("Training")
#
# #  Read file line by line
#
# print(" ============== Read file line by line ============== ")
# f = open("test.txt",'r',encoding = 'utf-8')
# for line in f:
#     print(line, end='')
#     # print(line)

print("\n=========== readlines() reads untill a new line character is found ============= ")

f = open("test.txt",'r',encoding = 'utf-8')
print(f.readline(), end='')
print(f.readline(), end='')
print(f.readline(), end='')
print(f.readline(), end='')

