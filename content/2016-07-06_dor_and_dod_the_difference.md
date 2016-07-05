Title: Definition of Ready & Definition of Done: the difference
Date: 2016-07-06 10:00
Category: General
Author: Nitish Tiwari
Email: tiwari.nitish@gmail.com
Summary: ![]({filename}/images/2016-07-06_dor_and_dod_the_difference/athletic.jpg) Projects, software or otherwise suffer from the common problem of miscommunication. While the client expects something else, the product owner has a different understanding. Then there are developers who at times have different understanding of work to be done. With Agile, many of such concerns are addressed, thanks to daily standups and clear goals set before a sprint. Still there are some areas that are generally looked upon during the beginning of the project and are only relevant when sprints approach completion. One of those is the clear difference between done criteria and the ready criteria. Generally people use these terms interchangeably causing avoidable confusion. In this post, I will try to clear the air on the definition of done and the definition of ready.


Projects, software or otherwise suffer from the common problem of miscommunication. While the client expects something else, the product owner has a different understanding. Then there are developers who at times have different understanding of work to be done. With Agile, many of such concerns are addressed, thanks to daily standups and clear goals set before a sprint. Still there are some areas that are generally looked upon during the beginning of the project and are only relevant when sprints approach completion. One of those is the clear difference between _done criteria_ and the _ready criteria_. Generally people use these terms interchangeably causing avoidable confusion. In this post, I will try to clear the air on the **definition of done** and the **definition of ready**.

![]({filename}/images/2016-07-06_dor_and_dod_the_difference/athletic.jpg)


### Done criteria

To start with, imagine when will you call something done? You may think, well until I finish everything. The problem is until this “everything” is clearly defined, this is all just vague - everyone will have their own done criteria. So, the key is to make sure done criteria is properly defined at the beginning of the sprint or whenever the task is assigned.

But what is done criteria? It is a guide that dictates when teams can legitimately claim that a given user story/task is "done" and can be moved to next steps, e.g. review, approval by the product owner. Different teams can have different criteria, but they’ll generally have some common items like

* Code review completed by another developer.
* Automated unit tests written and running.
* Smoke tests performed on dev/staging environment.
* QA sign off or paired programming session.
* Meets acceptance criteria stated in the story.

This is our current DoD for the Taiga Dev Team:

>
> For UX role:
>
>   - Are wireframes linked to the user story?
>   - Do they have the necessary annotations to clarify the functionality?
>   - Have you considered all error cases?
>   - Has the navigation map been updated?
>   - Have you updated the UX repository?
>   - Have you checked that the UX does not define multiple conflicting options?
>
> For Design role:
>
>   - Are the designs linked to the user story?
>   - Are there the necessary annotations to clarify the design?
>   - Have you updated the Design repository?
>
> For Front role:
>
>   - Have you added the unit tests (Karma)?
>   - Have you added end-to-end tests (Protractor)?
>   - Is the changelog file updated?
>   - Is the authors file updated?
>   - Is the setup documentation updated?
>   - Have you checked that the contrib plugins still work?
>   - Have you checked that Toggl's plugin still works?
>
> For Back role:
>
>   - Have you added tests?
>   - Is the changelog file updated?
>   - Is the authors file updated?
>   - Is the API documentation updated?
>   - Is the setup documentation updated?
>   - Have you considered performance?
>   - Do you have the needed DB migrations?
>   - Have you checked that the contrib plugins still work?
>


### Ready criteria

Ready criteria is a set of rules that a team adopts as a guide for when a story can legitimately be moved from the backlog into a Sprint. In simple terms, ready criteria indicates the story is immediately actionable.This is generally applicable either during Sprint Planning or during a Sprint where all committed stories have been completed.

You’ll generally see the following criteria applying as ready criteria

* Story has been reviewed and estimated by the team.
* Story is complete in format - `User X needs to Y so they can Z`.
* Acceptance criteria are clear and agreed upon.
* Product Owner has approved the story.

And this is our DoR criterials:

> 1. General overview of the functionality
>     - What it does?
>     - How it behaves?
>     - What is its main purpose?
>
> 2. Should the behavior change for different users?
>     - ...by type of user
>         - anonymous
>         - registered user but no member
>         - project member
>         - project admin
>         - project owner
>         - superadmin
>     - ...depending on the permissions you have
>         - with permissions
>         - without permissions
>
> 3. Does it change for different types of instances?
>     - Is it just for tree.taiga.io?
>     - It is included in the default setup?
>     - Is it the same behaviour for all instances? (can be enabled/disabled, has settings...)
>     - Is it a contrib plugin?
>
> 4. Add acceptance tests expressed in the form
>     - As a user 'X' doing 'Y', I expect 'Z' as a result.
>
> 5. How it interacts with other Taiga's features? (consider the navigation flow)
>     - plugins
>     - csv reports
>     - webhooks
>     - import/export
>     - initial sample data
>     - invitations
>     - emails
>     - Togglr's button
>
> 6. Does it change according to the amount of data?
>     - using data?
>     - no data? / placeholders are needed?
>     - can we have reliable statistics?
>
> 7. Was there related feedback and has it been taken into account?
>
> 8. Do you want to measure something?: business statistics, traceability of users...
>
> 9. Should we create/edit any section in the support documentation?
>
> 10. Is the team aware that this feature now exists?
>

### Conclusion

If you’d like to take away one thing from this, I’d like to sum it up for you - done criteria defines when a task/story can be moved to next stage after implementation is completed, so this is ideally applied at a later stage when a task is reaching completion, while ready criteria defines when a task/story can be taken up in a sprint for action, hence this generally applies at the planning/beginning stage of the sprint.

We hope this clarifies the air around the criteria confusion and helps you manage your project better. We would love hear any stories you have about criteria confusion in your project and how you overcame it. Just post them in comments section.
