# Prudential mpf price crawler

Steps:
  1. Extract the mpf prices from the website
  2. Store the extracted data as expected format (Nested List)
  3. Link to the Google Sheets by Google API and Google Sheets API
  4. Store data into specific range

## Q: How to get credentials?
## A: Goto:
- console.cloud.google.com > Create project
- Search "Google Drive API" > Enable
- Search "Google Sheets API" > Enable
- After enabled "Google Sheets API" > Credentials > Create Credentials > Service Account
- After created service account > Add Key > Save as JSON
- Create a file called "cred.yml" > Paste the JSON into the file
- Change the main.py file content if needed
