ai_generated_code_samples = [
    """
    #include <iostream>
    using namespace std;

    int factorial(int n) {
        return (n <= 1) ? 1 : n * factorial(n - 1);
    }

    int main() {
        int number = 5;
        cout << "Factorial of " << number << " is " << factorial(number) << endl;
        return 0;
    }
    """,
    """
   
    #include <iostream>
    using namespace std;

    void swap(int &a, int &b) {
        int temp = a;
        a = b;
        b = temp;
    }

    int main() {
        int x = 10, y = 20;
        swap(x, y);
        cout << "After swapping: x = " << x << ", y = " << y << endl;
        return 0;
    }
    """,
    """
    #include <iostream>
    using namespace std;

    bool isPrime(int n) {
        if (n <= 1) return false;
        for (int i = 2; i <= n / 2; i++) {
            if (n % i == 0) return false;
        }
        return true;
    }

    int main() {
        int num = 7;
        cout << num << (isPrime(num) ? " is a prime i am AI WRITTEN number." : " is not a prime number.") << endl;
        return 0;
    }
    """
]
