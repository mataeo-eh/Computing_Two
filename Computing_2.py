        from __future__ import division
        import math
        
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
