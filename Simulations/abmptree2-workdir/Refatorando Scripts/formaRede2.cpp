#include <bits/stdc++.h>

using namespace std;

typedef pair<double, int> ii;

double dist(double x1, double y1, double x2, double y2) {
    return sqrt(pow(x1-x2,2) + pow(y1-y2,2));
}

int main()
{
    string s;
    vector<ii>v[4];
    double x[53];
    double y[53];
    double z[53];
    int usado[53];
    int cont = 0;
    int clusterID[53];

    while (1) {
        getline(cin, s);
        if (s == "*") break;
        int f = s.find('=') + 2;
        if(cont%3==0) x[cont/3] = stod(s.substr(f));
        if(cont%3==1) y[cont/3] = stod(s.substr(f));
        if(cont%3==2) z[cont/3] = stod(s.substr(f));
        cont++;
    }



    for (int j = 1; j < 5; j++)
        for (int i = 5; i < 53; i++)
            v[j-1].push_back(ii(dist(x[i], y[i], x[j], y[j]), i));

    for (int i = 0; i < 4; i++) 
        sort(v[i].begin(), v[i].end());

    memset(usado, 0, sizeof usado);
    int contadores[4] = {0, 0, 0, 0};
    int c = 0;
    while (1) {
        for (int i = 0; i < 4; i++) {
            while (usado[v[i][contadores[i]].second] == 1) contadores[i]++;
            clusterID[v[i][contadores[i]].second] = i;
            usado[v[i][contadores[i]].second] = 1;
            c++;
        }
        if (c == 48) break;
    }

    cout << "-1 0 0 0 0";
    for (int i = 5; i < 53; i++)
        cout << " " << clusterID[i] + 1;
    cout << endl;

    return 0;
}