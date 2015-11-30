Title: Priority and severity: What’s the difference?
Date: 2015-11-30 09:53
Category: General
Author: Nitish Tiwari
Email: tiwari.nitish@gmail.com
Summary: ![stone and pen]({filename}/images/2015-11-30_priority_and_severity_what_is_the_difference/balanza.jpg) Filing bugs is a mundane task - everyone does it, from developers to testers, and sometimes even the end users. But many of us don’t understand one of the most important concepts while filing a bug, the difference between priority and severity. While some use these terms interchangeably, others use them with opposite meaning. Let us today clear the misconceptions about these two terms, so that teams can make the full use of their bug management tools.


Filing bugs is a mundane task - everyone does it, from developers to testers, and sometimes even the end users. But many of us don’t understand one of the most important concepts while filing a bug, the difference between priority and severity. While some use these terms interchangeably, others use them with opposite meaning.

Let us today clear the misconceptions about these two terms, so that teams can make the full use of their bug management tools.

![stone and pen]({filename}/images/2015-11-30_priority_and_severity_what_is_the_difference/balanza.jpg)

## Priority

By English definition,
> priority means the condition of being treated as more important than other items or activities in the fray.

So, logically you’d finish something that has a higher priority before than you take any activity with lower priority. Exactly the same applies in handling bugs. A bug with higher priority just means that it needs to be fixed first and then bugs with lesser priority should be taken up. To keep things simpler, let’s not add any extra meanings, i.e. don’t infer that something with high priority has more impact or severity. We’ll come to that in a moment.

For now, just one simple thought - if you are filing a bug, keep in mind that assigning higher priority to a bug means that you want to get it fixed faster than others, and if you are a developer, assigned with a bug that has a high priority, you need to fix that bug first.


## Severity

Let’s consider the English meaning of severity first
> severity measures the implication of something. We call something more severe if it has a greater impact and less severe if it doesn’t.

In the context of bug filing, this means a bug is more severe if it impacts the product in a big way, while it is less severe if it doesn’t have that big an impact. Now, you may think, only when a bug is severe, it will have a high priority, which is sometimes true. But, there may be cases when the bug is not very severe still needs to be fixed on a high priority, for example because of customer requests.


## Four cases

There can be four combinations, if we consider two values each for priority and severity. Let’s understand what each of them mean.

High priority & high severity
: Bugs that can block normal usage or testing or cause a severe system failure, fall under this category. 

High priority & low severity
: Defects which have to be fixed but do not impact the normal usage of application, come under this category. Say for example a particular error is not displayed properly. In this case, functionally the code throws an error, so there is not much impact, yet it should be solved with high priority to avoid discomfort to users.

Low priority & high severity
: Defects that are identified for fixing but not immediately. This can specifically occur during manual testing. It means that the functionality is affected to a large extent, but is observed only when certain uncommon input parameters are used.

Low priority & low severity
: Each project has it’s own dynamics, still generally cosmetic errors like cell sizes, button colors, gradients etc. can be put in this section.


## Priority & Severity in Taiga

While filing a bug in [Taiga](https://taiga.io), you can easily set the severity and priority. You can also filter the defects based on severity and priority.

To file a bug, go to the **issues section** on the left menu bar. Then click on **New Issue** button. This opens the form to add issue

![Lightbox: Create issue]({filename}/images/2015-11-30_priority_and_severity_what_is_the_difference/create_issue_lightbox.png)
<div style="text-align: center;"><small>Create issue lightbox</small></div>

Just fill in the details here. Note that the drop down next to the Bug drop down is the priority field and next to it, is the severity field.

To filter out bugs based on priority or severity, click on the corresponding link on the **secondary menu bar on the left side**.

![Filters]({filename}/images/2015-11-30_priority_and_severity_what_is_the_difference/filters.png)
<div style="text-align: center;"><small>Filter issuees by priority/severity</small></div>

You can also edit severity and priority from the **issue detail page**.

![Issue detail page]({filename}/images/2015-11-30_priority_and_severity_what_is_the_difference/edit_issue.png)
<div style="text-align: center;"><small>Issue detail page</small></div>

And finally, you can manage the available values for severity and priority selectors from the admin panel (**Admin > Attributes > priorities** and **Admin > Attributes > Severities**).

![iAdmin > Attributes > Severities]({filename}/images/2015-11-30_priority_and_severity_what_is_the_difference/admin_edit_severities.png)
<div style="text-align: center;"><small>Admin > Attributes > Severities</small></div>
