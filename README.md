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

_Please be careful to not re-distribute code that has your password or token!_ 

## Release Notes
###2020-11-20
  * Updated menu system with more granularity (still need an even better one)
  * Parameterized commands now run!
  * Help text to explain parameters shown before entry
  * More robust error handling
  
###Initial
  * Simple menu to run a number of no-input-required commands via the Tesla API
  * Only GET/POST which do not require input will run

## ToDo List
* ~~Better user interface~~
* ~~Parameter based API calls~~
* Finish testing/coding "soon" items
* Bug waking up the first time (rerun works)
* Interactive authentication
* After token, message user to set as env var for future use
* Convert Celsius to Fahrenheit
* Betterer user interface

## Acknowledgements
Props Jason Kaplan for the original code snippets & inspiration to make it better

## Contact
Caleb Cohen  
Caleb@Hail2Pitt.org  
https://github.com/PittCaleb  
Twitter: [@PittCaleb](https://www.twitter.com/PittCaleb)


  