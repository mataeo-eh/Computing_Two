from __future__ import division 
import math

type = input("please tell me which type you want: dissociation (1), titration (2) : ")

if type == "2":
    #input
    monoprotic = "monoprotic"
    diprotic = "diprotic"
    triprotic = "triportic"
    case1 = input("Please type one of the following: monoprotic, diprotic, triprotic :")

    if case1 == "monoprotic":
        kA1 = input("enter ka1 value: ")


        ka1 = float(kA1)
        
        OHNegative = input("enter OH- [OH] value : ")
        LOh = input("Enter L of OH-: ")
        LHA = input("Enter L of H3A: ")
        HA = input("Enter [H3A] value: ")


        OHnegative = float(OHNegative)
        LOH = float(LOh)
        LHA = float(LHA)
        HA = float(HA)


        # H3A
        AL3 = LHA * HA
        AJ3 = OHnegative * LOH
        AJ4 = AJ3 / (LOH + LHA)
        AJ6 = LOH - LHA
        AJ7 = AJ3 - AL3
        AJ8 = LOH + LHA
        AJ9 = AJ7 / AJ8
        AM4 = AL3 - AJ3
        AM5 = AM4 / (LOH + LHA)
        AF2 = AJ4

        # ae block
        AE6 = ka1 * AM5
        AE8 = 1
        AE10 = (-1) * AE6
        AE11 = AF2 + ka1
        AE12 = AE11 ** 2
        AE13 = AE12 - (4 * 1 * AE10)
        AE14 = math.sqrt(AE13)
        AE15 = (AE11 * -1) + AE14
        AE16 = AE15 / (2 * AE8)

        AE3 = AM5 - AE16

        # y-aa
        Y2 = ka1

        if Y2 == 0:
            AB2 = 0
        else:
            AB2 = (math.log10(Y2) * -1)




        if Y2 == 0:
            AB7 = 0
        else:
            AB7 = 0.000000000000001 / Y2



        # af block
        AF2 = AJ4
        AF3 = AE16

        AF9 = AE16




        # AG

        # AG7=X10*AH2
        AG9 = AE16

        # X block
        X9 = AE16 + 0.0000001 + 0
        X14 = X9

        if X9 <= 0:
            X3 = 0
        else:
            X3 = (math.log10(X9) * -1)
        pH = X3
        # if X10 <= 0:
        #   X4 = 0
        # else:
        #    X4 = (math.log10(X10) * -1)

        X18 = AE16 + 0.0000001
        if AE3==0:
            X19=0
        else:
            X19 = AF2 / AE3
        if X19 <= 0:
            X20 = 0
        else:
            X20 = math.log10(X19)

        X5 = AB2 + X20
        if AJ9 <= 0:
            X6 = 0
        else:
            X6 = (math.log10(AJ9) * -1)

        # misc block
        AF7 = X9 * 0
        Z9 = 14 - X3
        Y9 = (10 ** -Z9)
        Y11 = 10 ** (-X6)
        Z10 = 14 - X5
        Z11 = 14 - X6
        # X block pt 2
        HHE = X5
        EB = X6
        X7 = (AB2 + 0) / 2
        EP = X7
        NpH = 14 - (X3)
        NHHE = 14 - (X5)
        NEB = 14 - (X6)

        # final

        H3AF = AM5-AF3
        pKa1F = AB2

        H2AF = AE16

        if AM4 <= 0:
            H3a = AL3 / ((LOH + LHA))

            pKa1 = 0
            pKa2 = 0
            pKa3 = 0
            # HplusH2A=float(HplusH2a)
            if AM4 == 0:
                ka1=0.00000000000001/ka1
            else:
                ka1=ka1

            A = ((ka1) * (H3a))
            B = 1
            C = 0
            D = ((-1) * A)
            E = ((ka1) * (ka1))
            F = ((E) - (4 * (B) * D))
            G = math.sqrt(F)
            H = (-ka1) + G
            I = (H) / (2 * (B))
            Hpos = I
            if I == 0:
                pH = 0
            else:
                pH = (math.log10(I) * -1)
            pOH = 14 - (pH)
            if I > 0:
                H2af = I
            else:
                H2af = 0
            log1 = 10 ** ((pKa1) * -1)
            log2 = 10 ** ((pKa2) * -1)
            log3 = 10 ** ((pKa3) * -1)
            if ka1 == 0:
                pKa1F = 0
            else:
                pKa1F = (math.log10(ka1) * -1)

            # part2

            I9 = I




            J9 = Hpos

            pKB1 = 14 - pKa1F

            if pKa1F == 0:
                pKB1 = 0
            else:
                pKB1 = pKB1

            pH = 14 - pH
            pOH = 14 - (pH)



            print("[A-] =", H2af)

            print("pH   =", pH)
            print("[H+]   =", Hpos)
            print("pOH  =", pOH)
            print("pKa1 =", pKa1F)

            print("pKB1 =", pKB1)



        else:
            # block 2 normal monoprotic final outputs
            print("pKa1 = ", pKa1F)

            print("[HA] = ", H3AF)
            print("[A-] = ", H2AF)

            print("pH = ", pH)
            print("HHE = ", HHE)
            print("equivalence point = ", EP)
            print("excess base = ", EB)
            print("Non buffer excess base = ", NEB)
            print("pOH HHE = ", NHHE)
            print("pOH = ", NpH)
            # initialize sum and counter




    else:
        none = 2


