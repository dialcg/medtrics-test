# MedTrics Sessions

This web app helps you check session schedules for school courses. 
It uses Django for the backend and Vue.js for the frontend, and packaged up with Docker.

## Table of Contents

- [Architecture](#architecture)
  - [Layered Architecture](#layered-architecture)
  - [Service-Oriented Architecture](#service-oriented-architecture)
- [Setup and Installation](#setup-and-installation)
  - [Prerequisites](#prerequisites)
  - [Docker Setup](#docker-setup)
- [Running the Application](#running-the-application)
  - [Backend](#backend)
  - [Frontend](#frontend)
- [Testing](#testing)


## Architecture

### Layered Architecture

The app follows a **layered architecture** to keep things organized:

1. **Presentation Layer:** It’s built with Vue.js and totally decoupled from the backend.
2. **Service Layer:** This handles the business logic. It’s where the core functionality lives.
3. **Data Access Layer:** This layer deals with the database. It’s built using Django models and repositories.

### Service-Oriented Architecture

The app is also designed with a **service-oriented approach**:

- **Backend:** The backend manages different services, like session schedules and locations, and exposes them through a RESTful API.
- **Frontend:** The frontend interacts with backend services.

## Setup and Installation

### Prerequisites

Make sure you have Docker and Docker Compose installed on your machine.

### Docker Setup

1. **Clone the repository:**

   ``git clone https://github.com/yourusername/medtrics-sessions.git``

   ``cd medtrics-sessions``

2. **Go to the `deploy` directory:**

   `cd deploy`

3. **Build and start the Docker containers:**

   `docker-compose up --build`

   This command builds the Docker images for both the backend and frontend and starts the containers.

## Running the Application

### Backend

- The backend runs on port `8000` by default.
- It provides endpoints for listing session schedules, courses and locations.

### Frontend

- The frontend runs on port `80` by default bridged by Ngnix.
- It’s the interface you’ll use to interact with the session schedules search and filtering.

## Testing

### Running Tests

To run tests for the backend, use:

`docker-compose exec backend pytest`

This will execute the tests and give you feedback on your code.

