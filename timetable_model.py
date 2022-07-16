import classes_model as classes

teachers = [
    classes.teacher("Tatiana", "Voropaeva"),
    classes.teacher("Neethu", "Joseph"),
    classes.teacher("Grace", "Howarth"),
    classes.teacher("Reece", "Geursen"),
    classes.teacher("Cassie", "Swinerd"),
]

subjects = {
    "DTC": classes.subject("13DTC", "Computer Science", teachers[0]),
    "MAX": classes.subject("13MAX", "Statistics", teachers[1]),
    "ENG": classes.subject("13ENG", "English", teachers[2]),
    "PHX": classes.subject("13PHX", "Physics", teachers[3]),
    "BIO": classes.subject("13BIO", "Biology", teachers[4]),
}

monday = classes.days_subjects("Monday", classes.subject_instance())
tuesday = classes.days_subjects("Tuesday", classes.subject_instance())
wednesday = classes.days_subjects("Wednesday", classes.subject_instance())
thursday = classes.days_subjects("Thursday", classes.subject_instance())
friday = classes.days_subjects("Friday", classes.subject_instance())

timetable = [monday, tuesday, wednesday, thursday, friday]
