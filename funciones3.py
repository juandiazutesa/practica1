def salaryweek(hrs, salaryhr, job):
    salary = hrs * salaryhr
    salary = salary * 7
    print ("El sueldo de un ",job, "es ", salary)
salaryweek(8, 284, "Doctor")
salaryweek(4, 10, "Jardinero")