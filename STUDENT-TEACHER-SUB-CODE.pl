% Facts: student(StudentID, Name)
student(101, alice).
student(102, bob).
student(103, carol).
student(104, david).

% Facts: teacher(TeacherID, Name)
teacher(201, emily).
teacher(202, frank).
teacher(203, grace).

% Facts: subject(SubjectCode, SubjectName)
subject(301, math).
subject(302, science).
subject(303, history).

% Facts: teaches(TeacherID, SubjectCode)
teaches(201, 301).
teaches(202, 302).
teaches(203, 303).

% Facts: enrolled(StudentID, SubjectCode)
enrolled(101, 301).
enrolled(101, 302).
enrolled(102, 302).
enrolled(103, 303).
enrolled(104, 301).
enrolled(104, 303).

% Queries
% Find all students enrolled in a subject taught by a specific teacher
students_enrolled_in_subject(TeacherID, SubjectCode, StudentName) :-
    teaches(TeacherID, SubjectCode),
    enrolled(StudentID, SubjectCode),
    student(StudentID, StudentName).

% Find all subjects a student is enrolled in
subjects_enrolled_for_student(StudentID, SubjectName) :-
    enrolled(StudentID, SubjectCode),
    subject(SubjectCode, SubjectName).

% Find all teachers who teach a specific student
teachers_for_student(StudentID, TeacherName) :-
    enrolled(StudentID, SubjectCode),
    teaches(TeacherID, SubjectCode),
    teacher(TeacherID, TeacherName).
