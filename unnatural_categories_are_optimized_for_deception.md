## Unnatural Categories Are Optimized for Deception

**Followup to**: [Where to Draw the Boundaries?](https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries)

_There is an important difference between having a utility function defined over a statistical model's performance against specific real-world data (even if another mind with different values would be interested in different data), and having a utility function defined over features of the model itself._

_Arbitrariness in the map doesn't correspond to arbitrariness in the territory. Whatever criterion your brain is using to decide which word you want,_ is _your non-arbitrary reason ..._

So the one comes back to you and says:

> That seems wrong—why wouldn't I care about the utility of having a particular model? I agree that categories derive much of their usefulness from "carving reality at the joints"—that's _one_ very important kind of consequence of choosing to draw category boundaries in a particular way. But other consequences might matter too, if we have some _moral_ reason to _value_ drawing our categories a particular way.

> I don't see why I shouldn't be willing to trade off one unit of categorizational nonawkwardness for $X$ units of morality, even if trading off a million units of categorizational nonawkwardness for the same $X$ units of morality would be bad.

> [TODO: Palestine/Israel metaphor]

> I think of language, following Eliezer Yudkwosky's ["A Human's Guide to Words"](https://www.lesswrong.com/s/SGB7Y5WERh4skwtnb), as being a human-made project intended to help people understand each other. It draws on the structure of reality, but has many free variables, so that the structure of reality doesn't constrain it completely. This forces us to make decisions, and since these are not about factual states of the world—what the definition of a word _really_ is, in God's dictionary—we have nothing to make those decisions on except consequences.

... okay, I think I see the problem. I see how one might have gotten that out of "A Human's Guide to Words"—_if you skipped all the parts with math_. I am now prepared to explain _exactly_ what's wrong here [in _more detail_](https://www.lesswrong.com/posts/2TPph4EGZ6trEbtku/explainers-shoot-high-aim-low) than [my previous attempt](https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries): not just _that_ this position is not in harmony with the hidden Bayesian structure of language and cognition, but how the hidden Bayesian structure of language and cognition explains _why_ an intelligent system might find this particular mistake _tempting_ in the first place, and what breaks as a result.

Category "boundaries" are a useful _visual metaphor_ for helping explain the cognitive function of categorization. If you have the visualization but you _don't_ have the math, you might think you have the freedom to "redraw" the category "boundaries." Simple, compact boundaries might _tend_ to be more useful, but more complicated boundaries aren't _false_ and therefore aren't forbidden if you have some non-epistemic reason to prefer them ... right?

