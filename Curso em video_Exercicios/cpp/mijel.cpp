#include <iostream>
#include <string>
#include <stdlib.h>

using namespace std;

void calculoMedia();

int main(){
    float nota1,nota2,nota3,nota4;

        cout << "\tCÁLCULO D SUA MEDIA ANUAL\n\n";
        cout << "Digite suas notas abaixo:\n";
        cout << "1º Bimestre: "; cin >> nota1; 
        cout << "2º Bimestre: "; cin >> nota2; 
        cout << "3º Bimestre: "; cin >> nota3; 
        cout << "4º Bimestre: "; cin >> nota4; 

    calculoMedia(nota1, nota2, nota3, nota4);

    return 0;
}
void  calculoMedia(float nota1, float nota2, float nota3, float nota4){

        float mediaAnual = (nota1 + nota2 + nota3 + nota4)/4; 

        cout << "Sua média anual é:" << mediaAnual << endl;
}