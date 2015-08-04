Title: User stories demystified
Date: 2015-04-23 12:18
Category: General
Author: Nitish Tiwari
Email: tiwari.nitish@gmail.com
Summary: ![User stories, user stories everywhere!!]({filename}/images/2015-04-23_user_stories_demystified/userstories.png) In one of our [previous blog posts](/agile_as_management_tool_for_non_IT.html "See the post 'Agile as a management tool for non-IT industry: an insight'"), we took a close look at how Agile is widely used across industries, contrary to the popular belief that agile is only for software related activities. In that study we also found some pain points- one of them was difficulty to get started. Lets face it, Agile methodology is great at helping you churn out products at faster rate, but it comes with its own set of jargon which sometimes proves very difficult for newcomers to handle. In this post today we will focus on few such terms, specifically- user story and the user story points. We will see how can these be used to simplify projects, and of course how to set them up in [Taiga](http://taiga.io "Go to Taiga.io"){:target="_blank"}.


![User stories, user stories everywhere!!]({filename}/images/2015-04-23_user_stories_demystified/userstories.png)

In one of our [previous blog posts](/agile_as_management_tool_for_non_IT.html "See the post 'Agile as a management tool for non-IT industry: an insight'"), we took a close look at how Agile is widely used across industries, contrary to the popular belief that agile is only for software related activities. In that study we also found some pain points- one of them was difficulty to get started. Lets face it, Agile methodology is great at helping you churn out products at faster rate, but it comes with its own set of jargon which sometimes proves very difficult for newcomers to handle. In this post today we will focus on few such terms, specifically- user story and the user story points. We will see how can these be used to simplify projects, and of course how to set them up in [Taiga](http://taiga.io "Go to Taiga.io"){:target="_blank"}.


## User story

A user story- simply put, is a way to define a software feature from an end-user perspective, note the emphasis. For example, a user story may look like "As a user, I want to be able to update my profile with age, present occupation and social interests, so that people visiting my profile page get an idea of my interests". Generally, it is good to follow this template:

> As a `<end-user-type>`, I want to be able to `<user-requirement>` so that `<reason>`.

This will give the developers a clear idea of what they need to develop and why.

Sometimes this approach has problems, people tend to club too much or too less of information in one user story- but this will get sorted automatically once the team is one or two sprints old. Another issue is of dependency, user stories are supposed to be independent of each other, so that you can implement them in any order and still be able to have the feature working. But in real world scenarios, things depend on each other and so comes the concept of Epic stories. Epic stories can be thought of as a collection of related user stories. We have a very detailed [blog post on Epic stories here](/epic-stories.html "See post 'Epic stories'").


## User story points

Another aspect related to user stories are the user story points. These points are a way to estimate the task size. So, tougher/bigger the tasks (user stories), higher the points. Once you are 2-3 sprints old, these points play a critical role in estimating the efforts for user story implementation. Lets see how-

Consider this scenario:

> Team delivered:
>
> - 3 user stories in sprint 1 (total user story points 40)
> - 4 user stories in sprint 2 (total user story points 45)
> - 3 user stories in sprint 3 (total user story points 32)

Now, lets do simple math- calculate the average of user story points finished in the 3 sprints. Average is 39. Now, lets assume the 4th sprint has 4 user stories worth 50 points. Is it possible to complete it? Well, at least the team’s history says No. Team probably needs another sprint!

Also, note that the average story points, we calculated above is also called the team velocity.


## User story points vs man hours

There has been lot of speculation over what is a better way to estimate tasks- user story points or man hours. Historically, man hours has been the tool of choice by the project managers to estimate the efforts- it is simple, total time you think it will take to finish the task. But there is a problem, we humans are very bad at estimating time. Leave project aside for a moment, and think about the last time you were visiting your friends. When they called you, to check when will you reach- were you able to tell exactly how much time you will take or your answer was the customary "5 minutes". You may think, I guessed the time right, but got stuck in traffic- that is out of my hand, how would I know if there is traffic ahead.

Exactly the same thing may happen with your estimates to finish your project task- the nature of development (especially software) is that you develop 90% of the code in half of the estimated time and still overshoot the estimation because of debugging an issue. User story points give another dimension to the task estimates. You just need to estimate the complexity of the task at hand with the user story points- not the effort. The effort automatically gets calculated based on the team velocity!


## Taiga usage

I hope you got a pretty good idea of user stories and user story points. Lets now see how to put these in action, using your Taiga account.

#### User stories:

To add a user story, you need to first create a project with *Scrum* template. You can then go to the *Backlog* page and click on the *+ Add a new user story* button, new form appears, fill up the details and stories are added. All the users stories can be seen listed in the *User story* section. Next step is to add a user story to a sprint. To do so, select a user story by clicking on the small checkbox in its front. This will reveal a new button above- *Move to current sprint*. Click on this button to add the user story to the current sprint. Want to see this in action? Here is the video explaining the steps in detail:

<iframe width="640" height="480" src="https://www.youtube.com/embed/bYFFnnZRrNM" frameborder="0" allowfullscreen></iframe>


#### User story points

While adding the user story, you must have noticed the form. Just below the subject line in the form, there is the section to add the user story points. Here you have different modules- design, front and back. Just add the estimated story points for different modules and you are good to go.

The graph on the top of backlog page shows the burndown rate of the user story points- you can easily keep track of the optimal points per sprint and the real points per sprint. Note that the graph takes 100 project points as the reference, you can change it in the *Admin* >> *Project* >> *Project Details* >> *Number of US points*. You can also add new user story points in *Admin* >> *Attributes* >> *Points* >> *Add New Point*. Take a look at user story points in action here:

<iframe width="640" height="480" src="https://www.youtube.com/embed/kstSgsG3wKw" frameborder="0" allowfullscreen></iframe>

Have something to add to this story? Let us know in the comments below. We love to hear from you!
