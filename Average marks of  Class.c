#include <stdio.h>
void average ( int n , int s )
{
	float avg ;
	avg = ( float ) s / n ;
	printf ( "%0.2f" , avg ) ;
}
int main ( )
{	
	int n , array , s = 0 ;;
	scanf ( "%d" , &n ) ;
	int a [ n ] ;
	int *p = a ;
	for ( int i = 0 ; i < n ; i++ )
	{
		scanf ( "%d" , p + i ) ;
		s = s + *( p + i ) ;
	}
	average ( n , s ) ;
}
	           
	    		     
	                    		     