class pokemon{
    int level;
    String name;

    void call{
        System.out.println(name + "" + level);
    }
}

public class main{
    public static void main(String[] args){
        pokemon p = new pokemon();
        p.name= 'Pikachu'
        p.level= 10
        
        p.call()
    }
}

