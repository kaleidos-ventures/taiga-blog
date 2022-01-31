Title: Important update on TaigaNext and Kaleidos
Slug: update_taiganext 
Category: Announcements
Author: Taiga Team
Email: support@taiga.io
Summary: ![Current Taiga6 vs TaigaNext (WIP)](/images/2022-01-26_update_taiganext/taiga6-taiganext.jpg) Despite the fact that we have been actively working on Taiga's next version, we haven't posted an update on how things are going with the next major release of Taiga as well as Kaleidos' plans in general. This article should address all that!


Despite the fact that we have been actively working on Taiga's next version, we haven't posted an update [since last summer](https://blog.taiga.io/announcing_taiganext.html) on **how things are going with the next major release of Taiga as well as Kaleidos' plans in general.** This article should address all that!

You might remember that we, as part of Kaleidos' team, [decided to put aside all other consultancy commitments and focus on Taiga and Penpot](https://blog.kaleidos.net/Taiga-and-Penpot-lead-our-new-chapter-at-Kaleidos/), our two open source products. We did that because we believe it's the right thing to do if we want to get to the next level in terms of adoption and innovation. The transition to this new stage in our professional careers required almost the entire 2021 to become a reality but as for 2022, the entire Kaleidos team is behind this new era devoted to our own free & open source products. This means that both Penpot and Taiga teams have recently grown in both dev and design capacities, which is wonderful.

![Taiga team at a daily meeting](/images/2022-01-26_update_taiganext/Taiga_team_daily.jpg)
Taiga team at one of their daily meetings 

Before we go into the details of TaigaNext's progress, a quick note on [Penpot](https://penpot.app), its sister project. If you don't know **Penpot, it's the first professional open source design & prototype tool for multi-disciplinary teams.** Unlike the many options in project management, relevant design & prototyping tools are limited and are all proprietary. Basically, Figma, Sketch or Adobe XD are the ones that come to mind. We want to change that forever with Penpot and our bet on open standards like [SVG, its native format](https://help.penpot.app/faqs/). This factor allows developers and designers to work closer than ever with a tool compatible for both.

![Penpot workspace](/images/2022-01-26_update_taiganext/Penpot_flows_demo.jpg)
Penpot workspace: prototyping demo 

#### What's going on with TaigaNext?

Why don't we just call it Taiga7? Because we feel we need to have a different codename that reflects our ambitions, but you can privately think of it as Taiga7 if you want. [Esther Moreno](https://kaleidos.net/kaleiders/720B34), one of the UX designers at Taiga said the other day: 

>*"I love the fact that we can question **everything** with TaigaNext, we don't have to take anything for granted, nothing".* 

Exactly, that's the spirit. And because of that, we prefer to keep the repo private for a bit longer. If you had an estimated couple million users of your existing product and you needed some focus for a breakthrough release, you would probably consider the pros and cons of opening the repo up early on. 

Now, we can answer some questions already. Technology-wise nothing has changed, we are based on PostgreSQL, Python, Django, a Restful API and Angular but we are developing TaigaNext almost from scratch and using all the best practices of today (and a bit of tomorrow). We are focusing on the best possible user experience (including blazingly fast load times) keeping three aspects in mind:

- World-class API. This has been one of the key advantages of Taiga in the past and will continue to be. Taiga's web client will consume Taiga's API. [Yamila](https://kaleidos.net/kaleiders/D70A53), [David](https://kaleidos.net/kaleiders/FFF8E7), [Teresa](https://kaleidos.net/kaleiders/0F0F0F) and [Daniel](https://kaleidos.net/kaleiders/71A6D2) are working hard on this.
- UX redesigned and improved. You will recognize Taiga but you'll get the best possible *version* of the features we have (Scrum, KANBAN, issues, etc). [Miryam](https://kaleidos.net/kaleiders/32BDA0), [Esther](https://kaleidos.net/kaleiders/720B34) and [Natacha](https://kaleidos.net/kaleiders/492858) are obsessed about this.
- Accessibility. We are taking this very seriously and we'd love to share some more details in the future. Taiga aims to be the most accessible project management in the world. In order to do that, we are including accessibility as part of the design and development process. The frontend team with [Ramiro](https://kaleidos.net/kaleiders/E32841), [Marina](https://kaleidos.net/kaleiders/FF8A80), [Juanfran](https://kaleidos.net/kaleiders/40826D) and [Xavi](https://kaleidos.net/kaleiders/CC0000) are keeping a close eye on this.

In terms of licensing, we stick with MPL 2.0 and you will be able to host your own Taiga server as well as benefit from our Taiga SaaS offer at taiga.io.

#### Any new features?

Since we're developing TaigaNext almost from scratch, our first priority is to get *on par* with Taiga6 feature-wise. Now, having said that, we are already introducing new abstractions for managing organisations and teams so that you can better represent your reality. We call this *Organizations and Workspaces*. We are also taking a look at email integration, roadmaps and multi-project reporting. Additionally, we want to link Taiga with Penpot and allow for a seamless transition between the agile/lean process and the design process for projects/teams.

![Taiga6 vs TaigaNext](/images/2022-01-26_update_taiganext/taiga6-taiganext.jpg)
Current Taiga6 versus TaigaNext

Apart from this, we want to make sure that you can adapt Taiga even more to your use case. We have identified perfectly valid agile implementations that could benefit from some nice Taiga changes. Both Scrum and KANBAN modules will evolve to serve that purpose. That is why it's so important that [we keep listening to Taiga6 feedback](https://resources.taiga.io/extend/how-can-i-contribute/), it immediately feeds into TaigaNext development process.

Actually, our recent announcement on [Taiga+Zapier integration](https://resources.taiga.io/extend/zapier/) seeks to better understand how people decide to extend Taiga either *against* Taiga itself or with the help of other tools. For instance, if we see a lot of people adding workflow automations to their projects, that's evidence we can use for TaigaNext.

#### What happened after we opened up the Taiga SaaS free tier?

This might not be a question you had in mind but it was part of our new strategy and we wanted to share the preliminary results with you. In the past, Taiga's SaaS free tier was quite limited for private projects (public projects were always free no matter your team's size) so **we decided to give it a boost and set it at 5 private projects and 15 team members in total.** This generous move has been met with an even more generous response. Signups are an all-time high as well as invites sent. We thought this would, in turn, show a decline in the number of Taiga private instances (less incentive to run your own server if you are a small organisation, perhaps?) **but that hasn't slowed a bit**. Our optional anonymous telemetry (thanks for not switching it off, by the way, it helps us a lot) tells us quite a different story so we're quite happy.

By the way, we did some statistical analysis on this anonymous aggregated telemetry from Taiga servers and we discovered that:

- There are many more big Taiga instances than we previously thought. For us, a **big** Taiga instance means it serves **more than 500 users**.
- On average, mid-to-big Taiga instances (>250 users) have a higher activity score *per user*. We don't know how or why because we don't get specific data, although we speculate that it might be due to more integrations taking place, so *bots* and *scripts* could be the ones to blame for that extra activity?

#### Next steps

We're eager to share all the great stuff we're working on and at the same time we don't want to give away important aspects around new branding and *secret weapons*, etc., particularly while it's WIP and rough on the edges. We will consider a monthly report here or perhaps a live stream discussing a bit of agile and TaigaNext. We might send out a survey soon to ask for your opinion on this and other topics related to the product itself.

If you have more questions, feel free to ask in the comments section below. 

---

*[Sign up](https://www.taiga.io/trialsignup?hash=d95e930f99866fac03e5555f9634588e&landing_source=homepage&IP=77.229.149.140&_landing_hash=b192ae461649b7e7d078&_landing_version=nO0qRtWrDpRLjjIqj.9ZM9KYScWUZ2GS) and try Taiga for free with access to all features during 30 days!*