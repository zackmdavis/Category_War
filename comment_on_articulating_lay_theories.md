## Optimized Propaganda with Bayesian Networks: Comment on "Articulating Lay Theories Through Graphical Models"

Derek Powell, Kara Weisman, and Ellen M. Markman's ["Articulating Lay Theories Through Graphical Models: A Study of Beliefs Surrounding Vaccination Decisions"](http://www.derekmpowell.com/publication/lay-theories-cogsci) (a conference paper from [CogSci 2018](https://cognitivesciencesociety.org/past-conferences/)) represents an exciting advance in marketing research, showing how to use [Bayesian networks](https://www.lesswrong.com/posts/hzuSDMx7pd2uxFc5w/causal-diagrams-and-causal-models) to study why ordinary people have the beliefs they do, and how to intervene to make them be [less wrong](https://tvtropes.org/pmwiki/pmwiki.php/Main/TitleDrop).

The specific case our authors examine is that of childhood vaccination decisions: some parents don't give their babies the recommended vaccines, because they're afraid that vaccines cause autism. [(Not true.)](https://en.wikipedia.org/wiki/MMR_vaccine_and_autism) This is pretty bad—not only are those unvaccinated kids more likely to get sick themselves, but declining vaccination rates undermine the population's [herd immunity](https://en.wikipedia.org/wiki/Herd_immunity), leading to [new outbreaks of highly-contagious diseases like the measles](https://en.wikipedia.org/wiki/Measles_resurgence_in_the_United_States), which _used_ to be eradicated in the United States.

What's wrong with these parents, huh?! But that doesn't have to just be a rhetorical question—Powell _et al._ show how we can use statistics to make the rhetorical [hypophorical](https://en.wikipedia.org/wiki/Hypophora) and model _specifically_ what's wrong with these people! Realistically, people aren't going to just have a raw, "atomic" dislike of vaccination _for no reason_: parents who refuse to vaccinate their children probably do so _because_ they're (irrationally) more afraid of autism than they are of the measles. Nor are beliefs about vaccine effectiveness or side-effects _uncaused_, but instead depend on other beliefs.

To unravel the structure of the web of beliefs, our authors got [Amazon Mechanical Turk](https://en.wikipedia.org/wiki/Amazon_Mechanical_Turk) participants to take surveys about vaccination-related beliefs, rating statements like "Natural things are always better than synthetic alternatives" or "Parents should trust a doctor's advice even if it goes against their intuitions" on a 7-point [Likert-like scale](https://en.wikipedia.org/wiki/Likert_scale) from "Strongly Agree" to "Strongly Disagree".

Throwing some [off-the-shelf Bayes-net structure-learning software](https://www.bnlearn.com/) at a [training set](https://en.wikipedia.org/wiki/Training,_validation,_and_test_sets) from the survey data, plus some ancillary assumptions (more-general "theory" beliefs like "skepticism of medical authorities" can cause more-specific "claim" beliefs like "vaccines have harmful additives", but not _vice versa_) produces a range of models. This kind of learning is possible because not all possible causal relationships are consistent with the data: if $A$ and $B$ are independent of each other, but each depend on $C$ (and are _conditionally_ independent given the value of $C$), it's kind of hard to make sense of this except to posit that $A$ and $B$ are causes with the common effect $C$.

Simpler models with fewer arrows might sacrifice a little bit of predictive accuracy for the benefit of being more intelligible to humans. Powell _et al._ ended up choosing a model that can predict responses from the [test set](https://en.wikipedia.org/wiki/Cross-validation_(statistics)) at [_r_](https://en.wikipedia.org/wiki/Pearson_correlation_coefficient) = .825, explaining 68.1% of the variance. Not bad?!—check out the full 14-node graph in Figure 2 on page 4 of [the PDF](https://mindmodeling.org/cogsci2018/papers/0183/0183.pdf).

Causal graphs are useful as a guide for planning interventions. Our authors point out that since previous work showed that people's beliefs about vaccine dangers were difficult to influence, that suggests trying to intervene on the other parents of intent-to-vaccinate in the model: vaccine effectiveness and disease severity.

To make sure I really understand this, I want to adapt it into a simpler example with made-up numbers where I can do the arithmetic myself. Let me consider a simpler graph with just three nodes—

![vaccines are safe → vaccinate against measles ← measles are dangerous](https://i.imgur.com/NuYrnik.png)

Suppose this represents a [structural equation model](https://en.wikipedia.org/wiki/Structural_equation_modeling) where an anti-vaxxer-leaning parent-to-be's propensity-to-vaccinate-against-measles $C$ is expressed in terms of belief-in-vaccine-safety $A$ and belief-in-measles-badness $B$ as—

$$C = 0.7 \cdot A + 0.3 \cdot B $$

And suppose that you're trying to choose between two possible public education programs—one that would increase $A$ by 0.1, and another that would increase $B$ by 0.3.

You should choose the program that intervenes on $B$, because $(0.3)(0.3) = 0.9$ is bigger than $(0.7)(0.1) = 0.7$. That's actionable advice that we couldn't have derived without a quantitative model of how the audience thinks. Exciting!

At this point, some readers may be wondering why I've described this work as "marketing research" about constructing "optimized propaganda." A couple of those words usually have _negative_ connotations, but educating people about the importance of vaccines is a _positive_ thing. What gives?

I want to call "Learn the causal graph of why they think that and compute how to intervene on it to make them think something else" is a fully general persuasive technique that doesn't depend on whether the thing you're trying to convince them of is _true_.

In my simplified example, the choice to intervene on $B$ was based on the numbers showing that that was more effective at changing $C$ than intervening on $A$. But this is completely indifferent to what $A$, $B$, and $C$ _mean_. It would have worked just as well, and _for the same reasons_ if the graph had been—

[TODO: rephrase about B being easier-to-change]

![Coca-Cola isn't unhealthy → drink Coca-Cola ← Coca-Cola tastes great](https://i.imgur.com/lQmo66J.png)

https://www.lesswrong.com/posts/4ZvJab25tDebB8FGE/you-have-about-five-words  
http://benjaminrosshoffman.com/humility-argument-honesty/
beautiful weapons https://archive.is/LuQ66
https://www.lesswrong.com/posts/jnjjzkH8Fdzg4D6EK/causality-a-chapter-by-chapter-review

[^crux]

[^crux]: Thanks to [Anna Salamon](https://www.lesswrong.com/users/annasalamon) for this observation.


Said on graphs: https://www.lesswrong.com/posts/y4bkJTtG3s5d6v36k/stupidity-and-dishonesty-explain-each-other-away?commentId=zcBFbHL2azWBSa4kY

Imgur post: https://imgur.com/a/aTcjknM