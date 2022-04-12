Title: How to set up a free Oracle virtual machine
Date: 2022-04-11 12:25
Category: Networking
Tags: Virtual Machine, Oracle
Author: Freddie Larkins
Summary: Oracle have a handy little always-free tier where you can access two virtual machine instances. Here's how to get started.
Slug: how-to-set-up-a-free-oracle-vm-standard-e2-1-micro-instance

**I was looking for a free virtual machine to run some Python scripts on, and came across Oracle's free virtual machines.**

On their always-free tier, you can set up two virtual machine instances, each with 1GB of memory and 1 OCPU (or 'Oracle CPU').

The instances are in Oracle's **VM.Standard.E2.1.Micro** 'shape'. Oracle offer a load of different '[shapes](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computeshapes.htm)', each with differing amounts of computing power.

The VM instances are certainly not as powerful as a laptop, but for small/recurring tasks they're great. Plus, if you're a newbie like me, you get to learn a little about networking and accessing remote machines.

**This article will take you through how to get your own VM instances up and running.**

[TOC]

## Setting up your first VM instance

### 1. Set up an Oracle Cloud account

Head to [Oracle's website](https://www.oracle.com/uk/cloud/free/) to sign up for a free-tier Oracle Cloud account.

![The sign-up page for Oracle's free-tier Cloud account.](/images/webp/oracle-sign-up.webp)

You will be asked to provide payment details but as long as you don't stray from the 'always-free' services, you should be alright! I haven't seen any charges on my account yet.

### 2. Sign in and create your instance
Once your account is created, [sign in](https://www.oracle.com/uk/cloud/sign-in.html) to your newly-created Oracle Cloud account.

On your account [homepage](https://cloud.oracle.com/), scroll down until you see ['Create a VM instance'](https://cloud.oracle.com/compute/instances/create).

![The 'Create a VM instance' button on the Oracle Cloud account homepage.](/images/webp/oracle-create-instance.webp)

Click on the button and run through the setup form. The first thing to do is name your instance:

![The first stage of setting up a VM instance.](/images/webp/oracle-create-stage-1.webp)

For the purposes of the demo, you'll see that mine is called `website-demo`. You can name yours whatever you like.

You can leave everything else alone. The only other thing you should do before creating your instance is download the private key to connect to the instance via SSH.

![The button to download a private key in the setup page.](/images/webp/oracle-create-stage-1-ssh.webp)

And that's all! Once you've hit `Create` in the bottom bar, you'll be taken to the page that [lists all your instances](https://cloud.oracle.com/compute/instances). In my case, clicking on my `website-demo` instance takes me to the details page for that instance:

![Details page for my VM instance.](/images/webp/oracle-provisioned-instance.webp)

It takes a couple of minutes for the instance to get up and running after you create it; the status may initially show as `PROVISIONING` on this page.

### 3. SSH into your instance
Secure Shell Protocol (or SSH) is a protocol for securely connecting to remote machines. I'm assuming a level of familiarity with the `ssh` command here - if you're looking for an intro to SSH, I quite like [Computerphile's explanation](https://youtu.be/ORcvSkgdA58) on YouTube!

#### Add your virtual machine to your SSH `config` file
This step is optional but will save you from having to remember the IP address of your VM instance every time you want to connect to it!

Navigate to the `.ssh` folder in your home directory and create a file called `config` if it doesn't already exist. Replace my details with the equivalent ones for your VM instance:
```shell
# replace with the 'human-readable' name for your instance
Host website-test
	
	# replace with the public IP address of your instance
	HostName 123.456.789

	# keep the same!
	User opc

	# replace with the file path of the private key you saved earlier
	IdentityFile /path-to-your-private.key
```

With the config file updated, connecting to my VM is as simple as:
```console
$ ssh website-demo
```
If you're connecting for the first time, you may be denied entry the first time. Simply try again. Your terminal output should look something like this:

```console
$ ssh website-demo

Are you sure you want to continue connecting (yes/no/[fingerprint])? yes

Warning: Permanently added '123.456.789' (ECDSA) to the list of known hosts. 
Activate the web console with: systemctl enable --now cockpit.socket
Last login: Thu Apr 7 12:29:02 2022 from 84.245.194.200
```
And then you'll be in!
```console
[opc@website-demo ~]$
```
### 4. Optional: upgrade the software packages on your instance
It's generally a good idea to keep the software up-to-date on your laptop - the same applies to your virtual machine!

You can download the latest versions  all the preinstalled software on your instance with the following command:
```console
[opc@website-demo ~]$ sudo yum update -y
```
When I first did this, it took about 17 minutes for everything to download and update. Go and grab a cup of tea! You should see something like this in your terminal prompt:

![Terminal prompt showing the system packaged being updated on the VM instance.](/images/webp/system-update.webp)

And that's it. You could use it to run a [bin collection reminder bot](/building-a-bin-collection-reminder-bot-in-python.html), or do web-scraping tasks with Selenium. Enjoy!