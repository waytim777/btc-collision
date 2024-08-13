import pandas

p2pkh_1A = set()
p2pkh_1a = set()
p2pkh_A1 =set()
p2pkh_a1 = set()
p2pkh_Aa  = set()
p2pkh_aA = set()
p2pkh_AA = set()
p2pkh_11 = set()
p2pkh_aa = set()

p2sh_1A = set()
p2sh_1a = set()
p2sh_11 = set()
p2sh_AA = set()
p2sh_A1 = set()
p2sh_Aa = set()

p2wpkh_1a = set()
p2wpkh_11 = set()
p2wpkh_a1 = set()
p2wpkh_aa = set()

listA = []
lista = []
list1 = []

for i in range(48,58):
    list1.append(chr(i))

for i in range(97,123):
    lista.append(chr(i))

for i in range(65,91):
    listA.append(chr(i))

pd = pandas.read_csv("D://b1//1.csv", names=["amount","type", "address"], low_memory=False, iterator=True)
p = pd.get_chunk(5000000)
for i in range(1, 5000000):
    type = p['type'][i]
    address = p['address'][i]
    amount = float(p['amount'][i])
    # print(address)
    if amount / 100000000 < 0.7:
        print(amount)
        continue

    if type == "p2pkh":
        addt = address[1:2]
        addw = address[-1:]
        if list1.__contains__(addt) and list1.__contains__(addw):
            p2pkh_11.add(address)
        if list1.__contains__(addt) and listA.__contains__(addw):
            p2pkh_1A.add(address)
        if list1.__contains__(addt) and lista.__contains__(addw):
            p2pkh_1a.add(address)

        if listA.__contains__(addt) and list1.__contains__(addw):
            p2pkh_A1.add(address)
        if listA.__contains__(addt) and listA.__contains__(addw):
            p2pkh_AA.add(address)
        if listA.__contains__(addt) and lista.__contains__(addw):
            p2pkh_Aa.add(address)

        if lista.__contains__(addt) and list1.__contains__(addw):
            p2pkh_a1.add(address)
        if lista.__contains__(addt) and listA.__contains__(addw):
            p2pkh_aA.add(address)
        if lista.__contains__(addt) and lista.__contains__(addw):
            p2pkh_aa.add(address)
        print(type, i)
    if type == "p2sh":
        addt = address[1:2]
        addw = address[-1:]
        if list1.__contains__(addt) and list1.__contains__(addw):
            p2sh_11.add(address)
        if list1.__contains__(addt) and listA.__contains__(addw):
            p2sh_1A.add(address)
        if list1.__contains__(addt) and lista.__contains__(addw):
            p2sh_1a.add(address)

        if listA.__contains__(addt) and list1.__contains__(addw):
            p2sh_A1.add(address)
        if listA.__contains__(addt) and listA.__contains__(addw):
            p2sh_AA.add(address)
        if listA.__contains__(addt) and lista.__contains__(addw):
            p2sh_Aa.add(address)
        print(type, i)
    if type == "p2wpkh":
        addt = address[4:5]
        addw = address[-1:]
        if list1.__contains__(addt) and list1.__contains__(addw):
            p2wpkh_11.add(address)
        if list1.__contains__(addt) and lista.__contains__(addw):
            p2wpkh_1a.add(address)
        if lista.__contains__(addt) and list1.__contains__(addw):
            p2wpkh_a1.add(address)
        if lista.__contains__(addt) and lista.__contains__(addw):
            p2wpkh_aa.add(address)
        print(type, i)

index = 5000000
start = 5000000
end = 10000000
for q in range(0, 32):
    p2 = pd.get_chunk(5000000)
    for i in range(start, end):
        if i > 83200000:
            break

        type = p2['type'][i]
        add = p2['address'][i]
        amount = float(p2['amount'][i])
        if amount / 100000000 < 0.7:
            print(amount)
            continue
        tt = ''
        address = ''
        for t in type:
            tt = t
        for a in add:
            address = a

        if tt == "p2pkh":
            addt = address[1:2]
            addw = address[-1:]
            if list1.__contains__(addt) and list1.__contains__(addw):
                p2pkh_11.add(address)
            if list1.__contains__(addt) and listA.__contains__(addw):
                p2pkh_1A.add(address)
            if list1.__contains__(addt) and lista.__contains__(addw):
                p2pkh_1a.add(address)

            if listA.__contains__(addt) and list1.__contains__(addw):
                p2pkh_A1.add(address)
            if listA.__contains__(addt) and listA.__contains__(addw):
                p2pkh_AA.add(address)
            if listA.__contains__(addt) and lista.__contains__(addw):
                p2pkh_Aa.add(address)

            if lista.__contains__(addt) and list1.__contains__(addw):
                p2pkh_a1.add(address)
            if lista.__contains__(addt) and listA.__contains__(addw):
                p2pkh_aA.add(address)
            if lista.__contains__(addt) and lista.__contains__(addw):
                p2pkh_aa.add(address)
            print(tt, i)
        if tt == "p2sh":
            addt = address[1:2]
            addw = address[-1:]
            if list1.__contains__(addt) and list1.__contains__(addw):
                p2sh_11.add(address)
            if list1.__contains__(addt) and listA.__contains__(addw):
                p2sh_1A.add(address)
            if list1.__contains__(addt) and lista.__contains__(addw):
                p2sh_1a.add(address)

            if listA.__contains__(addt) and list1.__contains__(addw):
                p2sh_A1.add(address)
            if listA.__contains__(addt) and listA.__contains__(addw):
                p2sh_AA.add(address)
            if listA.__contains__(addt) and lista.__contains__(addw):
                p2sh_Aa.add(address)
            print(tt, i)
        if tt == "p2wpkh":
            addt = address[4:5]
            addw = address[-1:]
            if list1.__contains__(addt) and list1.__contains__(addw):
                p2wpkh_11.add(address)
            if list1.__contains__(addt) and lista.__contains__(addw):
                p2wpkh_1a.add(address)
            if lista.__contains__(addt) and list1.__contains__(addw):
                p2wpkh_a1.add(address)
            if lista.__contains__(addt) and lista.__contains__(addw):
                p2wpkh_aa.add(address)
            print(tt, i)
    start += 5000000
    end += 5000000




