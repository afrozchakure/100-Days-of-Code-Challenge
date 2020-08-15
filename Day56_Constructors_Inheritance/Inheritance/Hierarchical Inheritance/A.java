// Hierarchical Inheritance

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

}
class C extends A
{
    void showC()
    {
        System.out.println("c Class method");
    }
    public static void main(String[] args)
    {
        A ob1 = new A();
        ob1.showA();
//        ob1.showB();
        System.out.println("------------------");
        
        B ob2 = new B();
        ob2.showA();
        ob2.showB();
        System.out.println("------------------");
        
        C ob3 = new C();
        ob3.showA();
       // ob3.showB();  Not be able to call B
        ob3.showC();
    }}
