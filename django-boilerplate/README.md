# Django Boilerplate (v1.0.0)

Django boilerplate code based on Django 2.0 and Python 3

## Features

- Dotenv support to set environment variables from .env file.
- Logging middleware for request and response.
- Custom authentication middleware.
- Request validation middleware.
- Exception handling middleware for error handling.
- Custom http error utils having exceptions to be raised for returning standard JSON response.
- Custom http response utility classes.
- Overridden django error views for standard http error reporting.
- Logging utilities.
- Mongo (v3.6) model support with pymodm + default model managers.
- Elasticsearch  (v2.3) utilities.
- JSON utils to encode python datatypes as needed.
- Request client for external requests.

## Project Setup

1. Fork and clone it on your local system
2. Create and activate virtual environment.
3. Make sure Python 3.4 or higher is installed:

    - If the command below prints `Python 2.x.x`, try next command. If it prints `Python 3.4.x` or higher move to Step 4 i.
        ```
        python --version
        ```
    - If the command below prints `Python 3.4.x` or higher move to Step 4 ii. If not install Python 3 and pip 3.
        ```
        python3 --version
        ```

4. Install virtualenv and activate virtual environment:

    1. If Python 3 is default python version:

        ```
        pip install --upgrade virtualenv
        virtualenv venv
        source venv/bin/activate
        ```
    2. If Python 2 is default version and Python 3 is available on `python3` command:
        ```
        pip install --upgrade virtualenv
        virtualenv -p python3 venv
        source venv/bin/activate
        ```

5. Install package requirements:
    ```
    pip install -r requirements.txt
    ```

6. Edit .env file and change configurations.
    - Generate and set SECRET_KEY. Application will not boot up without it.
    - Provide AUTHENTICATION_URL for application layer authentication.
    - Provide ELASTIC_SEARCH_HOSTS and ENVIRONMENT_CODE (pd,st,qa) if using elasticsearch
    - Provide Mongo DB configurations. Leave out MONGO_DB_USER and MONGO_DB_PASSWORD if unused.

7. Start an app:
    ```
    python manage.py startapp <app_name>
    ```

8. Configure `care/settings/commons.py`. Mention app name which was provided in last step, in INSTALLED_APPS list.

9. Edit `care/urls.py` and register your app urls.
    ```
    path('app/', include('app_name.urls'), namespace='app_name'),
    ```

10. Run server:
   ```
   python manage.py runserver
   ```

## App Development Instructions

- Raise http errors imported from `commons.utils.http_error` rather than using django's error responses.
- Use class based views (`from django.views import View`) to support automatic method not allowed errors.
- Do not import requests module, use `make_request` from `commons.utils.request_client`
- Import and use response classes from `commons.utils.response` to return standard http success responses. For response codes for which classes are not provided, use generic JSONResponse.
- While writing PyMODM models, use/extend default model manager provided in `commons.utils.default_model_manager` for easy serialization/de-serialization or mongo model/queryset objects.
- Use `app_logger` provided in `commons.loggers' for any custom up to INFO level logging.
- Use `ESQuery` available in `commons.utils.es_query` to access Elasticsearch.
