class person():
    def __init__(self, name, age, contact_number):
        self.name = name
        self.age = age
        self.contact_number = contact_number
    
    def set_details(self, name, age, contact_number):
        self.name = name
        self.age = age
        self.contact_number = contact_number
    
    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}, Contact Number: {self.contact_number}"
    
class member(person):
    def __init__(self, name, age, gender, membership_id, sport, performance_score):
        super().__init__(name, age, gender)
        self.membership_id = membership_id
        self.sport = sport
        self.performance_score = performance_score
    
    def set_member_details(self, membership_id, sport):
        self.membership_id = membership_id
        self.sport = sport
    
    def add_performance_score(self, score):
        for i in score:    
            self.performance_score.append(i)
    
    def calculate_average_score(self):
        return sum(self.performance_score) / len(self.performance_score)
    
    def get_member_summary(self):
        return f"Name: {self.name}, Age: {self.age}, Contact Number: {self.contact_number}, Average_score: {self.calculate_average_score()}"
    
class coach(person):
    def __init__(self, name, age, gender, coach_id, specialisation, salary):
        super().__init__(name, age, gender)
        self.coach_id = coach_id
        self.specialisation = specialisation
        self.salary = salary
        self.mentees = []
        self.mentorship_group = []
    
    def set_coach_details(self, coach_id, specialisation, salary):
        self.coach_id = coach_id
        self.specialisation = specialisation
        self.salary = salary
    
    def assign_mentee(self, member):
        self.mentees.append(member)
        print(f"Coach {self.name} is now mentoring {member.name} in {member.sport}.")
    
    def get_mentees(self):
        output = []
        for i in self.mentees:
            output.append([i.name, i.sport])
        return output
    
    def increase_salary(self, percentage):
        self.salary *= (percentage/100 + 1)
    
    def mentor_coach(self, coach):
        self.mentorship_group.append(coach)
        print(f"Coach {self.name} is now mentoring Coach {coach.name} in {coach.specialisation}.")
    
    def get_mentorship_group(self):
        output = []
        for i in self.mentorship_group:
            output.append([i.name, i.specialisation])
        return output
    
class staff(person):
    def __init__(self, name, age, gender, staff_id, position, years_of_service):
        super().__init__(name, age, gender)
        self.staff_id = staff_id
        self.position = position
        self.years_of_service = years_of_service
    
    def set_staff_details(self, staff_id, position, years_of_service):
        self.staff_id = staff_id
        self.position = position
        self.years_of_service = years_of_service
    
    def increment_service_years(self):
        self.years_of_service += 1
    
    def assist_member(self, member):
        print(f"Staff {self.name} assisted {member.name} in resolving an issue.")
    
    def get_staff_summary(self):
        return f"Name: {self.name}, Age: {self.age}, Contact Number: {self.contact_number}, Years of service: {self.years_of_service}"
    
Doug = member("Doug", 19, "Male", 12345, "Tennis", [2])
Dog = member("Dog", 8, "Male", 12346, "Woofleball", [1])

Douglas = coach("Douglas", 24, "Male", 12345, "Tennis", 12345)
Douglette = coach("Douglette", 28, "Female", 12346, "Wiffleball", 10000)

Dougie = staff("Dougie", "unknown", "unknown", "refused", "Receptionist", 7)

Douglas.assign_mentee(Doug)

Dog.add_performance_score([2, 1, 4, 5])

Dougie.assist_member(Doug)

Douglette.increase_salary(15)

Dougie.increment_service_years()

print(Doug.get_member_summary(), Dog.get_member_summary(), Douglas.get_details(), Douglette.get_details(), Dougie.get_staff_summary())

Douglas.mentor_coach(Douglette)

print(Douglas.get_mentees())
print(Douglas.get_mentorship_group())