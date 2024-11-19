import random
import datetime


def Euclid(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a


def TrialDivs(n):
    n = str(n)
    i = 0
    a = []
    while i < len(n):
        a.append(int(n[i]))
        i += 1
    m = [2, 3, 5]
    i = m[-1] + 1
    while i < 1000:
        if MillRab(i) == 1:
            m.append(i)
        i += 1
    dividers = []
    i = 0
    while i < len(m):
        r = [1]
        j = 0
        summ = 0
        while j < len(a) - 1:
            r.append((r[j]*10) % m[i])
            j += 1
        j = 0
        while j < len(a):
            summ += a[len(a)-j-1] * r[j]
            j += 1
        if summ % m[i] == 0:
            dividers.append(m[i])
        i += 1
    if len(dividers) == 0:
        return 1
    return dividers


def MillRab(p):
    d = p - 1
    s = 0
    k = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    if (d * (2**s)) != (p - 1):
        print('d =', d)
        print('s =', s)
        print('d * (2**s) =', d * (2**s))
        return 'incorrect number arrangement'
    while k < 1000:
        cheker_x = 0
        x = random.randint(2, p)
        if Euclid(x, p) != 1:
            return 0
        x = pow(x, d, p)
        if x == 1 or x == p - 1:
            cheker_x = 1
        else:
            x_r = pow(x, 2, p)
            i = 0
            while i < s:
                if x_r == p - 1:
                    cheker_x = 1
                    break
                if x_r == 1:
                    return 0
                x_r = pow(x_r, 2, p)
                i += 1
        if cheker_x == 0:
            return 0
        if pow(x, p-1, p) != 1:
            return 0
        k += 1
    return 1


def BBS(n):
    lst = []
    p = hex(0xD5BBB96D30086EC484EBA3D7F9CAEB07)         #284100283511244958272321698211826428679
    q = hex(0x425D2B9BFDB25B9CF6C416CC6E37B59C1F)       #22582480853028265529707582510375286184991
    p = int(p, 16)
    q = int(q, 16)
    pq = p * q
    r = random.randint(2, pq - 1)
    for i in range(0, n - 2):
        r = pow(r, 2, pq)
        r_i = bin(r).replace("0b", "")
        for j in range(0, 8):
            lst.append(int(r_i[-1-j]))
    while len(lst) > n - 2:
        lst.pop()
    lst.insert(0, 1)
    lst[-1] = 1
    return lst


def LstToInt(lst):
    n = 0
    i = 0
    while i < len(lst):
        n += lst[i] * pow(2, len(lst) - 1 - i)
        i += 1
    return n


################################################################ prime pairs


def PrimePair():
    pq = []
    notpq = []
    var = LstToInt(BBS(256))
    while len(pq) != 4:
        if TrialDivs(var) == 1 and MillRab(var) == 1:
            var1 = 2 * var + 1
            i = 2
            while i <= 1000:
                if TrialDivs(var1) == 1 and MillRab(var1) == 1:
                    pq.append(var1)
                    var = LstToInt(BBS(256))
                    print('+1 prime:', var1)
                    break
                notpq.append(var1)
                var1 = 2 * i * var + 1
                i += 1
        else:
            notpq.append(var)
            var += 2
    return pq, notpq

# first prime:  45589500175138419810605827826965423704973340527401499738488070268197183796573
# second prime: 54290326760511864918550127498880471135557280756772989329621604474316143476327
# third prime:  41091338020461255661075724377333013226799584037846379685182111393700244340443
# fourth prime: 49875309757275072695320512104599864882127527325639082212024030120285317628513

# fifth prime:    8674807315756815137745126128131963482740637207311401765694960758383906252753233
# sixth prime:    3409612075716033060475062719661797033616973381096875330409508114082024484201447
# seventh prime:  3135256236609377947518154846846688200114833584150255068832670463685911859501003
# eights prime:   8449343209690068101726672581788740419563156705986768291413898782478811780265849
# with time:      0:01:51.797744



################################################################ GenerateKeyPair()
#the function must return and/or store the secret key (d, p, q) and public key (n,e)


def GenerateKeyPair(p, q):
    e = 2 ** 16 + 1
    n = p * q
    phi = (p - 1) * (q - 1)
    d = pow(e, -1, phi)
    secret_key = [d, p, q]
    public_key = [e, n]
    return secret_key, public_key

def Encrypt(public_key, m):
    e = public_key[0]
    n = public_key[1]
    c = pow(m, e, n)
    return c

def Decrypt(secret_key, c):
    d = secret_key[0]
    n = secret_key[1] * secret_key[2]
    m = pow(c, d, n)
    return m

def Sign(secret_key, m):
    d = secret_key[0]
    n = secret_key[1] * secret_key[2]
    s = pow(m, d, n)
    return s, m

def Verify(public_key, signed_message):
    e = public_key[0]
    n = public_key[1]
    s = signed_message[0]
    m = signed_message[1]
    if m == pow(s, e, n):
        return m, 'Signature is correct!'
    else:
        return 0, 'Warning! Signature is not correct!'


def SendKey(public_key_B, secret_key_A, k):
    d = secret_key_A[0]
    n = secret_key_A[1] * secret_key_A[2]
    e1 = public_key_B[0]
    n1 = public_key_B[1]
    k1 = pow(k, e1, n1)
    s = pow(k, d, n)
    s1 = pow(s, e1, n1)
    return k1, s1

def ReceiveKey(k1, s1, secret_key_B, public_key_A):
    d1 = secret_key_B[0]
    n1 = secret_key_B[1] * secret_key_B[2]
    e = public_key_A[0]
    n = public_key_A[1]
    k = pow(k1, d1, n1)
    s = pow(s1, d1, n1)
    if k == pow(s, e, n):
        return k, 'Authenticity verified. Secret k is formed.'
    else:
        return 0, 'Warning! Authenticity is not verified. Secret k is not formed.'


# a = PrimePair()
# a = a[0]
# p = a[0]
# q = a[1]
# print(GenerateKeyPair(p, q))

d = 6862323573569154035379922209119836841115390275268559483801135900685048709401724733918482998792225512544552101571319585589191200821883611477701665905682982353
p = 6056523998345083068153632736999626975585662195330339763086273950282403841022371
q = 12975095444814703575414293514359857791616309465139690887027833560529795744995257
# e = 65537
# n = 78583976942338222613435953489269045440534567966149848486785784295508655821782446759527117507479476595295168200421264088352723501354044530569879164193425894347
# n = hex(78583976942338222613435953489269045440534567966149848486785784295508655821782446759527117507479476595295168200421264088352723501354044530569879164193425894347)

# n = 16e50f8dffd23b26621e88bc663aafbf82cad3459597b7870dc2541dcc424fede81f40dc8099d6736c09c8011de051aae0eafba2d9c04d804e9b5f363be0b8e8abcb
# n1 = 0xB7D90B502714AB262680C0B4392860B4C4EF821AD239B272C43246453E3E53C7
e1 = 0x10001


# S = 0x9C78A66AEDB6ED289CD339E35DB61DD8B1CC090B83D8BCF2F2B412B9A855E21C
# print(Verify([e1, n1], [S, 0xabc]))

# k1 = 0x15EBA6468622084A925AAB5D9584145C51B064527E42D34925194D73B67A7DF9BA46ADC1BC52F75CBBF6A9D64E63BDFE1B27152A4C6110122CB1BF23D65C80780F11
# S1 = 0x0FBBBD3DA81E2FC68A63288027AD0A4DFBFCD05537EFA6C7081CA42D7D4B215F7D0F0CECC058337470BC02B1AA24ADCDB542914D17B0D0F366FA3C8B8C8788E686A8
# print(ReceiveKey(k1, S1, [d, p, q], [0x10001, 0xB7D90B502714AB262680C0B4392860B4C4EF821AD239B272C43246453E3E53C7]))
# print(hex(ReceiveKey(k1, S1, [d, p, q], [0x10001, 0xB7D90B502714AB262680C0B4392860B4C4EF821AD239B272C43246453E3E53C7])[0]))
print(len(bin(78583976942338222613435953489269045440534567966149848486785784295508655821782446759527117507479476595295168200421264088352723501354044530569879164193425894347)))

n1 = 0xDB1E614D8FF0B48032F30F10F66B2B27F0267E88517903309382B8F27C96B9CCFCF8C4CB19D87D1D1BC5E41C49BEB5C4A95674C35FA8DCEFAED4AC33CF0824C96B0901EFDAA835D9895199
k1, S1 = SendKey([e1, n1], [d, p, q], 0xabc)
print(hex(k1), hex(S1))






# start_time = datetime.datetime.now()
# a = PrimePair()
# pq = a[0]
# notpq = a[1]
#
# p1 = max(pq)
# pq.remove(p1)
# q1 = max(pq)
# pq.remove(q1)
# p = pq[0]
# q = pq[1]
# A_params = GenerateKeyPair(p, q)
# B_params = GenerateKeyPair(p1, q1)
# print('\nПараметри користувача А:\nсекретний ключ [d, p, q] =', A_params[0], '\nпублічний ключ [e, n]:', A_params[1], '\n')
# print('Параметри користувача B:\nсекретний ключ [d, p, q] =', B_params[0], '\nпублічний ключ [e, n]:', B_params[1], '\n')
# print('Кількість кандидатів у p та q, які не пройшли тести на простоту:', len(notpq), '\nЇх перелік:', notpq)
# print('Витрачений час на генерацію:', datetime.datetime.now() - start_time)
#
# start_time1 = datetime.datetime.now()
# M_A = LstToInt(BBS(250))
# M_B = LstToInt(BBS(250))
# C_A = Encrypt(B_params[1], M_A)
# C_B = Encrypt(A_params[1], M_B)
# S_A = Sign(A_params[0], M_A)
# S_B = Sign(B_params[0], M_B)
# print('\nВідкритий текст від А:', M_A, ';\nШифротекст, створений А для B:', C_A, ';\nПідпис даного повідомлення:', S_A)
# print('\nВідкритий текст від B:', M_B, ';\nШифротекст, створений B для A:', C_B, ';\nПідпис даного повідомлення:', S_B)
# print('Витрачений час:', datetime.datetime.now() - start_time1)
#
# start_time1 = datetime.datetime.now()
# Decrypt_C_A = Decrypt(B_params[0], C_A)
# Decrypt_C_B = Decrypt(A_params[0], C_B)
# Check_S_A = Verify(A_params[1], S_A)
# Check_S_B = Verify(B_params[1], S_B)
# print('\nРозшифрований текст для В:', Decrypt_C_B, ';\nОригінальний текст:', M_B, '\nПеревірка підпису:', Check_S_B)
# print('\nРозшифрований текст для A:', Decrypt_C_A, ';\nОригінальний текст:', M_A, '\nПеревірка підпису:', Check_S_A)
# print('Витрачений час:', datetime.datetime.now() - start_time1)
#
#
# k = LstToInt(BBS(250))
# key = SendKey(B_params[1], A_params[0], k)
# secret = ReceiveKey(key[0], key[1], B_params[0], A_params[1])
# print('\nСпільний секрет:', k, ';\nШифрований секрет від А до В:', key,
#       ';\nРозшифрування секрету і перевірка автентичності:', secret)
# print('\nЗагалом витрачено часу:', datetime.datetime.now() - start_time)