# README for Spam Detection REST API

## Overview
This project implements a REST API for a spam detection application, designed to be consumed by a mobile app. The API allows users to:

1. Register and manage their profiles.
2. Mark phone numbers as spam.
3. Search for people by name or phone number.
4. Access details about search results, including spam likelihood.

The application is built using Django with a relational database for persistence.

---

## Features

### 1. User Registration and Profile Management
- Users can register with their **name**, **phone number**, and **password** (email is optional).
- Only one user can register with a particular phone number.
- Users must be logged in to access any API endpoints.

### 2. Spam Reporting
- Users can mark any phone number as spam.
- Spam markings are stored in the global database and used to calculate spam likelihood.

### 3. Search Functionality
#### Search by Name
- Returns all matching results (complete or partial matches).
- Results prioritize names starting with the search query over those containing the query.
- Each result includes the name, phone number, and spam likelihood.

#### Search by Phone Number
- If a registered user exists for the number, only that result is shown.
- If no registered user exists, all entries matching the number are returned (names can vary due to multiple users’ contacts).
- Email is displayed only if the searched user is registered and the searcher is in their contact list.

### 4. Data Population
- Includes a script to populate the database with random sample data using the **Faker** library.

---

## Technologies Used
- **Language/Framework:** Python/Django
- **Database:** PostgreSQL (recommended) or SQLite (for development)
- **Libraries:**
  - Django REST Framework (DRF) for API implementation
  - Faker for generating sample data
- **Authentication:** Token-based authentication using Django REST Framework’s authentication system

---

## API Endpoints

### User Authentication
- **Register:** `/api/register/`
- **Login:** `/api/login/`
- **Logout:** `/api/logout/`

### Spam Management
- **Mark as Spam:** `/api/spam/mark/`
  - Payload: `{ "phone_number": "<number>" }`

### Search
- **Search by Name:** `/api/search/name/`
  - Query Parameters: `?query=<name>`
- **Search by Phone Number:** `/api/search/phone/`
  - Query Parameters: `?number=<phone_number>`

---

## Database Schema
### User
- **id**: Primary Key
- **name**: String
- **phone_number**: Unique String
- **email**: String (optional)
- **password**: Hashed String

### Contact
- **id**: Primary Key
- **name**: String
- **phone_number**: String
- **user**: Foreign Key to User (indicating the owner of the contact)

### Spam
- **id**: Primary Key
- **phone_number**: String
- **reported_by**: Foreign Key to User (indicating who marked it as spam)

---

## Setup Instructions

### Prerequisites
- Python (>=3.8)
- Django (>=4.0)
- PostgreSQL (optional but recommended)

### Installation Steps
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd spam-detection-api
   ```

2. Set up a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the database:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Populate the database with sample data:
   ```bash
   python manage.py populate_data
   ```

6. Start the development server:
   ```bash
   python manage.py runserver
   ```

---

## Data Population Script
The `populate_data` command generates random users, contacts, and spam reports using the **Faker** library:

1. **Random Users:**
   - Name, phone number, email, and password are randomly generated.

2. **Contacts:**
   - Each user gets a random set of contacts, with names and phone numbers generated using Faker.

3. **Spam Reports:**
   - Random phone numbers are marked as spam.

To run the script:
```bash
python manage.py populate_data
```

---

## Testing
Run the following command to execute unit tests:
```bash
python manage.py test
```

---

## Security Features
- Passwords are hashed using Django’s authentication system.
- Token-based authentication for secure API access.
- Input validation to prevent SQL injection and other attacks.

---

## Next Steps
- Implement rate limiting for API endpoints.
- Add email verification for new users.
- Optimize database queries for scalability.

---

## Conclusion
This REST API serves as the backend for a spam detection application. It provides robust features for user registration, spam marking, and contact search while adhering to best practices for performance, security, and code structure.

