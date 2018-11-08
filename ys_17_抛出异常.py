def input_password():

    # 提示用户输入密码
    pdw = input("请输入密码：")
    # 判断密码长度是否大于8，返回输入的密码
    if len(pdw) >= 8:
        return pdw

    # 如果小于8，抛出异常
    print("主动抛出异常")
    # 创建异常对象
    ex = Exception("密码不足八位")
    # 主动抛出异常
    raise ex

# 提示用户输入密码
try:
    print(input_password())
except Exception as result:
    print(result)