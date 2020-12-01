from faker import Faker

for _ in range(10):
    f = Faker()
    f = Faker("zh_CN")
# 随机生成姓名
    print(f.name())
# # 随机生成地址
    print(f.address())
# 随机生成手机号
    print(f.phone_number())
# 随机生成password
#     print(f.password())
