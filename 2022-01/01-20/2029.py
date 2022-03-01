class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        # 数字虽然是无穷的，但又其实是有限的
        # 数学本质上是规则的集合，是对现实的抽象，但又不完全来源于现实。
        # Only in one way Bob will lose the game:
        # there only left stone(s) that will cause the sum of all removed stones is divisibled by 3
        # 0. 由于是除以3,所以所有的数值可以分为除3余0,1,2三种情况，对应的石头数量记为n0, n1, n2。
        # 0.1 Alice具有先手选择权，Bob在所有石头被选完的情况下依然胜利。
        # 0.2 Alice第一手要不选1,要不选2，并且Alice选了1,Bob也必须选同样类型的石头，同时也会导致类型发生转变，所以可以进行游戏的序列一定是：
        # 11212121...; 22121212... (Alice选了1之后，Bob必须一直选1，Alice必须一直选2;Alice选了2之后，Bob必须一直选2，Alice必须一直选1)
        # 1. 首先n0是偶数的情况下，n0对应的石头不会影响胜负（双方都会进行最优操作，劣势一方选0来延长对局，另一方也会选0来抵消，而优势一方不会主动选0,让出优势），所以可以忽略n0
        # 1.1 我们知道Bob输的情况，一定是Bob选择了并且只能选择使得被移除的石头和为3的倍数。所以n1=0,n2=0或n1=0或n2=0的情况下，Bob赢（即无法迫使Bob选择使得和为3的倍数的石头）;
        # 1.2 n1和n2都存在的情况下，Alice可以迫使Bob只能选择使得和为3的倍数的石头，必胜(Alice选择数量不是最多的或者相等的情况下任意选择)。
        # 2. n0是奇数的情况下，等价于n0=1的情况，此时Bob可以优先选择n0来规避困境，若Bob不使用，则Alice可以使用，但只要使用就一定会切换双方使用的类型（换手）。
        # 2.1 如果Alice要赢，必须迫使Bob只能选择和为3的倍数的石头，但由于出现了一个反制的选择，如果Alice继续拿更少的石子（或者相等数量的石子），Bob拿n0的石子进行换手会导致自己永远要选更少的石子而先输掉游戏(比如Alice先拿1，本来是Bob需要一直选1,1更少的情况下，Bob会输，但使用n0进行换手，则导致Alice需要选1)。
        # 2.2 所以Alice必须拿数量更多的石子，并且只多一个或两个还不行，因为那样Bob只需要把n0留到最后进行换手，Bob必胜。
        # 2.3 如果abs(n1 - n2)>2，则Alice只需要在第一轮选择最多的石子即可获胜（第一手选完后，Bob同样需要选数量多的石子来避免出局，Alice则选数量少的石子，并在数量少的石子用完后使用n0进行换手，使得Bob最后必须选择使得和为3的倍数的石子）。
        # 即使Bob先使用n0进行换手（此时变成Alice选择数量多的石子，Bob需要选数量少的，则Bob在选完数量少的石子后，依然会在最后必须选择使得和为3的倍数的石子），Alice依然获胜。
        # examples for 2.1, 2.2, 2.3:
        # [1,1,1,2,2,0]
        # ABABAB
        # 112120 Alice lose
        # 110212 although Alice choose 0 still lose
        # 2021 if choose less, Alice lose faster
        # [1,1,1,1,2,2,0,]
        # ABABABA
        # 1121210 Alice lose
        # 1102121 although Alice choose 0 still lose
        # 2021 if choose less, Alice lose faster
        # [1,1,1,1,1,2,2,0]
        # ABABABA
        # 1121210 Alice win
        # 1121201
        # ABABABAB
        # 10121211 Alice win

        # personal resolution
        n0 = n1 = n2 = 0
        for s in stones:
            if s % 3 == 0:
                n0 += 1
            elif s % 3 == 1:
                n1 += 1
            else:
                n2 += 1

        if n0 % 2 == 0:
            if n1 == 0 or n2 == 0:
                return False
            return True
        else:
            if abs(n1 - n2) > 2:
                return True
            return False

        # official resolution
        # cnt0 = cnt1 = cnt2 = 0
        # for val in stones:
        #     if (typ := val % 3) == 0:
        #         cnt0 += 1
        #     elif typ == 1:
        #         cnt1 += 1
        #     else:
        #         cnt2 += 1
        # if cnt0 % 2 == 0:
        #     return cnt1 >= 1 and cnt2 >= 1
        # return cnt1 - cnt2 > 2 or cnt2 - cnt1 > 2
        #
