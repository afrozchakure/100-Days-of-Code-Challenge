class Test  
{
    void show(String a, int b)
    {
        System.out.println("1");
    }
    void show(int a, String b)
    {
        System.out.println("2");
    }
    public static void main(String[] args){
        Test t = new Test();
        t.show("abc", 20);
    }
}

// Different Arguments (Same method name and class name)
// Different Sequence, data types and no. of arguments
