# PythonFlaskCalculator
A very basic calculator that mimics the 'standard' mac/windows calculator using Flask. Users can compute multiple operations while the backend performs the computations.

## How to use
1. Pull this repo locally and open up a terminal/cmd prompt or whatever CLI you are using.
2. Install the required packages by running
```
pip install -r requirements.txt
```
3. Next, navigate to the root directory where this is mapped and run
```
python app.py
```

## Feature requests & Enancements before production
- [ ] The rendering is very basic and only uses an HTML table with minimal CSS. Using a framework would enhance UX/UI.</br>
- [ ] Prevent the user from entering too many operations which could cause an overflow.</br>
- [ ] Encode all passthrough from frontend<->backend</br>
- [ ] TLS/HTTPS ssl</br>
- [ ] CSRF Protection</br>
- [ ] Add Logging & unit tests using pytest
