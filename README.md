# **Welcome to Angelina Loh's profile**

My name is **Angelina Loh**, an upcoming Sophomore enrolled in high school as of summer 2019. This website is a compliation of code I have written in Code Hobbits Ethical Hacking class. This website features a variety of projects done over the course of a week, including but not limited to Morse code translator, Caesar code translator, and web page pranks. I took this class to further my programming skills and have a basic understanding of hacking. This profile is a demonstration of the journey along the way of such milestones.

You can use the [editor on GitHub](https://github.com/AngelinaLoh/profile/edit/master/README.md) to maintain and preview the content for your website in Markdown files.

Whenever you commit to this repository, GitHub Pages will run [Jekyll](https://jekyllrb.com/) to rebuild the pages in your site, from the content in your Markdown files.

## **List of Projects**
- Terminal Commands
- [Morse Code Translator](shell.md)
- Python Hacks
- Web Pranks - Check them out [here](https://prankz.netlify.com/)

## **Applications Used:**
- Pycharm https://www.jetbrains.com/pycharm/download/#section=mac
- Atom https://atom.io/
- MacOS Terminal
- GitHub https://desktop.github.com/

## **A Journal of the Journey**
### _July 29, 2019 Day 1_
  As I walked into the expansive, empty building, I wondered about the 8 hours ahead of me. I struggled to keep my eyes awake as I walked into the room and met my instructor, Mr. Blu. Once everyone arrived, we were given kits with gadgets and other materials in them. We were instructed to take the picks and transparent lock out of our boxes. Mr. Blu guided us as we replayed a video on how to pick open a lock. I was frustrated but I kept at it until the lock finally clicked open. “Again,” said Mr. Blu. With a new determination, I locked it again and started picking at it once more.

  Afterwards, Mr. Blu informed us about the ethics of hacking and internet security. We read over a pledge of honor and agreed to follow it. Then, it all began with installing Virtual Box and Kali Linux. We went through the steps meticulously, yet our downloads of Kali Linux kept failing. Eventually, we figured out the problem was that not enough memory was dedicated to the download. I changed the ram limit from 8 GB to 16, and the download was successful but it lagged out my computer to the point in which I had to restart my entire MacBook Air.

  After lunch had ended, Mr. Blu instructed us to open up our terminal. There, he gave us our first missions as “hackers.” With no help or guidance from Mr. Blu, we were to gain access of a foreign computer using only the IP address, port, username, and password. What he asked us seemed impossible at first. After a few tips here and there and painful loads of google searching, we finally learned to use the ssh username@ip.address command. We had thought that challenge was difficult enough, but then Mr. Blu asked us to create a “back door.” What does that even mean? Brainstorm after brainstorm, Mr. Blue finally revealed that we must “think like thieves and behave like FBI agents”, and it meant adding a new user with admin perms to the victim’s computer. I understood what to do now…. But now the new question stands in my way: how? I kept hopelessly googling terms until Mr. Blu revealed that “root” is the god of the system and to add new users, we must first enter the root. From there, hacking in was easy. I first went into root and then used the command sudo to add a new user and password. Then, I logged out of root and logged in as my new administrative account. Our final challenge of the day was to access a file called GreenLantern. From my previous terminal experience, I knew to use cd and ls. I quickly googled information on how to change directories and access files. First, I checked my current location using the pwd command. Now knowing that I was in my own directory, I went to the root using cd /. From there, I did ls and then used cd home. I went into users and did ls to see all users on the computer. Then I went into the victim’s home directory using cd zork. I then did ls and cat to view the GreenLantern file, which, to my surprise, turned out as bait.

  I felt so exhausted at the end of the day when Mr. Blu asked us questions and reviewed what we learned today. In these 8 hours, I felt I have accomplished so much and have begun my hacker profile.

### _July 30, 2019 Day 2_
  I felt so exhausted as I walked back into the room for a second day of ethical hacking. Without any warmups, we were prompted to find a hidden message in zork’s account. By luck, I came across a command that showed all hidden files and directories. I used it and we were able to skip a step in Mr. Blu’s challenge. However, this backfired as we were now confused on what to do. We all struggled with the next steps until time was up. When Mr. Blu explained the solution step by step, we came to a greater understanding of terminal commands, files, directories, and zip files.

  After we had attempted to crack Mr. Blu’s challenge, we were to create our own “Capture the Flag” game. We had to hide a file of value and create a security system for it, and then try and hack into each other’s programs. I worked hard to stall for time using random fake files. My grand plan was to add images that would be clues to the passwords to certain files hidden all around the terminal. Then, you would have to find the file that instructed to change users and provided the password. From there, as a guest, you would have to login to the new user and search through the directories and unzip the zip file to win. However, when we began, I realized how irresponsible I was when starting as I had forgotten my password and not logged in anywhere. Therefore, no one was able to even attempt mine. In addition, I realized there were many flaws within my system and improvement to be made.

  Mr. Blu then gave us a short presentation on social engineering, which uses social skills instead of coding to hack people. We sat there bewildered as he then moved onto the basics of Python. We finished the final hours of the day by writing a program that would encrypt and decrypt morse code in Python. I figured out how to encrypt a message easily using a dictionary. However, I got stuck on decrypting a morse code message since I did not know how to obtain a key from a value in a dictionary. I thought I was familiar with the basics of Python, but as my progress from today has shown, I have mountains yet to conquer.

### _July 31, 2019 Day 3_
  I was excited about the Python challenges ahead of me for the day. We started the day off from where we left off yesterday, the morse code encryptor and decryptor. Mr. Blu gave us a few minutes to ponder and then proceeded to pull up his solution. He explained in depth each line of the code and informed us to take a single character of the morse code and follow it throughout the program to understand how the decryptor worked.

  After finally understanding it, Mr. Blu then showed us a video on Khan Academy about the Caesar Code. The Caesar Code is a code used by Julius Caesar to transfer secret messages in warfare. Each letter in the code is shifted a certain number in the index of the alphabet. Mr. Blu instructed us to code an encryptor and decryptor of the Caesar code in Python. I started thinking about the problem out logically step by step. For the encryptor, I used a for loop and added the shift factor with the index of each letter to print out an encrypted message. For the decryptor, I did the reverse and used a nested for loop that ran 26 times and subtracted i from the index of each letter. I thought I had completed the challenge, but then Mr. Blu challenged me by trying to break my code and finding flaws in my code. For instance, I had to modify my code in order to support inputs that were out of index range and had spaces. It was frustrating solving the errors but it was worth the satisfaction of success at the end.

  Since I was ahead of others, I was given the next challenge: to use pafy, a package on Python, to legally extract mp3 files from YouTube videos. I felt this task was tedious as I had to struggle to install so many packages and run into technical errors. I downloaded the YouTube video as an mp4 and was able to extract audio file as a webm. I then got stuck struggling to convert the webm file to mp3. I worked with Mr. Blu with it to try various solutions. The end of the day was approaching and with our energy diminished, we agreed to continue working out the problem tomorrow. Satisfied with what I did today, I closed my laptop and headed out, ready for whatever awaited me tomorrow.

### _August 1, 2019 Day 4_
  I stayed up late the night before finishing an art piece, so when I came into class today, I felt as if I would not be able to survive the long 8 hours ahead of me. We started the day off back in Python to try and document all keystrokes in a text file. Unfortunately, the MacOS detected what we were attempting to do and blocked it.

  We then started off anew by downloading an application called Atom to create web pages. Mr. Blu wanted this to be an entertaining experience for all of us, so he wanted us to create pranks using HTML, Java Script, and cascading style sheets. He first used analogies to explain each component of a web page. There is HTML for structure, CSS for style, and Java Script for interaction. He showed us each step in detail to how to make the basics of an html file. For instance, he taught us to code buttons, background colors, images, and moving buttons. After we learned the bare basics, we were ready to take on our first challenge. Based on what we learned, we were now to create our very own prank. I made a very simple page that looked like a free boba advertisement but pressing the buttons would prompt the program to ask for a credit card number. Our class shared our entries, and Mr. Blu then proceeded to guide us through another web page, this time with more in-depth logic-based code. Through this code, I learned about for loops, functions, and arrays in JavaScript. Mr. Blu gave us the final challenge of the day: making a prank involving sounds and images. Mr. Blu said we had to depend on only ourselves without his guidance. Throughout the entire day, I kept coding in JavaScript and HTML like Python, which resulted in frustration. However, looking back now, the fact that I was able to learn three languages in a day and overcome that frustration makes it worth all the effort and time I spent.

### Markdown

Markdown is a lightweight and easy-to-use syntax for styling your writing. It includes conventions for

```markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```
