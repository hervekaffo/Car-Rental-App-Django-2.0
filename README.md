# final-project herve Kaffo
- This is a car renting Application Implemented using Python (Django), Sqlite3, JavaScripcrip(Jquery) where a user can rent or post a car for renting.
- Working Functionalities 
	1. 	A new user Can resister to the application by creating an account 
	2 Email account validation : In order to validate your account the user should click the link he received by email
		*notice: I logged in the registered user directly for testing time purposes for the grader although you can still check you email and validate your account.  
	3. A registered user can at any time logout with a logout confirmation
	4. A registered user can reset his password on the login windows
	    *notice: This is also thought an email link the application send to the user 
	5. A registered user can also access the account setting on the account dashboard where he can add, reverify, or remove his existing email account 
	6. The application has a pagination feature on the list of cars at the home page 
	7. Any site visitor can search for Available cars for rent either by the city, Car specifications. he can also order by the most recent added car (JavaScript touch) 
	8. Any site visitor can also see the prices for different cars available 
	10. A registered user can post a vehicle for rent and set the daily renting price 
	11. A registered user can rent a car for a desired period of time 

- Attempted and non working Functionalities
	I am still working on the following functionalities and was not able to implement those within the time frame given for the project
	1. I added but did not tested a translation module using I18N
	2. setup the location for any added car so that users can search near by cars for rent 
	3. Process the payment 
	4. provide the user information on how to get the car he rented 

		Notices: 
	- the texts on the car list look blurry on Google Chrome I don't know why. They look alright on Mozilla Firefox and IE  

- References
  1. www.w3schools.com
  2. CSCI E-33a Lectures, sessions and source code
  3. gunicorn activcar.wsgi:application --preload
  
  
  Thanks to the CS-50's Teaching Staff for all the knowledges they gave me absolutely a great plus om how I will develop application 
