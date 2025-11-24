# Learning Flask

A collection of Flask projects for learning web development.

## Projects

### 1. Task Smash (simple_project)
A simple task management app where you can:
- Add new tasks
- View all tasks with creation date
- Edit existing tasks
- Delete tasks

**To run:**
```bash
cd simple_project
python app.py
```
Then open `http://localhost:5000` in your browser.

### 2. Get_Post
A Flask application demonstrating GET and POST requests with file handling.

**To run:**
```bash
cd Get_Post
python app.py
```

### 3. First_Project
An introductory Flask project.

**To run:**
```bash
cd First_Project
python app.py
```

## Setup

1. **Create a virtual environment:**
   ```bash
   python -m venv venv
   ```

2. **Activate the virtual environment:**
   - Windows: `venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Technologies Used
- Flask
- SQLAlchemy
- Jinja2 Templates
- Bootstrap 4

## Notes
- Each project has its own `app.py` file
- Database files (*.db) are ignored by `.gitignore`
- Static files (CSS, images) are in each project's `static/` folder