public class Calculator {

	public static void main(String args[]) {

		Operations operator = new Operations();

		System.out.println("The addition is " + opeartor.sum(2,3));
		System.out.println("The rest is " + opeartor.rest(3,2));
		System.out.println("The multi is " + opeartor.multi(4,3));
		System.out.println("The division is " + opeartor.div(10,2));
	}
	
	puclic suma(String args[]){
		
	}
}


/*public class Calculator {

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
	
	puclic suma(String args[]){
		
	}
}*/