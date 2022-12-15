/* To run:
        make 07-cpp
        ./07-cpp
   Make sure input.txt is in the same folder. */
#include <iostream>
#include <fstream>

using namespace std;
struct linked_list_int {
    int n;
    linked_list* next;
};

struct tree {
    tree* children = NULL;
    int amount = 0;
    tree* next = NULL;
};

int num_contained_by (tree* node) {
    int n = 0;
    tree* check = node->children;
    while (check->next != NULL) {
        n += check->amount;
        n += num_contained_by(check->node) * check->amount;
        check = check->next;
    }
    return n;
}

int main() {
    ifstream f;
    f.open("input.txt",ifstream::in);
    int cols = 0;
    char* temp;
    while (getline(f, temp))
        ++cols;

    cout << num_contained_by(shiny_gold) << endl;
    return 0;
}
