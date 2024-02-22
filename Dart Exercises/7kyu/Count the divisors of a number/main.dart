// This function was sent to Codewars
int divisors(int n) {
  int numDivisors = 0;
  
  for (var divisor = 1; divisor <= n; divisor++) {
    if (n % divisor == 0) {
      // print('Divisor: ${divisor}');
      numDivisors++;
    }
    continue;
  }
  return numDivisors;
}

// Best Way
// User Built-In Methods is faster than for statement
int divisors2(n) => List<int>.generate(n, (i) => i + 1)
                        .where((element) => n%element == 0)
                        .length;

void main(List<String> args) {
  final divisores = divisors(20);
  final divisores2 = divisors2(20);
  print(divisores);
  print(divisores2);
}
