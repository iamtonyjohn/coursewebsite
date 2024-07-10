# coursewebsite
Courses Website with Django A feature-rich courses website using Django, offering login, signup, course listings, detailed descriptions, and booking. Videos are locked/unlocked after payment via Razorpay. Secure user authentication and seamless payment integration for an optimal learning experience.

Here's a GitHub repository description for your courses website built with Django, including all the specified functionalities:

---

## Courses Website with Django

This repository contains the source code for a feature-rich courses website built using Django. The application offers a robust platform for users to explore and enroll in various courses, with integrated payment and content management functionalities.

### Key Features

- **User Authentication**
  - **Login**: Secure login functionality for returning users.
  - **Signup**: Easy registration process for new users.

- **Course Management**
  - **Courses**: A comprehensive listing of available courses.
  - **Book Now**: Simple and efficient course booking system.
  - **Show More**: Detailed course descriptions, including instructors, curriculum, and reviews.

- **Video Content**
  - **Locked/Unlocked Videos**: Course videos are locked until payment is made.
  - **Video Playback**: High-quality video streaming for enrolled users.

- **Payment Gateway**
  - **Razorpay Integration**: Secure and seamless payment processing through Razorpay.

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/courses-website-django.git
   cd courses-website-django
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure the database**:
   - Update the `settings.py` file with your database credentials.
   - Run migrations:
     ```bash
     python manage.py migrate
     ```

4. **Configure Razorpay**:
   - Update `settings.py` with your Razorpay API keys.

5. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

6. **Access the application**:
   Open your browser and navigate to `http://127.0.0.1:8000`.

### Usage

- **User Registration**: Sign up for a new account to start using the platform.
- **Browse Courses**: Explore the available courses and view detailed descriptions.
- **Book a Course**: Select a course and complete the booking process.
- **Make a Payment**: Use Razorpay to securely pay for the selected course.
- **Access Content**: Unlock and view course videos after successful payment.

### Contributing

We welcome contributions from the community. To contribute, please fork the repository, create a new branch, and submit a pull request with your changes.

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---
