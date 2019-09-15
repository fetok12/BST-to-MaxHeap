#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include <malloc.h>
#define TRUE 1


//KATEGORI DUGUMU


struct node{
    char kategori_ismi[40];
    int alt_kategori_sayisi;
    int kullanici_sayisi;
    int rezervasyon_sayisi;
    int kategori_yolu;
    int derinlik;
    struct node *child;
    struct node *sibling;
};


struct node* start = NULL;
struct node* temp;
struct node* cat;

struct node* createNode()
{
    struct node* newNode = (struct node*)malloc(sizeof(struct node));
    return newNode;

}

void createRootNode( char *a,int b, int c, int d, int e, int f)
{
    struct node* Root = (struct node*)malloc(sizeof(struct node));
        strcpy(Root->kategori_ismi,a);
        Root->alt_kategori_sayisi=b;
        Root->kullanici_sayisi=c;
        Root->rezervasyon_sayisi=d;
        Root->kategori_yolu=e;
        Root->derinlik =f;

        start = Root;
        start->child = NULL;
        start->sibling = NULL;
}
struct node* createCategoryNode( char *a,int b, int c, int d, int e, int f)
{
    struct node* Category = (struct node*)malloc(sizeof(struct node));
        strcpy(Category->kategori_ismi,a);
        Category->alt_kategori_sayisi=b;
        Category->kullanici_sayisi=c;
        Category->rezervasyon_sayisi=d;
        Category->kategori_yolu=e;
        Category->derinlik=f;

        Category->child = NULL;
        Category->sibling = NULL;
        return Category;
}

void addChild(struct node *kategori, struct node *eklenecek_kategori,char *a, int b, int c, int d, int e, int f)
{
        eklenecek_kategori=createCategoryNode(a,b,c,d,e,f);


        if(kategori->child != NULL){
            temp = kategori->child;
            while( temp->sibling != NULL)
            {
                temp= temp->sibling;
          }
             temp->sibling = eklenecek_kategori;
             printf("%s\n", temp->sibling->kategori_ismi);

        }


        if(kategori->child == NULL){
            kategori->child = eklenecek_kategori;
            printf("%s\n", kategori->child->kategori_ismi);

        }
}




// KULLANICI DUGUMU
struct userNode {
    char kullanici_id[50];
    char kategori_ismi[50];
    int rezervasyon_sayisi;
    struct userNode *left, *right;
    struct userNode *next;
};

 int i =0;
 int counter =0;
 int arr[1000];
 char as[100][100];
 char sa[100][100];

struct userNode* getNode(char *a, char *b, int data)
{ printf(" GIRILEN KULLANICI: %s REZERVASYON SAYISI: %d\n", a,data);
    struct userNode* newNode = (struct userNode *)malloc(sizeof(struct userNode));
    strcpy(newNode->kullanici_id,a);
    strcpy(newNode->kategori_ismi,b);
    newNode->rezervasyon_sayisi = data;
    newNode->left = newNode->right = NULL;
    newNode->next=NULL;
    return newNode;
}


struct userNode* insert(struct userNode* node, char *a, char *b,int key)
{
    if (node == NULL) return getNode(a,b,key);

    if (key < node->rezervasyon_sayisi)
        node->left  = insert(node->left,a,b, key);
    else if (key > node->rezervasyon_sayisi)
        node->right = insert(node->right,a,b, key);

    return node;
}


void postorderTraversal(struct userNode*);


void inorderTraversal(struct userNode* root, int arr[])
{
    if (root == NULL)
        return;

    inorderTraversal(root->left, arr);

        arr[++i] = root->rezervasyon_sayisi;
        strcpy(as[++i], root->kullanici_id);
        strcpy(sa[++i], root->kategori_ismi);
        counter++;

    inorderTraversal(root->right, arr);
}

void BSTToMaxHeap(struct userNode* root, int arr[], int *i)
{
    if (root == NULL)
        return;

    BSTToMaxHeap(root->left, arr, i);

    BSTToMaxHeap(root->right, arr, i);

        root->rezervasyon_sayisi = arr[++*i];
        strcpy(root->kullanici_id,as[++*i]);
        strcpy(root->kategori_ismi,sa[++*i]);

}

void maxHeapify(struct userNode* root)
{

    int i = 0;

    inorderTraversal(root, arr);

  BSTToMaxHeap(root, arr, &i);
}


void postorderTraversal(struct userNode* root)
{
    if (!root)
        return;

    postorderTraversal(root->left);

    postorderTraversal(root->right);
     printf("Kullanici Id:%s Rezervasyon Sayisi:%d\n", root->kullanici_id,root->rezervasyon_sayisi);

}

