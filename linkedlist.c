#include <stdio.h>
#include <stdlib.h>
struct student
{
    int n;
};
struct node
{
    struct student s;
    struct node *next;
}*head,*prev;
struct node * getnode();
struct node * getnode()
{
    struct node *p;
    p=malloc(sizeof(struct node));
    printf("enter the data\n");
    scanf("%d",&p->s.n);
    p->next=NULL;
    return p;
};
void insertbeg()
{
    struct node *p;
    p=getnode();
    if(head==NULL)
    {
        head=p;
        prev=p;
    }
    else
    {
        p->next=head;
        head=p;
    }
}
void insertend()
{
    struct node *p;
    p=getnode();
    if(head==NULL)
    {
        head=p;
        prev=p;
    }
    else
    {
        prev->next=p;
        prev=p;
    }
}
void insertbtwn()
{
    struct node *p,*temp;
    temp=head;
    int key;
    printf("enter the element after which you want to insert the element\n");
    scanf("%d",&key);
    if(head==NULL)
    {
        insertbeg();
    }
    if(head->next==NULL)
    {
        insertend();
    }
    else
    {
        while(temp->s.n!=key)
        {
            temp=temp->next;
        }
        p=getnode();
        p->next=temp->next;
        temp->next=p;
    }
}
void deletebeg()
{
    if(head==NULL)
    {
        printf("linked list already empty\n");
    }
    else if(head->next==NULL)
    {
        head=NULL;
        prev=NULL;
    }
    else
    {
        head=head->next;
    }
}
void deleteend()
{
    struct node *temp;
    temp=head;
    if(head==NULL)
    {
        printf("linked list already empty\n");
    }
    else if(head==prev)
    {
        head=NULL;
        prev=NULL;
    }
    else
    {
        while(temp->next->next!=NULL)
        {
            temp=temp->next;
        }
        temp->next=NULL;
        prev=temp;
    }
}
void deletebtwn()
{
    struct node *temp,*r;
    temp=head;
    if(head==NULL)
    {
        printf("linked list already empty\n");
    }
    int key;
        printf("enter the element to be deleted\n");
        scanf("%d",&key);
     if(head->s.n==key)
    {
        deletebeg();
    }
    else if(prev->s.n==key)
    {
        deleteend();
    }
    else
    {
        while(temp->next->next->s.n!=key)
        {
            temp=temp->next;
        }
        r=temp->next->next;
        temp->next=r->next;
    }
}
void display()
{
    struct node *temp;
    temp=head;
    while(temp->next!=NULL)
    {
        printf("%d\n",temp->s.n);
        temp=temp->next;
    }
    printf("%d\n",temp->s.n);
}
int main()
{
    head=NULL;
    prev=NULL;
    int choice;
    for(;;)
    {
	printf("1.INSERT ELEMENT IN THE BEGINNING\n2.INSERT ELEMENT IN THE END\n3.INSERT ELEMENT IN BETWEEN\n4.DELETE ELEMENT AT THE BEGINNING\n5.DELET ELEMENT AT THE END\n6.DELETE ELEMENT IN BETWEEN\n7.DISPLAY LINKED LIST\n");
        printf("enter the choice\n");
        scanf("%d",&choice);
        switch(choice)
        {
            case 1:insertbeg();
            break;
            case 2:insertend();
            break;
            case 3:insertbtwn();
            break;
            case 4:deletebeg();
            break;
            case 5:deleteend();
            break;
            case 7:display();
            break;
            case 6:deletebtwn();
            break;
            default:
	    {
		printf("Invalid choice\n");
		exit(0);
	    }
        }
    }
}
