// Single Inheritance

class A
{
    void showA()
    {
        System.out.println("a Class method");
    }
}
class B extends A
{
    void showB()
    {
        System.out.println("b Class method");
    }
    public static void main(String[] args)
    {
        A ob1 = new A();
        ob1.showA();
//        ob1.showB();
        B ob2 = new B();
        ob2.showA();
        ob2.showB();
    }
}