struct rezNode {
    char yer_adi[70];
    char rezervasyon_zamani[60];
    char enlem[60];
    char boylam[60];
    char sehir[70];
    struct rezNode *next;


    };


// rezervasyon dugumu

struct rezNode* first = NULL;


struct rezNode* dugumOlustur(char *a, char *b, char *c, char *d, char *e)
{
    struct rezNode* yeniDugum = (struct rezNode*)malloc(sizeof(struct rezNode));
    strcpy(yeniDugum->yer_adi,a);
    strcpy(yeniDugum->rezervasyon_zamani,b);
    strcpy(yeniDugum->enlem,c);
    strcpy(yeniDugum->boylam,d);
    strcpy(yeniDugum->sehir,e);
    yeniDugum->next = NULL;


    return yeniDugum;
}

void sonaEkle(char *a, char *b, char *c, char *d, char *e)
{
    struct rezNode* sonaEklenecek = dugumOlustur(a,b,c,d,e);
    if (first == NULL)
    {
        first = sonaEklenecek;
    }

    else
    {
        struct rezNode* temp = first;

        while (temp->next != NULL)
        {
            temp = temp->next;
        }

        temp->next = sonaEklenecek;
    }
}

//////////// VERI CEKME ISLEMLERI

int getWords(char *base, char target[10][200])
{
	int n=0,i,j=0;
	for(i=0;TRUE;i++)
	{
		if(base[i]!=','){
			target[n][j++]=base[i];
		}
		else{
			target[n][j++]='\0';//insert NULL
			n++;
			j=0;
		}
		if(base[i]=='\0')
		    break;
	}
	return n;

}
int getWords2(char *base, char target[10][200])
{
	int n=0,i,j=0;
	for(i=0;TRUE;i++)
	{
		if(base[i]!=':'){
			target[n][j++]=base[i];
		}
		else{
			target[n][j++]='\0';//insert NULL
			n++;
			j=0;
		}
		if(base[i]=='\0')
		    break;
	}
	return n;

}
char kategori_veri[10000][400];
char ana_kategoriler[400][200];
char ana_kategoriler_unique[100][200]; //bunun iicinde 12 tane ana kategori var
char kategoriler[400][200]; // WORDS ICINDE KULLANICI ARAT
char veriler[100][400];




