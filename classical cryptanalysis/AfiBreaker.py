import math
import string
from itertools import islice, cycle

#TODO: 1.File Handling, 2.Clean up the code, 3.Manual text break option

def gcd(a, b):
    while b != 0:
        c = a % b
        a = b
        b = c
    return a


def relatively_first(a, mod):
    if gcd(a, mod) == 1:
        return True
    else:
        return False


def xgcd(x, N) -> object:
    if x > N:
        return False, False, False
    X, Y, R, S = 1, 0, 0, 1
    while N != 0:
        C = x % N
        Q = math.floor(x / N)
        x, N = N, C
        Rp, Sp = R, S
        R = X - Q * R
        S = Y - Q * S
        X, Y = Rp, Sp
    d = x
    u = X
    v = Y
    return d, u, v


def mod_inverse(x, N):
    d, u, v = xgcd(x, N)
    if d != 1:
        return False
    return u % N


def soe(x1, x2, y1, y2):
    tempx = (x2 - x1) % 26
    tempy = (y2 - y1) % 26
    if mod_inverse(tempx, 26) is not False:
        a = (tempy * mod_inverse(tempx, 26)) % 26
        b = (y1 - (x1 * a) % 26) % 26
        return a, b
    else:
        return 0,0


def cong(number_of_letter, a, b):
    if relatively_first(a, 26) != True:
        return 0
    else:
        x = ((number_of_letter - b) * mod_inverse(a, 26)) % 26
        return x


def shift_dict(dct, shift):
    shift %= len(dct)
    return dict(
        (k, v)
        for k, v in zip(dct.keys(), islice(cycle(dct.values()), shift, None)))


def get_dicts(ctxt):
    tab_ctxt = []  # text in array
    tab_ctxt_numbers = []  # assigned numbers to letters
    tab_of_letters = list(map(chr, range(65, 91)))  # alphabet generator
    dict_of_letters = dict(zip(string.ascii_uppercase, range(0, 26)))  # Alphabet generator as dictionary with numeration
    calc_freq_letters = {}  # Dictionary with frequency of letters
    letters_frequency = {}  #Dictionary which one have elements with with the greatest frequency (for congruention)

    #Loading text to array
    for x in range(0, len(ctxt)):
        tab_ctxt.append(ctxt[x])
        tab_ctxt_numbers.append(ord(ctxt[x]) - 65)

    # Calculate of frequency
    for x in range(0, 26):
        counter = 0
        for y in range(0, len(ctxt)):
            if tab_ctxt[y] == tab_of_letters[x]:
                counter += 1
        calc_freq_letters[tab_of_letters[x]] = counter

    sorted_letters_with_freq = list(dict(sorted(calc_freq_letters.items(), key=lambda x: x[1], reverse=True)))[:len(eng)]
    for x in range(0, len(eng)):
        letters_frequency[sorted_letters_with_freq[x]] = dict_of_letters[sorted_letters_with_freq[x]]
    print(tab_ctxt_numbers)
    print(letters_frequency)
    return tab_ctxt_numbers, letters_frequency

#Decryption with idea of all combinations... It should work better than brutal force but it depends on the numbers of letters in ang and pol arrays
def decryption(ctxt_numbers, lang_sens, letters_frequency):
    for i in range(0,len(lang_sens)-1):
        lang_sens =shift_dict(lang_sens,i)
        for j in range(0,len(lang_sens)-1):
            letters_frequency = shift_dict(letters_frequency,j)
            y1 = list(letters_frequency.values())[i]
            x1 = list(lang_sens.values())[i]

            y2 = list(letters_frequency.values())[i + 1]
            x2 = list(lang_sens.values())[i + 1]
            a, b = soe(x1, x2, y1, y2)
            for j in range(0, len(ctxt_numbers)):
                ptxt.append(chr(cong(ctxt_numbers[j], a, b) + 65))
            print("".join(ptxt))

            ptxt.clear()


def exec_polish(ctxt):
    tab_ctxt_numbers, letter_frequency = get_dicts(ctxt)
    decryption(tab_ctxt_numbers, pol, letter_frequency)


def exec_english(ctxt):
    tab_ctxt_numbers, letter_frequency = get_dicts(ctxt)
    decryption(tab_ctxt_numbers, eng, letter_frequency)

######################################################################################################

