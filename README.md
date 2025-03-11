# Todo List  

A simple **Todo List** project built using **Django** for the backend and **Bootstrap** for the frontend.  

---  

## 🚀 Features  
✅ Add new tasks  
✅ Edit existing tasks  
✅ Delete tasks  
✅ Mark tasks as complete or incomplete  
✅ Sort tasks by status  

---  

## 🛠️ Technologies Used  
- **Django** – Python-based backend framework  
- **Bootstrap** – Frontend styling and UI framework  
- **SQLite** – Default database for Django  

---  

## 📂 Project Setup  

### 1. 💾 Clone the Repository  
```bash  
git clone https://github.com/mahdi-rezayi/todo_list_django.git
```

### 2. 🗄️ Apply Migrations
```bash 
python manage.py makemigrations  
python manage.py migrate
```

### 3. 🚀 Start the Development Server
```bash 
python manage.py runserver
```
## 📋 API Endpoints (Optional)
| Method | Endpoint | Description |
|---------|-----------|-------------|
| `GET` | `/` | Display the list of tasks |
| `POST` | `/add/` | Add a new task |
| `POST` | `/edit/<id>/` | Edit a task |
| `POST` | `/delete/<id>/` | Delete a task |

## 🌟 Contributing
This is a personal project. If you have suggestions or improvements, feel free to submit a **Pull Request** or open a **New Issue**. 🙌

## 📝 License
This project is licensed under the **MIT License**.
