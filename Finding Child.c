#include <stdio.h>
int findchild ( int *a , int k , int n )
{
	int index , c = 1 ;
	for ( int i = 0 ; i < n ; i++ )
	{
		if ( a [ i ] == k )
		{
			index = i ;
			c++ ;
		}
	}
	if ( c == 1 )
	{
		return -1 ;
	}
	else
	{
		return index ;
	}
}
int main ( )
{
	int n ;
	scanf ( "%d" , &n ) ;
	int a [ n ] , k , *p ;
	for ( int i = 0 ; i < n ; i++ )
	{
		scanf ( "%d" , &a [ i ] ) ;
	}
	scanf ( "%d" , &k ) ;
	p = &k ;
	int x = findchild ( a , *p , n ) ;
	printf ( "%d" , x ) ;
}