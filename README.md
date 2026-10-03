# UDP5WA4CF-UN03_back_end_development

This website is built for my ~~Back End~~ Data-Centric Development milestone project 3 with [Code Institute](https://codeinstitute.net) via [University Centre Peterborough](https://www.ucp.ac.uk/).


## Justification

Tracking of success rate for PiL course tests; possibility of teaching improvements via targetted understanding of strengths/weaknesses.


---

Visit the homepage [here](https://un03-back-end-development-743a39d8016b.herokuapp.com/).

---


### Reflections

If an infinite `while` loop is created by accident, close Visual Studio Code and repoen it; something about being caught in an infitine loop breaks the ability to run the fixed code, despite refreshing the terminal.

`pip freeze > requirements.txt` and `pip install -r requirements.txt` is awesome functionality.

If something isn't working but the code _seems_ fine, remember to check DevTools for any JavaScript errors (or other errors)! This probably seems trivial, but today I spent most of an hour thinking everything was fine, but something was broken and couldn't see what; then I thought to check DevTools and it told me that the JavaScript wasn't being read... Which, of course, immediately led me to the problem. Small win, but good foundation.

`assert` is a cool error checking tool.

Although the Heroku build logs are daunting, they can be helpful.


## Contents

1. [Introduction](https://github.com/stillprocrastinating/UDP5WA4CF-UN03_back_end_development/tree/main#udp5wa4cf-un03_back_end_development)  
    1.1. [Justification](https://github.com/stillprocrastinating/UDP5WA4CF-UN03_back_end_development/tree/main#justification)  
    1.2. [Visit the homepage](https://github.com/stillprocrastinating/UDP5WA4CF-UN03_back_end_development/tree/main#visit-the-homepage-here)  
    1.3. [Reflections](https://github.com/stillprocrastinating/UDP5WA4CF-UN03_back_end_development/tree/main#reflections)
1. [Design](https://github.com/stillprocrastinating/UDP5WA4CF-UN03_back_end_development/tree/main#design)  
    2.1. [User Stories](https://github.com/stillprocrastinating/UDP5WA4CF-UN03_back_end_development/tree/main#user-stories)  
    2.2. [Features](https://github.com/stillprocrastinating/UDP5WA4CF-UN03_back_end_development/tree/main#features)  
    2.3. [ERDs](https://github.com/stillprocrastinating/UDP5WA4CF-UN03_back_end_development/tree/main#entity-relationship-diagrams)  
1. [Credits](https://github.com/stillprocrastinating/UDP5WA4CF-UN03_back_end_development/tree/main#credits)  
    3.1. [Development](https://github.com/stillprocrastinating/UDP5WA4CF-UN03_back_end_development/tree/main#development)  
    3.2. [Libraries](https://github.com/stillprocrastinating/UDP5WA4CF-UN03_back_end_development/tree/main#libraries)  
    3.3. [Accessibility](https://github.com/stillprocrastinating/UDP5WA4CF-UN03_back_end_development/tree/main#accessibility)  
    3.4. [Images](https://github.com/stillprocrastinating/UDP5WA4CF-UN03_back_end_development/tree/main#images)  
    3.5. [Fonts](https://github.com/stillprocrastinating/UDP5WA4CF-UN03_back_end_development/tree/main#fonts)  

---


## Design


### User Stories

Please find a comprehensive list of user story goal progress under _0_documents_ > _README_ > _files_ > _[user_stories](https://github.com/stillprocrastinating/UDP5WA4CF-UN03_back_end_development/blob/main/0_documents/README/files/user_stories.md)_.  
TLDR as follows.

_You may click on any screenshot image to be taken to the fullscreen view (and use the browser back button to return here)._

| # | Description | Solution |
|-|-|-|
| 1 | As an admin, I want CRUD functionality for test questions. | ![solution1](https://github.com/stillprocrastinating/UDP5WA4CF-UN03_back_end_development/blob/main/0_documents/README/images/user_stories/solution1.jpeg) |
| 2 | As a tester, I want to create tests I host. | ![solution2](https://github.com/stillprocrastinating/UDP5WA4CF-UN03_back_end_development/blob/main/0_documents/README/images/user_stories/solution2.png) |
| 3 | As a tester, I want to create test answers of my students. | ![solution3](https://github.com/stillprocrastinating/UDP5WA4CF-UN03_back_end_development/blob/main/0_documents/README/images/user_stories/solution3.png) |
| 4 | As a student, I want to be able to prepare for which questions may occur on the test. | ![solution4](https://github.com/stillprocrastinating/UDP5WA4CF-UN03_back_end_development/blob/main/0_documents/README/images/user_stories/solution4.png) |
| 5 | As a tester, I want to be able to see which questions are more difficult than others. | ![solution5](https://github.com/stillprocrastinating/UDP5WA4CF-UN03_back_end_development/blob/main/0_documents/README/images/user_stories/solution5.jpeg) |
| 6 | As a tester, I want to be able to tell the difference between a question being difficult because it is difficult or because I am teaching it poorly. | ![solution6](https://github.com/stillprocrastinating/UDP5WA4CF-UN03_back_end_development/blob/main/0_documents/README/images/user_stories/solution6.jpeg) |
| 7 | As a tester, I want to be able to see which tests were more difficult than others. | ![solution7](https://github.com/stillprocrastinating/UDP5WA4CF-UN03_back_end_development/blob/main/0_documents/README/images/user_stories/solution7.jpeg) |


### Features

_You may click on any screenshot image to be taken to the fullscreen view (and use the browser back button to return here)._

| Pages | Sizes | Feature | Presentation |
|-|-|-|-|
| All | All | `<noscript>` to handle disabled JavaScript | ![noscript](https://github.com/stillprocrastinating/UDP5WA4CF-UN03_back_end_development/blob/main/0_documents/README/images/features/noscript.png) |
| question_detail.html | All | `.correct` to clearly show which answer is correct | ![correct](https://github.com/stillprocrastinating/UDP5WA4CF-UN03_back_end_development/blob/main/0_documents/README/images/features/correct.jpeg) |
| test_detail.html | All | An explanation for when a dataset is empty (and a handy-dandy button-link to the form to add data) | ![no-answers](https://github.com/stillprocrastinating/UDP5WA4CF-UN03_back_end_development/blob/main/0_documents/README/images/features/no-answers.png) |
| test_detail.html | All | `<a>` to see a quick list of the questions in that test and be able to jump to a particular question quickly _- this may not seem pertinent, but will be appreciated in later versions of the site when the number of questions per test matches reality (~30)_ | ![alq-list](https://github.com/stillprocrastinating/UDP5WA4CF-UN03_back_end_development/blob/main/0_documents/README/images/features/alq-link.png) |


### Entity relationship diagrams

Please find a comprehensive list of ERDs under _0_documents_ > _README_ > _files_ > _[erd](https://github.com/stillprocrastinating/UDP5WA4CF-UN03_back_end_development/blob/main/0_documents/README/files/erd.md)_.  
TLDR as follows.

>Question

:arrow_down:

>Test

:arrow_down:

>Answer

---


## Credits

[UCL brand resources](https://www.ucl.ac.uk/brand-and-experience/brand/brand-resources) directly influenced my colour theme, [Favicon](https://github.com/stillprocrastinating/UDP5WA4CF-UN03_back_end_development/blob/main/0_static/images/favicon/favicon.svg), and footer image [banner](https://github.com/stillprocrastinating/UDP5WA4CF-UN03_back_end_development/blob/main/0_static/images/base/ucl200_stretch_banner_3000x2280mm_original.jpg).

[rxaviers](https://gist.github.com/rxaviers)' GitHub markdown [emojis](https://gist.github.com/rxaviers/7360908).

Raghav Kovvuri, my tutor during my [Code Institute](https://codeinstitute.net) course, helped me fix a few bugs:
- [main 8675b17] replace participants & correct with @property
- [main 053aeeb] python manage.py migrate
- [main 85ca76c] restructure Answer
- [main 497787c] register Answer
- [main 220d7f8] fix url pathing


### Development

This website was developed using HTML5, CSS3, JavaScript, and Python in [Visual Studio Code](https://code.visualstudio.com); SQLTools, Python, and PostgreSQL, [Visual Studio Code](https://code.visualstudio.com) extensions were also used. The terminal and source control were used to commit and push to [GitHub](https://github.com/dashboard). The code was pulled from [GitHub](https://github.com/dashboard) into [Heroku](https://id.heroku.com), which built the site.


### Libraries

Inspiration for much of the code was modified directly from the [Code Institute](https://codeinstitute.net) "Django Blog" (repo [here](https://github.com/stillprocrastinating/UDP5WA4CF-TU_django_blog)) walkthrough project.

The edit and delete code for the Answer and Test apps was modified from [python tutorial](https://www.pythontutorial.net) [Django UpdateView](https://www.pythontutorial.net/django-tutorial/django-updateview/) page.


### Accessibility

Please find a comprehensive list of accessibility under _0_documents_ > _README_ > _files_ > _[accessibility](https://github.com/stillprocrastinating/UDP5WA4CF-UN03_back_end_development/blob/main/0_documents/README/files/accessibility.md)_.  
TLDR as follows.

| Object | Ratio | WCAG AA |
|-|-|-|
| [--color-dark on --color-white](https://webaim.org/resources/contrastchecker/?fcolor=2F1C48&bcolor=FFFFFF) | 15.21 : 1 | pass |
| [--color-dark on --color-background](https://webaim.org/resources/contrastchecker/?fcolor=2F1C48&bcolor=EFDDFF) | 11.92 : 1 | pass |
| [--color-black on --color-secondary](https://webaim.org/resources/contrastchecker/?fcolor=000000&bcolor=38D8FF) | 12.43 : 1 | pass |

| Object | Method | Description |
|-|-|-|
| `.correct` | `aria-label` | This is the correct answer |
| `.nav-item` | `aria-current` | page |
| various buttons/links | `aria-label` | descriptions such as "Submit the [test/answer] form" |


### Images

Files can be found under _0\_static_ > _images_ > _[base](https://github.com/stillprocrastinating/UDP5WA4CF-UN03_back_end_development/tree/main/0_static/images/base)_.

The original [zebrafish image](https://www.istockphoto.com/vector/zebrafish-gm479692688-68004101) was designed by [designdunja](https://www.istockphoto.com/portfolio/designdunja?mediatype=illustration) and sourced from [iStock by Getty Images](https://www.istockphoto.com). The image indicates that a subject of the PiL course tests is zebrafish. I edited the image to remove the background so that it looked more aesthetic in my header.

The [Home Office](https://www.gov.uk/guidance/research-and-testing-using-animals) and [Royal Society of Biology](https://www.rsb.org.uk) images were sourced from [DuckDuckGo images](https://duckduckgo.com/?q=duckduckgo+images&t=opera&ia=images&iax=images).

The original [UCL stretch banner](https://imagestore.ucl.ac.uk/imagestore/start/ucl-new-templates/UCL200/UCL200%20Stretch%20Banners?fc=browse&column=7&listview=overview&view=preview&fileid=1&fuid=UCL200%20Stretch%20banner%203000x2280mm_02.pdf) was sourced from [UCL Brand Resources](https://imagestore.ucl.ac.uk/imagestore/start/ucl-new-templates?fc=browse&column=7). The banner indicates that I am affiliated with University College London. I edited the image to replace the background colour with `--color-dark: #2f1c48` to match the colour of the footer.

The [REAL Rating](https://www.realgoodai.org/real-rating) 1 - Automation image was sourced from [REAL Good AI](https://www.realgoodai.org). The Reported Engagement with AI Level (REAL) rating indicates that my pages were assisted by Artificial Intelligence (AI) automation (for example, automatic completion of standard code), but no idea-generation or copy-pasting from a generative AI was used (there are other ratings to indicate as such).


#### Favicon

Files can be found under _0\_static_ > _images_ > _[favicon](https://github.com/stillprocrastinating/UDP5WA4CF-UN03_back_end_development/tree/main/0_static/images/favicon)_.

The favicon was generated from the [UCL social icon](https://imagestore.ucl.ac.uk/imagestore/pcache/10034/0e/l_icon_square_1080x1080px_e51db.jpg) (sourced from [UCL Brand Resources](https://imagestore.ucl.ac.uk/imagestore/start/ucl-new-templates?fc=browse&column=7)) using [RealFaviconGenerator](https://realfavicongenerator.net).


#### Icons

Files can be found under _0\_documents_ > _README_ > _images_ > _[icons](https://github.com/stillprocrastinating/UDP5WA4CF-UN03_back_end_development/tree/main/README/images/icons)_.

The test answer image SVGs were sourced from [Lucide](https://lucide.dev/).
- The edit image was [square-pen](https://lucide.dev/icons/square-pen).
- The delete image was [trash-2](https://lucide.dev/icons/trash-2).


### Fonts

- [UCL Sans](https://imagestore.ucl.ac.uk/imagestore/start/ucl-new-templates/UCL/UCL%20Fonts?fc=browse&column=7&listview=overview&view=preview&fileid=1&fuid=UCL%20Sans.zip)  
![UCLSans Aa font demonstration as an image](https://github.com/stillprocrastinating/UDP5WA4CF-UN03_back_end_development/blob/main/0_documents/README/images/fonts/UCLSans.png)

---

Raghav, thank you, I really appreciate you :)

[↑ Return to top](https://github.com/stillprocrastinating/UDP5WA4CF-UN03_back_end_development)


