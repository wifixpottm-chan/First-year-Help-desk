#install python 3.6.7
#ctrl+alt+s then go to project -> python interpretor -> add speech recognition, pyttsx3,pyaudio
from win10toast import ToastNotifier
import requests
import random
import time as t
from bs4 import BeautifulSoup
from pywikihow import HowTo
import datetime
import pywhatkit
import speech_recognition as sr
import pyttsx3
import wikipedia
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty('voice',voices[1].id)
engine.say("Heyyyy! call me saffron")
engine.say("How can I help you?")
engine.runAndWait()
def talk(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
    try:
        with sr.Microphone() as source:
            print("listening")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(command)
            '''if 'saffron' in command:
                command = command.replace("saffron","")
                command = command.replace("hey","")
                print(command)'''
    except:
        pass
    return command
def run_saffron():

    command = take_command()
    if "play" in command:
        song = command.replace("play","")
        talk("playing"+song)
        print("playing"+song)
        pywhatkit.playonyt(song)
    elif "tell me about" in command:

        if "robotic eye" in command:
            talk("robotic eye is organized by takshak expo core and it is held outdoor")
            print("robotic eye is organized by takshak expo core and it is held outdoor")
        elif "pick and place" in command:
            talk("pick and place robot is organised by takshak expo core and it is held in main auditorium")
            print("pick and place robot is organised by takshak expo core and it is held in main auditorium")
        elif 'autonomous robot' in command:
            talk("autonomous robot is organised by takshak expo core and it is held in main auditorium")
            print("pick and place robot is organised by takshak expo core and it is held in main auditorium")
        elif 'autonomous drone' in command:
            talk("autonomous drone is organised by takshak expo core and it is held in main auditorium")
            print("autonomous drone is organised by takshak expo core and it is held in main auditorium")
        elif 'gesture controlled robot' in command:
            talk("gesture controlled robot is organised by takshak expo core and it is held in m p varghese common space")
            print("gesture controlled robot is organised by takshak expo core and it is held in m p varghese common space")
        elif 'lithophane collage' in command:
            talk("lithophane collage is being held by takshak expo core in stall office parking")
            print("lithophane collage is being held by takshak expo core in stall office parking")
        elif 'photobooth' in command:
            talk("photobooth is being held by takshak expo core in fablab")
            print("photobooth is being held by takshak expo core in fablab")
        elif 'led cube' in command:
            talk("led cube is being held by takshak expo core in fablab")
            print("led cube is being held by takshak expo core in fablab")
        elif 'flower' in command:
            talk("flower is being held by takshak expo core in machines lab and stall office parking")
            print("flower is being held by takshak expo core in machines lab and stall office parking")
        elif 'robotic drawing machine' in command:
            talk('robotic drawing machine is being held by takshak expo core in m p varghese block entrance')
            print('robotic drawing machine is being held by takshak expo core in m p varghese block entrance')
        elif 'greenhouse automation' in command:
            talk('greenhouse automation is being held by takshak expo core in common space opposite to i o t room')
            print('greenhouse automation is being held by takshak expo core in common space opposite to i o t room')
        elif 'self balancing robot' in command:
            talk('self balancing robot is being held by takshak expo core in i o t room')
            print('self balancing robot is being held by takshak expo core in i o t room')
        elif 'google assistant robot' in command:
            talk('google assistant robot is being held by takshak expo core in i o t room')
            print('google assistant robot is being held by takshak expo core in i o t room')
        elif 'space room' in command:
            talk('space room-aisa is being held by takshak expo core in room f 3 0 4, f 3 0 5 and corridor')
            print('space room-aisa is being held by takshak expo core in room f 3 0 4, f 3 0 5 and corridor')
        elif 'i e d c stall' in command:
            talk('iedc stall is being held by takshak expo core in office parking lot')
            print('iedc stall is being held by takshak expo core in office parking lot')
        elif 'piano stairs' in command:
            talk('piano stairs is being held by takshak expo core in main stair, m p varghese block stair and e c block stair')
            print('piano stairs is being held by takshak expo core in main stair, m p varghese block stair and e c block stair')
        elif 'cutting machine' in command:
            talk('foam cutting machine is being held by takshak expo core in m p varghese block entrance')
            print('foam cutting machine is being held by takshak expo core in m p varghese block entrance')
        elif 'line following robot' in command:
            talk('line following robot is being held by takshak expo core in i o t room')
            print('line following robot is being held by takshak expo core in i o t room')
        elif 'smart parking system' in command:
            talk('smart parking system is being held by takshak expo core in i o t room')
            print('smart parking system is being held by takshak expo core in i o t room')
        elif 'trig' in command:
            talk('e-trig is being held by takshak expo core in i o t room')
            print('e-trig is being held by takshak expo core in i o t room')
        elif 'bionic arm' in command:
            talk("bionic arm is organised by electronics department and it is being held in classroom l109")
            print("bionic arm is organised by electronics department and it is being held in classroom l109")
        elif "snake robot" in command:
            talk("snake robot is organised by electronics department and it is being held in classroom l110")
            print("snake robot is organised by electronics department and it is being held in classroom l110")
        elif "robotics expo" in command:
            talk("robotics expo is organised by electronics department and it is b`eing held in classroom l101, digital lab l103 and classroom l108")
            print("robotics expo is organised by electronics department and it is being held in classroom l101, digital lab l103 and classroom l108")
        elif "hand gesture" in command: #help
            talk("hand gesture dio game is organsied by electronics departmenr and it is being held in classroom l109")
            print("hand gesture dio game is organsied by electronics departmenr and it is being held in classroom l109")
        elif "light painting with an led robot" in command:
            talk("light painting with an led robot is organised by electronics department and it is being held in classroom l109")
            print("light painting with an led robot is organised by electronics department and it is being held in classroom l109")
        elif "solar tracker" in command:
            talk("solar tracker is organised by electronics department and is being held in classroom l110")
            print("solar tracker is organised by electronics department and is being held in classroom l110")
        elif "fire fighting robot" in command:
            talk("fire fighting robot is being held by electronics department in room l110")
            print("fire fighting robot is being held by electronics department in room l110")
        elif "lock" in command:
            talk("mask recognized door lock is being held by electronics department in room l110")
            print("mask recognized door lock is being held by electronics department in room l110")
        elif "smart pill box" in command:
            talk("smart pill box is being held by electronics department in room l110")
            print("smart pill box is being held by electronics department in room l110")
        elif 'd c microgrid' in command:
            talk("dc microgrid is being held by triple e department in carpentry front space")
            print("dc microgrid is being held by triple e department in carpentry front space")
        elif 'skeleton dance' in command:
            talk('skeleton dance is being held by triple e department in machines lab')
            print('skeleton dance is being held by triple e department in machines lab')
        elif 'ladder' in command:
            talk('jacob’s ladder is being held by triple e department in machines lab')
            print('jacob’s ladder is being held by triple e department in machines lab')
        elif 'tesla coil' in command:
            talk('tesla coil is being held by triple e department in machines lab')
            print('tesla coil is being held by triple e department in machines lab')
        elif 'hydro electric' in command:
            talk('hydro electric power plant-still model is being held by triple e department in machines lab')
            print('hydro electric power plant-still model is being held by triple e department in machines lab')
        elif 'wind mill' in command:
            talk('wind mill is being held by triple e department in machines lab')
            print('wind mill is being held by triple e department in machines lab')
        elif 'testing setup' in command:
            talk('elcb testing set up is being held by triple e department in machines lab')
            print('elcb testing set up is being held by triple e department in machines lab')
        elif 'van de graaff' in command:
            talk('vandegraff is being held by triple e department in machines lab')
            print('vandegraff is being held by triple e department in machines lab')
        elif 'metro train' in command:
            talk('metro train is being held by triple e department in machines lab')
            print('metro train is being held by triple e department in machines lab')
        elif 'nutmeg sorter' in command:
            talk('nutmeg sorter is being held by triple e department in machines lab')
            print('nutmeg sorter is being held by triple e department in machines lab')
        elif 'solar system' in command:
            talk('solar p v system is being held by triple e department in machines lab')
            print('solar p v system is being held by triple e department in machines lab')
        elif 'tunnel' in command:
            talk('vortex tunnel is being held by triple e department in entrance electric workshop')
            print('vortex tunnel is being held by triple e department in entrance electric workshop')
        elif 'infinity mirror' in command:
            talk('infinity mirror is being held by triple e department in entrance electric workshop')
            print('infinity mirror is being held by triple e department in entrance electric workshop')
        elif 'cycle' in command:
            talk('cycle is being held by triple e department in machines lab')
            print('cycle is being held by triple e department in machines lab')


        elif 'led display' in command:
            talk('clap-led dispaly is being held by triple e department in machines lab')
            print('clap-led dispaly is being held by triple e department in machines lab')
        elif 'thor hammer' in command:
            talk('thor hammer is being held by triple e department in machines lab')
            print('thor hammer is being held by triple e department in machines lab')
        elif 'steady hand game' in command:
            talk('steady hand game is being held by triple e department in machines lab')
            print('steady hand game is being held by triple e department in machines lab')
        elif 'electric kick' in command:
            talk('electric kick scooter is organised by mechanical department in the parking lot infront of basketball court')
            print('electric kick scooter is organised by mechanical department in the parking lot infront of basketball court')
        elif 'electrical power' in command:
            talk('electrical power is being held by mechanical department in front right side')
            print('electrical power is being held by mechanical department in front right side')
        elif 'museum of illusion' in command:
            talk('museum of illusion is a takshak premium event being held by civil department in rooms pg203, pg 204, pg 205, pg 206, pg 208')
            print('museum of illusion is a takshak premium event being held by civil department in rooms pg203, pg 204, pg 205, pg 206, pg 208')
        elif 'contraction' in command:
            talk(' contraption is held by civil department in pg107')
            print(' contraption is held by civil department in pg107')
        elif 'fixed wing' in command:
            talk('fixed wing is being held by s a e in front plot')
            print('fixed wing is being held by s a e in front plot')
        elif 'go kart' in command:
            talk('go cart is being held by s a e in parking lot in front of basketball court')
            print('go cart is being held by s a e in parking lot in front of basketball court')
        elif 'tractor' in command:
            talk('trackter is being held by s a e in parking lot in front of basketball court')
            print('trackter is being held by s a e in parking lot in front of basketball court')
        elif 'electric scooter' in command:
            talk('electric scooter is being held by s a e and a s m e in parking lot in front of basketball court')
            print('electric scooter is being held by s a e and a s m e in parking lot in front of basketball court')
        elif 'light the lives' in command:
            talk('light of lives is being held by i triple e in front of carpentry')
            print('light of lives is being held by i triple e in front of carpentry')
        elif 'pro life exhibition' in command:
            talk('pro life exhibition is being held by i triple e in room m p v 201')
            print('pro life exhibition is being held by i triple e in room m p v 201')
            #ye mere me se hai (iske peeche ka)
        elif '3d theatre' in command:
            talk('3d theatre is being held by c a department in m p v 105')
            print('3d theatre is being held by c a department in m p v 105')
        elif 'flood rescue robot' in command:
            talk('flood rescue robot is being held by c a department in m p v 108')
            print('flood rescue robot is being held by c a department in m p v 108')
        elif 'dam' in command:
            talk('dam is being held by c a department in m p v 109')
            print('dam is being held by c a department in m p v 109')
        elif 'angry birds' in command:
            talk('angry birds in real is being held by m c a department in mpv-mca open area')
            print('angry birds in real is being held by m c a department in mpv-mca open area')
        elif 'wonders of light' in command:
            talk('wonders of light is being held by m c a department in mpv-mca open area')
            print('wonders of light is being held by m c a department in mpv-mca open area')
        elif 'covi guard' in command:
            talk('covi guard is being held by m c a department in mpv-mca open area')
            print('covi guard is being held by m c a department in mpv-mca open area')
        elif 'dynamic speed governor and smart traffic system' in command:
            talk('a i based dynamic speed governor and smart traffic system for accident avoidence is being held by m c a department in mpv-mca open area')
            print('a i based dynamic speed governor and smart traffic system for accident avoidence is being held by m c a department in mpv-mca open area')
        elif 'smoke remover' in command:
            talk('smoke remover is being held by m c a department in mpv-mca open area')
            print('smoke remover is being held by m c a department in mpv-mca open area')
        elif 'earth 2 point o' in command:
            talk('earth 2 point o is being held by m c a department in mpv-mca open area')
            print('earth 2 point o is being held by m c a department in mpv-mca open area')
        elif 'conversion of plastic' in command:
            talk('conversion of plastic into sand, fuel, electricity, l p g, water is being held by m c a department in mpv-mca open area')
            print('conversion of plastic into sand, fuel, electricity, l p g, water is being held by m c a department in mpv-mca open area')
        elif 'third generation nuclear' in command:
            talk('third generation nuclear still model power plant is being held by m c a department in mpv-mca open area')
            print('third generation nuclear still model power plant is being held by m c a department in mpv-mca open area')

        elif 'kinetic and drawing table' in command:
            talk('kinetik and drawing table is organised by c s department and is being held in electronics block ground floor entry')
            print('kinetik and drawing table is organised by c s department and is being held in electronics block ground floor entry')
        elif 'tic tac toe soccer' in command:
            talk('tic tac toe soccer is being organised by c s department and is being held at the common courtyard of electronics department block')
            print('tic tac toe soccer is being organised by c s department and is being held at the common courtyard of electronics department block')
        elif 'smart mirror' in command:
            talk('smart mirror is being organised by c s department and is being held in i o t room')
            print('smart mirror is being organised by c s department and is being held in i o t room')
        elif 'plate' in command:
            talk('chladni plate is being organised by c s department and it is being held in classroom l201 in electronics block')
            print('chladni plate is being organised by c s department and it is being held in classroom l201 in electronics block')
        elif 'sign language translator' in command:
            talk('sign language translator is being organised by c s department and it is being held at classroom l201 in electronics block')
            print('sign language translator is being organised by c s department and it is being held at classroom l201 in electronics block')
        elif 'push up counter' in command:
            talk('push up counter is being organised by c s department and it is being held in classroom l218 in the electronics block')
            print('push up counter is being organised by c s department and it is being held in classroom l218 in the electronics block')
        elif 'alcohol detection helmet' in command:
            talk('alcohol detection helmet is being organised by c s department and it is being held in classroom l218 in the electronics block')
            print('alcohol detection helmet is being organised by c s department and it is being held in classroom l218 in the electronics block')
        elif 'tube' in command:
            talk("ruben's tube is being organised by c s department in classroom l212")
            print("ruben's tube is being organised by c s department in classroom l212")
        elif 'laser mirror' in command:
            talk("laser mirror art is being organised by c s department in classroom l217")
            print("laser mirror art is being organised by c s department in classroom l217")
        elif 'thermal mirror' in command:
            talk("thermal mirror is being organised by c s  department and it is being hel din classroom l218")
            print("thermal mirror is being organised by c s  department and it is being hel din classroom l218")
        elif 'interactive hologram' in command:
            talk('you are talking to interactive hologram right now')
            print('you are talking to interactive hologram right now')
        elif 'led dance off' in command:
            talk("led dance off is being organised by c s  department and it is being hel din classroom l217")
            print("led dance off is being organised by c s  department and it is being hel din classroom l217")
        elif 'pandora' in command:
            talk('c s e signature project pandora is being organised by c s department in classroom l219')
            print('c s e signature project pandora is being organised by c s department in classroom l219')
        elif 'keyboard artwork' in command:
            talk('keyboard artowrk is being organised by c s department and is held in c s e entrance')
            print('keyboard artowrk is being organised by c s department and is held in c s e entrance')
        elif 'still models' in command:
            talk('still models organised by c s department is held in c s e labs l203, l204 and l206')
            print('still models organised by c s department is held in c s e labs l203, l204 and l206')

        elif 'helicopter' in command:
            talk('helicopter is a takshak premium event organised by takshak core and it is held in cricket ground on 26th and 27th of november')
            print('helicopter is a takshak premium event organised by takshak core and it is held in cricket ground on 26th and 27th of november')
        elif 'stall for painting' in command:
            talk('the stall for paintings and other art works is a takshak premium event organised by takshak core and it is held in foundry opposite to parking')
            print('the stall for paintings and other art works is a takshak premium event organised by takshak core and it is held in foundry opposite to parking')
        elif 'stall for photographs' in command:
            talk('stall for photo graphs is a takshak premium event being organised by takshak core and it is being held in foundry opposite to parking')
            print('stall for photo graphs is a takshak premium event being organised by takshak core and it is being held in foundry opposite to parking')
        elif 'stall for photograph' in command:
            talk('stall for photo graphs is a takshak premium event being organised by takshak core and it is being held in foundry opposite to parking')
            print('stall for photo graphs is a takshak premium event being organised by takshak core and it is being held in foundry opposite to parking')
        elif 'doll for photographs' in command:
            talk('stall for photo graphs is a takshak premium event being organised by takshak core and it is being held in foundry opposite to parking')
            print('stall for photo graphs is a takshak premium event being organised by takshak core and it is being held in foundry opposite to parking')
        elif 'doll for photograph' in command:
            talk('stall for photo graphs is a takshak premium event being organised by takshak core and it is being held in foundry opposite to parking')
            print('stall for photo graphs is a takshak premium event being organised by takshak core and it is being held in foundry opposite to parking')
        elif 'carnival' in command:
            talk('carnival is a takshak premium event being organised by takshak core and it is being held in 5 plots inside college near basketball court')
            print('carnival is a takshak premium event being organised by takshak core and it is being held in 5 plots inside college near basketball court')
        elif 'construction and destruction' in command:
            talk('construction and destruction is a takshak premium event being organised by civil department in pg 310')
            print('construction and destruction is a takshak premium event being organised by civil department in pg 310')
        elif 'hackathon' in command:
            talk('a r workshop and hackathon is a takshak premium event being organised by i triple e in t n p seminar hall')
            print('a r workshop and hackathon is a takshak premium event being organised by i triple e in t n p seminar hall')
        elif 'gaming arcade' in command:
            talk('gaming arcade is a takshak premium event and it is organised by c s department in room l301')
            print('gaming arcade is a takshak premium event and it is organised by c s department in room l301')
        elif 'mission impossible' in command:
            talk('mission impossible is a takshak premium event organised by c s department and is it being held in classroom l304')
            print('mission impossible is a takshak premium event organised by c s department and is it being held in classroom l304')
        elif 'forza' in command:
            talk('forza simulator is a takshak premium event organised by e c department in room l109')
            print('forza simulator is a takshak premium event organised by e c department in room l109')
        elif 'periods pain' in command:
            talk('periods pain simulator is a takshak premium event organised by e c department in room l109')
            print('periods pain simulator is a takshak premium event organised by e c department in room l109')
        elif 'de meido' in command:
            talk('de meido is a takshak premium event organised by triple e department in library up 2 rooms')
            print('de meido is a takshak premium event organised by triple e department in library up 2 rooms')
        elif 'dredge' in command:
            talk('dredge it is a takshak premium event organised by triple e department and it is a treasure hunt throughout college')
            print('dredge it is a takshak premium event organised by triple e department and it is a treasure hunt throughout college')
        elif 'flip the bottle' in command:
            talk('flip the bottle is a takshak premium event organised by triple e department inside basketball court')
            print('flip the bottle is a takshak premium event organised by triple e department inside basketball court')
        elif 'paintball' in command:
            talk('paintball is a takshak premium event organised by mechanical  department in college parking lot')
            print('paintball is a takshak premium event organised by mechanical  department in college parking lot')
        elif 'bull ride game' in command:
            talk('bull ride game is a takshak premium event organised by mechanical department in ground in front of library')
            print('bull ride game is a takshak premium event organised by mechanical department in ground in front of library')
        elif 'virtual racing' in command:
            talk('virtual racing simulator is a takshak premium event organised by s a e in carnival area')
            print('virtual racing simulator is a takshak premium event organised by s a e in carnival area')
        elif 'reusable rocket' in command:
            talk('reusable rocket is a takshak premium event organised by a i s a in seminar hall 2 or p t a seminar hall')
            print('reusable rocket is a takshak premium event organised by a i s a in seminar hall 2 or p t a seminar hall')
        elif 'air balloon' in command:
            talk('air balloon is a takshak premium event organised by takshak core 2nd and 3rd december in cricket ground')
            print('air balloon is a takshak premium event organised by takshak core 2nd and 3rd december in cricket ground')
        elif 'financial management' in command:
            talk('financial management by sharique sasudheen is a takshak premium event organised by takshak core on 3rd december at o a t')
            print('financial management by sharique sasudheen is a takshak premium event organised by takshak core on 3rd december at o a t')
        elif 'trilit labs' in command:
            talk('trilit labs v r gaming is a takshak premium event organised by takshak core and it is being held in room m119')
            print('trilit labs v r gaming is a takshak premium event organised by takshak core and it is being held in room m119')
        elif 'car racing' in command:
            talk('rc car racing is a takshak premium event organised by takshak core and i o t club in mpv 201')
            print('rc car racing is a takshak premium event organised by takshak core and i o t club in mpv 201')
        elif 'drone workshop' in command:
            talk('drone workshop is a takshak premium event organised by expo core in seminar hall 2')
            print('drone workshop is a takshak premium event organised by expo core in seminar hall 2')

        else:
            talk("couldn't hear you clearly")
            print("couldn't hear you clearly")
    elif "time" in command:
        time=datetime.datetime.now().strftime('%I:%M %p')
        talk( 'The time is '+time)
        print("The time is "+time)
    elif "reminder" in command:
        toaster = ToastNotifier();
        a='reminder'
        print("what is the reminder for?")
        talk("what is the reminder for?")
        take_command()
        b=command
        t.sleep(5)
        toaster.show_toast(a,b,duration=10,threaded=True)

    elif (("your name")) in command:
        ask = command.replace("your name", "")
        ask = command.replace("who are you", "")
        ask = command.replace("yourself", "")
        info = "I am Saffron, your personal AI."
        print(info)
        talk(info)
    elif (("who are you")) in command:
        ask = command.replace("your name", "")
        ask = command.replace("who are you", "")
        ask = command.replace("yourself", "")
        info = "I am Saffron, your personal AI."
        print(info)
        talk(info)
    elif ("Wow") in command:
        print("Thankyou")
        talk("Thankyou")
    elif (("yourself")) in command:
        ask = command.replace("your name", "")
        ask = command.replace("who are you", "")
        ask = command.replace("yourself", "")
        info = "I am Saffron, your personal AI."
        print(info)
        talk(info)
    elif (("how are you")) in command:
        ask = command.replace("how are you", "")
        info = "I am doing great! Thanks for asking"
        print(info)
        talk(info)
    elif (("you doing")) in command:
        ask = command.replace("what are you doing", "")
        info = "I am doing great! Thanks for asking"
        print(info)
        talk(info)
    elif (("wagwan my g")) in command:
        ask = command.replace("wagwan my g", "")
        info = "I am doing great! Thanks for asking"
        print(info)
        talk(info)
    elif (("what is"))in command:
        ask = command.replace("what is", "")
        info = wikipedia.summary(ask,3)
        print(info)
        talk(info)
        '''elif (("tell me about"))in command:
        ask = command.replace("tell me about", "")
        info = wikipedia.summary(ask,3)
        print(info)
        talk(info)'''
    elif (("who is "))in command:
        ask = command.replace("who is", "")
        info = wikipedia.summary(ask,3)
        print(info)
        talk(info)
    elif (("who was"))in command:
        ask = command.replace("who was", "")
        info = wikipedia.summary(ask,3)
        print(info)
        talk(info)
    elif (("when was"))in command:
        ask = command.replace("when was", "")
        info = wikipedia.summary(ask,3)
        print(info)
        talk(info)
    elif (("when did"))in command:
        ask = command.replace("when did", "")
        info = wikipedia.summary(ask,3)
        print(info)
        talk(info)
    elif (("who is the"))in command:
        ask = command.replace("who is the", "")
        info = wikipedia.summary(ask,3)
        print(info)
        talk(info)
    elif (("what is the"))in command:
        ask = command.replace("what is the", "")
        info = wikipedia.summary(ask,3)
        print(info)
        talk(info)
    elif (("who was the"))in command:
        ask = command.replace("who was the", "")
        info = wikipedia.summary(ask,3)
        print(info)
        talk(info)
    elif (("joke")) in command:
        ask = command.replace("joke", "")
        a=["What did the fish say when he swam into a wall? Dam.","What do you call a fish with no eyes? A fsh","What do you call a can opener that doesn’t work? A can’t opener!","I'm afraid for the calendar. Its days are numbered.","My wife said I should do lunges to stay in shape. That would be a big step forward.","Why do fathers take an extra pair of socks when they go golfing?" "In case they get a hole in one!","Singing in the shower is fun until you get soap in your mouth. Then it's a soap opera.","What do a tick and the Eiffel Tower have in common?" "They're both Paris sites.","What do you call a fish wearing a bowtie?" "Sofishticated.","How do you follow Will Smith in the snow?" "You follow the fresh prints."]
        b=random.randrange(0,9)
        info=a[b]
        print(info)
        talk(info)
    elif (("make me laugh")) in command:
        ask = command.replace("joke", "")
        a=["What did the fish say when he swam into a wall? Dam.","What do you call a fish with no eyes? A fsh","What do you call a can opener that doesn’t work? A can’t opener!","I'm afraid for the calendar. Its days are numbered.","My wife said I should do lunges to stay in shape. That would be a big step forward.","Why do fathers take an extra pair of socks when they go golfing?" "In case they get a hole in one!","Singing in the shower is fun until you get soap in your mouth. Then it's a soap opera.","What do a tick and the Eiffel Tower have in common?" "They're both Paris sites.","What do you call a fish wearing a bowtie?" "Sofishticated.","How do you follow Will Smith in the snow?" "You follow the fresh prints."]
        b=random.randrange(0,9)
        info=a[b]
        print(info)
        talk(info)
    elif (("i am sad")) in command:
        ask = command.replace("joke", "")
        a = ["What did the fish say when he swam into a wall? Dam.", "What do you call a fish with no eyes? A fsh","What do you call a can opener that doesn’t work? A can’t opener!","I'm afraid for the calendar. Its days are numbered.","My wife said I should do lunges to stay in shape. That would be a big step forward.","Why do fathers take an extra pair of socks when they go golfing?" "In case they get a hole in one!","Singing in the shower is fun until you get soap in your mouth. Then it's a soap opera.","What do a tick and the Eiffel Tower have in common?" "They're both Paris sites.","What do you call a fish wearing a bowtie?" "Sofishticated.","How do you follow Will Smith in the snow?" "You follow the fresh prints."]
        b = random.randrange(0, 9)
        info = a[b]
        print("I will tell a joke to cheer you up")
        talk("I will tell a joke to cheer you up")
        print(info)
        talk(info)
    elif (("interesting")) in command:
        ask = command.replace("interesting", "")
        a=["Cows don’t actually have four stomachs; they have one stomach with four compartments.","Octopuses have three hearts.","Elephants can’t jump. ","Bats are the only mammal that can actually fly.","The Earl of Sandwich, John Montagu, who lived in the 1700s, reportedly invented the sandwich so he wouldn’t have to leave his gambling table to eat. ","Sliced bread was first manufactured by machine and sold in the 1920s by the Chillicothe Baking Company in Missouri. It was the greatest thing since…unsliced bread?","The tallest man ever recorded was American giant Robert Wadlow (1918–1940), who stood 8 feet 11 inches. Wadlow's size was the result of abnormally enlarged pituitary gland.","There actually aren’t “57 varieties” of Heinz ketchup, and never were. Company founder H.J. Heinz thought his product should have a number, and he liked 57. Hint: Hit the glass bottle on the “57,” not the bottom, to get the ketchup to flow. ","The Barbie doll’s full name is Barbara Millicent Roberts, from Willows, Wisconsin. Her birthday is March 9, 1959, when she was first displayed at the New York Toy Fair.","Three presidents, all Founding Fathers—John Adams, Thomas Jefferson, and James Monroe—died on July 4. Presidents Adams and Jefferson also died the same year, 1826; President Monroe died in 1831. Coincidence? You decide. "]
        b = random.randrange(0, 9)
        info = a[b]
        print(info)
        talk(info)
    elif ("funfact") in command:
        ask = command.replace("funfact", "")
        a=["Cows don’t actually have four stomachs; they have one stomach with four compartments.","Octopuses have three hearts.","Elephants can’t jump. ","Bats are the only mammal that can actually fly.","The Earl of Sandwich, John Montagu, who lived in the 1700s, reportedly invented the sandwich so he wouldn’t have to leave his gambling table to eat. ","Sliced bread was first manufactured by machine and sold in the 1920s by the Chillicothe Baking Company in Missouri. It was the greatest thing since…unsliced bread?","The tallest man ever recorded was American giant Robert Wadlow (1918–1940), who stood 8 feet 11 inches. Wadlow's size was the result of abnormally enlarged pituitary gland.","There actually aren’t “57 varieties” of Heinz ketchup, and never were. Company founder H.J. Heinz thought his product should have a number, and he liked 57. Hint: Hit the glass bottle on the “57,” not the bottom, to get the ketchup to flow. ","The Barbie doll’s full name is Barbara Millicent Roberts, from Willows, Wisconsin. Her birthday is March 9, 1959, when she was first displayed at the New York Toy Fair.","Three presidents, all Founding Fathers—John Adams, Thomas Jefferson, and James Monroe—died on July 4. Presidents Adams and Jefferson also died the same year, 1826; President Monroe died in 1831. Coincidence? You decide. "]
        b = random.randrange(0, 9)
        info = a[b]
        print(info)
        talk(info)
    elif ("fact") in command:
        ask = command.replace("fact", "")
        a=["Cows don’t actually have four stomachs; they have one stomach with four compartments.","Octopuses have three hearts.","Elephants can’t jump. ","Bats are the only mammal that can actually fly.","The Earl of Sandwich, John Montagu, who lived in the 1700s, reportedly invented the sandwich so he wouldn’t have to leave his gambling table to eat. ","Sliced bread was first manufactured by machine and sold in the 1920s by the Chillicothe Baking Company in Missouri. It was the greatest thing since…unsliced bread?","The tallest man ever recorded was American giant Robert Wadlow (1918–1940), who stood 8 feet 11 inches. Wadlow's size was the result of abnormally enlarged pituitary gland.","There actually aren’t “57 varieties” of Heinz ketchup, and never were. Company founder H.J. Heinz thought his product should have a number, and he liked 57. Hint: Hit the glass bottle on the “57,” not the bottom, to get the ketchup to flow. ","The Barbie doll’s full name is Barbara Millicent Roberts, from Willows, Wisconsin. Her birthday is March 9, 1959, when she was first displayed at the New York Toy Fair.","Three presidents, all Founding Fathers—John Adams, Thomas Jefferson, and James Monroe—died on July 4. Presidents Adams and Jefferson also died the same year, 1826; President Monroe died in 1831. Coincidence? You decide. "]
        b = random.randrange(0, 9)
        info = a[b]
        print(info)
        talk(info)
    elif (("i do not know")) in command:
        ask = command.replace("i dont know", "")
        a=["Cows don’t actually have four stomachs; they have one stomach with four compartments.","Octopuses have three hearts.","Elephants can’t jump. ","Bats are the only mammal that can actually fly.","The Earl of Sandwich, John Montagu, who lived in the 1700s, reportedly invented the sandwich so he wouldn’t have to leave his gambling table to eat. ","Sliced bread was first manufactured by machine and sold in the 1920s by the Chillicothe Baking Company in Missouri. It was the greatest thing since…unsliced bread?","The tallest man ever recorded was American giant Robert Wadlow (1918–1940), who stood 8 feet 11 inches. Wadlow's size was the result of abnormally enlarged pituitary gland.","There actually aren’t “57 varieties” of Heinz ketchup, and never were. Company founder H.J. Heinz thought his product should have a number, and he liked 57. Hint: Hit the glass bottle on the “57,” not the bottom, to get the ketchup to flow. ","The Barbie doll’s full name is Barbara Millicent Roberts, from Willows, Wisconsin. Her birthday is March 9, 1959, when she was first displayed at the New York Toy Fair.","Three presidents, all Founding Fathers—John Adams, Thomas Jefferson, and James Monroe—died on July 4. Presidents Adams and Jefferson also died the same year, 1826; President Monroe died in 1831. Coincidence? You decide. "]
        b = random.randrange(0, 9)
        info = a[b]
        print(info)
        talk(info)
    elif ("thankyou") in command:
        print("no problem")
        talk("no problem")
        '''
    elif "how to" or "how can i" in command:
        akk = command.replace("how to","")
        akk = command.replace("how can i","")
        print(akk)
        b=list(akk)
        s=''
        for i in range (0,len(b)):
            if (b[i]==' '):
                b[i]=='+'
                s=s+b[i]
        how_to = HowTo("https://www.wikihow.com/"+akk)
        talk(how_to.steps[0])
            
             
    elif:
            def query():
                user_query = command
                URL = "https://www.google.co.in/seach?q=" + command
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
                }
                page = requests.get(URL, headers=headers)
                soup = BeautifulSoup(page.content, 'html.parser')
                result = soup.find(class_='Z0LcW XcVN5d').get_text()
                talk(result)
            try:
                query()
            except Exception:
                print("No result")
            
            a=input("Enter")
            req = requests.get("https://www.google.com/search?q="+a)
            soup = BeautifulSoup(req.content, "html.parser")
            res = soup.title
            print(soup.get_text())
    '''
    elif (("stop it"))in command:
        exit()
    elif (("please stop"))in command:
        exit()
    elif (("shut up"))in command:
        exit()
    else:
        talk("Not found")
while True:
    run_saffron()
