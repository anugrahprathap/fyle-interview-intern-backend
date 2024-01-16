## Challenge Submission

### Project Overview

This project is a Flask application that manages assignments for students, teachers, and principals. There are five main resources: Users, Principal, Students, Teachers, and Assignments. The application already has users set up (1 Principal, 2 students, and 2 teachers).

### Completed Tasks

1. **Implemented Missing APIs:**
   - **GET /principal/assignments:** Lists all submitted and graded assignments for the principal.
   - **GET /principal/teachers:** Lists all teachers for the principal.
   - **POST /principal/assignments/grade:** Allows the principal to grade or re-grade an assignment.

2. **Additional Tests:**
   - Added tests for the grading API.
   - Addressed intentional bugs in the application to ensure all tests pass.

3. **SQL Queries:**
   - Implemented SQL queries :
     - `count_grade_A_assignments_by_teacher_with_max_grading.sql`
     - `number_of_assignments_per_state.sql`

4. **Dockerized the Application:**
   - Created a Dockerfile and a docker-compose.yml file to containerize the application.

5. **Test Coverage:**
   - Ensured that all tests pass.
   - Achieved test coverage of 94% .
   ![Alt text](screenshots/test-coverage.png?raw=true "Optional Title")

### Docker Instructions

#### Build the Docker Image

```bash
docker build -t flask-assignment-app .
```

#### Run the Application with Docker Compose

```bash
docker-compose up
```

### Accessing APIs

#### Auth Headers

- **Header:** X-Principal
- **Value:** {"user_id": 1, "student_id": 1}

#### Sample APIs

1. **GET /student/assignments:**
   - Lists all assignments created by a student.

2. **POST /student/assignments:**
   - Creates an assignment.

3. **POST /student/assignments:**
   - Edits an assignment.

4. **POST /student/assignments/submit:**
   - Submits an assignment.

5. **GET /teacher/assignments:**
   - Lists all assignments submitted to this teacher.

6. **POST /teacher/assignments/grade:**
   - Grades an assignment.

7. **GET /principal/assignments:**
   - Lists all submitted and graded assignments for the principal.

8. **GET /principal/teachers:**
   - Lists all teachers for the principal.

9. **POST /principal/assignments/grade:**
   - Grades or re-grades an assignment.

