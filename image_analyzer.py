from ultralytics import YOLO
import tempfile

yolo_model = YOLO("yolov8s.pt")

def analyze_image(uploaded_file):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp:
        tmp.write(uploaded_file.read())
        img_path = tmp.name

    results = yolo_model(img_path)[0]

    person_count = 0
    CONFIDENCE_THRESHOLD = 0.5  # Try 0.5 to 0.7 for more precision

    for box in results.boxes:
        cls_id = int(box.cls)
        label = results.names[cls_id]
        confidence = float(box.conf)

        if label == "person" and confidence >= CONFIDENCE_THRESHOLD:
            person_count += 1

    return person_count, {}
