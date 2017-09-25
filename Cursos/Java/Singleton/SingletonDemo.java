public class SingletonDemo {
	
	public static void main(String[] args){
		ClassicSingleton tmp = ClassicSingleton.getInstance();
		ClassicSingleton tmp2 = ClassicSingleton.getInstance();
		tmp.print();
		tmp.print();
	}
}