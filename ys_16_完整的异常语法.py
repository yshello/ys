try:
    # 不能确定正确执行的代码
    num = int(input("请输入一个数字"))
    result = 8 / num
    print(result)
except ValueError:
    print("输入正确的数字")

except Exception as result:
    print("未知错误 %s" % result)
else:
    print("尝试成功")
finally:
    print("无论怎样都会输出")

print("-" * 30)

