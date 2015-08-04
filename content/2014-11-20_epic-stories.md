Title: EPIC Stories
Date: 2014-11-20 10:17
Category: General
Author: Antonio de la Torre
Email: antonio.delatorre@kaleidos.net
Summary: ![EPIC Stories]({filename}/images/2014-11-20_epic-stories/epic_stories.png){: style="width:100%" } Last week we had an interesting email exchange amongst the team at [Taiga.io](https://taiga.io "Taiga.io"). It went like this: The question was a recurring one amongst users of our platform. *What is an epic story?*

![EPIC Stories]({filename}/images/2014-11-20_epic-stories/epic_stories.png){: style="width:100%" }
<small> _Photo Credit: [Kulawat Wongsaroj][photo-author] from the post [Visualizing the Big Picture of your Agile
Project][photo-post]._</small>

Last week we had an interesting email exchange amongst the team at [Taiga.io][taiga]. It went like this: The
question was a recurring one amongst users of our platform

**What is an epic story?**

I answered:

> According to the inventors of agile, An EPIC story is a large undefined user story that must be subdivided.
>
> An EPIC must be broken down into smaller user stories. As far as I recall, user stories should follow the
> "INVEST" pattern where "I" stands for "independent" and "V" for "valuable". In my opinion, an EPIC can make
> sense and be visible, perhaps in a different color so as to reflect its state as an embryonic proto-story,
> but not part of the application structure in the guise of a module or layer.
>
> **That leads to other questions:**
>
> All those subdivided and tiny user stories, would not deploy alone, they are related.
>
> Indeed, this is where the idea of EPIC can be useful as an aggregator of user stories. That is to say as
> an encompassing module. But you have to be careful as it can be very confusing to manage such a thing on
> any project management tool, or even on paper. It makes it very difficult for any client to prioritize as
> there are too many dependencies. Using tags will probably help here I think.
>
> **Are my designer’s prototypes a big story, an EPIC?**
>
> If so, then that can be either a problem of documentation, or that the designer is working on prototypes
> before user stories are specified, or that they’ve been broken down by the back end engineers with all of
> what that entails, or some combination of all three. If the user stories are independent they should each
> have a very clear prototype. You shouldn't have to dig deep to see which button refers to the user story
> that you are addressing at any specific moment.
>
> **But aren’t EPICS a way to group large functional blocks of the project, For example an API, the front part,
> Mobile?**
>
> No. But you can call these "modules" or something similar to that, but these modules don't have any specific
> value. The word EPIC is used by Mike Cohn in his book, so it is the official:-). I searched Google and found
> this wonderful article by Mike Cohn talking about all this:
> [Agile User Stories, Epics and Themes](https://www.scrumalliance.org/community/spotlight/mike-cohn/march-2014/agile-user-stories-epics-and-themes "Agile User Stories, Epics and Themes"). It's a copy of this 2001 article:
> [Agile User Stories, Epics and Themes](http://www.mountaingoatsoftware.com/blog/stories-epics-and-themes "User Stories, Epics and Themes")

Following this email exchange, **we had a meeting to define what an EPIC could look like on [Taiga]{taiga}?**

EPICS can be useful, and serve as the basis for a preliminary analysis, it can be the framework for conversations,
diagrams, wireframes, even prototypes. That's information we want to capture.

If we divide and EPIC into smaller stories, where do we put all that information? We decided that in
[Taiga]{taiga} the final format will be a user story marked as EPIC and distinguished in the backlog by its
color. The EPIC and all its derived user stories Will be related to one another and in that manner we will be
able to access all the previous information should it be necessary.

As a bonus, that aggregation of user stories into an EPIC Will allow us to then track the number of stories that
have been completed, providing us with something similar to a module or a grouping of related stories.

As an additional bonus, the stories that may emerge from an epic may not necessarily pertain to the project at
hand, perhaps they ought to belong to a subproject. We could then have a "base" project in the form of: "Main
Company" an EPIC named "Christmas Campaign", user stories pertaining to that EPIC in the sub-project, "Marketing
Department" such as "TV Spots". All of these being related and trackable from the EPIC itself.

What do you think?


[photo-author]: http://www.infoq.com/author/Kulawat-Wongsaroj "Kulawat Wongsaroj"
[photo-post]: http://www.infoq.com/articles/visualize-big-picture-agile "Visualizing the Big Picture of your Agile Project"
[taiga]: https://taiga.io "Taiga.io"
