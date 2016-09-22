#include <stdlib.h>
#include <iostream>
using namespace std;

void main(){

struct Coordinate       //Структура являющаяся звеном списка
{
    double x;     //Значение x будет передаваться в список
    double y;
    Coordinate *next;
    Coordinate *prev; //Указатели на адреса следующего и предыдущего элементов списка
};


struct List   //Создаем тип данных Список
{
    Coordinate *head;
    Coordinate *tail;  //Указатели на адреса начала списка и его конца
};


void add_dot( List *list, int x, int y )
{
        Coordinate *temp = new Coordinate(); // Выделение памяти под новый элемент структуры
        temp->next = NULL;       // Указываем, что изначально по следующему адресу пусто
        temp->x = x;
        temp->y = y;             // Записываем значение в структуру

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

void print_dot( List * list )
{
        Coordinate * temp = list->head;  // Временно указываем на адрес первого элемента
        while( temp != NULL )      // Пока не встретим пустое значение
        {
                cout <<"x:"<<temp->x<<"y:"<<temp->y<<" ";//Выводим значение на экран
                temp = temp->next;     //Смена адреса на адрес следующего элемента
        }
        cout<<"\n";
}
int main()
{
  cout<<"Enter 20 pairs of coordinates"<<"\h";
  List List1;
  for (int i = 0; i<20; i++)
  {
      int x;
      int y;
      cin >> x>>y;
      add_dot(&List1,x,y);
  }

}