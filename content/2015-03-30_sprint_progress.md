Title: Q: "I'd like to measure the sprint progress through closed tasks"
Date: 2015-03-30 07:18
Modified: 2015-08-04 11:48
Category: General
Author: Antonio de la Torre
Email: antonio.delatorre@kaleidos.net
Summary: ![Sprint progress graph]({filename}/images/2015-03-30_sprint_progress_question/sprint_progress_graph.png) Taiga users are using the [support forums](https://groups.google.com/forum/#!forum/taigaio "Go to Taiga mailing list"){:target="_blank"} to raise interesting questions and debate about the use of the tool and whether their philosophy and the objectives of the tool coincide. Here’s an example about sprint progress:


Taiga users are using the [support forums](https://groups.google.com/forum/#!forum/taigaio "Go to Taiga mailing list"){:target="_blank"} to raise interesting questions and debate about the use of the tool and whether their philosophy and the objectives of the tool coincide.

Here’s an example about sprint progress:

![Sprint progress graph]({filename}/images/2015-03-30_sprint_progress_question/sprint_progress_graph.png)

> “The current graphic (Taiga’s Sprint Burndown Chart) is not valid for us because “burnt” points appear only when all the tasks in a given user story are closed, which means that during the first week of a sprint we get the impression that we haven’t advanced even though we are closing tasks inside various user stories.
>
> The requirements we have from our Scrum Master is to work with the philosophy of tasks as a measure of what the team is doing and the real progress (they even account for hours)”

The Scrum Master they refer to follows the book. The official scrum guide in its section dealing with sprint backlogs says:

> ***Monitoring Sprint Progress***
>
> At any point in time in a Sprint, the total work remaining in the Sprint Backlog can be summed. The Development Team tracks this total work remaining at least for every Daily Scrum to project the likelihood of achieving the Sprint Goal. ***By tracking the remaining work throughout the Sprint, the Development Team can manage its progress.***

A well known, and more in-depth development as narrated by _Henrik Kniberg_ in his book _["Scrum and XP from the trenches"](http://www.infoq.com/minibooks/scrum-xp-from-the-trenches "See book webpage"){:target="_blank"}_ also speaks of accounting for the pending work in a sprint.

In both cases they talk about **asking the team how much work they think it is still needed for every user story, be it in points or hours, then add them all and find how much it is still left for the sprint**.

Implementation-wise, what this team is doing is accounting for the hours worked on completed tasks.

The progress of tasks in a user story does not give you actual information on the progress of the sprint, because if we are faithful to Scrum, during the demo we can show only finished stories, not 'almost' finished stories.

A graph of pending tasks in the sprint showing that 90% of the sprint is finished sprint, while really only 2 of the 8 stories are complete (25%), may lead to a false sense of comfort, and avoids something very important, which is to focus on finishing stories.

Besides this, by keeping track of tasks, and doing so in hours, makes it necessary that they be estimated at the start of the sprint with the effort that entails.

When back in 2010 we tried to do a faithful approximation counting the hours remaining in the sprint, we soon realized that there was a micromanagement that didn't really add much to what the panel told us. The blockages that may have been present in a story can be detected just as easily during the daily: "You've had three days with this 2 point story. Is there a problem? " Is much more effective.

In my opinion, if you want to have a **"Sprint Burndown" graph** with more detail than is currently present in [Taiga](https://tree.taiga.io "Go to Taiga PM tool"), I would recommend, as the literature does, that the team be asked during the daily: *"How many hours do you figure you have left in your story?"* It is much more realistic and independent of completed tasks. And with that information you could make a chart to hang on the board or on a shared doc.

If you want to automate the process, in this [past week’s release of Taiga](/taiga-abies-bifolia-release-160.html "See post about past release"), you can create a custom field and start inputting the remaining number of hours, and use that field to easily draw a graph.

Very interesting topic, no doubt. Next time we’ll talk about detailed control of time, which we internally call _"The Time-Tracking dilemma”_.

