@echo off
:: Navigate to the project directory (optional)
cd C:\Users\n1cit\OneDrive - Cape Peninsula University of Technology\Documents\2KRONOS\PYTHON\Python leanring journey

:: Stage all changes
git add .

:: Read commit message from commit_message.txt
set /p commit_message=<commit_message.txt

:: Commit the changes with the message from the text file
git commit -m "%commit_message%"

git commit add origin https://github.com/2Kronos/Python-learning-journey

:: Push the changes to the remote repository
git push -u origin master

:: Optional: Print a success message
echo Code committed and pushed to GitHub successfully!
