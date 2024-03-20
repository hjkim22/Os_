// C언어를 이용해 연결리스트를 구현하는 예제 첨부.

#include <stdio.h>
#include <stdlib.h>

// 연결 리스트의 노드를 정의.
struct Node {
    int data;
    struct Node* next;
};

// 연결 리스트에 새로운 노드를 삽입.
void insert(struct Node** head_ref, int new_data) {
    // 새로운 노드를 생성.
    struct Node* new_node = (struct Node*)malloc(sizeof(struct Node));
    new_node->data = new_data;
    new_node->next = *head_ref;
    // 헤드를 새로운 노드로 변경.
    *head_ref = new_node;
}

// 연결 리스트에서 특정 값을 삭제.
void delete(struct Node** head_ref, int key) {
    struct Node* temp = *head_ref, *prev;
    // 삭제할 값이 헤드에 있는 경우
    if (temp != NULL && temp->data == key) {
        *head_ref = temp->next;
        free(temp);
        return;
    }
    // 헤드가 아닌 경우
    while (temp != NULL && temp->data != key) {
        prev = temp;
        temp = temp->next;
    }
    // 찾지 못한 경우
    if (temp == NULL) return;
    // 찾은 경우
    prev->next = temp->next;
    free(temp);
}

// 연결 리스트에서 특정 값을 검색.
struct Node* search(struct Node* head, int key) {
    struct Node* current = head;
    while (current != NULL) {
        if (current->data == key) return current;
        current = current->next;
    }
    return NULL;
}

// 연결 리스트를 출력.
void print(struct Node* node) {
    while (node != NULL) {
        printf("%d ", node->data);
        node = node->next;
    }
    printf("\n");
}

// 메인 함수
int main() {
    struct Node* head = NULL;
    // 연결 리스트에 데이터를 삽입.
    insert(&head, 10);
    insert(&head, 20);
    insert(&head, 30);
    insert(&head, 40);
    insert(&head, 50);
    printf("연결 리스트: ");
    print(head);
    // 연결 리스트에서 데이터를 삭제.
    delete(&head, 20);
    printf("20을 삭제한 후: ");
    print(head);
    // 연결 리스트에서 데이터를 검색.
    int key = 30;
    struct Node* found = search(head, key);
    if (found != NULL) {
        printf("%d를 찾았습니다.\n", key);
    } else {
        printf("%d를 찾지 못했습니다.\n", key);
    }
    return 0;
}