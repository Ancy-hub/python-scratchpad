struct node{
    int data;
    struct node * next;
};

struct node *head = NULL;

p=head;
while (p!=NULL){
    printf("%d ",p->data);
    p=p->next;
}