int main()
{
    while(1==1){
            int secim;
printf("\nSecim yapiniz:\n");
printf("1.Rezervasyon.txt den kayitlari alip ilgili dugumlere at dugumlere at\n");
printf("2.Kullanici Binary Tree Max Heapify Yap\n");
printf("3. Kullanici Ekle\n");
printf("4.Kategori Ekle\n");
printf("5.Kategoriye gore kullanici listele\n");
printf("6.MAX HEAP SORT\n");
scanf("%d", &secim);

if(secim == 1){

    int na;
	int ia;

    int satir = 10000;
    int max_sayir_sayisi = 10000;

    char **words = (char **)malloc(sizeof(char*)*satir);
    if (words==NULL)
        {
        exit(1);
        }

    FILE *fp = fopen("rezervasyon.txt", "r");
    if (fp == NULL)
        {
        fprintf(stderr,"Dosya acilmadi.\n");
        exit(2);
        }

    int i;
    for (i=0;1;i++)
        {
        int j;

        if (i >= satir)
            {
            int new_size;
            new_size = satir*2;
            words = (char **)realloc(words,sizeof(char*)*new_size);
            if (words==NULL)
                {
                exit(3);
                }
            satir = new_size;
            }

        words[i] = malloc(max_sayir_sayisi);
        if (words[i]==NULL)
            {
            exit(4);
            }
        if (fgets(words[i],max_sayir_sayisi-1,fp)==NULL)
            break;

        for (j=strlen(words[i])-1;j>=0 && (words[i][j]=='\n' || words[i][j]=='\r');j--)
            ;
        words[i][j+1]='\0';
        }
    fclose(fp);



    int j;
    int sayac =0;
   for(j = 1; j < 21; j++)
        {
            strcpy(veriler[sayac],words[j]);
            sayac++;
        }
   for(j = 400; j < 420; j++)
        {
            strcpy(veriler[sayac],words[j]);
            sayac++;
        }
  for(j = 800; j < 820; j++)
        {
            strcpy(veriler[sayac],words[j]);
            sayac++;
        }
  for(j = 1050; j < 1070; j++)
        {
            strcpy(veriler[sayac],words[j]);
            sayac++;
        }
   for(j = 1500; j < 1520; j++)
        {
            strcpy(veriler[sayac],words[j]);
            sayac++;
        }
    printf("-----------------------------------------------------------\n");
printf("REZERVASYON TXT DEN CEKILEN KAYITLAR:\n\n");
printf("-----------------------------------------------------------\n");
    for(j=0; j<sayac; j++){
        printf("%s\n", veriler[j]);
    }
    printf("\n\n");


    int toplam_veri=i;

	char arr[10][200];

    for(j=0; j<sayac; j++){

    na = getWords(veriler[j],arr);

            strcpy(kategori_veri[j],arr[na]);

    }


   int counter = 0;
  for (i=0; i<sayac; i++)
    {

        int j;
        for (j=0; j<i; j++)
           if (strcmp(kategori_veri[i],kategori_veri[j]) == 0)
               break;

        if (i == j){
                strcpy(kategoriler[counter], kategori_veri[i]);
        counter++;

        }
    }


    printf("\n\n");
   //////////////
//ALT KATEGORI BURDAN BUL

        for(j=0; j<counter; j++){
    na = getWords2(kategoriler[j],arr);

            strcpy(ana_kategoriler_unique[j],arr[0]);

    }

int thecounter=0;

   for (i=0; i<counter; i++)
    {
        int j;
        for (j=0; j<i; j++)
           if (strcmp(ana_kategoriler_unique[i],ana_kategoriler_unique[j]) == 0)
               break;

        if (i == j){
            strcpy(ana_kategoriler[thecounter],ana_kategoriler_unique[i]);
            thecounter++;
        }

    }
    printf("\nTxT den Ayiklanan Kategoriler:\n");
    for(i=0; i<thecounter; i++){
        printf("%s\n", ana_kategoriler[i]);
    }

    printf("\n\n");
    char altkategori1[25][60];
    char altkategori2[25][60];
    char altkategori3[25][60];
    char altkategori4[25][60];
    char altkategori5[25][60];
    char altkategori6[25][60];
    char altkategori7[25][60];
    char altkategori8[25][60];
    char sayac2=0;
    char sayac3=0;
    char sayac4=0;
    char sayac5=0;
    char sayac6=0;
    char sayac7=0;
    char sayac8=0;
    char sayac9=0;
            for(j=0; j<counter; j++){
            if(strstr(kategoriler[j],ana_kategoriler[0]) != NULL){
                na = getWords2(kategoriler[j],arr);
            strcpy(altkategori1[sayac2],arr[1]);
            sayac2++;

            }
        }
        for(j=0; j<counter; j++){
            if(strstr(kategoriler[j],ana_kategoriler[1]) != NULL){
                  na = getWords2(kategoriler[j],arr);
            strcpy(altkategori2[sayac3],arr[1]);
            sayac3++;

            }
        }
         for(j=0; j<counter; j++){
            if(strstr(kategoriler[j],ana_kategoriler[2]) != NULL){
                 na = getWords2(kategoriler[j],arr);
            strcpy(altkategori3[sayac4],arr[1]);
            sayac4++;

            }
        }
         for(j=0; j<counter; j++){
            if(strstr(kategoriler[j],ana_kategoriler[3]) != NULL){
                 na = getWords2(kategoriler[j],arr);
            strcpy(altkategori4[sayac5],arr[1]);
            sayac5++;

            }
        }
         for(j=0; j<counter; j++){
            if(strstr(kategoriler[j],ana_kategoriler[4]) != NULL){
                 na = getWords2(kategoriler[j],arr);
            strcpy(altkategori5[sayac6],arr[1]);
            sayac6++;

            }
        }
         for(j=0; j<counter; j++){
            if(strstr(kategoriler[j],ana_kategoriler[5]) != NULL){
                 na = getWords2(kategoriler[j],arr);
            strcpy(altkategori6[sayac7],arr[1]);
           // printf("%s\n",altkategori6[sayac3] );
            sayac7++;

            }
        }
    for(j=0; j<counter; j++){
            if(strstr(kategoriler[j],ana_kategoriler[6]) != NULL){
                 na = getWords2(kategoriler[j],arr);
            strcpy(altkategori7[sayac8],arr[na]);
            sayac8++;

            }
        }
         for(j=0; j<counter; j++){
            if(strstr(kategoriler[j],ana_kategoriler[7]) != NULL){
                 na = getWords2(kategoriler[j],arr);
            strcpy(altkategori8[sayac9],arr[na]);
           // printf("%s\n",altkategori8[sayac3] );
            sayac9++;

            }
        }
 int altkategori_sayisi[thecounter];
        altkategori_sayisi[0] = sayac2;
        altkategori_sayisi[1] = sayac3;
        altkategori_sayisi[2] = sayac4;
        altkategori_sayisi[3] = sayac5;
        altkategori_sayisi[4] = sayac6;
        altkategori_sayisi[5] = sayac7;
        altkategori_sayisi[6] = sayac8;
        altkategori_sayisi[7] = sayac9;


//////////////////////////////
    //Veriler de KATEGORININ KULLANICILARINI ARA
int rezervasyon_sayisi1=0;
for(i=0; i<sayac2; i++){
    for(j=0; j<sayac; j++){
    if(strstr(veriler[j],altkategori1[i]) !=NULL){
           // printf("%s\n", veriler[j]);
         rezervasyon_sayisi1++;
    }
    }

}
printf("-----------------------------------------------------------\n");
printf("REZERVASYON TXT DEN ALINAN KATEGORILER DUGUMLERE EKLENIYOR...\n");
printf("-----------------------------------------------------------\n");
////// ANA KATEGORILERI ve ALT KATEGORILERINI KATEGORI DUGUMUNE AT
printf("Ana Kategoriler\n\n");
    createRootNode("rezervasyon", 5,5,6,6,7);

for(i=0; i<thecounter; i++){
    addChild(start, cat, ana_kategoriler[i],altkategori_sayisi[i],2,rezervasyon_sayisi1,12,7);
}
printf("\n\nAlt Kategoriler\n\n");

printf("1.Kategorinin alt kategoriler:\n\n");
for(i=0; i<sayac2; i++){
    addChild(start->child, cat, altkategori1[i],0,2,8,12,6);
}
printf("\n2.Kategorinin alt kategoriler:\n\n");
for(i=0; i<sayac3; i++){
    addChild(start->child->sibling, cat, altkategori2[i],0,1,6,12,6);
}
printf("\n3.Kategorinin alt kategoriler:\n\n");
for(i=0; i<sayac4; i++){
    addChild(start->child->sibling->sibling, cat, altkategori3[i],0,3,5,12,6);
}
printf("\n4.Kategorinin alt kategoriler:\n\n");
for(i=0; i<sayac5; i++){
    addChild(start->child->sibling->sibling->sibling, cat, altkategori4[i],0,2,7,12,6);
}
printf("\n5.Kategorinin alt kategoriler:\n\n");
for(i=0; i<sayac6; i++){
    addChild(start->child->sibling->sibling->sibling->sibling, cat, altkategori5[i],0,3,9,12,6);
}
printf("\n6.Kategorinin alt kategoriler:\n\n");
for(i=0; i<sayac7; i++){
    addChild(start->child->sibling->sibling->sibling->sibling->sibling, cat, altkategori6[i],0,1,5,12,6);
}
printf("\n7.Kategorinin alt kategoriler:\n\n");
for(i=0; i<sayac8; i++){
    addChild(start->child->sibling->sibling->sibling->sibling->sibling->sibling, cat, altkategori7[i],0,1,5,12,6);
}
printf("\n8.Kategorinin alt kategoriler:\n\n");
for(i=0; i<sayac9; i++){
    addChild(start->child->sibling->sibling->sibling->sibling->sibling->sibling->sibling, cat, altkategori8[i],0,1,5,12,6);
}

printf("\n\n");
// KULLANICI VERILERINI AIT OLDUGU ALT KATEGORILERE AT
}
if(secim ==2){
    struct userNode *root2 = NULL;
    root2 = insert(root2,"whitney-mcnamara","kategori",50);
    insert(root2,"charles-smith","kategori", 30);
    insert(root2,"wil-stephens","kategori", 20);
    insert(root2,"michael-diamant","kategori", 40);
    insert(root2, "richard-titus","kategori",70);
    insert(root2,"brad-feld","kategori", 60);
    insert(root2,"jon-steinberg","kategori", 80);

    maxHeapify(root2);
    printf("\nHeapSort islemi sonrasi: (POSTORDER TRAVERSAL)\n");
    postorderTraversal(root2);


}
if(secim ==3){

}
if(secim == 4){
createRootNode("rezervasyon", 5,5,6,6,7);
char ad[40];
printf("Kategori adi girin:");
scanf("%s", &ad);
fflush(stdin);
printf("Eklenen kategori:");
addChild(start, cat,ad,0,1,6,12,6);
}
if(secim ==5){

}
if(secim == 6){

   struct userNode *root = NULL;
    root = insert(root,"harj-taggar","american",3);
    insert(root,"fred-wilson","american", 5);
     maxHeapify(root);
    printf("\nFood:American kategorisindeki kullanicilar: (MAX HEAP SORT SONRASI) (POSTORDER TRAVERSAL)\n\n");
    postorderTraversal(root);
}
    }


    printf("\n");

  struct userNode *root = NULL;
    root = insert(root,"fred-wilson,","american",5);
    insert(root,"harj-taggar","american", 3);
    insert(root, "maia-bittner","american",7);
    insert(root, "ben-parr","american",4);


    maxHeapify(root);

    start->child->child->child = root;
    start->child->child->child->sibling = root->left;






    return 0;
}



