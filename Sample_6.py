def minion_game(string):
    v="AEIOU"
    sscore=0
    kscore=0
    length=len(string)
    for i in range(length):
        if s[i] in v:
           kscore=kscore+(length-i)
        else:
           sscore=sscore+(length-i)
    if sscore>kscore:
       print ("Stuart", sscore)
    elif kscore>sscore:
       print ("Kevin", kscore)
    elif kcore==sscore:
       print ("Draw")
if __name__ == '__main__':
    s = input()
    minion_game(s)
