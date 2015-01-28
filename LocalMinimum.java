/*
You are given an array of distinct numbers. You need to return an index to a "local minimum" element, 
which is defined as an element that is smaller than both its adjacent elements. 
In the case of the array edges, the condition is reduced to one adjacent element. 
Reach a solution with better time complexity than the trivial solution of O(n). 

If there are multiple "local minimums", returning any one of them is fine.
*/

public class LocalMinimum{
	public int localMinimum(int [] arr, int left, int right){
		if(left == right) return left;
		if(right - left == 1) {
			if(arr[left] < arr[right])
				return left;
			else
				return right;
		}
		int mid = left + (right - left) / 2;
		int result = -1;

		if(arr[mid - 1] > arr[mid] && arr[mid + 1] > arr[mid])
		{
			result = mid;
		}
		else{
			if(arr[mid - 1] < arr[mid])
			{
				result = localMinimum(arr, left, mid - 1);
			}
			else if(arr[mid + 1] < arr[mid])
			{
				result = localMinimum(arr, mid + 1, right);
			}
		}
		System.out.println (result);
		System.out.println ("---");
		return result;
	}
	public static void main(String [] args){
		LocalMinimum c = new LocalMinimum();
		int [] test = new int[7];
		test[0] = 11;
		test[1] = 5;
		test[2] = 12;
		test[3] = 7;
		test[4] = 6;
		test[5] = 4;
		test[6] = 1;
		System.out.println(c.localMinimum(test, 0, test.length - 1));
	}
}