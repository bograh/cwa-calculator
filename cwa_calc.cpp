#include <iostream>

using namespace std;

void CWA() {
	string course_code_letters;
	int course_code_num;
	int credits;
	double midsem_score;
	double end_of_sem_score;
	int total_credits;
	total_credits = 0;
	int num_of_courses;

	cout << "Enter number of courses to calculate CWA: ";
	cin >> num_of_courses;

	for (int i = 0; i < num_of_courses; i++)
	{
		cout << "Enter course code: ";
		cin >> course_code_letters >> course_code_num;
		cout << "Enter credit hours for " << course_code_letters << " " << course_code_num << ": ";
		cin >> credits;
		cout << "Enter midsem score (30%): ";
		cin >> midsem_score;
		cout << "Enter End of sem score (70%): ";
		cin >> end_of_sem_score;

		total_credits += credits;
	}
	
	cout << total_credits;
}


int main()
{
	
	cout << "WELCOME TO CWA CALCULATOR !!" << endl;
	cout << "*****************************" << endl;

	// int total_credits = 0;
	// int num_of_courses;

	// cout << "Enter number of courses to calculate CWA: ";
	// cin >> num_of_courses;

	// for (int i = 1; i <= num_of_courses; i++) {
	// 	CWA();
	// }

	CWA();



	return 0;
}