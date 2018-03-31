# Django Blog 

## Setup for "secrets.json"
The motivation of this setup is to keep secret values away from your public repository without using environment variables.

In this case it's used to maintain the privacy of the email login details.

In this setup, the "secrets.json" file is allocated in the project's root directory.

### Example for a Gmail account
    {
      "EMAIL_HOST": "smtp.gmail.com",
      "EMAIL_HOST_USER": "this_is_not_a_real_email@gmail.com",
      "EMAIL_HOST_PASSWORD": "not_a_real_password_1234",
      "EMAIL_PORT": 587
    }