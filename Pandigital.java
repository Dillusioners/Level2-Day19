

public class Pandigital {

    //Method to check if a number is prime
    public static boolean isPrime(long n) {  
        if (n <= 1) {  
            return false;  
        }  
        for (long i = 2; i < Math.sqrt(n); i++) {  
            if (n % i == 0) {  
                return false;  
            }  
        }  
        return true;  
    }  
  //method to split a number into an array of its digits
	static long[] arr_return(long num,int len)
	{
		
		long[] digs = new long[len];
		int counter = 0;
		while(num >= 1)
		{
			digs[counter] = num % 10;
			num /= 10;
			counter++;
		}
		return digs;
	}
    //method to check if a number is pandigital
	static boolean is_pandigital(long num)
	{
		int lent = Long.toString(num).length();
		long[] digits_of_num = arr_return(num,lent);
		for(int i=1; i <= lent; i++)
		{
			int dig_cnt = 0;
			for(int j=0;j<lent;j++)
			{
				if(digits_of_num[j] == i)
					++dig_cnt;
				
			}
            if(dig_cnt != 1)
					return false;
		}
		return true;
	}
    //Method to find the answer
    public static void solve()
    {
        long max = 0;
        for(long i=1000000; i<=9999999; i++)
        {
            long temp = i; 
            if(isPrime(i) && is_pandigital(temp)){
                max = i;
            }
        }
        System.out.println(max);
        //System.out.println(max);
    }
    
	public static void main(String[] args){
		solve();
	}

}
