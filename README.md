# Taiga blog

Taiga blog (https://blog.taiga.io/) made with Pelican (https://github.com/getpelican/pelican).

#### For developers:

- Install python dependencies:
  ```
  mkvirtualenv -p /usr/bin/python3 taiga-blog
  workon taiga-blog
  pip install -r requirements.txt
  ```

- Install SASS:
  ```
  gem install sass scss-lint
  export PATH="/usr/bin/core_perl:$(ruby -e "print Gem.user_dir")/bin:$PATH"
  ```
