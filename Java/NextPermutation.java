import java.util.Collections;
import java.util.List;
import java.util.ListIterator;

public class NextPermutation {
    public void nextPermutation(int[] nums) {
        int i;
        for (i = nums.length - 1; i > 0; i--)
            if (nums.get(i) > nums.get(i - 1))
                break;
        if (i != 0) {
            List<Integer> subList = nums.subList(nums.size() - i, nums.size());
            ListIterator<Integer> it = subList.listIterator(subList.size());
            while (it.hasPrevious()) {
                if (it.previous() > nums.get(i - 1)) {
                    Collections.swap(nums, i - 1, nums.size() - subList.size() + it.nextIndex());
                    break;
                }
            }
        }
        Collections.reverse(nums.subList(i, nums.size()));

    }

    public static void main(String[] args) {
        NextPermutation obj = new NextPermutation();
        int[] nums = { 1, 2, 3 };
        obj.nextPermutation(nums);
        for (int i : nums)
            System.out.print(i + " ");
    }
}


// code explanation
// The code iterates through the list of numbers, and if a number is greater than the previous number in the list, it swaps that number with the last one.
//The code iterates through all of the numbers in a list until it finds an index where two consecutive numbers are not equal.
//Then it swaps those two numbers so that they are next to each other.
//The code iterates through the list of numbers and swaps the current number with the one before it if that number is greater than the previous.