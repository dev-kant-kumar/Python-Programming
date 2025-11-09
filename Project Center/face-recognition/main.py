import cv2 , dlib  ,time

# load dlib's face detector
detector = dlib.get_frontal_face_detector()

#star main webcam
video = cv2.VideoCapture(0)
video.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
video.set(cv2.CAP_PROP_FRAME_HEIGHT,720)

print("Press 'q' in the video window to quit and 'f to toggle fullscreen")

prev_time = time.time()

while True:
    ret , frame = video.read()
    if not ret:
        break
    # flip the image (mirror effect)
    frame = cv2.flip(frame,1)

    # convert the frame to grayscale
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    # calculates fps
    current_time = time.time()
    fps = 1 / (current_time-prev_time)
    prev_time = current_time

    # detect faces in frame
    faces = detector(gray)

    # draw rectangles around the detected faces
    for i, face in enumerate(faces):
        x, y, w, h = face.left(),face.top(),face.width(),face.height()
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

        # label each face
        cv2.putText(frame,f'Person {i + 1}',(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,255,0),1)

    # display info
    num_faces = len(faces)
    title = "Face Detection System"

    #title - top left
    cv2.putText(frame,title,(20 ,50),cv2.FONT_HERSHEY_DUPLEX,1,(0,0,0),2)

    #face count - top left  (below title)
    cv2.putText(frame,f'Faces {num_faces}',(20,100),cv2.FONT_HERSHEY_SIMPLEX,1,(0,165,255),2)

    # fps
    cv2.putText(frame,f'FPS: {int(fps)}',(20,150),cv2.FONT_HERSHEY_SIMPLEX,0.7,(255,255,0),2)

    # status - top right
    status = "Active" if num_faces > 0 else "Searching face..."
    color = (0,255,0) if num_faces >0 else (0,0,255)
    position =  (frame.shape[1]-100,50) if num_faces > 0 else (frame.shape[1]-300,50)
    
    cv2.putText(frame,status,position,cv2.FONT_HERSHEY_SIMPLEX,1,color,2)

    # resolution (below status)
    cv2.putText(frame,f'Resolution: {frame.shape[1]}x{frame.shape[0]}',(frame.shape[1]-240,100),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,0,0),1)




    # show frame
    cv2.imshow('Face Recognition System',frame)

    # exit on 'q' key press and 'f' to toggle fullscreen
    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break
    elif key == ord('f'):
        current = cv2.getWindowProperty('Face Recognition System',cv2.WND_PROP_FULLSCREEN)
        if current == cv2.WINDOW_FULLSCREEN:
            cv2.setWindowProperty('Face Recognition System',cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_NORMAL)
        else:
            cv2.setWindowProperty('Face Recognition System',cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)





# cleanup
video.release()
cv2.destroyAllWindows()
print("Camera release. Program ended")
