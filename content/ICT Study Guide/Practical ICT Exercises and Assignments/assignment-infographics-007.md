---
title: Assignment - Infographics - 007
slug: assignment-infographics-007
weight: 7
description: Learn to create visually engaging infographics with these practical ICT assignments designed to enhance creativity, critical thinking, and digital communication skills. Perfect for mastering infographic tools and presenting complex ideas effectively.
---

{{< callout type="info" >}}
These instructions serve as general guidelines. Adapt them as needed to suit the specific requirements of the task or creative vision. Avoid following them rigidly without considering the context.
{{< /callout >}}


A Student's Daily Routine

## Objective

Transform the provided data into a visually engaging and informative infographic.

## Instructions

1. **Review the Data:** Carefully analyze the information given below. Understand its structure and how the various elements relate to each other.
2. **Select a Tool:** Choose a digital tool that suits your design needs. Popular options include [Draw.io](https://app.diagrams.net/) and [Canva](https://www.canva.com/), but feel free to use any platform you are comfortable with.
3. **Design Your Infographics:** Based on the data, your infographic should take the form of a [**Markov Process**](https://en.wikipedia.org/wiki/Markov_chain#/media/File:Markovkate_01.svg).

#### Nodes (States)

1. Home (Morning) - Represented by a small house or a bed, indicating the start of the day.
2. Commute - Illustrated by a bus or a bicycle, showing the transition from home to school.
3. Class - A book or a classroom chalkboard, representing time spent in educational activities.
4. Recess - A playground or a snack, symbolizing break time.
5. Study Hall/Library - A stack of books or a library silhouette, indicating focused study time.
6. Extracurricular Activities - A soccer ball or a musical note, representing after-school activities.
7. Commute Home - Similar to the morning commute but perhaps with a setting sun to indicate the evening.
8. Home (Evening) - A dinner plate or a family silhouette, symbolizing return to home and family time.
9. Homework Time - A desk with a lamp, indicating a time for homework and preparation for the next day.
10. Leisure/Free Time - A TV or a video game controller, representing relaxation time.
11. Bedtime - A moon or a bed, indicating the end of the day and time to sleep.

### Edges (Transitions) and Possible Weights

- Home (Morning) to Commute: 0.9 (Assuming most students will leave for school, but a small chance of staying home, e.g., due to illness)
- Commute to Class: 0.95 (High likelihood of going to class after arriving at school)
- Class to Recess: 0.8 (Most of the time, students will have a break, but sometimes classes might extend)
- Recess to Class: 0.7 (Returning to class, but there might be special events or assemblies occasionally)
- Class to Study Hall/Library: 0.6 (Depends on the student's schedule; some might have more classes, others might have study periods)
- Study Hall/Library to Extracurricular Activities: 0.5 (Students might engage in activities or go straight home)
- Extracurricular Activities to Commute Home: 0.8 (After activities, most students will commute home)
- Commute Home to Home (Evening): 0.9 (Likely to arrive home, small chance of going elsewhere)
- Home (Evening) to Homework Time: 0.7 (Assuming students will do homework, but there's a chance they might skip)
- Homework Time to Leisure/Free Time: 0.8 (After homework, students are likely to take some leisure time)
- Leisure/Free Time to Bedtime: 0.9 (High likelihood of going to bed after some relaxation)
- Bedtime to Home (Morning): 0.95 (Indicating the cycle restarts the next day)

