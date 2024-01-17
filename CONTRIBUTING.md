tl;dr We want to write awesome code that we all are proud of. Perfection is not the goal, but we want good code.

## Code Quality

### Understand every part of the code you check in
1. If you don't understand, clearly call this out in a PR comment. Someone who understands the tech must review it.
2. If you can't explain the logic to someone else so that they understand, then keep working to understand.

### There shouldn't be patches on patches. If there is doubt about how something works, go back and understand it, then fix it. 
1. If it is too difficult, get help from someone else

### When copying and pasting...
1. Ask "could I instead make this a reusable component or method or CSS class?"
2. Make sure what you are copying was done right in the first place. Don't proliferate bad code.
3. Make sure every part of what you copy is needed

### When you find a bug
1. Fix it if it very small or fits into your PR
2. Log bugs on the backlog when you find them. Because later never happens.
3. Option to submit a small PR for the bug separately with a story. This can be very quick.

### Speed is not the most important thing
1. If you feel that something is taking too long, ask for guidance. 

### When writing tests
1. Tests should be added for almost every pull request
2. The [Given When Then](https://martinfowler.com/bliki/GivenWhenThen.html) test naming convention is encouraged as it helps readers of the code quickly know what the test is testing.
2. Using [Arrange Act Assert](https://automationpanda.com/2020/07/07/arrange-act-assert-a-pattern-for-writing-good-tests/) comments to organize your tests is encouraged, especially when they grow larger.

## PR Quality

### Commit and make PRs with intentionality
1. Reread the code before committing like you would an essay.
2. Before finalizing the PR, review it yourself. The entire Git Diff. It is faster for you to do this than for someone else.
    - Make sure you are not committing things that are not in the scope of your PR.
3. For UI changes, provide screenshot(s) or a video of the code working with the console open is super helpful and fast.
    - https://www.screentogif.com/ (it saves MP4s too!)
4. Only solves one problem/work item. Smaller PRs
5. No build error or warnings
6. Code runs correctly (don't trust that last innocuous change without a rerun)
7. Formatting of all docs meets standards
   - Format on save is great!
8. Code is readable, appropriate white space and comments.
9. No console errors
10. No merge conflicts with main

### Branch names
1. [github username]/[work item #]-[short description]
