Title: 6 excellent continuous integration tools
Date: 2015-06-29 10:01
Modified: 2015-08-04 11:48
Category: General
Author: Nitish Tiwari
Email: tiwari.nitish@gmail.com
Summary: ![Noria by Siyan Ren]({filename}/images/2015-06-29_6_excellent_continuous_integration_tools/noria_by_siyan_ren.jpg "Noria by Siyan Ren") Continuous integration is an integral part of an agile setup. Sprint after sprint teams strive to “not break the build” while delivering incremental features. But, while developers focus completely on adding features, it happens sometimes that code errors creep in and render the software unusable. To stop such errors from being integrated to the SCM, a CI server is the gatekeeper that helps keep a tab on code quality. Even if the code is integrated to SCM, a CI server can very quickly tell you what went wrong.


Continuous integration is an integral part of an agile setup. Sprint after sprint teams strive to “not break the build” while delivering incremental features. But, while developers focus completely on adding features, it happens sometimes that code errors creep in and render the software unusable. To stop such errors from being integrated to the SCM, a CI server is the gatekeeper that helps keep a tab on code quality. Even if the code is integrated to SCM, a CI server can very quickly tell you what went wrong. In this post, lets look at 6 open source CI server tools, that you can use in your agile setup.

![Noria by Siyan Ren]({filename}/images/2015-06-29_6_excellent_continuous_integration_tools/noria_by_siyan_ren.jpg "Noria by Siyan Ren")
<small> Photo by [Siyan Ren](https://unsplash.com/ramblere "Siyan Ren's profile at Unspkash.com"){target="_blank"}</small>


### Jenkins

The best known among the CI servers, Jenkins branched from Hudson. It is developed in Java and can be easily installed using “java -jar jenkins.war”. You can also deploy it in servlet containers. Jenkins supports an array of SCM tools - Git, Mercurial, Subversion, Clearcase and many more. You can build Apache Ant, Apache Maven based projects and other shell scripts or windows batch files for pre/post build activities.

![JenkinsCI]({filename}/images/2015-06-29_6_excellent_continuous_integration_tools/jenkins_logo.jpg "JenkinsCI logo"){style="height: 84px; float:right;"}

Product page
:   [http://jenkins-ci.org/](http://jenkins-ci.org/ "See JenkinsCI web page"){target="_blank"}

License
:   [Creative commons attribution 4.0](https://creativecommons.org/licenses/by/4.0/ "Read Creative commons attribution 4.0"){target="_blank"}

Source code
:   [https://github.com/jenkinsci](https://github.com/jenkinsci "Go to jenkinsCI source code"){target="_blank"}


### Buildbot

Developed in Python, it is based on Twisted framework. It started as an alternative to the Tinderbox project, and is now used at projects like Mozilla, Webkit, Chromium etc. Buildbot installation has one or more masters and a collection of slaves. The masters monitor source-code repositories for changes, coordinate the activities of the slaves, and report results to users and developers. Slaves run on a variety of operating systems. You can configure Buildbot by providing a Python configuration script to the master. This script can be very simple, configuring built-in components, but full python power is available.

![Buildbot]({filename}/images/2015-06-29_6_excellent_continuous_integration_tools/buildbot_logo.png "Buildbot logo"){style="height: 84px; float:right;"}

Product page
:   [http://buildbot.net/](http://buildbot.net/ "See Buildbot web page"){target="_blank"}

License
:   [GNU GPL V2](https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html "Read GNU GPL V2"){target="_blank"}

Source code
:   [https://github.com/buildbot/buildbot](https://github.com/buildbot/buildbot "Go to Buildbot source code"){target="_blank"}

### Travis CI

Travis CI is probably one of the most easiest CI servers to get started with. Apart from being open source and free to host on
your own infrastructure, Travis CI offers a SaaS version that allows free testing for open source projects. Set up is as easy
as linking your GitHub account, giving the relevant permissions and updating the .travis.yaml file with your project specific
requirements. A new Travis CI build is triggered after a file is committed to GitHub. Read more
[here](http://docs.travis-ci.com/user/for-beginners "See Travis CI documentation"){target="_blank"}. 

*Fun fact: we at Taiga use Travis CI.

![Travis CI]({filename}/images/2015-06-29_6_excellent_continuous_integration_tools/travis_ci_logo.png "Travis CI logo"){style="height: 84px; float:right;"}

Product page
:   [https://travis-ci.org/](https://travis-ci.org/ "See Travis CI web page"){target="_blank"}

License
:   [MIT License](http://opensource.org/licenses/MIT "Read MIT License"){target="_blank"}

Source code
:   [https://github.com/travis-ci](https://github.com/travis-ci "Go to Travis CI source code"){target="_blank"}


### Strider-cd

Strider is written in Node.JS / JavaScript and uses MongoDB as a backing store. MongoDB and Node.js are prerequisites for installing Strider. Finally you can install it using “npm install”. Though, extremely customizable through plugins, Strider may need you to put your hands in code - not a bad thing to do, but if you would like a more quick setup without much programming effort, you should probably look at other options.

![Strider-cd]({filename}/images/2015-06-29_6_excellent_continuous_integration_tools/stridercd_logo.png "Strider-cd logo"){style="height: 84px; float:right;"}

Product page
:   [http://stridercd.com/](http://stridercd.com/ "See Strider-cd web page"){target="_blank"}

License
:   [BSD License](http://www.linfo.org/bsdlicense.html "Read the BSD License"){target="_blank"}

Source code
:   [https://github.com/Strider-CD/strider](https://github.com/Strider-CD/strider "Go to Strider-cd source code"){target="_blank"}


### GoCD

As with other advanced CI servers, GoCD lets you distribute your builds across different systems and monitor them at one place. Activities that you regularly perform can be added as pipelines in GoCD and then instances of these activities are called as jobs. GoCD comes with an easy to use GUI and a detailed [documentation](http://www.go.cd/documentation/user/current/index.html "See GoCD documentation"){target="_blank"}. GoCD was created and then open sourced by ThoughtWorks.

![GoCD]({filename}/images/2015-06-29_6_excellent_continuous_integration_tools/go_logo.png "GoCD logo"){style="height: 84px; float:right;"}

Product page
:   [http://www.go.cd/](http://www.go.cd/ "See GoCD web page"){target="_blank"}

License
:   [Apache license V2](http://www.apache.org/licenses/LICENSE-2.0 "Read Apache license V2"){target="_blank"}

Source code
:   [https://github.com/gocd/gocd/](https://github.com/gocd/gocd/ "Go to GoCD source code"){target="_blank"}


### Integrity

Built on Ruby, integrity is available under MIT license. Preconditions to install Integrity are Ruby (>= 1.8.7), RubyGems (>= 1.3.5) and git (>= 1.6). Once you install Integrity, you need to configure it using “init.rb” file. A sample for this file is available in the Integrity product page. Note that Integrity currently works with git only.

Product page
:   [http://integrity.github.io/](http://integrity.github.io/ "See Integrity web page"){target="_blank"}

License
:   [MIT License](http://opensource.org/licenses/MIT "Read MIT License"){target="_blank"} (From [Wikipedia](http://www.wikiwand.com/en/Comparison_of_continuous_integration_software "See wikipedia article 'Comparison of continuous integration software'"){target="_blank"})

Source code
:   [https://github.com/integrity/integrity](https://github.com/integrity/integrity "Go to Integrity source code"){target="_blank"}
