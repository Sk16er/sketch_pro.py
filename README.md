

⚙️SkETCH_PRO

---


# 📸 Sketch Pro — Auto Image Capture & Sketch Drawing with Turtle

Welcome to **Sketch Pro** — a Python-based project that uses your webcam to **capture images**, convert them into **pencil sketches**, and draw them using **Turtle graphics**! All done automatically with real-time **Windows notifications**.

---

## 🌐 GitHub Repository

🔗 **Project Repo**: [repo](https://github.com/Sk16er/sketch_pro.py)

---

## 🚀 Features

- ✅ Capture live images from your webcam by just pressing the **Space bar**.
- ✅ Auto-convert captured images into beautiful **pencil sketches**.
- ✅ Sketch drawing using **Turtle graphics** for a fun visualization.
- ✅ **Windows system notifications** when:
  - Image is captured and saved.
  - Sketch is created and saved.
- ✅ **No overwrite problem**: Automatically names files to prevent replacing existing ones.
- ✅ Continuous mode: Take multiple photos and sketches without restarting the app.
- ✅ Full paths shown for every saved file.

---

## 📦 Libraries to Install

Make sure to install these Python libraries before running the program:

```bash
pip install opencv-python
pip install numpy
pip install plyer
pip install turtle
pip install wheel
pip install sketchpy
```

---

## 🖥 How It Works

1. **Run the Python script**:
   ```bash
   python main.py
   ```

2. A **live webcam feed** will open.

3. **Press `Space bar`** to:
   - Capture an image.
   - Auto-generate a sketch from the image.
   - Get a Windows notification for file save locations.
   - Automatically start Turtle drawing of the sketch.
   - Resume live webcam feed for next capture!

4. **Press `ESC`** to exit the application anytime.

---

## 📂 File Naming & Saving Logic

- **Captured images** are saved as:
  ```
  captured_image1.jpg, captured_image2.jpg, captured_image3.jpg, ...
  ```

- **Sketches** are saved as:
  ```
  sketch_image1.jpg, sketch_image2.jpg, sketch_image3.jpg, ...
  ```

- ✅ **No overwrite guarantee**: If previous files exist, numbering will continue automatically from the last file.

---

## 🔔 Windows Notifications

After every action:
- **Image captured** notification with file path.
- **Sketch created** notification with file path.

Example:

```
📸 Image Captured
Saved at: C:/Users/YourName/Path/captured_image3.jpg

🎨 Sketch Created
Saved at: C:/Users/YourName/Path/sketch_image3.jpg
```

---

## 💡 How to Use

| Key         | Action                                    |
|-------------|-------------------------------------------|
| `Space bar` | Capture image, generate sketch, draw it   |
| `ESC`       | Exit the program                         |

---

## 📷 Demo Screenshots

_(Some example images — privacy-respecting placeholders)_

- ![Example Image 1](https://github.com/user-attachments/assets/67606422-f23a-471c-adb7-7720582de7a9)
- ![Example Image 2](https://github.com/user-attachments/assets/4447b92a-bdcc-471e-8103-25a70be925d3)
- ![Example Image 3](https://github.com/user-attachments/assets/43df39ee-bc4c-40eb-86b2-c994a9538b81)
- ![Example Image 4](https://github.com/user-attachments/assets/86d08222-54db-4120-8a4f-3ae6c436aa06)
- ![Example Image 5](https://github.com/user-attachments/assets/7af3129d-010b-4e37-b188-89992e7beb41)

---

## ⚡ Bonus: Pikachu Drawing Added!

Now you can **draw Pikachu** using Turtle:

- Check `pika.py` file: [pika.py](https://github.com/Sk16er/sketch_pro.py/blob/main/pika.py)

---

## 📜 License

This project is open-source under the **MIT License**.  
Feel free to use, modify, and distribute it as you wish!

---

## 💬 Contributions & Support

- Feel free to **fork this repo** and make pull requests!
- Found an issue? Open an [Issue](https://github.com/Sk16er/sketch_pro.py/issues).
- Have a suggestion? Start a **Discussion**!
- live at [fuckin_link](https://sk16er.github.io/sketch_pro.py/)

---

### 🚀 Made with ❤️ by [Sk16er](https://github.com/Sk16er)


---

If you want, I can also add **badges** like:
- `Made with Python`
- `MIT License`
- `Open to Contributions`
- `Built with ❤️ by Sk16er`

💬 Let me know if you want me to add those badges on top!

🚀 Ready to publish now! Want me to help prepare `index.md` for a proper GitHub Pages site?
