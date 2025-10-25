#include<stdio.h>
#include<math.h>
// Incluimos las constantes
const float a1 = 15.6;
const float a2 = 16.8;
const float a3 = 0.72;
const float a4 = 23.3;
const float a5 = 34.0;
// Funcion Energia de enlace por nucleon con correccion de apareamiento
float f(float A, int Z){
    float resultado = a1 -a2*pow(A,-1.0/3.0)-a3*Z*(Z-1)*pow(A,-4.0/3.0)-a4*pow((A-2*Z),2.0)*pow(A,-2.0);
    if(Z%2 !=0 && (int)A%2!=0){
        resultado -= a5*pow(A,-7.0/4.0);
    }
    else if(Z%2 ==0 && (int)A%2==0)
    {
        resultado += a5*pow(A,-7.0/4.0);
    }
    else{
        resultado = resultado + 0;
    }
    return resultado;
}
// Funcion Energia de enlace por nucleon sin correccion de apareamiento
float fxd(float A, int Z){
float resultado = a1 -a2*pow(A,-1.0/3.0)-a3*Z*(Z-1)*pow(A,-4.0/3.0)-a4*pow((A-2*Z),2.0)*pow(A,-2.0);
return resultado;
}

//Relacion empirica del numero de masa con el número atómico
float AAA(int Z){
    float res =1.61*pow(Z,1.1);
    return res ;
}

int main(void){
float A = 0;
int Z = 2;
int Z_max = 100;
int A_max = 250;
int i=0;
//Para A variable y Z fijo
// while (i<A_max){
// float xd =0;
// xd = f(A,Z);
// }

/*Esto es para A dependiendo de Z*/
while ( i < Z_max)
{
    float x1 = 0;
    float x2 = 0;
    x1 = fxd(AAA(Z),Z);
    x2 = f(AAA(Z),Z);
    printf("%.1f %.2f %.2f \n",AAA(Z),x1,x2);
    Z++;
    i++;
}

//Para todos los A, considerando
}