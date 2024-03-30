I started this project in January 2024 with Dr. Michael Price, a Professor of Economics at The University of Alabama who studies charitable giving.

The project involves gathering mission statements from tax-exempt organizations (nonprofits/charities) from the United States, the United Kingdom, Australia, and Canada. We used the Python requests and BeautifulSoup libraries to accomplish this with web scraping. The United States data was scraped from the Internal Revenue Service, GuideStar, and Charity Navigator. The file 'webscrape.py' is used to scrape and store data. Generating the data is the longest part of this project because there are over 1.8 million nonprofits just in America, and web scraping can send limited requests to websites each second. I collect data one state at a time.

After data generation, we use Natural Language Processing techniques to identify patterns among these mission statements, with the goal of seeing how mission statements impact fundraising. We hope that this research benefits future charitable giving. We preprocess text with the SpaCy library and calculate linguistic readability and richness features with the R package quanteda (Quantitative Textual Data Analysis). The main goal of this project, however, is to see how Donor-Serving vs Society-Serving mission statements impact revenue, for most mission statements of nonprofits either describe how they benefit donors/members or describe how they benefit society at large.

The data (mission statements, EINs, nonprofits' names, etc.) are found in the 'data' folder. The United States data are found in the 'american' folder and organized by states and sectors and labeled as abbreviation_data.xlsx (example: AL_data.xlsx). There will also be a master spreadsheet that combines the information from all of the 51 other spreadsheets (50 states and D.C.). The folder 'irs-exempt-orgs' contains financial data from the IRS. 

The 'literature' folder contains past research that I considered helpful when beginning this project, as well as a small literature review.

The 'nlp' folder contains scripts that I wrote to perform various Natural Language Processing tasks, such as preprocessing text, building machine learning models, calculating linguistic complexity metrics such as readability and richness scores, and finding keywords.

The 'publications' folder includes the posters and writings that I will use to write relevant papers, posters, and presentations to showcase my work. This research has been presented at The University of Alabama's Undergraduate Research and Creative Activity (URCA) Conference, and I will apply to present at additional conferences.

For any questions regarding this research, please feel free to email me: hgunda@crimson.ua.edu.