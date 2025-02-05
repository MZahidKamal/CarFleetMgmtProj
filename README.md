# Car Fleet Management System

🚗 **Car Fleet Management System** is a **web-based platform** designed for **Lynk&Co Car Company**, covering the **entire vehicle lifecycle** from manufacturers and dealers to final delivery to customers. This system streamlines the fleet management process, ensuring seamless coordination between car manufacturers, dealers, drivers, and customers.

### 🔥 Key Features  
- **Car Inventory Management**:  
  - Car manufacturers and dealers can **add, update, and manage** car models and details.  
  - Vehicle specifications, images, and documents are stored in the system.  

- **Dealer & Driver Management**:  
  - Dealers can **register cars, assign drivers**, and track fleet movements.  
  - Drivers can be appointed by car dealers for vehicle pickup and delivery.  

- **Car Pickup Process**:  
  - A driver **picks up the car** from the dealer.  
  - The system records **car details, images, and necessary documentation**.  
  - A **pickup report** is generated and stored.  

- **Car Delivery Process**:  
  - The driver **delivers the car to the client’s location**.  
  - **Final vehicle inspection** is performed, and images are recorded.  
  - The client **signs digitally** to confirm the successful delivery.  

- **Automated Reporting & History Tracking**:  
  - **Comprehensive reports** are generated at each step of the process.  
  - These reports are **accessible by car dealers, manufacturers, and clients**, ensuring **full transparency** in the fleet management system.  

This **Django-powered** system ensures a structured and **efficient workflow**, reducing manual errors and improving the overall **car fleet management experience**. 🚀  
  

Built with **Django, MySQL, Bootstrap**, and hosted on **AWS EC2**.

## 🚀 Features
- Manage car fleet inventory, dealers, and customer orders  
- User authentication and role-based access control  
- Seamless integration with AWS for storage  
- Responsive UI built with Bootstrap  
- REST API powered by Django REST Framework  

## 📑 Table of Contents
- [Installation](#installation)  
- [Usage](#usage)  
- [Configuration](#configuration)  
- [Dependencies](#dependencies)  
- [Troubleshooting](#troubleshooting)  
- [Contributing](#contributing)  
- [License](#license)  

---

Here is the corrected `.md` format with proper spacing and line breaks:


## 🛠 Installation

### 1. Clone the repository
```bash
git clone https://github.com/MZahidKamal/CarFleetMgmtProj.git
cd CarFleetMgmtProj
````

### 2. Set up a virtual environment

```bash
python -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a `.env` file in the root directory and configure:

```plaintext
DEBUG=True
DATABASE_URL=postgres://user:password@localhost:5432/car_fleet_db
AWS_STORAGE_BUCKET_NAME=your-bucket-name
```

### 5. Run database migrations

```bash
python manage.py migrate
```

### 6. Start the development server

```bash
python manage.py runserver
```

The website should now be accessible at `http://127.0.0.1:8000/`.

---

## 🎮 Usage

- Admin can **add, edit, and delete** fleet cars
- Dealers can **manage vehicle allocations**
- Customers can **view and order cars**
- API endpoints for **integrations**

---

## ⚙️ Configuration

Modify `settings.py` to adjust database settings, AWS storage, and other configurations.

Example for **PostgreSQL**:

```python
DATABASES = {
    'default': dj_database_url.config(default=os.getenv('DATABASE_URL'))
}
```


---

## 🎮 Usage

- Admin can **add, edit, and delete** fleet cars
- Dealers can **manage vehicle allocations**
- Customers can **view and order cars**
- API endpoints for **integrations**

---

## ⚙️ Configuration

Modify `settings.py` to adjust database settings, AWS storage, and other configurations.

Example for **PostgreSQL**:

```python
DATABASES = {
    'default': dj_database_url.config(default=os.getenv('DATABASE_URL'))
}
```

---

## 📦 Dependencies

The project relies on the following key dependencies (full list in `requirements.txt`):

- **Django 5.0.4** - Web framework
- **Django REST Framework** - API support
- **PostgreSQL/MySQL** - Database
- **Bootstrap 5** - Frontend UI
- **AWS S3 (django-storages)** - Cloud storage

Install all dependencies using:

```bash
pip install -r requirements.txt
```

---

## 🔧 Troubleshooting

- **Database errors?** Ensure PostgreSQL/MySQL is running and `.env` is correctly configured.
- **AWS storage issues?** Check your AWS credentials and bucket permissions.
- **Server not starting?** Run `python manage.py migrate` before `runserver`.

---

## 👨‍💻 Contributing

Feel free to fork this repository and submit pull requests! Contributions are welcome.

---

## 📜 License

This project is licensed under the **MIT License**.

---

🚀 **Developed with Django, Bootstrap, and AWS**  
🔗 [GitHub Repository](https://github.com/MZahidKamal/CarFleetMgmtProj)

```
Let me know if you need any modifications! 😊🚀
```

---
