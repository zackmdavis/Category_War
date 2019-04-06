"Where to Draw the Boundaries?"

**Followup to:** [Where to Draw the Boundary?](https://www.lesswrong.com/posts/d5NyJ2Lf6N22AD9PB/where-to-draw-the-boundary)

_Figuring where to cut reality in order to carve along the joints—figuring which things are similar to each other, which things are clustered together:_ this _is the problem worthy of a rationalist. It is what people_ should _be trying to do, when they set out in search of the floating essence of a word. Once upon a time it was thought that the word "fish" included dolphins ..._

The one comes to you and says:

> The list: `{salmon, guppies, sharks, dolphins, trout}` is just a list—you can't say that a list is _wrong_. You draw category boundaries in specific ways to capture tradeoffs you care about: sailors in the ancient world wanted a word to describe the swimming finned creatures that they observed in the sea, which included salmon, guppies, sharks—and dolphins. That grouping may not be the one favored by modern biologists, but an alternative categorization system is not an error, and borders are not objectively true or false. You're not standing in defense of truth if you insist on a word, brought explicitly into question, being used with some particular meaning. So my definition of _fish_ cannot possibly be 'wrong,' as you claim. I can define a word any way I want—in accordance with my values!

So, there is a legitimate complaint here. It's true that sailors may not benefit from

`{salmon, guppies, sharks, dolphins, trout}`

-----


> Questions about how to draw category boundaries may be best understood as questions about values or priorities rather than about the actual content of the actual world. Reality doesn't come with its joints pre-labeled. Everything we identify as a joint is only a joint because we care about it.

Everything we identify as a joint is a joint not "because we care about it", but because it _helps us think about_ the things we care about.

There is an _important difference_ between "not including mountains on a map because it's a political map that doesn't show any mountains" and "not including Mt. Everest on a geographic map, because my friends don't like Mt. Everest and would be upset if they saw it on my map."

There is an _important difference_ between "identifying this pill as not being 'poison' allows me to concentrate my probability-mass when [anticipating](https://www.lesswrong.com/posts/a7n8GdKiAZRX86T5A/making-beliefs-pay-rent-in-anticipated-experiences) what I'll observe after administering the pill to a human (even if [most possible minds](https://www.lesswrong.com/posts/tnWRXkcDi5Tw9rzXw/the-design-space-of-minds-in-general) have never seen a 'human' and would never waste cycles imagining administering the pill to one)" and "identifying this pill as not being 'poison', because if I did call it 'poison', then the manufacturer of the pill might sue me."

There is an _important difference_ between having a utility function defined over a statistical model's _performance_ against specific real-world data (even if another mind with different values would be interested in different data), and having a utility function defined over features of _the model itself_.


You _can't_ change the categories your mind _actually_ uses and still perform as well on prediction tasks, although you can change your [_verbally reported_](https://www.lesswrong.com/posts/NMoLJuDJEms7Ku9XS/guessing-the-teacher-s-password) categories, much as how one can verbally report "believing" in an [invisible, inaudiable, flour-permeable dragon](https://www.lesswrong.com/posts/CqyJzDZWvGhhFJ7dY/belief-in-belief) in one's garage without having any false anticipations-of-experience about the garage.

This may be easier to see with a simple _numerical_ example.

Suppose we have some entities that exist in the three-dimensional vector space ℝ³. There's one cluster of entities centered at [1, 2, 3], and we call those entities Foos, and there's another cluster of entities centered at [2, 4, 6], which we call Quuxes.

The one comes and says, "Well, I'm going redefine the meaning of 'Foo' such that it also includes the things near [2, 4, 6] as well as the Foos-with-respect-to-the-old-definition, and you can't say my new definition is wrong, because if I observe [2, \_, \_] (where the underscores represent yet-unobserved variables), I'm going to categorize that entity as a Foo but still predict that the unobserved variables are 4 and 6, _so there_."

But if the one were _actually using_ the new definition of Foo _internally_ and not just _saying the words_ "categorize it as a Foo", they _wouldn't_ predict 4 and 6! They'd predict 3 and 4.5, because those are the average values of a generic Foo-with-respect-to-the-new-definition in the 2nd and 3rd coordinates (because (2+4)/2 = 6/2 = 3 and (3+6)/2 = 9/2 = 4.5). (The already-observed 2 in the first coordinate isn't average, but by [conditional independence](https://www.lesswrong.com/posts/gDWvLicHhcMfGmwaK/conditional-independence-and-naive-bayes), that only affects our prediction of the other two variables _by means_ of its effect on our "prediction" of category-membership.) The cluster-structure knowledge that "entities for which x₁≈2, also tend to have x₂≈4 and x₃≈6" needs to be represented _somewhere_ in the one's mind _in order to get the right answer_. And given that that knowledge needs to be represented, it might also be useful to have a _word_ for "the things near [2, 4, 6]" in order to efficiently share that knowledge with others.

Certainly, there isn't going to be a _unique_ way to encode the knowledge into natural language: there's no rule of rationality that says the word/symbol "Foo" needs to represent "the stuff near [1, 2, 3]" rather than "both the stuff near [1, 2, 3] and also the stuff near [2, 4, 6]". But if speakers of particular language were _already_ using "Foo" to specifically talk about the stuff near [1, 2, 3], then you can't swap in a new definition of "Foo" without _changing the truth values_ of sentences involving the word "Foo." Or rather: sentences involving Foo-with-respect-to-the-old-definition [are _different_ propositions](https://www.lesswrong.com/posts/shoMpaoZypfkXv84Y/variable-question-fallacies) from sentences involving Foo-with-respect-to-the-new-definition, even if they get written down using the same symbols in the same order.

Certainly, this all becomes much more complicated as we move away from the simplest idealized examples. For example, if the points are more evenly distributed in configuration space rather than belonging to cleanly distinguishable clusters, then essentialist "X is a Y" cognitive algorithms perform less well, and we get [Sorities paradox](https://plato.stanford.edu/entries/sorites-paradox/) situations where the mapping of structure-in-the-world to human natural language is a lot messier. Or, as with the fish _vs._ _dagim_ example, it might not be clear which aspects of reality are most relevant. (Clusters can "split" or "collapse" depending on _which_ dimensions of configuration space you want to look at.) Or there might be social or psychological forces anchoring word usages on easily-distinguishable Schelling points, even at the cost of some statistical "fit."

We could go on listing more such complications. But the fundamental thing is this: _the map is not the territory_. Maybe sometimes we might _want_ something to belong to a category that it currently doesn't. For example, maybe I want to be a physicist. (I am not a physicist.) To _solve_ that kind of problem, we need to intervene on the territory, not the map! In the case of me wanting to be a physicist, [if for many years I practice the techniques](http://yudkowsky.net/rational/virtues/) and submit myself to strict constraints, it may be that I will glimpse the center and thereby have _become_ a physicist: I will have _moved_ my location within the [high-dimensional configuration space](https://www.lesswrong.com/posts/WBw8dDkAWohFjWQSk/the-cluster-structure-of-thingspace) of human psychology into the region of people we call "physicists" (while remaining in the same place in the subspace of dimensions that make me myself).

It might be that there are insurmountable obstacles to me becoming a physicist: maybe I'm not smart enough, or maybe I don't have any money for textbooks. That's really sad! But the only way to make things _less_ sad is to fix the problems _in the territory_: for example, by giving me money, or intelligence-enhancing gene therapy. 

Certainly, there's not going to be one Objective True Definition of who is and is not a "physicist" (What topics do you need to have mastered? Do you need to be employed as a professor, or is just having done a Ph.D. enough? _&c._), and you might want to use different criteria in different contexts depending on what you're trying to talk about at the time. But choosing a definition _because you feel bad for poor-and-stupid physics students_ may not actually be helping anyone!

-----

Faced with an arbitrary choice, you should make an arbitrary choice

color vision

if someone honestly believes that the choice between multiple category systems is arbitrary or somewhat-arbitrary, then they should accept the choice being made arbitrarily or somewhat-arbitraril

[appeal-to-arbitrariness conversation halter](https://www.lesswrong.com/posts/wqmmv6NraYv4Xoeyj/conversation-halters)

[knowing about philosophy-of-language can hurt people](https://www.lesswrong.com/posts/AdYdLP2sRqPMoe8fb/knowing-about-biases-can-hurt-people)

if your preferences are about the map rather than the territory, you could just lie

appeal to values is worse than appeal to dictionary

