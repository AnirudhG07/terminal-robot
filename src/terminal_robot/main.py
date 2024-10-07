import _thread
import os
import subprocess

import click
import cv2

from terminal_robot.robotspeech import linearize

IMAGE_DIR = os.path.join(os.path.dirname(__file__), "images")
__version__ = "1.0.0"


@click.group(context_settings={"help_option_names": ["-h", "--help"]})
@click.version_option(version=f"v{__version__}")
def main():
    """
    A cool fun terminal robot that speaks and moves its mouth with your input text.
    """
    pass


@main.command(short_help="Speak with the robot.")
@click.option(
    "--speed",
    "-s",
    default=125,
    type=int,
    help="The speed of the robot's speech.",
)
@click.option(
    "--pitch",
    "-p",
    default=50,
    type=int,
    help="The pitch of the robot's speech.",
)
def speak(speed: int, pitch: int):
    """
    A cool fun terminal robot that speaks and moves its mouth with your input text.
    """
    print("Input sentence for the robot:")
    text = input()
    meta_text = ""
    waitempty, waitfullstop, waitchar = 0, 0, 0

    def espeak(text: str, robot_speed: int = speed, robot_pitch: int = pitch) -> int:
        """Use espeak to convert text to speech."""
        return subprocess.run(
            ["espeak", f"-s {robot_speed} -p {robot_pitch}", text], check=True
        ).returncode

    _thread.start_new_thread(espeak, (text,))
    meta_text = linearize(text) + "              "
    # print(meta_text)
    waitchar, waitfullstop, waitempty = 60, 60, 60

    mouthdict = {
        " ": "robot_m.png",
        ".": "robot_h.png",
        "!": "robot_h.png",
        "?": "robot_h.png",
        ",": "robot_h.png",
        ", ": "robot_h.png",
        "a": "robot_u.png",
        "b": "robot_e.png",
        "c": "robot_e.png",
        "d": "robot_h.png",
        "e": "robot_e.png",
        "f": "robot_m.png",
        "g": "robot_u.png",
        "h": "robot_h.png",
        "i": "robot_h.png",
        "j": "robot_o.png",
        "k": "robot_o.png",
        "l": "robot_s.png",
        "m": "robot_m.png",
        "n": "robot_m.png",
        "o": "robot_o.png",
        "p": "robot_e.png",
        "q": "robot_s.png",
        "r": "robot_o.png",
        "s": "robot_s.png",
        "t": "robot_e.png",
        "u": "robot_u.png",
        "v": "robot_s.png",
        "w": "robot_s.png",
        "x": "robot_s.png",
        "y": "robot_s.png",
        "z": "robot_s.png",
    }
    for char in meta_text:
        if char in mouthdict:
            if char == " ":
                mouth = mouthdict[char]
                # print(mouth)
                cv2.imshow(f"{char}", cv2.imread(os.path.join(IMAGE_DIR, mouth)))
                cv2.waitKey(waitempty)
                cv2.destroyAllWindows()
            elif char in [".", "!", "?"]:
                mouth = mouthdict[char]
                # print(mouth)
                cv2.imshow(f"{char}", cv2.imread(os.path.join(IMAGE_DIR, mouth)))
                cv2.waitKey(8 * waitfullstop)
                cv2.destroyAllWindows()
            elif char in [",", ", "]:
                mouth = mouthdict[char]
                cv2.imshow(f"{char}", cv2.imread(os.path.join(IMAGE_DIR, mouth)))
                cv2.waitKey(waitfullstop * 4)
            else:
                mouth = mouthdict[char]
                # print(mouth)
                cv2.imshow(f"{char}", cv2.imread(os.path.join(IMAGE_DIR, mouth)))
                cv2.waitKey(waitchar)
