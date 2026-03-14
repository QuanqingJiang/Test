"""
字符串反转工具集 (String Reversal Utilities)
展示了在 Python 中反转字符串的四种常用方法。
"""

def reverse_string1(s):
    """
    方法1：使用切片 (Slicing) [推荐]
    原理：利用 Python 列表/字符串切片的特性 [start:stop:step]，步长设为 -1 表示倒序。
    优点：代码最简洁，执行效率最高，是 Pythonista 最常用的方法。
    """
    return s[::-1]


def reverse_string2(s):
    """
    方法2：使用内置的 reversed() 函数
    原理：reversed() 会返回一个反转的迭代器，然后使用 ''.join() 将其重新拼接成字符串。
    优点：可读性很强，语义明确（一眼就能看出是干嘛的）。
    """
    return ''.join(reversed(s))


def reverse_string3(s):
    """
    方法3：使用 for 循环拼接
    原理：遍历原字符串的每个字符，每次都把新字符加到结果字符串的最前面。
    缺点：由于 Python 中字符串是不可变的，每次拼接都会在内存中创建新对象，
          因此在处理超大字符串时，这种方法的性能最差。
    """
    result = ''
    for char in s:
        result = char + result  # 将当前字符放在已有结果的前面
    return result


def reverse_string4(s):
    """
    方法4：转换为列表后使用 reverse() 方法
    原理：先将字符串打散成字符列表，调用列表自带的 .reverse() 方法进行原地反转，最后再拼接。
    优点：如果是对列表进行操作，这种方法效率很高，但对于字符串来说多了一步类型转换。
    """
    chars = list(s)    # 字符串转列表：'abc' -> ['a', 'b', 'c']
    chars.reverse()    # 列表原地反转：['c', 'b', 'a']
    return ''.join(chars) # 列表转回字符串


# 使用示例（入口程序）
if __name__ == '__main__':
    print("=== 字符串反转测试程序 ===")
    test_str = input("请输入要反转的字符串: ")
    
    print(f"\n原始字符串: {test_str}")
    print("-" * 20)
    print(f"方法1 (切片)   结果: {reverse_string1(test_str)}")
    print(f"方法2 (内置函数) 结果: {reverse_string2(test_str)}")
    print(f"方法3 (for循环)  结果: {reverse_string3(test_str)}")
    print(f"方法4 (列表反转) 结果: {reverse_string4(test_str)}")