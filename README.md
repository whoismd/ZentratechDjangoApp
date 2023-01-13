# ZentratechDjangoApp

Make sure you have Django and the necessary dependencies installed.
In your project's root directory, run the command python manage.py runserver to start the development server.
In your browser, navigate to localhost:8000
A form should be displayed on the page where you can enter a Flipkart listing page URL
After submitting the form, the view function will scrape the data from the page and save it in the corresponding fields of the model, then it will redirect you to the home page
You can check the scraped data in the admin page.



Create a new Django app using the command django-admin startapp scraper

The url_scraper.py is a new route in the app's urls.py file that will accept a URL as a parameter

The models.py and views.py file is for the logic of scraping and store the scraped data.

The print.py is created in the app's templates folder to display the scraped data

The testcase.py is the code for creating testcases



