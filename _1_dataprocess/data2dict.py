import os


def nodedict():
    resdict = {}
    with open("node.txt") as f:
        ll = [[], [], [], [], [], []]
        for i in f:
            ss = i.split(' ')
            level = len(ss[0])
            datas = ss[1].split('\n')[0]
            ll[level - 1].append(datas)
            if level == 1:
                continue
            else:
                resdict[datas] = ll[level - 2][len(ll[level - 2]) - 1]
    return resdict


def nodelist():
    reslist = {}
    with open("node.txt") as f:
        for i in f:
            ss = i.split(' ')
            datas = ss[1].split('\n')[0]
            level = len(ss[0])
            reslist[datas] = "k{}".format(level)
    return reslist


def nodeid():
    idlist = {}
    cnt = 0
    with open("node.txt") as f:
        for i in f:
            ss = i.split(' ')
            datas = ss[1].split('\n')[0]
            idlist[datas] = cnt
            cnt += 1
    return idlist
ln = ['栈','树','二叉树','搜索树','哈夫曼树']
ldesc = [
    '栈（stack）又名堆栈，它是一种运算受限的线性表。限定仅在表尾进行插入和删除操作的线性表。这一端被称为栈顶，相对地，把另一端称为栈底。向一个栈插入新元素又称作进栈、入栈或压栈，它是把新元素放到栈顶元素的上面，使之成为新的栈顶元素；从一个栈删除元素又称作出栈或退栈，它是把栈顶元素删除掉，使其相邻的元素成为新的栈顶元素。',
    '树是一种数据结构，它是由n(n>=1)个有限节点组成一个具有层次关系的集合。把它叫做“树”是因为它看起来像一棵倒挂的树，也就是说它是根朝上，而叶朝下的。',
    '二叉树（Binary tree）是树形结构的一个重要类型。许多实际问题抽象出来的数据结构往往是二叉树形式，即使是一般的树也能简单地转换为二叉树，而且二叉树的存储结构及其算法都较为简单，因此二叉树显得特别重要。二叉树特点是每个结点最多只能有两棵子树，且有左右之分',
    '二叉查找树（Binary Search Tree），（又：二叉搜索树，二叉排序树）它或者是一棵空树，或者是具有下列性质的二叉树： 若它的左子树不空，则左子树上所有结点的值均小于它的根结点的值； 若它的右子树不空，则右子树上所有结点的值均大于它的根结点的值； 它的左、右子树也分别为二叉排序树。',
    '给定N个权值作为N个叶子结点，构造一棵二叉树，若该树的带权路径长度达到最小，称这样的二叉树为最优二叉树，也称为哈夫曼树(Huffman Tree)。哈夫曼树是带权路径长度最短的树，权值较大的结点离根较近。'
]
lcode = [
    '''
class SqStack
{
private:
    enum { MaxSize = 100 };
    int data[MaxSize];
    int top;
public:
    SqStack();
    ~SqStack();
    bool isEmpty();
    void pushint(int x);
    int popint();
    int getTop();
    void display();
};
SqStack::SqStack()
{
    top = -1;
}
SqStack::~SqStack() {}
bool SqStack::isEmpty() //判断栈为空
{
    return(top == -1);
}
void SqStack::pushint(int x)//元素进栈
{
    if (top == MaxSize - 1)
    {
        cout << "栈上溢出！" << endl;
    }
    else
    {
        ++top;
        data[top] = x;
    }
}
int SqStack::popint()//退栈
{
    int tmp = 0;
    if (top == -1)
    {
        cout << "栈已空！" <<endl;
    }
    else
    {
        tmp = data[top--];
    }
    return tmp;
}
int SqStack::getTop()//获得栈顶元素
{
    int tmp = 0;
    if (top == -1)
    {
        cout << "栈空！" << endl;
    }
    else
    {
        tmp = data[top];
    }
    return tmp;
}
void SqStack::display()//打印栈里元素
{
    cout << "栈中元素：" << endl;
    for (int index = top; index >= 0; --index)
    {
        cout << data[index] << endl;
    }
}
    ''',
    '''
template <class DataType>
struct BiNode
{
    DataType data;
    BiNode<DataType> * lchild,*rchild;
};

template <class DataType>
class BiTree
{
public:
    BiTree(){root = Create(root);}
    ~BiTree(){Release(root);}
    void PreOrder(){PreOrder(root);}    //前序遍历
    void InOrder(){InOrder(root);}      //中序遍历
    void PostOrder(){PostOrder(root);}  //后序遍历
private:
    BiNode<DataType> * root;
    BiNode<DataType> * Create(BiNode<DataType> *bt);
    void Release(BiNode<DataType> *bt);
    void PreOrder(BiNode<DataType> *bt);
    void InOrder(BiNode<DataType> *bt);
    void PostOrder(BiNode<DataType> *bt);
};
template <class DataType>
BiNode<DataType> *BiTree<DataType>::Create(BiNode<DataType> *bt)
{
    DataType ch;
    cin>>ch;
    if(ch == '#') bt = NULL;
    else{
        bt = new BiNode<DataType>;
        bt->data = ch;
        bt->lchild = Create(bt->lchild);
        bt->rchild = Create(bt->rchild);
    }
    return bt;
}
    ''',
    '''
template <class DataType>
struct BiNode
{
    DataType data;
    BiNode<DataType> * lchild,*rchild;
};

template <class DataType>
class BiTree
{
public:
    BiTree(){root = Create(root);}
    ~BiTree(){Release(root);}
    void PreOrder(){PreOrder(root);}    //前序遍历
    void InOrder(){InOrder(root);}      //中序遍历
    void PostOrder(){PostOrder(root);}  //后序遍历
private:
    BiNode<DataType> * root;
    BiNode<DataType> * Create(BiNode<DataType> *bt);
    void Release(BiNode<DataType> *bt);
    void PreOrder(BiNode<DataType> *bt);
    void InOrder(BiNode<DataType> *bt);
    void PostOrder(BiNode<DataType> *bt);
};
template <class DataType>
BiNode<DataType> *BiTree<DataType>::Create(BiNode<DataType> *bt)
{
    DataType ch;
    cin>>ch;
    if(ch == '#') bt = NULL;
    else{
        bt = new BiNode<DataType>;
        bt->data = ch;
        bt->lchild = Create(bt->lchild);
        bt->rchild = Create(bt->rchild);
    }
    return bt;
}
    ''',
    '''
#ifndef BSTREE_H
#define BSTREE_H
#include <algorithm> 
#include <iostream>
using namespace std;
 
// 定义二叉搜索树的节点
template<typename K=int, typename V=int>   // key: value类型的节点 
struct BSTreeNode
{
	BSTreeNode* leftchild;
	BSTreeNode* rightchild;
	K key;
	V value;
	
	BSTreeNode(K& theKey, V& theValue)
	{
		key = theKey;
		value = theValue;
		leftchild = NULL;
		rightchild = NULL;
	}
}; 
template<typename K, typename V>
class BSTree
{
	typedef BSTreeNode<K, V> BSTreeNode;
	private:
	BSTreeNode* root;     // 二叉搜索树的根节点
	int treeSize;
	void destory(BSTreeNode* mroot);       // 删除二叉树的所有节点  // 析构函数 
	BSTreeNode* find(K theKey, BSTreeNode* mroot); 
	void insert(K theKey, V theValue, BSTreeNode* mroot);
	void remove(K theKey, BSTreeNode* mroot); // 删除特定的节点 
	void out_put(BSTree* mroot);
	 
	public:
	BSTree();
	~BSTree();
	// void destory(); 
	// 查找二叉树的节点
	BSTreeNode* find(K theKey);  // 参数：键值
	void insert(K theKey, V theValue);
	void remove(K theKey); 
	void out_put();
};
 
template<typename K, typename V>
void BSTree<K, V>::destory(BSTreeNode* mroot)
{
	// 删除所有节点   递归调用 
	if(mroot!=NULL)
	{
		destory(mroot->leftchild);
		destory(mroot->rightchild);
		delete mroot;
	}	 
}
template<typename K, typename V>
BSTree<K, V>::BSTree()
{
	treeSize = 0;
	root = NULL;
}
 
template<typename K, typename V> 
BSTree<K, V>::~BSTree()
{
	// 删除二叉树的节点
	destory(root); 
}
 
template<typename K, typename V>
BSTreeNode* BSTree<K, V>::find(K theKey)
{
	// 二叉搜索树的查找函数
	// 根据关键字查找：
	return find(theKey, root); 
}
 
template<typename K, typename V>
BSTreeNode* BSTree<K, V>::find(K theKey, BSTreeNode* mroot)
{
	if(mroot != NULL)
	{
		if(mroot->key==theKey)
		{
			return mroot;
		}
		else if(mroot->key>theKey)   // 搜索左子树
		{
			return find(theKey, mroot->leftchild);    // 递归的方法 
		} 
		else   // 搜索右子树
		{
			return find(theKey, mroot->rightchild);
		} 
	}
	return NULL;  // 没有找到 
}
 
template<typename K, typename V>
void BSTree<K, V>::insert(K theKey, V theValue, BSTreeNode* mroot)
{
	// NULL
	
	if(mroot==NULL)
	{
		mroot = new BSTreeNode(theKey, theValue);
		return;    // 递归结束    
	}
	
	if(mroot->key==theKey)   // 关键字已经存在 
	{
		mroot->value = theValue;
		return;    // 结束递归 
	} 
	else if(theKey < mroot->key)    // 插入左子树
	{
		insert(theKey, theValue, mroot->leftchild);
	} 
	
	else   // 插入右子树 
	{
		insert(theKey, theValue, mroot->rightchild); 
	}
	
}
 
template<typename K, typename V>
void BSTree<K, V>::insert(K theKey, V theValue)
{
	insert(theKey, theValue, root);
}
 
template<typename K, typename V>
void BSTree<K, V>::remove(K theKey, BSTreeNode* mroot)
{
	/* 
	if(mroot==NULL)   // 结束的条件 
	{
		cout << "No such node" << endl; 
		return;
	}
	*/
	 
	// 只有一个节点
	if(mroot->leftchild==NULL && mroot->rightchild==NULL)   // 最底层的节点 
	{
		if(root->key==theKey)   // 是要查找的节点 
		{
			delete mroot;
			mroot = NULL;
			return;
		}
		
	}
	
	if(theKey<mroot->key)    // 搜索左子树 
	{
		remove(theKey, mroot->leftchild); 
	} 
	else if(theKey>mroot->key)
	{
		remove(theKey, mroot->rightchild);   // 搜索右子树 
	}
	else     // 相等。且不是最底层的节点  
	{
		BSTreeNode* del = NULL;    // 临时的指针
		if(mroot->leftchild==NULL)   // 只有右孩子 
		{
			del = mroot;
			mroot = mroot->rightchild;   // 取右孩子
			delete del;
			del = NULL;
			return; 
		} 
		else if(mroot->rightchild==NULL)   // 只有左孩子
		{
			del = mroot;
			mroot = mroot->leftchild;
			delete del;
			del = NULL;
			return;
		}
		else   // 要删除的节点有左右子树 
		{
			BSTreeNode* rightFirst = mroot->rightchild;   // 获取要删除的节点的右孩子
			while(rightFirst->leftchild!=NULL)
			{
				rightFirst = rightFirst->leftchild;
			} 
			
			// 交换
			// 将要删除的节点交换到最底层 
			swap(mroot->key, rightFirst->key);
			swap(mroot->value, rightFirst->value); 
			remove(theKey, mroot->rightchild);     // 接着删除
		    return;   // ? 
		} 
	} 
	
}
 
template<typename K, typename V>
void BSTree<K, V>::remove(K theKey)
{
	remove(theKey, root);
}
 
template<typename K, typename V>
void BSTree<K, V>::out_put(BSTreeNode* mroot)
{
	if(mroot==NULL)
	{
		return;
	}
	out_put(mroot->leftchild);
	cout << "key: " << mroot->key << " value: " << mroot->value << " ";
	out_put(mroot->rightchild);
}
 
template<typename K, typename V>
void BSTree<K, V>::out_put() 
{
	out_put(root);
} 
 
#endif
    ''',
    '''
//树结点定义
typedef  struct 
{
    int weight;
    int parent;
    int lchild;
    int rchild;
}HTNode,*HuffmanTree;

static char N[100];//用于保存正文

//哈弗曼编码，char型二级指针
typedef char **HuffmanCode;

//封装最小权结点和次小权结点
typedef  struct 
{
    int s1;
    int s2;
}MinCode;

//函数声明
void Error(char *message);
HuffmanCode HuffmanCoding(HuffmanTree &HT,HuffmanCode HC,int *w,int n);
MinCode   Select(HuffmanTree HT,int n);

//当输入1个结点时的错误提示
void Error(char *message)
{  
    fprintf(stderr,"Error:%s\\n",message);  
    exit(1);
}

//构造哈夫曼树HT，编码存放在HC中,w为权值,n为结点个数
HuffmanCode HuffmanCoding(HuffmanTree &HT,HuffmanCode HC,int *w,int n)
{ 
    int i,s1=0,s2=0; 
    HuffmanTree p;
    char *cd;
    int f,c,start,m;
    MinCode min;

    if(n<=1) 
    {
        Error("Code too small!");//只有一个结点不进行编码，直接exit(1)退出。非return,如果return 会造成main函数HT[i]无值
    }

    m=2*n-1;//哈弗曼编码需要开辟的结点大小为2n-1
    HT=(HuffmanTree)malloc((m+1)*sizeof(HTNode));//开辟哈夫曼树结点空间 m+1 。为了对应关系，我们第0个空间不用。

    //初始化n个叶子结点,w[0] = 0,main函数已赋值
    for(p=HT,i=0;i<=n;i++,p++,w++)
    { 
        p->weight=*w;  
        p->parent=0; 
        p->lchild=0; 
        p->rchild=0;
    }

    //将n-1个非叶子结点的初始化
    for(;i<=m;i++,p++)
    { 
        p->weight=0;  
        p->parent=0; 
        p->lchild=0;
        p->rchild=0;
    }

    //构造哈夫曼树
    for(i=n+1;i<=m;i++)
    {
        min=Select(HT,i-1);//找出最小和次小的两个结点
        s1=min.s1 ; //最小结点下标
        s2=min.s2;//次小结点下标
        HT[s1].parent=i; 
        HT[s2].parent=i;
        HT[i].lchild=s1;
        HT[i].rchild=s2;
        HT[i].weight=HT[s1].weight+HT[s2].weight;//赋权和
    }

    //打印哈弗曼树
    printf("HT  List:\\n");
    printf("Number\\t\\tweight\\t\\tparent\\t\\tlchild\\t\\trchild\\n");

    for(i=1;i<=m;i++)
    {
        printf("%d\\t\\t%d\\t\\t%d\\t\\t%d\\t\\t%d\\t\\n",i,HT[i].weight,HT[i].parent,HT[i].lchild,HT[i].rchild);
    }

    //从叶子结点到根节点求每个字符的哈弗曼编码
    HC=(HuffmanCode)malloc((n+1)*sizeof(char *));
    cd=(char *)malloc(n*sizeof(char *));//为哈弗曼编码动态分配空间
    cd[n-1]='\\0';//如：3个结点编码最长为2。cd[3-1] = '\\0';

    //求叶子结点的哈弗曼编码
    for(i=1;i<=n;i++)
    { 
        start=n-1;
        //定义左子树为0，右子树为1
        /*
        从最下面的1号节点开始往顶部编码(逆序存放)，然后编码2号节点，3号......
        */
        for(c=i,f=HT[i].parent; f!=0; c=f,f=HT[f].parent)
        {
            if(HT[f].lchild==c)  
                cd[--start]='0';
            else 
                cd[--start]='1';
        }

        //为第i个字符分配编码空间
        HC[i]=(char *)malloc((n-start)*sizeof(char *));
        //将当前求出结点的哈弗曼编码复制到HC
        strcpy(HC[i],&cd[start]);   
    }
    free(cd);
    return HC;
}

MinCode Select(HuffmanTree HT,int n)
{  
    int min,secmin;
    int temp = 0;
    int i,s1,s2,tempi = 0;
    MinCode  code ;
    s1=1;
    s2=1;

    min = 66666;//足够大

    //找出权值weight最小的结点，下标保存在s1中
    for(i=1;i<=n;i++)
    {
        if(HT[i].weight<min && HT[i].parent==0)
        {
            min=HT[i].weight;
            s1=i;
        }
    }

    secmin = 66666;//足够大

    //找出权值weight次小的结点，下标保存在s2中
    for(i=1;i<=n;i++)
    {
        if((HT[i].weight<secmin) && (i!=s1) && HT[i].parent==0)
        {
            secmin=HT[i].weight; 
            s2=i;
        }
    }

    //放进封装中
    code.s1=s1;
    code.s2=s2;
    return code;
}

void HuffmanTranslateCoding(HuffmanTree HT, int n,char* ch)
{//译码过程
    int m=2*n-1;
    int i,j=0;

    printf("After Translation:");
    while(ch[j]!='\\0')//ch[]:你输入的要译码的0101010串
    {
        i=m;
        while(0 != HT[i].lchild && 0 != HT[i].rchild)//从顶部找到最下面
        {
            if('0' == ch[j])//0 往左子树走
            {
                i=HT[i].lchild;
            }
            else//1 往右子树走
            {
                i=HT[i].rchild;
            }
            ++j;//下一个路径
        }
        printf("%c",N[i-1]);//打印出来
    }
    printf("\\n");
}

void main()
{
    HuffmanTree HT=NULL;
    HuffmanCode HC=NULL;
    int *w=NULL;
    int i,n;
    char tran[100];

    printf("Input  N(char):");
    gets(N);
    fflush(stdin);
    n = strlen(N);

    w=(int *)malloc((n+1)*sizeof(int *));//开辟n+1个长度的int指针空间
    w[0]=0;
    printf("Enter weight:\\n");

    //输入结点权值
    for(i=1;i<=n;i++)
    {  
        printf("w[%d]=",i);  
        scanf("%d",&w[i]);
    }
    fflush(stdin);
    //构造哈夫曼树HT，编码存放在HC中,w为权值,n为结点个数
    HC=HuffmanCoding(HT,HC,w,n);

    //输出哈弗曼编码
    printf("HuffmanCode:\\n");
    printf("Number\\t\\tWeight\\t\\tCode\\n");
    for(i=1;i<=n;i++)
    {
        printf("%c\\t\\t%d\\t\\t%s\\n",N[i-1],w[i],HC[i]);
    }

    fflush(stdin);
    //译码过程
    printf("Input HuffmanTranslateCoding:");
    gets(tran);
    HuffmanTranslateCoding(HT, n, tran);
    return;
}

    '''
]
lresaon = [
    '栈某种意义上讲，它像是一个开口的盒子，先放进去的东西总是会被后放进去的东西压在下面，那么如果想拿出被压住的东西，必须要先取出顶部的东西，也就是后放进去的东西。换个说法就是先入后出。',
    '树是由结点或顶点和边组成的(可能是非线性的)且不存在着任何环的一种数据结构。没有结点的树称为空(null或empty)树。一棵非空的树包括一个根结点，还(很可能)有多个附加结点，所有结点构成一个多级分层结构。',
    '棵二叉树是节点的一个有限集合，该集合或者为空，或者由一个根节点加上两棵左子树和右子树组成.',
    '二叉搜索树作为一种经典的数据结构，它既有链表的快速插入与删除操作的特点，又有数组快速查找的优势；所以应用十分广泛，例如在文件系统和数据库系统一般会采用这种数据结构进行高效率的排序与检索操作。',
    '哈夫曼树是一种单词树，广泛使用于数据压缩之中。将会根据每个字符的权重，来构建一颗Huffman树，同时根据Huffman树对原来的文本进行二次编码，以达到压缩数据的目的'
]
def nodedesc():
    nodedescp={}
    for i,j in zip(ln,ldesc):
        nodedescp[i] = j
    for i in nodelist():
        if i in ln:
            continue

        nodedescp[i]=i+'描述'
    return nodedescp


def nodecode():
    nodecodes = {}

    for i, j in zip(ln, lcode):
        nodecodes[i] = j.replace('\n','</br>')
    for i in nodelist():
        if i in ln:
            continue
        nodecodes[i] = i+'代码'
    return nodecodes

def noderes():
    noderesn={}

    for i, j in zip(ln, lresaon):
        noderesn[i] = j
    for i in nodelist():
        if i in ln:
            continue
        noderesn[i] = i+'引入原因'
    return noderesn
