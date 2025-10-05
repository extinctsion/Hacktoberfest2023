import java.util.Scanner;

class Stack {
    private int top;
    private int capacity;
    private int[] stackArray;

    // Constructor
    public Stack(int size) {
        capacity = size;
        stackArray = new int[capacity];
        top = -1; // empty stack
    }

    // Push an element
    public void push(int value) {
        if (isFull()) {
            System.out.println("Stack Overflow! Cannot push " + value);
            return;
        }
        stackArray[++top] = value;
        System.out.println(value + " pushed to stack.");
    }

    // Pop an element
    public int pop() {
        if (isEmpty()) {
            System.out.println("Stack Underflow! Nothing to pop.");
            return -1;
        }
        int value = stackArray[top--];
        System.out.println(value + " popped from stack.");
        return value;
    }

    // Peek (top element)
    public int peek() {
        if (isEmpty()) {
            System.out.println("Stack is empty!");
            return -1;
        }
        return stackArray[top];
    }

    // Check if stack is empty
    public boolean isEmpty() {
        return top == -1;
    }

    // Check if stack is full
    public boolean isFull() {
        return top == capacity - 1;
    }

    // Display elements
    public void display() {
        if (isEmpty()) {
            System.out.println("Stack is empty!");
            return;
        }
        System.out.print("Stack elements (top → bottom): ");
        for (int i = top; i >= 0; i--) {
            System.out.print(stackArray[i] + " ");
        }
        System.out.println();
    }
}

public class StackOps {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter stack size: ");
        int size = sc.nextInt();
        Stack stack = new Stack(size);

        while (true) {
            System.out.println("\n1. Push");
            System.out.println("2. Pop");
            System.out.println("3. Peek");
            System.out.println("4. Display");
            System.out.println("5. Exit");
            System.out.print("Enter your choice: ");

            int choice = sc.nextInt();

            switch (choice) {
                case 1:
                    System.out.print("Enter value to push: ");
                    int val = sc.nextInt();
                    stack.push(val);
                    break;
                case 2:
                    stack.pop();
                    break;
                case 3:
                    System.out.println("Top element: " + stack.peek());
                    break;
                case 4:
                    stack.display();
                    break;
                case 5:
                    System.out.println("Exiting...");
                    sc.close();
                    System.exit(0);
                default:
                    System.out.println("Invalid choice!");
            }
        }
    }
}
