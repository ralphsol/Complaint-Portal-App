## Populate DB Script

## clear database
for table in db.tables():
	try:
		db(db[table].id>0).delete()
		print "Cleared",table
	except Exception, e:
		print "Couldn't clear",table

## create 3 students
db.users.insert(
	first_name="Saiesvar",  # Kumaon
	last_name="Vipparathy",
	email="cs1140266@cse.iitd.ac.in",
	username="cs1140266",
	entry_no="2014CS10266",
	type_=0,
	password="saiesvar",
)

db.users.insert(
	first_name="Harshil",   # Girnar
	last_name="Meena",
	email="cs1140222@cse.iitd.ac.in",
	username="cs1140222",
	entry_no="2014CS10222",
	type_=0,
	password="harshil",
)

db.users.insert(
	first_name="Nagaraju",  # Girnar
	last_name="Ajmeera",
	email="cs1140208@cse.iitd.ac.in",
	username="cs1140208",
	entry_no="2014CS10208",
	type_=0,
	password="nagaraju",
)


## create 2 wardens + 1 dean

db.users.insert(
	first_name="Warden",
	last_name="Kumaon",
	email="wardenkumaon@cse.moodle.in",
	username="wardenkumaon",
	entry_no="wardenkumaon",
	type_=1,
	password="wardenkumaon",
)

db.users.insert(
	first_name="Warden",
	last_name="Girnar",
	email="wardengirnar@cse.iitd.ac.in",
	username="wardengirnar",
	entry_no="wardengirnar",
	type_=1,
	password="wardengirnar",
)


db.users.insert(
	first_name="Dean",
	last_name="Student Welfare",
	email="dean@cse.iitd.ac.in",
	username="dean",
	entry_no="dean",
	type_=1,
	password="dean",
)

## create 3 individual courses + 2 hostel courses + 1 insti course
db.courses.insert(
	name="saiesvarcourse",
	code="saiesvarcourse",
	description="none",
	credits=3,
	l_t_p="none"
)

db.courses.insert(
	name="harshilcourse",
	code="harshilcourse",
	description="none",
	credits=3,
	l_t_p="none"
)

db.courses.insert(
	name="nagarajucourse",
	code="nagarajucourse",
	description="none",
	credits=3,
	l_t_p="none"
)

db.courses.insert(
	name="kumaoncourse",
	code="kumaoncourse",
	description="none",
	credits=3,
	l_t_p="none"
)

db.courses.insert(
	name="girnarcourse",
	code="girnarcourse",
	description="none",
	credits=3,
	l_t_p="none"
)

db.courses.insert(
	name="iitcourse",
	code="iitcourse",
	description="none",
	credits=3,
	l_t_p="none"
)



## create 7 registered courses
db.registered_courses.insert(	
	course_id=1,
	professor=1,
	year_=2016,
	semester=2,
	starting_date=datetime(2016,1,1),
	ending_date=datetime(2016,5,10),
)

db.registered_courses.insert(
	course_id=2,
	professor=2,
	year_=2016,
	semester=2,
	starting_date=datetime(2016,1,1),
	ending_date=datetime(2016,5,10),
)

db.registered_courses.insert(
	course_id=3,
	professor=3,
	year_=2016,
	semester=2,
	starting_date=datetime(2016,1,1),
	ending_date=datetime(2016,5,10),
)

db.registered_courses.insert(
	course_id=4,
	professor=4,
	year_=2016,
	semester=2,
	starting_date=datetime(2016,1,1),
	ending_date=datetime(2016,5,10),
)

db.registered_courses.insert(
	course_id=5,
	professor=5,
	year_=2016,
	semester=2,
	starting_date=datetime(2016,1,1),
	ending_date=datetime(2016,5,10),
)

db.registered_courses.insert(
	course_id=6,
	professor=6,
	year_=2016,
	semester=2,
	starting_date=datetime(2016,1,1),
	ending_date=datetime(2016,5,10),
)


## register 3 students for 5 courses each out of 7 registered courses
db.student_registrations.insert(student_id=1,registered_course_id=4)
db.student_registrations.insert(student_id=2,registered_course_id=5)
db.student_registrations.insert(student_id=3,registered_course_id=5)
db.student_registrations.insert(student_id=1,registered_course_id=6)
db.student_registrations.insert(student_id=2,registered_course_id=6)
db.student_registrations.insert(student_id=3,registered_course_id=6)



## Create Static Variables
db.static_vars.insert(
	name="current_year",
	int_value=2016,
	string_value="2016"
)

db.static_vars.insert(
	name="current_sem",
	int_value=2,
	string_value="2"
)
