#include<iostream>

using namespace std;

void RandomGraphs(int n_edge, int n_vertex);

int main()
{
	int e, v;
	cout << "Random graph generation: ";
	cout << "\nThe number of vertex: ";cin >> v;
	int max = v * (v - 1) / 2;
	cout << "\nThe number of edges:  ";
	cin >> e;
	while (e > max) {
		cout << "\nThe number of edges:  ";
		cin >> e;
	}
	RandomGraphs(e, v);
	system("pause");
}

void RandomGraphs(int n_edge, int n_vertex)
{
	int i = 0;
	int j = 0;
	int** edge = new int* [n_edge];
	for (int i = 0; i < n_edge; ++i)
		edge[i] = new int[2];
	do
	{	
		edge[i][0] = rand() % n_vertex + 1;
		edge[i][1] = rand() % n_vertex + 1;
		if (edge[i][0] == edge[i][1])
			continue;
		for (j = 0; j < i; j++)
		{
			if ((edge[i][0] == edge[j][0] && edge[i][1] == edge[j][1])
				|| (edge[i][0] == edge[j][1] && edge[i][1] == edge[j][0]))
				i--;
		}
		i++;
	} while (i < n_edge);

	// Print the graph.
	cout << "\nThe random directed graph: ";
	for (i = 0; i < n_vertex; i++)
	{
		cout << "\n" << i + 1 << " ->: ";
		for (j = 0; j < n_edge; j++)
		{
			if (edge[j][0] == i + 1)
				cout << edge[j][1] << "   ";
			else if (edge[j][1] == i + 1)
				cout << edge[j][0] << "   ";
		}
		cout << " \n";
	}
	for (int i = 0; i < n_edge; ++i)
		delete[] edge[i];
	delete[] edge;
}
