# CSI 480 Problem Set 6

In this problem set, you will use gradient descent and a multivariate linear regression model to predict the weight of a fish based on its dimensions.

The data set is in the file `Fish.csv`. The first column is the fish species, the second is the weight, the third is a length measure, the fourth is a different length measure, the fifth is yet another length measure, the sixth is the height, and the seventh is the width. This is a real data set. Here is a link to the source of the data set: [https://www.kaggle.com/aungpyaeap/fish-market](https://www.kaggle.com/aungpyaeap/fish-market). It is based on public domain data that has been cleaned up a bit and remixed under the GPL license.

The dimensions are in centimeters. The weight is in grams.

You are being provided code to load the data set, run gradient descent to form a linear regression model, and the plost the cost function over the iterations that gradient descent runs. You will need to write a little bit of additional code. You will need to understand the code that is provided to you.

Note that you will need to install `matplotlib` to run this code. You can do this by running the following command in your terminal:

```bash
pip3 install matplotlib
```

Depending on your personal computer's setup, it may be `pip` instead of `pip3`.

## Hints

- Make sure you understand all of the fundamental statistics before you start (z-scores, linear regression, r-squared, etc.).
- Carefully read through the provided code. It is not very long, and it is very important that you understand it.
- You don't need to write a lot of code, just the right code. Do not rely on GitHub Copilot without understanding everything that it is writing for you. It does not always write the correct code.

## Rules

1. You must complete this problem set individually. You can discuss it with a friend, but you should not be copying their code or looking at their code despite the final result of this being a quiz on Canvas.
2. You must complete this assignment using the provided statistical functions. Do not use a third party Python library, or Excel, or R. Keep in mind the accuracy of our statistical functions may differ from Excel or R and the Canvas quiz answers depend on the accuracy of our statistical functions.

## Setup

1. Create your own **private** repository from this repo by hitting the "Use this template" button at the top of the page
2. Add me (@davecom) as a collaborator on your **private** repository.
3. Install matplotlib (`pip3 install matplotlib`).
3. Complete the assignment quiz on Canvas.

## Grading

This particular problem set is based on a quiz on Canvas that you can only take one time. Each question is worth 1 point. You have unlimited time on the quiz until the deadline, but you can only submit it once.

## Note on Repository Access

This repository should stay private. If you make it public, you are possibly providing your solution to other students taking the class. Generally the problem sets in this class are not great portfolio projects because they are too small, or contain a significant portion of code that is not your own and therefore do not demonstrate your skill. Please keep your repository private so other students can't use your solution.
