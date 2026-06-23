%{
#include <stdio.h>
#include <string.h>

int count = 0;
%}

TO_BE_VERB    am|is|are|was|were|be|being|been

%%

{TO_BE_VERB}    { count++; printf("Found 'to be' verb: %s\n", yytext); }

[a-zA-Z]+       ;

.|\n            ;

%%

int yywrap()
{
    return 1;
}

int main()
{
    printf("Enter a paragraph:\n\n");

    yylex();

    printf("\nTotal 'to be' verbs found: %d\n", count);

    return 0;
}
