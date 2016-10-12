#include <iostream>
#include <cstring>
using namespace std;

struct Node
{
    Node *next;
    char *key;
    char *value;
};



Node *hashTable[32];

unsigned int my_hash(char *str)
{
    unsigned  int hash_value =  0;
    unsigned  char *p;
    for (p = (unsigned char *) str; *p != '\0'; p++)
        hash_value = 77 * hash_value + *p;
    return hash_value % 78;
}

Node *insert_node(char *key, char *value)
{
    int hash_value = 0;
    Node *new_node;
    hash_value = my_hash(key);
    new_node = new Node;
    new_node ->key = key;
    new_node ->value = value;
    new_node->next = hashTable[hash_value];
    hashTable[hash_value] = new_node;
    return new_node;
}

void print_node(char *key)
{
    cout << "{key, value} = {" << hashTable[my_hash(key)]->key << ", " << hashTable[my_hash(key)]->value << "}" << endl;
}

bool find_node(char *key)
{
    Node *new_node;
    for (new_node = hashTable[ my_hash(key)]; ! new_node; new_node = new_node->next )
        if (! strcmp(key, new_node->key))
            return true;
}


int main ()
{

    insert_node("first", "8 800 555 35 35");
    insert_node("second", "8 800 555 35 36");
    insert_node("third", "8 800 555 35 37");
    insert_node("fourth", "8 800 555 35 38");
    insert_node("fifth", "8 800 555 35 39");
    insert_node("sixth", "8 800 555 35");
    insert_node("seventh", "8 800 555");


    print_node("first");
    print_node("second");
    print_node("third");
    print_node("fourth");
    print_node("fifth");
    print_node("sixth");
    print_node("seventh");

    if (find_node("first"))
        cout << "first element is in the table" << endl;

    return 0;

}