# Scanner_py

`Scanner_py` is a document scanner application built using Python, OpenCV, and other supporting libraries. It allows you to detect and scan documents from images, perform perspective transformations, and apply thresholding for clear document scans.

## Features

- **Document Detection**: Detects the contour of a document from an image.
- **Perspective Transformation**: Applies a perspective transformation to get a top-down view of the document.
- **Thresholding**: Applies local thresholding to enhance the clarity of the scanned document.
- **Image Display and Saving**: Displays intermediate results and saves the final scanned image.

## Requirements

- Python 3.x
- OpenCV
- NumPy
- imutils
- scikit-image

You can install the required packages using `pip`. The dependencies are listed in `requirements.txt`.

## Installation

1. **Clone the Repository**

   ```sh
   git clone https://github.com/yourusername/scanner_py.git
   cd scanner_py
   ```

2. **Install Dependencies**

   Make sure you have Python 3 installed. Install the required packages using:

   ```sh
   pip install -r requirements.txt
   ```

## Usage

### Command-Line Interface

You can run the document scanner directly from the command line:

```sh
python scanner.py <image_path> [--output_path <output_path>]
```

- `<image_path>`: Path to the input image file.
- `--output_path <output_path>`: Optional. Path to save the output image (default is `./scan.png`).

#### Example

To process an image and save the output as `scan.png`, use:

```sh
python scanner.py ../img/omr10.jpg
```

To specify a different output path:

```sh
python scanner.py ../img/omr10.jpg --output_path ./output_scan.png
```

### Importing as a Module

You can also import the functions into another Python script or project:

```python
from scanner import main

# Run the document scanner
main('../img/omr10.jpg', './output_scan.png')
```

## Code Structure

- `scanner.py`: The main script for scanning documents. Contains functions for loading images, processing, and saving results.
- `transform.py`: Contains helper functions for perspective transformation.
- `requirements.txt`: Lists the Python packages required to run the code.

## Contributing

Contributions are welcome! To contribute:

1. **Fork the Repository**: Create a personal copy of the repository.
2. **Create a Branch**: Create a new branch for your changes.
3. **Make Changes**: Implement your changes or new features.
4. **Submit a Pull Request**: Open a pull request with a description of your changes.

Please ensure that your code adheres to the existing coding style and passes any tests before submitting a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions or feedback, you can reach out to:

- [Your Name](https://github.com/yourusername)

---

Feel free to customize further, including replacing placeholders like `yourusername` with your actual GitHub username and adjusting the file paths and names as necessary.
