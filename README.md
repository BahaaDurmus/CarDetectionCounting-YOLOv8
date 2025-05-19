# 🚗 CarDetectionCounting-YOLOv8

Gerçek zamanlı araç tespiti ve toplam araç sayımı yapan YOLOv8 tabanlı Python projesi.  
Bu proje, bir videodaki araçları tespit eder, her araca ID atar ve sahneden geçen toplam araç sayısını takip eder.

---

## 🔧 Kullanılan Teknolojiler

- Python 3.10
- [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)
- OpenCV (cv2)
- Conda ortamı / pip kurulumu destekli

---

## 📂 Proje Dosya Yapısı

CarDetectionCounting-YOLOv8/
├── car_detection.py # Ana Python dosyası
├── environment.yml # Conda ortam dosyası
├── requirements.txt # pip için bağımlılıklar
├── LICENSE # MIT lisansı
└── README.md # Proje dökümantasyonu

> **Not:** `output_detected.mp4`, `runs/`, `.pt` gibi dosyalar `.gitignore` ile dışlanmıştır.

---

## ⚙️ Ortam Kurulumu

### Conda ile:
```bash
conda env create -f environment.yml
conda activate car_detection
```

pip ile:
pip install -r requirements.txt

▶️ Projeyi Çalıştırma
python car_detection.py

Örnek için projede kullanabileceğiniz youtube videosu
https://youtu.be/MNn9qKG2UFI?si=T-ZxfSr0Xecrhqjn


🛡️ Lisans
Bu proje MIT Lisansı ile lisanslanmıştır.
Kod özgürce kullanılabilir, değiştirilebilir ve paylaşılabilir.

✉️ İletişim
Her türlü öneri, katkı veya soru için: durmusoglubahadir@gmail.com



