

!ffmpeg -y -i detections.mp4 -vf "fps=10" -loop 0 detections.gif


from IPython.display import Image
Image(open('./detections.gif','rb').read())

