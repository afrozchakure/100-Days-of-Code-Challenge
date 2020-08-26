class AutomaticPromotion{
    void show(int a){
    System.out.println("int method");
    }
    void show(String a){
    System.out.println("String method");
    }
    public static void main(String[] args){
        AutomaticPromotion t = new AutomaticPromotion();
        t.show('a');
    }
}

// Makes use of concept of automatic promotion - char gets converted into int

// Object a
// String a
// t.show("a")  -- calls child class
