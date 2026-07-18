# Distributed Task Scheduler

A distributed task scheduling system built with **Python, FastAPI, Redis, and worker processes**. The goal of this project is to design a system where multiple workers can process tasks from a shared queue with features like job tracking, retries, scheduling, and fault tolerance.

## 🚀 Project Overview

In a real-world application, long-running tasks such as:

* Sending emails
* Generating reports
* Processing files
* Running ML pipelines
* Data processing jobs

should not block the main application.

This project implements a task scheduler where:

1. A client submits a job through an API.
2. The job is stored and queued.
3. Worker processes pick up available tasks.
4. Workers execute tasks independently.
5. Job status is updated throughout the lifecycle.

---

## 🏗️ System Architecture

```
                Client
                  |
                  |
                  v
            FastAPI Server
                  |
                  |
                  v
             Job Manager
                  |
                  |
                  v
             Redis Queue
                  |
        ---------------------
        |                   |
        v                   v
    Worker 1            Worker 2
        |                   |
        ---------------------
                  |
                  v
            Task Execution
```

---

## ✨ Features

### Current Features

* ✅ FastAPI backend setup
* ✅ Pydantic-based request validation
* ✅ Job creation API
* ✅ Unique job ID generation using UUID
* ✅ Job status management
* ✅ In-memory job storage
* ✅ Retrieve job details by ID
* ✅ API error handling

### Planned Features

* ⬜ Redis-based distributed queue
* ⬜ Multiple worker processes
* ⬜ Background task execution
* ⬜ Job retry mechanism
* ⬜ Failure handling
* ⬜ Scheduled and recurring jobs
* ⬜ Persistent database storage
* ⬜ Real-time monitoring dashboard
* ⬜ Worker health monitoring

---

## 🛠️ Tech Stack

### Backend

* Python
* FastAPI
* Pydantic

### Queue & Distributed Processing

* Redis
* Multiprocessing / Worker Processes

### Storage

* In-memory storage (current)
* PostgreSQL (planned)

### Development Tools

* Git
* GitHub
* Uvicorn

---

## 📂 Project Structure

```
distributed-task-scheduler/
│
├── app/
│   ├── models/
│   │   └── job.py              # Job data models
│   │
│   ├── services/
│   │   └── job_service.py      # Job business logic
│   │
│   ├── storage/
│   │   └── memory.py           # Temporary job storage
│   │
│
├── tests/                      # Test cases
│
├── main.py                     # FastAPI application
├── requirements.txt            # Dependencies
├── README.md
└── .gitignore
```

---

# ⚙️ Installation & Setup

## 1. Clone the repository

```bash
git clone https://github.com/ishita-chandraa/Distributed-task-scheduler.git

cd Distributed-task-scheduler
```

---

## 2. Create virtual environment

```bash
python3 -m venv venv
```

Activate it:

### Linux / WSL

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Run the application

```bash
uvicorn main:app --reload
```

The server will start at:

```
http://127.0.0.1:8000
```

API documentation:

```
http://127.0.0.1:8000/docs
```

---

# 📌 API Documentation

## Create a Job

### POST `/jobs`

Creates a new task.

### Request

```json
{
  "task": "send_email",
  "payload": {
    "to": "abc@gmail.com"
  }
}
```

### Response

```json
{
  "id": "8fd0f1c3-09b4-46d8-8351-b42cdc082bda",
  "status": "pending",
  "task": "send_email",
  "payload": {
    "to": "abc@gmail.com"
  }
}
```

---

## Get Job Details

### GET `/jobs/{job_id}`

Retrieves information about a specific job.

Example:

```
GET /jobs/8fd0f1c3-09b4-46d8-8351-b42cdc082bda
```

Response:

```json
{
  "id": "8fd0f1c3-09b4-46d8-8351-b42cdc082bda",
  "status": "pending",
  "task": "send_email",
  "payload": {
    "to": "abc@gmail.com"
  }
}
```

If the job does not exist:

```json
{
  "detail": "Job not found"
}
```

---

# 🧠 Concepts Implemented

This project demonstrates:

* REST API design
* Backend architecture
* Separation of concerns
* Data validation
* Service layer pattern
* Job lifecycle management
* Distributed task processing concepts

---

# 🎯 Future Improvements

The next phase of development will introduce:

### Distributed Queue

Replacing in-memory storage with Redis:

```
API
 |
 v
Redis Queue
 |
 v
Workers
```

### Worker System

Multiple workers will:

* Pull tasks from the queue
* Execute jobs independently
* Update job status

### Reliability Features

* Automatic retries
* Timeout handling
* Failed job recovery
* Worker monitoring

---

## 👩‍💻 Author

**Ishita Chandra**

GitHub:
https://github.com/ishita-chandraa

---

## ⭐ Project Status

🚧 Currently under active development.

The project is being built incrementally to explore backend engineering and distributed systems concepts.
