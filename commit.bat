@echo off
:: Navigate to the project directory (optional)
cd /d "C:\path\to\your\project"

:: Stage all changes
git add .

:: Read commit message from commit_message.txt
set /p commit_message=<commit_message.txt

:: Commit the changes with the message from the text file
git commit -m "%commit_message%"

:: Push the changes to the remote repository
git push origin main

:: Optional: Print a success message
echo Code committed and pushed to GitHub successfully!
