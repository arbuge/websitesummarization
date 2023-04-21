import requests
import openai
from bs4 import BeautifulSoup

# Make a request to the webpage and grab the HTML response
page = requests.get("https://cometeer.com/").content

# Pass the HTML response to Beautiful Soup
soup = BeautifulSoup(page, 'html.parser')

# Extract only the human-readable text and remove blank lines
text = "\n".join(line.strip() for line in soup.get_text().split("\n") if line.strip())

#print(text)

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "Your job is to write a 500 word summary of whatever the user inputs."},
        {"role": "user", "content": text}
    ]
)

#print(response) #use this for api-type json output

#use the below for printing output to screen
content = response["choices"][0]["message"]["content"]
print(content)
