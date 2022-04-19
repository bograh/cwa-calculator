#include <iostream>
#include <string>

using namespace std;


int main()
{
	int num_of_students;
	int indexNO;
	string grade;
	string course_code;
	int credits;
	double midsem_score;
	double end_of_sem_score;
	int total_credits;
	total_credits = 0;
	int num_of_courses;
	int num_of_semesters;
	double end_of_sem_total;
	double overall_total;
	overall_total = 0;
	double product_sum;
	double average_sum;
	average_sum = 0;
	double cumulative_weighted_average;


	cout << "WELCOME TO CWA CALCULATOR !!" << endl;
	cout << "*****************************" << endl;

	cout << "Enter number of students to calculate CWA: ";
	cin >> num_of_students;
	while (num_of_students < 0) {
		cout << "Number of stuedents entered is Invalid!!\nRe-enter number of students to calculate CWA: ";
		cin >> num_of_students;
	}
	cout << "\n";

	for (int student = 1; student <= num_of_students; student++) {
		cout << "Enter student index number: ";
		cin >> indexNO;

		cout << "Enter number of semesters: ";
		cin >> num_of_semesters;
		while (num_of_semesters < 0) {
			cout << "Enter a valid number of semesters completed: ";
			cin >> num_of_semesters;
		}

		for (int i = 1; i <= num_of_semesters; i++) {
			cout << "\nSemester " << i << endl;
			cout << "**********" << endl;
			cout << "Enter number of courses for semester " << i << ": ";
			cin >> num_of_courses;
			while (num_of_courses < 0) {
				cout << "Invalid number of courses for semester " << i << " entered!!\nRe-enter a valid number of courses for semester " << i << ": ";
			}
		
			for (int j = 1; j <= num_of_courses; j++) {
				cout << "Enter course code: ";
				cin.ignore();
				getline(cin, course_code);
				cout << "Enter credit hours for " << course_code << ": ";
				cin >> credits;
				while (credits < 0) {
					cout << "Invalid credits entered \nRe-enter the credit hours: ";
					cin >> credits;
				}
				cout << "Enter midsem score (out of 30): ";
				cin >> midsem_score;
				while (midsem_score < 0 || midsem_score > 30) {
					cout << "Mid semester exam score is out of range! \nRe-enter midem exam score (out of 30): ";
					cin >> midsem_score;
				}
				cout << "Enter End of sem score (out of 70): ";
				cin >> end_of_sem_score;
				while (end_of_sem_score < 0 || end_of_sem_score > 70) {
					cout << "End of semester exam score is out of range! \nRe-enter midem exam score (out of 70): ";
					cin >> end_of_sem_score;
				}

				end_of_sem_total = midsem_score + end_of_sem_score;
				overall_total += end_of_sem_total;

				product_sum = credits * end_of_sem_total;

				total_credits += credits;

				average_sum += product_sum;
			}
			cout << "\n";
	

		cumulative_weighted_average = average_sum / total_credits;

		if (cumulative_weighted_average >= 70) {
			grade = "First Class";
		} else if (cumulative_weighted_average >= 60) {
			grade = "Second Class Upper";
		} else if (cumulative_weighted_average >= 50) {
			grade = "Second Class Lower";
		} else if (cumulative_weighted_average >= 40) {
			grade = "Third Class";
		} else if (cumulative_weighted_average >= 30) {
			grade = "Pass";
		} else {
			grade = "Fail";
		}

		cout << indexNO << endl;
		cout << overall_total << endl;
		cout << total_credits << endl;
		cout << cumulative_weighted_average << endl;
		cout << grade << endl;
		
		}
	
	}

	return 0;
}