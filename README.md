# teslaAPI
Tesla API interactive examples

A simple app to allow users to poll and utilize the Tesla API to interrogate their vehicles for data or perform functions.

Full documentation may be found at https://tesla-api.timdorr.com/vehicle/commands/climate

## Usage
```bash
python main.py
```

## Requirements
```
pip install response readchar
```

## Authentication
1. Edit code and add email and tesla.com password to the file
2. Edit code and add known token to the file
3. Add environment variable TESLA_API_TOKEN to your system
  * Windows:
    * SET TESLA_API_TOKEN=YOUR-TOKEN-HERE
    
_Please be careful to not re-distribute code that has your password or token!_ 

## Release Notes

### 2020-11-20
  * Finish coding all API endpoints, couple do not work, but coded properly
  * Move menu definition to a data helper file for cleanliness
  * Add disclaimer on launch
  * Sleep after wake_up to allow it to finish
  * Updated menu system with more granularity (still need an even better one)
  * Parameterized commands now run!
  * Help text to explain parameters shown before entry
  * More robust error handling
  
### Initial
  * Simple menu to run a number of no-input-required commands via the Tesla API
  * Only GET/POST endpoints which do not require input

## ToDo List
* ~~Better user interface~~
* Betterer user interface
* ~~Parameter based API calls~~
* ~~Finish testing/coding "soon" items~~
* ~~Bug waking up the first time~~
* Interactive authentication
* After token, message user to set as env var for future use
* Send (share) address to car
* Summary screen with important info before main menu
* Auto-populate locked parameters
* Convert Celsius to Fahrenheit
* Intro text per menu
* Help text per item unrelated to parameters

## Acknowledgements
Props Jason Kaplan for the original code snippets & inspiration to make it better

## Contact
Caleb Cohen  
Caleb@Hail2Pitt.org  
https://github.com/PittCaleb  
Twitter: [@PittCaleb](https://www.twitter.com/PittCaleb)


  