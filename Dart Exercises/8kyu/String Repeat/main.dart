// Function was sent to CodedWars
String repeatString2(int n, String s) => s * n;

// Best Way
final repeatString = (int n, String s) => s * n;

void main(List<String> args) {
  final texto = repeatString2(3, "Hola");
  final texto2 = repeatString(3, "Hola");
  print(texto);
  print(texto2);
}
