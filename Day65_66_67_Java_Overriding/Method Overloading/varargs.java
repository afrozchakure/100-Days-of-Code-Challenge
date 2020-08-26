class varargs
{
    void show(int a)
    {
        System.out.println("int method");
    }
    void show(int... a)
    {
        System.out.println("varargs method");
    }
    public static void main(String[] args){
        varargs t = new varargs();
        t.show(10, 20, 30);
    }
}

// varargs has least priority
