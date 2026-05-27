## Pull Request Summary

<!-- Provide a concise summary of the changes in this PR. -->

---

## Related Issue

<!-- Link the issue(s) this PR addresses. Use "Closes #N" to auto-close on merge. -->

Closes #

---

## Type of Change

<!-- Check the type(s) that apply to this PR. -->

- [ ] Bug fix (non-breaking change that fixes an issue)
- [ ] New feature (non-breaking change that adds functionality)
- [ ] Breaking change (fix or feature that causes existing functionality to change)
- [ ] Documentation update
- [ ] Database change (schema, view, trigger, query)
- [ ] Security improvement
- [ ] UI / styling change
- [ ] Refactoring (no functional change)
- [ ] Chore / maintenance

---

## What Changed

<!-- Describe the specific changes made in this PR. Be precise. -->

### Files Modified
<!-- List the key files changed and what was done to each. -->

- `app.py` — 
- `schema.sql` — 
- `templates/` — 

---

## Database Changes

<!-- If this PR modifies the database schema, queries, views, or triggers, describe them here. -->

- [ ] This PR includes database changes

<!-- If yes, describe: -->
- **Tables added/modified:**
- **Views added/modified:**
- **Triggers added/modified:**
- **`schema.sql` updated:** Yes / No

---

## Testing

<!-- Describe how you tested your changes. -->

- [ ] Tested locally with the development MySQL instance
- [ ] Verified admin workflow
- [ ] Verified player workflow
- [ ] Verified database changes with sample data
- [ ] Tested edge cases (empty data, invalid input, etc.)
- [ ] No regressions observed in existing functionality

### Test Scenarios Covered

| Scenario | Result |
|---|---|
| | ✅ Pass / ❌ Fail |

---

## Screenshots (if applicable)

<!-- For UI changes, before/after screenshots are highly encouraged. -->

---

## ✅ Checklist

<!-- Complete this checklist before requesting review. -->

- [ ] My branch is up to date with `main`
- [ ] My code follows the project's coding standards (PEP 8, parameterised SQL)
- [ ] I have not committed any credentials, passwords, or secret keys
- [ ] All new routes use the appropriate authentication decorators
- [ ] Database connections and cursors are properly closed
- [ ] I have updated `schema.sql` if the database was modified
- [ ] The PR title is clear and follows the `<type>: <description>` format
- [ ] I have linked the relevant issue in this PR

---

## Additional Notes

<!-- Anything else the reviewer should know about this PR. -->
