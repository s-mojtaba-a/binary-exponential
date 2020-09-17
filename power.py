def power(x,y,n):
    ans=1
    while y>0 :
        if y&1==1 :
            ans=ans*x%n
        x=x*x%n
        y>>=1
    return(ans)


def power(x,y):
    ans=1
    while y>0 :
        if y%2==1 :
            ans*=x
        x*=x
        y>>=1
    return(ans)


// c++ impelemenation

#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

ll power(ll x,ll y , ll n){
    ll ans=1 ;
    while (y>0){
        if (y&1==1){
            ans=ans*x%n ;
        }
        x=x*x%n ;
        y>>=1 ;
    }
    return(ans);
}
