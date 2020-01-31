yatirilanPara = int(input('Yatırılan para?'))
ay = 1
kazanilanPara = 0

while ay <= 12:
    if ay == 1:
        if yatirilanPara < 1000:
            kazanilanPara = kazanilanPara + yatirilanPara * 0.2
        elif yatirilanPara > 1000:
            kazanilanPara = kazanilanPara + yatirilanPara * 0.3
    elif ay == 2:
        if yatirilanPara < 1500:
            kazanilanPara = kazanilanPara + yatirilanPara * 0.1
        elif yatirilanPara > 2000:
            kazanilanPara = kazanilanPara + yatirilanPara * 0.12
        else:
            kazanilanPara = kazanilanPara + yatirilanPara * 0.05

    elif ay == 3:
        if yatirilanPara < 1500:
            kazanilanPara = kazanilanPara + yatirilanPara * 0.1
        elif yatirilanPara > 2000:
            kazanilanPara = kazanilanPara + yatirilanPara * 0.12
        else:
            kazanilanPara = kazanilanPara + yatirilanPara * 0.04
    else:
        kazanilanPara = kazanilanPara + yatirilanPara * 0.03
    ay = ay + 1

print(kazanilanPara)
