
public class Main
{
	/*
	 * Evaluates various properties of a set of three double values
	 */
	
	
	// Tests smallest, largest, average, allThSame, and allDifferent
	public static void main(String[] args) {
		System.out.println(smallest (3.5, 6.7, -8.5)); // expect -8.5
		System.out.println(smallest (3.5, 6.7, 3.5)); // expect 3.5
		System.out.println(smallest (10.5, 6.7, 0.0) ); // expect 0.0
		
		System.out.println(largest (3.5, 6.7, -8.5));  // expect 6.7
		System.out.println(largest (3.5, 6.7, 3.5));  // expect 6.7
		System.out.println(largest (10.5, 6.7, 0.0));  // expect 10.5
		
		System.out.println(average (3.5, 6.7, -8.5)); // expect 0.5666666666666664
		System.out.println(average (1.0, 1.0, 1.0)); // expect 1.0
		System.out.println(average (1.0, 0.0, 1.0)); // expect 0.6666666666666666
		
		System.out.println(allTheSame (3.5, 6.7, -8.5)); // expect False
		System.out.println(allTheSame (1.0, 1.0, 0.0)); // expect False
		System.out.println(allTheSame (1.0, 1.0, 1.0)); // expect True
		
		System.out.println(allDifferent (3.5, 6.7, -8.5)); // expect True
		System.out.println(allDifferent (1.0, 1.0, 0.0)); // expect False
		System.out.println(allDifferent (1.0, 1.0, 1.0)); // expect False

	}
	
	public static Double smallest(Double numZero, Double numOne, Double numTwo) {
		/*
		 * This method takes three double values as parameters and
		 *  returns the smallest value of the three. 
		 */
		Double result = numZero;
		if (numOne < result) {
			result = numOne;
		} 
		if (numTwo < result) {
			result = numTwo;
		}
		
		return result;
		
	}
	
	public static Double largest(Double numZero, Double numOne, Double numTwo) {
		/*
		 * This method takes three double values as parameters and 
		 * returns the largest value of the three
		 */
		Double result = numZero;
		if (numOne > result) {
			result = numOne;
		} 
		if (numTwo > result) {
			result = numTwo;
		}
		
		return result;
	}
	
	public static Double average(Double numZero, Double numOne, Double numTwo) {
		/*
		 * This method takes three double values as parameters and 
		 * returns the average of the three. 
		 */
		return ((numZero + numOne + numTwo) / 3.0);
		
	}
	
	public static Boolean allTheSame(Double numZero, Double numOne, Double numTwo) {
		/*
		 * This method returns True if all three double values sent in as parameters are of equal value, and 
		 * returns False if at least one of the three double values is different from the other two
		 */

		return ((Math.abs(numZero - numOne) < 0.00001) && (Math.abs(numZero - numTwo) < 0.00001));
		
	}
	
	public static Boolean allDifferent(Double numZero, Double numOne, Double numTwo) {
		/*
		 *  This method returns True if all three double values sent in as parameters have different values, and 
		 *  returns False if at least two of the three doubles are of equal value.   
		 */
		return ((Math.abs(numZero - numOne) > 0.00001) && (Math.abs(numZero - numTwo) > 0.00001) 
				&& (Math.abs(numOne - numTwo) > 0.00001));
		
	}

	
}


/* ======= OUTPUT ========

-8.5
3.5
0.0
6.7
6.7
10.5
0.5666666666666664
1.0
0.6666666666666666
false
false
true
true
false
false

*/


