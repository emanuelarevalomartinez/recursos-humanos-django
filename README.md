# Human Resources

**Web-based human resources management platform for institutional AE2 and AE3 Excel report generation, processing, visualization, and administrative control built with Django, PostgreSQL, TailwindCSS, and Pandas.**

Human Resources centralizes the management of institutional personnel data, allowing administrators to import Excel datasets, persist information into PostgreSQL, generate AE2 and AE3 reports, visualize historical records, manage users, and create statistical graphics from institutional indicators.

---

# 📌 Description

This project was developed as a web platform focused on the administration and processing of institutional human resources information through Excel-based workflows.

The system allows administrators to:

✔ Upload `.xlsx` files into the platform

✔ Persist imported data into PostgreSQL

✔ Generate institutional AE2 and AE3 reports

✔ Manage users and permissions

✔ Track historical system activity

✔ Visualize statistical indicators through charts

✔ Export structured institutional spreadsheets

The application follows Django’s **Model-View-Template (MVT)** architecture and integrates server-side rendering using Django Templates together with TailwindCSS for the interface layer.

The project structure is organized into multiple functional applications dedicated to domains such as:

- User management
- Excel processing
- Historical records
- Graphical visualization
- Authentication
- Administrative operations

The platform was also developed with coordination and technical collaboration within a shared development environment.

---

# ✨ Main Features

- 🔐 Session-based authentication system

- 👤 User and administrator role management

- 📄 Upload and processing of `.xlsx` files

- 📊 AE2 and AE3 institutional report generation

- 📈 Statistical chart visualization with ApexCharts

- 🕓 Historical operation tracking with pagination

- 🧮 Excel data processing using Pandas and NumPy

- 📑 Automated spreadsheet generation with OpenPyXL

- 🎨 TailwindCSS integration using django-tailwind + npm

- ⚡ PostgreSQL persistence

- 🐳 Dockerized PostgreSQL + pgAdmin environment

---

# 🛠 Tech Stack

| Technology       | Usage                     |
| ---------------- | ------------------------- |
| Django           | Backend framework         |
| Django Templates | Server-side rendering     |
| PostgreSQL       | Database                  |
| TailwindCSS      | Styling                   |
| django-tailwind  | Tailwind integration      |
| Pandas           | Excel data processing     |
| NumPy            | Data operations           |
| OpenPyXL         | Excel generation          |
| ApexCharts       | Statistical graphics      |
| Docker           | Database containerization |
| pgAdmin          | Database administration   |

---

# 📁 Project Structure

```text
RecursosHumanos/
│
├── docker/
├── exel_exports/
├── graphics/
├── main/
├── manage_data/
├── media/
├── static/
├── templates/
├── theme/
├── users/
├── requirements.txt
├── manage.py
└── README.md
```

## 🚀 Installation & Usage

Clone the repository:

```bash
git clone https://github.com/emanuelarevalomartinez/recursos-humanos-django.git
cd recursos-humanos-django
```

### 🐍 Python Virtual Environment

Create the virtual environment depending on your operating system.

### Linux / macOS

```bash
python3 -m venv env
source env/bin/activate
```

### Windows

```bash
python -m venv env
env\Scripts\activate
```

### 📦 Install Dependencies

Install all required Python packages:

```bash
pip install -r requirements.txt
```

## 🐳 Database Setup (PostgreSQL + pgAdmin)

The project includes a Docker environment configured with PostgreSQL and pgAdmin for database persistence and administration.

Start the database services:

```bash
cd docker
docker compose up -d
```

This will start:

- PostgreSQL database on port `5444`
- pgAdmin interface on port `8080`

---

## 🗄 PostgreSQL Configuration

| Variable      | Value              |
| ------------- | ------------------ |
| Database      | `recursos_humanos` |
| User          | `enterprisedb`     |
| Password      | `4444`             |
| Internal Port | `5432`             |
| External Port | `5444`             |

---

## 🌐 pgAdmin Access

pgAdmin URL:

```text
http://localhost:8080
```

Default credentials:

| Field    | Value          |
| -------- | -------------- |
| Email    | `admin@rh.com` |
| Password | `admin123`     |

---

## 🔌 PostgreSQL Connection From pgAdmin

When registering the PostgreSQL server inside pgAdmin, use:

