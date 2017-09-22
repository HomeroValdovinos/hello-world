package homero.calculator;

public class Calculator {

	public static void main(String args[]) {
		double num=0;
		String one = args[0];
//		Operations operator = new Operations();
		for ( int i=0; i<args.length; i++ ){
			
			System.out.println("This is num: " + num);
			num = Double.parseDouble( args[i] ) + num; 
			System.out.println("Num has changed to: " + num);
		}
		 
		System.out.println("The sum is " + num);
		System.out.println("Esto trae one:" + one);
	}
}

/*
package homero.valdovinos.calculator;

public class Calc {

	public static void main(String[] args) {
		
		Operations ope = new Operations();
		System.out.println("The result is: " + ope.c);

	}
}

package homero.valdovinos.calculator;

public class Operations {

	int a = 5;
	int b = 10;
	int c;
	
	public void callSuma(){
		Operations luis = new Operations();
		c = luis.suma();
		System.out.println("This is the result: " + c);
	}
	
	public int suma (){
		//c = a+b;
		return a+b;
	}
}

package toledo.homero;

public class Example1 {


	public static void main(String[] args) {

		Operations operations = new Operations();
		
		System.out.println("This is the age: " + operations.getEdad());
		
	}

}

package toledo.homero;

public class Operations {
	
//	public Operations(String name, int edad) {
//		super();
//		this.name = name;
//		this.edad = edad;
//	}
	
	private String name = "Homero";
	private int edad = 32;
	
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public int getEdad() {
		return edad;
	}
	public void setEdad(int edad) {
		this.edad = edad;
	}
}


*/