Title: What’s an Epic? Our research
Date: 2016-10-13 10:00
Category: General
Author: Esther Moreno
Email: esther.moreno@kaleidos.net
Summary: ![Epics]({filename}/images/2016-10-13_epics-research/epics_research.jpg "Epics") If you work with agile methodologies, you’ve surely heard about epics. Epics are hard to define, because there isn’t an official definition, and if you ask around you’ll see that not everyone shares a unique idea of what an epic is. But if you watch how people use epics you can get a clue about them.

If you work with agile methodologies, you’ve surely heard about epics. Epics are hard to define, because there isn’t an official definition, and if you ask around you’ll see that not everyone shares a unique idea of what an epic is. But if you watch how people use epics you can get a clue about them.

Say you’re defining a user story. While doing so, you realize how diffuse everything is, you still don’t have all the information, the story is too big and it will take more than one sprint… “Diffuse” and “Big size” are pretty much the opposite of what a user story is, so you might be looking at an epic.

![Epics]({filename}/images/2016-10-13_epics-research/epics1.png "Epic research")
<small>Diffuse and Large</small>

Traditionally, teams keep epics alive until they have more information. Then they’re divided into detailed user stories and finally deleted. However, for many teams it is interesting to keep the epic as a container of user stories, as a reference, or to store general documentation about the whole feature, such as requirements, wireframes, designs...

![Epics]({filename}/images/2016-10-13_epics-research/epics-wrap.png "Epic wraps US")
<small>Container of user stories</small>

We had no epics in Taiga, so our customers would resort to all sorts of hacks to achieve a similar effect:

- Using a common tag for a few user stories, so that they’d belong to the same category
- Adding the word EPIC to a user story’s title, to better identify them
- Creating multiple projects (one per epic) so that user stories would be grouped
- Creating large user stories (tagged as ‘epic’) and moving them from sprint to sprint until the epic was finally closed
- …

We knew that these tricks didn’t really solve the issue, and that we’d have to take care of it ourselves, eventually. Well, that time has finally come : )

As you can imagine, this is a big challenge: adding a feature that’s critical for many customers, and making it flexible and adaptable for any workflow (this is particularly important, since there’s no official literature about epics and each team solves them in their own personal way).

Epics need to solve a need, but what do teams really need? At Kaleidos we already had some feedback from our own teams and customers, but it wasn’t enough. So we did some research about how stuff is done out there, and we now want to share the results with you.

###Lego workshop
In order to get familiar with the concepts, we organised a small workshop with LEGO, where we asked participants to build a workflow with epics. This workshop was an experiment, with a very limited number of attendees: a developer (JuanFran) and someone with a more strategic vision (Pablo). **The outcome was very interesting: each of them had a different concept of what an epic was.** JuanFran considered an epic as somebody else’s responsibility, completely unconnected to his daily work. Pablo saw it as something connected with many departments, that would allow him to get information from many sources.

![Epic lego workshop]({filename}/images/2016-10-13_epics-research/epics-lego.png "Epic lego workshop")
<small>LEGO Workshop</small>

###Survey
The main part of our research took the form of a survey. Thanks to Toño (who was then working as a developer at Kaleidos) we got in touch with a diverse group of people on the software world. Some of them worked developing products, some of them did consultancy work, using different team management tools, at different company sizes, etc. The objective of the survey was to know more about the work process around epics, answering a few questions that would help us get a better idea of what people had in mind when they used the word ‘epic’. The questions were:

1. Should an epic live inside a sprint (along with the rest of the user stories)?
2. What about Kanban (along with the rest of the user stories)?
3. Is an epic a user story of type ‘epic’, or is it something else?
4. Can a user story belong to two different epics?

The answers to these questions were presented visually. It was important to know which were the most common opinions. As an example, here’s how the first question “Should an epic live inside a sprint (along with the rest of the user stories)?” was presented on that document:

![Epic survey]({filename}/images/2016-10-13_epics-research/epics-survey.png "Epic survey")

<small>In Spanish 'Sí' means 'Yes'</small>

Most people thought they shouldn’t, even when our first impression had been the exact opposite (probably because everyone at Kaleidos thought it was more “logical” that they would).

In addition to the answers to these questions, the reasoning behind them revealed some subtle details (did the delete epic after splitting them? if they didn’t, why did they use them? who was responsible for managing epic?…). This gave us a very rich information and a pretty complete perspective about their usage.

###Conclusions

- Epics have some similarities with user stories, but they’re not the same. They’re bigger, diffuse, and work as containers for user stories.
- Epics are usually reviewed by people with more strategic roles on a project. Not all team members need to see them regularly.
- You can create an epic from the start, when you’re dealing with a diffuse task; or turn a user story into an epic if it turns out to be bigger than you initially imagined.
- An epic can be deleted or kept after splitting it into user stories. Most team keep them around.
- It is generally accepted that epics shouldn’t get mixed with user stories on sprints or kanban, but they should have their own kandan or dashboard to manage them and understand their progress.
- If an epic won’t be deleted, it’s a good place to store general information like UX wireframes, design documents, etc… Adding UX and design disciplines to agile teams raises some issues like this one (where to store documentation) and this could be a way to solve it.

If you want to take a look at the whole research, you can [download this PDF]({filename}/images/2016-10-13_epics-research/EPICS_Research_Taiga.pdf "Epic research full"){target="_blank"} (In spanish)

If you want to know more about epics, here’s a post we wrote about them over at Taiga’s blog: https://blog.taiga.io/epic-stories.html

Thanks a lot to the people who helped us with their experience and feedback about this issue. Now you’re also part of Taiga:

- Rafa Fonts [@boronatix](https://twitter.com/boronatix){target="_blank"}
- Ángel Díaz-Maroto [@adiazmaroto](https://twitter.com/adiazmaroto){target="_blank"}
- Ángel Medinilla  [http://bit.ly/AngelMedinilla](http://bit.ly/AngelMedinilla){target="_blank"}
- David Bonilla [@david_bonilla](https://twitter.com/david_bonilla){target="_blank"}
- Jerónimo Palacios [https://jeronimopalacios.com](https://jeronimopalacios.com){target="_blank"}
- Carlos Ble [@carlosble](https://twitter.com/carlosble){target="_blank"}
- David Parra Catalán [@dparracatalan](https://twitter.com/dparracatalan){target="_blank"}
- Jose Manuel Beas [@jmbeas](https://twitter.com/jmbeas){target="_blank"}
- Álvaro Sánchez [@alvaromako](https://twitter.com/alvaromako){target="_blank"}
- Vanesa Tejada [@vanesa_tejada](https://twitter.com/vanesa_tejada){target="_blank"}
- Eduardo Ferro Aldama [@eferro](https://twitter.com/eferro){target="_blank"}
- Raúl Herranz [https://es.linkedin.com/in/raulherranz/es](https://es.linkedin.com/in/raulherranz/es){target="_blank"}
- Israel Alcázar [@ialcazar](https://twitter.com/ialcazar){target="_blank"}
- Primitivo Cachero [@primicachero](https://twitter.com/primicachero){target="_blank"}
- Maria Luisa Muñoz Chavarrias [@marisamunoz](https://twitter.com/marisamunoz){target="_blank"}
