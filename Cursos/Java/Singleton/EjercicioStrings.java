import java.lang.StringBuilder;
/*public class EjercicioStrings {
	public static void main(String args[]) {
		String cadena="";
		String cadena2="";
		
		System.out.println ("Esto trade cadena " + cadena);

		int cortar = 5;
		for (int i=0; i <= cortar; i++){
			cadena2+=cadena.charAt(i);
		}
		System.out.println ("Esto trade resultado " + cadena2);
	}
}
*/
/*
public class EjercicioStrings {
	public static void main(String args[]) {
		String initializedToNull=null;
		initializedToNull += "Java";
		System.out.println (initializedToNull);
	}
}

public class EjercicioStrings {
	public static void main(String args[]) {
		StringBuilder sbl = new StringBuilder();
		char[] name = {'J','A','v','a','7'};
		sbl.append(name,1,3);
		System.out.println (sbl);
	}
}
public class EjercicioStrings {
	public static void main(String args[]) {
		StringBuilder sbl = new StringBuilder("0123456");
		sbl.delete(2,4);
		System.out.println (sbl);
	}
}
*/
public class EjercicioStrings {
	public static void main(String args[]) {
		StringBuilder sbl = new StringBuilder("0123456");
		sbl.replace(2,4,"ABCD");
		System.out.println (sbl);
	}
}
