#include <math.h>
#include <iostream>

using namespace std;

struct Node       //Структура являющаяся звеном списка
{
    int x;//Значение x будет передаваться в список
    int y;
    Node *next = NULL, *prev = NULL; //Указатели на адреса следующего и предыдущего элементов списка
};


struct List   //Создаем тип данных Список
{
    Node *head = NULL;
    Node *tail = NULL;  //Указатели на адреса начала списка и его конца
};


void add( List *list, int x , int y)
{
    Node *temp = new Node(); // Выделение памяти под новый элемент структуры
    temp->next = NULL;       // Указываем, что изначально по следующему адресу пусто
    temp->x = x;             // Записываем значение в структуру
    temp->y = y;

    if ( list->head != NULL ) // Если список не пуст
    {
        temp->prev = list->tail; // Указываем адрес на предыдущий элемент в соотв. поле
        list->tail->next = temp; // Указываем адрес следующего за хвостом элемента
        list->tail = temp;       //Меняем адрес хвоста
    }
    else //Если список пустой
    {
        temp->prev = NULL; // Предыдущий элемент указывает в пустоту
        list->head = list->tail = temp;    // Голова=Хвост=тот элемент, что сейчас добавили
    }
}

void print( List * list )
{
    Node * temp = list->head;  // Временно указываем на адрес первого элемента
    while( temp != NULL )      // Пока не встретим пустое значение
    {
        cout << temp->x <<" " << temp->y << endl; //Выводим значение на экран
        temp = temp->next;     //Смена адреса на адрес следующего элемента
    }
    cout<<"\n";
}

void findFirst (List *list, int check_x, int check_y){
    Node * temp = list->head;
    int i = 1;
    while (temp != NULL){
        if ((temp->x == check_x) && (temp->y == check_y)) {
            cout << "It's on the " << i << " place from the begin" << endl;
            break;
        }
        temp = temp->next;
        i++;
    }
    if (temp == NULL)
        cout << "No such element"<<endl;

}

void findLast (List *list, int check_x, int check_y) {
    Node * temp = list->tail;
    int i = 1;
    while (temp != NULL){
        if ((temp->x == check_x) && (temp->y == check_y)) {
            cout << "It's on the " << i << " place from the end" << endl;
            break;
        }
        temp = temp->prev;
        i++;
    }
    if (temp == NULL)
        cout << "No such element"<<endl;
}

void addIn (List *list, int index, int X, int Y){
    Node * temp = list->head;
    for(int i = 1; i < index - 1; i++){
        temp = temp->next; //Доберемся до index-го элемента списка
    }
    Node * newElem = new Node; //Выделяем память для новго элемента
    newElem->x = X;
    newElem->y = Y;
    // Сначала указатели нового элемента направим на temp и на temp->next,
    // далее их указатели непосредственно на новый элемент

    newElem->prev=temp;
    newElem->next=temp->next;
    temp->next=newElem;
    newElem->next->prev=newElem;
}

void deleteFrom(List *list, int index){//Убираем либо голову, либо хвост, либо элемент посередине.
    //Отвязываем элемент от прочих элементов списка и удаляем его, чтобы не допустить утечку памяти
    Node *temp = list->head;
    if (index == 1) {
        temp->next->prev = NULL;
        list->head = temp->next;
        delete temp;
    }
    else{
        for (int i = 1; i < index; i++)
            temp = temp->next;
        if (temp->next == NULL){
            temp->prev->next = NULL;
            list->tail = temp->prev;
            delete temp;
        }
        else{
            temp->prev->next = temp->next;
            temp->next->prev = temp->prev;
            delete temp;
        }
    }
}

bool evenElementX(int x){
    if (x % 2 == 0)
        return true;
    else
        return false;
}

List *criterion( List * list , bool (*func)(int))
{
    Node * temp = list->head;// Временно указываем на адрес первого элемента
    List * newList = new List;

    while( temp != NULL )      // Пока не встретим пустое значение
    {
        if (func(temp->x)){
            add(newList, temp->x, temp->y);
        }
        temp = temp->next;     //Смена адреса на адрес следующего элемента
    }
    return newList;
}

double distance(Node *first, Node *second){
    return sqrt((first->x - second->x) * (first->x - second->x) + (first->y - second->y) * (first->y - second->y));
}

struct Rast{
    Node *node;
    double dist;
};

bool my_less(Node *first, Node *second, Node *center){
    return distance(first, center) < distance(second, center);
}

Node *cmass(List *list){
    Node * temp = list->head;
    Node *center = new Node();
    center->x = center->y = 0;
    int count = 0;
    while (temp!=NULL){
        center->x += temp->x;
        center->y += temp->y;
        count++;
        temp = temp->next;
    }
    center->x = center->x/count;
    center->y = center->y/count; //получили координаты центра масс
    return center;
}

List *task7(List *list){
    Node *center = cmass(list);
    cout << "center " << center->x << " " << center->y << endl;
    Node *h[6];
    int nh = 0;
    Node *temp = list->head;
    while (temp != NULL){
        h[nh] = temp;
        for (int i = nh; i - 1 >= 0 && my_less(h[i], h[i - 1], center); i--){
            std::swap(h[i], h[i - 1]);
        };
        if (nh < 5) nh++;
        temp = temp->next;
    }
//    printf("nh %d\n", nh);
    List *newList = new List;
    for (int i = 0; i < 5 && i < nh; i++){
        add(newList, h[i]->x, h[i]->y);
    }
    return newList;
//    std::vector<Rast*> heap(h, h+6);
//    std::make_heap(heap.begin(), heap.end(), comp);
}



int main(void){
    //in Java: public static void main(String args[])
    List *list = new List;
    for (int i = 0; i < 6; i++) {
        int x = rand()%1000;
        int y = rand()%1000;
        add(list, x, y);
    }
    List *new_list = criterion(list, evenElementX);
    print(list);
//    print(new_list);
//    popIn(new_list,0);
//    addIn(new_list,1,9,1997);
//    print(new_list);
    addIn(list,2,9,1997);
    print(list);
    List *closest = task7(list);
    //itworksdeleteFrom(list,2);
    print(closest);
    return 0;
}