with open('D://p/p2pkh_11.txt', 'a+', encoding='utf-8') as fe:
    for pp in p2pkh_11:
        fe.writelines(pp + "\n")
fe.close()

with open('D://p/p2pkh_1Aszdx.txt', 'a+', encoding='utf-8') as fe:
    for pp in p2pkh_1A:
        fe.writelines(pp + "\n")
fe.close()

with open('D://p/p2pkh_1aszxx.txt', 'a+', encoding='utf-8') as fe:
    for pp in p2pkh_1a:
        fe.writelines(pp + "\n")
fe.close()



with open('D://p/p2pkh_A1dxsz.txt', 'a+', encoding='utf-8') as fe:
    for pp in p2pkh_A1:
        fe.writelines(pp + "\n")
fe.close()

with open('D://p/p2pkh_AAdxdx.txt', 'a+', encoding='utf-8') as fe:
    for pp in p2pkh_AA:
        fe.writelines(pp + "\n")
fe.close()

with open('D://p/p2pkh_Aadxxx.txt', 'a+', encoding='utf-8') as fe:
    for pp in p2pkh_Aa:
        fe.writelines(pp + "\n")
fe.close()



with open('D://p/p2pkh_a1xxsz.txt', 'a+', encoding='utf-8') as fe:
    for pp in p2pkh_a1:
        fe.writelines(pp + "\n")
fe.close()

with open('D://p/p2pkh_aAxxdx.txt', 'a+', encoding='utf-8') as fe:
    for pp in p2pkh_aA:
        fe.writelines(pp + "\n")
fe.close()

with open('D://p/p2pkh_aaxxxx.txt', 'a+', encoding='utf-8') as fe:
    for pp in p2pkh_aa:
        fe.writelines(pp + "\n")
fe.close()






with open('D://p/p2sh_11.txt', 'a+', encoding='utf-8') as fe:
    for pp in p2sh_11:
        fe.writelines(pp + "\n")
fe.close()

with open('D://p/p2sh_1Aszdx.txt', 'a+', encoding='utf-8') as fe:
    for pp in p2sh_1A:
        fe.writelines(pp + "\n")
fe.close()

with open('D://p/p2sh_1aszxx.txt', 'a+', encoding='utf-8') as fe:
    for pp in p2sh_1a:
        fe.writelines(pp + "\n")
fe.close()


with open('D://p/p2sh_A1dxsz.txt', 'a+', encoding='utf-8') as fe:
    for pp in p2sh_A1:
        fe.writelines(pp + "\n")
fe.close()

with open('D://p/p2sh_AAdxdx.txt', 'a+', encoding='utf-8') as fe:
    for pp in p2sh_AA:
        fe.writelines(pp + "\n")
fe.close()

with open('D://p/p2sh_Aadxxx.txt', 'a+', encoding='utf-8') as fe:
    for pp in p2sh_Aa:
        fe.writelines(pp + "\n")
fe.close()






with open('D://p/p2wpkh_11.txt', 'a+', encoding='utf-8') as fe:
    for pp in p2wpkh_11:
        fe.writelines(pp + "\n")
fe.close()

with open('D://p/p2wpkh_1a.txt', 'a+', encoding='utf-8') as fe:
    for pp in p2wpkh_1a:
        fe.writelines(pp + "\n")
fe.close()


with open('D://p/p2wpkh_a1.txt', 'a+', encoding='utf-8') as fe:
    for pp in p2wpkh_a1:
        fe.writelines(pp + "\n")
fe.close()

with open('D://p/p2wpkh_aa.txt', 'a+', encoding='utf-8') as fe:
    for pp in p2wpkh_aa:
        fe.writelines(pp + "\n")
fe.close()
