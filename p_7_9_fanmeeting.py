from p_7_4_karatsuba import *

#member = input("멤버의 성별을 입력하세요(서 있는 순서대로):")
#fan = input("팬의 성별을 입력하세요(서 있는 순서대로):")

member = "mfmfmfffmmmfmf"
fan = "mmfffffmfffmffffffmfffmffffmfmmfffffff"

member = member.upper()
fan = fan.upper()

def mul_array(x):
    ret = []

    for i in range(len(x)):
        ret.append(x[i])

    return np.array(ret)

members_array = mul_array(member)
fans_array = mul_array(fan)[::-1]

def hugs(members, fans):

    members_size = len(members)
    fans_size = len(fans)

    mem = np.zeros((members_size,))
    fan = np.zeros((fans_size,))

    for i in range(members_size):
        if members[i] == "M":
            mem[i] = 1

    for j in range(fans_size):
        if fans[j] == "M":
            fan[j] = 1
    print(mem);print(fan)
    c = multiply(mem, fan)
    all_hugs = 0
    print(c)

    for i in range(members_size-1,fans_size):
        if c[i] == 0:
            all_hugs += 1

    return all_hugs


print(hugs(members_array, fans_array))

