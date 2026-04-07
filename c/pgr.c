#include<stdio.h>
#include<locale.h>

int main (void)

{
    setlocale(LC_ALL,"");
    char nome[40], cidade[40];
    int idade;
    printf("digite o nome da pessoa ");
    scanf("%s",&nome);

    printf("digite o nome da cidade ");
    scanf("%s",&cidade);

    printf("digite a idade da pessoa ");
    scanf("%d",&idade);

    if (idade>=18)
    {
        printf("%s, nascido em %s, com a idade %d, � maior de idade",nome, cidade, idade );
    }
    else
    {
        printf(" %s, nascido em %s, com a idade %d, � menor de idade",nome, cidade, idade );
    }
}

