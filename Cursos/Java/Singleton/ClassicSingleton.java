public class ClassicSingleton {

   private static ClassicSingleton instance = null;
   private ClassicSingleton() {
   }

   public static ClassicSingleton getInstance() {
      if(instance == null) {
         instance = new ClassicSingleton();
      }
      return instance;
   }
   public void print(){
	   System.out.println ("hola");
   }
   
   public String name="homero";
	   
}