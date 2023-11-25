from ultralytics import YOLO
from PIL import Image

# Load a pretrained YOLOv8n model
model = YOLO('./Best_Trained_Model_with_Custom_Dataset/best.pt')

# Define path to the image file
source = './Input/task2-test.jpg'

# Run inference on the source
results = model(source)  # list of Results objects

# Show the results
for r in results:
    im_array = r.plot()  # plot a BGR numpy array of predictions
    im = Image.fromarray(im_array[..., ::-1])  # RGB PIL image
    im.show()  # show image
    im.save('./Output/task2-result_.jpg')  # save image