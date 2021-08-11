# Taiga blog

Taiga blog (https://blog.taiga.io/) made with Pelican (https://github.com/getpelican/pelican).

### For developers:

#### Setup

- Create virtualenv:

    ```bash
    python3 -m venv .env
    source .env/bin/activate
    ```

- Install python dependencies:

  ```bash
  pip install -r requirements.txt
  ```

- Install SASS (only if you want to modify style):

You need to install ruby package first

  ```bash
  gem install sass scss-lint
  export PATH="/usr/bin/core_perl:$(ruby -e "print Gem.user_dir")/bin:$PATH"
  ```

#### Run/Stop

- Enable the enviroment

    ```bash
    source .env/bin/activate
    ```

- Run dev server

  ```bash
  pelican -r
  ```

On another terminal run

  ```bash
  cd output && python -m http.server 8080
  ```
  
- Stop dev server

  CTRL+C pelican -r terminal


- Deactivate the enviroment
  ```bash
  deactivate
  ```

#### Recompile styles

You need `sass` and `scss-lint` installed

```bash
make compile_styles
```

### HOWTOs

#### Use a custom `og:image` in a blog post

Use the meta `og_image`. For example:

```
Title: Join #Hacktoberfest with Taiga!
Date: 2019-10-11 09:00
Category: Announcements
Author: Taiga Team
og_image: {filename}/images/2019-09-11_taiga_hackoctoberfest/hackoctoberfest.jpg
...
```
