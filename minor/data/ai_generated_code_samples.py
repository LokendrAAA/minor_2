ai_generated_codes = [
    """
    #include <iostream>
    
    int main() {
        // Create a variable to store the message
        std::string outputMessage = "Hello from AI!";
        
        // Output the message to the console
        std::cout << outputMessage << std::endl;
        
        // Exit the program
        return 0;
    }
    """,

    """
    #include <iostream>
    
    int multiplyTwoNumbers(int numberOne, int numberTwo) {
        // Temporary variable to store multiplication result
        int resultOfMultiplication = numberOne * numberTwo;
        return resultOfMultiplication; // Return result
    }
    
    int main() {
        int a = 5;
        int b = 10;
        int product = multiplyTwoNumbers(a, b);
        
        // Print the result
        std::cout << "Product: " << product << std::endl;
        return 0;
    }
    """,

    """
    #include <iostream>
    
    int sumOfFirstNNumbers(int N) {
        // Initialize the sum to zero
        int sumTotal = 0;
        
        // Loop to calculate the sum
        for (int i = 1; i <= N; i++) {
            sumTotal += i; // Add i to the sum
        }
        return sumTotal; // Return the calculated sum
    }
    
    int main() {
        int N = 100;
        std::cout << "Sum of first " << N << " natural numbers is: " << sumOfFirstNNumbers(N) << std::endl;
        return 0;
    }
    """,

    """
    #include <iostream>
    
    int findMaximumOfThreeNumbers(int numOne, int numTwo, int numThree) {
        // Determine which number is the greatest
        if (numOne >= numTwo && numOne >= numThree) {
            return numOne;
        } else if (numTwo >= numOne && numTwo >= numThree) {
            return numTwo;
        } else {
            return numThree;
        }
    }
    
    int main() {
        int a = 15, b = 20, c = 5;
        std::cout << "The maximum number is: " << findMaximumOfThreeNumbers(a, b, c) << std::endl;
        return 0;
    }
    """,

    """
    #include <iostream>
    
    int findSquareOfNumber(int inputNumber) {
        // Squaring the input number
        return inputNumber * inputNumber;
    }
    
    int main() {
        int number = 7;
        std::cout << "Square of " << number << " is: " << findSquareOfNumber(number) << std::endl;
        return 0;
    }
    """,

    """
    #include <iostream>
    
    bool isNumberEven(int numberToCheck) {
        // Use modulo operator to check if the number is even
        if (numberToCheck % 2 == 0) {
            return true; // Number is even
        } else {
            return false; // Number is odd
        }
    }
    
    int main() {
        int num = 9;
        if (isNumberEven(num)) {
            std::cout << num << " is even." << std::endl;
        } else {
            std::cout << num << " is odd." << std::endl;
        }
        return 0;
    }
    """,

    """
    #include <iostream>
    
    int calculateFibonacci(int fibonacciIndex) {
        if (fibonacciIndex <= 1) {
            return fibonacciIndex;
        }
        // Recursive call for calculating the Fibonacci number
        return calculateFibonacci(fibonacciIndex - 1) + calculateFibonacci(fibonacciIndex - 2);
    }
    
    int main() {
        int index = 6;
        std::cout << "Fibonacci number at index " << index << " is: " << calculateFibonacci(index) << std::endl;
        return 0;
    }
    """,

    """
    #include <iostream>
    
    int calculateAreaOfRectangle(int lengthOfRectangle, int widthOfRectangle) {
        // Calculate and return the area
        return lengthOfRectangle * widthOfRectangle;
    }
    
    int main() {
        int length = 12;
        int width = 8;
        std::cout << "The area of the rectangle is: " << calculateAreaOfRectangle(length, width) << std::endl;
        return 0;
    }
    """,

    """
    #include <iostream>
    
    int main() {
        // Loop from 10 down to 1
        for (int i = 10; i >= 1; --i) {
            std::cout << i << std::endl; // Print the value of i
        }
        std::cout << "Countdown complete!" << std::endl;
        return 0;
    }
    """,

    """
    #include <iostream>
    
    double calculateAverageOfArray(int arrayOfNumbers[], int sizeOfArray) {
        int sum = 0;
        for (int i = 0; i < sizeOfArray; i++) {
            sum += arrayOfNumbers[i]; // Add each element to the sum
        }
        return static_cast<double>(sum) / sizeOfArray; // Return the average
    }
    
    int main() {
        int numbers[] = {2, 4, 6, 8, 10};
        std::cout << "Average: " << calculateAverageOfArray(numbers, 5) << std::endl;
        return 0;
    }
    """,

    """
    #include <iostream>
    #include <string>
    
    std::string reverseString(const std::string& inputString) {
        std::string reversedString = "";
        for (int i = inputString.length() - 1; i >= 0; --i) {
            reversedString += inputString[i];
        }
        return reversedString;
    }
    
    int main() {
        std::string myString = "AI code generation";
        std::cout << "Reversed string: " << reverseString(myString) << std::endl;
        return 0;
    }
    """,

    """
    #include <iostream>
    
    std::string determineGrade(int score) {
        if (score >= 90) {
            return "A";
        } else if (score >= 80) {
            return "B";
        } else if (score >= 70) {
            return "C";
        } else {
            return "F";
        }
    }
    
    int main() {
        int score = 85;
        std::cout << "Grade: " << determineGrade(score) << std::endl;
        return 0;
    }
    """,

    """
    #include <iostream>
    
    double convertCelsiusToFahrenheit(double temperatureInCelsius) {
        return (temperatureInCelsius * 9.0 / 5.0) + 32.0; // Convert to Fahrenheit
    }
    
    int main() {
        double celsius = 25.0;
        std::cout << "Temperature in Fahrenheit: " << convertCelsiusToFahrenheit(celsius) << std::endl;
        return 0;
    }
    """,

    """
    #include <iostream>
    
    int calculateSumOfArrayElements(int arr[], int size) {
        int totalSum = 0;
        for (int i = 0; i < size; i++) {
            totalSum += arr[i]; // Add each element to the sum
        }
        return totalSum; // Return the total sum
    }
    
    int main() {
        int myArray[] = {1, 2, 3, 4, 5};
        std::cout << "Sum of array elements: " << calculateSumOfArrayElements(myArray, 5) << std::endl;
        return 0;
    }
    """,

    """
    #include <iostream>
    #include <string>
    
    int countVowelsInString(const std::string& inputString) {
        int vowelCount = 0;
        for (char c : inputString) {
            if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' ||
                c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U') {
                vowelCount++;
            }
        }
        return vowelCount;
    }
    
    int main() {
        std::string input = "Artificial Intelligence";
        std::cout << "Number of vowels: " << countVowelsInString(input) << std::endl;
        return 0;
    }
    """,

    """
    #include <iostream>
    
    bool isPrimeNumber(int number) {
        if (number <= 1) return false;
        for (int i = 2; i < number; i++) {
            if (number % i == 0) return false;
        }
        return true;
    }
    
    int main() {
        int number = 29;
        if (isPrimeNumber(number)) {
            std::cout << number << " is a prime number." << std::endl;
        } else {
            std::cout << number << " is not a prime number." << std::endl;
        }
        return 0;
    }
    """,

    """
    #include <iostream>
    #include <string>
    
    std::string concatenateStrings(const std::string& firstString, const std::string& secondString) {
        return firstString + " " + secondString; // Concatenate the two strings
    }
    
    int main() {
        std::string first = "Hello";
        std::string second = "World";
        std::cout << "Concatenated string: " << concatenateStrings(first, second) << std::endl;
        return 0;
    }
    """,

    """
    #include <iostream>
    
    int factorial(int number) {
        if (number < 0) return -1; // Negative numbers don't have factorials
        if (number == 0) return 1; // Base case
        return number * factorial(number - 1); // Recursive call
    }
    
    int main() {
        int num = 5;
        std::cout << "Factorial of " << num << " is: " << factorial(num) << std::endl;
        return 0;
    }
    """,

    """
    #include <iostream>
    
    void swapTwoNumbers(int& numOne, int& numTwo) {
        int temp = numOne;
        numOne = numTwo;
        numTwo = temp;
    }
    
    int main() {
        int a = 5, b = 10;
        std::cout << "Before swap: a = " << a << ", b = " << b << std::endl;
        swapTwoNumbers(a, b);
        std::cout << "After swap: a = " << a << ", b = " << b << std::endl;
        return 0;
    }
    """,

    """
    #include <iostream>
    
    double calculateSimpleInterest(double principalAmount, double rateOfInterest, double timePeriod) {
        return (principalAmount * rateOfInterest * timePeriod) / 100; // Simple interest formula
    }
    
    int main() {
        double principal = 1000.0, rate = 5.0, time = 3.0;
        std::cout << "Simple Interest: " << calculateSimpleInterest(principal, rate, time) << std::endl;
        return 0;
    }
    """
]
