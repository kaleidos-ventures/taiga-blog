Title: Why is KANBAN not working for me?
Date: 2020-08-18
Category: Agile
Author: Pablo Ruiz-Múzquiz
Email: support@taiga.io
Summary:  ![Screenshot of Taiga showing the kanban mode]({filename}/images/2020-08-18_why_is_kanban_not_working_for_me/taiga_kanban_move.gif)When teams all over the world try to adopt agile methodologies, sooner or later they will be faced with a key question - Is KANBAN the right technique for us? Sometimes, they have known and experienced other agile techniques like SCRUM but most often they are new to agile to begin with. In this article I will try to explain what are some of the pros and cons of KANBAN and what common mistakes are unknowingly made so you can self-diagnose your particular use case, whether you're new to KANBAN or new to agile altogether.


When teams all over the world try to adopt agile methodologies, sooner or later they will be faced with a key question; Is KANBAN the right technique for us?
Sometimes, they have known and experienced other agile techniques like SCRUM but most often they are new to agile to begin with. In this article I will try to explain what are some of the pros and cons of KANBAN and what common mistakes are unknowingly made so you can self-diagnose your particular use case, whether you're new to KANBAN or new to agile altogether.

Personally, I love KANBAN for two reasons related to *the results it delivers*.

* KANBAN is designed to adapt your workflow to changing priorities and interruptions. It makes bad news to be engulfed by the process. That's amazing. Instead of embarking yourself on "change management", you embrace it as a natural activity.
* Since KANBAN can tell you the average time a task takes to be completed, you can  more or less predict when any random task will be finished. Averages aren't robust statistics but over time they can give superuseful time ranges.

##KANBAN Pros

Within the agile principles and frameworks KANBAN shines as one of the two most widely known techniques, together with Scrum. It is probably overused and overstretched but this is due to its obvious merits. What are those merits in the context of a team and a project?

###Simple, everyone can understand it

KANBAN portrays itself as a board with as many states or *columns* are needed for an organic flow of tasks or *cards*. Your objective is to move those *cards* from the leftmost *column* to the rightmost *column* and crossing it off the list.
It brings certain order and spatial awareness to the classical TODO list.
You can't deny its simplicity and almost every cultural context provides the *user* with the tools to understand that this is a simple way to organize pending work.

![Screenshot of Taiga showing the kanban mode with several columns (upcoming, ready, in progress) with items with pictures from the Princess Bride. Gif shows how an item is moved from a column to another one.]({filename}/images/2020-08-18_why_is_kanban_not_working_for_me/taiga_kanban_move.gif)
<small>KANBAN reflects progress in part by moving cards from left to right in a step by step transition to the piece of work.</small>


###Shared view

A team is more than just a collection of individualities, there has to be a mutual purpose, a common vocabulary and a agreed upon priority. KANBAN is a nice shortcut to all that. The KANBAN status can be equated to the TEAM status or the PROJECT status. It's a nice example of visual management or an information *radiator* because everyone in the team is equally exposed to the same information.

###Identify bottlenecks

Any organic flow is highly adaptative, true, but only if we are quick to remove any sudden bottlenecks. There is no use in a KANBAN board that lets certain *cards* die when they reach a particular *column*. You can picture those bottlenecks as death traps for tasks. You want to keep an eye and remove them as they appear. KANBAN is amazing as a heat map for bottlenecks, it even allows you to specify how many *cards* trigger the idea of a bottleneck per column.

![Screenshot of Taiga showing the kanban mode with a zoom out view.There are lots of columns and rows.]({filename}/images/2020-08-18_why_is_kanban_not_working_for_me/taiga_seequestor_kanban.jpg)
<small>This great KANBAN zoom out view allows you to see not only WIP LIMIT-breaching columns (see red lines) but also a general sense of potential bottlenecks.</small>


##KANBAN Cons

There are some weaknesses inherent to the way people use KANBAN. I wouldn't go as far as to say they are KANBAN flaws, but rather common misuses that many teams eventually develop as they are *enjoying the ride*.

###Everything has to go to the KANBAN

You know the saying about someone having a hammer and seeing everything as a nail, right? Any KANBAN board needs to remain significant for a team and a project, otherwise its apparent simplicity will suddenly make it look as a untidy room and trigger avoidance behaviours. This can happen if we force everything related to a project or a team to go to the KANBAN. Some information might be better handled through other means.

