import os
from flask import Flask
from flask.globals import request
from flask.wrappers import Response
import psutil
import subprocess

# Configuration Arguments
arguments = ' --led-gpio-mapping=adafruit-hat --led-rows=32 --led-cols=64 --led-slowdown-gpio=4 --led-multiplexing=1'
imageArguments = ' -C'
fullBinPath = '/home/pi/Documents/testing/rest-led-panel/backend/bin/'
fullImagesPath = '/home/pi/Documents/testing/rest-led-panel/backend/images/'

"""Display an image on the led panel"""
def displayImage(image, config):
    displayImageOperation = f'sudo {fullBinPath}led-image-viewer'
    return executeCommand(displayImageOperation, fullImagesPath+image, config)

"""Display text on the led panel"""
def displayText(text, config):
    staticTextOperation = 'sudo ./bin/text-example -f ./fonts/10x20.bdf -C159,226,191'
    return executeCommand(staticTextOperation, text, config)

"""Display scrolling text on the led panel"""
def displayScrollingText(text, config):
    scrollingTextOperation = 'sudo ./bin/text-scroller -f ./fonts/10x20.bdf -C159,226,191'
    return executeCommand(scrollingTextOperation, text, config)

processes = []
"""Execute a command based on the operation and parameters given"""
def executeCommand(operation, parameters, config):
    commandBuilder = f"{operation} {parameters} {config}"

    # Start a subprocess without stdout and stderr
    process = subprocess.Popen(commandBuilder, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Add the process to the list of processes
    processes.append(process)
    
    # If we have more than one process, kill the older one
    if len(processes) > 1:
        processToKill = processes.pop(0)
        processToKill.terminate()

    # Respond with 200 OK
    return Response("Updated LED", status=200)


"""Handle a Command Request"""
def handleRequest(inputOperation, inputParameters):
    if (inputOperation == "displayImage"):
        return displayImage(inputParameters, arguments+imageArguments)
    elif (inputOperation == "displayText"):
        return displayText(inputParameters, arguments)
    elif (inputOperation == "displayScrollingText"):
        return displayScrollingText(inputParameters, arguments)
    else:
        return Response("Invalid Operation", status=400)

#create flask web app object
app = Flask(__name__)

# define http route
@app.route("/led",methods=['POST'])
def led():
        requestJson = request.get_json()
        return handleRequest(requestJson['operation'], requestJson['parameters'])

#run the app
if __name__ == "__main__":
    app.run()