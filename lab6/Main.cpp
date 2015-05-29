#include <iostream>
#include <math.h>
using namespace std;

void gauss(double(*f)(double), double a, double b, int n);
void s(double(*f)(double), double a, double b, int n);

double f(double x)
{
	return cos(x) / (x + 1);
}

int main()
{
	int key = 0;
	double a = 0;
	double b = 3;

	while (key != 3)
	{
		cout << "\n1 - simpson \n2 - gauss\n3 - exit\n";
		cin >> key;
		switch (key)
		{
		case 1:s(&f, a, b, 10); break;
		case 2:gauss(&f, a, b, 5); break;
		}
	}
	int pause;
	cin >> pause;
	return 0;
}

void gauss(double(*f)(double), double a, double b, int n)
{
	double I = 0;
	double X[8][8] = { { 0.5, 0, 0, 0, 0, 0, 0, 0 },
	{ -0.577350, 0.577350, 0, 0, 0, 0, 0, 0 },
	{ -0.774597, 0, 0.774597, 0, 0, 0, 0, 0 },
	{ -0.861136, -0.339981, 0.339981, 0.861136, 0, 0, 0, 0 },
	{ -0.906180, -0.538470, 0, 0.538470, 0.906180, 0, 0, 0 },
	{ -0.932470, -0.661210, -0.238620, 0.238620, 0.661210, 0.932470, 0, 0 },
	{ -0.949108, -0.741531, -0.405845, 0, 0.405845, 0.741531, 0.949108, 0 },
	{ -0.960290, -0.796666, -0.525532, -0.183434, 0.183434, 0.525532, 0.796666, 0.960290 } };
	double C[8][8] = { { 2, 0, 0, 0, 0, 0, 0, 0 },
	{ 1, 1, 0, 0, 0, 0, 0, 0 },
	{ 0.555555, 0.888889, 0.555555, 0, 0, 0, 0, 0 },
	{ 0.347855, 0.652145, 0.652145, 0.347855, 0, 0, 0, 0 },
	{ 0.236927, 0.478629, 0.568889, 0.478629, 0.236927, 0, 0, 0 },
	{ 0.171324, 0.360761, 0.467914, 0.467914, 0.360761, 0.171324, 0, 0 },
	{ 0.129485, 0.279705, 0.381830, 0.417960, 0.381830, 0.279705, 0.129485, 0 },
	{ 0.101228, 0.222381, 0.313707, 0.362684, 0.362684, 0.313707, 0.222381, 0.101228 } };

	for (int i = 0; i < n; i++)
	{
		I = I + f((a + b) / 2 + ((b - a) / 2)*X[n - 1][i])*C[n - 1][i];
	}

	cout << "I = " << I*((b - a) / 2) << endl;
}

void s(double(*f)(double), double a, double b, int n)
{
	double h;
	h = (b - a) / n;
	double I, I2 = 0, I4 = 0;
	I4 = f(a + h);
	for (int k = 2; k < n; k += 2)
	{
		I4 += f(a + (k + 1)*h);
		I2 += f(a + k*h);
	}
	I = f(a) + f(b) + 4 * I4 + 2 * I2;
	I *= h / 3;
	cout << endl << "      I = " << I << endl;
}