![Screenshot of Taiga showing to the left a colum with filter options and to the right issues related to the princess bride classified by type, severity, priority and votes. There is also a columns associated to the status, last modified and assigned user.]({filename}/images/2020-08-18_why_is_kanban_not_working_for_me/taiga_issues_theprincessbride.jpg)
<small>Sometimes Taiga Issue’s module can be of much help to lower the burden on the KANBAN</small>

###Too many workflow states

Overclassification can be tempting for teams that want to have powerful metrics and detailed accountability but there is a point when too much classification might impose cognitive and operational overhead. We are aware that NEW, IN PROGRESS and DONE columns might not work for every project on earth, but CRAZY IDEAS, REVIEWED IDEAS, DEFINED IDEAS, READY, DESIGN, TO BE DEVELOPED, DEVELOPED, TO BE TESTED, TESTED, TO BE DEPLOYED, DEPLOYED, DONE, ARCHIVED, REJECTED and POSTPONED could be a bit too much for many others.
This typically happens when a team wished a tool could replace normal peer-to-peer communication.


###Dubious quality of the initial column

Draft stages of a task or *card* should be carefully considered before entering the KANBAN. The initial column normally tracks recently added tasks. We use column names such as NEW, IDEAS, CRAZY STUFF, TO BE DISCUSSED and so on and so forth. That's great as long as it doesn't become a tasks graveyard. You can't afford to have one of those bottlenecks or death traps *right at the beginning of the flow*. If you start using that initial KANBAN column as your brain dump after every meeting, you are doing a disservice to one of the advantages we highlighted above.


![Screenshot of Taiga showing the kanban mode with a zoom out view.There are lots of columns and rows. The first column, "ideas", is specially long]({filename}/images/2020-08-18_why_is_kanban_not_working_for_me/taiga_kanbanzoomout.jpg)
<small>Taiga’s zoom out view of a KANBAN card is showing here a problematic initial column. Watch out for long scrolls in early stage KANBAN columns.</small>

###People saying "What should I do next?" too often

Whether you have daily stand-ups borrowed from Scrum or regular checkpoints for sharing impediments or progress, one question you don't want to hear *very* often is "What should I do next?". Sometimes, it's the most appropriate question to ask, because there's a need for an arbiter to prioritise between seemingly important tasks. But if you keep hearing that question it might mean the KANBAN is not self-explanatory. To ask is to talk, and a team that has members talking to each other is great, don't get me wrong, but it's always better to have quality conversations where everyone is exercising their most proactive and responsible role. Ideally, if you use KANBAN, you generally know what to do next among the options in front of you.


##Am I doing KANBAN wrong?

You are entitled to question your KANBAN approach but you have to be aware of some unnecessary constraints you might have self-imposed. Let's give some examples borrowed from experience where we take the first Agile Manifesto point "Individuals & Interactions *over* Processes and Tools" as our razor tool.

###Who's assigned to what?

For a streamlined KANBAN process where you are counting on the "flow" to work like a charm, everyone in the team needs to know what they are responsible for. Multiple assignment is a dangerous practice as you risk diluting accountability but there can be a person assigned to a card that hold subtasks assigned to different people.

Also, anyone in the team should be able to know whether they should self-assign a card without asking too many questions.

To help with this, some platforms have the concept of roles or subteams and it might perfectly work to have a role assigned to the card as a first soft assignment and then allow anyone belonging to that role or subteam to take it for themselves alone.

![A gif sgowing first an issue "performing a miracle" with a picture from the princess bride and then a screen where you can select the user you assign it to.]({filename}/images/2020-08-18_why_is_kanban_not_working_for_me/taiga_select_assigned_user.gif)
<small>KANBAN cards in Taiga have built-in role assignment so you can shortcut your assignment process. Just make sure there is a clear policy on what to do with multiple assignees.</small>

If a card is in the middle of the KANBAN board but no one is working on it anymore, the kanban is not reflecting the state of the project, don't hesitate to remove the assignment and move it back to a suitable initial KANBAN state.

![Screenshot showing to the left a filter column with several options (status, tags, assigned users) and to the right showning the kanban board with cards assigned to Princess Brides characters]({filename}/images/2020-08-18_why_is_kanban_not_working_for_me/taiga_filters_kanban.jpg)
<small>Taiga’s KANBAN board has custom filters. Here we decided to show only KANBAN cards that were assigned to either Buttercup, Princess of Florin or Count Tyrone Rugen.</small>


