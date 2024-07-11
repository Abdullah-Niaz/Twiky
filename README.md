# Twiky

Twiky is a social media web application built using Django, a high-level Python web framework. Users can register, log in, and post tweets, similar to Twitter. This project demonstrates the use of Django for web development, including user authentication, form handling, and database interactions.

## Features

- User registration and authentication
- Posting tweets
- Viewing a list of tweets
- Simple and clean user interface

## Requirements

- Python 3.6+
- Django 3.2+
- SQLite (default database)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Abdullah-Niaz/Twiky.git
    cd Twiky
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Apply the migrations:

    ```bash
    python manage.py migrate
    ```

5. Create a superuser to access the Django admin:

    ```bash
    python manage.py createsuperuser
    ```

6. Start the development server:

    ```bash
    python manage.py runserver
    ```

7. Open your web browser and go to `http://127.0.0.1:8000/` to see the application in action.

## Usage

### Register

- Go to the registration page at `/accounts/register/`.
- Fill in the registration form and submit it.
- You will be logged in automatically after registration.

### Login

- Go to the login page at `/accounts/login/`.
- Enter your credentials and submit the form.
- You will be redirected to the homepage.

### Post a Tweet

- Once logged in, you can post a tweet from the homepage.
- Enter your tweet content and submit the form.

### View Tweets

- You can view all tweets on the homepage.
- Tweets are displayed in reverse chronological order.

## Project Structure

- `accounts/` - Contains the user authentication views, forms, and URLs.
- `tweets/` - Contains the views, models, and URLs related to tweets.
- `templates/` - Contains the HTML templates for the application.
- `static/` - Contains the static files (CSS, JS, images).

## Contributing

Contributions are welcome! Please create an issue or submit a pull request for any changes or improvements.

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Make your changes and commit them.
4. Push your changes to your forked repository.
5. Create a pull request to the main repository.


## Acknowledgements

- [Django Documentation](https://docs.djangoproject.com/en/stable/)
- [Bootstrap](https://getbootstrap.com/) - for the front-end framework
