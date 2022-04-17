'''
AUTHOR	->	BERNARD OGRAH
DATE	->	16th APRIL, 2022
PROGRAM	->	THIS IS A PROGRAM TO CALCULATE THE CUMULATIVE WEIGHTED AVERAGE OF A STUDENT AT KNUST.
'''


########## ~ FUNCTION FOR FILE CONTROL ~ ##########

def files():
	global f
	global file
	global f_add
	global file_add

	# file = open('cwa.txt', 'w')
	# f = open('cwa.csv', 'w')
	file_add = open('cwa.txt', 'a')
	f_add = open('cwa.csv', 'a')

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
	weighted_average = 0
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

			global end_of_sem_total_score

			end_of_sem_total_score = midsem_exam_score + end_of_sem_exam_score
			total_credits = total_credits + credits

			product_sum = credits * (end_of_sem_total_score)

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

			print("INDEX NUMBER\tEND OF SEM SCORE\tTOTAL CREDITS\t   C W A\t GRADE\n")
			print("************\t****************\t*************\t   *****\t *****\n")
			print(f" {indexNo}\t\t     {end_of_sem_total_score}\t\t {total_credits}\t\t   {round(cumulative_weighted_average, 2)}\t\t {grade}\n")

		
			########### ~ THIS BLOCK WRITES THE RESULTS TO A TEXT FILE ~ ##########

			file_add.write(
				# "INDEX NUMBER\tEND OF SEM SCORE\tTOTAL CREDITS\t   C W A\t GRADE\n"
				# "************\t****************\t*************\t   *****\t *****\n"
				f" {indexNo}\t\t     {end_of_sem_total_score}\t\t {total_credits}\t\t   {round(cumulative_weighted_average, 2)}\t\t {grade}\n"
				)

			#######################################################################
		
			########### ~ THIS BLOCK WRITES THE RESULTS TO A CSV FILE ~ ##########

			f_add.write(
				# "INDEX NUMBER,END OF SEM SCORE,TOTAL CREDITS,C W A,GRADE\n"
				f" {indexNo},{end_of_sem_total_score},{total_credits},{round(cumulative_weighted_average, 2)},{grade}\n"
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