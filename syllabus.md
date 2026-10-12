# Syllabus

## CSS SKL 342: Programming Issues With Object-Oriented Languages

### UW1-041, Friday 1:15pm-5:15pm

---

|  |  |
| --- | --- |
| **Instructor:** Kelvin Sung | **Office:** UW1-260-O |
| **Email:** [ksung@uw.edu](mailto:ksung@uw.edu) | **Office Hours:** Tue 4-5pm on Zoom (link and passcode on Canvas), or email for an appointment |

---

### Basic Course Information

Covers language and development/execution environment differences, including data types, control structures, arrays, and I/O; addressing and memory management issues including pointers, references, functions, and their passing conventions; object-oriented design specifics related to structured data, classes, templates, and operator overload.

CSS SKL 342 is a credit/no-credit (CR/NC) lab taught alongside the first half of CSS 342. It has no exams and no final exam.

### Course Objectives

This lab helps students who can already write small programs in Java or C# write larger programs in C++, the language of CSS 342 and 343. The ideas carry over, but the syntax differs a little and the usage differs a lot, especially in memory management and the build toolchain. The labs teach the C++ details your CSS 342 assignments need, so the CSS 342 lectures can stay on data structures. The pace is fast: each week is part lecture, part hands-on lab.

By the end of the course you should be able to:

1. Build, run, and debug C++ programs on Linux with g++, make, gdb, and VS Code.
2. Explain C++ types, conversions, and parameter passing (by value, by reference, by const reference).
3. Use pointers, arrays, and dynamic memory (`new`/`delete`) correctly, and find memory errors with valgrind.
4. Write classes with constructors, destructors, operator overloads, and correct copy behavior (the rule of three).
5. Write and use function and class templates, and handle errors with exceptions.
6. Use the C++ Standard Library: `string`, `vector`, `list`, `map`, iterators, file streams, and algorithms.

### Suggested Reading and References

No textbook is required. The lab pages on this site are the main reading.

- **C++ reference sites:** keep a couple of favorites open, for example
  - For the language and the standard library: <https://en.cppreference.com/w/>
  - For the standard library: <https://cplusplus.com/reference/>
- **C++ reference book:**
  - Bjarne Stroustrup, *The C++ Programming Language*, 4th edition, Addison-Wesley, 2013. The canonical reference.
- **Working on Unix/Linux:**
  - Harley Hahn, *Harley Hahn's Student Guide to UNIX*, 2nd edition, McGraw-Hill, 1996. If you are new to Unix or Linux and want to learn more, get a book like this.
- **The Standard Library and good C++ practice:**
  - Nicolai M. Josuttis, *The C++ Standard Library*, 2nd edition, Addison-Wesley, 2012. A complete reference with examples; not a tutorial.
  - Scott Meyers, *Effective STL: 50 Specific Ways to Improve Your Use of the Standard Template Library*, Addison-Wesley, 2001.
  - Scott Meyers, *Effective C++: 55 Specific Ways to Improve Your Programs and Designs*, 3rd edition, Addison-Wesley, 2005. The book you must read to become a C++ programmer.
  - Scott Meyers, *Effective Modern C++: 42 Specific Ways to Improve Your Use of C++11 and C++14*, O'Reilly, 2014.

### Course Schedule

Before the first lab, complete the [Pre-Lab](Pre-Lab/index.html) to set up VS Code, Docker, and the course Linux container.

| **Date** | **Topics** |
| --- | --- |
| Jan 9 | **Lab 1:** Toolchain and C++ basics: your Linux environment, how C++ programs are built, types and conversions, references and parameter passing. |
| Jan 16 | **Lab 2:** Debugging, classes, and operators: gdb and the VS Code debugger, classes, object lifetime, operator overloading. |
| Jan 23 | **Lab 3:** Pointers, arrays, and dynamic memory: pointers, arrays, `new`/`delete` and valgrind, linked nodes. |
| Jan 30 | **Lab 4:** Templates and classes that own memory: templates, the rule of three, copying a linked chain, exceptions and RAII. |
| Feb 6 | **Lab 5:** Iterators and the Standard Library: `vector`, `string`, and files; iterators; `list` and `map`; algorithms and lambdas. |

