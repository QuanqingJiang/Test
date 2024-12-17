# 方法1：使用切片
def reverse_string1(s):
    return s[::-1]

# 方法2：使用reversed函数
def reverse_string2(s):
    return ''.join(reversed(s))

# 方法3：使用循环
def reverse_string3(s):
    result = ''
    for char in s:
        result = char + result
    return result

# 方法4：转换为列表后反转
def reverse_string4(s):
    chars = list(s)
    chars.reverse()
    return ''.join(chars)

# 使用示例
if __name__ == '__main__':
    test_str = input("请输入要反转的字符串: ")
    
    print(f"原始字符串: {test_str}")
    print(f"方法1结果: {reverse_string1(test_str)}")
    print(f"方法2结果: {reverse_string2(test_str)}")
    print(f"方法3结果: {reverse_string3(test_str)}")
    print(f"方法4结果: {reverse_string4(test_str)}")
