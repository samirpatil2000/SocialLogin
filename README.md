## Installation steps

1. Ensure you have python installed

2. Clone the repository `https://gitlab.com/rkritikapaul17/sociallogin.git`
3. create a virtual environment using `python -m venv venv`
4. Activate the virtual environment by running `source venv/bin/activate`

- On Windows use `source venv\Scripts\activate`

5. Install the dependencies using `pip install -r requirements.txt`

6. Migrate existing db tables by running `python manage.py migrate`

7. Run the django development server using `python manage.py runserver`