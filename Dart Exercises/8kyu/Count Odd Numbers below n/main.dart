/**
 * Things to think:
 * In this exercise I realized that using for statement is faster than
 * using Filters (Where Filter).
 */


// Function Sent to CodedWars. It's Fast, but not so much.
int oddCount(int n) {
  int count = 0;
  final list = List.generate(n, (index) => index);
  for (var num in list) {
    if (num.isOdd) count++;
  }
  return count;
}

// This is other way to solve the problem, but it's slower
int oddCount2(int n) {
  final count = List.generate(n, ((index) => index))
      .where((element) => element.isOdd)
      .length;
  return count;
}

// Best Practice and Faster
/**
 * * Why is this the best way?
 * ! When the quantity of odd or even numbers is required,
 * ! this value is the half of the last number.
 * ! Formula: First "n" numbers -> (n~/2)+1 even | (n~/2) odd
 * !        Where: ' ~/ ' -> truncate number
 * ! Example
 * ! 13 -> 7 even | 6 odd
 */
int oddCountBest(int n) => n ~/ 2;


void main(List<String> args) {
  int cantidad1 = oddCount(1);
  int cantidad = oddCountBest(1);
  // int cantidad2 = oddCount2(9666131);
  print(cantidad);
  print(cantidad1);
  // print(cantidad2);
}
