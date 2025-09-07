
# Supermarket Assistant Chatbot

## Description
This project is a web-based chatbot that assists customers in finding products on shelves. It extracts products from user input using basic Natural Language Processing (NLP) and associates them with the appropriate store shelf numbers.


## Features
- Extracts items from a shopping list typed in natural language.
- Displays the shelf location for each item.
- Allows printing the shopping list with shelf numbers.
- Allows downloading the shopping list as a text file.


## Sample Input and Output

**Input** 
I want to buy apple and milk 


**Output**  
apple → Shelf 1
milk → Shelf 3


## Project Structure
project_folder/
│
├─ app.py # Flask backend
├─ chatbot.py # Python functions: extract_items  and find_shelves
├─ index.html # Frontend HTML
├─ style.css # Optional styling for the frontend
├─ README.md # This file


---

## Setup Instructions

1.  Install Python packages:

```bash
pip install flask spacy
python -m spacy download en_core_web_sm

2. Ensure  project folder has all the required files (app.py, chatbot.py, index.html, style.css).

3. Run the Flask application
       python app.py

4. Open your web browser and go to
    
    http://127.0.0.1:5000/
    
## How to Use the Chatbot
1. Enter your shopping list in the text area
2. Click Find Shelves.
3. The chatbot will display the shelf locations for each item.
4. Click Print List to print the shopping list.
5. Click Download List to save it as a text file.





