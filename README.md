# CV Reader Application

This Python application presents CV data through a REST API and a Command-Line Interface (CLI). It provides information about personal details, education, work experience and skills. You can retrieve the data using HTTP GET requests to specific endpoints or by running a CLI command. The CV data can be read from a JSON file.

## Requirements
This application requires Docker and Docker Compose. No other specific requirements are needed.

## Files
- `routes/cv.py`: Defines the routes for the CV data REST API.
- `crud/cv.py`: Contains the function to fetch CV data from a JSON file.
- `cv.json`: JSON file that stores your CV data.
- `manage.py`: The CLI command for retrieving CV data.
- `Makefile`: Contains handy Makefile commands to build, start and stop the application.

## How to Use
1. Clone this repository to your local machine.
2. To build and start the application, use the following command:
   ```
   make build && make up
   ```
3. The CV data is accessible (**at http://localhost:5002/**) via the following endpoints:

   - **GET /cv/personal**: Personal information.
   - **GET /cv/experience**: Work experience details.
   - **GET /cv/education**: Educational background.
   - **GET /cv/skills**: List of skills.

4. To retrieve CV data via the Flask CLI command, use the following command:

   ```
   python manage.py section
   ```

   You will be prompted to enter the section you want to retrieve (e.g., 'personal', 'experience', 'education', or 'skills').

## Available Sections
- **personal**: Personal information including name, phone, email, LinkedIn and GitHub.
- **experience**: Work experience details with titles, companies, locations, dates and descriptions.
- **education**: Educational background with institutions, degrees, locations and dates.
- **skills**: List of languages, frameworks, libraries, development tools, clouds and other skills.

## Docker Commands
- `make build`: Builds the Docker containers for the application.
- `make up`: Starts the application.
- `make down`: Stops and removes the Docker containers and volumes.

## Docker Container Access
- `make connect_main`: Connects to the main application container.
- `make connect_main_root`: Connects to the main application container with root privileges.

Remember to stop the application using `make down` when you are done using it.

Enjoy exploring your CV data through the REST API or the CLI command!
