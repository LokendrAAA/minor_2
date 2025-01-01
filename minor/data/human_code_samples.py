human_codes = [
    """
    #include <iostream>
    int main() {
        std::cout << "Hello World!";
        return 0;
    }
    """,
    
    """
    #include <iostream>
    int add(int a, int b) {
        return a + b;
    }
    int main() {
        std::cout << add(5, 3);
        return 0;
    }
    """,
    
    """
    #include <iostream>
    void printMessage() {
        std::cout << "C++ is fun!";
    }
    int main() {
        printMessage();
        return 0;
    }
    """,
    
    """
    #include <iostream>
    int main() {
        int arr[] = {1, 2, 3, 4, 5};
        for (int i = 0; i < 5; ++i) {
            std::cout << arr[i] << " ";
        }
        return 0;
    }
    """,
    
    """
    #include <iostream>
    int main() {
        for (int i = 1; i <= 10; ++i) {
            std::cout << i * i << " ";
        }
        return 0;
    }
    """,
    
    """
    #include <iostream>
    int main() {
        int a = 10, b = 20, temp;
        temp = a;
        a = b;
        b = temp;
        std::cout << "a: " << a << ", b: " << b;
        return 0;
    }
    """,
    
    """
    #include <iostream>
    int main() {
        int num;
        std::cout << "Enter a number: ";
        std::cin >> num;
        if (num % 2 == 0)
            std::cout << "Even";
        else
            std::cout << "Odd";
        return 0;
    }
    """,
    
    """
    #include <iostream>
    int main() {
        int sum = 0;
        for (int i = 1; i <= 100; ++i) {
            sum += i;
        }
        std::cout << "Sum: " << sum;
        return 0;
    }
    """,
    
    """
    #include <iostream>
    int main() {
        int factorial = 1, n;
        std::cout << "Enter a number: ";
        std::cin >> n;
        for (int i = 1; i <= n; ++i) {
            factorial *= i;
        }
        std::cout << "Factorial: " << factorial;
        return 0;
    }
    """,
    
    """
    #include <iostream>
    int main() {
        int arr[] = {10, 20, 30, 40};
        int* p = arr;
        std::cout << *p << " " << *(p + 1);
        return 0;
    }
    """,

    """
    #include <iostream>
    int main() {
        std::string str = "C++ Programming";
        std::cout << "Length: " << str.length();
        return 0;
    }
    """,

    """
    #include <iostream>
    void swap(int& a, int& b) {
        int temp = a;
        a = b;
        b = temp;
    }
    int main() {
        int x = 5, y = 10;
        swap(x, y);
        std::cout << "x: " << x << ", y: " << y;
        return 0;
    }
    """,

    """
    #include <iostream>
    int main() {
        std::string s1 = "Hello", s2 = "World";
        std::string s3 = s1 + " " + s2;
        std::cout << s3;
        return 0;
    }
    """,

    """
    #include <iostream>
    int main() {
        int arr[] = {2, 4, 6, 8, 10};
        int* ptr = arr;
        for (int i = 0; i < 5; ++i) {
            std::cout << *(ptr + i) << " ";
        }
        return 0;
    }
    """,

    """
    #include <iostream>
    int main() {
        int n;
        std::cout << "Enter a number: ";
        std::cin >> n;
        for (int i = 1; i <= 10; ++i) {
            std::cout << n << " x " << i << " = " << n * i << "\\n";
        }
        return 0;
    }
    """,

    """
    #include <iostream>
    int main() {
        int a, b;
        std::cout << "Enter two numbers: ";
        std::cin >> a >> b;
        std::cout << "Sum: " << a + b;
        return 0;
    }
    """,

    """
    #include <iostream>
    int main() {
        int a = 5, b = 7;
        int max = (a > b) ? a : b;
        std::cout << "Max: " << max;
        return 0;
    }
    """,

    """
    #include <iostream>
    int main() {
        char grade;
        std::cout << "Enter your grade (A/B/C): ";
        std::cin >> grade;
        switch (grade) {
            case 'A': std::cout << "Excellent"; break;
            case 'B': std::cout << "Good"; break;
            case 'C': std::cout << "Fair"; break;
            default: std::cout << "Invalid";
        }
        return 0;
    }
    """,

    """
    #include <iostream>
    int main() {
        int num = 12345, reversed = 0;
        while (num != 0) {
            int digit = num % 10;
            reversed = reversed * 10 + digit;
            num /= 10;
        }
        std::cout << "Reversed: " << reversed;
        return 0;
    }
    """,

    """
    #include <iostream>
    int fibonacci(int n) {
        if (n <= 1) return n;
        return fibonacci(n - 1) + fibonacci(n - 2);
    }
    int main() {
        int n;
        std::cout << "Enter a number: ";
        std::cin >> n;
        std::cout << "Fibonacci: " << fibonacci(n);
        return 0;
    }
    """
]
