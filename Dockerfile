FROM python:3.7.3-stretch
invalid
## Step 1:
# Create a working directory
WORKDIR /app

# added this line to fix the error during lint
ENV PIP_NO_CACHE_DIR=1

## Step 2:
# Copy source code to working directory
COPY app.py /app/
COPY Makefile /app/
COPY requirements.txt /app/
COPY templates /app/templates
COPY static /app/static

## Step 3:
# Install packages from requirements.txt
# hadolint ignore=DL3013
RUN pip install --upgrade pip setuptools wheel --use-pep517 pip &&\
	pip install -r requirements.txt

## Step 4:
# Expose port 5000
EXPOSE 5000

## Step 5:
# Run app.py at container launch
CMD ["python", "app.py"]