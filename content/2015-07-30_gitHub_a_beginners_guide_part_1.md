Title: GitHub: A beginner's guide, Part I
Date: 2015-07-30 11:57
Category: General
Author: Nitish Tiwari
Email: tiwari.nitish@gmail.com
Summary: !['GitHub office' by Dave Fayram](images/2015-07-30_gitHub_a_beginners_guide_part_1/github_office-dave_fayram.jpg "'GitHub office' by Dave Fayram") Today GitHub is world’s favorite place to host code - whether your software is open source or proprietary, you can host it on GitHub, choose who gets to see and contribute to your repository and be rest assured that you will have access to your software anytime anywhere. And why only code, you can even host and collaborate on other stuff like text files with GitHub. But, to the uninitiated, this looks like a huge maze with so many commands. There is also the obvious fear of doing something wrong and screwing everything up (more so because of there are others watching). In this two article series, lets take a close look at various GitHub features and when to use them in real world scenarios.


Today [GitHub](https://github.com/ "GitHub Home"){target="_blank"} is world’s favorite place to host code - whether your software is open source or proprietary, you can host it on GitHub, choose who gets to see and contribute to your repository and be rest assured that you will have access to your software anytime anywhere. And why only code, you can even host and collaborate on other stuff like text files with GitHub. But, to the uninitiated, this looks like a huge maze with so many commands. There is also the obvious fear of doing something wrong and screwing everything up (more so because of there are others watching). In this two article series, lets take a close look at various GitHub features and when to use them in real world scenarios.

!['GitHub office' by Dave Fayram](images/2015-07-30_gitHub_a_beginners_guide_part_1/github_office-dave_fayram.jpg "'GitHub office' by Dave Fayram")
<small>Photho by [Dave Fayram](https://www.flickr.com/photos/davefayram/ "Dave Fayram profile at Flickr"){target="_blank"} ([CC-BY 2.0](https://creativecommons.org/licenses/by/2.0/ "Creative Commons - Attribution 2.0 Generic (CC BY 2.0)"){target="_blank"})</small>

Before jumping to GitHub, I would like to introduce you to [Git](https://git-scm.com/ "Git Home Page"){target="_blank"} - the protocol GitHub runs on. Git was developed by [Linus Torvalds](https://en.wikipedia.org/wiki/Linus_Torvalds "Torvalds' bio"){target="_blank"} with contributions from several others. The initial release was on 7th April 2005. Git was designed for Linux kernel development and has since become on the most widely used version control system. GitHub or for that matter other sites such as [GitLab](https://about.gitlab.com/ "GitLab Home Page"){target="_blank"}, Gitorious (acquired by GitLab now), [Googs](http://gogs.io/ "Googs Home Page"){target="_blank"} are all based on Git. To understand GitHub features well, lets first understand basic Git commands. Don’t worry about the command format, you can learn them on the go with “git help”, after you [install Git on your system](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git "Getting Started - Installing Git"){target="_blank"}. Rather, more important is a clear idea of what the command does.

```git init```
:   Initializes a Git repository inside the folder you issue this command. For example, if you are in the folder ```~/My_Git_Project``` and issue the command ```git init```, a Git repository will be initialized in the folder and further git commands will be accepted. This is a one time step in the process of new project creation.

```git add```
:   This command lets you add a file to Git tracking. Once the file is added, you can track it via Git. Just type ```git add filename```.

```git status```
:   This command shows you which file are inside the repo and which of them still need to be committed. It also shows you the branch you are working on.

```git commit```
:   One of the key commands - as is obvious, this lets you commit your files to the repository. A commit is generally identified by a revision number. You can use it later to come back to this commit.

```git branch```
:   This lets you create a new branch or a clone of the master repository. The advantage is that you can make changes here safely without affecting the master repository.

```git merge```
:   Once you are done with the changes done in the branch, you can issue the git merge command to merge your branch with the master repository.

```git push```
:   Till now we were at our local machine enjoying solitary life, but as is the nature of software development, we need to collaborate with others. To do so, the changes should be pushed to the remote system (such as GitHub) for everyone to be able to use them - ```git push``` does that for you.

```git pull```
:   This is the exact opposite of git push. This command gets the latest version of the repository from the remote system on your desk.

Now that you have a clear idea of the most commonly used Git commands, we will see how they map with various GitHub features in the next part of this series.
