# Multi-Face Detection & Tracking using OpenCV 🎥🤖

This project detects **multiple moving faces** in real-time using OpenCV's **Haar Cascade Classifier**. It highlights detected faces with rectangles and tracks them as they move.

## 🚀 Features
- ✅ Detects **multiple faces** simultaneously.
- ✅ Works **in real-time** using a webcam.
- ✅ Draws **bounding boxes** around faces.
- ✅ Press **'f'** to exit the program.

## 🛠 Installation

### 1️⃣ Clone this repository:
```bash
git clone https://github.com/yourusername/face-detection.git
cd face-detection
```

### 2️⃣ Install dependencies:
```bash
pip install opencv-python
```

## 🎯 Usage
Run the script to start face detection:
```bash
python face_detection.py
```
💡 **Make sure your webcam is connected!**

## 🔍 How It Works
1. **Opens the webcam** and continuously captures frames.
2. **Converts frames to grayscale** for better detection.
3. **Uses Haar cascade classifier** to detect multiple faces.
4. **Draws a green rectangle** around detected faces.
5. **Tracks faces** as they move across the frame.
6. **Press 'f' to exit** the detection window.

## 🛠 Troubleshooting
| Issue                     | Solution |
|---------------------------|----------|
| Webcam not opening | Ensure it's connected and not in use by another app. |
| Faces not detected | Improve lighting or adjust `scaleFactor` & `minNeighbors`. |
| Laggy detection | Reduce frame size by setting `video_cap.set(3, 640)` & `video_cap.set(4, 480)`. |

## 📌 Future Improvements
- 🔹 Use **Deep Learning (DNN)** for better face detection.
- 🔹 Implement **face recognition** to identify people.
- 🔹 Add **face tracking algorithms** (KCF, MOSSE).

## 📜 License
This project is licensed under the **MIT License**.

---

Made with ❤️ using OpenCV.  
**Contributions & feedback are welcome!** 🚀