if case1 == "monoprotic":
        kA1 = input("enter ka1 value: ")


        ka1 = float(kA1)
        
        OHNegative = input("enter OH- [OH] value : ")
        LOh = input("Enter L of OH-: ")
        LHA = input("Enter L of H3A: ")
        HA = input("Enter [H3A] value: ")


        OHnegative = float(OHNegative)
        LOH = float(LOh)
        LHA = float(LHA)
        HA = float(HA)


        # H3A
        AL3 = LHA * HA
        AJ3 = OHnegative * LOH
        AJ4 = AJ3 / (LOH + LHA)
        AJ6 = LOH - LHA
        AJ7 = AJ3 - AL3
        AJ8 = LOH + LHA
        AJ9 = AJ7 / AJ8
        AM4 = AL3 - AJ3
        AM5 = AM4 / (LOH + LHA)
        AF2 = AJ4

        # ae block
        AE6 = ka1 * AM5
        AE8 = 1
        AE10 = (-1) * AE6
        AE11 = AF2 + ka1
        AE12 = AE11 ** 2
        AE13 = AE12 - (4 * 1 * AE10)
        AE14 = math.sqrt(AE13)
        AE15 = (AE11 * -1) + AE14
        AE16 = AE15 / (2 * AE8)

        AE3 = AM5 - AE16

        # y-aa
        Y2 = ka1

        if Y2 == 0:
            AB2 = 0
        else:
            AB2 = (math.log10(Y2) * -1)




        if Y2 == 0:
            AB7 = 0
        else:
            AB7 = 0.000000000000001 / Y2



        # af block
        AF2 = AJ4
        AF3 = AE16

        AF9 = AE16




        # AG

        # AG7=X10*AH2
        AG9 = AE16

        # X block
        X9 = AE16 + 0.0000001 + 0
        X14 = X9

        if X9 <= 0:
            X3 = 0
        else:
            X3 = (math.log10(X9) * -1)
        pH = X3
        # if X10 <= 0:
        #   X4 = 0
        # else:
        #    X4 = (math.log10(X10) * -1)

        X18 = AE16 + 0.0000001
        if AE3==0:
            X19=0
        else:
            X19 = AF2 / AE3
        if X19 <= 0:
            X20 = 0
        else:
            X20 = math.log10(X19)

        X5 = AB2 + X20
        if AJ9 <= 0:
            X6 = 0
        else:
            X6 = (math.log10(AJ9) * -1)

        # misc block
        AF7 = X9 * 0
        Z9 = 14 - X3
        Y9 = (10 ** -Z9)
        Y11 = 10 ** (-X6)
        Z10 = 14 - X5
        Z11 = 14 - X6
        # X block pt 2
        HHE = X5
        EB = X6
        X7 = (AB2 + 0) / 2
        EP = X7
        NpH = 14 - (X3)
        NHHE = 14 - (X5)
        NEB = 14 - (X6)

        # final

        H3AF = AM5-AF3
        pKa1F = AB2

        H2AF = AE16

        if AM4 <= 0:
            H3a = AL3 / ((LOH + LHA))

            pKa1 = 0
            pKa2 = 0
            pKa3 = 0
            # HplusH2A=float(HplusH2a)
            if AM4 == 0:
                ka1=0.00000000000001/ka1
            else:
                ka1=ka1

            A = ((ka1) * (H3a))
            B = 1
            C = 0
            D = ((-1) * A)
            E = ((ka1) * (ka1))
            F = ((E) - (4 * (B) * D))
            G = math.sqrt(F)
            H = (-ka1) + G
            I = (H) / (2 * (B))
            Hpos = I
            if I == 0:
                pH = 0
            else:
                pH = (math.log10(I) * -1)
            pOH = 14 - (pH)
            if I > 0:
                H2af = I
            else:
                H2af = 0
            log1 = 10 ** ((pKa1) * -1)
            log2 = 10 ** ((pKa2) * -1)
            log3 = 10 ** ((pKa3) * -1)
            if ka1 == 0:
                pKa1F = 0
            else:
                pKa1F = (math.log10(ka1) * -1)

            # part2

            I9 = I




            J9 = Hpos

            pKB1 = 14 - pKa1F

            if pKa1F == 0:
                pKB1 = 0
            else:
                pKB1 = pKB1

            pH = 14 - pH
            pOH = 14 - (pH)



            print("[A-] =", H2af)

            print("pH   =", pH)
            print("[H+]   =", Hpos)
            print("pOH  =", pOH)
            print("pKa1 =", pKa1F)

            print("pKB1 =", pKB1)



        else:
            # block 2 normal monoprotic final outputs
            print("pKa1 = ", pKa1F)

            print("[HA] = ", H3AF)
            print("[A-] = ", H2AF)

            print("pH = ", pH)
            print("HHE = ", HHE)
            print("equivalence point = ", EP)
            print("excess base = ", EB)
            print("Non buffer excess base = ", NEB)
            print("pOH HHE = ", NHHE)
            print("pOH = ", NpH)
            # initialize sum and counter

