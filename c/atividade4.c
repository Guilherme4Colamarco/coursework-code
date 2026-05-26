#include <stdio.h>

int main(void)
{
    int n;


    do {
        printf("Digite ums numero entre 1 e 130: ");
        scanf("%d", &n);
    } while (n <= 0 || n >= 131);

    for (int i = n; i >= 0; i--) {
        printf("%d\n", i);
    }

    return 0;
}
