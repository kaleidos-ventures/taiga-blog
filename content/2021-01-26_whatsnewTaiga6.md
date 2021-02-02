Title: Taiga6: what's new in this historic release?
Date: 2021-01-26 09:00
Slug: taiga6-release
Category: Announcements
Author: Taiga Team
Email: support@taiga.io
Summary: ![Taiga6 overview](/images/2021-01-26_whatsnewTaiga6/taiga6.jpg) A year in the making! We spent the best part of 2020 figuring out what the future of Taiga and agile project management should look like. Even if this new journey has just started, we couldn't wait to share with you a glimpse of that feature. Behold Taiga6!

![Taiga6 overview](/images/2021-01-26_whatsnewTaiga6/taiga6.jpg)

That's right, we, the Taiga team, felt we were at a crossroads. On one hand we had **a stable and sustainable open source business** that could evolve at a steady but calm pace. On the other hand, we felt **we should be doubling down on our agenda** towards a much better agile project management experience. The challenges were many, both technological and product driven. So far, we have tackled just a few of them and **that's exactly what we're presenting today as Taiga6**, our best release **ever** since Taiga 1.0.


<h2><a id="lets-start-with-the-obvious-stuff">Let's start with the obvious stuff</a></h2>

Sure, you might be as excited as us but you need **to see and feel** the new release. We absolutely get it! We've put together an express overview of the major changes that come with Taiga6.

<h3><a id="user-interface-revamp">User Interface revamp</a></h3>


Taiga's user interface has never stopped evolving but it had aged quite a bit. We're not talking just a new theme or some polishing, it's really **more intuitive, slicker and faster than ever**. This is still a work in progress but it's impossible not to notice the improvements. We believe this will be one of those major UI changes that will garner almost **universal positive recognition**.

[![Taiga6 UI revamp example](/images/2021-01-26_whatsnewTaiga6/revamp.gif)](/images/2021-01-26_whatsnewTaiga6/revamp.gif)
<figcaption>Before & After for Scrum's backlog, that's *compactness*. Click to enlarge.</figcaption>


[![Taiga6 UI revamp example](/images/2021-01-26_whatsnewTaiga6/kanban-then-and-now.gif)](/images/2021-01-26_whatsnewTaiga6/kanban-then-and-now.gif)
<figcaption>Before & After for KANBAN, what's not to love really?. Click to enlarge.</figcaption>


[![Taiga6 UI revamp example](/images/2021-01-26_whatsnewTaiga6/DND-interaction-taskboard.gif)](/images/2021-01-26_whatsnewTaiga6/DND-interaction-taskboard.gif)
<figcaption>Nice feedback, nice touches. Click to enlarge.</figcaption>


<h3><a id="swimlanes-on-kanban">Swimlanes on Kanban</a></h3>

Taiga's KANBAN ranks high in flexibility and features. That's probably because we always thought KANBAN was deceptively simple and we made sure you got **all its potential**, not a second-class agile citizen. But... we lacked swimlanes. **Swimlanes allow your team to create independent paths** for your KANBAN cards and enjoy a much more powerful and flexible visual management state of things. Swimlanes can be almost anything you consider to deserve a particular space, from subteams to priorities or miniprojects. Try them out!


[![Taiga6 swimlanes](/images/2021-01-26_whatsnewTaiga6/kanban-with-swimlanes.png)](/images/2021-01-26_whatsnewTaiga6/kanban-with-swimlanes.png)
<figcaption>A nice two-swimlane shot. Click to enlarge.</figcaption>

[![Taiga6 swimlanes interaction](/images/2021-01-26_whatsnewTaiga6/swimlanes-interaction.gif)](/images/2021-01-26_whatsnewTaiga6/swimlanes-interaction.gif)
<figcaption>KANBAN swimlanes interaction with cards. Click to enlarge.</figcaption>

<h3><a id="better-use-of-space">Better use of space</a></h3>