| Field    | Value              |
| -------- | ------------------ |
| Host     | `postgres`         |
| Port     | `5432`             |
| Database | `recursos_humanos` |
| Username | `enterprisedb`     |
| Password | `4444`             |

---

## 🧵 TailwindCSS Setup

Before running the Django server, TailwindCSS must be started in a separate terminal with the virtual environment activated.

```bash
python manage.py tailwind start
```

This command watches and compiles TailwindCSS styles dynamically.

## ▶ Running the Application

Start the Django development server:

```bash
python manage.py runserver
```

By default, the API runs on:

```text
http://localhost:8000
```

---

## ⚠ Initial Administrative Access Setup

The project does not include:

- Default administrator accounts
- Automatic seeders
- Automatic report generation
- Automatic Excel imports

The administrator user must be created manually the first time.

### 🔓 Temporary Access Configuration

Open:

```text
users/views.py
```

Locate the class:

```python
class AdminSession(View):
```

Temporarily comment the cookie validation line:

```python
def get(self, request):
    # if( not request.COOKIES.get('autha')): return redirect('login')
    return render(request, self.template)
```

This temporarily disables route protection for initial setup.

### 👤 Create the First User

With the server running, access:

```text
http://localhost:8000/admin_session/
```

From this panel:

Create a new user
Provide:

- Username
- Email
- Password

#### Important:

Passwords are stored encrypted
Newly created users are created with role `user`

### 🗄 Promote User to Administrator

Open PostgreSQL using pgAdmin or another database manager.

Locate the table:

```text
users_user
```

Find the created user and edit the column:

```text
role
```

Change:

```text
user
```

To:

```text
admin
```

After that, you can log into the platform as administrator and create additional users from the administrative panel.

Once administrative access is working correctly, re-enable route protection by uncommenting the cookie validation line.

---

## 📂 Excel File Workflow

The directory:

```text
media/uploads/
```

does not contain default files.

This folder is used only for uploaded Excel documents.

The backend is currently designed to read only the first Excel file detected inside this folder.

---

## 📄 Excel Templates & Generated Reports

Inside:

```text
docks/
```

the repository includes example Excel documents used by the system:

* `Ae2.xlsx`
* `Ae3.xlsx`
* `datos.xlsx`

These files serve as reference templates for imports and report generation workflows.

## 📊 Generated Institutional Reports

Inside:

```text
static/informes/
```

the system automatically generates the resulting institutional Excel reports:

* `Ae2.xlsx`
* `Ae3.xlsx`

These files represent the exported outputs generated from the processed data stored in PostgreSQL.

## ⚠ Important Import Process Notes

The uploaded Excel file does not require a specific filename to function correctly.

However, it is strongly recommended to upload only a single Excel file at a time into:

```text
media/uploads/
```

The backend is currently designed to automatically detect and process only the first Excel file found inside this directory.

For organizational purposes, using the filename:

```text
datos.xlsx
```

is recommended, although it is not mandatory.

Important distinctions:

* Uploading a file is not the same as importing data
* The file must first be uploaded through the administrator interface
* After uploading, the administrator can execute the import process to persist the Excel data into PostgreSQL
* Only the first detected Excel file inside media/uploads/ will be processed by the backend

## 📊 System Modules

| Module         | Responsibility                     |
| -------------- | ---------------------------------- |
| `users`        | Authentication and user management |
| `manage_data`  | Excel import and data persistence  |
| `exel_exports` | AE2 and AE3 report generation      |
| `graphics`     | Statistical chart visualization    |
| `templates`    | Server-rendered UI views           |
| `theme`        | TailwindCSS configuration          |

---

## 📚 Core Functionalities

The platform supports:

✔ User registration

✔ User authentication

✔ Role management

✔ Historical activity visualization

✔ Uploading Excel files

✔ Importing Excel data into PostgreSQL

✔ AE2 report generation

✔ AE3 report generation

✔ Statistical chart rendering

✔ Institutional spreadsheet exports

✔ Historical pagination

✔ Dynamic form validation

---

## 📝 License

UNLICENSED

---

## 🔗 Repository

[GitHub - Restaurante Presidente Backend](https://github.com/emanuelarevalomartinez/restaurante-backend-nest)