if case1 == "monoprotic":
        kA1 = input("enter ka1 value: ")


        ka1 = float(kA1)
        
        OHNegative = input("enter OH- [OH] value : ")
        LOh = input("Enter L of OH-: ")
        LHA = input("Enter L of H3A: ")
        HA = input("Enter [H3A] value: ")


        OHnegative = float(OHNegative)
        LOH = float(LOh)
        LHA = float(LHA)
        HA = float(HA)


        # H3A
        AL3 = LHA * HA
        AJ3 = OHnegative * LOH
        AJ4 = AJ3 / (LOH + LHA)
        AJ6 = LOH - LHA
        AJ7 = AJ3 - AL3
        AJ8 = LOH + LHA
        AJ9 = AJ7 / AJ8
        AM4 = AL3 - AJ3
        AM5 = AM4 / (LOH + LHA)
        AF2 = AJ4

        # ae block
        AE6 = ka1 * AM5
        AE8 = 1
        AE10 = (-1) * AE6
        AE11 = AF2 + ka1
        AE12 = AE11 ** 2
        AE13 = AE12 - (4 * 1 * AE10)
        AE14 = math.sqrt(AE13)
        AE15 = (AE11 * -1) + AE14
        AE16 = AE15 / (2 * AE8)

        AE3 = AM5 - AE16

        # y-aa
        Y2 = ka1

        if Y2 == 0:
            AB2 = 0
        else:
            AB2 = (math.log10(Y2) * -1)




        if Y2 == 0:
            AB7 = 0
        else:
            AB7 = 0.000000000000001 / Y2



        # af block
        AF2 = AJ4
        AF3 = AE16

        AF9 = AE16




        # AG

        # AG7=X10*AH2
        AG9 = AE16

        # X block
        X9 = AE16 + 0.0000001 + 0
        X14 = X9

        if X9 <= 0:
            X3 = 0
        else:
            X3 = (math.log10(X9) * -1)
        pH = X3
        # if X10 <= 0:
        #   X4 = 0
        # else:
        #    X4 = (math.log10(X10) * -1)

        X18 = AE16 + 0.0000001
        if AE3==0:
            X19=0
        else:
            X19 = AF2 / AE3
        if X19 <= 0:
            X20 = 0
        else:
            X20 = math.log10(X19)

        X5 = AB2 + X20
        if AJ9 <= 0:
            X6 = 0
        else:
            X6 = (math.log10(AJ9) * -1)

        # misc block
        AF7 = X9 * 0
        Z9 = 14 - X3
        Y9 = (10 ** -Z9)
        Y11 = 10 ** (-X6)
        Z10 = 14 - X5
        Z11 = 14 - X6
        # X block pt 2
        HHE = X5
        EB = X6
        X7 = (AB2 + 0) / 2
        EP = X7
        NpH = 14 - (X3)
        NHHE = 14 - (X5)
        NEB = 14 - (X6)

        # final

        H3AF = AM5-AF3
        pKa1F = AB2

        H2AF = AE16

        if AM4 <= 0:
            H3a = AL3 / ((LOH + LHA))

            pKa1 = 0
            pKa2 = 0
            pKa3 = 0
            # HplusH2A=float(HplusH2a)
            if AM4 == 0:
                ka1=0.00000000000001/ka1
            else:
                ka1=ka1

            A = ((ka1) * (H3a))
            B = 1
            C = 0
            D = ((-1) * A)
            E = ((ka1) * (ka1))
            F = ((E) - (4 * (B) * D))
            G = math.sqrt(F)
            H = (-ka1) + G
            I = (H) / (2 * (B))
            Hpos = I
            if I == 0:
                pH = 0
            else:
                pH = (math.log10(I) * -1)
            pOH = 14 - (pH)
            if I > 0:
                H2af = I
            else:
                H2af = 0
            log1 = 10 ** ((pKa1) * -1)
            log2 = 10 ** ((pKa2) * -1)
            log3 = 10 ** ((pKa3) * -1)
            if ka1 == 0:
                pKa1F = 0
            else:
                pKa1F = (math.log10(ka1) * -1)

            # part2

            I9 = I




            J9 = Hpos

            pKB1 = 14 - pKa1F

            if pKa1F == 0:
                pKB1 = 0
            else:
                pKB1 = pKB1

            pH = 14 - pH
            pOH = 14 - (pH)



            print("[A-] =", H2af)

            print("pH   =", pH)
            print("[H+]   =", Hpos)
            print("pOH  =", pOH)
            print("pKa1 =", pKa1F)

            print("pKB1 =", pKB1)



        else:
            # block 2 normal monoprotic final outputs
            print("pKa1 = ", pKa1F)

            print("[HA] = ", H3AF)
            print("[A-] = ", H2AF)

            print("pH = ", pH)
            print("HHE = ", HHE)
            print("equivalence point = ", EP)
            print("excess base = ", EB)
            print("Non buffer excess base = ", NEB)
            print("pOH HHE = ", NHHE)
            print("pOH = ", NpH)
            # initialize sum and counter
