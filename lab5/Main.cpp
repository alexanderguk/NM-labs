#include <iostream>
#include "math.h"
#include "conio.h" 
#include <fstream>
#define N 5                       
#define h 0.25                   

using namespace std;

double* u;                        
double* y;                        

struct CubicSpline				
{
	double a, b, c, d, x;       
} *cspline;

double func(double x)
{
	if (x < 0)
		return sin(x) - pow(-x * 2, 1.0 / 3.0);
	else
		return sin(x) + pow(x * 2, 1.0/3.0);
}

void output(double* matrix, int rows)
{
	for (int i = 0; i < rows; i++)
	{
		printf("%3.5f ", matrix[i]);
		cout << endl;
	}
}

double Lagrange(double x0)
{
	ofstream out("output.txt");
	double c = 1;               
	double s = 0;                
	for (int i = 0; i < N; i++)
	{
		c = 1;
		for (int j = 0; j < N; j++)
		{
			if (i != j)
			{
				c *= (x0 - u[j]) / (u[i] - u[j]);
				out << (1.0 / (u[i] - u[j]));
				out << " " << (-u[j] / (u[i] - u[j])) << endl;
				//x1 = 1.0 / 
			}
		}
		out << endl << y[i] << endl;
		s += y[i] * c;

	}
	return s;
}

void spline(double* x, double* y)
{
	cspline = new CubicSpline[N];
	
	for (int i = 0; i < N; i++)
	{
		cspline[i].x = x[i];
		cspline[i].a = y[i];
	}
	
	cspline[0].c = cspline[N - 1].c = 0;
	
	double *alpha = new double[N - 1];
	double *beta = new double[N - 1];
	
	for (int i = 1; i<N - 1; i++)
	{
		double h_i = x[i] - x[i - 1];
		double h_i1 = x[i + 1] - x[i];
		double A = h_i;
		double C = 2 * (h_i + h_i1);
		double B = h_i1;
		double F = 6 * ((y[i + 1] - y[i]) / h_i1 - (y[i] - y[i - 1]) / h_i);
		double z = (A * alpha[i - 1] + C);
		alpha[i] = -B / z;
		beta[i] = (F - A * beta[i - 1]) / z;
	}
	
	for (int i = N - 2; i > 0; i--)
		cspline[i].c = alpha[i] * cspline[i + 1].c + beta[i];
	
	for (int i = N - 1; i > 0; i--)
	{
		double h_i = x[i] - x[i - 1];
		cspline[i].d = (cspline[i].c - cspline[i - 1].c) / h_i;
		cspline[i].b = h_i*(2 * cspline[i].c + cspline[i - 1].c) / 6 + (y[i] - y[i - 1]) / h_i;
	}
}

double coef(double x)
{
	CubicSpline *s;
	if (x <= cspline[0].x)             
	{
		s = cspline + 1;
	}
	else if (x >= cspline[N - 1].x) 
	{
		s = cspline + N - 1;
	}
	else                      
	{
		size_t i = 0, j = N - 1;
		while (i + 1 < j)
		{
			size_t k = i + (j - i) / 2;
			if (x <= cspline[k].x) j = k;
			else i = k;
		}
		s = cspline + j;
	}
	double dx = (x - s->x);
	cout << endl;
	
	printf("%5.2f  ", x);
	printf("%10.6f ", s->a);
	printf("%11.6f ", s->b);
	printf("%11.6f ", s->c);
	printf("%11.6f", s->d);

	ofstream out("output.txt", ios_base::app);
	
	out << x << " " << s->a + (s->b + (s->c / 2 + s->d * dx / 6) * dx) * dx << endl;
	return s->a + (s->b + (s->c / 2 + s->d * dx / 6) * dx) * dx;
}

void interp()
{
	spline(u, y);						
	printf("\n   x         a           b           c           d        Error");
	for (double l = u[0]; l <= u[N - 1]; l += h)
	{
		double s = coef(l);
		printf("%11.5f", s - func(l));       
	}
	getchar();
}
void main()
{
	u = new double[N];      
	u[0] = -1; u[1] = 1; u[2] = 3; u[3] = 5; u[4] = 7;
	y = new double[N];      
	
	for (int i = 0; i < N; i++)
	{
		y[i] = func(u[i]);   
	}
	
	cout << "Interpolation points:" << endl;
	output(u, N);
	cout << endl;
	
	cout << "Values of the function:" << endl;
	output(y, N);
	cout << endl;
	//double p = -6;
	for (int i = -1; i <= 7; i = i + 2)
	{
		cout << "Value of Lagrange`s polinom at point " << i << ": " << Lagrange(i);
	}
	
	interp();
	getchar();
}
