# project_euler
Solutions (and/or attempted solutions) to Project Euler problems - 2023
## Introduction
I was introduced to Project Euler back in 2018 or 2019, when I was working to transition from a research career in academia to a Data Science career in industry. I had worked in MATLAB for over 10 years, and figured it was as good a project as any to start working on in Python. I briefly re-visit at the height of COVID, and I think made it up to problem 12 or so.

It's 2023, and after a hiatus in personal projects, another shot at Project Euler seems feels like a great way to get back into the habit. Since my last work on Euler Chat-GPT has arrived, and solutions to these problems (or some plausible-but-incorrect approxumation of one) are available at with a couple of keystrokes. I will not use Chat-GPT or any other LLM or AI-assistant to generate or inspire any code found here, not least because it would ruin the fun. If you're a hiring manager or recruiter reading this, I guess you'll have to take my word for it!

As a physicist by training, and an applied (rather than theoretical) physicist in my academic career, I did not cover the data structures and algorithms content found in mathematics and computer science courses, or more heavily computational physics, etc. As such I absolutely will be researching problems where necessary to identify efficient algorithms to find solutions. My intention is to keep notes on each problem in this document, and try to be diligent in citing external sources when they are used.
## Notes
### Problem 1
Easy problem, I don't think I suspect my previous solutions were less elegant.
### Problem 2
This was a fun problem coming from a non-CS background. I confused my recollection that some later problem about finding primes requires an efficient algorithm with the problem of generating Fibonacci numbers at the relatively small scale required for this problem. Instead of simply generating the sequence by addition, as would probably have been the most efficient course of action, I searched for fast Fibonacci algorithms.

I came across [this webpage](https://www.nayuki.io/page/fast-fibonacci-algorithms#:~:text=Definition%3A%20The%20Fibonacci%20sequence%20is,of%20algorithms%20to%20do%20so.) and implemented a simplified version of the matrix exponentiation algorithm. The full algorithm is particualrly efficient when calculating some Nth number in the Fibonacci sequence without iteratively generating the entire sequence, and requires the use of [exponention by squaring](https://en.wikipedia.org/wiki/Exponentiation_by_squaring) to maintain efficiency as N becomes large.

While implementing the algorithm, I also discovered the python `@` operator, which can be used to generate the matrix product of two numpy arrays.
