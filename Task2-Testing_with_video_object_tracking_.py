import cv2
from ultralytics import YOLO

# Load the YOLOv8 model
model = YOLO('./Best_Trained_Model_with_Custom_Dataset/best.pt')

# Open the video file
video_path = "./Input/task2-test.mp4"
cap = cv2.VideoCapture(video_path)

# Get the video's width, height, and frames per second (fps)
width = int(cap.get(3))
height = int(cap.get(4))
fps = cap.get(5)

# Define the codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # You can choose another codec based on your needs
output_video_path = "./Output/task2-output-video1.mp4"
out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

# Loop through the video frames
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()

    if success:
        # Run YOLOv8 tracking on the frame, persisting tracks between frames
        results = model.track(frame, persist=True)

        # Visualize the results on the frame
        annotated_frame = results[0].plot()

        # Write the annotated frame to the output video file
        out.write(annotated_frame)

        # Display the annotated frame
        cv2.imshow("YOLOv8 Object Tracking", annotated_frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        # Break the loop if the end of the video is reached
        break

# Release the video capture object, video writer, and close the display window
cap.release()
out.release()
cv2.destroyAllWindows()
