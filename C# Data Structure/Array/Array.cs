
using System;
using System.Collections.Generic;

namespace Data_Structure.Array
{
    public static class ArrayStr
    {
        public static int[] nums = new int[] {1,2,3,4,5,6,7};
        public static int target = 5;
        public static void ArrayTest()
        {
   
        string[] weekDays = new string[]{
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday"
        };
        string weekDayConCat = "";
        
        for(int i = 0; i< weekDays.Length; i++){
            weekDayConCat += weekDays[i] + '-';
        }
        
        string reverseWeek= "";
        // reverse arrays
        for(int i = weekDays.Length-1; i>0; i--){
           reverseWeek += weekDays[i] + '-';
        }
        Console.WriteLine($"Reverse String : {reverseWeek}");
        Console.WriteLine(weekDayConCat);
        
        Console.WriteLine(weekDayConCat);
        Console.WriteLine($"Array Length: {weekDays.Length}");
        }
        public static void MultiDimensionalArrayTest()
        {
            int[, ] twoDimArray = new int[,]
            {
                {1,2},
                {3,4},
                {5,6}
            };
            int [, , ] threDimArray = new int[, , ]{
                {
                    {1,2,3},
                    {4,3,2},
                    {2,3,4}            
                }
        };

        // access 2 dim arrays with
        for(int i =0; i<3; i++){
            for(int j=0;j<2;j++){
                Console.WriteLine("2D Array Test"+ twoDimArray[i,j]);
            }
        }
    }
    
        public static void JaggedArrayTest(){
            //declare 
            int[][] jaggedArray = new int [4][];
            //Initialize int
            jaggedArray[0] = new int[] {1,2,3,4};
            jaggedArray[1] = new int[] {5,6,7,8};
            jaggedArray[2] = new int[] {9,10,11,12};
            jaggedArray[3] = new int[] {13,14,15,16};

            // print rows and columns 
            for(int i = 0; i < jaggedArray.Length; i++)
             {
                //print row numbers
                Console.WriteLine("Row {0}", i);
                string[] conCatInts = new string[jaggedArray[i].Length];

                for(int j = 0; j < jaggedArray[i].Length; j++)
                {
                    conCatInts[j] += jaggedArray[i][j].ToString();
                    //Console.WriteLine("{0}", jaggedArray[i][j]);
                }
                Console.WriteLine(string.Join(",", conCatInts));
            }

        }
        
        public static int BinarySearch(int[] nums, int target)
        {
            int low =0;
            int high = nums.Length - 1;
            while(low<=high)
            {
                int mid = low + (high-low/2);
                if(nums[mid] == target){
                    return mid;
                }
                else if (nums[mid]<target){
                    low =  mid+1;
                }
                else high = mid-1;
            }
            return low;
        }

        public static int ConvertRomantoInteger(string s)
        {
            int sum = 0;
            // MCMCIV
            var dic = new Dictionary<char, int>()
            {
                {'I', 1},
                {'V', 5},
                {'X', 10},
                {'L', 50},
                {'C', 100},
                {'D', 500},
                {'M', 1000}
            };
            for (int i=0; i< s.Length; i++)
            {
                char currentRomanChar = s[i]; // M
                dic.TryGetValue(currentRomanChar, out int num); // 1000
                if(i+1 < s.Length && dic[s[i+1]]> dic[currentRomanChar])
                {
                    sum -= num;
                }
                else
                {
                    sum += num;
                }
            }
            return sum;
        }
    }
}
