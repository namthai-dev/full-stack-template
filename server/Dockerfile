# Use the official Python image as the base image
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy only the dependency files to the container first
COPY poetry.lock pyproject.toml /app/

# Install poetry
RUN pip install --no-cache-dir poetry

# Install dependencies using poetry
RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

# Copy the rest of the application code into the container
COPY . /app/

# Expose any ports that the application uses
EXPOSE 8000

# Define the command to run the application when the container starts
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
