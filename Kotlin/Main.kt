fun bubbleSort(numbers: IntArray) {
    for (pass in 0 until (numbers.size - 1)) {
        // A single pass of bubble sort
        for (currentPosition in 0 until (numbers.size - 1)) {
            // This is a single step
            if (numbers[currentPosition] > numbers[currentPosition + 1]) {
                val tmp = numbers[currentPosition]
                numbers[currentPosition] = numbers[currentPosition + 1]
                numbers[currentPosition + 1] = tmp
            }
        }
    }
}

fun main() {
    val numbers: IntArray = intArrayOf(10, 20, 30, 40, 50,54,3253,236,2,2)
    println("Before"+ numbers.joinToString  (","))

    bubbleSort(numbers)
    println("Sorted"+ numbers.joinToString  (","))

}
