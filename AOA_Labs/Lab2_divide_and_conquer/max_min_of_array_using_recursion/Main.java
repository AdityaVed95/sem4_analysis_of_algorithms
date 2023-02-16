import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

// testing_in_java
public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter size of list: ");
        int sizeOfList = sc.nextInt();
        List<Integer> list1 = new ArrayList<Integer>();
        for (int i = 0; i < sizeOfList; i++) {
            list1.add((int) (Math.random() * 1000000000000L));
        }

        long start = System.nanoTime();
        int[] minMax = findMinMax(list1, 0, list1.size() - 1);
        long end = System.nanoTime();

        System.out.println("Using Recursive using Divide and Conquer Approach : ");
        System.out.println("Minimum number is : " + minMax[0] + " and Maximum number is : " + minMax[1]);
        System.out.println("Time taken for finding max and min no of list using divide conquer using recursion is : " + (end - start) + " ns");

        start = System.nanoTime();
        int[] basicMinMax = findMinMaxUsingBasicApproach(list1);
        end = System.nanoTime();

        System.out.println("Now using Basic Approach without divide and conquer");
        System.out.println("Minimum number is : " + basicMinMax[0] + " and Maximum number is : " + basicMinMax[1]);
        System.out.println("Time taken for finding max and min no of list using basic approach is : " + (end - start) + " ns");
    }

    private static int[] findMinMax(List<Integer> listSearch, int low, int high) {
        if (low == high) {
            return new int[]{listSearch.get(low), listSearch.get(low)};
        } else if (low == high - 1) {
            if (listSearch.get(low) > listSearch.get(high)) {
                return new int[]{listSearch.get(high), listSearch.get(low)};
            } else {
                return new int[]{listSearch.get(low), listSearch.get(high)};
            }
        } else {
            int mid = (low + high) / 2;
            int[] leftMinMax = findMinMax(listSearch, low, mid);
            int[] rightMinMax = findMinMax(listSearch, mid + 1, high);

            int min = Math.min(leftMinMax[0], rightMinMax[0]);
            int max = Math.max(leftMinMax[1], rightMinMax[1]);

            return new int[]{min, max};
        }
    }

    private static int[] findMinMaxUsingBasicApproach(List<Integer> listSearch) {
        int min = listSearch.get(0);
        int max = listSearch.get(0);
        for (int i = 1; i < listSearch.size(); i++) {
            int currentNum = listSearch.get(i);
            if (currentNum < min) {
                min = currentNum;
            }
            if (currentNum > max) {
                max = currentNum;
            }
        }

        return new int[]{min, max};
    }
}
