from ultralytics import YOLO
import tempfile

# Load YOLO model once
yolo_model = YOLO("yolov8s.pt")

def analyze_image(uploaded_file):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp:
        tmp.write(uploaded_file.read())
        img_path = tmp.name

    result = yolo_model(img_path)[0]
    person_count = sum(1 for box in result.boxes if result.names[int(box.cls)] == "person")

    # Skip additional analysis
    return person_count, {}
