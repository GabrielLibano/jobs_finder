# Job Data Scraper
#### This project is a web scraping tool that uses Selenium and the SerpAPI to scrape job listings and salary information from Glassdoor and Google Jobs. The project also uses the Pandas library to create and store the data in a .xlsx and .json file.

## Getting Started
#### These instructions will help you to run the project on your local machine for development and testing purposes.

## Prerequisites
#### You will need to have the following software installed on your machine:

* Python 3.x
* Selenium
* SerpAPI
* Pandas
* Selenium
* dotenv
* You will also need to have an API key from SerpAPI.

### Connect you API from Serpapi
#### You will be prompted to enter the job title and location of the job you want to scrape. Once the script completes running, it will generate two files: "jobs.xlsx" and "jobs.json" which contains all the job listings and "salarios.xlsx" and "jobsal.json" which contains the salary information.

##### Note
* The script is set to scrape up to 450 job listings. If you want to scrape more or less, you can change the range of the for loop in the main function.

* The script also saves the date and time the script was ran in the "date_time" column of the "jobs.xlsx" file.

* The script also saves the search term and search location in the "search_term" and "search_location" columns of the "jobs.xlsx" file.
