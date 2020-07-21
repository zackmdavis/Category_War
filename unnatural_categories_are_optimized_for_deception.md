## Unnatural Categories Are Optimized for Deception

**Followup to**: [Where to Draw the Boundaries?](https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries)

_There is an important difference between having a utility function defined over a statistical model's performance against specific real-world data (even if another mind with different values would be interested in different data), and having a utility function defined over features of the model itself._

_Arbitrariness in the map doesn't correspond to arbitrariness in the territory. Whatever criterion your brain is using to decide which word you want,_ is _your non-arbitrary reason ..._

So the one comes back to you and says:

> That seems wrong—why wouldn't I care about the utility of having a particular model? I agree that categories derive much of their usefulness from "carving reality at the joints"—that's _one_ important kind of consequence of choosing to draw category boundaries in a particular way. [TODO: introduce "morality"]

> I don't see why I shouldn't be willing to trade off one unit of categorizational nonawkwardness for $X$ units of morality, even if trading off one million units of categorizational nonawkwardness for the same $X$ units of morality would be bad.

> [TODO: Palestine/Israel metaphor]

> I think of language, following Eliezer Yudkwosky's ["A Human's Guide to Words"](https://www.lesswrong.com/s/SGB7Y5WERh4skwtnb), as being a human-made project intended to help people understand each other. It draws on the structure of reality, but has many free variables, so that the structure of reality doesn't constrain it completely. This forces us to make decisions, and since these are not about factual states of the world—what the definition of a word _really_ is, in God's dictionary—we have nothing to make those decisions on except consequences.

Okay, I think I see the problem. I see how one might have gotten that out of "A Human's Guide to Words"—_if you skipped all the parts with math_. I am now prepared to explain _exactly_ what's wrong here in _more detail_ than [my previous attempt](https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries): not just _that_ this position is not in harmony with the hidden Bayesian structure of language and cognition, but how the hidden Bayesian structure of language and cognition explains _why_ an intelligent system might find this particular mistake _tempting_ in the first place.

Category "boundaries" are a useful _visual metaphor_ for helping explain the cognitive function of categorization. If you have the visualization but you _don't_ have the math, you might think you have the freedom to "redraw" the category "boundaries." Simple, compact boundaries might _tend_ to be more useful, but more complicated boundaries aren't _false_ and therefore aren't forbidden if you have some non-epistemic reason to prefer them ... right?

