/* versao em C++ do algoritmo de alocação de canais */

/*
 * @author: Marcello Maruqes de Oliveira
 * using adjacency Matrix to store the graph
 * list can have a better performance when the Graph is prunned
 */

#include <iostream> //cin cout
#include <cstring>  //memset
#include <utility>  //pair
#include <vector>   //vector
#include <queue>    //priority_queue
#include <bitset>   //bitset
#include <iomanip>  //setw

#define MAX_ND 100 //MAX num of Nodes
#define MAX_CH 100 //MAX num of channels

#define MANUAL 0 //MANUAL TESTS

#define fi first
#define se second

typedef std::pair<int, int> ii;

//reading num of nodes and connections,
//filling G(raph)
//return num of nodes
int readGraph(int G[][MAX_ND]) {
    int v, e;    //vertex (num of nodes) edges (num of connections)
    int a, b, pf; //edge(a,b) = edge(b,a) = (p)rob inter(f)erence

    if (MANUAL) std::cout << "Node quantity: ";       
    std::cin >> v;
    if (MANUAL) std::cout << "Connections quantity: "; 
    std::cin >> e;
    
    //fill 0 initially all have no interference
    memset(G, 0, sizeof(int) * MAX_ND * MAX_ND);

    //ideal is e = (v^2-v)/2
    for (int i = 0; i < e; i++) {
        if (MANUAL) std::cout << i << " - Conn(a, b, (p)robinter(f)): ";
        std::cin >> a >> b >> pf;
        G[a][b] = G[b][a] = pf; //(non-di)graph
    }

    return v;
}

//reading probability,
//recreating the G(raph)
void prunningGraph(int G[][MAX_ND], int v) {
    int p;
    if (MANUAL) std::cout << "Prob. Interference Limiar: "; 
    std::cin >> p;       

    for (int i = 0; i < v; i++)
        for (int j = 0; j < v; j++)
            G[i][j] = (int)(G[i][j] > p); 
}


void printGraph(int G[][MAX_ND], int v) {
    for (int i = 0; i < v; i++) {
        for (int j=  0; j < v; j++)
            std::cout << G[i][j];
        std::cout << std::endl;
    }
}

void solve(int G[][MAX_ND], int n) {
    int c; //quantity of channels
    if (MANUAL) std::cout << "Quantity Channels: "; 
    std::cin >> c;    

    int degrees[n]; //store degrees of vertex i
    bool used[n]; //mark if already calculated
    std::bitset<MAX_CH> channels[n]; //channels available 
    std::priority_queue<ii> nodes; //ii(degree, node)

    memset(degrees, 0, sizeof degrees);
    memset(used, false, sizeof used);

    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            if (G[i][j]) 
                degrees[j]++;

    for (int i = 0; i < n ; i++)
        nodes.push(ii(degrees[i], i));

    int interf[n]; //interference nodes
    int f; //quantity of interference nodes
    int u; //quantity of sub-redes on interf already calc
    int qtChannels; //quantity of channels aloc
    std::bitset<MAX_CH> channelsCheck; //check channels available

    while (!nodes.empty()) {

        ii act = nodes.top(); 
        std::cout << act.fi << " " << act.se << std::endl;
        nodes.pop();
        used[act.se] = 1;

        f = 0;
        u = 0;
        for (int i = 0; i < n; i++)
            if (G[act.se][i]) {
                interf[f++] = i;
                if (used[i]) u++;
            }

        channelsCheck.reset();
        for (int i = 0; i < f; i++)
            channelsCheck |= channels[interf[i]];

        qtChannels = (c - (int)channelsCheck.count()) / (1 + degrees[act.se] - u); 

        for (int i = 0; i < c; i++)
            if (!channelsCheck[i]) {
                channels[act.se].set(i);
                qtChannels--;
                if(!qtChannels)
                    break;
            }
    }

    //Printing answer
    for (int i = 0; i < n; i++)
    {
        std::cout << "sub-network " << i << " (" << std::setw(2) 
                  << channels[i].count() << ") channels -> ";
        for (int j = 0; j < c; j++)
            if (channels[i][j])
                std::cout << std::setw(2) << j << " ";
        std::cout << std::endl;
    } std::cout << std::endl;
}

int main() 
{
    int G[MAX_ND][MAX_ND]; //(non-di)graph

    while (1)
    {
        int n = readGraph(G); //num of nodes
        if (!n) break;
        prunningGraph(G, n);
        //printGraph(G, n);
        solve(G, n);
    }

    return 0;
}