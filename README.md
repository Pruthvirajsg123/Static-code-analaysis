# Static-code-analaysis

1.Which issues were the easiest to fix, and which were the hardest? Why?

•	Easiest: Minor formatting issues like inconsistent indentation, unused imports, and variable naming conventions were easiest to fix since they only required simple code clean-up or adherence to style guidelines.
•	Hardest: Logical or potential runtime issues flagged by the static analysis tool (such as uninitialized variables or null pointer risks) were harder to fix because they required understanding the code’s flow and modifying logic carefully to avoid introducing new bugs.




2. Did the static analysis tools report any false positives? If so, describe one example.

Yes, a few false positives were reported.
For example, the tool flagged a variable as "unused," even though it was referenced inside a conditional block that only executes under certain runtime configurations. This indicates that static analysis sometimes lacks full context about dynamic behavior.



3. How would you integrate static analysis tools into your actual software development workflow? Consider continuous integration (CI) or local development practices

I would integrate static analysis tools into the CI/CD pipeline so that each commit is automatically analyzed before merging.
Additionally, I would run the tools locally before pushing changes to catch issues early.
 This ensures consistent code quality checks and reduces the chances of introducing style or logic errors into the main branch.

4. What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?
  After applying the suggested fixes, I observed cleaner, more consistent, and readable code.
Unused variables and redundant statements were removed, improving maintainability.
  The tool also helped identify potential runtime issues, making the codebase more robust and reliable.
 Overall, the project became easier to navigate and less prone to hidden bugs.


