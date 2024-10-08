# Terminal-robot🤖

The terminal-robot is a fun feature you can add to your terminal to get a speaking robot.
You can easily run the python code. Enter the text you would like the robot to say and it will speak in a robotic-y voice with mouth movements!

https://github.com/AnirudhG07/terminal-robot/assets/146579014/24712b57-227b-43e6-8079-54b76c5e3959

## Installation

You can install the terminal-robot using the following ways -

### 1. Using pip

```bash
pip install terminal-robot
```

### 2. Using Homebrew (For MacOS)

```bash
brew install anirudhg07/anirudhg07/terminal-robot
```

### 3. Docker

You can run the docker image of terminal-robot by running -

```bash
docker run -it --rm anirudhg07/terminal-robot
```

### 4. Manual Installation

```bash
git clone https://github.com/AnirudhG07/terminal-robot.git
cd terminal-robot
pip install .
```

And you are good to go!

## Features You can change

You can always change features of the robot voice like speed and pitch. You can change it using the `--speed` and `--pitch` flags.

1. Speed - You can change the speed of the robot voice by changing the speed value. The default value is 150. You can change it by running -

```bash
terminal-robot speak --speed 200
```

2. Pitch - You can change the pitch of the robot voice by changing the pitch value. The default value is 50. You can change it by running -

```bash
terminal-robot speak --pitch 100
```

## Dependencies

The dependencies for the terminal=-robot are automaticaly taken care of by the package managers. You can also download the requirements by running -

```bash
pip install -r requirements.txt
```

Check out the requirements.txt file for more details.

## Future work!

```bash
Hi I am your terminal assistant. How can i help you?
```

2. Make this robot as a terminal assistant with chatbot to actually answer your terminal queries and give suggestions for errors
3. Add more features like changing robot face, robot talking speed and all. Since I have used espeak, it can be done without much difficulty.
4. More ideas and suggestions...
