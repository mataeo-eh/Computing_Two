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
