# taskmanagement

# Task Management API

This is a Django-based API for user and task management. The API allows you to:
- Create users
- Retrieve a list of users
- Create tasks and assign them to users
- Retrieve tasks assigned to a specific user

## Endpoints

### User Endpoints
1. **Create User**  
   `POST /users/create/`  
   Body (JSON):
   ```json
   {
     "name": "John Doe",
     "email": "john.doe@example.com",
     "mobile": "1234567890"
   }
Get User List
GET /users/
Task Endpoints

Create Task
POST /tasks/create/
Body (JSON):

json

{
  "name": "Task 1",
  "description": "Task description",
  "task_type": "development",
  "status": "pending"
}

Assign Users to Task
POST /tasks/<task_id>/assign/
Body (JSON):
json
{
  "user_ids": [1, 2, 3]
}


Retrieve User Tasks
GET /users/<user_id>/tasks/

Models
Customuser
name: CharField (max_length=255)
email: EmailField (unique=True)
mobile: CharField (max_length=15, blank=True, null=True)


Task
name: CharField (max_length=255)
description: TextField
created_at: DateTimeField (auto_now_add=True)
task_type: CharField (max_length=50)
completed_at: DateTimeField (null=True, blank=True)
status: CharField (max_length=50)
assigned_users: ManyToManyField(Customuser)
