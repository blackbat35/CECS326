#include<iostream>
#include<stdlib.h>

using namespace std;

void RandomGraphs(int n_edge, int n_vertex);

int main()
{
	int e, v;
	cout << "Random graph generation: \n";
	cout << "The order(v): ";   cin >> v;
	int max = v * (v - 1) / 2;
	cout << "\nThe size(e) : "; cin >> e;
	while (e > max) {
		cout << "\nThe size (e < " << max << "): ";
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
	for (int i = 0; i < n_edge; ++i) {
		edge[i] = new int[2];
	}

	do
	{
		edge[i][0] = rand() % n_vertex + 1;
		edge[i][1] = rand() % n_vertex + 1;

		if (edge[i][0] == edge[i][1])
			continue;
		else
		{
			for (j = 0; j < i; j++)
			{
				if ((edge[i][0] == edge[j][0] && edge[i][1] == edge[j][1])
					|| (edge[i][0] == edge[j][1] && edge[i][1] == edge[j][0]))
					i--;
			}
		}
		i++;
	} while (i < n_edge);

	// Print the graph.
	int count = 0;
	cout << "\nThe random directed graph: ";
	for (i = 0; i < n_vertex; i++)
	{
		cout << "\n" << i + 1 << "->: ";
		for (j = 0; j < n_edge; j++)
		{
			if (edge[j][0] == i + 1)
			{
				cout << edge[j][1] << "   ";
				count++;
			}
			else if (edge[j][1] == i + 1)
			{
				cout << edge[j][0] << "   ";
				count++;
			}
			else if (j == n_edge - 1 && count == 0)
				cout << "Isolated Vertex!";
		}
		cout << " \n";
	}
	for (int i = 0; i < n_edge; ++i) {
		delete[] edge[i];
	}
	delete[] edge;
}

