# Django Weather App

Simple Django application that displays current weather for a city using a public weather API.

## Features
- **City search** to fetch current weather
- **Clean UI** with basic styling
- **Server-side rendering** with Django templates

## Tech Stack
- **Backend:** Django (Python)
- **Templates:** Django Templates (HTML)
- **HTTP:** requests (or built-in urllib)

## Prerequisites
- Python 3.10+
- pip / venv

## Getting Started
1. Clone the repository
   - Replace with your GitHub link below once you publish.
   - Example:
     ```bash
     git clone https://github.com/SanjeewaRupasinghe/weather_app-django.git
     cd weather_app-django
     ```

2. Create and activate a virtual environment
   ```bash
   python -m venv .venv
   # Windows
   .venv\\Scripts\\activate
   # macOS/Linux
   # source .venv/bin/activate
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```
   If a requirements file is not present, you can install the basics:
   ```bash
   pip install django requests python-dotenv
   ```

4. Configure environment variables
   - Create a `.env` file in the project root with:
     ```env
     API_KEY=your_api_key_here
     ````

6. Run the development server
   ```bash
   python manage.py runserver
   ```
   Visit http://127.0.0.1:8000/

## Usage
- Enter a city name on the home page to view current weather data.
- Ensure `API_KEY` is valid (e.g., from OpenWeatherMap).

## Environment Variables
- `API_KEY`: API key from your weather provider

## Project Structure (simplified)
```
weatherapp/           # Django project settings
weather/              # Django app (views, urls, templates)
  templates/          # HTML templates (e.g., index.html)
manage.py
```

## Deployment
- Use environment variables for secrets in production
- Set `DEBUG=False`
- Configure `ALLOWED_HOSTS` in `settings.py`
- Collect static files if applicable:
  ```bash
  python manage.py collectstatic
  ```

## Troubleshooting
- If API calls fail, verify `API_KEY` and network access.
- If templates don't render, confirm template dirs in `settings.py`.
- For Windows venv activation issues, ensure execution policy allows scripts.

## License
This project is licensed under the MIT License. See `LICENSE` if provided.

## Author & Links
- **Author:** Sanjeewa Rupasinghe (https://sanjewa.com)
- **GitHub:** https://github.com/SanjeewaRupasinghe
- **Repository:** https://github.com/SanjeewaRupasinghe/weather_app-django

---