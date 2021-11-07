# USE ONLY RECOMMENDED WITH PIXELBOT RELATED PROJECTS
We don't take responsibility for what you do with this.

## FORK - ADDED FEATURES THAT DON'T EXIST IN UPSTREAM
- Automatic Captcha Solving using Captcha Buster extension (click on the captcha and click on the solver button)
- Script doesn't close anymore after it's done (press enter to start the process again after completion, this clears cookies too)
- Script only saves the details after they are entered

# Reddit Account Generator
 **WHAT IS IT?**
 
 This is a semi-automatic Reddit account generator. I'm saying "semi-automatic" because it still requires a Google Captcha to be completed at the end of the creation process.
 
 **HOW DOES IT WORK?**
 
 This script was made for quickly creating Reddit throwaways. _See my other project -- the Reddit Account Deleter, which is made to completly erase Reddit accounts (including comments and all)._
 It generates an username derived from a Wikipedia:Random article, and then appending some random digits to it as to have it be unique. Then, it completes the Reddit sign-up process, leaving you only to complete the Captcha at the end.
 
 **REQUIRMENTS**
 
 Only Selenium and webdriver-manager (pip install selenium && pip install webdriver-manager).
 A file named "namesforreddit.txt" should be in the same folder as the .py executable.
