# SecretSanta
Secret Santa matcher and email sender

# How to use
0. Make sure you have python 3 installed.


1. Create a csv file in the working directory with all the participants, with the following format:

```Participant Name, participants@email.address```

Refer to testdata.csv for example


2. Update the email message returned in sendEmail.constructMessage(), to suit your own group's needs. 


3. In authenticationInfo.py, fill in your own login and password information for the email address you wish to send the emails from. Currently, gmail and gsuite addresses will work. If you want to use a non-gmail/non-gsuite address, you additionally need to update  SMPTSERVER in sendEmails.py.


4. If using a gmail/gsuite account, allow [less secure apps](https://myaccount.google.com/lesssecureapps) for the account.


5. Send the emails from the working directory with:
```python main.py participantlist.csv```


6. Enjoy your Secret Santa exchange! When it is over, you can check the file santa_solution. Each name in the list is the santa for the following name in the list. The last name in the list is the Santa for the first name.

## License

This project is available under the [MIT LICENSE](https://github.com/fullmers/SecretSanta/blob/master/LICENSE)
