class case5{
    void show(int a, float b){
    System.out.println("int float method");
    }
    void show(float a, int b){
    System.out.println("float int method");
    }
    public static void main(String[] args){
        Test t = new Test();
        t.show(20.5f, 10);  // float int method
        t.show(10.5f, 20.5f); // will give error (no automatic promotion)
    }
}
