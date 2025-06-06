# Noble_ANA-680_FINAL

This repository contains the final project for ANA 680 by J-Nobull.  
It includes:  
- A Jupyter Notebook for data analysis
- A Flask web application
- Supporting files for deployment and reproducibility
- Datafiles

## Contents

- **Noble_ANA680_Final.ipynb**: The main Jupyter Notebook containing the data analysis and modeling steps.
- **app.py**: Flask application to serve the model or analysis results.
- **Final.pkl**: Serialized (pickle) machine learning model.
- **requirements.txt**: List of required Python packages.
- **Dockerfile**: Configuration for containerizing the application.
- **Procfile**: For deployment on Heroku (or similar platform).
- **templates/**: Directory for HTML templates used by the Flask app.
- **LICENSE**: Repository license.
- **.gitignore**: Files and directories excluded from version control.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/J-Nobull/Noble_ANA-680_FINAL.git
   cd Noble_ANA-680_FINAL
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Jupyter Notebook

Open and run `Noble_ANA680_Final.ipynb` for step-by-step analysis.

### Flask App

To run the Flask app locally:
```bash
python app.py
```
The app will be available at `http://127.0.0.1:5000/`.

### Docker

To build and run the Docker container:
```bash
docker build -t noble-ana680-final .
docker run -p 5000:5000 noble-ana680-final
```

## Deployment

This project includes a `Procfile` for deployment to cloud platforms like Heroku.  
Make sure to set up the appropriate environment variables, if required.

## Requirements

- Python 3.x
- Packages in `requirements.txt`:
  - pandas, numpy, scipy, scikit-learn, seaborn, matplotlib, flask, joblib, gunicorn

## License

See the [LICENSE](LICENSE) file for license information.
