%{
#include<stdio.h>
%}

%%

[+-]?[0-9]+(\.[0-9]+)?[eE][+-]?[0-9]+   {printf("Exponential Number: %s\n", yytext);}

[+-]?[0-9]+[+-][0-9]+i                  {printf("Complex Number: %s\n", yytext);}

[+-]?[0-9]+\.[0-9]+                     {printf("Floating Point Number: %s\n", yytext);}

[+-]?[0-9]+                             {printf("Integer Number: %s\n", yytext);}

.|\n                                    ;

%%

int yywrap()
{
    return 1;
}

int main()
{
    yylex();
    return 0;
}