Even if our screens get larger and larger and their resolutions dream of becoming 8K, we are quite *effective* at finding ways to get our digital workspace cluttered. Taiga was always weary of that annoying tendency to put on display as much as possible. What we've done is learn from user feedback, user interactions and most common behaviour pattern **to redesign where things are, when they do appear and how you know they are there**. *Lists of items* in particular and also *zoom levels* have been redesigned with your precious cognitive load in mind.

[![Taiga6 collapse mockup](/images/2021-01-26_whatsnewTaiga6/taskboard-animated-mockup.gif)](/images/2021-01-26_whatsnewTaiga6/taskboard-animated-mockup.gif)
<figcaption>Collapse mockup concept. Click to enlarge.</figcaption>

[![Taiga6 collapse sprint taskboard](/images/2021-01-26_whatsnewTaiga6/better-use-of-space.gif)](/images/2021-01-26_whatsnewTaiga6/better-use-of-space.gif)
<figcaption>Collapse in action at Sprint taskboard view. Click to enlarge.</figcaption>


<video autoplay="" muted="" loop="" playsinline=""  class="screenshot__media" width="100%" height="auto"><source src="/images/2021-01-26_whatsnewTaiga6/improved-filters-1.mp4" type="video/mp4"></video>
<figcaption>Really, this is a so much better filter panel.</figcaption>


<h3><a id="taiga-resources">Taiga Resources</a></h3>

We had lots of information about Taiga scattered around. We decided to inventory all that was relevant about Taiga and create a [new resources centre](https://resources.taiga.io) for you to be assured that either your information need is satisfied there or it's accessible through it. **Nearly everything has been written again from scratch**, from tutorials, critical articles on agile techniques, community contributions or FAQs.

[![Taiga6 resources](/images/2021-01-26_whatsnewTaiga6/resources.jpg)](https://resources.taiga.io)
<figcaption>Screenshot of Taiga Resources landing page. Click to visit Taiga Resources.</figcaption>

<h3><a id="new-and-improved-text-editor">New and improved text editor</a></h3>


Our dual HTML/Markdown editor was good enough for some time but it was time to acknowledge the amazing work by the great people at CKEditor. We have tweaked it a bit to address our Right-To-Left needs and also some convenient "stay on top" mode as well as keeping with the good "non-destructive mistakes" habits. Taiga's new editor will try hard **to protect your half-baked changes whether your accidentally** refresh page or click on cancel, hit escape, etc.

[![Taiga6 editor](/images/2021-01-26_whatsnewTaiga6/editor.gif)](/images/2021-01-26_whatsnewTaiga6/editor.gif)
<figcaption>Just focus on nice content...</figcaption>

<h2><a id="docker-image">Docker image</a></h2>

We have back-pedalled on one of the most sacred long-standing truths here at Taiga; *"don't devote resources to an official on-premise/private cloud Taiga image"*. **The response from the community was absolutely amazing** providing quite a number of really great Taiga docker images and alternative deployment schemes. Eventually, we decided we should be taking a stance on the hundreds of thousands of private Taiga installations out there and **provide an [official Taiga docker image](https://github.com/taigaio/docker-taiga)**. Depending on its success and acceptance, we hope to expand to other ways for deploying Taiga.

[![Taiga6 editor](/images/2021-01-26_whatsnewTaiga6/docker.jpg)](https://github.com/taigaio/docker-taiga)
<figcaption>Visit our [docker repository](https://github.com/taigaio/docker-taiga).</figcaption>

<h2><a id="what-to-expect">What to expect from Taiga in 2021</a></h2>


**Short answer**: A lot. **Long answer**: We want to go from the best open source agile project management platform to become one of the best project management platforms out there. We started this journey a few years ago and we are far from done. We want to do comprehensive under-the-hood tech overhaul as well as starting adding new project modules and really innovative features while we make sure to protect the key Taiga differentiators; **ease of use, flexibility and straightforward agile for cross-domain teams**.

Also, **we developed Penpot**, the first open source design and prototyping platform, [check it out](https://penpot.app)!