Only in the sense that _no_ hypothesis is "false"! Hypotheses make probabilistic predictions. As long as you [never assign a probability of _zero_](https://www.lesswrong.com/posts/QGkYCwyC7wTDyt3yT/0-and-1-are-not-probabilities) (which is a log-odds of negative infinity), nothing you believe can ever be _definitively_ [(infinitely)](https://www.lesswrong.com/posts/ooypcn7qFzsMcy53R/infinite-certainty) "falsified"—it "just" makes worse predictions than other hypotheses.

Because category "boundaries" are merely a _visualization_ for a probabilistic model that makes predictions about the real world, you _can't_ "redraw the boundaries" associated with a communication signal without messing with the model that generates them, which means messing with your predictions about the real world.

Might there be some non-epistemic reason for an agent to prefer a model that makes worse predictions? Sure! Correct maps are useful for steering reality into configurations ranked higher in your preference ordering—but causing a _different_ agent to have _incorrect_ maps might make them _mis_-navigate reality in a way that benefits you! We call this [_deception_](https://www.lesswrong.com/posts/fmA2GJwZzYtkrAKYJ/algorithms-of-deception).

In a closely related phenomenon, a poorly-designed agent might get confused and end up manipulating its _own_ beliefs: optimizing its map to _inaccurately_ portray a high-value territory, rather than optimizing the territory to be high-value using a map that reflects the territory—a kind of _self_-deception. We call this _wireheading_.

Intelligent systems with shared interests will design communication protocols to efficiently share information in accordance with the [_mathematical laws_](https://www.lesswrong.com/posts/eY45uCCX7DdwJ4Jha/no-one-can-exempt-you-from-rationality-s-laws) of probability and information theory. Systems that communicate in ways that _depart_ from these laws, do so in order to achieve non-shared interests (deception), possibly non-shared interests of subsystems _within_ an agent (wireheading).

-----

Let's walk through a simple example. [Imagine that you have a peculiar job in a peculiar factory](https://www.lesswrong.com/posts/4FcxgdvdQP45D6Skg/disguised-queries): specifically, you're a machine-learning engineer tasked with automating away the jobs of humans who sort objects from a mysterious conveyor belt.

Another engineer has already written a system that processes camera and sensor data about the objects into more convenient ["features"](https://en.wikipedia.org/wiki/Feature_(machine_learning)): color (measured on an eight-point blueness scale), shape (measured on an eight-point "eggness" scale), and vanadium content (a boolean Yes or No). Your task is to further process this information into a format suitable for giving commands to other systems—for example, the robot arm that will physically move the objects into appropriate bins.

The feature data consists of the blueness–eggness–vanadium-content joint distribution given by this 128-entry table:

![blueness–eggness–vanadium joint distribution](https://i.imgur.com/zR83zOq.png)

**Table 1.**

This seems like ... not the most useful representation? The data is all there, so _in principle_, you could code whatever you needed to do based off the full table, but it seems like it would be an unmaintainable mess: you'd sooner _resign_ than write a 128-case [switch statement](https://en.wikipedia.org/wiki/Switch_statement). Furthermore, when the system is deployed, you hope to typically be able to give the binning robot messages based on _only_ the color and shape observations, because the Sorting Scanner that the vanadium readings come from is expensive to run. You _could_ just do a Bayesian update on the entire joint distribution, of course, but it seems like it should be possible to be more efficient by exploiting regularities in the data, not entirely unlike how your colleague's system has _already_ made your job much simpler by giving you blueness and eggness feature scores rather than raw camera data. Eyeballing the table, you notice it seems to have a lot of redundancy: most of the probability-mass is concentrated in two regions where the blueness and eggness scores are either both high or both low—and vanadium is _only_ found when both blueness and eggness are high.

O tragedy O the stars! _If only_ there were _some more convenient and flexible way_ to represent this knowledge—some kind of deep structural insight to rescue you from this cruel predicament!

... alright, dear reader—I shouldn't patronize. [You already know how this story ends.](https://www.lesswrong.com/posts/gDWvLicHhcMfGmwaK/conditional-independence-and-naive-bayes) The distribution factorizes!

$$\sum_{\mathrm{category}} P(\mathrm{category}) \cdot P(\mathrm{blueness}|\mathrm{category}) \cdot P(\mathrm{eggness}|\mathrm{category}) \cdot P(\mathrm{vanadium}|\mathrm{category})$$

(The distribution in this made-up toy example factorizes _exactly_, but [in a messy real-world application](https://www.lesswrong.com/posts/Zvu6ZP47dMLHXMiG3/optimized-propaganda-with-bayesian-networks-comment-on), you might have a spectrum of approximate models to choose from.)

We can simplify our representation of our observations by using a [naïve Bayes model](https://en.wikipedia.org/wiki/Naive_Bayes_classifier), a "star-shaped" [Bayesian network](https://www.lesswrong.com/posts/hzuSDMx7pd2uxFc5w/causal-diagrams-and-causal-models) where a central "category" node is posited to underlie all of our observations: we believe that each object either "is a blegg" (and therefore contains vanadium and has high blueness and eggness scores) with probability 0.48, "is a rube" (and therefore has no vanadium and low blueness and eggness scores) with probability 0.48, or belongs to a catch-all "other"/error class with probability 0.04. (Maybe the camera is buggy sometimes, or maybe there are some other random objects mixed in with the rubes and bleggs?)

![factorized object distribution](https://i.imgur.com/zIaDccJ.png)

**Figure 1.**

Whereas the full joint distribution had 127 degrees of freedom (a table of $8 \cdot 8 \cdot 2 = 128$ separate probabilites, constrained to add up to 1), the naïve-Bayes representation only has 50 ($3 \cdot 1$ prior probabilities for the categories, plus $3 \cdot 8 = 24$, $3 \cdot 8 = 24$, and $3 \cdot 1 = 3$-entry _conditional_ probability tables for each of the features, with each table constrained to add up to 1). The advantage would be much larger for more complicated problems—the joint distribution table grows exponentially with more features, quickly becoming infeasible to _store and represent_, let alone _learn_.

It must be stressed that our "categories" here are a _specific mathematical model_ that makes _specific_ (probabilistic) predictions. Suppose we see a black-and-white photo of an egg-shaped object: specifically, one with an eggness score of 7. Given that observation of $\mathrm{eggness} = 7$, we can update our probabilities of category-membership.

$$P(\mathrm{category} = c | \mathrm{eggness} = 7) = \frac{P(\mathrm{eggness} = 7|\mathrm{\mathrm{category} = c})P(\mathrm{category} = c)}{\sum_{d \in \{\mathrm{blegg}, \mathrm{rube}, \mathrm{??} \} } P(\mathrm{eggness} = 7| \mathrm{category}=d)P(\mathrm{category} = d)}$$

We think the egg-shaped object is almost certainly a blegg (specifically, with probability 0.96), even if the black-and-white photo doesn't directly tell us how blue it is, _because_

$$P(\mathrm{category} = \mathrm{blegg} | \mathrm{eggness} = 7) = \frac{\frac{1}{4} \cdot \frac{12}{25}}{\frac{1}{4} \cdot \frac{12}{25} + 0 \cdot \frac{12}{25} + \frac{1}{8} \cdot \frac{1}{25}} = \frac{24}{25} = 0.96$$

We can then use our updated beliefs about category membership (0.96 blegg/0 rube/0.04 unknown, as contrasted to the 0.48/0.48/0.04 prior) to get our updated posterior distribution on the 0–7 blueness score (0.005/0.005/0.005/0.005/0.005/0.245/0.485/0.245—left as an excercise for the reader).

------

In addition to categories facilitating efficient probabilistic inference _within_ the system that you're currently programming, _labels_ for categories turn out to be useful for _communicating_ with other systems. Maybe there's a robot arm in the Sorting room that puts bleggs in a blegg bin, which gets taken to a room elsewhere in the factory where there's sophisticated vanadium ore-processing machinery that has to handle both bleggs and gretrahedrons.

Maybe the binning arm doesn't need to _know_ about the blueness and eggness scores: it can close its claws around rubes and bleggs alike, and you only need to program it to pick up an object from a certain spot on the conveyor belt and place it into the correct bin. But maybe the vanadium-ore-processing machine does need to do further information processing before it can operate on an object—maybe it needs to vary its drill speed in proportion to the density of a particular blegg's flexible outer material (which it can estimate based on how brightly the blegg glows in the dark), but it uses a different drilling pattern for gretrahedrons.

If you need to send commands to the binning arm and the ore-processing machine, it's a more efficient communication protocol to just be able to send the 28-byte JSON payload `{"object_category": "BLEGG"}` and let the other machines do their work using their _own_ models of bleggs, rather than having to send over the raw camera data plus the binary code of the Bayesian network and feature extractors that the classifier system initially used to identify bleggs.

The `{"object_category": "BLEGG"}` message is a useful _shorthand_ for "linking up" the models between different machines. Different machines might not use the _same_ model: the classifer system uses blueness and eggness scores to _identify_ bleggs, but the ore-processing machine, having been _told_ that an object is a blegg, can take its blueness and eggness for granted and only needs to reason about its luminescence and vanadium content.

But [this trick of using a signal to correlate the models between different machines](https://www.lesswrong.com/posts/4hLcbXaqudM9wSeor/philosophy-in-the-darkest-timeline-basics-of-the-evolution) only works _because_ and _insofar as_ both models are pointing to the same [cluster-structure](https://www.lesswrong.com/posts/WBw8dDkAWohFjWQSk/the-cluster-structure-of-thingspace) in reality. If the model in the classifier system doesn't meaningfully _match_ the model in the ore-processing system—if the classifier code sends the `BLEGG` message given a object with eggness score between 5 and 7, but the ore-processor, upon recieving the `BLEGG` message, positions its drills in the expectation of processing an object with an eggness score between 0 and 2—then the factory doesn't work.

This is also, at an abstract high level, how human natural language works—how it _has_ to work. There is an idea in my head. When I speak, my larynx creates pressure wave in the air. When the waves hit your eardrum and are decoded by your auditory cortex, that hopefully [triggers](https://www.lesswrong.com/posts/YF9HB6cWCJrDK5pBM/words-as-mental-paintbrush-handles) a similar idea in your head. You don't have direct access to the computations going on in my head, but your brain can _infer_ something about them from the noises I make, and that's what it means to speak and to listen in a reductionist universe.

I am not a cognitive scientist and I don't _know_ the details of _how_ language works in the brain. But I do know a _little_ information theory and probability theory—enough to glimpse a bit of how the laws of mathematics constain how language _has_ to work, to the extent that it works.






-----

As a human learning math, it's helpful to examine [multiple representations of the same mathematical object](https://en.wikipedia.org/wiki/Multiple_representations_(mathematics_education)). We've already seen our blueness–eggness–vanadium model represented as a table, and factorized into a graphical model. We've done also some algebraic calculations with it. But we can also visualize it: the set of camera observations that the model classifies as a blegg with probability $\ge 0.96$ can be thought of a area with a boundary in two-dimensional blueness–eggness space:

![](file:///home/zmd/Documents/Drafts/Category_War/bleggspace.png)

**Figure 2.**

If you were trying to _teach_ someone about the hidden Bayesian structure of language and cognition, but thought your audience was too stupid or lazy to understand the actual math, you might be tempted to skip the part about factorizing a joint distribution into a star-shaped Bayesian network and just talk about "drawing" "boundaries" in configuration space for human convenience, perhaps with a hokey metaphor about national borders. Then the audience might walk away with the idea that there's no reason not to replace the old _blegg_ concept and its boring compact boundary, with a new _blegg\*_ concept that has an exciting squiggly border.

Alaska isn't even _contiguous_ with the rest of the United States. If _that's_ okay, why can't the borders of bleggness be a little squiggly?

![](file:///home/zmd/Documents/Drafts/Category_War/blegg-star-space.png)

**Figure 3.**

Because the "national borders" metaphor is [just a metaphor](https://www.lesswrong.com/posts/C4EjbrvG3PvZzizZb/failure-by-analogy). It _immediately_ breaks down as soon as you try to do any calculations.

When we say that [the United States purchased Alaska from the Russian Empire](https://en.wikipedia.org/wiki/Alaska_Purchase), that _means_ that this-and-such physical area on the Earth's surface went from being the territory of the Russian government, to being territory of the United States government, where land being the "territory of" a "government" is a complicated idea that has something to do [Schelling points over who gives orders to policemen and soldiers in that area](https://www.lesswrong.com/posts/YMtZRGLbvdD4BGaqN/generalized-efficient-markets-in-political-power#Governance_as_Schelling_Point).

When you reprogram your machine-learning system to send an `{"object_category": "BLEGG"}` message when it sees an object with an eggness score of 2 and a blueness score of 1, then your vanadium-ore-processing machine wears down its drill bits trying to process a rube.

_Other than_ the fact that _some aspects_ of these situations can be usefully _visualized_ as changes to a two-dimensional diagram depicting an area with a boundary, what do these situations have to do with each other? They don't. Countries aren't Bayesian networks. They just aren't. Why would you expect to understand a machine-learning concept by telling a story about national borders?

------

[TODO Objection: but you can do Bayesian inference with the "gerrymandered" boundary! It still has a lot of mutual information with the data! Reply: but it increases the mean squared error of feature predictions.]

------

[TODO Objection: but I assign utility to doing it this way. Reply: where would that utility function come from?]
[TODO: decision-determined problems]

-----

[TODO Example: "safe" meat temperature. If we start out with a discrete distribution between 100F and 200F. If I tell you the temperature is between 165 and 200, I've cut down your uncertainty from lg(100)=6.643 to lg(35)=5.1292: 1.514 bits, because I cut down the number of possibilities by a factor of 2.85, and lg(2.85)=1.514. But if I told you the temperature was _either_ between 165 and 190, OR between 130 and 140, that's ALSO cutting it down to 35 possibilities, but it doesn't answer the question I want to know about, which is whether I'll get sick from eating. Objection: but isn't that "instrumental"? It "safe" depends on your values! Reply: no, it's a conditional prediction about bacteria and getting sick.]

----

[...]

_(Thanks to Jessica Taylor for discussion.)_
