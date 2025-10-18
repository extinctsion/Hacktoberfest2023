class BSTimplementation{ //implementatiion of binary search tree 
    public class Node{
        int data;
        Node left;
        Node right;
        int height;
        Node(int data){
            this.data=data;
            this.left=null;
            this.right=null;
            this.height=1;
        }
        public int getValue(){
            return data;
        }
    }
    private Node root;

   public int height(Node node){
    if(node == null){
        return -1;

    }
    return node.height;
   }
   public boolean isEmpty(){
    return root==null;
   }


    public void insert(int value){
     root = insert(value,root);
    }
   private Node insert(int value , Node node ){ //insertion function in binary tree
    if(node==null)
    return new Node(value);
    if(value<node.data){
        node.left = insert(value,node.left);
    }
    if(value>node.data){
        node.right = insert(value,node.right);
    }
return node;
   }



   public boolean balanced(){
    return isBalanced(root);
   }
    private boolean isBalanced(Node node){
        if(node==null){
            return true;
        }
        return Math.abs(height(node.left)-height(node.right))<=1 && isBalanced(node.left) && isBalanced(node.right);
    }


    public void display(){
        display(this.root,"root Node is ");
    }
    private void display(Node node , String details){
        if(node==null){
            return;
        }
        System.out.println(details+node.data);
        display(node.left,"left child of "+node.data+" is ");
        display(node.right,"right child of "+node.data+" is ");
    }



    //inserting multiple items
    public void populate(int[] values){
        for(int value:values){
            insert(value);
        }
    }
    


    public void populatesorted(int[] values){
        populatesorted(values,0,values.length-1);
    }
    private void populatesorted(int[] nums,int start , int end){
        if(start>=end){
            return;
        }
        int mid = start + (end-start)/2;
        this.insert(nums[mid]);
        populatesorted(nums,start,mid-1);
        populatesorted(nums,mid+1,end);
    }
    //in general we will be using self balacing binary trees like an AVL tree or a Red Black Tree 
}
