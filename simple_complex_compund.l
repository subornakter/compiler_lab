%{
#include<stdio.h>

%}

%%

.*(and|but|or|so).* { printf("Compound Sentence\n");}

.*(because|although|if|when|since|while|that).* { printf("Complex Sentence\n");}

.* { printf("Simple Sentence\n");}

%%

int yywrap()
{
    return 1;
}

int main()
{
    printf("Enter a sentence:\n");

    yylex();

    return 0;
}