###Are team members created equal?

KANBAN provides a shared vision but, unfortunately, that doesn't always equate to a shared empowerment. Very often, there are *classes*, where some people enjoy a certain status quo represented by a preference of vocabulary or a preference of workflow.

If KANBAN is your primary visual management technique and you feel somewhat alienated, then it's other people's KANBAN and you're just a visitor. That doesn't work as it undermines a lean approach where everyone enjoys a virtuous circle around accountability and autonomy.

Be aware of people not feeling comfortable with the KANBAN design and its contents. Very often, the developers will impose a particular workflow or card vocabulary because they are more used to states and workflows. It might be a great start but if the KANBAN board is going to reflect the whole process, it has to appeal to the whole team.

###Is there a clear workflow?

On a small team and a small project, you need not to worry, personal interactions sort out 95% of impediments and decisions. For bigger teams (beyond 7-8 people) and bigger projects (beyond 3-4 months), how you treat *demand management* can be of enormous value.

First, should a small issue (like a bug in software development) enter the KANBAN alongside more fleshed-out tasks or not? Some teams try to make sure *everything* goes into the KANBAN. After all, isn't it a shared view? Yes. But a good shared view needs consistency. If cards that are very different in nature compete with each other, it's likely you are going to end up in a big mess. Consider having a separate view for a specific type of task. It could be a second KANBAN with a different workflow or perhaps a more simple TODO list.

![Gif showing first a screenshot of taiga with an issue titled "not a lot of money in revenge" with a pic from Princess Bride and then a screen where you can select the user you assign it to]({filename}/images/2020-08-18_why_is_kanban_not_working_for_me/taiga_issue_user_story.gif)
<small>Taiga allows issues to be promoted to KANBAN cards (or user stories) when you need additional filters in your demand management workflow.</small>

Make sure the main KANBAN board represents the project's state quite faithfully and be open to add secondary boards or TODO lists for that remaining 10% of the project that doesn't fit into the main view.

###Do you have a top level view?

The organic flow of a KANBAN board is much about the *current state*. It's an optimisation technique that leads to less waste and more predictability but what about the big picture?

When there are strategic objectives, it's easy to get lost in the *now* and forget about them. The KANBAN itself behaves a bit like a heat map. Work In Progress limit per column plus a bird's eye view of the whole KANBAN board might provide you with a qualitative assessment of the overall performance. It is sometimes very useful to have the ability to zoom out and get a sense of the general distribution of cards across all states.

Moreover, you might need a separate view where you keep track of your top level objectives. You can call them Epics, you can call them Objectives, Targets, Subprojects, it doesn't matter. What matters is that you can enjoy the progress of these big milestones or containers separately and quickly jump from Epic to Epic and view what KANBAN cards relate to them.

![Screen titled "Epics: the princess bride" and then a list with several columns: votes, name, project, sprint, assined, status and progress. Below there are listed several items with different levels of progress shown by a progress bar in green]({filename}/images/2020-08-18_why_is_kanban_not_working_for_me/taiga_epics_theprincessbride.jpg)
<small>Taiga has an Epics module, where you can create bigger or more strategic goals that contain KANBAN cards so you can keep track of overall progress.</small>


##Key insights to take away

KANBAN is a deceptively simple agile technique. It requires relatively mature teams able to adapt to an organic flow of tasks. This is the quintessence of tuned teams so expect some bumps along the way.

It is vital that you see the KANBAN board and all its bells and whistles as a physical (or rather, digital) manifestation of a process, not a recipe to follow. And to do that, it is important to understand the value of KANBAN as well as some of the most common pitfalls. Without this, frustration will govern every team interaction and work and a sense of disorientation will permeate through all layers, from operation to strategy.

Is KANBAN suitable for everyone? Certainly not, but before questioning KANBAN itself, start analysing your specific KANBAN approach. After all, continuous improvement is part of the deal, right?

![Screenshot of Taiga showing the kanban mode with several columns (upcoming, ready, in progress, ready to test, done, archived) with cards for each item with pictures from the Princess Bride.]({filename}/images/2020-08-18_why_is_kanban_not_working_for_me/taiga_Kanban-The-Princess-Bride.jpg)
<small>Taiga’s KANBAN module is flexible and simple, like it should be.</small>
