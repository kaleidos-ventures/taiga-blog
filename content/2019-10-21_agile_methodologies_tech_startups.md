Title: The best methodology for a tech startup in 2020
Date: 2019-10-21 09:00
Category: Announcements
Author: Taiga Team
Email: support@taiga.io
Summary: ![Hacktoberfest]({filename}/images/2019-10-21_agile_methodologies_tech_startup/userstories_taiga_kaleidos.jpg) Which methodology is best for a tech startup? We discuss different implementations of the agile methodology (scrum or kanban?), how and when to implement them and which are some of the most common misconceptions.

Which methodology is best for a tech startup? The best methodology is any that prioritizes efficiency and at the same time is agile and adaptable whenever required. Methodologies which quickly detect mistakes, allow to learn from them and apply corrective measures. Even the most focused startups can end up in a roller coaster, partly because most of the time the founding team pivots after re-evaluating their ideas. Any methodology that penalizes change (whether directly or by burying it under processes, bureaucracy or documentation) will not do it.

Currently, only agile methodologies fit these needs. All of them have in common the Agile Manifesto:

* Individuals and Interactions over processes and tools
* Working Software over comprehensive documentation
* Customer Collaboration over contract negotiation
* Responding to Change over following a plan

![Kaleidos's Team]({filename}/images/2019-10-21_agile_methodologies_tech_startup/userstories_taiga_kaleidos.jpg)

##Scrum or Kanban?

Scrum and Kanban are two popular implementations of the Agile Manifesto. But for us, the manifesto has always priority over specific methodologies. We don’t think of them as recipes to follow strictly. It’s principles what matter. An example: if we apply Scrum but only techs really use it, we are at least invalidating the first principle: individuals over processes. This is a very common mistake among startups: developers use agile methodologies but the rest of the people use other formulas. This will cause frustration and misunderstandings midterm. 

Scrum works best for teams who can commit to deliverables every few weeks (sprints) and when the amount of external interference is limited. This is usually the case before the first public release. Our sprints normally last 2 to 3 weeks, leaning towards 2 for earlier self-evaluation. While Scrum aims for a predictable speed per sprint, Kanban aims for a predictable speed per life cycle of a task. Kanban has no time-slots where tasks fit, but instead it takes tasks and moves them around several states (New, In Progress, Testing, ...) until their conclusion. It looks easier, but it’s harder to master and requires much more mature teams. It goes in hand with the idea of Work In Progress Limit, which sets a limit in the number of tasks that can exist in any given state. Kanban is the default when external factors interfere significantly, which typically happens after a product has been released and there is already a community of users.


![Kanban board using Taiga]({filename}/images/2019-10-21_agile_methodologies_tech_startup/kanban_taiga.jpg)

##Good Practices

Our list of good practices is:

* Scrum for pre-release, Kanban for post-release (exception: if there are too many stakeholders, we always use Kanban).

* Every team profile, tech & non-tech, must get involved in the methodology. Everyone should be at the standup dailies, demos, retros… Including the external client, if any. Transparency is key.

* If using Scrum: we do a design sprint that takes user stories from the high-priority backlog and starts processing them so they are ready for the more organic sprints that will complete them in a demo.

* One person each time takes the role of “Dread Pirate Roberts", who does QA and normally takes the demo each sprint. It often makes unnecessary the figure of Scrum Master.

* We give visibility when a person takes responsibility for a user story outside of their comfort zone. We call that taking a dose of iocane (fictional poison) knowing that in small doses and over time that person will become immune to a large lethal dose.

* When using Kanban we simulate the sprint concept and plan a demo & retro every 2 weeks or so.


![Example of retro at Kaleidos]({filename}/images/2019-10-21_agile_methodologies_tech_startup/retro_kaleidos_taiga.jpg)

##When to start applying a methodology


How about just start fully with one methodology any single day? Nope. You need to learn to walk before you run. We take two steps before starting any actual development.

* Analysis and Definition Step: first we discuss the idea of a product in 2-4 weeks, with 4-6 sessions on specifics of the project. The result is a shared vision and a plan.
* Cylon Step: the same team thinks about what is the best technology, methodology and most appropriate team for the project.

After these steps, the project itself starts, with the building of the product as a demo. Several iterations later, we may consider changes in the methodology, such as switching to Kanban for example.


##Common Misconceptions

There is a widespread myth, believed even by some agile gurus, where making estimations of tasks is a taboo and it is impossible to predict what will be delivered when. This is only a half-truth. To estimate the work of a user story, regardless of the metric, is not an anti-agilist practice. Plus, it helps clarify the task itself and relate its value to the time it will take.

When we estimate each user story, two things will happen, though:
* User stories can mutate or be relegated quickly, making the effort put into the estimations a partial waste, something that agile methodologies frown upon.
* What will be in production 10 sprints in the future is impossible to predict because the methodology and principles enable us to pivot every few weeks. 

This second point is what is used to argue not estimating in Agile, but that’s a fallacy. Agile generally guarantees that at any given date a product will be developed with the most value and less waste. It doesn’t say what it will contain, but it does say its nature and its order of magnitude. That’s no good reason not to estimate.

Do we make estimations in Kaleidos? Sometimes we do, sometimes we don’t. It depends on the project and the team. In general, we tend to estimate only top priority items which will likely be part of the work for the next few weeks. Also, previous UX & UI work greatly helps this estimation, which gains in quality and accuracy.

![Kaleidos Team]({filename}/images/2019-10-21_agile_methodologies_tech_startup/kaleidos_team.jpg)


##Final Considerations

Very often, the main value of a product is how things are made. A sustained rhythm, adaptability and continuous self-evaluation. It is key that everyone is involved, especially the client.

A very important part is the transparency of the process. We are talking about the business core of a new company and half-measures are not valid, which fits perfectly the third principle of the Agile Manifesto: *Customer Collaboration over contract negotiation*. Makes sense: technological products are not made by contracts.
