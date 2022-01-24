#Weight and balance calc
from flask import Flask, render_template,jsonify,send_file, send_from_directory, abort, request, session
import numpy as np
import handler


app = Flask(__name__, 
            static_folder='static',
            template_folder='templates')
app.secret_key = 'mySecretKey'




def calculate(req):
    try:
        pWeight = float(req['pWeight']) #Pilot weight
        pArm = float(req['pArm']) #Pilot arm
        cWeight = float(req['cWeight']) #Copilot weight
        cArm = float(req['cArm']) #Copilot arm
        bWeight = float(req['bWeight']) #Back passenger weight
        bArm = float(req['bArm']) #Back passenger arm
        caWeight = float(req['caWeight']) #Cargo weight
        caArm = float(req['caArm']) #Cargo arm

        addedWeight = pWeight + cWeight + bWeight + caWeight #Add all weights
        totalMoment = (pWeight * pArm) + (cWeight * cArm) + (bWeight * bArm) + (caWeight * caArm) #Multiply weight by arm and add all
        cog = totalMoment/addedWeight #Find center of gravity
        returnStr = {'1':pWeight,'2':pArm,'3':cWeight,'4':cArm,'5':bWeight,'6':bArm,'7':caWeight,'8':caArm,'9':addedWeight,'10':totalMoment,'11':cog}
        return(returnStr)
    except:
        returnStr = {'1':'error'} #If user entered bad input return error
        return(returnStr)



@app.route('/',methods=["POST","GET"])
def homepage():
    if request.method == 'POST':
        req = request.form
        outStr = calculate(req) #Take user input and pass to the calculate function
        if(outStr.get('1') == 'error'):
            return(render_template('indexBase.html',x='Entered values are incorrect')) #Return error if bad inputs
        else:
            return(render_template('index.html',a = str(outStr.get('1')),b = str(outStr.get('2')),c = str(outStr.get('3')),d = str(outStr.get('4')),e = str(outStr.get('5')),f = str(outStr.get('6')),g = str(outStr.get('7')),h = str(outStr.get('8')),i = str(outStr.get('9')),j = str(outStr.get('10')),k = str(outStr.get('11')))) #Return output vals if user entered good values

    return(render_template('indexBase.html'))


app.run(host="0.0.0.0")