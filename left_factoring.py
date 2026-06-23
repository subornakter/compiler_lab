def left_factoring(non_terminal, productions):

    if len(productions) < 2:
        print("No factoring needed")
        return


    # Step 1: Find common prefix
    prefix = productions[0]

    for prod in productions[1:]:

        temp = ""

        for i in range(min(len(prefix), len(prod))):

            if prefix[i] == prod[i]:
                temp += prefix[i]

            else:
                break

        prefix = temp



    if prefix == "":

        print("No common prefix found")
        return



    # Step 2: Find remaining parts

    alpha_list = [
        prod[len(prefix):]
        for prod in productions
    ]


    new_nt = non_terminal + "'"



    # Step 3: Print factored grammar

    print(non_terminal + " -> " + prefix + new_nt)

    print(new_nt + " -> " + " | ".join(alpha_list))





# -------- Main Program --------


grammar = {

    "A": ["abc", "acd"]

}



print("Original Grammar")
print("----------------")

for nt, prod in grammar.items():

    print(nt + " -> " + " | ".join(prod))



print("\nAfter Left Factoring")
print("--------------------")


for nt, prod in grammar.items():

    left_factoring(nt, prod)
