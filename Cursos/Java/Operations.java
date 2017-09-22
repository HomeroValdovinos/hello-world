package homero.calculator;

public class Operations {

	/*public float sum(float a, float b){
		return a + b;
	}
	*/
	public void sum(float... args) {  
		  double sumar = 0;  
		  for (float i : (args))  
		    sumar += i;  
		  System.out.println("La suma es " + sumar);  
	}
		
	public float rest(float a, float b){
		return a - b;
	}
	public float multi(float a, float b){
		return a * b;
	}
	public float div(float a, float b){
		return a / b;
	}
}
