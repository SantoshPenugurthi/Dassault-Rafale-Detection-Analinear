from ultralytics import YOLO
from PIL import Image

# Load a pretrained YOLOv8n model
model = YOLO('yolov8n.pt')
# model = YOLO('yolov8n-seg.pt')
# model = YOLO('yolov8n-pose.pt')
# model = YOLO('yolov8n-cls.pt')

# Define path to the image file
# source="https://cdn.britannica.com/79/232779-050-6B0411D7/German-Shepherd-dog-Alsatian.jpg"
source = './Unseen-Image.jpg'

# Run inference on the source
results = model(source)  # list of Results objects

# Show the results
for r in results:
    im_array = r.plot()  # plot a BGR numpy array of predictions
    im = Image.fromarray(im_array[..., ::-1])  # RGB PIL image
    im.show()  # show image
    # im.save('results.jpg')  # save image
