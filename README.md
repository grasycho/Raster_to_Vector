An intelligent, heuristic-based Python pipeline that converts messy, rasterized icon images (PNG, JPG) into pixel-perfect, strict [Lucide-compliant](https://lucide.dev/guide/design/icon-design-guide) SVG vectors.

Unlike traditional image tracers (like Potrace or Adobe Image Trace) that blindly trace blurry pixels into distorted and wavy paths, this engine performs **Semantic Geometry Reconstruction**. It analyzes the input image, identifies structural components (frames, dividers, hooks, checkmarks), and completely rebuilds them using pristine, mathematically perfect SVG primitives on a strict 24x24 grid.

## ✨ Key Features

* **True Lucide Compliance:** Automatically enforces Lucide design guidelines, including the 24x24 viewBox, 2px stroke width, rounded caps/joins, and dynamic border radii (`rx="2"` for large shapes, `rx="1"` for small shapes).
* **Semantic Reconstruction:** Doesn't just trace pixels—it understands what a "frame" or a "divider" is, and swaps messy pixels for hardcoded, perfect SVG `<rect>`, `<line>`, and `<path>` tags.
* **Ultra-High Precision (1920px Engine):** Upscales input imagery to a massive 1920x1920 processing canvas (where 1 Lucide grid unit = 80 pixels), allowing for flawless extraction of micro-elements and 2px grid spacing gaps.
* **Aspect Normalization:** Automatically forces asymmetric or oddly-sized input images into a visually centered, perfectly square container before processing, preventing aspect ratio distortion.
* **User-Friendly GUI:** Includes a lightweight Tkinter desktop interface for easy file selection and conversion.

## 🛠️ Requirements

This project requires **Python 3.7+**. The required dependencies are minimal:

* `opencv-python` (for high-definition feature extraction and matrix transformations)
* `numpy` (for rapid matrix and grid calculations)

## 🚀 Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/grasycho/raster-to-lucide.git]
   cd raster-to-lucide

```

2. **Create a virtual environment (Recommended):**
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\\Scripts\\activate

```


3. **Install the dependencies:**
```bash
pip install opencv-python numpy

```



## 💻 Usage

### Launching the GUI

You can start the graphical interface by running the main Python script:

```bash
python main.py

```

*(Alternatively, if you are on Windows, you can simply double-click the provided `run_app.bat` file).*

### Converting an Icon

1. Click **Browse...** to select your raster image (`.png`, `.jpg`, etc.).
2. Click **Generate Lucide Icon**.
3. The engine will process the image, snap the geometry to the 24x24 grid, and prompt you to save the resulting `.svg` file.

## 🧠 Under the Hood: How It Works

1. **Sanitization:** The input image's alpha channels are flattened, and it is padded into a perfect center-of-gravity square.
2. **Matrix Upscaling:** The image is upscaled to 1920x1920. At this resolution, a 2px Lucide stroke becomes exactly 160 pixels wide.
3. **Contour Extraction:** OpenCV isolates individual shape components (ignoring standard noise).
4. **Heuristic Classification:** The script evaluates the scaled boundaries of each component. Is it a large outer box? A horizontal divider? A top mounting hook?
5. **Primitive Swapping:** The script discards the raw, messy contour data and generates clean, native SVG math (`M`, `L`, `<rect>`, `<line>`) snapped explicitly to integer and half-pixel coordinates.
6. **Boilerplate Compilation:** It wraps the deduplicated paths in the official Lucide `<svg>` container configuration.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! If you want to add more heuristic classifications (e.g., detecting perfect circles, arrows, or specific glyphs), feel free to open a Pull Request.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

Distributed under the MIT License. See `LICENSE` for more information.
""")

