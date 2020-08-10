## Unnatural Categories Are Optimized for Deception

**Followup to**: [Where to Draw the Boundaries?](https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries)

_There is an important difference between having a utility function defined over a statistical model's performance against specific real-world data (even if another mind with different values would be interested in different data), and having a utility function defined over features of the model itself._

_Arbitrariness in the map doesn't correspond to arbitrariness in the territory. Whatever criterion your brain is using to decide which word you want,_ is _your non-arbitrary reason ..._

So the one comes back to you and says:

> That seems wrong—why wouldn't I care about the utility of having a particular model? I agree that categories derive much of their usefulness from "carving reality at the joints"—that's _one_ very important kind of consequence of choosing to draw category boundaries in a particular way. But other consequences might matter too, if we have some _moral_ reason to _value_ drawing our categories a particular way. I don't see why I shouldn't be willing to trade off one unit of categorizational nonawkwardness for $X$ units of morality, even if trading off a million units of categorizational nonawkwardness for the same $X$ units of morality would be bad.

> [TODO: Palestine/Israel metaphor]

> I think of language, following Eliezer Yudkwosky's ["A Human's Guide to Words"](https://www.lesswrong.com/s/SGB7Y5WERh4skwtnb), as being a human-made project intended to help people understand each other. It draws on the structure of reality, but has many free variables, so that the structure of reality doesn't constrain it completely. This forces us to make decisions, and since these are not about factual states of the world—what the definition of a word _really_ is, in God's dictionary—we have nothing to make those decisions on except consequences.

... okay, I think I see the problem. I see how one might have gotten that out of "A Human's Guide to Words"—_if you skipped all the parts with math_. I am now prepared to explain _exactly_ what's wrong here [in _more detail_](https://www.lesswrong.com/posts/2TPph4EGZ6trEbtku/explainers-shoot-high-aim-low) than [my previous attempt](https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries): not just _that_ this position is not in harmony with the hidden Bayesian structure of language and cognition, but how the hidden Bayesian structure of language and cognition explains _why_ an intelligent system might find this particular mistake _tempting_ in the first place, and what breaks as a result.

Category "boundaries" are a useful _visual metaphor_ for helping explain the cognitive function of categorization. If you have the visualization but you _don't_ have the math, you might think you have the freedom to "redraw" the category "boundaries." Simple, compact boundaries might _tend_ to be more useful, but more complicated boundaries aren't _false_ and therefore aren't forbidden if you have some non-epistemic reason to prefer them ... right?

