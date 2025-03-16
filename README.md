# UML Class Diagram Generator

This is a Python-based UML Class Diagram Generator that uses **Graphviz** to visually represent the class structure of a system.

## Features
- Automatically generates UML class diagrams from Python class definitions.
- Displays class attributes, methods, inheritance, and relationships.
- Produces high-resolution diagrams suitable for documentation or presentations.

---

## Requirements
- Python 3.6 or higher
- **Graphviz** installed on your system (ensure the `dot` command is accessible in your system's PATH).

---

## Steps to Set Up a Python Virtual Environment

### 1. Navigate to Your Project Directory
Run the following command to navigate to your project folder:
```bash
cd /path/to/your/project
```

### 2. Create and Activate a Virtual Environment
#### For Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

#### For macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Required Python Libraries
Install the `graphviz` library in your virtual environment:
```bash
pip install graphviz
```

---

## Example Usage

### 1. Add the Class Data to a Python File
Create a Python file named `classes_data.py` with the following content:
```python
classes = {
    'User': {
        'attributes': ['- int: user_id', '- String: username', '- String: password', '- String: name', '- String: email', '- String: contact_details', '- String: profile_picture'],
        'methods': ['+ getName(): String', '+ setName(name: String): void', '+ getEmail(): String', '+ setEmail(email: String): void', '+ getProfilePicture(): String', '+ setProfilePicture(pic: String): void'],
        'related_classes': ['Course', 'Attendance', 'Marks', 'Notice']
    },
    'Admin': {
        'attributes': [],
        'methods': ['+ createUserProfile(): void', '+ updateUserProfile(): void', '+ createCourse(): void', '+ updateCourse(): void', '+ createNotice(): void', '+ updateNotice(): void', '+ createTimetable(): void', '+ updateTimetable(): void'],
        'inherits': 'User',
        'related_classes': ['Course', 'Attendance', 'Marks', 'Notice']
    },
    'Lecturer': {
        'attributes': [],
        'methods': ['+ updateProfileExceptPassword(): void', '+ modifyMaterials(): void', '+ uploadMarks(): void', '+ viewUndergraduateDetails(): void', '+ viewEligibility(): void', '+ viewMarksAndGPA(): void', '+ viewAttendanceAndMedical(): void', '+ viewNotices(): void'],
        'inherits': 'User',
        'related_classes': ['Course', 'Attendance', 'Marks', 'Notice']
    },
    'TechnicalOfficer': {
        'attributes': [],
        'methods': ['+ updateProfileExceptPassword(): void', '+ addAttendanceDetails(): void', '+ updateAttendanceDetails(): void', '+ addMedicalDetails(): void', '+ updateMedicalDetails(): void', '+ viewNotices(): void', '+ viewTimetables(): void'],
        'inherits': 'User',
        'related_classes': ['Course', 'Attendance', 'Marks', 'Notice']
    },
    'Student': {
        'attributes': ['- int: student_id', '- float: CA_marks', '- float: attendance_percentage', '- boolean: eligible_for_final_exam'],
        'methods': [
            '+ updateContactDetails(): void',
            '+ updateProfilePicture(): void',
            '+ viewAttendanceDetails(): void',
            '+ viewMedicalDetails(): void',
            '+ viewCourseDetails(): void',
            '+ viewGradesAndGPA(): void',
            '+ viewTimetable(): void',
            '+ viewNotices(): void',
            '+ calculateAttendancePercentage(): void',
            '+ checkEligibilityForFinalExam(): boolean',
            '+ calculateSGPA(): float',
            '+ calculateCGPA(): float'
        ],
        'inherits': 'User',
        'related_classes': ['Course', 'Attendance', 'Marks', 'Medical', 'Notice']
    },
    'Course': {
        'attributes': ['- int: course_id', '- String: course_name', '- boolean: has_practical', '- int: total_sessions', '- int: credit_hours', '- float: CA_percentage_required'],
        'methods': ['+ getCourseName(): String', '+ getTotalSessions(): int', '+ hasPractical(): boolean', '+ checkCAEligibility(student_id: int): boolean'],
        'related_classes': ['Student', 'Attendance', 'Marks', 'Notice']
    },
    'Attendance': {
        'attributes': ['- int: attendance_id', '- int: student_id', '- int: course_id', '- date: attendance_date', '- boolean: attended', '- boolean: medical'],
        'methods': ['+ getAttendanceDate(): date', '+ getAttendanceStatus(): boolean', '+ getMedicalStatus(): boolean', '+ calculateAttendancePercentage(): void'],
        'related_classes': ['Student', 'Course']
    },
    'Marks': {
        'attributes': ['- int: course_id', '- int: student_id', '- float: Quiz_01', '- float: Quiz_02', '- float: Quiz_03', '- float: Assesment_01', '- float: Assesment_02', '- float: Assesment_03', '- int: MidExam', '- int: FinalExam'],
        'methods': ['+ uploadMarks(): void', '+ AddQuizMark(): void', '+ AddAssesmentMark(): void'],
        'related_classes': ['Course', 'Student']
    },
    'Department': {
        'attributes': ['+ DepartmentID: String', '+ DepartmentName: String', '+ HODID: String'],
        'methods': ['+ UpdateHODID(): void'],
        'related_classes': ['Lecturer', 'TechnicalOfficer']
    },
    'Notice': {
        'attributes': ['+ NoticeID: String', '+ Title: String', '+ DateTime: DateTime', '+ FilePath: String', '+ Description: String'],
        'methods': ['+ createCourse(): void', '+ deleteCourse(): void', '+ editCourse(): void', '+ AddNotice(): void', '+ RemoveNotice(): void'],
        'related_classes': ['Admin', 'Lecturer', 'Student']
    },
    'Medical': {
        'attributes': ['- int: medical_id', '- date: start_date', '- date: end_date'],
        'methods': ['+ getMedicalDetails(): String', '+ getMedicalDuration(): String'],
        'related_classes': ['Student']
    },
    'Timetable': {
        'attributes': ['+ StartTime: String', '+ EndTime: String', '+ Level: String', '+ DepartmentID: String'],
        'methods': [],
        'related_classes': ['Department']
    }
}
```

### 2. Use the UML Diagram Generator Script
Create a script to generate the UML diagram based on the `classes_data.py` file. For example:
```python
from graphviz import Digraph
from classes_data import classes

def generate_uml(data):
    dot = Digraph('UML Diagram', format='png')
    dot.attr(rankdir='BT')

    for class_name, details in data.items():
        attributes = '\l'.join(details.get('attributes', []))
        methods = '\l'.join(details.get('methods', []))
        label = f"{{ {class_name} | {attributes}\l | {methods}\l }}"
        dot.node(class_name, shape='record', label=label)

        if 'inherits' in details:
            dot.edge(details['inherits'], class_name, arrowhead='onormal')

        for related in details.get('related_classes', []):
            dot.edge(class_name, related, arrowhead='diamond')

    return dot

uml_diagram = generate_uml(classes)
uml_diagram.render('output/uml_diagram', cleanup=True)
```

### 3. Run the Script
Execute the script to generate the UML diagram:
```bash
py main.py
```

### 4. View the Output
Check the `output` directory for the `uml_diagram.png` file containing your class diagram.

---

## Troubleshooting

- **Error: `'dot' is not recognized as an internal or external command`**
  - Ensure that Graphviz is installed and added to your system's PATH.

- **Graphviz Installation**
  - Download Graphviz from [Graphviz Download Page](https://graphviz.org/download/).
  - Follow the installation instructions for your operating system.

---
