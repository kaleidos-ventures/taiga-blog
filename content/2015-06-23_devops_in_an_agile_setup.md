Title: DevOps in an Agile setup
Date: 2015-06-23 10:01
Status: Draft
Category: General
Author: Nitish Tiwari
Email: tiwari.nitish@gmail.com
Summary: ![One-man band](/images/2015-06-23_devops_in_an_agile_setup/one_man_band.jpg "One-man band") In recent years, agile went from experimental new technique for project management to a mainstream project management philosophy. Almost everyone is doing Agile now evenoutside of software development.

In recent years, agile went from experimental new technique for project management to a mainstream project management philosophy. Almost everyone is doing Agile now evenoutside of software development.

![One-man band](/images/2015-06-23_devops_in_an_agile_setup/one_man_band.jpg "One-man band")
<small>Photo by [Andrew Malone](https://www.flickr.com/photos/andrewmalone/5163238038 "'One man band' by Andrew Malone, on Flickr"){target="_blank"}</small>

###  What is DevOps

One of the most compelling reasons of using Agile over other methodologies is the promise of fast time to market ­ techniques such as continuous integration and test driven development make it possible to be ready with working software at any point of time. But if you take a closer look, is having working code in GitHub repo, end of your responsibilities? Are your customers going to deploy the software themselves? What about the L1 support?

Often the done criteria of a sprint corresponds to working functionalities but actually taking the software to the client involves far more steps, done mostly by the operations & support teams, that too at a very different pace than the development teams. Typical scenario looks like -

![Workflow without DevOps](/images/2015-06-23_devops_in_an_agile_setup/without_devops.jpg "Workflow without DevOps"){style="width: 600px;"}

Now, even if you had working code at the end of sprint 1, it doesn’t really matter till the end of sprint 2, when the operations team actually deploys or releases the software to the customer. Any issues while deployment can delay the release even further. You can see this as two cogs of the system ­ stopping one of them brings the whole system to a halt.

If these cogs belong to the same system ­ why not make them one! That is the thoughtbehind DevOps. If the different teams in an organization are aware of the dependencies of other teams working in tandem, it becomes far more easy to execute a development and release plan flawlessly. DevOps mandates that business, development and operations teams collaborate on a continuous basis to make sure the software solution gets developed and released to the market in a coherent, predictable and timely manner.

Lets see how a DevOps enabled team should generally look like -

![Workflow with DevOps](/images/2015-06-23_devops_in_an_agile_setup/with_devops.jpg "Workflow with DevOps"){style="width: 600px;"}

### DevOps in Agile

Here are a few steps to start organizing your teams in DevOps fashion.

1. Product backlogs: Generally the product backlogs include the requirements from a functional point of view, but in a DevOps set up it is also important to plan and list the environment & deployment requirements like a new configuration or a new server setup required for a feature. This way the dev and ops teams are in sync about the new features and there are no surprises at the release time.
2. Scrum of scrums: It may be difficult to put all the members of all the teams in a single stand up meeting, chaos will ensue. A better approach is to call for a scrum of scrums where scrum masters of different teams (including Ops team) and the product owners can discuss progress and plan their own schedules accordingly.
3. Done definition: Adding operations related items to the done definition is another handy approach to make sure operational issue are addressed (sometimes even before they are caught). Along with routine development related chores like coding, testing, and documentation, adding items like code validation on mock production parts, document updated for platform requirements etc can make sure there are no surprises during deployment.
