import java.util.ArrayList;
import java.util.Collections; import java.util.Comparator;
import java.util.List;
/| Define a Student class to represent a student
class Student {
String name;
String rollNumber;
double cgpa;
public Student(String name, String
rollNumber, double cgpa) {
this.name = name;
this.rollNumber = rollNumber;
this.cgpa = cgpa;
}
public class Main {
/| Comparator to compare students based on CGPA
public static Comparator<Student> cgpaComparator = new Comparator<Student>() {
public int compare(Student s1, Student s2) {
if (s1.cgpa > s2.cgpa) {
return 1;
} else if (s1.cgpa < s