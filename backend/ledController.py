import os
from flask import Flask
from flask.globals import request

# Configuration Arguments
arguments = ' --led-gpio-mapping=adafruit-hat --led-rows=32 --led-cols=64 --led-slowdown-gpio=4 --led-multiplexing=1'
imageArguments = ' -C'

"""Display an image on the led panel"""
def displayImage(image, config):
    displayImageOperation = 'sudo ./bin/led-image-viewer'
    executeCommand(displayImageOperation, image, config)

"""Display text on the led panel"""
def displayText(text, config):
    staticTextOperation = 'sudo ./bin/text-example -f rpi-rgb-led-matrix/fonts/10x20.bdf -C159,226,191'
    executeCommand(staticTextOperation, text, config)

"""Display scrolling text on the led panel"""
def displayScrollingText(text, config):
    scrollingTextOperation = 'sudo ./bin/text-scroller -f rpi-rgb-led-matrix/fonts/10x20.bdf -C159,226,191'
    executeCommand(scrollingTextOperation, text, config)

"""Execute a command based on the operation and parameters given"""
def executeCommand(operation, parameters, config):
    commandBuilder = operation+parameters+config
    os.system(commandBuilder)

"""Handle a Command Request"""
def handleRequest(inputOperation, inputParameters):
    if (inputOperation == "displayImage"):
        displayImage(inputParameters, arguments+imageArguments)
    elif (inputOperation == "displayText"):
        displayText(inputParameters, arguments)
    elif (inputOperation == "displayScrollingText"):
        displayScrollingText(inputParameters, arguments)

#create flask web app object
app = Flask(__name__)

# define http route
@app.route("/led",methods=['POST'])
def led():
        handleRequest("displayImage", " ./images/bmclogo.png")
        return "Updated Led"

#run the app
if __name__ == "__main__":
    app.run()