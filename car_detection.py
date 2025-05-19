import cv2
from ultralytics import YOLO

# Araç sınıfları (COCO ID'leri)
vehicle_class_ids = [2, 3, 5, 7]  # car, motorcycle, bus, truck

# Model yükle
model = YOLO('yolov8n.pt')

# Video dosyasını aç
video_path = r"C:\Users\Acer\Downloads\WhatsApp Video 2025-05-19 saat 13.39.58_6e8bc045.mp4"
cap = cv2.VideoCapture(video_path)

# Video çıkışı (opsiyonel)
out = cv2.VideoWriter("output_total_count.mp4", cv2.VideoWriter_fourcc(*'mp4v'), 30,
                      (int(cap.get(3)), int(cap.get(4))))

# ID'leri tutmak için set (benzersiz liste)
counted_ids = set()

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    # Takip ile sonuç al
    results = model.track(frame, persist=True, classes=vehicle_class_ids, verbose=False)

    if results[0].boxes.id is not None:
        ids = results[0].boxes.id.cpu().tolist()
        cls = results[0].boxes.cls.cpu().tolist()

        for obj_id, cls_id in zip(ids, cls):
            if int(cls_id) in vehicle_class_ids:
                if obj_id not in counted_ids:
                    counted_ids.add(obj_id)

    # Sonuçları çiz
    annotated = results[0].plot()

    # Araç sayısını çiz
    cv2.putText(annotated, f"Toplam Araç: {len(counted_ids)}", (30, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 3)

    # Göster
    cv2.imshow("Araç Tespiti", annotated)
    out.write(annotated)

    if cv2.waitKey(1) == 27:  # ESC ile çık
        break

cap.release()
out.release()
cv2.destroyAllWindows()
