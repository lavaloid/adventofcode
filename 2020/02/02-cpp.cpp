#include <iostream>
#include <fstream>

using namespace std;
int main() {
    ifstream f;
    f.open("input.txt",ifstream::in);
    int result = 0;
    
    while (f.peek() != EOF) {
        int min = 0;
        char last = '\0';
        while (true) {
            f.get(last);
            if (last == '-') break;
            min *= 10;
            min += last - '0';
        }
        
        int max = 0;
        while (true) {
            f.get(last);
            if (last == ' ') break;
            max *= 10;
            max += last - '0';
        }
        
        char find; f.get(find); f.get(); f.get();
        
        int count = 0;
        while (true) {
            f.get(last);
            if (last == '\n') break;
            if (last == find) count++;
        }
        
        if (count >= min && count <= max) result++;
    }
    cout << result << endl;
    f.close();
}
