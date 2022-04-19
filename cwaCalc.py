'''
AUTHOR	->	BERNARD OGRAH
DATE	->	16th APRIL, 2022
PROGRAM	->	THIS IS A PROGRAM TO CALCULATE THE CUMULATIVE WEIGHTED AVERAGE OF A STUDENT AT KNUST.
'''
import os

########## ~ CHECKS IF THE FILE FOR THE RESULTS EXISTS OR NOT ~ ##########

filename = 'Results/cwaResults.txt'
file_csv = 'Results/cwaResults.csv'

if os.path.exists(filename) or os.path.exists(file_csv):
    append_write = 'a' # append if already exists
else:
    append_write = 'w' # make a new file if not

##########################################################################


########## ~ FUNCTION FOR FILE CONTROL ~ ##########

def files():
	global f_csv
	global file
	file = open(filename, append_write)
	f_csv = open(file_csv, append_write)

###################################################


########## ~ FUNTION CONTAINING WELCOME MESSAGE ~ ##########

def main():
	print("WELCOME TO THE CWA CALCULATION APP")
	print("**********************************\n")

############################################################


########## ~ FUNCTION CONTAING CODES FOR THE MAIN FUNCTIONALITY OF THE APP ~ ##########
def CWA():
	num_of_semester = int(input("Enter number of semesters completed: "))
	while num_of_semester < 0:
		num_of_semester = int(input("Enter a valid number of semesters comleted: "))
	
	global total_credits
	total_credits = 0
	global overall_total
	overall_total = 0
	average_sum = 0

	# Loop through the number of semesters entered
	for no_semester in range(1, num_of_semester+1):
		print(f"Semester {no_semester}")
		print("************************")
		n = int(input(f"Enter number of courses for semester {no_semester}: "))
		while n < 0: #To ensure the user enters a valid number of courses per semester
			n = int(input(f"Invalid number of courses for semester {no_semester} entered!!\nRe-enter a valid number of courses for semester {no_semester}"))
		
		# Loop through the number of courses for every semester
		for i in range(1, n+1):
			course_code = str(input("Enter course code: "))
			credits = int(input(f"Enter number of credits for {course_code}: "))
			while credits < 0 or credits > 4:
				credits = int(input(f"Invalid credits entered!!\nRe-enter number of credits: "))
			
			# Accept result for mid semester exams and validate
			midsem_exam_score = float(input("Enter marks for midsem exams (out of 30): "))
			while midsem_exam_score < 0 or midsem_exam_score > 30:
				print("Mid semester exam score is out of range!!")
				midsem_exam_score = float(input("Re-enter a score for mid semester exams (out of 30):"))

			# Accept result for end of semester exams and validate
			end_of_sem_exam_score = float(input("Enter marks for end of semester exam (out of 70): "))
			while end_of_sem_exam_score < 0 or end_of_sem_exam_score > 70:
				print("End of semester exam score is out of range!!")
				end_of_sem_exam_score = float(input("Re-enter a score for end of semester exams (out of 70):"))
			
	###########Calculations for the Cumulative Weighted Average - CWA #############			

			end_of_sem_total = midsem_exam_score + end_of_sem_exam_score
			overall_total = overall_total + end_of_sem_total

			total_credits = total_credits + credits

			product_sum = credits * (end_of_sem_total)

			average_sum = average_sum + product_sum
		print("\n")
	

	global cumulative_weighted_average
	cumulative_weighted_average = average_sum / total_credits


#####################################################################################################################
	print("\n")


#################### ~ THIS BLOCK CONTAINS CODE FOR INDIVIDUAL STUDENT CREDENTIALS ~ ####################

def studentCredentials():
	num_of_students = int(input("Enter number of sudents to calculate CWA: "))
	while num_of_students < 0:
		num_of_students = int(input("Number of stuedents entered is Invalid!!\nRe-enter number of students to calculate CWA: "))

	print("\n")

	def tabularResults():
		for student in range(1, num_of_students+1):
			indexNo = int(input("Enter student index number: "))
			CWA()

			##### GRADING SYSTEM ######
			if cumulative_weighted_average >= 70:
				grade = "First Class"
			elif cumulative_weighted_average >= 60:
				grade = "Second Class Upper"
			elif cumulative_weighted_average >= 50:
				grade = "Second Class Lower"
			elif cumulative_weighted_average >= 40:
				grade = "Third Class"
			elif cumulative_weighted_average >= 30:
				grade = "Pass"
			else:
				grade = "Fail"
			###########################
			print("INDEX NUMBER\tFINAL TOTAL SCORE\tTOTAL CREDITS\t   C W A\t\t GRADE\n")
			print("************\t*****************\t*************\t   *****\t\t *****\n")
			print(f" {indexNo}\t\t     {overall_total}\t\t {total_credits}\t\t   {round(cumulative_weighted_average, 2)}\t\t   {grade}\n")

		
			########### ~ THIS BLOCK WRITES THE RESULTS TO A TEXT FILE ~ ##########
			if append_write == 'w':
				file.write(
					"INDEX NUMBER\tFINAL TOTAL SCORE\tTOTAL CREDITS\t   C W A\t\t GRADE\n"
					"************\t*****************\t*************\t   *****\t\t *****\n"
					f" {indexNo}\t\t     {overall_total}\t\t {total_credits}\t\t   {round(cumulative_weighted_average, 2)}\t\t   {grade}\n"
					)
			elif append_write == 'a':
				file.write(
					f" {indexNo}\t\t     {overall_total}\t\t {total_credits}\t\t   {round(cumulative_weighted_average, 2)}\t   {grade}\n"
					)

			#######################################################################
		
			########### ~ THIS BLOCK WRITES THE RESULTS TO A CSV FILE ~ ##########
			if append_write == 'w':
				f_csv.write(
					"INDEX NUMBER,FINAL TOTAL SCORE,TOTAL CREDITS,C W A,GRADE\n"
					f" {indexNo},{overall_total},{total_credits},{round(cumulative_weighted_average, 2)},{grade}\n"
					)
			elif append_write == 'a':
				f_csv.write(
					f" {indexNo},{overall_total},{total_credits},{round(cumulative_weighted_average, 2)},{grade}\n"
					)
	
			######################################################################
		
	tabularResults()

#########################################################################################################


########## ~ FUNCTION CALLS ~ ##########

files()

if __name__ == '__main__':
	main()

studentCredentials()

########################################