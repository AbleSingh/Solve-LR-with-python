def solvelr():
    #enter the number of productions
    n=int(input("enter the number of productions :: "))
    #enter the productions in array
    p=[]
    print("Enter productions :: ")
    for i in range(n):
        x = input()
        p.append(x)

    #dictionary of productions
    prod={}
    nonterminals = []
    t = []

    #split the productions
    for i in range(n):
        prodlist=p[i].split('->')
        tempdict = {prodlist[0]:prodlist[1].split('|')}
        prod.update(tempdict)
        tempdict.clear()
        nonterminals.append(prodlist[0])
        t.append(prodlist[1].split('|'))

    terminals1=[]

    terminals = [item for sublist in t for item in sublist]
    for i in terminals:
        terminals1.append(list(i))

    terminals = [item for sublist in terminals1 for item in sublist]
    terminals = list(set(terminals))
    for i in terminals:
        if i in nonterminals:
            terminals.remove(i)

    print("\n  Productions :: ", prod)
    print("Non Terminals :: ", nonterminals)
    print("    Terminals :: ", terminals)


    for i in prod:
        for j in prod:
            if i != j and j != "S":
                for k in range(len(prod[j])):
                    if i == prod[j][k][0]:
                        for l in range(len(prod[i])):
                            letter1 = (prod[j][k+l].replace(i, prod[i][l]))[0]
                            # print(letter1, j)
                            prod[j].append(prod[j][k])
                            if letter1 == j:
                                prod[j][k+l] = prod[j][k+l].replace(i, prod[i][l])



    lrprod={}
    nonlrprod = prod.copy()
    # print(prod)
    # print(nonlrprod)


    #select productions with left recursion
    print("\n")
    for i in prod:
        for j in range(len(prod[i])):
            if i == prod[i][j][0]:
                # print("Left Recursion in Grammar", i, "->", prod[i][j])
                if i not in lrprod:
                    lst = [prod[i][j]]
                    lrprod.update({i:lst})
                else:
                    lrprod[i].append(prod[i][j])

    #select productions with no left recursion
    for it in range(5, 0, -1):
        for i in nonlrprod:
            for j in range(len(nonlrprod[i])-it):
                if i == nonlrprod[i][j][0]:
                    # print(nonlrprod[i])
                    # print(nonlrprod[i][j])
                    nonlrprod[i].remove(nonlrprod[i][j])

    for i in nonlrprod:
        nonlrprod[i] = list(set(nonlrprod[i]))

    #printing all lr productions
    count = 0
    print("\nLeft Recursive Productions :: ")
    for i in lrprod:
        for j in range(len(lrprod[i])):
            print(i, "->", lrprod[i][j])
            count+=1
    print("\nTotal Left Recursive Productions :: ", count)

    #printing all non lr productions
    count = 0
    print("\nNon Left Recursive Productions :: ")
    for i in nonlrprod:
        for j in range(len(nonlrprod[i])):
            print(i, "->", nonlrprod[i][j])
            count+=1
    print("\nTotal Non Left Recursive Productions :: ", count)

    # print(lrprod)
    # print(nonlrprod)

    newprod={}

    alphalist = []
    list1=[]
    for i in nonterminals:
        if i in lrprod:
            alphalist.append(lrprod[i])
            alpha_list = [item for sublist in alphalist for item in sublist]
            alphalist.clear()
            for j in alpha_list:
                list1.append(list(j))
            alpha_list.clear()
            alpha_list = [item for sublist in list1 for item in sublist]
            list1.clear()
            for k in alpha_list:
                if k == i:
                    alpha_list.remove(k)
            # print(alpha_list)
            alpha_list = [e + i + "'" for e in alpha_list]
            newnonterm = i+"'"
            newprod.update({newnonterm:alpha_list})
            newprod[newnonterm].append("E")

    for i in nonterminals:
        if i in nonlrprod and i!="S":
            nonlrprod[i] = [e + i + "'" for e in nonlrprod[i]]
            nonlrprod.update({i:nonlrprod[i]})

    print("\nAlpha productions :: ", newprod)
    print("\n Beta Productions :: ", nonlrprod)

    def Merge(dict1, dict2):
        res = {**dict1, **dict2}
        return res

    final_productions = (Merge(nonlrprod, newprod))
    print("\nFinal Productions :: ", final_productions)

    #printing all final productions
    count = 0
    print("\nFinal Productions :: ")
    for i in final_productions:
        for j in range(len(final_productions[i])):
            print(i, "->", final_productions[i][j])
            count+=1
    print("\nTotal Final Productions :: ", count)


solvelr()

# S->Abc|Xbc
# A->Ab|Ac|ash
# B->Bb|xyb|xA
# X->yAb|Xb|Sab
# Y->xBa|abB