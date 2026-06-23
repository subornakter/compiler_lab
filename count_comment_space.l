%{
#include<stdio.h>

int space_count = 0;
int comment_count = 0;

%}

%%

"//".*                         { comment_count++; }

"/*"([^*]|\*+[^*/])*\*+"/"     { comment_count++; }

[ \t]+                         { space_count += yyleng; }

.|\n                             ;

%%

int yywrap()
{
    return 1;
}

int main()
{
    yylex();

    printf("Number of Spaces: %d\n", space_count);
    printf("Number of Comments: %d\n", comment_count);

    return 0;
}
