| # | Date IDd | Bug description | Date resolved | Resolution | Commit | Comments |
|-|-|-|-|-|-|-|
| 1 | 2026-01-20 | `python manage.py collectstatic` does not actually collect from static | 2026-01-24 | _settings.py_ ~~`STATIC_DIRS`~~ `STATICFILES_DIRS` | [main b996c51] BUGFIX python manage.py collectstatic | [Ceri](https://github.com/Ceri-Jane) is a saint <3 |
| 2 | 2026-01-24 | _script.js_ `loVerbose()` does not seem to be targetting `.q-lo` | 2026-01-25 | `loVerbose()` was targetting `.q-lo`, needed to use `=` instead of `==` in `if` statement | [main 7b310e0] BUGFIX loVerbose() ||
| 3 | 2026-01-24 | _style.css_ `@font-face{UCLSans}` isn't functioning | 2026-01-25 | 1. `url()` path needed to be relative to _style.css_ \| 2. Run `python manage.py collectstatic` | [main 37b696c] BUGFIX @font-face{UCLSans} ||
| 4 | 2026-01-28 | __404__ Reverse for 'questions' not found. 'questions' is not a valid view function or pattern name. | 2026-01-29 | _app / urls.py_ `path(name)` needed to match _base.html_ url reference | [main 7801f0c] BUGFIX Reverse for 'questions' not found. |
| 5 | 2026-01-30 | __404__ Deployed page doesn't load