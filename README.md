1. Create MySQL db:

    ```
    sudo apt-get install mysql-server mysql-client python3-dev libmysqlclient-dev build-essential
    mysql -u root -p
    mysql> CREATE DATABASE `developx_test` DEFAULT CHARACTER SET `utf8` DEFAULT COLLATE `utf8_general_ci`;
    mysql> CREATE USER 'django'@'localhost' IDENTIFIED BY 'password';
    mysql> GRANT ALL PRIVILEGES ON `developx_test`.* TO `django`@`localhost`;
    mysql> FLUSH PRIVILEGES;
    ctrl+D
    ```


2. Install Redis:

    ```
    sudo apt-get install redis-server
    ```

3. Init virtual-environment:

    ```
    virtualenv venv
    ```

4. Install requirements:

    ```
    . venv/bin/activate && pip install -r requirements.txt
    ```

5. Apply db migrations:
    ```
    . venv/bin/activate && python manage.py migrate
    ```

6. Spawn celery worker

   ```
   . venv/bin/activate && celery -A developx_test worker -l info
   ```

7. Spawn celery beat

   ```
   . venv/bin/activate && celery -A developx_test beat -l info
   ```

8. Run Django:

   ```
   . venv/bin/activate && python manage.py runserver
   ```
