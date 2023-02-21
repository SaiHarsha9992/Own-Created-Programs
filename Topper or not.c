#include <stdio.h>
int main ( )
{
	int n , c = 0 ;
	scanf ( "%d" , &n ) ;
	char nameslist [ n ] [ 100 ] , name [ 100 ];
	for ( int i = 0 ; i < n ; i++ )
	{
		scanf ( "%s" , &nameslist [ i ] ) ;
	}
	scanf ( "%s" , name ) ;
    for ( int i = 0 ; i < n ; i++ )
    {
    	if ( nameslist [ i ] == name )
    	{
    		c = 1 ;
		}
	}
	if ( c == 1 )
	{
		printf ( "Top %d" , n ) ;
	}
	else
	{
		printf ( "Below top %d" , n ) ;
	}
}