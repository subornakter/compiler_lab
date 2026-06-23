%{
#include<stdio.h>
#include<string.h>

int isKeyword(char buffer[])
{
    char keywords[32][10] = {
        "auto","break","case","char","const","continue","default",
        "do","double","else","enum","extern","float","for","goto",
        "if","int","long","register","return","short","signed",
        "sizeof","static","struct","switch","typedef","union",
        "unsigned","void","volatile","while"
    };

    for(int i=0;i<32;i++)
    {
        if(strcmp(keywords[i],buffer)==0)
            return 1;
    }

    return 0;
}

%}

%%

"#include"<.*">"        { printf("%s : PREPROCESSOR\n", yytext); }

[a-zA-Z_][a-zA-Z0-9_]*  { 
                            if(isKeyword(yytext))
                                printf("%s : KEYWORD\n",yytext);
                            else
                                printf("%s : IDENTIFIER\n",yytext);
                         }

[0-9]+(\.[0-9]+)?       { printf("%s : CONSTANT\n",yytext); }

[+\-*/%=<>]             { printf("%s : OPERATOR\n",yytext); }

[(){};,]                { printf("%s : PUNCTUATOR\n",yytext); }

[ \t\n]+                ;

.                       { printf("%s : UNKNOWN\n",yytext); }

%%

int yywrap()
{
    return 1;
}

int main()
{
    printf("Enter C Program:\n\n");

    yylex();

    return 0;
}