# Assignment: CD

You need to master the following to complete this assignment:

- Creating and provisioning a server at Digital Ocean;
- Connecting to a Linux server over SSH;
- Running basic terminal commands on a Linux server;
- Deploying a Flask application on a Linux server.

**Continuous Deployment (CD)** is the idea of having the product your team is working on be deployed frequently, where 'deployed' means packaged and distributed to the customer(s). For the web, this mostly means updating some code. It is not set in stone how frequent deployment should happen before it's 'continuous'. Some teams work with nighties (nightly releases) and other teams deploy several times a day.

In this assignment you will use GitHub Actions to implement a continuous deployment **pipeline**. As a starting point, we assume you have set up a VPS running a Flask application as described in a previous exercise. If this is not the case, go back to those instructions and set one up.

The continuous deployment pipeline should look like this:

- You manually write, commit and push some code. This only requires you to be familiar with **git**.
- GitHub Actions runs tests on your code. You can use **Pytest** for this.
- If and only if the tests pass, GitHub Actions logs into the VPS you have running with Digital Ocean and runs commands such that the code is updated to the latest version.
  
The only new part here is step 3, and we will let you think about how to best implement this. Here are some tips that you might find useful:

Tip 1: [GitHub: Deploy Keys](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/managing-deploy-keys#deploy-keys/)

You can think of an SSH key as a username and password in one. You can use it to make reading and writing to repositories under your account on GitHub easier. A deploy key is an SSH key that grants access to just one repository. You can even set the key to only allow read-only access for extra security.

Tip 2: **sh** files. You should be fairly comfortable with the Bash by now. For this assignment it would come in handy if you were able to chain Bash commands! This can be done by placing commands you want to run in a **.sh** file and running it with **sh example.sh**. It's just like programming in any other language!

```bash
echo "Here is some code."
echo "We wrote it in Bash."
echo "Bash is just a programming language, really."
# This is a comment.
# Let's read a file.
cat some_file.txt
# Do something extremely useful for continous deployment
git pull
# Hmmm, we should probably restart the application after we've pulled in
# new code, otherwise we can be looking for what went wrong for quite a
# while..
systemctl restart my-application
```

Tip 3: **Secrets**. In order to execute commands on the VPS that your application is running on you need to have access to it within a workflow on GitHub Actions. On the other hand we don't never want to put log-in credentials in the repository itself. The way to do this is by using encrypted secrets.

- [GitHub Actions -- Creating Encrypted Secrets for a Repository](https://docs.github.com/en/actions/security-guides/encrypted-secrets#creating-encrypted-secrets-for-a-repository)
- [GitHub Actions -- Using Encrypted Secrets in a Workflow](https://docs.github.com/en/actions/security-guides/encrypted-secrets#using-encrypted-secrets-in-a-workflow)

💡 Note

It's usually not a good idea to give continuous deployment pipelines root access to your server, but we will accept it for this assignment. If you are interested, you can look into how to create and use new users on Ubuntu (and Linux in general).

It's up to you to put the pieces of the puzzle together and create the continuous deployment pipeline as described above. The complexity of your Flask application is not important here, only that you use a GitHub Actions workflow to test and -- if it passed -- update the code running on your server after a push.

Finally, write a short, 200/300-word report in which you discuss at least the following:

- Name three components of your solution, explain what they are and how they relate to each other. A 'component' can be anything from GitHub Actions or Bash to Digital Ocean and SSH.
- Discuss three problems that you encountered along the way and how you solved them.
- (optional) Anything of note that you want to share about the process of solving this assignment.

You can include this report as a **README.md** file in your repository. You can use Markdown syntax to structure your document if you want, but it is not required.