#The most frequency repeated letters in Polish
pol = {'A': ord('A') - 65, 'I': ord('I') - 65, 'O': ord('O') - 65, 'E': ord('E') - 65, 'Z': ord('Z') - 65,
       'N': ord('N') - 65, 'R': ord('R') - 65, 'W': ord('W') - 65, 'S': ord('S') - 65, 'T': ord('T') - 65,
       'C': ord('C') - 65, 'Y': ord('Y') - 65, 'K': ord('K') - 65, 'D': ord('D') - 65, 'P': ord('P') - 65,
       'M': ord('M') - 65, 'U': ord('U') - 65, 'J': ord('J') - 65}
#The most frequency repeated letters in English
eng = {'E': ord('E') - 65, 'T': ord('T') - 65, 'A': ord('A') - 65, 'O': ord('O') - 65, 'I': ord('I') - 65,
       'N': ord('N') - 65, 'S': ord('S') - 65, 'H': ord('H') - 65, 'R': ord('R') - 65, 'D': ord('D') - 65,
       'L': ord('L') - 65, 'U': ord('U') - 65, 'C': ord('C') - 65, 'M': ord('M') - 65, 'F': ord('F') - 65,
       'W': ord('S') - 65, 'Y': ord('S') - 65,'G': ord('G') - 65,'P': ord('P') - 65 }

# test texts(English)
ctxt = "EGNWTAWHPNHCEGVPWAHSTSJVFEVHSNMNAJVPNVPEHANDVSYBHTEGFEENMVPWAVDFAVOBJHSJNASNYXVEGGVRGLTFOVEBENJGSVJFODFSTPJAVWEPVEPNDWGFPVPVPHSFAEFSYENJGSHOHRBFPVSEGNTSYNAOBVSRRANNZXHAY"
ctxt = "FYEPXMOCYFPYZYLQWMLBMIDMGYFPYIPLMYGUVUCFLKSYBKLFMFMIFPYMBMUFXKAYSMZYXFUYVVULFHQFPUIYWPUKLYFUUWYYGFUUWYKLQULFUUBCDDFURDKQFPYSKAY"
ctxt = "BKDBCRBHAROIRKBBKIESKRSKUPERRANCPIEPSAIBKDDCJQEPAROEXKUBERRANCPIEPACIGHCRSKUIBKDDCJQEPAROEXKUBQKKMAROBKJESAIKUPGHEBKMESFCBIQCFCXPEBCXUBJKGCHENCBKQCFCXPEBCBKOCBHCPABHKUOHBGCKRFSQCFCXPEBCJAYDKPBERBCNCRBISKUQERQCFCXPEBCERRANCPIEPACIGABHSKUPRCZBHUIXERJSKUJKRBFAMCGHEBADAQMKUBIKABHKUOHBGHSXKBHCPAOKBSKUEDPCICRBGKPBHEJKFFEPVKPCNCPSBAYCSKUGCPCRAQCBKYCBHAISCEPHCPCIEVANCOAVBQCPBAVAQEBCVKPYQJKREFJIAVSKUGERBYCBKDPCBCRJFAMCAQEPCEXKUBKUPERRANCPIEPSAGAFFSKUGERBBKOKKUBBKJARRCPKMESKMESAFFBEMCSKUBKDALLEHUBAVABFFIHUBSEUDABHKUOHBSKUKRFSHEJBKQCFCXPEBCERRANCPIEPACIGHAFCSKUGCPCIBAFFRFKNC"
ctxt = "EGNWTAWHPNHCEGVPWAHSTSJVFEVHSNMNAJVPNVPEHANDVSYBHTEGFEENMVPWAVDFAVOBJHSJNASNYXVEGGVRGLTFOVEBENJGSVJFODFSTPJAVWEPVEPNDWGFPVPVPHSFAEFSYENJGSHOHRBFPVSEGNTSYNAOBVSRRANNZXHAY"
#test texts(Polish)
#2ctxt = "BWGXOIYCFKXACWK"
ptxt = []


def affi_breaker(arg, ctxt):
    if arg == '1':
        exec_polish(ctxt)
    elif arg == '2':
        exec_english(ctxt)
    else:
        quit()
print("[1]. Polish")
print("[2]. English")
arg = input("Select language\n")
affi_breaker(arg,ctxt)