There is no final exam. For the last day to drop or withdraw, see the Registrar's [Drop or Withdraw](https://registrar.washington.edu/drop-withdraw/) page and the quarter's academic calendar.

### Grading

This course is graded credit/no-credit (CR/NC); see the UW [grading system](https://www.washington.edu/students/gencat/front/Grading_Sys.html). There are no exams. Learning C++ takes time spent understanding and practicing, so plan for that time each week.

Each lab has these parts:

- **Section quizzes (in lab, on Canvas):** each lab has four parts. Each part ends with a short (about 10-minute) Canvas quiz on that part's exercise.
- **Lab code submission (on Canvas):** at the end of the lab, submit one zip of your LabN folder with your exercise code. The instructor reviews your programs during and after the lab.
- **Post-lab quizzes (on Canvas):** short open-book quizzes on each lab's topics.

To earn credit (CR), you must complete each lab's work and receive a *check* for it on Canvas. Due dates and the requirements for a check are posted on Canvas.

**Attendance:** the labs are hands-on, so plan to attend and take part. If you must miss a lab, email me as soon as you can. You do not need a doctor's note: per UW policy, I cannot require or accept medical documentation for an absence.

**Late work:** late work will not be accepted. Please do contact me about any personal or unexpected challenges. I am a reasonable person, but in general, running out of time due to lack of planning is not an acceptable excuse.

**Incompletes:** if circumstances arise that prevent you from completing the course by the end of the quarter, please reach out to me. The UW does not require me to grant a student's request for an Incomplete, but requests submitted in the last 3 weeks of the quarter by students who have done satisfactory work up to that point may be considered. See the Registrar's [Incomplete Grades](https://registrar.washington.edu/grades/incomplete-grade-policy/) page.

### Technology Use

Bring a laptop to every lab: the labs are hands-on, and you will build and run code in the course Linux container (set up in the [Pre-Lab](Pre-Lab/index.html)). If you do not have a laptop that can run Docker, contact me immediately at [ksung@uw.edu](mailto:ksung@uw.edu).

### Using On-line Tools (Including AI and Google)

AI tools such as ChatGPT, Claude, and GitHub Copilot are becoming as common in programming as spelling and grammar checkers are in writing. You may use generative AI tools and on-line resources in this course, with two cautions and a few rules.

The cautions: the point of this lab is for *you* to be able to write and debug C++ in your CSS 342 assignments. If a tool writes the code and you cannot explain it, you have not learned it. Also, AI tools can be confidently wrong, especially about memory and undefined behavior; test what they give you.

The rules:

- Cite the AI tool inline and in your references list, using the citation format for a website URL.
- Briefly summarize the prompts you entered into the AI tool.
- For code output, include a comment at the top of the corresponding file saying that some of the code was generated by AI.

Example of a citation in a references list:

- OpenAI. (n.d.). "Why does my C++ program crash when I delete a pointer twice?" ChatGPT. <https://chatgpt.com>

Example of a comment at the top of a code file:

- `// AI usage: about 20 lines of the code in this file were generated by GitHub Copilot`

Section quizzes and post-lab quizzes are open book, but answer them yourself: do not share answers with other students. If you are unsure whether a use of a tool is allowed, ask me.

### Academic Integrity

The University takes academic integrity very seriously. Behaving with integrity is part of our responsibility to our shared learning community. If you're uncertain about whether something is academic misconduct, ask me. I am willing to discuss questions you might have.

In this lab, you may work on the exercises in small groups, and each group member may submit a copy of the group's code. Put the names of everyone in the group in a comment at the top of each file. Quizzes are individual work.

Acts of academic misconduct may include but are not limited to:

- Cheating (sharing quiz answers, taking a quiz for someone else, or previewing a quiz)
- Plagiarism (representing the work of others, including AI-generated code, as your own without giving appropriate credit)
- Unauthorized collaboration (working together on work that must be individual, such as the quizzes)

The University's policy on academic misconduct is part of the Student Conduct Code ([WAC 478-121](https://app.leg.wa.gov/WAC/default.aspx?cite=478-121)); see [Student Governance Policy, Chapter 209, Section 7.C](https://policy.uw.edu/directory/sgp/sgp-209-student-conduct-policy-for-academic-misconduct-and-behavioral-misconduct/) and [Community Standards & Student Conduct: Academic Misconduct](https://www.washington.edu/cssc/academic-misconduct/). Concerns about these or other behaviors prohibited by the Student Conduct Code will be referred for investigation and adjudication by the UW Bothell [Office of Student Conduct](https://www.uwb.edu/student-affairs/studentconduct). Students found to have engaged in academic misconduct may not receive a check for that work and may be reported to the Office of Student Conduct.

### Access and Accommodations

Your experience in this class is important to me. It is the policy and practice of the University of Washington to create inclusive and accessible learning environments consistent with federal and state law. If you have already established accommodations with Disability Resources for Students (DRS), please activate your accommodations via [myDRS](https://denali.accessiblelearning.com/Washington/) so we can discuss how they will be implemented in this course.

If you have not yet established services through DRS but have a temporary health condition or permanent disability that requires accommodations (conditions include but are not limited to mental health, learning, vision, hearing, physical or health impacts), contact DRS directly to set up an Access Plan. DRS facilitates the interactive process that establishes reasonable accommodations. Contact DRS at <https://www.washington.edu/drs/>. The UW Bothell DRS office is at 425-352-5426 or [uwbdrs@uw.edu](mailto:uwbdrs@uw.edu).

### Religious Accommodations

Washington state law requires that UW develop a policy for accommodation of student absences or significant hardship due to reasons of faith or conscience, or for organized religious activities. The UW's policy, including more information about how to request an accommodation, is available at [Religious Accommodations Policy](https://registrar.washington.edu/staff-faculty/religious-accommodations-policy/). Accommodations must be requested within the first two weeks of this course using the [Religious Accommodations Request form](https://registrar.washington.edu/students/religious-accommodations-request/).

### Pregnancy and Related Conditions

If you are pregnant or have a related condition (including childbirth, miscarriage, abortion, or lactation), you may be entitled to modifications and accommodations so you can keep taking part in this course. See the UW's [Pregnancy & Related Conditions](https://www.washington.edu/civilrights/seeking-support/pregnancy-and-related-conditions/) page, and feel free to talk with me.

### Discrimination, Harassment, and Sexual Misconduct

University of Washington policy, in concert with federal and state laws, provides the right to participate in University programs and activities free from sexual misconduct or discrimination on the basis of protected characteristics, including but not limited to disability, race, sex and others. Sexual misconduct includes, but is not limited to, sexual assault, relationship violence, sexual harassment, and stalking.

Students who believe they have experienced [civil rights discrimination, harassment](https://www.washington.edu/civilrights/seeking-support/civil-rights-discrimination/), or [sexual misconduct](https://www.washington.edu/civilrights/seeking-support/sexual-misconduct/) are encouraged to contact a Civil Rights Compliance Office Case Manager by making a [Civil Rights & Title IX Report](https://www.washington.edu/civilrights/making-a-report/make-a-report/). Case managers can provide guidance on available supportive measures and resolution options. [Confidential Advocates](https://www.washington.edu/sexualassault/support/advocacy/) offer confidential support for students impacted by sexual assault, relationship violence, or stalking.

Most UW employees, including me, who become aware of discrimination, harassment, or sexual misconduct involving students are required to share that information with the Civil Rights Compliance Office. They may withhold the impacted student's name if requested.

### For Our Veterans

If you are a student who has served in our nation's military forces, *thank you* for your service. I hope that you feel comfortable enough to confidentially self-identify to me so I can help you make a successful transition from the military to higher education.

### Problems

If you have problems with anything in the course, please come and see me during office hours, make an appointment to see me at some other time, or send me an email. I want you to succeed in this course and, by extension, in CSS 342.
