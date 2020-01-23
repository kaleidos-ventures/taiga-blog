Title: Four Agile Antipatterns and a Big Fat Lie
Date: 2019-12-10 09:00
Category: Agile
Author: Pablo Ruiz-Múzquiz
Email: support@taiga.io
Summary: ![Taiga's Team]({filename}/images/2019-12-10_agile_antipatterns/kanbanzoomout.jpg)In any transition to agile methodologies there is a risk of maintaining old practices that survive in disguise as “agile adaptations”. In the medium term they become structural blocks, agile antipatterns that gradually reinforce this involution. I summarize four of these identified thanks to the involuntary help of Taiga users.

##Taiga, Symptom Detector

Five years ago Taiga was released. Now it is used by thousands of teams and organizations worldwide, with more than one million estimated users. From this privileged observatory we have access to a lot of information that helps us to detect the symptoms that lead to agile antipatterns. Most of them come from requests for new features: that "only missing functionality" that will make Taiga "the perfect platform." The vast majority of these requests are the tip of the iceberg of an antipattern.


![Taiga translated into farsi, screenshot]({filename}/images/2019-12-10_agile_antipatterns/taiga_farsi.jpg)
<small>Screenshot of Taiga in Farsi, one of the 20 languages ​​it has been translated into, with RTL support</small>

##Agile Antipattern 1: Workflows and ISO-Compliant Permissions

"In this organization it is important to follow a specific process of approvals and revisions to comply with ISO standards and that implies workflows with very specific permissions so that nobody can make mistakes."
There’s a fallacy and a problem here. The fallacy is that if ISO standards survive so well over the years, it is precisely because they make sure not to mix processes with specific implementations, it is not true that ISO forces a hyper-fiscalization of certain workflows. And the problem is that it would favor a minimal delegation, in contrast to Agile’s maximum delegation. The objective in Agile is to give actors of an organization the maximum responsibility, favoring the autonomy of the teams. ISO has nothing to say in this regard, no matter how much some consultants insist on it.
If with the excuse of ISO regulations we allow people to become passive participants at a model that actually requires them to be protagonists and take risks, it is impossible that the pre-conditions for Agile's promises are met.

##Agile Antipattern 2: Team Commitment Is Not Respected

“In this organization we want to be able to intervene halfway through the sprint. If the team is moving faster than expected, we want to be able to add more tasks. If new priorities have emerged in the backlog, we want to be able to make an urgent interruption.”

Actually, it is the reverse request that usually comes to Taiga: “We are tired of getting things added in the middle of a sprint. We need Taiga to prevent certain users from doing this to us.” Scrum as an agile methodology needs teams to make commitments with a delivery at the end of the sprint. This key commitment is dynamited when a stakeholder modifies an ongoing sprint, generating a lot of frustration.

This antipattern is usually accompanied by a rush forward; move from Scrum to Kanban, since the latter is a more organic model where sprints do not exist. Unfortunately, then the Kanban board will reflect the same underlying problem in the form of traffic jams: interruption and constant priority changes.

![A kanban at the minimum zoom level helps detect bottlenecks]({filename}/images/2019-12-10_agile_antipatterns/kanbanzoomout.jpg)
<small>A kanban at the minimum zoom level helps detect bottlenecks</small>


##Agile Antipattern 3: All for Sprint’s Speed

“In Scrum, only user stories completed in a sprint can add their story points; that causes partial jobs not to count for sprint speed and give a bad image.” It is one of my favorite antipatterns and one of the most controversial with eternal threads of discussion.

A good burndown chart is almost the holy grail of Scrum. It represents a good pace of closing user stories. The problem arises when we fail to close user stories and still pretend to count a significant percentage of the points associated with those stories. The origin of these disastrous sprints is multiple, but some of the most common causes are a bad estimate (easy to justify at the beginning of a project but more difficult after some months), a tendency to start all user stories on the first day of the sprint and try to close them all at once just before the demo, or the very last antipattern we just explained, among others.


![A wonderful burndown chart, “burning” functionality at a good pace, but is it really the case?]({filename}/images/2019-12-10_agile_antipatterns/burndown.jpg)
<small>A wonderful burndown chart, “burning” functionality at a good pace, but is it really the case?</small>


##Agile Antipattern 4: Planning in Advance


“In this organization we have implemented Agile with Scrum; we created a backlog, prioritized, estimated and then created all the filled in sprints to know when we will have all the functionalities finished.”

Scrum, Kanban and Lean models manage advance planning very poorly when the quality of the information is low, which is usual. Therefore, to estimate, evaluate, prioritize and develop it is recommended to wait for the optimal moment. There are people who cannot assimilate this vision and use the agile vocabulary but the waterfall modes: they create n sprints with the user stories already programmed in each cycle.

This is not just nonsense but it will result in chaos in every small replanning. Agile's promise is that for any given future date, the product of greater value and less waste will be produced, but says nothing about what that product will be in particular. Waterfall in return follows the reverse path, guarantees what will a product contain for a given date but does not worry about the value delivered or how much waste is generated.


![An example of a small Taiga project using Scrum: it is common to have more than 10 sprints and that’s where this antipattern can show up ]({filename}/images/2019-12-10_agile_antipatterns/scrum-taiga.jpg)
<small>An example of a small Taiga project using Scrum: it is common to have more than 10 sprints and that’s where this antipattern can show up</small>




##... and a Big Fat Lie: "In Agile It Is Forbidden to Estimate the Effort of a Task"

We reserve for the end a very controversial issue in the agile circles partly promoted by the interests created by a quick sale of agile in certain contexts. In Agile it is very valuable to estimate regardless of our ability to predict, as we said in the fourth anti-pattern, what concrete expression a product will have at a future date. To begin, estimating serves to provide quality to a user story and manage its priority with knowledge of the cause. They are not contradictory issues although one is often used in a fallacious sine qua non exercise.
What is true is that estimating is an often laborious process for which quality time is not reserved and with very high risk of waste. Of course, we must know "how many layers of paint" estimate to give each user story at each time.
By the way, aware of this huge challenge in the teams, Taiga 5 comes with Taiga Seed, a small but powerful additional tool to facilitate the estimates that we hope will allow the teams to perform this very interesting work much more frequently.


![Taiga Seedtime with an anti-spoiler filter ]({filename}/images/2019-12-10_agile_antipatterns/seedtime.jpg)
<small>Taiga Seedtime with an anti-spoiler filter</small>


##Final remarks

Almost two decades after the publication of the agile manifesto, no multipurpose framework has emerged that better solves the scenario of uncertainty and speed of the Internet era. It is not a panacea and many agile experts excuse themselves by blaming failures on bad practice when the model fails. However, in some cases we should ask ourselves whether Agile is the right methodology. What is certain is that there is a high probability of failing with a dysfunctional Agile, an Agile that pursues the promises of this model but drags old methods with excuses and fears of the past. A guaranteed formula for disaster.
