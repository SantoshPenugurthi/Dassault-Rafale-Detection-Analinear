from ultralytics import YOLO
from PIL import Image

# Load a pretrained YOLOv8n model
model = YOLO('./best.pt')

# Perform object detection
results = model("./Unseen-Image.jpg")

# Show the results
for r in results:
    im_array = r.plot()  # plot a BGR numpy array of predictions
    im = Image.fromarray(im_array[..., ::-1])  # RGB PIL image
    im.show()  # show image
    im.save('results.jpg')  # save image