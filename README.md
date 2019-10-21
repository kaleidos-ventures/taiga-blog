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
  
- Run in devel mode
  ```
  make compile_styles
  make devserver
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
