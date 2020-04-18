#include <bits/stdc++.h>
using namespace std;

#define t t_i n a b
#define ar array

int t, t_i, n, a, b

void solve() {
	cin >> n >> b;
	for(int i=0; i<n; i++)
		cin >> a[i];
		cout << a << endl;
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	t_i = 1;
	cin >> t;
	while(t--) {
		// cout << "Case #" << t_i << ": ";
		solve();
		t_i++;
	}
}
