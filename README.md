# Terminal-robot🤖
The terminal-robot is a fun feature you can add to your terminal to get a speaking robot.
You can easily run the python code. Enter the text you would like the robot to say and it will speak in a robotic-y voice with mouth movements!

# How to use
Follow the given steps and get yourself a talking robot-
1. git clone the repository in your home
2. Install dependencies in your environment
3. In home directory, paste the terminal-robot.sh file
4. Follow the below commands one by one to create an alias for it, to never run the python files
```bash
# STEP 1
open ~/.zshrc  # OR open ~/.bashrc
# STEP 2 - Paste the below at the end of the file (or anywhere)
alias terminal-robot='bash terminal-robot.sh'
# STEP 3 - Save the file with Cmd S or Ctrl S. Reopen the Terminal and...
# STEP 4
terminal-robot 
```

# Features You can change
1. You can always change features of the robot's voice like voice type, speed, pitch, etc.
2. If you don't like the robot, go to the cloned repository and change the images according to your mouth settings. Don't forget to rename the pics as given.
   
# Dependencies
```bash
python3 -m pip install opencv-python
python3 -m pip install metaphone
python3 -m pip install _thread
```
Make sure to have this in your environment before running this application else "No module named `libarary`" may show up.

# Contributions
1. Put it in homebrew so as to directly get it to run in terminal.
```bash
brew install terminal-robot
terminal-robot
```
```bash
Hi I am your terminal assistant. How can i help you?
```
2. Make this robot as a terminal assistant with chatbot to actually answer your terminal queries and give suggestions for errors
3. Add more features like changing robot face, robot talking speed and all. Since I have used espeak, it can be done without much difficulty.
4. More ideas and suggestions...
