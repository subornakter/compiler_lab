def automated_cfg_resolver(ambiguous_rules):

    print("------ Original Grammar ------")

    for nt, productions in ambiguous_rules.items():

        rules = []

        for p in productions:
            rules.append(" ".join(p))

        print(nt + " -> " + " | ".join(rules))


    print()



    operators = []
    atoms = []


    productions = ambiguous_rules["E"]


    for p in productions:


        if len(p)==3 and p[0]=="E" and p[2]=="E":

            operators.append(p[1])


        elif "E" not in p:

            atoms.append("".join(p))



    if len(operators)<=1:

        print("Grammar is already non-ambiguous")
        return



    print(f"Ambiguity Detected! Operators found: {operators}")

    print("Logic: Applying Precedence Layering (Lowest to Highest)\n")



    levels = ["E","T","F"]


    resolved=[]



    for i,op in enumerate(operators):


        current = levels[i]

        next_nt = levels[i+1]


        resolved.append(
            f"{current} -> {current} {op} {next_nt} | {next_nt}"
        )



    resolved.append(
        f"{levels[len(operators)]} -> ( E ) | {' | '.join(atoms)}"
    )



    print("--- Non-Ambiguous Grammar Generated ---")


    for rule in resolved:

        print(rule)





# Input Grammar

input_rules = {


"E":[

["E","+","E"],

["E","*","E"],

["(","E",")"],

["id"]

]

}

automated_cfg_resolver(input_rules)
