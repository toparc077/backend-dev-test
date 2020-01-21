# The ingestion

## Setup
We provide a one-button setup using vagrant and virtualbox which you are more
than welcome to use. If you prefer to use some manually set environment, go for
it, but this is similar to how we maintain integrity between local dev
environments and production down here at Smartia. Having that integrity is
of extreme importance for us, as often the environment involves a mixture
of less-tha-popular technology, maintaining of which manually is unreasonable.

### Vagrant
1. Get [vagrant](https://www.vagrantup.com/) and 
[virtualbox](https://www.virtualbox.org/wiki/Downloads)
2. Steer into project directory and issue `vagrant up`
3. When the command is done, you are ready to go. You can either use [vagrant
box with pycharm](https://www.jetbrains.com/help/pycharm/vagrant-support.html)
which is akin to how we work, or `vagrant ssh` to work in the remote box
console. The choice is yours!

### Non-vagrant
Check Setup section, content of `Vagrantfile` and good luck.

## Your task

### Description
One of our employees just finished a tough period of integrating with two
external services, one that provides us with data from factory, and the other
a proprietary time series database. It is now a working solution, but also not
the prettiest, sitting alone in `ingest.py`, completely away from out Django
stack. Even the barely some tests we started to prepare in `features` following
our favorite [BDD convention](https://behave.readthedocs.io/en/latest/) are
not even started to be implemented yet, or cover all the scenarios right now.

The reason for integration with django is because that is where we keep all our
data infrastructure and pipelines, it serves as focal point of our ecosystem,
and right now we have no plans to get away from it. We didn't include code for
that in the test as it's simply not needed. Just assume that this is quite
big django project already.

### Your task - the required code part
As part of this task we have one hard requirement - we want you to convert the
`ingest.py` into a Django command. A simple task, and very simple test for
someone who has done it previously with django. That's all the code you are
required to do for this task.

### Your task - the fun part
Now with the ingestion moved as django command, we need to whip this repository
into shape. Of course we don't expect you to actually implement that, there
is so much work to be done here - from automating the vagrant file further
(and possibly putting it into ansibles), expanding `.feature` files to cover
all sort of scenario, much more robust django setup with logging, error
reporting and parallelization (one way or another, we will need the ingestion
code to scale both up-ways and side-ways) that asking you to implement even
one of those would be unfair. So we are not going to do that.

Instead we want you to prepare a short presentation on how, given ownership of
this product you would take it from where it's now to a production grade system,
ready and willing to process data in micro and macro scale. You can prepare this
presentation as psudo code, diagram, pps, sharpie notes on your hand - it does
not matter as you will be the one giving the presentation during the code 
review! Don't make it too long too, stick to key points, just like you were
presenting a battle plan to a CTO in a small company. And be prepared to have
the presentation interrupted with question, best to keep it in conversational
format, as this is more of a discussion rather than an academic presentation.

## Final notes
This is a task taken directly from our pipeline just few weeks ago (obviously
simplified, but the core of issue remains) and we cannot wait to hear your 
thoughts on how to solve it! Please do not spent more than 2-3 hours preparing,
it will not net you extra points, and we do not want you to spend enormous
amount of time on throw-away test. Our primary focus is to verify that you do
know how to code, and think like a product owner, who will ultimately have to
deliver and be responsible for the delivery.

We hope that you will have fun with it! Once you are ready, submit a pull 
request with your solution and shoot us an email at jobs@smartia.tech with a
link to your pull request and copy of CV. We will then try to schedule a call
with you as soon as we receive it, and we will review the work together.
