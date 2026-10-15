# WorkExperience26
Work experience for October 12-16th October 2026.

## Content

* [Topics](#topics)
* [Requirements](#requirements)
* [Timetable](#timetable)
* [Resources](#resources)

## Topics

Stuff you will learn about:

* Using the command line:
  * `ls`, `pwd`, `cd`, `rm`, `mkdir`, `rmdir`, `which`
  * On Windows can get `bash` using `git bash` part of the `git` install or can install the Windows Subsytem for Linux in the Powershell:
    ```powershell
    # To see what distributions are available
    wsl.exe --list --online
    # Can install the Ubuntu distribution
    wsl.exe -- install Ubuntu
    # Will ask you to create an account - set a password you will not 
    # forget. Can launch from the command line using:
    # wsl.exe -d Ubuntu
    # or in a powershell window you can just type bash
    ```
  
  * Software Carpentry [The Unix Shell](https://swcarpentry.github.io/shell-novice/)
* Using an editor:
  * `vi`, `nano`, [visual studio code](https://code.visualstudio.com/download)
* Markdown ([cheat sheet](https://www.markdownguide.org/cheat-sheet/))
* Git and GitHub
  * local git repo, set credentials (`git config --global user/email`), create repo in a sub directory (`git init`), status (`git status`), adding (`git add`), committing (`git commit`) 
  * remote repo, pulling (`git pull`), pushing (`git push`), hurdles, resolving conflicts
  * forked repositories
  * Software Carpentry [Version Control with Git](https://swcarpentry.github.io/git-novice/)
* Python
  * Virtual environments:
    ```shell
    python -m venv .myenv
    . .myenv/bin/activate
    ```
  * Jupyter notebooks
    '''bash
     py -3.13 -m venv .jupyterenv
     '''
  * AI assists
  * Software Carpentry [Programming with Python](https://swcarpentry.github.io/python-novice-inflammation/) or [Plotting and Programming with Python](https://swcarpentry.github.io/python-novice-gapminder/)

## Requirements

In order to participate you will need to bring a Windows or Mac laptop in which you have the rights to install software. If you do not have access to such a machine please get in touch and I will try to source a laptop for the duration of the work experience.

Software that will be needed ( you do NOT have to preinstall these pieces of software - we can do that as needed):

1. [git](https://git-scm.com/install)
2. bash

## Timetable

Assume a one hour break for lunch.
ACF tour pencilled in for Tuesday at the moment.

|       | Morning (9:30 - 12:00) | Afternoon (13:00 - 15:30) |
| ----- | ---------------------- | ------------------------- |
| Day 1 | Induction              |                           |
| Day 2 | Trip to the ACF        |                           |
| Day 3 |                        |                           |
| Day 4 |                        |                           |
| Day 5 |                        |                           |

## Induction

* Welcome to EPCC 
* Sort out:
  * Get Visitor passes for entry into the Bayes
  * Network laptops

## Resources

* BBC World Service [Inside a supercomputer: A Tech Life special](https://www.bbc.co.uk/sounds/play/w3ct8jyj) (26 mins), actually talks about the supercomputer at Edinburgh. Available on 07/10/26.
