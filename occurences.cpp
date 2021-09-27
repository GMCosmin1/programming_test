#include<vector>
#include<algorithm>
#include<iostream>
#include<stdio.h>

using namespace std;

int max_occurences(vector<int> v) {
    // occurences 1(un numar apare de cel putin o data)
    int occurences = 1, max = 0, max_occurences = 0;
    int current = 0;

    // sortam vectorul, complexitate O(n * log(n))
    std::sort(v.begin(), v.end());

    // print vector sortat
    for (auto i : v)
        cout << i << " ";
    cout << endl;

    // numarul maxim care apare de cele mai multe ori este primul element
    // la fel si numarul curent, cu care testam
    max = v[0];
    current = v[0];

    // incepem de la al 2-lea element(ca sa nu avem o aparitie in plus)
    for (int i = 1; i < v.size(); i++) {
        
        // daca elementul curent este egal cu numarul din sir pe care il testam
        // ex: daca am avut un 1 inainte, pe poz. v[i - 1]
        // vreau sa testez ca elementul curent are aceeasi valoare ca precedentul
        if (v[i] == current) {
            occurences++;
        // daca nu are aceeasi valoare, verific daca are cel mai mare numar de aparitii
        // fiind un vector sortat, intotdeauna cand o sa se modifice numarul maxim de aparitii
        // o sa se modifice si cel mai mare numar(max)
        } else {
            if (occurences >= max_occurences) {
                max_occurences = occurences;
                max = v[i - 1];
            }
            // trecem la urmatorul numar
            current = v[i];
            occurences = 1;
        }
    }
    return max;
}

        // int-ul a fost folosit doar pentru a verifica ca algoritmul functioneaza
        // l-am lasat in caz ca se doreste testarea acestuia
int main() {


    vector<int> nums = {4, 4, 4, 1, 3, 0, 1, 0, 6, 2, 3, 4, 3, 6, 5, 6, 4, 5, 2, 1, 3, 9, 4, 3, 2, 1, 5, 8, 6, 5, 3, 1, 8, 4, 3, 1, 3, 4, 8, 5, 200};

    cout << max_occurences(nums);
    printf("\n");
    return 0;
}
