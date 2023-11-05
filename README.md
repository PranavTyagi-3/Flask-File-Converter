# File Conversion Web Application

This Flask-based web application allows users to convert files from one format to another. Users can upload files of specific types, and the application provides options to convert them to the desired format. The application supports several file conversion options.

## Prerequisites

Before running the application, ensure that you have the following Python libraries installed:

- Flask
- Pillow (PIL)
- moviepy

You can install these libraries using `pip`:

```bash
pip install flask pillow moviepy
```

## Functionality

The web application offers the following features:

1. **Convert WebM to MP4**: Users can upload WebM video files and convert them to MP4 format. The converted file can then be downloaded.

2. **Convert WAV to MP3**: Users can upload WAV audio files and convert them to MP3 format. The converted file can be downloaded.

3. **Convert PNG to JPG**: Users can upload PNG image files and convert them to JPG format. The converted image can be downloaded.

4. **Convert WebP to PNG**: Users can upload WebP image files and convert them to PNG format. The converted image can be downloaded.

5. **Convert WebP to JPG**: Users can upload WebP image files and convert them to JPG format. The converted image can be downloaded.

The application also handles errors gracefully, such as when users attempt to upload files of the wrong format.

## How to Run the Application

1. Clone the repository to your local machine.

2. Make sure you have the required Python libraries installed, as mentioned in the prerequisites.

3. Create a folder named `static` in the project directory to store uploaded files. Inside the `static` folder, create a subfolder named `uploads`. This is where uploaded files will be stored.

   ```bash
   mkdir static
   mkdir static/uploads
   ```

4. In the terminal, navigate to the project directory containing the `app.py` file.

5. Run the Flask application using the following command:

   ```bash
   python app.py
   ```

6. Once the application is running, open a web browser and go to `http://localhost:5000` to access the application.

## Using the Application

- Navigate to the desired conversion option from the main page.

- Upload a file of the specified format for conversion.

- The application will check if the uploaded file is of the correct format. If it is, the file will be converted and made available for download.

- Users can click the "Download" link to download the converted file.

## Adding More Conversion Options

To add more file conversion options, follow the same pattern as existing options in the code:

1. Create a new route function in `app.py` for the desired conversion, similar to the existing ones.

2. Modify the HTML templates in the `templates` folder to include a new form for the conversion.

3. Update the route for file download (`/downl/<id>`) to handle the conversion and download for the new format.

4. Add the corresponding Python library or method for the new conversion task if needed.

5. Ensure the new file format is supported and properly validated in the form handling logic.

## Acknowledgments

This application was created as a utility tool for file format conversion. It serves as a simple example of how to create a Flask web application for file conversion. Users can further enhance and customize the application to support additional file formats and conversion options as per their requirements.
