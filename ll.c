#include <stdio.h>
#include <stdlib.h>
#define MAX_SIZE 3  
struct node 
{
int data;
struct node *link;
}
*top = NULL;
int count = 0;
void push(int element);
void pop();
void display();
void search(int element);
int main() 
{
int num, choice;
printf("\nStack using linked list\n");
printf("1.PUSH\n");
printf("2.POP\n");
printf("3.DISPLAY\n");
printf("4.SEARCH\n");
printf("5-EXIT\n");
while (1) 
{
printf("\n\nEnter the choice: ");
scanf("%d", &choice);
switch (choice) 
{
case 1:
if(count == MAX_SIZE) 
{
printf("\nStack Overflow! Cannot push more than %d elements.\n", MAX_SIZE);
break;
}
printf("\nEnter the element: ");
scanf("%d", &num);
push(num);
break;
break;
case 2:
pop();
break;
case 3:
display();
break;
case 4:
printf("Enter the element to search: ");
scanf("%d", &num);
search(num);
break;
case 5:
printf("Exiting...\n");
exit(0);
default:
printf("\nEnter valid choice!!\n");
break;
}
}
return 0;
}
void push(int element) 
{
struct node *temp;
temp = (struct node *)malloc(sizeof(struct node));
if (!temp) 
{
printf("\nMemory allocation failed. Stack Overflow!\n");
return;
}
temp->data = element;
temp->link = top;
top = temp;
count++; 
printf("%d pushed onto the stack.\n", element);
}
void pop() 
{
struct node *temp;
if (top == NULL) 
{
printf("\nError: Stack Underflow! Stack is empty, cannot pop.\n");
return;
}
temp = top;
top = top->link;
printf("Popped element is %d\n", temp->data);
free(temp);
count--;
}
void display() 
{
struct node *temp = top;
if (temp == NULL) 
{
printf("\nStack is empty!!\n");
return;
}
printf("\nStack elements are:\n");
while (temp != NULL) 
{
printf("%d ---> ", temp->data);
temp = temp->link;
}
printf("NULL\n");
}
void search(int element) 
{
struct node *temp = top;
int index = 0;
while (temp != NULL) 
{
if (temp->data == element) 
{
printf("Element %d found at index %d (from top).\n", element, index);
return;
}
temp = temp->link;
index++;
}
printf("Element %d not found in the stack.\n", element);
}