Only in the sense that _no_ hypothesis is "false"! Hypotheses make probabilistic predictions. As long as you [never assign a probability of _zero_](https://www.lesswrong.com/posts/QGkYCwyC7wTDyt3yT/0-and-1-are-not-probabilities) (which is a log-odds of negative infinity), nothing you believe can ever be _definitively_ [(infinitely)](https://www.lesswrong.com/posts/ooypcn7qFzsMcy53R/infinite-certainty) "falsified"—it "just" makes worse predictions than other hypotheses.

Category "boundaries" are a convenient _visualization_ for a probabilistic model that makes predictions about the real world. You _can't_ "redraw the boundaries" without messing with the model that generates them, which means messing with your predictions about the real world.

-----

Let's walk through a simple example. [Imagine that you have a peculiar job in a peculiar factory](https://www.lesswrong.com/posts/4FcxgdvdQP45D6Skg/disguised-queries): specifically, you're a machine-learning engineer tasked with automating away the jobs of humans who sort objects from a mysterious conveyor belt.

Another engineer has already written a system that processes camera and sensor data about the objects into more convenient ["features"](https://en.wikipedia.org/wiki/Feature_(machine_learning)): color (measured on an eight-point blueness scale), shape (measured on an eight-point "eggness" scale), and vanadium content (a boolean Yes or No). Your task is to further process this information into a format suitable for giving commands to other systems—for example, the robot arm that will physically move the objects into appropriate bins.

The feature data consists of the blueness–eggness–vanadium-content joint distribution given by this 128-entry table:

![blueness–eggness–vanadium joint distribution](https://i.imgur.com/zR83zOq.png)

This seems like ... not the most useful representation? The data is all there, so _in principle_, you could code whatever you needed to do based off this, but it seems like it would be an unmaintainable mess: you'd sooner _resign_ than write a 128-case [switch statement](https://en.wikipedia.org/wiki/Switch_statement). Furthermore, when the system is deployed, you hope to typically be able to give the binning robot commands based on _only_ the color and shape observations, because the Sorting Scanner that the vanadium readings come from is expensive to run. You _could_ just do a Bayesian update on the entire joint distribution, of course, but it seems like it should be possible to be more efficient by exploiting regularities in the data, not entirely unlike how your colleague's system has _already_ made your job much simpler by giving you blueness and eggness feature scores rather than raw camera data. Eyeballing the table, you notice it seems to have a lot of redundancy: most of the probability-mass is concentrated in two regions where the blueness and eggness scores are either both high, or both low, and vanadium is _only_ found with both blueness and eggness are high.

O tragedy O the stars! _If only_ there were _some more convenient and flexible way_ to represent this knowledge—some kind of deep structural insight to rescue you from this cruel predicament!

... alright, dear reader—I shouldn't patronize. [You already know how this story ends.](https://www.lesswrong.com/posts/gDWvLicHhcMfGmwaK/conditional-independence-and-naive-bayes) The distribution factorizes!

$$\sum_{\mathrm{category}} P(\mathrm{category}) \cdot P(\mathrm{blueness}|\mathrm{category}) \cdot P(\mathrm{eggness}|\mathrm{category}) \cdot P(\mathrm{vanadium}|\mathrm{category})$$

(The distribution in this made-up toy example factorizes _exactly_, but [in a messy real-world application, you might have a range of "reasonable" approximate models to choose from](https://www.lesswrong.com/posts/Zvu6ZP47dMLHXMiG3/optimized-propaganda-with-bayesian-networks-comment-on).)

We can simplify our representation of our observations by using a naïve Bayes model where a central "category" node is posited to underlie all of our observations: we believe that each object either "is a blegg" (and therefore contains vanadium and has high blueness and eggness scores) with probability 0.48, "is a rube" (and therefore has no vanadium and low blueness and eggness scores) with probability 0.48, or belongs to a catch-all "other"/error class with probability 0.04. (Maybe the camera is buggy sometimes, or maybe there are some other random objects mixed in with the rubes and bleggs?)

![factorized object distribution](https://i.imgur.com/zIaDccJ.png)

Whereas the full joint distribution had 127 degrees of freedom (a table of $8 \cdot 8 \cdot 2 = 128$ separate probabilites, constrained to add up to 1), the naïve-Bayes representation only has 50 ($3 \cdot 1$ prior probabilities for the categories, plus $3 \cdot 8 = 24$, $3 \cdot 8 = 24$, and $3 \cdot 1 = 3$-entry _conditional_ probability tables for each of the features, with each table constrained to add up to 1). (The advantage would be much larger for more complicated problems—the joint distribution grows exponentially with more features, quickly becoming infeasible to _store and represent_, let alone _learn_.)

In addition to these economies _within_ the system that you're currently programming, categories are also useful for _communicating_ with other systems. The robot arm that puts bleggs in the blegg bin doesn't necessarily need to _know_ about the blueness and eggness scores; you only need to program it to act appropriately when told that an object is a `BLEGG`.

But if another system _does_ need to do cognitive work concerning our sortable objects, category labels can be used as signals to link up the models between different systems. Suppose there's some delicate vanadium-ore processing machinery elsewhere in the factory that needs to handle both bleggs and gretrahedrons. You want to be able to send commands to that machine, telling it to process a `BLEGG` using its _own_ models, _without_ having to send over all the binary code of the Bayesian network and feature extractors that we used to identify the blegg. The ore-processor's models might be different from the three-feature models we used to identify bleggs in the Sorting room—maybe it needs to vary its drill speed in proportion to the density of a particular blegg's flexible outer material.

[another diagram about using a signal to link up different models]

[there are more facts about bleggs than just three]

is a _specific mathematical model_ that makes _specific_ (probabilistic) predictions. What it _means_ is that if we see a black-and-white photo of an egg-shaped object (specifically, one with an eggness score of 7)







[argument from common usage]

For this reason [it is written of the third virtue of lightness](https://yudkowsky.net/rational/virtues/): you _cannot_ make a true map of the category by drawing lines upon paper according to impulse; you must observe the joint distribution and draw lines on paper that correspond to what you see. If, seeing the category unclearly, you think that you can shift a line just a little to the right, just a little to the left, according to your caprice, this is just the same mistake.
