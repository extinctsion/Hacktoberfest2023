public class UniqueMinimumProductSubarray {

    public static void main(String[] args) {
        int[] nums = {1, -2, -3, 0, 7, -8, -2};
        int minProduct = findMinimumProductSubarray(nums);
        System.out.println("Minimum product subarray is: " + minProduct);
    }

    public static int findMinimumProductSubarray(int[] nums) {
        int n = nums.length;
        int minEndingHere = 1;
        int maxEndingHere = 1;
        int minProduct = Integer.MAX_VALUE;

        	for (int num : nums) {
            if (num > 0) {
                maxEndingHere = Math.max(maxEndingHere * num, 1);
                minEndingHere = Math.min(minEndingHere * num, 1);
            } else if (num == 0) {
                maxEndingHere = 1;
                minEndingHere = 1;
            } else {
                int temp = maxEndingHere;
                maxEndingHere = Math.max(minEndingHere * num, 1);
                minEndingHere = temp * num;
            }
            if (minProduct > minEndingHere) {
                minProduct = minEndingHere;
            }
        }

        return minProduct;
    }
}
