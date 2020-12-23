import rospy

from playsound import playsound

try:
    audio_path_params = rospy.get_param("/PATH/AUDIO")
    audio_path = audio_path_params

except:
    raise Exception("Missing ROS parameters. Check the launch file.")

def speak(reply, sentiment):
    
    reply = str(reply)
    playsound(audio_path + '/' + sentiment + '/' + reply + '.mp3')