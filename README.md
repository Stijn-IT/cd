# Final assignment CD

## Three components of the solution

- **SSH key**

"An SSH key is an access credential in the SSH protocol."
It has the same function as a password, but after setting up the SSH, acces will be automated.

It consists of a private and public key. You can think of the private key as the key and the public key as the lock. In my assignment I put the private key in github secrets.

- **Github actions**

"GitHub Actions is a continuous integration and continuous delivery (CI/CD) platform."
In the assignment, the (py)test must first pass, then the site will be deployed.

- **GITHUB_WORKSPACE**

GITHUB_WORKSPACE is an Ubuntu environment. Via a yml file in the YAML programming language, instructions are given to install Python and the specified software in requirements.txt with every push. It is then instructed to run the (py)test and, if successful, to deploy the site on Digital Ocean. At the end of the process, the environment "disappears" again. With a next push, the process will start again

## Three problems I encountered

### Gunicorn

I had the farm site with the file farm.service still running on Gunicorn. That's why the command: systemctl enable --now cd didn't work.
Solution:

```cmd
$pkill gunicorn
```

### Github repository in droplet

I didn't realize at first that the directory in the droplet also has to be a git directory. Solution:

- $ git init
- $ git clone

### Venv

I had a venv module on my computer. I found out it contains quite a lot of data.
Solution:

- .gitignore
- Install the venv directly on the VPS if you wish, so not via a push.

## PHP on VPS for my future job

I have a job as a back-end developer! I had to make an assignment for my application. This was in PHP. It was quite a challenge to run both a Flask and a PHP site on the same VPS. But I did it! If you like you can take a look.

[link PHP](http://146.190.28.250:81/)

- **link droplet assignment:**

[link assignment](http://146.190.28.250)
