%{
#include<stdio.h>

int id_count = 0;

%}

%%

"int"|"float"|"double"|"char"|"if"|"else"|"for"|"while"|"do"|"return"|"void"|"auto"|"break"|"case"|"const"|"continue"|"default"|"enum"|"extern"|"goto"|"long"|"register"|"short"|"signed"|"sizeof"|"static"|"struct"|"switch"|"typedef"|"union"|"unsigned"|"volatile" ;

\".*\" ;

[a-zA-Z_][a-zA-Z0-9_]* { printf("Identifier: %s\n", yytext); id_count++; }

.|\n ;

%%

int yywrap()
{
    return 1;
}

int main()
{
    yylex();

    printf("\nTotal Identifiers = %d\n", id_count);

    return 0;
}