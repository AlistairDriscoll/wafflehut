# Testing

## Manual Testing

| Page    | User Actions           | Expected Results | Y/N | Comments    |
|-------------|------------------------|------------------|------|-------------|
| Sign Up     |                        |                  |      |             |
| 1           | Click on Sign Up button | Redirection to Sign Up page | Y |          |
| 2           | Enter a username, input an invalid password twice and press sign-up button | Declines sign-up with a message saying why | Y |          |
| 3           | Enter a username, input two different passwords and press sign-up button | Declines sign-up | Y |          |
| 4           | Enter a username, input a valid password twice and press sign-up button | Takes user to their new userpage | Y |          |
| 5           | Enter valid email | Field will only accept email address format, declines when email is already used | Y |          |
| Sign In/Out |                        |                  |      |             |
| 1           | Go to logout | Takes user to a confirm logout page | Y |          |
| 2           | Click logout confirmation button | User logged out, directed to home page | Y |          |
| 3           | Press login button | Redirects user to login page | Y |          |
| 4           | Type in login details | Redirects user to their user page | Y |          |
| 11          | Click Remember Me checkbox | Remembers user | Y |          |
| 12          | Click on Log In button | Redirects user to blank In page | Y |          |
| 13          | Click logout button | Redirects user to home page | Y |          |
| 14          | Click browser back button | You are still logged out | Y |          |
| 15          | Click on Log In button | Redirection to Log In page prefilled | Y |          |
| Navigation  |                        |                  |      |             |
| 1           | Click on the logo | Redirection to home page | Y |          |
| 2           | Click Store | Redirection to Store page | Y |          |
| 3           | Click wishlist button | Redirection to wishlist page | Y |          |
| 4           | Click bag button | Redirection to bag page | Y |          |
| 5           | Click Profile button | Redirection to Profile page | Y |          |
| 6           | Click Logout button | Redirection to logout page | Y |          |