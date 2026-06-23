%{
#include<stdio.h>

int char_count = 0;
int word_count = 0;
int line_count = 0;

%}

%%

[a-zA-Z0-9_]+ {
    word_count++;
    char_count += yyleng;
}

[ \t] ;

\n {
    char_count++;
    line_count++;
}

. {
    char_count++;
}

%%

int yywrap()
{
    return 1;
}

int main()
{
    yylex();

    printf("Characters: %d\nWords: %d\nLines: %d\n",
            char_count, word_count, line_count);

    return 0;
}