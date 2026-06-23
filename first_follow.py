EPSILON = 'ε'

def compute_first_of_string(symbols, first, terminals):

    result = set()

    for sym in symbols:

        if sym == EPSILON:
            result.add(EPSILON)
            break

        elif sym in terminals:
            result.add(sym)
            break

        else:
            result.update(first[sym] - {EPSILON})

            if EPSILON not in first[sym]:
                break

    else:
        result.add(EPSILON)

    return result



def compute_first(grammar, non_terminals, terminals):

    first = {nt:set() for nt in non_terminals}

    changed = True

    while changed:

        changed = False

        for nt in grammar:

            for production in grammar[nt]:

                before = len(first[nt])

                first[nt].update(
                    compute_first_of_string(
                        production,
                        first,
                        terminals
                    )
                )

                if len(first[nt]) != before:
                    changed=True

    return first




def compute_follow(grammar, non_terminals, terminals, start_symbol, first):

    follow = {nt:set() for nt in non_terminals}


    follow[start_symbol].add('$')


    changed=True


    while changed:

        changed=False


        for head in grammar:


            for production in grammar[head]:


                for i,symbol in enumerate(production):


                    if symbol in non_terminals:


                        before=len(follow[symbol])


                        beta=production[i+1:]


                        if beta:

                            first_beta = compute_first_of_string(
                                beta,
                                first,
                                terminals
                            )


                            follow[symbol].update(
                                first_beta-{EPSILON}
                            )


                            if EPSILON in first_beta:

                                follow[symbol].update(
                                    follow[head]
                                )


                        else:

                            follow[symbol].update(
                                follow[head]
                            )


                        if len(follow[symbol]) != before:
                            changed=True


    return follow





# ---------------- MAIN ----------------


if __name__=="__main__":


    grammar = {


        'E':[['T',"E'"]],
        "E'":[['+','T',"E'"],[EPSILON]],
        'T':[['F',"T'"]],
        "T'":[['*','F',"T'"],[EPSILON]],
        'F':[['(','E',')'],['id']]

    }



    start_symbol='E'


    non_terminals=set(grammar.keys())


    terminals=set()



    for productions in grammar.values():

        for production in productions:

            for symbol in production:

                if symbol not in non_terminals and symbol != EPSILON:

                    terminals.add(symbol)





    # Grammar Print


    print("="*50)

    print("Grammar")

    print("="*50)



    for nt,productions in grammar.items():

        print(
            nt,
            "->",
            " | ".join(
                "".join(p) for p in productions
            )
        )




    first = compute_first(
        grammar,
        non_terminals,
        terminals
    )



    print("\nFIRST SET")

    print("-"*50)



    for nt in grammar:


        print(
            "FIRST("+nt+") = {",
            ", ".join(first[nt]),
            "}"
        )




    follow = compute_follow(
        grammar,
        non_terminals,
        terminals,
        start_symbol,
        first
    )



    print("\nFOLLOW SET")

    print("-"*50)



    for nt in grammar:


        print(
            "FOLLOW("+nt+") = {",
            ", ".join(follow[nt]),
            "}"
        )