Only in the sense that _no_ hypothesis is "false"! Hypotheses make probabilistic predictions. As long as you [never assign a probability of _zero_](https://www.lesswrong.com/posts/QGkYCwyC7wTDyt3yT/0-and-1-are-not-probabilities) (which is a log-odds of negative infinity), nothing you believe can ever be _definitively_ [(infinitely)](https://www.lesswrong.com/posts/ooypcn7qFzsMcy53R/infinite-certainty) "falsified"—it "just" makes worse predictions than other hypotheses.

Because category "boundaries" are merely a _visualization_ for a probabilistic model that makes predictions about the real world, you _can't_ "redraw the boundaries" associated with a communication signal without messing with the model that generates them, which means messing with your predictions about the real world.

Might there be some non-epistemic reason for an agent to prefer a model that makes worse predictions? Sure! Correct maps are useful for steering reality into configurations ranked higher in your preference ordering—but causing a _different_ agent to have _incorrect_ maps might make them _mis_-navigate reality in a way that benefits you! We call this [_deception_](https://www.lesswrong.com/posts/fmA2GJwZzYtkrAKYJ/algorithms-of-deception).

In a closely related phenomenon, a poorly-designed agent might get confused and end up manipulating its _own_ beliefs: optimizing its map to _inaccurately_ portray a high-value territory, rather than optimizing the territory to be high-value by using a map that reflects the territory—a kind of _self_-deception. We call this _wireheading_.

Intelligent systems with shared interests will design communication protocols to efficiently encode information in accordance with the [_mathematical laws_](https://www.lesswrong.com/posts/eY45uCCX7DdwJ4Jha/no-one-can-exempt-you-from-rationality-s-laws) of probability and information theory. Systems that communicate in ways that deviate from efficient encodings, do so in order to achieve non-shared interests (via deception), possibly non-shared interests of subsystems _within_ an agent (wireheading).

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

In addition to categories facilitating efficient probabilistic inference _within_ the system that you're currently programming, _labels_ for categories turn out to be useful for _communicating_ with other systems. Maybe there's a robot arm in the Sorting room that puts bleggs in a blegg bin, which gets taken to a room elsewhere in the factory where there's sophisticated vanadium-ore-processing machinery that has to handle both bleggs and gretrahedrons.

Maybe the binning arm doesn't need to _know_ about the blueness and eggness scores: it can close its claws around rubes and bleggs alike, and you only need to program it to pick up an object from a certain spot on the conveyor belt and place it into the correct bin. But maybe the vanadium-ore-processing machine does need to do further information processing before it can operate on an object—maybe it needs to vary its drill speed in proportion to the density of a particular blegg's flexible outer material (which it can estimate based on how brightly the blegg glows in the dark), but it uses a different drilling pattern for gretrahedrons.

If you need to send commands to the binning arm and the ore-processing machine, it's a more efficient communication protocol to just be able to send the 28-byte JSON payload `{"object_category": "BLEGG"}` and let the other machines do their work using their _own_ models of bleggs, rather than having to send over the raw camera data plus the binary code of the Bayesian network and feature extractors that the feature-extraction and classifier systems initially used to identify bleggs.

The `{"object_category": "BLEGG"}` message is a useful _shorthand_ for "linking up" the models between different machines. Different machines might not use the _same_ model: the classifer system uses blueness and eggness scores to _identify_ bleggs, but the ore-processing machine, having been _told_ that an object is a blegg, can take its blueness and eggness for granted and only needs to reason about its luminescence and vanadium content.

But [this trick of using a signal to correlate the models between different machines](https://www.lesswrong.com/posts/4hLcbXaqudM9wSeor/philosophy-in-the-darkest-timeline-basics-of-the-evolution) only works _because_ and _insofar as_ both models are pointing to the same [cluster-structure](https://www.lesswrong.com/posts/WBw8dDkAWohFjWQSk/the-cluster-structure-of-thingspace) in reality. If the model in the classifier system doesn't meaningfully _match_ the model in the ore-processing system—if the classifier code sends the `BLEGG` message given a object with eggness score between 5 and 7, but the ore-processor, upon recieving the `BLEGG` message, positions its drills in the expectation of processing an object with an eggness score between 0 and 2—then the factory doesn't work.

This is also, at an abstract high level, how human natural language works—how it _has_ to work. There is an idea in my head. When I speak, my larynx creates pressure wave in the air. When the waves hit your eardrum and are decoded by your auditory cortex, that hopefully [triggers](https://www.lesswrong.com/posts/YF9HB6cWCJrDK5pBM/words-as-mental-paintbrush-handles) a similar idea in your head. You don't have direct access to the computations going on in my head, but your brain can _infer_ something about them from the noises I make, and that's what it means to speak and to listen in a reductionist universe.

I am not a cognitive scientist and I don't _know_ the details of _how_ language works in the brain. But I do know a _little_ information theory and probability theory—enough to glimpse a bit of how the laws of mathematics constain how language _has_ to work, to the extent that it works.

In studying or explaining the math, I like to focus on simple examples with explicit probability distributions that I can do my own calculations for with pencil or Python. If I want to tell a story to go along with the math, I want to make the story about factory machines that I could actually program.

The actual implementation of natural language in human brains is going to be _much_ more complicated, of course. Telling a story problem about computer programs controlling factory machines has the advantage not only of being a simple explanation of the [math](https://www.lesswrong.com/posts/bkSkRwo9SRYxJMiSY/beautiful-probability) that we can [trust](https://www.lesswrong.com/posts/BL9DuE2iTCkrnuYzx/trust-in-bayes) governs the more complicated real-world phenomenon. It's also less tempting to rationalize about the story problem about factory machines, than it is to directly think about language.

(As it is written of the tenth virtue of precision: even if you cannot do the math, knowing that the math exists tells you that the dance step is precise and has no room in it for your whims.)

Humans are designed to decieve each other—it's always tempting to speak in a way that propagates misinformation while retaining deniability that we weren't _lying_—it's the other guy's _fault_ for misinterpreting what I _really meant_. When we think about designing messages for computer programs to give commands to each other about quantifiable observables, this excuse vanishes: if there's a bug in deterministic computer code such that the robot arm puts an object in the rube bin when it gets the `BLEGG` message, then that's what happens. There's no room to use the complexity of humans and their political games to obscure the behavior of the physical system and how it's processing information.

[TODO: more cleanly distinguish two reasons for example choice: simplicity, and sidestepping political intuitions. Link to "Toolbox-thinking and law-thinking".]

-----

As a human learning math, it's helpful to examine [multiple representations of the same mathematical object](https://en.wikipedia.org/wiki/Multiple_representations_(mathematics_education)). We've already seen our blueness–eggness–vanadium model represented as a table, and factorized into a graphical model. We've done also some algebraic calculations with it. But we can also visualize it: the set of camera observations that the model classifies as a blegg with probability $\ge 0.96$ can be thought of a area with a boundary in two-dimensional blueness–eggness space:

![](file:///home/zmd/Documents/Drafts/Category_War/bleggspace.png)

**Figure 2.**

[TODO: highlight the significance of "with probability > p"—inside/outside the boundaries is a simplification that loses information if we're using a model where the classes generate overlapping observations in whatever subspace we're making observations in]

If you were trying to _teach_ someone about the hidden Bayesian structure of language and cognition, but thought your audience was too stupid or lazy to understand the actual math, you might be tempted to skip the part about factorizing a joint distribution into a star-shaped Bayesian network and just talk about "drawing" "boundaries" in configuration space for human convenience, perhaps with a hokey metaphor about national borders. Then the audience might walk away with the idea that there's no reason not to replace the old _blegg_ concept and its boring compact boundary, with a new _blegg\*_ concept that has an exciting squiggly border.

Alaska isn't even _contiguous_ with the rest of the United States. If _that's_ okay, why can't the borders of bleggness be a little squiggly?

![](file:///home/zmd/Documents/Drafts/Category_War/blegg-star-space.png)

**Figure 3.**

Because the "national borders" metaphor is [just a metaphor](https://www.lesswrong.com/posts/C4EjbrvG3PvZzizZb/failure-by-analogy). It _immediately_ breaks down as soon as you try to do any calculations.

When we say that [the United States purchased Alaska from the Russian Empire](https://en.wikipedia.org/wiki/Alaska_Purchase), that _means_ that this-and-such physical area on the Earth's surface went from being the territory of the Russian government, to being territory of the United States government, where land being the "territory of" a "government" is a complicated idea that has something to do [Schelling points over who gives orders to policemen and soldiers in that area](https://www.lesswrong.com/posts/YMtZRGLbvdD4BGaqN/generalized-efficient-markets-in-political-power#Governance_as_Schelling_Point).

When you reprogram your machine-learning system to send an `{"object_category": "BLEGG"}` message when it sees an object with an eggness score of 2 and a blueness score of 1, then your vanadium-ore-processing machine wears down its drill bits trying to process a rube.

_Other than_ the fact that _some aspects_ of both of these situations can be usefully _visualized_ as changes to a two-dimensional diagram depicting an area with a boundary, what do these situations have to do with each other? They don't. Countries aren't Bayesian networks. They just aren't. When we depict a country on a map, we're _not talking_ about a cognitive system that can use observations of latitude to estimate probabilities of country-membership and then use that distribution on country-membership to get an updated probability distribution on longitude. (I mean, given a world map, you _could_ program such a thing, but it seems kind of useless—it's not clear why anyone would _want_ that particular program.) Why would you expect to understand an AI-theory concept by telling a story about national borders?

------

So, that's what's wrong with the national-borders metaphor. But we haven't yet really explained the problem with "unnatural" categories—those that you would _visualize as_ a squiggly, "gerrymandered" boundary. The squiggly _blegg\*_ boundary doesn't have the nice property of corresponding to the category labels in our nice factorized naïve Bayes model, but it still contains information. You can still do a Bayesian update on being told that an object lies within a squiggly boundary in configuration space. If that update eliminates half of your probability-mass, that's one information-theoretic bit, no matter how the category is shaped in Thingspace.

If you only care about how much probability you assign to the _exact_ answer, then a bit is a bit. But if an approximate answer is approximately as good—if your answerspace has a metric on it, so that "approximate" can mean something—then some bits can be more valuable than others.

Suppose some random variable $X$ is uniformly distributed on the set $\{1, 2, 3, 4, 5, 6, 7, 8\}$. You have the option of being told whether an observation $x$ is even or odd, or whether $x$ is greater or less than 4.5. Either way, you eliminate half of your hypotheses: the entropy of your probability distribution goes from $log_2 8 = 3$ to $log_2 4 = 2$. You've learned 1 bit.

But if you learn whether $x$ is even or odd, your mean squared error only goes down from 10.5 to 10, whereas if you learn whether $x$ is 1–4 or 5–8, your mean squared error plummets to 2.5. [(The squared error has nicer mathematical properties than the absolute error.)]((https://www.benkuhn.net/squared/)) By being compact, the "1–4 or 5–8" category system is much more useful for getting _close_ to the right answer than the "even/odd" category system, even though they both provide the same amount of information about the _exact_ answer.

The same goes for natural categories _vs._ squiggly category "boundaries" in higher dimensions. For our blueness–eggness–vanadium distribution, your mean squared error before being told anything about an object is about 27.26 (with respect to Euclidean distance on blueness-score ✕ eggness-score ✕ 1-if-vanadium-present-else-0). On being told that an object is a blegg, your mean squared error plummets to about 0.46. On being told that an object is a blegg\*, your mean squared error only goes down to about 4.13.

In this sense, the gerrymandered blegg\* concept is _quantitatively less informative_ than the original, compact blegg concept. The _metric_ we assigned to blueness–eggness–vanadium space was our choice, and could depend on our values: if we simply _don't care_ about predicting how blue an object is, we could disregard the blueness score and only define a concept on the eggness–vanadium subspace. Or if we don't care about predicting blueness _very much_, we could calculate our error score with respect to a metric that gave blueness very little weight.

But _given_ a metric on the variables that you care about predicting and using to inform predictions, which categories are cognitively useful depends on the the distribution of data in the world (not on your values). You can't define a word any way you want.

[TODO: rewrite cleaner code and double-check and footnote-hyperlink calculations; quote how the squared error changes with different metrics]

------

The one replies: "You're still not addressing my crux! I don't doubt what you say about minimizing prediction error. But what if I don't care about that? My utility function assigns high value to using the squiggly _blegg\*_ category boundary—such that the utility of using my preferred category outweighs the disutility of making less accurate predictions. You _can_ define a word any way you want—if you're willing to pay the costs."

... so, what, you just intrinsically assign high utility to using the same communication signal to encode eggness-2/blueness-1 observations as eggness-6/blueness-6 observations, given the joint distribution specified in my story problem about sorting objects in a factory? Really?

"... yes!"

... okay, but where would that kind of exotic utility function come from? How would it arise naturally in an intelligent system?

There's a _trivial_ sense in which you can interpret any action taken by an agent as being taken because the agent _values taking that action_. This theory [is compatible with all possible behaviors and therefore explains nothing](https://www.lesswrong.com/posts/jiBFC7DcCrZjGmZnJ/conservation-of-expected-evidence).

The value of [decision-theoretic utility functions](https://www.lesswrong.com/posts/DQ4pyHoAKpYutXwSr/underappreciated-points-about-utility-functions-of-both) isn't that "Because utility!" serves as an all-purpose excuse for any possible behavior. It's that [simple coherence deciderata _imply_ that an agent's behavior should be _describable as_ maximizing expected utility for some utility function](https://www.lesswrong.com/posts/RQpNHSiWaXTvDxt6R/coherent-decisions-imply-consistent-utilities)—with corresponding _constraints_ on the shape of that behavior.

Situations like the [Allias paradox](https://www.lesswrong.com/posts/zJZvoiwydJ5zvzTHK/the-allais-paradox) illustrate what these constaints look like. Consider an AI faced with playing the following game. There's a switch that can be turned On or Off, that starts out on in the Off position.

At midnight, a coin is flipped. If the coin comes up Tails, the game ends. If the coin comes up Heads, then at a quarter past midnight, if the switch is Off, then the AI gets paid $100, and if the switch is On, a six-sided die is rolled, and the AI gets paid $110 if the die doesn't come up 6.

Suppose that, before midnight, the AI is willing to pay a dollar to flip the switch On (as if it thought that winning $110 with a probability of 5/12 is better than winning $100 with a probability of 1/2). Suppose the coin comes up Heads, and the AI is then willing to pay another dollar to flip the switch Off again (as if it thought that $100 with certainty is better than $110 with probability 5/6). Then the AI is two dollars poorer in exchange for the switch being in the same position it started in.

[TODO: sentence about violating the independence axiom]

Must we condemn such an AI as "irrational"? I mean, maybe not; it depends on what you mean by "rational". (If you speak overmuch of the Way, you will not attain it.) If, for some reason, you specifically programmed the AI to prefer options it considers "certain", or to want switches to be "On" before midnight but "Off" after midnight, then it would be functioning as designed.

What we _can_ say about such an AI, is that it's _not optimizing for acquiring money_.[^fully] (We say that a system is an optimizer if it systematically steers reality into configurations that rank higher with respect to some preference ordering. This helps us make predictions about what _effects_ the system has, without having to model the details of _how_ it brings those effects about.) A well-designed agent that was optimizing for acquiring money would be expected to obey the independence axiom.

[^fully]: At least, not _fully_ optimizing.

If the AI playing this game isn't coherently optimizing for acquiring money, what _is_ it optimizing for? To tell, we'd need to observe its behavior in different environments. If it is trying to acquire money but is just _biased_ to prefer certainty (in violation of the vNM axioms), then we'd expect it to make choices that result in money but continue to exhibit Allais-like glitches around gambles involving probabilities close to 1. If it just likes switches to be off after midnight, then we'd expect it to turn switches off at that time even if there's no gambling game going on.

This methodology for attributing goals to an agent—consider it to be "optimizing for" outcomes that it systematically achieves across a variety of environments—applies to the behavior of sending communication signals, just as it does to the behavior of flipping switches.

Back to the factory. Our classifier system that sends a `BLEGG` message when it gets camera data corresponding to the compact _blegg_ concept is optimized for sending messages that allow other systems to minimize the squared error of their predictions of objects with respect to our standard metric on blueness–eggness–vanadium space. We _don't_ intrinsically assign utility to using that particular category system; the category is the _solution_ to an optimization problem about how to efficiently get blueness–eggness–vanadium information from one place to another.

A system that sends a `BLEGG` message when it gets camera data corresponding to the gerrymandered _blegg\*_ concept would be optimized for ... what? If you don't instrinsically assign utility to using that particular category system, then _why_ would you program the system that way? What optimization problem is being solved?

Well. Suppose that, besides your dayjob as a machine-learning engineer, you _also_ happen to own a side interest in the firm that supplies rubes and bleggs to this very factory. And suppose that vanadium fetches higher market prices than palladium, such that the factory is to pay the supplier $2 per blegg but only $1 per rube—and that the accounts-payable records are to be compiled based on how much the classifier you're coding sends `BLEGG` and `RUBE` messages, not how much metal actually gets harvested.

You can't help but notice that you stand to make more money if the system you're programming sends `BLEGG` messages more often. You can't just make it send `BLEGG` all the time—someone would notice and you'd get fired. But the ore-processing room can cope with a _few_ suboptimally-sorted objects. Surely it's no big deal if you just ... adjusted the category boundary of `BLEGG`-ness a bit?

We saw earlier that the _blegg_ concept does better than the _blegg\*_ concept with respect to mean squared error (given a metric on the feature space).

That's not the only possible scoring function. Suppose instead we score our category system by which one best minimizes the squared error _minus_ [TODO: specify exact function after rewriting code] revenue to the supplier. [TODO: run the numbers;  rewrite cleaner code and double-check and footnote-hyperlink calculations]

So with respect to _that_ scoring function, the _blegg\*_ category "boundary" is preferable.

-----

The one says, "But now it sounds like you're agreeing with me! The compact _blegg_ category serves the factory owner's goals better, which you formalized in terms of minimizing average squared error. The squiggly _blegg\*_ boundary makes the factory perform less well, but it serves the moonlighting engineer's goals better, which you formalized in terms of minimizing squared error minus supplier revenue. There's no rule of rationality against the engineer using the _blegg\*_ category boundary if it suits their goals better."

Only in the same sense that there's no rule of rationality against _lying!_

Minimizing the squared error scoring function is _about_ map–territory correspondence: ways of communicating that help the factory machines make better predictions about the objects get a higher score.

Minimizing the squared-error-minus-revenue scoring function is a _compromise_ between map–territory correspondence and saying whatever makes the supplier the most money.

If we assume that the factory doesn't need to make any decisions based on the blueness or eggness scores of rubes or unclassified objects, then as far as the _inputs and outputs_ between the supplier and the various machines in the factory are concerned, there's _no difference_ between adopting the gerrymandered _blegg\*_ cateogry and keeping the old categories but just _lying_ that 3 rubes out of every 16[^lying-frequencies-rube] and 7 unclassified objects out of every 64[^lying-frequencies-unclassified] are bleggs!

[^lying-frequencies-rube]:

[^lying-frequencies-unclassified]: The 

Depending on your goals, deception can be rational! If you don't care about other agents having accurate models and just want them to believe whatever makes them behave in a way that benefits you, or whatever makes them happy, then you can do that! There's nothing physically stopping you! But in order to help you _decide_ whether decieving people is the right thing to do, it helps to _notice_ that what you're doing is decieving people!

And this Orwellian _mind game_ of redefining words in unnatural ways, confident that you'll be able to dodge any accusations of dishonesty with the excuse of, "Oh, but I'm not lying about the location of entities in configuration space—I can still tell you the blueness or eggness score of any individual object if you ask about that—I'm just chopping up the space into an alternate category system that better satisfies my goals, and reusing existing words for my new categories", is just a really sophisticated way of deceiving people without having to admit to yourself that you're deceiving people!

I'll admit, it's clever! You are very smart! And it's _true_ that words don't have intrinsic definitions! And it's _true_ that there are many ways to chop up configuration space into categories depending on your goals—you might want to run your clustering algorithm with respect to different subspaces or with different weights on the axes depending on exactly what variables you want your category to predict!

However! It's _also_ true that there are _mathematical laws_ describing the relationship between the categories you 


-----

[wireheading: explain wireheading via attractiveness]

-----

[mimickry: butterflies and meat. The thing that distinguishes mimickry from deception is that mimickry is actually seeking resemblance in the territory, not just the map. The boundary between mimickry and deception is actually somewhat fuzzy insofar as the map is part of the territory: changing the "title" coordinate does change the job. ]

-----

For these reasons [it is written of the third virtue of lightness](https://yudkowsky.net/rational/virtues/): you _cannot_ make a true map of the category by drawing lines upon paper according to impulse; you must observe the joint distribution and draw lines on paper that correspond to what you see. If, seeing the category unclearly, you think that you can shift a line just a little to the right, just a little to the left, according to your caprice, this is just the same mistake.

And as it is written of a virtue which is nameless: perhaps your conception of rationality is that it is rational to believe the words of the Great Teacher, who [lives in an area where claiming that the sky is blue would be political suicide](https://www.lesswrong.com/posts/DoPo4PDjgSySquHX8/heads-i-win-tails-never-heard-of-her-or-selective-reporting).

And the Great Teacher says, "Some people I usually respect for their willingness to publicly die on a hill of facts, now seem to be talking as if color references are necessarily a factual statement about frequencies of light. But using language in a way _you_ dislike, is not lying. You're not standing in defense of truth if you insist on a word, brought explicitly into question, being used with some particular meaning." And you look up at the sky and see blue.

If you think: "It may look like the sky is blue, such that I'd ordinarily think that someone who said 'The sky is green' was being deceptive. But surely the Great Teacher wouldn't egregiously mislead people about the philosophy of language when being egregiously misleading happens to be politically convenient," you lose a chance to discover your mistake.

How will you discover your mistake? Not by comparing your description to itself.

But by comparing it to that which you did not name.

_(Thanks to Jessica Taylor for discussion.)_
