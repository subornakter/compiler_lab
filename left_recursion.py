def remove_left_recursion(non_terminal, productions):

    alpha = []   # left recursive part
    beta = []    # non-left recursive part


    # separate alpha and beta
    for prod in productions:

        if prod.startswith(non_terminal):

            # remove non-terminal part
            alpha.append(prod[len(non_terminal):])

        else:

            beta.append(prod)



    # if no left recursion
    if not alpha:

        print(non_terminal + " -> " + " | ".join(beta))
        return



    new_non_terminal = non_terminal + "'"



    # A -> βA'
    print(non_terminal + " -> ", end="")

    print(" | ".join(
        [b + new_non_terminal for b in beta]
    ))



    # A' -> αA' | ε
    print(new_non_terminal + " -> ", end="")

    print(" | ".join(
        [a + new_non_terminal for a in alpha]
    ) + " | ε")


# -------- Main Program --------


grammar = {

    "E": ["E+T", "T"],

    "T": ["T*F", "F"],

    "F": ["(E)", "id"]

}



print("Original Grammar")
print("----------------")


for nt, prod in grammar.items():

    print(nt + " -> " + " | ".join(prod))



print("\nAfter Removing Left Recursion")
print("-----------------------------")



# apply function for every non terminal

for nt, prod in grammar.items():

    remove_left_recursion(nt, prod)
