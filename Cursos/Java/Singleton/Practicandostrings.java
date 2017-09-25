public class Practicandostrings {
	public static void main(String args[]) {
		String letters = "ABCAB";
		System.out.println(letters.startsWith("AB"));
		System.out.println(letters.startsWith("a"));
		System.out.println(letters.startsWith("A", 3));
		System.out.println(letters.startsWith("CAB"));
		System.out.println(letters.startsWith("B"));
		System.out.println(letters.startsWith("b"));
	}
}

